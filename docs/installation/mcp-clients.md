# Install for any other MCP-speaking client

Every one of the 8 tools this project has specifically checked (Claude Code, VS Code/Copilot,
Copilot CLI, Cursor, Gemini CLI, OpenCode, Codex, Antigravity) works as a genuine MCP client — even
the ones whose Skills-format support needs a placement step (Gemini CLI, Codex, Antigravity) work
here with **no placement step at all**. This is a real, equally-valid path, not a fallback for
"unsupported" tools — a tool that can't auto-discover `SKILL.md` can still get full access to
Refract's grounded data through this route.

## What you get

`mcp-server/` exposes 4 tools — `rule_check`, `hardware_lookup`, `corpus_query`,
`validate_team_config` — as thin wrappers over the exact same deterministic scripts the skills
themselves call. See [`mcp-server.md`](../mcp-server.md) for the full tool reference with real
example calls and outputs.

## Setup

```bash
git clone https://github.com/N0v4ont0p/Refract.git
cd Refract
pip install -r mcp-server/requirements.txt
```

Point your MCP client at `python3 <path-to-repo>/mcp-server/server.py` as the server command —
every MCP client's config format differs slightly, but all of them accept a local command this
way. Per-tool config file locations, checked directly against each tool's own docs:

| Tool | Config file |
|---|---|
| VS Code | `.vscode/mcp.json` (workspace) or user profile config |
| Copilot CLI | `~/.copilot/mcp-config.json` or `.copilot/mcp-config.json` (repo-level) |
| Cursor | `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project) |
| Gemini CLI | `mcpServers` object in `settings.json` |
| OpenCode | `mcp` key in `opencode.json` |
| Codex | `~/.codex/config.toml` or project-scoped `.codex/config.toml` |
| Antigravity | Built-in MCP server management (local or remote) |

Example, in the `mcpServers`/`servers`-object shape most of these share:

```json
{
  "mcpServers": {
    "refract": {
      "command": "python3",
      "args": ["/absolute/path/to/Refract/mcp-server/server.py"]
    }
  }
}
```

(VS Code's own `mcp.json` uses the top-level key `servers` instead of `mcpServers` — otherwise the
same shape.)

## Verify it's working

```bash
python3 mcp-server/test_server.py
```

Runs each tool through the MCP-decorated function and compares the result byte-for-byte against
the same query run directly against the underlying skill script. If that passes, the server itself
is sound — a client-specific connection issue after that point is about your client's MCP config,
not the server.
