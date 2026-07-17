# MCP server

`mcp-server/` exposes Refract's 4 deterministic capabilities as MCP tools, for any MCP-speaking
client — not just Claude Code. **It is a thin wrapper, not a reimplementation**: every tool
subprocess-calls the exact same scripts the skills themselves call (`rules.py`, `motor_math.py`,
`trajectory_solver.py`, `validate_config.py`, `check_freshness.py`) and returns their real output
verbatim, including abstentions, citations, and staleness flags. No grounding logic lives twice —
if a script's behavior changes, the MCP tool's behavior changes with it, automatically.

This isn't an aspiration — it's fidelity-tested (`mcp-server/test_server.py` compares each tool's
MCP-path output byte-for-byte against the same query run directly against the underlying script),
and every example below is real output from actually running each tool, not written from memory.

## Setup

```bash
pip install -r mcp-server/requirements.txt
python3 mcp-server/server.py          # speaks MCP over stdio
```

Point any MCP client at `python3 <repo>/mcp-server/server.py` as the command — see
[`installation/mcp-clients.md`](installation/mcp-clients.md) for per-tool config file locations.

## The 4 tools

### `rule_check(ids?, query?)`

Wraps `check_freshness.py` → `rules.py lookup` → `rules.py verify`. The freshness gate runs first
on every call — this is not a shortcut around `ftc-rule-check`'s own flow, it's the same flow.
`query` does a plain AND-substring keyword pre-filter over the rules corpus to find candidate IDs
if you don't already know one.

**Real call**: `rule_check(ids=["R207"])`

**Real output** (truncated):
```json
{
  "freshness": {
    "season": "decode-2025-26",
    "stored_incorporates_through": "Team Update 32",
    "status": "UNVERIFIABLE",
    "flag": true,
    "reason": "could not read a live Team Update number (no marker on page); treat corpus as possibly stale and say so in the answer"
  },
  "resolved_ids": ["R207"],
  "lookup": {
    "rules": [{
      "rule_id": "R207",
      "found": true,
      "short_title": "ROBOTS don’t use air",
      "text": "ROBOTS are restricted in their use of air in the following ways: A. ROBOTS may not use any closed air devices..."
    }]
  },
  "verify": { "missing": [], "all_valid": true }
}
```

Note the `freshness.flag: true` — a real network limitation surfaced honestly rather than silently
dropped. This is what "grounded" actually means in practice: the tool tells you when it can't
confirm currency, instead of answering as if it always can.

### `hardware_lookup(action, part?, driver?, driven?, ext?, wheel_mm?, distance?, height?, speed?, high_arc?)`

Wraps `motor_math.py` (`action`: `spec`/`external`/`wheel-speed`/`ticks`) or
`trajectory_solver.py` (`action="trajectory"`). Abstains — does not fabricate — on a part outside
the seeded catalog, exit code 3, same as calling the script directly.

**Real call**: `hardware_lookup(action="spec", part="5203-2402-0019")`

**Real output** (truncated):
```json
{
  "part": "5203-2402-0019",
  "name": "goBILDA 5203 Series Yellow Jacket Planetary Gear Motor, 19.2:1",
  "source": {
    "url": "https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-19-2-1-ratio-24mm-length-8mm-rex-shaft-312-rpm-3-3-5v-encoder/",
    "tier": 1,
    "retrieved": "2026-07-05"
  },
  "record": {
    "no_load_rpm_output": 312,
    "no_load_current_a": 0.25
  }
}
```

### `corpus_query(filter?)`

Globs and parses `ftc-corpus-builder/references/patterns/*.yaml`. Confidence and provenance
classification are returned exactly as stored — never inflated, never stripped.

**Real call**: `corpus_query(filter="shooter")`

**Real output** (as of this writing — the corpus grows over time, so re-run it rather than trust
this count): 21 matching patterns. First result:
```json
{
  "id": "12808-A-shooter-empirical-bilinear-fielded",
  "finding_ref": "shooter-empirical-vs-physics",
  "problem": "Produce flywheel-velocity / hood / turret setpoints for a variable-distance turreted shooter, including shoot-on-the-move, on a physics-capable team that also BUILT a full ballistics solver."
}
```

### `validate_team_config(config_path)`

Wraps `validate_config.py` — the exact `generation_allowed` gate `ftc-team-config` and
`ftc-construct` both check before doing anything.

**Real call**: `validate_team_config(".claude/skills/ftc-team-config/evals/fixtures/19859-real-confirmed.yaml")`

**Real output** (a genuinely confirmed config — team 19859's real, live-confirmed fixture):
```json
{
  "valid": true,
  "generation_allowed": true,
  "active_season": "decode-2025-26",
  "config_found": true,
  "errors": [],
  "warnings": [],
  "unconfirmed_mandatory": []
}
```

## Verify it yourself

```bash
python3 mcp-server/test_server.py
```

Compares all 4 tools' MCP-path output against the direct script path, byte-for-byte, including a
deliberately-unseeded part (confirms the abstention survives the MCP layer, not just the direct
script call).
