# Install for GitHub Copilot CLI

**Not the same tool as the VS Code Copilot extension** — Copilot CLI is GitHub's separate,
standalone terminal tool, with its own skill-discovery mechanism. Verified directly against
[GitHub's own Copilot CLI docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills),
not assumed to inherit the VS Code extension's behavior: **zero setup required here too** — Copilot
CLI scans `.github/skills/`, `.claude/skills/`, or `.agents/skills/` for project skills, with no
configuration step.

## Setup

1. Clone this repo, or copy `refract-suite/skills/` into your own robot-code repository at
   `.claude/skills/`.
2. Run `copilot` in that repository. Skills are discovered at session start.

If you add a skill mid-session (rather than before starting), GitHub's docs note you can run
`/skills reload` to pick it up without restarting.

## Verify it's working

Ask something that should trigger a skill (see [`getting-started.md`](../getting-started.md)). If
nothing triggers, confirm you're actually running `copilot` (the CLI) in the repo root that
contains `.claude/skills/`, not a subdirectory.

## The other path: MCP

Copilot CLI also supports MCP servers directly — configuration lives in `~/.copilot/mcp-config.json`
(user-level) or `.copilot/mcp-config.json` (repository-level, shareable with a team), using a
standard `mcpServers` object. If you'd rather point Copilot CLI at Refract's deterministic tools
directly, see [`mcp-clients.md`](mcp-clients.md). Note Copilot CLI's config file uses the key
`mcpServers`; the VS Code extension's equivalent file uses `servers` — similar shape, not
identical, per GitHub's own docs.
