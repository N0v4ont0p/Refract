# Troubleshooting

## A skill doesn't seem to trigger at all

1. **Confirm the skill files are actually where your tool scans.** Per-tool paths differ —
   see [`installation/`](installation/) for the exact one your tool needs. A tool that needs
   `.agents/skills/` (Codex, Antigravity, Gemini CLI) will find nothing if the files only exist at
   `.claude/skills/`.
2. **Confirm your tool's version is current.** Several of the zero-config paths documented here
   (Cursor's `.claude/skills/` compatibility, in particular) are relatively recent additions — an
   older client version may predate them.
3. **Try asking more directly.** A skill triggers off its own `description` matching what you
   asked — "write a teleop for our shooter" should route to `ftc-team-config`/`ftc-construct`
   clearly; a vaguer request may not.

## `ftc-team-config` keeps re-asking something I already confirmed

This shouldn't happen — confirmed fields are meant to stay settled. If it does, check
`team-config.yaml` at your project root: the field should show `confirmed: true`. If it shows
`confirmed: false` or is missing, something reset it (a manual edit, a fresh elicitation run
against the wrong path) rather than the skill re-deciding to re-ask on its own.

## `ftc-construct` won't generate anything

By design, if `generation_allowed` isn't `true` on your `team-config.yaml`, `ftc-construct` hands
back to `ftc-team-config` instead of guessing. Run
`python3 .claude/skills/ftc-team-config/scripts/validate_config.py <path-to-team-config.yaml>` —
the `unconfirmed_mandatory` list in the output names exactly what's still open.

## A rule verdict came back "ambiguous" or flagged `UNVERIFIABLE`

Both are real, valid outcomes, not something broken. `UNVERIFIABLE` means the live freshness check
couldn't confirm the corpus is current against the live manual (see
[`faq.md`](faq.md)) — the verdict itself still stands, with that caveat attached. `ambiguous` means
the retrieved rule text genuinely doesn't resolve the question either way — that's the system
declining to invent a confident answer it can't support, per
[`architecture.md`](architecture.md)'s note on calibrated abstention.

## The MCP server won't connect

1. Confirm dependencies installed: `pip install -r mcp-server/requirements.txt`.
2. Confirm the server runs standalone: `python3 mcp-server/server.py` should sit waiting on stdio,
   not error out immediately.
3. Run the fidelity test: `python3 mcp-server/test_server.py`. If this passes, the server itself is
   sound and the issue is in your client's MCP config (see
   [`installation/mcp-clients.md`](installation/mcp-clients.md) for the exact config shape/location
   per tool) — a wrong path or a missing `python3` on your system `PATH` are the two most common
   causes.

## A hardware spec or catalog lookup abstains instead of answering

This is deliberate, not a bug — the part genuinely isn't in the seeded catalog. The abstention
reason names the exact missing artifact. If you have the real spec, it's worth reporting as a real
catalog gap rather than working around it by asking a differently-worded question (which won't
produce a different, more complete answer — the catalog either has the part or it doesn't).

## Something in this documentation doesn't match what you're actually seeing

Report it. Every claim here is checked against something real — a script actually run, a tool's own
current documentation, a live fetch — as of when it was written. Tools update their own behavior;
if something has drifted since, that's a real, useful finding, the same standard this project
applies to its own internal claims.
