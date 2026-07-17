# Install for Gemini CLI

Verified directly against [Gemini CLI's own docs](https://geminicli.com/docs/cli/skills/) — two
things worth being precise about rather than rounding to "just works":

1. **Placement matters.** Gemini CLI scans `.gemini/skills/` (or the `.agents/skills/` alias) — not
   `.claude/skills/`. Refract's skills need to be placed or symlinked there.
2. **Whether a placed skill is enabled by default is genuinely unresolved — stated here honestly,
   not resolved into a clean single path.** Multiple direct checks of Gemini CLI's own
   documentation (the rendered docs site and the underlying GitHub source, checked independently)
   describe discovery as automatic ("Gemini CLI scans the discovery tiers... at the start of a
   session") but never explicitly state whether a skill placed in a standard location starts
   *enabled*, or requires an explicit `/skills enable` first. The docs do confirm
   `/skills enable`/`/skills disable`/`/skills link` exist as real commands — but not which side of
   that switch a fresh placement lands on. **This could not be confirmed from Gemini's own
   documentation**, across three separate attempts; it is reported as an open question, not guessed
   either way.

## Setup

1. Clone this repo, or copy `refract-suite/skills/` into `.gemini/skills/` in your own robot-code
   repository (or symlink `.agents/skills/` to the same content, since Gemini CLI treats that as an
   alias).
2. Open Gemini CLI in that repository and try asking something that should trigger a skill (see
   [`getting-started.md`](../getting-started.md)).

**If it doesn't trigger:** run `/skills enable` explicitly, then try again. This is the concrete
fallback for the ambiguity above, not a confirmed extra requirement — it may turn out to be
unnecessary once the underlying question is resolved, but it's the right first thing to try.

## Verify it's working

If a skill triggers after placement alone, that's itself a useful data point (suggests standard
locations are enabled by default). If it only triggers after `/skills enable`, that's the opposite
data point. Either way, reporting which one happened is worth doing — it's exactly what would
resolve the open question above.

## The other path: MCP

Gemini CLI supports MCP servers via the `mcpServers` object in `settings.json`, with environment
variable expansion and automatic sanitization of sensitive host environment variables when
spawning server processes. See [`mcp-clients.md`](mcp-clients.md) for the setup — this path has no
placement or enable-state ambiguity at all.
