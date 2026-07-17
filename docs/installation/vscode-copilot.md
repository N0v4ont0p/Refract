# Install for VS Code (GitHub Copilot)

**Zero setup required.** Verified directly against VS Code's own documentation
([Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)): VS Code
scans `.claude/skills/` as one of its own default project-skill locations, alongside
`.github/skills/` and `.agents/skills/`.

## Setup

1. Clone this repo, or copy `refract-suite/skills/` into your own robot-code repository at
   `.claude/skills/` (matching the path VS Code already scans).
2. Open the repo in VS Code with the GitHub Copilot extension enabled. That's the whole setup —
   no config file, no manifest edit.

## Verify it's working

Open Copilot Chat and ask something that should trigger a skill (see
[`getting-started.md`](../getting-started.md) for examples). If a skill doesn't seem to trigger,
confirm the Copilot extension itself is current — this is a directly-scanned path, not an opt-in
feature, so an outdated extension version is the most likely cause of a miss.

## The other path: MCP

VS Code also fully supports MCP servers (`.vscode/mcp.json`, or **MCP: Open User Configuration**
for a user-level server). If you'd rather point VS Code at Refract's deterministic tools directly
instead of relying on skill-triggering, see [`mcp-clients.md`](mcp-clients.md).
