#!/usr/bin/env python3
"""Empirical elicitation ordering (R47/R48) — deterministic, no LLM.

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

    per_path, per_axis, total = Counter(), Counter(), 0
    for f in sorted(patterns_dir.glob("*.yaml")):
        data = yaml.safe_load(f.read_text()) or {}
        for pat in data.get("patterns", []) or []:
            cond = str(pat.get("applicable_when", ""))
            if not cond or cond.startswith("n/a"):
                continue
            total += 1
            for tok in set(TOKEN.findall(cond)):
                per_path[tok] += 1
                axis = tok.split(".")[0]
                # 'season' tokens are season-extension features, not core axes — kept but labeled
                per_axis[axis if axis in core_axes else f"season:{axis}"] += 1

    ranked = [
        {"feature": path, "patterns_branching_on_it": n}
        for path, n in per_path.most_common()
    ]
    print(json.dumps({
        "patterns_with_conditions": total,
        "ranked_features": ranked,
        "axis_totals": dict(per_axis.most_common()),
        "note": "soft ordering for NON-mandatory questions only; mandatory set asks first regardless",
    }, indent=2))


if __name__ == "__main__":
    main()
