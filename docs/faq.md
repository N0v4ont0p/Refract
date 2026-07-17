# FAQ

**Do I have to use Claude Code?**
No. Claude Code is the native path (a real plugin, install with two commands), but the skills
format is an open standard several other tools read directly — see
[`installation/`](installation/) for exactly which of the 8 checked tools need zero setup, which
need a placement step, and which need an explicit enable step. Any MCP-speaking client can also
reach Refract's deterministic tools directly through `mcp-server/`, regardless of Skills-format
support.

**Why does it ask so many questions the first time I request code?**
It shouldn't ask more than a handful, and only the ones that change what gets generated.
`ftc-team-config` runs a deterministic extractor over your repo first and only asks about what
code genuinely can't answer — see [`skills-guide.md`](skills-guide.md) for exactly how the
question list gets built and ordered. Once confirmed, it isn't asked again.

**What's the difference between `ftc-team-config` and `ftc-construct`?**
`ftc-team-config` establishes and confirms *what your robot is* — it never writes code.
`ftc-construct` writes the actual code, once a config is confirmed, and hands back to
`ftc-team-config` if it isn't. See [`skills-guide.md`](skills-guide.md).

**Does this work for seasons other than DECODE (2025-26)?**
The shipped data reflects DECODE specifically, but the architecture is built to carry forward — see
[`architecture.md`](architecture.md)'s note on the core-model/season-extension split. A season
transition replaces one file, not the whole system.

**Is my code or repo data sent anywhere?**
The skills read your repo locally (to infer config, to review existing code) and read Refract's own
bundled reference data (rule text, hardware catalogs, library docs) — both local operations. The
MCP server subprocess-calls local scripts; it doesn't call out to any external service on its own.
Whatever LLM you're using (Claude, or whichever model your MCP client is paired with) handles
requests the same way it does for any other task in that tool.

**A hardware spec or rule citation looks wrong. What do I do?**
Say so — every value is source-cited (a URL and a retrieval date for hardware/library specs, a
rule ID and tagged manual text for legality verdicts), so a wrong value is checkable and fixable
at the source, not something to just work around. This is exactly the kind of report this project
treats as a real finding, not noise.

**Why does a legality verdict sometimes say "I can't confirm this is current"?**
`ftc-rule-check` (and anything that calls its freshness gate) checks the corpus's stored Team
Update number against a live fetch of the manual page before answering. If that live check fails
(a network issue, or the live page not exposing a parseable marker), the verdict still comes back —
with that caveat attached, not silently dropped. See [`architecture.md`](architecture.md)'s section
on calibrated abstention for why this is deliberate rather than a bug.

**Can I see what data is bundled and where it came from?**
Yes — `refract-suite/ftc-shared-foundation/references/` holds the library docs (each file
source-cited with a fetch date), and `.claude/skills/ftc-hardware-lookup/references/catalogs/`
holds the hardware catalog (each value source-cited). Nothing in either is generated; both are
meant to be spot-checked against their own cited sources.
