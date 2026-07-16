# Phase C1/C2 findings — cross-tool compatibility, MCP server, continuous input layer

Per ROADMAP.md's Phase C: reach as many of the eight named tools as possible without a bespoke
integration per tool, and build an active corpus-input layer that keeps the human-gated merge
discipline. This doc is the record Phase D's README rewrite pulls from later.

---

## Step 0 — MCP mechanics, verified before building

Did not build against assumed syntax. First WebFetch attempt against the python-sdk README
returned a class name (`MCPServer`) and version (`2.0.0b1`) that repeated identically across two
unrelated fetches — a hallucination pattern, not real page content — so it was discarded and
cross-checked independently via WebSearch against multiple unrelated sources (gofastmcp.com,
DataCamp, CircleCI, a direct search for the exact official import path). Confirmed:

- Package: `pip install mcp` (stable, currently 1.28.1; v2 is beta, not for production)
- Import: `from mcp.server.fastmcp import FastMCP`
- Tool definition: `@mcp.tool()` decorator, type hints → JSON schema, docstring → tool description
- Entry point: `mcp.run()` under `if __name__ == "__main__":`
- Python 3.10+ (repo runs 3.13.5)

Installed and smoke-tested (`FastMCP('smoke-test')` + a decorated `add` tool, called directly)
before writing anything real.

## Step 1 — MCP server built as a thin wrapper

`mcp-server/server.py`, four tools, each a `subprocess` call into the exact script the
corresponding skill already runs — see `mcp-server/README.md` for the full mapping. Nothing
re-derives grounding logic that already exists; `rule_check` runs `check_freshness.py` as an
actual first step (not skipped) before `rules.py lookup`/`verify`, matching the same parity
`ftc-construct` and `ftc-code-review` were brought to in Phase B — this server does not shortcut
around that gate either.

One genuinely new (not reimplemented) piece: `rule_check`'s optional `query` parameter does a thin
AND-substring keyword filter over `rules.json` to surface candidate rule IDs, since no existing
script does keyword search and an MCP client calling this tool standalone has no other way to
discover valid IDs. This is additive — it never bypasses freshness/lookup/verify, it only helps
find what to look up. `corpus_query`'s `filter` parameter is the same shape, and was explicitly
asked for in the phase spec ("search/retrieve patterns").

## Step 2 — Fidelity tested, not just "it runs"

`mcp-server/test_server.py`, one real query per tool, MCP path vs. direct skill-script path,
byte-compared:

