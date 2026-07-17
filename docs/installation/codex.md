# Install for OpenAI Codex

Verified directly against [Codex's own skills docs](https://learn.chatgpt.com/docs/build-skills):
Codex scans `.agents/skills/` — walking up from the current working directory, through parent
folders in a git repository, to the repository root, plus `$HOME/.agents/skills` and an
admin-scoped `/etc/codex/skills`. **It does not scan `.claude/skills/`** — confirmed explicitly,
not assumed from a sibling tool's behavior. A placement step is required.

## Setup

1. Clone this repo, or copy `refract-suite/skills/` into your own robot-code repository at
   `.agents/skills/` (a plain copy, or a symlink to `.claude/skills/` if you're also using a tool
   that reads that path, so you don't maintain two copies).
2. Run Codex in that repository. Detection is automatic — Codex's own docs note "Codex detects
   skill changes automatically. If an update doesn't appear, restart Codex."

## Verify it's working

Ask something that should trigger a skill (see [`getting-started.md`](../getting-started.md)). If
a skill was disabled via `~/.codex/config.toml`'s `[[skills.config]]` entries, re-enabling it needs
a Codex restart per the same docs.

## The other path: MCP

Codex supports MCP servers via `config.toml` — `~/.codex/config.toml` (user-level) or a
project-scoped `.codex/config.toml` (trusted projects only), sharing configuration with the
ChatGPT desktop app and the IDE extension. See [`mcp-clients.md`](mcp-clients.md) for the setup —
this path needs no `.agents/skills/` placement at all.
