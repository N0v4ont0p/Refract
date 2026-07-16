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
LIBRARY_DOCS_DIR = ROOT / "refract-suite/ftc-shared-foundation/references/library-docs"
PATTERNS_DIR = ROOT / ".claude/skills/ftc-corpus-builder/references/patterns"
FETCHED_RE = re.compile(r"Fetched:\s*(\d{4}-\d{2}-\d{2})")


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
    args = ap.parse_args()
    run_all = not (args.team_repos or args.libraries or args.rules)

    report = {
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "github_token_present": bool(os.environ.get("GITHUB_TOKEN")),
    }
    if run_all or args.team_repos:
        report["team_repos"] = scan_team_repos()
    if run_all or args.libraries:
        report["libraries"] = scan_libraries()
    if run_all or args.rules:
        report["rules"] = scan_rules()

    print(json.dumps(report, indent=2))
    # Never writes anywhere. A human decides what, if anything, enters the mining pipeline.


if __name__ == "__main__":
    main()
