# Refract MCP server

Exposes Refract's four deterministic capabilities — rule lookup, hardware lookup, corpus
query, config validation — as MCP tools, for any MCP-speaking client (not just Claude Code).

**This is a thin wrapper, not a reimplementation.** Every tool subprocess-calls the exact same
scripts the FTC skills themselves call (`rules.py`, `motor_math.py`, `trajectory_solver.py`,
`validate_config.py`, `check_freshness.py`) and returns their real output verbatim — including
abstentions, citations, and staleness flags. No grounding logic lives twice.

## Tools

| Tool | Wraps | Notes |
|---|---|---|
| `rule_check(ids?, query?)` | `check_freshness.py` → `rules.py lookup` → `rules.py verify` | Freshness gate runs first, every call — matches `ftc-rule-check`'s and `ftc-construct`'s own flow, not a shortcut around it. `query` does a simple AND-substring keyword pre-filter over `rules.json` to find candidate IDs (new, thin — no existing script does keyword search); pass `ids` directly if you already know them. |
| `hardware_lookup(action, part?, distance?, height?, speed?, ...)` | `motor_math.py` (spec/external/wheel-speed/ticks) or `trajectory_solver.py` (action="trajectory") | Abstains (does not fabricate) on an unseeded part, exit 3, same as the direct script. |
| `corpus_query(filter?)` | glob + parse `ftc-corpus-builder/references/patterns/*.yaml` | Confidence and provenance fields returned intact, never inflated or stripped. |
| `validate_team_config(config_path)` | `validate_config.py` | The exact `generation_allowed` gate `ftc-team-config` and `ftc-construct` both check before doing anything. |

## Install & run

```bash
pip install -r mcp-server/requirements.txt
python3 mcp-server/server.py          # speaks MCP over stdio
```

Point any MCP client at `python3 <repo>/mcp-server/server.py` as the command.

## Verify

```bash
python3 mcp-server/test_server.py
```

Runs each tool through the MCP-decorated function and compares the result byte-for-byte against
the same query run directly against the underlying skill script — confirms the MCP path never
silently drops a citation, an abstention, or a confidence/provenance field. All 4 tools also
verified over the real MCP stdio protocol (not just as plain Python calls) during development —
see `../PHASE-C1-C2-FINDINGS.md` at repo root.
