# Refract MCP server

Exposes Refract's four deterministic capabilities — rule lookup, hardware lookup, corpus query,
config validation — as MCP tools, for any MCP-speaking client (not just Claude Code). A thin
wrapper, not a reimplementation: every tool subprocess-calls the exact same scripts the FTC skills
themselves call and returns their real output verbatim.

Quick start:

```bash
pip install -r mcp-server/requirements.txt
python3 mcp-server/server.py          # speaks MCP over stdio
python3 mcp-server/test_server.py     # verify: MCP path vs. direct script path, byte-for-byte
```

Full docs — the tool reference, real example calls and output, per-client config —
live at [`../docs/mcp-server.md`](../docs/mcp-server.md) and
[`../docs/installation/mcp-clients.md`](../docs/installation/mcp-clients.md).
