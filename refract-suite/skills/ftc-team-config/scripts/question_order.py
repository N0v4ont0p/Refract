#!/usr/bin/env python3
"""Empirical elicitation ordering (REQ-47/REQ-48) — deterministic, no LLM.

Counts which feature-model axes the pattern corpus's `applicable_when` conditions actually branch
on. A feature many patterns key off has high information gain as a question; a feature nothing
branches on doesn't earn a question at all (§13). Output: ranked JSON on stdout.

The ranking is a SOFT ordering for the non-mandatory questions. The mandatory-ask set
(drivetrain topology, season mechanism set, software stack) always comes first regardless —
that's §13's explicit carve-out, not something this script decides.

Usage: question_order.py [--suite-root <path>]
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    print(json.dumps({"error": "pyyaml not installed"}))
    sys.exit(1)

TOKEN = re.compile(r"\b([a-z_]+\.[a-z_]+)\b")


def find_suite_root(start: Path) -> Path:
    # Plugin: $CLAUDE_PLUGIN_ROOT/ftc-shared-foundation (env or __file__-derived); else source-repo walk.
    import os
    cands = []
    pr = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if pr:
        cands.append(Path(pr) / "ftc-shared-foundation")
    cands.append(Path(__file__).resolve().parents[3] / "ftc-shared-foundation")
    for c in cands:
        if (c / "core-feature-model.yaml").exists():
            return c
    for p in [start, *start.parents]:
        if (p / "core-feature-model.yaml").exists():
            return p
    raise FileNotFoundError("core-feature-model.yaml not found (plugin or source layout)")


def main():
    args = sys.argv[1:]
    if "--suite-root" in args:
        suite = Path(args[args.index("--suite-root") + 1])
    else:
        suite = find_suite_root(Path(__file__).resolve())

    # Corpus patterns live in the shared foundation (plugin: <suite>/patterns/) or the source repo.
    patterns_dir = suite / "patterns"
    if not patterns_dir.exists():
        patterns_dir = suite / ".claude/skills/ftc-corpus-builder/references/patterns"
    core = yaml.safe_load((suite / "core-feature-model.yaml").read_text())
    core_axes = {k for k in core if not k.startswith("_")}
    # Season filter: a pattern scoped to another season can't justify a question this season, and a
    # mechanism token (e.g. DECODE's `shooter.requires`) the ACTIVE season doesn't declare isn't askable.
    active = (suite / "season-extensions" / "ACTIVE").read_text().strip()
    season = yaml.safe_load((suite / "season-extensions" / f"{active}.yaml").read_text()) or {}
    season_mechs = set((season.get("season_mechanisms") or {}).keys())
    other_season_mechs = set()
    for sf in (suite / "season-extensions").glob("*.yaml"):
        other_season_mechs |= set(((yaml.safe_load(sf.read_text()) or {}).get("season_mechanisms") or {}).keys())
    other_season_mechs -= season_mechs

    per_path, per_axis, total = Counter(), Counter(), 0
    skipped_other_season, dropped_tokens = Counter(), Counter()
    for f in sorted(patterns_dir.glob("*.yaml")):
        data = yaml.safe_load(f.read_text()) or {}
        for pat in data.get("patterns", []) or []:
            cond = str(pat.get("applicable_when", ""))
            if not cond or cond.startswith("n/a"):
                continue
            scope = pat.get("season_scope", "invariant")
            if scope not in ("invariant", active):
                skipped_other_season[scope] += 1
                continue
            total += 1
            for tok in set(TOKEN.findall(cond)):
                axis = tok.split(".")[0]
                if axis in other_season_mechs:
                    dropped_tokens[tok] += 1
                    continue
                per_path[tok] += 1
                # 'season' tokens are season-extension features, not core axes — kept but labeled
                per_axis[axis if axis in core_axes else f"season:{axis}"] += 1

    ranked = [
        {"feature": path, "patterns_branching_on_it": n}
        for path, n in per_path.most_common()
    ]
    print(json.dumps({
        "active_season": active,
        "patterns_with_conditions": total,
        "skipped_patterns_scoped_to_other_seasons": dict(skipped_other_season),
        "dropped_tokens_not_in_active_season": dict(dropped_tokens.most_common()),
        "ranked_features": ranked,
        "axis_totals": dict(per_axis.most_common()),
        "note": "soft ordering for NON-mandatory questions only; mandatory set asks first regardless",
    }, indent=2))


if __name__ == "__main__":
    main()
