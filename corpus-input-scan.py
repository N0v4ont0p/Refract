#!/usr/bin/env python3
"""Continuous corpus-input scanner (Phase C2). Detects candidate material for
the existing human-gated mining pipeline — NEVER writes into references/,
patterns/, or rules.json. Draft-only, always: prints a JSON report; a human
runs the existing Phase-4-style mining/tagging process against it, same as
every prior corpus addition.

Manual or externally cron/CI-triggered — no scheduling logic lives here.

Three checks, run independently or together:
  --team-repos    candidate new public FTC team repos (GitHub code search),
                  diffed against the already-mined team list (derived from
                  ftc-corpus-builder's own pattern files' meta.team fields)
  --libraries     release-feed check for the GitHub-hosted bundled libraries,
                  against the "Fetched: YYYY-MM-DD" header already stamped in
                  every library-docs file
  --rules         Team Update freshness — thin wrapper over check_freshness.py,
                  same script every other freshness check in this repo uses
  (no flag)       runs all three

Auth: reads GITHUB_TOKEN from the environment if set — same env-var discipline
already used elsewhere in this repo (CLAUDE_PLUGIN_ROOT), not a new credential
mechanism. Raises the GitHub API rate limit from 60/hr to 5000/hr; not
required at low scan volume, falls back to unauthenticated.

Usage:
  GITHUB_TOKEN=... python3 corpus-input-scan.py
  python3 corpus-input-scan.py --libraries
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# GitHub-hosted libraries only — REV Robotics (vendor docs), Limelight (vendor
# docs), and goBILDA build guides (product-page PDFs) have no GitHub release
# feed to check against; they're intentionally excluded here, not missed.
LIBRARY_REPOS = {
    "ftclib": "FTCLib/FTCLib",
    "roadrunner": "acmerobotics/road-runner",
    "easyopencv": "OpenFTC/EasyOpenCV",
    "ftc-dashboard": "acmerobotics/ftc-dashboard",
    "ftc-sdk": "FIRST-Tech-Challenge/FtcRobotController",
    "pedro-pathing": "Pedro-Pathing/PedroPathing",
}
# G5 (Phase G): commit-tracked, not release-tracked — TickTree is pre-alpha with only one release
# (v0.1.0) and its docs were deliberately fetched at HEAD, not that tag (see the doc headers'
# own note). Comparing against "latest release" here would be actively wrong, not just imprecise —
# it would report CURRENT against a stale tag while real commits pile up unfetched. Compares the
# commit hash embedded in each doc's own Source URL against the repo's live default-branch HEAD.
#
# ponytail: this is a correct fix for TickTree's CURRENT temporary state (docs and releases out of
# sync), not a standing architectural decision — don't let it calcify into permanent special-case
# logic. Revisit once TickTree's own release practice stabilizes, then move it back into the
# ordinary LIBRARY_REPOS release-based check above and DELETE this block plus its branch in
# scan_libraries() — do not keep a second, permanently-diverging code path.
#
# RE-CHECKED 2026-08-06 (I3): the condition is CLOSER but NOT met, so this stays. What changed:
# a new tag v0.1.1 now points at 998011a — the exact commit these docs were fetched at — where
# before, the only tag (v0.1.0, c1f6b13) predated the docs entirely. Tags and docs now move
# together, which was the stated condition. What is still missing: those are **tags only, not
# published GitHub releases** — `/repos/N0v4ont0p/Ticktree/releases/latest` returns 404 and the
# releases list is empty, so the release-based check would error out rather than work. Move it back
# when a real release exists, not merely a tag.
COMMIT_TRACKED_REPOS = {"ticktree": "N0v4ont0p/Ticktree"}
LIBRARY_DOCS_DIR = ROOT / "refract-suite/ftc-shared-foundation/references/library-docs"
PATTERNS_DIR = ROOT / ".claude/skills/ftc-corpus-builder/references/patterns"
FETCHED_RE = re.compile(r"Fetched:\s*(\d{4}-\d{2}-\d{2})")
COMMIT_RE = re.compile(r"/blob/([0-9a-f]{7,40})/")


def _gh_api(path, params=None):
    url = f"https://api.github.com{path}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                "User-Agent": "refract-corpus-input-scan"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode()), None
    except Exception as e:  # rate limit, network, 404 — report, don't crash the scan
        return None, f"{type(e).__name__}: {e}"


def already_mined_teams():
    teams = set()
    for f in PATTERNS_DIR.glob("*.yaml"):
        m = re.search(r"team:\s*[\"']?(\d+)", f.read_text())
        if m:
            teams.add(m.group(1))
    return teams


def scan_team_repos():
    known = already_mined_teams()
    data, err = _gh_api("/search/repositories", {
        "q": "topic:first-tech-challenge+topic:ftc-robotics+in:name",
        "sort": "updated", "per_page": "30",
    })
    if err:
        return {"status": "error", "detail": err, "note": "GitHub search API — check GITHUB_TOKEN / rate limit"}

    candidates = []
    for repo in data.get("items", []):
        m = re.search(r"\b(\d{3,6})\b", repo["name"])
        team_num = m.group(1) if m else None
        if team_num and team_num not in known:
            candidates.append({
                "team_guess": team_num, "repo": repo["full_name"], "url": repo["html_url"],
                "updated_at": repo["updated_at"], "stars": repo["stargazers_count"],
            })
    return {
        "status": "ok", "already_mined_teams": sorted(known),
        "candidate_count": len(candidates), "candidates": candidates,
        "note": "Candidate list only — heuristic name match, human review required before any mining pass, per Phase-4 discipline.",
    }


def scan_libraries():
    results = {}
    for lib, repo in LIBRARY_REPOS.items():
        lib_dir = LIBRARY_DOCS_DIR / lib
        if not lib_dir.exists():
            results[lib] = {"status": "skipped", "reason": "no local library-docs dir"}
            continue

        fetched_dates = []
        for f in lib_dir.rglob("*.md"):
            m = FETCHED_RE.search(f.read_text(errors="ignore")[:500])
            if m:
                fetched_dates.append(m.group(1))
        stored_fetch = max(fetched_dates) if fetched_dates else None

        release, err = _gh_api(f"/repos/{repo}/releases/latest")
        if err or release is None:
            results[lib] = {"status": "error", "detail": err, "repo": repo, "stored_fetch_date": stored_fetch}
            continue

        live_date = release["published_at"][:10]
        results[lib] = {
            "status": "STALE" if stored_fetch and live_date > stored_fetch else "CURRENT",
            "repo": repo, "stored_fetch_date": stored_fetch,
            "latest_release_tag": release["tag_name"], "latest_release_date": live_date,
        }

    for lib, repo in COMMIT_TRACKED_REPOS.items():
        lib_dir = LIBRARY_DOCS_DIR / lib
        if not lib_dir.exists():
            results[lib] = {"status": "skipped", "reason": "no local library-docs dir"}
            continue

        stored_commits = set()
        for f in lib_dir.rglob("*.md"):
            head = f.read_text(errors="ignore")[:500]
            m = COMMIT_RE.search(head)
            if m:
                stored_commits.add(m.group(1))

        head_commit, err = _gh_api(f"/repos/{repo}/commits/HEAD")
        if err or head_commit is None:
            results[lib] = {"status": "error", "detail": err, "repo": repo, "stored_commits": sorted(stored_commits)}
            continue

        live_sha = head_commit["sha"]
        results[lib] = {
            "status": "CURRENT" if any(live_sha.startswith(c) for c in stored_commits) else "STALE",
            "repo": repo, "tracking": "commit (pre-alpha, no meaningful release cadence — see G5)",
            "stored_commits": sorted(stored_commits), "live_head_commit": live_sha,
        }
    return results



# --- doc-set COMPLETENESS (distinct from staleness) -------------------------------------------
# Staleness asks "is what we stored out of date?". Completeness asks "is anything MISSING?" — a
# different question with a different failure mode: a corpus can be perfectly current and still
# have never fetched an entire section. Phase D2 found exactly that (the FTC SDK's whole
# apriltag/vision_portal tree was absent, not stale) and closed it by hand. This makes it a
# standing check so it never has to be a manual sweep again.
#
# spec: lib -> (kind, source, selector)
#   kind "repo"    — count doc files in the upstream git tree under `subdir` with `exts`
#   kind "sitemap" — count sitemap URLs matching `include` (and, for a sitemapindex, follow subs)
DOC_SOURCES = {
    "pedro-pathing": ("repo", "Pedro-Pathing/Docs", {"subdir": "content", "exts": (".mdx", ".md")}),
    "ftc-sdk":       ("repo", "FIRST-Tech-Challenge/ftcdocs", {"subdir": "docs/source", "exts": (".rst", ".md")}),
    "ftc-dashboard": ("repo", "acmerobotics/ftc-dashboard", {"subdir": "docs", "exts": (".md",)}),
    "easyopencv":    ("repo", "OpenFTC/EasyOpenCV", {"subdir": "", "exts": (".md",)}),
    "ftclib":        ("repo", "FTCLib/FTCLib-Docs", {"subdir": "", "exts": (".md",), "ref": "v2.1.0"}),
    "ticktree":      ("repo", "N0v4ont0p/Ticktree", {"subdir": "docs", "exts": (".md",)}),
    "limelight":     ("sitemap", "https://docs.limelightvision.io/sitemap.xml", {"include": "/docs/"}),
    "roadrunner":    ("sitemap", "https://rr.brott.dev/sitemap.xml", {"include": "/docs/v1-0/"}),
    "rev-robotics":  ("sitemap", "https://docs.revrobotics.com/sitemap.xml",
                      {"include_any": ("/duo-control/", "/duo-build/", "/ftc-kickoff-concepts/",
                                       "/rev-crossover-products/", "/rev-hardware-client/",
                                       "/rev-hardware-client-2/", "/software-resources/")}),
    # gobilda-build-guides has no enumerable index — product-page PDFs discovered per part.
    # Excluded deliberately, not missed; a completeness number there would be fiction.
}
_LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")


def _sitemap_urls(url, depth=0):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (refract-scan)"})
        xml = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    except Exception as e:
        raise RuntimeError(f"{type(e).__name__}: {e}")
    urls = _LOC_RE.findall(xml)
    if "<sitemapindex" in xml and depth < 2:
        out = []
        for sub in urls:
            try:
                out += _sitemap_urls(sub, depth + 1)
            except RuntimeError:
                pass
        return out
    return urls


def scan_doc_completeness():
    results = {}
    for lib, (kind, source, sel) in DOC_SOURCES.items():
        lib_dir = LIBRARY_DOCS_DIR / lib
        if not lib_dir.exists():
            results[lib] = {"status": "skipped", "reason": "no local library-docs dir"}
            continue
        stored = sum(1 for _ in lib_dir.rglob("*.md"))
        try:
            if kind == "repo":
                ref = sel.get("ref")
                if not ref:
                    meta, err = _gh_api(f"/repos/{source}")
                    if err or not meta:
                        raise RuntimeError(err or "no repo metadata")
                    ref = meta["default_branch"]
                tree, err = _gh_api(f"/repos/{source}/git/trees/{ref}", {"recursive": "1"})
                if err or not tree:
                    raise RuntimeError(err or "no tree")
                sub = sel["subdir"]
                paths = [t["path"] for t in tree.get("tree", []) if t["type"] == "blob"]
                if sub:
                    paths = [p for p in paths if p.startswith(sub + "/")]
                upstream = [p for p in paths if p.endswith(sel["exts"])
                            and not any(d in p.split("/") for d in
                                        (".github", "node_modules", "build", "_static", "_templates", "javadoc"))]
                detail = {"ref": ref, "truncated": bool(tree.get("truncated"))}
            else:
                urls = _sitemap_urls(source)
                if "include" in sel:
                    upstream = [u for u in set(urls) if sel["include"] in u]
                else:
                    upstream = [u for u in set(urls) if any(k in u for k in sel["include_any"])]
                detail = {"sitemap_total": len(set(urls))}
        except RuntimeError as e:
            results[lib] = {"status": "error", "detail": str(e), "source": source, "stored_files": stored}
            continue
        n = len(upstream)
        # stored can legitimately EXCEED upstream: curated syntheses live alongside the mirror
        # (see library-docs/_MIRROR-README.md). Only a shortfall is a gap.
        gap = max(0, n - stored)
        results[lib] = {
            "status": "COMPLETE" if gap == 0 else "GAP",
            "kind": kind, "source": source, "stored_files": stored,
            "upstream_docs": n, "missing_estimate": gap, **detail,
        }
    return results


def scan_rules():
    r = subprocess.run([sys.executable, str(ROOT / "scripts/check_freshness.py")],
                        capture_output=True, text=True, cwd=ROOT)
    try:
        return json.loads(r.stdout.strip())
    except json.JSONDecodeError:
        return {"status": "error", "stdout": r.stdout, "stderr": r.stderr}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--team-repos", action="store_true")
    ap.add_argument("--libraries", action="store_true")
    ap.add_argument("--rules", action="store_true")
    ap.add_argument("--completeness", action="store_true",
                    help="doc-set completeness (are pages MISSING) — distinct from staleness")
    args = ap.parse_args()
    run_all = not (args.team_repos or args.libraries or args.rules or args.completeness)

    report = {
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "github_token_present": bool(os.environ.get("GITHUB_TOKEN")),
    }
    if run_all or args.team_repos:
        report["team_repos"] = scan_team_repos()
    if run_all or args.libraries:
        report["libraries"] = scan_libraries()
    if run_all or args.completeness:
        report["doc_completeness"] = scan_doc_completeness()
    if run_all or args.rules:
        report["rules"] = scan_rules()

    print(json.dumps(report, indent=2))
    # Never writes anywhere. A human decides what, if anything, enters the mining pipeline.


if __name__ == "__main__":
    main()
