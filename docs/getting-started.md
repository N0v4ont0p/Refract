# Getting started

## What Refract is

Refract is a suite of 5 grounded skills for FTC (FIRST Tech Challenge) robotics, plus a small set
of standalone tools around them. It exists because a confident-sounding rule citation, motor
spec, or API call that's wrong compiles and deploys just fine — it just fails at a match, or gets
a robot disqualified at inspection. Every fact Refract's skills produce is retrieved from a stored
source or computed by a deterministic script, never generated from memory. See
[`architecture.md`](architecture.md) for why that distinction is the actual point of this project,
not an implementation detail.

## What it does

- **`ftc-team-config`** confirms your robot's real configuration (drivetrain, mechanisms, software
  stack) before anything gets generated against a guess.
- **`ftc-construct`** writes new code — OpModes, subsystems, mechanisms — grounded in real library
  docs, the hardware catalog, and a corpus of patterns mined from real competitive teams.
- **`ftc-hardware-lookup`** answers spec and math questions from structured tables and scripts,
  never from memory.
- **`ftc-rule-check`** delivers legality verdicts with verified citations against the tagged
  Competition Manual.
- **`ftc-code-review`** reviews code you already have — deterministic anti-pattern linting plus
  pattern-aware structural review.

Full depth on each, with a real example interaction: [`skills-guide.md`](skills-guide.md).

## What's in this repo

**`refract-suite/`** is the plugin — the only thing that gets installed via `/plugin install`.
**`mcp-server/`** and **`corpus-input-scan.py`** are separate, standalone tools usable by cloning
this repo directly, not installed through the plugin marketplace — see
[`mcp-server.md`](mcp-server.md) for the former; the latter is a draft-only scanner that flags
candidate new team repos, stale library releases, and Team Update drift for human review, and
never writes into the corpus itself. Everything else (`PLAN.md`, `ROADMAP.md`, `TRACEABILITY.md`,
the elite-team pattern corpus, mining scripts, phase-by-phase findings docs) is the full
development record — how the suite was designed, mined, and verified. Kept for transparency; you
don't need any of it to just use the plugin.

## Where to actually start

**The strongest fact in this whole compatibility story, stated up front rather than buried: every
tool checked so far reaches Refract, no exceptions.** Some (Claude Code, VS Code, Copilot CLI,
OpenCode, Cursor) read the skills directly with zero setup. The rest (Gemini CLI, Codex,
Antigravity) need a placement step for that path — but every single one of the 8 also works as a
plain MCP client, which reaches the exact same grounded data with no placement step at all. A tool
that can't auto-discover `SKILL.md` is never actually unsupported here.

1. **Install** for your tool of choice — see [`installation/`](installation/) for the one that
   matches what you use.
2. **Describe your robot once.** The first time you ask for code in a repo with no confirmed
   config, `ftc-team-config` will ask a handful of questions — only the ones that actually change
   what gets built — and remembers the answer.
3. **Ask for what you need** — a legality check, a hardware spec, a new subsystem, a review of
   existing code. The right skill triggers automatically from what you ask, not from a command you
   have to remember.

## If something doesn't match what's documented here

Say so. Every claim in this documentation set is checked against something real — a script run, a
tool's own current docs, a live fetch — not asserted from confidence. If a tool's behavior has
moved since a page was written, that's a real gap worth closing, not something to paper over. See
[`troubleshooting.md`](troubleshooting.md) first; if it's not covered there, it's worth reporting.
