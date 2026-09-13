#!/usr/bin/env python3
"""Season-transition readiness gate (PLAN §19 step 6). Deterministic; no model in the loop.

  transition_check.py --season <slug>     JSON report, exit 0 only if ready_to_flip (or already live and healthy)

Every season-scoped artifact a flip of season-extensions/ACTIVE depends on is checked by path:
season yaml (source == plugin), rules corpus + manual tables (source == plugin, meta names the season),
live freshness, lint tokens cover every mechanism, every code_constraints rule ID exists in that
season's manual, per-season evals for each skill, at least one fixture stamped with the season.
The DRAFT/not_active flags are reported, not required: sign-off is a human act; this gate says
whether everything else is in place for it.
"""
import argparse, filecmp, json, os, re, sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
PLUGIN = ROOT / "refract-suite"
SKILLS = ["ftc-rule-check", "ftc-hardware-lookup", "ftc-team-config", "ftc-code-review"]


def same_tree(a, b):
    if not (a.is_dir() and b.is_dir()):
        return False
    c = filecmp.dircmp(a, b, ignore=[".impeccable", ".DS_Store"])
    if c.left_only or c.right_only or c.diff_files:
        return False
    if any(not filecmp.cmp(a / f, b / f, shallow=False) for f in c.common_files):
        return False
    return all(same_tree(a / d, b / d) for d in c.common_dirs)


def check(slug):
    res = {}

    def put(name, ok, detail=""):
        res[name] = {"ok": bool(ok), "detail": detail}

    sy, py = ROOT / "season-extensions" / f"{slug}.yaml", PLUGIN / "ftc-shared-foundation/season-extensions" / f"{slug}.yaml"
    season = yaml.safe_load(sy.read_text()) if sy.is_file() else None
    put("season_yaml", season is not None and py.is_file() and filecmp.cmp(sy, py, shallow=False),
        "source and plugin copies exist and are identical")
    season = season or {}
    put("game_name", bool(season.get("game_name")), season.get("game_name", "missing"))

    rules = ROOT / ".claude/skills/ftc-rule-check/references/rules" / slug
    rj = json.loads((rules / "rules.json").read_text()) if (rules / "rules.json").is_file() else None
    put("rules_corpus", rj is not None and rj["meta"].get("season") == slug
        and same_tree(rules, PLUGIN / "skills/ftc-rule-check/references/rules" / slug),
        f"{len(rj['rules']) if rj else 0} rules; meta.season matches; plugin copy identical")
    ids = {r["rule_id"] for r in rj["rules"]} if rj else set()
    if rj:
        dang = json.loads((rules / "dangling_citations.json").read_text())["dangling"]
        put("no_dangling_citations", not dang, f"{len(dang)} flagged for human review")
    tables = ROOT / ".claude/skills/ftc-hardware-lookup/references/manual-tables" / slug
    put("manual_tables", (tables / "INDEX.json").is_file()
        and same_tree(tables, PLUGIN / "skills/ftc-hardware-lookup/references/manual-tables" / slug), "per-season tables, plugin identical")

    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        import check_freshness
        fr = check_freshness.check(slug)
        put("freshness_current", fr["status"] == "CURRENT", f"{fr['status']}: {fr['reason']}")
    except Exception as e:  # network etc. — abstain, don't pass
        put("freshness_current", False, f"could not run: {e}")

    mechs = set((season.get("season_mechanisms") or {}).keys())
    toks = season.get("code_tokens") or {}
    put("code_tokens_cover_mechanisms", mechs and mechs <= set(toks), f"missing: {sorted(mechs - set(toks))}")
    cons = season.get("code_constraints") or []
    bad = []
    for c in cons:
        for rid in re.findall(r"\b[A-Z]\d{3}\b", str(c.get("rule", ""))):
            if rid not in ids:
                bad.append(f"{c.get('id')}: {rid}")
    put("code_constraints_rules_exist", bool(cons) and not bad, f"{len(cons)} constraints; unknown rule IDs: {bad}")

    missing_evals = [s for s in SKILLS if not (ROOT / ".claude/skills" / s / "evals" / f"{slug}.json").is_file()]
    put("per_season_evals", not missing_evals, f"missing: {missing_evals}")
    stamped = [str(p.relative_to(ROOT)) for p in (ROOT / ".claude/skills").glob("*/evals/fixtures/**/*.yaml")
               if f"season: {slug}" in p.read_text()]
    put("fixture_stamped", bool(stamped), f"{len(stamped)} fixture(s)")

    active = (ROOT / "season-extensions/ACTIVE").read_text().strip()
    pactive = (PLUGIN / "ftc-shared-foundation/season-extensions/ACTIVE").read_text().strip()
    put("active_pointers_agree", active == pactive, f"source={active} plugin={pactive}")
    meta = season.get("_meta") or {}
    live = not meta.get("not_active") and not str(meta.get("status", "")).upper().startswith("DRAFT")
    open_q = len(((season.get("deliberation_checkpoint") or {}).get("open_questions")) or [])

    blocking = [k for k, v in res.items() if not v["ok"]]
    return {"season": slug, "active": active, "season_marked_live": live,
            "open_deliberation_questions": open_q, "checks": res, "blocking": blocking,
            "ready_to_flip": not blocking,
            "next": ("flip: set _meta.status: live + not_active: false, write the slug into BOTH ACTIVE files, "
                     "re-run this gate and the fixture/eval regression" if not blocking and active != slug else
                     "healthy" if not blocking else "fix blocking checks first")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", required=True)
    a = ap.parse_args()
    r = check(a.season)
    print(json.dumps(r, indent=2))
    sys.exit(0 if r["ready_to_flip"] else 1)


if __name__ == "__main__":
    main()
