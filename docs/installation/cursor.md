# Install for Cursor

**Zero setup required — verified directly against Cursor's current docs**
([Skills](https://cursor.com/docs/context/skills)), and worth stating plainly because this is a
recent change: Cursor's own documentation now states "for compatibility, Cursor also loads skills
from Claude and Codex directories" — meaning `.claude/skills/` (and `~/.claude/skills/`) are
scanned directly, alongside Cursor's own `.cursor/skills/`/`.agents/skills/` paths. An earlier pass
through this same documentation found Cursor did **not** read `.claude/skills/` and needed a
separate placement step; that's no longer accurate as of this check, and the record has been
corrected rather than left stale.

## Setup

1. Clone this repo, or copy `refract-suite/skills/` into your own robot-code repository at
   `.claude/skills/`.
2. Open the repo in Cursor. No config file, no manifest edit.

## Verify it's working

Ask something that should trigger a skill (see [`getting-started.md`](../getting-started.md)). If
you're on an older Cursor version and nothing triggers, this compatibility path may not exist yet
in your version — updating Cursor is the first thing to try, since this is a documented but
relatively recent addition.

## The other path: MCP

Cursor supports MCP servers via `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project),
using the standard `mcpServers` object. Cursor caps active tools at roughly 40 across all
configured MCP servers combined — worth knowing if you're running several servers alongside
Refract's. See [`mcp-clients.md`](mcp-clients.md) for the setup.
