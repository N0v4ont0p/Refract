# Refract

A Claude Code plugin suite for FTC robotics: citation-grounded rules compliance, structured
hardware lookup, elite-team-pattern-aware code review, config-gated code generation grounded in
real library documentation, and a narrow legality handoff between review and rules — built so
Claude never guesses at a rule number, a motor spec, an API call, or what your robot actually has
on it.

## Install

```
/plugin marketplace add N0v4ont0p/Refract
/plugin install refract-suite@refract
```

That's it. Requirements: Claude Code, and an FTC robot code repo to run it in.

## Update

```
/plugin marketplace update refract
```

Pulls the latest commit pushed to this repo's `main` branch. Run it whenever you want the current
version — nothing updates automatically.

## Uninstall

```
/plugin uninstall refract-suite@refract
/plugin marketplace remove refract
```

Uninstall the plugin first, then remove the marketplace. To reinstall from a different source
later (a fork, a different remote), re-add the marketplace pointing at that source and install
again.

## Which skill do I use?

This is the one thing to get right before anything else — the five skills split the work cleanly,
and picking the wrong one is the most common way to get confused.

| Skill | Use it for |
|---|---|
| **`ftc-team-config`** | **Start here for anything code-related.** Confirms your robot's config (drivetrain, mechanisms, software stack). Doesn't write code itself — once the config is confirmed, it hands off to `ftc-construct` for the actual generation. |
| **`ftc-construct`** | Writes new code — a new OpMode, subsystem, or mechanism feature, from scratch. Reads your confirmed config, scaffolds from an interface-based template, and grounds every API call and tuning value in real library docs and the hardware catalog. Runs a mandatory rules-and-review check on its own output — at genuine parity with `ftc-rule-check`'s own freshness-gate-then-verdict flow, not an approximation of it — before calling anything done. Hands back to `ftc-team-config` if the config isn't confirmed yet. |
| **`ftc-hardware-lookup`** | Spec and math questions — motor specs, gear ratios, part compatibility, encoder ticks. Abstains rather than guesses on a part outside the seeded catalog. |
| **`ftc-rule-check`** | "Is X legal," rule citations, Team Update questions. Every verdict runs a freshness check first and cites verified rule text — never answered from memory. |
| **`ftc-code-review`** | Reviewing, auditing, or debugging code that **already exists** in your repo. Does not write new code. If a review turns up a genuine legality question about that code, it resolves it through `ftc-rule-check`'s own real flow (not a guess dressed as a review finding) rather than either reviewing it structurally or deferring you elsewhere. |

**Code review and code generation are different skills.** If you want something written from
scratch, start with `ftc-team-config` (it hands off to `ftc-construct` once your config is
confirmed) — not `ftc-code-review`, whose job is to look at code you already have, not produce new
code for you.

## Example

```
You:    write a teleop opmode for our shooter

Claude: (ftc-team-config) Quick check before anything gets generated — I don't see a confirmed
        config for this repo yet. A couple of questions:
        1. What's your software stack — raw LinearOpMode, or a command-based framework
           (FTCLib/SolversLib)?
        2. Shooter mechanism — flywheel or something else, and is it single-speed or does
           it need variable RPM for distance?

You:    raw linear opmode, flywheel, variable RPM based on distance to goal

Claude: Confirming: mecanum drivetrain (inferred from hardware map), raw LinearOpMode,
        flywheel shooter with distance-based RPM control. Sound right?

You:    yep

Claude: (ftc-construct) Config confirmed — generating ShooterOpMode.java against it now,
        grounded in your software stack's actual API docs...
        [creates the file]
        Running the rules and code-review checks on what I just wrote... clean — no
        undeclared-mechanism or known-failure-mode findings, no legality issues (freshness
        checked, verdict grounded in the current manual).
```

## Beyond Claude Code — cross-tool compatibility

Refract's 5 skills use the open [Agent Skills format](https://agentskills.io) — a
folder with a `SKILL.md` file, `name`/`description` frontmatter, originally built by Anthropic and
released as an open standard. That means other tools can read them too, but *how much setup that
takes varies by tool* — stated precisely below, not as a blanket "it just works," because that
claim was checked directly against each tool's own documentation, not assumed from one page's
description of its own adoption. (One prior version of this claim — "5 of 8 tools, zero bridge" —
didn't survive that check; this table is the corrected version.)

| Tool | What it takes |
|---|---|
| **VS Code / GitHub Copilot** | **Nothing.** Scans `.claude/skills/` directly — this repo's skills are already in a location it reads. |
| **OpenCode** | **Nothing.** Also scans `.claude/skills/` directly. |
| **Cursor** | Auto-discovers skills, but only from `.agents/skills/` or `.cursor/skills/` — not `.claude/skills/`. Symlink or copy this repo's `refract-suite/skills/` folders into one of those locations to pick them up. |
| **OpenAI Codex** | Same shape as Cursor: auto-discovers, but only from `.agents/skills/` — place the skill folders there. |
| **Gemini CLI** | Needs the skills placed (as above) *and* an explicit link + enable step per skill: `/skills link <path>` then `/skills enable`. |
| **Antigravity** | Not verified either way — wasn't in the tools checked directly, and wasn't found in the Agent Skills client list either. Don't assume support until someone checks. |

**Everything else in the suite — deterministic scripts, live tool execution — is available to any
MCP-speaking client** via `mcp-server/` in this repo (not part of the installed plugin; run it
separately: `pip install -r mcp-server/requirements.txt && python3 mcp-server/server.py`). It
exposes rule lookup, hardware lookup, corpus query, and config validation as thin wrappers over the
exact same scripts the skills themselves call — no logic duplicated, no grounding lost. See
`mcp-server/README.md` for the tool list and `PHASE-C1-C2-FINDINGS.md` for the full compatibility
investigation, including how the PreToolUse safety hook (blocking writes to reference-only
directories) can also be carried into OpenCode via a separate community plugin, and what that
specifically requires.

## What's in this repo

**`refract-suite/`** is the plugin — that's the only thing that gets installed via
`/plugin install`. **`mcp-server/`** and **`corpus-input-scan.py`** are separate, standalone tools
usable by cloning this repo directly (not installed through the plugin marketplace) — the former
exposes Refract's grounded data to any MCP client, the latter is a draft-only scanner that flags
candidate new team repos, stale library releases, and Team Update drift for human review; it never
writes into the corpus itself. Everything else (`PLAN.md`, `ROADMAP.md`, `TRACEABILITY.md`, the
elite-team pattern corpus, mining scripts, phase-by-phase findings docs) is the full development
record: how the suite was designed, mined, and verified. It's kept for transparency — you don't
need any of it to just use the plugin.

## Current season

**DECODE (2025-26).** The rules corpus and hardware references reflect this season specifically;
the suite is built to carry forward when the season changes, but the shipped data is DECODE's.

## Credits

Team 19859 Reflection.

## License

[MIT](./LICENSE)