| Tool | Test | Result |
|---|---|---|
| `rule_check` | `ids=["R207"]` (flywheel-shooter legality, same rule verified live in Phase B) | Cited text and verify result byte-match the direct `rules.py` call |
| `rule_check` | `query="flywheel scoring element"` | Resolved `R207` by keyword search — caught and fixed a real bug here: an OR-based first draft matched on FTC-manual boilerplate words ("scoring", "element" appear in dozens of unrelated rules); switched to AND semantics, re-verified |
| `hardware_lookup` | `action="spec", part="5203-2402-0019"` (seeded SKU) | Matches direct `motor_math.py spec` output exactly |
| `hardware_lookup` | `action="spec", part="5203-2402-0001"` (deliberately unseeded — same SKU Phase B's eval-3 used) | Abstains (`abstain: true`) through the MCP path too, not fabricated |
| `corpus_query` | `filter="shooter"` | 17 matching patterns, count matches a direct parse, `confidence`/`provenance` fields present on every result |
| `validate_team_config` | the confirmed `veteran-swerve-turret.yaml` fixture | `valid`/`generation_allowed`/`unconfirmed_mandatory` all match the direct `validate_config.py` call |

All 6 assertions pass (`python3 mcp-server/test_server.py`). Beyond the Python-function level, also
opened a real MCP client session over stdio (`mcp.client.stdio`) against the running server,
called `list_tools()` and confirmed all 4 tools are discoverable over the actual protocol, then
called `validate_team_config` through a real `CallToolRequest` and confirmed the response matches —
this is a genuine MCP server, not just four functions with the right decorator.

## Step 3 — Skills-format baseline, corrected after independent per-tool verification

**First pass was wrong to trust at face value — corrected here, not just caveated.** Fetching
agentskills.io alone and taking its client-showcase listing as "5 of 8 tools, zero bridge" was a
single source describing its own spec's adoption — exactly the kind of claim this project doesn't
ship without independent corroboration (Rule 7). Went back and fetched each of the 5 named tools'
*own* documentation directly. **The claim did not fully hold up**, and the corrected picture is more
useful precisely because it's more specific:

| Tool | Own docs say | Scans `.claude/skills/` directly? | Verified |
|---|---|---|---|
| **VS Code / GitHub Copilot** | "Project skills, stored in your repository `.github/skills/`, `.claude/skills/`, `.agents/skills/`" | **Yes** | Genuinely zero-action for Refract's current layout |
| **OpenCode** | "OpenCode searches these locations" — lists `.claude/skills/<name>/SKILL.md` explicitly | **Yes** | Genuinely zero-action for Refract's current layout |
| **Cursor** | "automatically discovers skills from skill directories" — but only `.agents/skills/`, `.cursor/skills/` (+ user-home variants); `.claude/skills/` is not one of them | No | Format-compatible, auto-discovering, but needs Refract's skills ALSO placed at `.agents/skills/` — a real (if small) placement action, not "zero" |
| **OpenAI Codex** | scans `.agents/skills/` "in every directory from your current working directory up to the repository root" — no mention of `.claude/skills/` | No | Same shape as Cursor: needs placement at `.agents/skills/` |
| **Gemini CLI** | scans `.gemini/skills/`/`.agents/skills/` alias, but *also* requires an explicit step — `/skills link <path>` then `/skills enable` — even for a correctly-placed folder | No | Least automatic of the five: placement AND an explicit enable step |

**The real finding, more useful than the original overstatement**: `.claude/skills/` is directly
recognized by exactly 2 of the 5 (VS Code/Copilot, OpenCode) — genuinely zero-action today.
**`.agents/skills/` is the emerging shared convention** the other 3 (Cursor, Codex, and Gemini CLI's
alias) actually converge on. A single additional step — publishing (or symlinking) Refract's skill
folders at `.agents/skills/` alongside the existing `.claude/skills/` — would cover 4 of 5 with no
code changes to any of those tools, leaving only Gemini CLI's explicit enable step as a genuinely
separate per-user action. **Not built this pass** (wasn't asked, and Step 4 below scoped the actual
"implement if cheap" check to OpenCode specifically) — flagged here as a concrete, low-cost
candidate for whoever does Phase C's fuller per-tool work, or as a Phase D README recommendation.

Antigravity: not found in agentskills.io's client showcase and not independently checked against
its own docs this pass — still genuinely unverified, not confirmed either way.

## Step 4 — OpenCode cheap win, checked, documented not implemented

Two separate things, confirmed separately (OpenCode's own docs directly fetched and quoted above,
not just the agentskills.io listing):

1. **Skills themselves**: OpenCode scans `.claude/skills/` directly (verified above) — the 5 FTC
   skills already work with zero bridge, zero config, zero action from this repo.
2. **Hooks (the PreToolUse write-block safety mechanism Phase B built)**: a real community plugin
   exists (`opencode-claude-hooks`) that discovers and runs an existing project's
   `.claude/settings.json` hooks under OpenCode, including `permissionDecision: "deny"` (the exact
   mechanism the corpus-sources/32008teamcode/19859crucialcodeauthentic write-block hook uses).
   **Not zero-config**: it requires one manifest line in the OpenCode *user's own* global config
   (`~/.config/opencode/opencode.json`, adding `"plugin": ["opencode-claude-hooks"]`) — a one-time
   step on the OpenCode side, not something this repo can install on someone else's machine or ship
   as a Refract-side file. Genuinely cheap, but there is no Refract-repo artifact to change here —
   the correct action is documenting it (this section, destined for the Phase D README) rather than
   building anything, which is what "implement only if cheap, defer if it needs real work" resolves
   to when the "implementation" is a note on someone else's config file, not code in this repo.

## Step 5 — Continuous input layer: built, real-scanned, closing Phase C's second goal

Per ROADMAP.md's C2: "active" must mean continuous *detection and drafting*, never continuous
*auto-merge* — the human-gated checkpoint is the single most load-bearing discipline in this
project (it caught 21813's matrix error, corrected the 24089 reframe, validated R58). Nothing here
changes that; `corpus-input-scan.py` only ever drafts, it never writes into `references/`,
`patterns/`, or `rules.json` — there is no write path in the script at all.

**Built at repo root**: `corpus-input-scan.py`, a script (not a service — this repo has no
persistent server and wasn't asked for one). Three checks, run independently (`--team-repos`,
`--libraries`, `--rules`) or together (no flag):

- **New public team repos**: GitHub repo-search API, diffed against the already-mined team list —
  derived by scanning `ftc-corpus-builder`'s own pattern files' `meta.team` fields (9 teams found:
  12808, 15083, 15993, 16093, 18742, 19043, 22105, 24089, 3543), not a hardcoded list that could
  drift from the actual corpus. Emits a candidate list, heuristic (repo-name digit match against a
  topic-scoped search) — human review required before anything is mined, same as every prior team.
- **Library releases**: checks the 6 bundled libraries that actually have a GitHub release feed
  (FTCLib, RoadRunner, EasyOpenCV, FTC Dashboard, the FTC SDK, Pedro Pathing) against the
  "Fetched: YYYY-MM-DD" header already stamped in every `library-docs/` file. **REV Robotics,
  Limelight, and goBILDA build guides are intentionally excluded** — they're vendor docs/PDFs with
  no GitHub release concept, not a missed check.
- **Team Updates**: thin subprocess wrapper over `check_freshness.py` — zero new logic, the exact
  same script every other freshness check in this repo already uses.

**Auth**: reads `GITHUB_TOKEN` from the environment if present (same env-var-read discipline as
`CLAUDE_PLUGIN_ROOT` elsewhere in this repo — no new credential mechanism), raising the GitHub API
limit from 60/hr to 5000/hr; not required at low scan volume, degrades to unauthenticated.

**Real-scanned, not just smoke-tested** — ran it live with `GITHUB_TOKEN=$(gh auth token)`:
- **A genuine finding, first run**: `ftc-sdk` came back `STALE` — the local docs were fetched
  2026-07-12; the FTC SDK's `v11.2` release published 2026-07-15, 3 days later. Real, current,
  unprompted evidence the mechanism works, not a synthetic test case.
- Caught and fixed a real bug in the process: the initial `Pedro-Pathing/Pedro` repo guess 404'd —
  verified the actual repo name (`Pedro-Pathing/PedroPathing`) via a **direct GitHub API call**
  (not another LLM-summarized fetch, after the earlier MCP-docs hallucination this pass already
  caught once), confirmed `v2.1.2` resolves, fixed the mapping, re-ran clean.
- `--team-repos` returned 0 candidates this run — the topic-scoped search query's real hit rate at
  scale is unproven; flagging honestly rather than claiming it's been stress-tested against a real
  influx of new repos.

**Trigger, deliberately not built**: manual (`python3 corpus-input-scan.py`) or your own external
cron/CI, per instruction — no scheduling infrastructure lives in this repo.
