# Install for Antigravity

Previously unverified in either direction. Resolved here directly against Google's own
[Antigravity skills codelab](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)
and cross-referenced against independent coverage: **Antigravity supports both the Skills format
and MCP**, but Skills need a placement step — it does not scan `.claude/skills/`.

## Skills

Antigravity scans two tiers:
- **Global**: `~/.gemini/config/skills/` — available across all Antigravity products.
- **Project**: `<project-root>/.agents/skills/` — available only within that project.

No explicit registration step beyond placement is documented — Antigravity uses semantic
triggering (matching your request against skill descriptions), not a name you invoke directly.

### Setup

1. Clone this repo, or copy `refract-suite/skills/` into your own robot-code repository at
   `.agents/skills/` (project-scoped — the more portable choice for a team repo than the global
   path).
2. Open the repo in Antigravity.

## MCP

Antigravity supports both local and remote MCP servers, with one-click installs for several
Google Cloud-integrated servers already built in. See [`mcp-clients.md`](mcp-clients.md) for
pointing it at Refract's server specifically — this path needs no `.agents/skills/` placement.

## Verify it's working

Ask something that should trigger a skill (see [`getting-started.md`](../getting-started.md)). If
you're using an Antigravity CLI variant specifically rather than the IDE, note some sources
describe a distinct global path (`~/.gemini/antigravity-cli/skills/`) for that variant — worth
checking your specific product's own settings if the standard path above doesn't pick up the
skills.
