# Refract

[![License: MIT](https://img.shields.io/github/license/N0v4ont0p/Refract)](./LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/N0v4ont0p/Refract)](https://github.com/N0v4ont0p/Refract/commits/main)

A grounded FTC (FIRST Tech Challenge) robotics skill suite: citation-grounded rules compliance,
structured hardware lookup, elite-team-pattern-aware code review, and config-gated code
generation — built so Claude never guesses at a rule number, a motor spec, an API call, or what
your robot actually has on it. See [`docs/architecture.md`](docs/architecture.md) for why that's
the actual point of this project, not a tagline.

## Install

**Every tool checked so far reaches Refract's grounded data — every one, with no exceptions.**
Some read the skills directly with zero setup; the rest still get full access through a plain MCP
connection, regardless of whether they read skills at all. Nothing here was left unsupported.

Fastest path, Claude Code:

```
/plugin marketplace add N0v4ont0p/Refract
/plugin install refract-suite@refract
```

For VS Code, Copilot CLI, Cursor, Gemini CLI, OpenCode, Codex, Antigravity, or any other
MCP-speaking client, see [`docs/installation/`](docs/installation/) for exactly what each one
needs — checked against that tool's own current documentation, not guessed.

### Update

```
/plugin marketplace update refract
/plugin uninstall refract-suite@refract
/plugin install refract-suite@refract
```

All three steps are needed — `marketplace update` alone refreshes the catalog but not what's
already installed, verified with a real reinstall, not assumed (detail:
[`docs/installation/claude-code.md`](docs/installation/claude-code.md)).

### Uninstall

```
/plugin uninstall refract-suite@refract
/plugin marketplace remove refract
```

## Which skill do I use?

The one thing to get right before anything else — the five skills split the work cleanly, and
picking the wrong one is the most common way to get confused.

| Skill | Use it for |
|---|---|
| **`ftc-team-config`** | **Start here for anything code-related.** Confirms your robot's config (drivetrain, mechanisms, software stack). Doesn't write code itself — once the config is confirmed, it hands off to `ftc-construct` for the actual generation. |
| **`ftc-construct`** | Writes new code — a new OpMode, subsystem, or mechanism feature, from scratch. Reads your confirmed config, scaffolds from an interface-based template, and grounds every API call and tuning value in real library docs and the hardware catalog. Runs a mandatory rules-and-review check on its own output before calling anything done. Hands back to `ftc-team-config` if the config isn't confirmed yet. |
| **`ftc-hardware-lookup`** | Spec and math questions — motor specs, gear ratios, part compatibility, encoder ticks. Abstains rather than guesses on a part outside the seeded catalog. |
| **`ftc-rule-check`** | "Is X legal," rule citations, Team Update questions. Every verdict runs a freshness check first and cites verified rule text — never answered from memory. |
| **`ftc-code-review`** | Reviewing, auditing, or debugging code that **already exists** in your repo. Does not write new code. If a review turns up a genuine legality question, it resolves that through `ftc-rule-check`'s own real flow rather than approximating it. |

**Code review and code generation are different skills.** Something written from scratch starts
with `ftc-team-config` (it hands off to `ftc-construct` once confirmed) — not `ftc-code-review`,
whose job is code you already have. Real depth on each, with a full example interaction:
[`docs/skills-guide.md`](docs/skills-guide.md).

## Example

```
You:    write a teleop opmode for our shooter

Claude: (ftc-team-config) I don't see a confirmed config for this repo yet. A couple of questions:
        1. What's your software stack — raw LinearOpMode, or a command-based framework?
        2. Shooter mechanism — flywheel or something else, variable RPM or fixed?

You:    raw linear opmode, flywheel, variable RPM based on distance to goal

Claude: Confirming: mecanum drivetrain (inferred from hardware map), raw LinearOpMode, flywheel
        shooter with distance-based RPM control. Sound right?

You:    yep

Claude: (ftc-construct) Config confirmed — generating ShooterOpMode.java, grounded in your
        software stack's actual API docs. Running the mandatory rules-and-review check...
        clean. Done.
```

## Docs

- [**Getting started**](docs/getting-started.md) — what Refract is, where to start
- [**Installation**](docs/installation/) — per-tool setup, precisely what each one needs
- [**Skills guide**](docs/skills-guide.md) — real depth and an example for each of the 5 skills
- [**MCP server**](docs/mcp-server.md) — the 4 tools, real example calls and output
- [**Architecture**](docs/architecture.md) — the actual differentiator, explained properly
- [**FAQ**](docs/faq.md) · [**Troubleshooting**](docs/troubleshooting.md) · [**Changelog**](docs/changelog.md)

## Current season

**DECODE (2025-26).** Built to carry forward when the season changes — see
[`docs/architecture.md`](docs/architecture.md) for how the schema keeps season-specific data
separate from what doesn't change.

## Credits

Team 19859 Reflection.

## License

[MIT](./LICENSE)
