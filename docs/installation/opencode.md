# Install for OpenCode

**Zero setup required.** Verified directly against [OpenCode's own docs](https://opencode.ai/docs/skills/):
OpenCode scans `.claude/skills/<name>/SKILL.md` directly as one of its standard search locations
(alongside `.opencode/skills/` and `.agents/skills/`), walking up from the current working
directory to the git worktree root.

## Setup

1. Clone this repo, or copy `refract-suite/skills/` into your own robot-code repository at
   `.claude/skills/`.
2. Run `opencode` in that repository. No config file, no manifest edit.

## Verify it's working

Ask something that should trigger a skill (see [`getting-started.md`](../getting-started.md)).

## The safety hooks — a separate thing from skills

Refract's `PreToolUse` write-block hook (which stops an agent from accidentally writing into
reference-only directories) is a Claude Code-specific mechanism, not part of the Skills format
itself. Carrying it into OpenCode needs a separate community plugin
(`opencode-claude-hooks`), which reads an existing project's `.claude/settings.json` hooks —
including `permissionDecision: "deny"`, the exact mechanism Refract's hook uses. This requires one
manifest line in *your own* OpenCode global config
(`~/.config/opencode/opencode.json`: `"plugin": ["opencode-claude-hooks"]`) — not something this
repo can install for you, since it's a change to your own machine's config, not a repo file.
Skills themselves work without this; the hook bridge is a separate, optional step.

## The other path: MCP

OpenCode supports MCP servers via the `mcp` key in `opencode.json` (project-local, safe to check
into git — OpenCode looks for it walking up from the current directory to the nearest git root).
See [`mcp-clients.md`](mcp-clients.md) for the setup.
