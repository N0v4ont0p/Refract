#!/usr/bin/env python3
"""Refract MCP server — thin wrapper over the same deterministic scripts every
FTC skill already calls (rules.py, motor_math.py, trajectory_solver.py,
validate_config.py, check_freshness.py). No logic is reimplemented: every tool
subprocess-calls the real script and returns its real output verbatim,
including abstentions and freshness flags, so any MCP client gets the same
grounding a Claude Code skill invocation gets."""
import json
import subprocess
import sys
from pathlib import Path

import yaml
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent.parent
mcp = FastMCP("refract")


def _run(*args):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=ROOT)
    out = r.stdout.strip()
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return {"stdout": out, "stderr": r.stderr.strip(), "exit_code": r.returncode}


@mcp.tool()
def rule_check(ids: list[str] | None = None, query: str | None = None) -> dict:
    """FTC rules legality check, grounded in the tagged Competition Manual — runs
    the same flow ftc-rule-check itself runs: freshness gate first, then rule
    lookup with one-hop cross-references, then citation verification. Pass known
    rule IDs (e.g. ["R207"]) or a plain-language `query` (e.g. "pneumatic
    flywheel") to find candidate IDs first. Never a verdict from memory — this
    always resolves through the real, current corpus."""
    rules_script = str(ROOT / ".claude/skills/ftc-rule-check/scripts/rules.py")
    freshness = _run(str(ROOT / "scripts/check_freshness.py"))

    resolved_ids = list(ids) if ids else []
    if not resolved_ids and query:
        corpus = json.loads((ROOT / ".claude/skills/ftc-rule-check/references/rules/rules.json").read_text())
        terms = query.lower().split()
        for r in corpus["rules"]:
            hay = (r["short_title"] + " " + r["text"]).lower()
            if all(t in hay for t in terms):
                resolved_ids.append(r["rule_id"])
        resolved_ids = resolved_ids[:5]

    if not resolved_ids:
        return {"freshness": freshness, "error": "no rule IDs given or found for query", "query": query}

    return {
        "freshness": freshness,
        "resolved_ids": resolved_ids,
        "lookup": _run(rules_script, "lookup", *resolved_ids),
        "verify": _run(rules_script, "verify", *resolved_ids),
    }


@mcp.tool()
def hardware_lookup(
    action: str, part: str | None = None,
    driver: int | None = None, driven: int | None = None,
    ext: float | None = None, wheel_mm: float | None = None,
    distance: float | None = None, height: float | None = None, speed: float | None = None,
    high_arc: bool = False,
) -> dict:
    """FTC hardware specs and deterministic math — same scripts
    ftc-hardware-lookup itself calls, never a value from memory. action:
    "spec"/"external"/"wheel-speed"/"ticks" (needs `part`, a catalog SKU) or
    "trajectory" (needs distance/height/speed — the DECODE launch-angle
    solver). Abstains rather than fabricates if a part isn't in the seeded
    catalog — surface that abstention, don't fill the gap."""
    if action == "trajectory":
        args = [str(ROOT / ".claude/skills/ftc-hardware-lookup/scripts/trajectory_solver.py")]
        if distance is not None:
            args += ["-d", str(distance)]
        if height is not None:
            args += ["-t", str(height)]
        if speed is not None:
            args += ["-v", str(speed)]
        if high_arc:
            args += ["--high-arc"]
        return _run(*args)

    args = [str(ROOT / ".claude/skills/ftc-hardware-lookup/scripts/motor_math.py"), action, part]
    if driver is not None:
        args += ["--driver", str(driver)]
    if driven is not None:
        args += ["--driven", str(driven)]
    if ext is not None:
        args += ["--ext", str(ext)]
    if wheel_mm is not None:
        args += ["--wheel-mm", str(wheel_mm)]
    return _run(*args)


@mcp.tool()
def corpus_query(filter: str | None = None) -> dict:
    """Search the elite-team FTC pattern corpus. Returns each matching pattern
    with its confidence and provenance classification intact and unaltered —
    never inflate a single-source pattern's confidence, never strip its
    caveats; display faithfully, same discipline ftc-code-review's own
    pattern-citation step enforces. Optional `filter` substring-matches
    against id, problem, solution_approach, and applicable_when."""
    results = []
    for f in sorted((ROOT / ".claude/skills/ftc-corpus-builder/references/patterns").glob("*.yaml")):
        doc = yaml.safe_load(f.read_text())
        for p in doc.get("patterns", []):
            hay = " ".join(str(p.get(k, "")) for k in ("id", "problem", "solution_approach", "applicable_when")).lower()
            if filter and filter.lower() not in hay:
                continue
            results.append(p)
    return {"count": len(results), "patterns": results}


@mcp.tool()
def validate_team_config(config_path: str) -> dict:
    """Validate a team's config.yaml against the confirmed-before-generate
    gate — the exact script ftc-team-config and ftc-construct both call before
    anything is elicited or generated. Returns generation_allowed and, if
    false, the unconfirmed_mandatory field list."""
    return _run(str(ROOT / ".claude/skills/ftc-team-config/scripts/validate_config.py"), config_path)


if __name__ == "__main__":
    mcp.run()
