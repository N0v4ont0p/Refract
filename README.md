# Refract

A Claude Code plugin suite for FTC robotics: citation-grounded rules compliance, structured
hardware lookup, elite-team-pattern-aware code review, and config-gated code generation grounded
in real library documentation — built so Claude never guesses at a rule number, a motor spec, an
API call, or what your robot actually has on it.

## Install

```
/plugin marketplace add N0v4ont0p/Refract
/plugin install refract-suite@refract
```

That's it. Requirements: Claude Code, and an FTC robot code repo to run it in.

## Which skill do I use?

This is the one thing to get right before anything else — the five skills split the work cleanly,
and picking the wrong one is the most common way to get confused.

| Skill | Use it for |
|---|---|
| **`ftc-team-config`** | **Start here for anything code-related.** Confirms your robot's config (drivetrain, mechanisms, software stack). Doesn't write code itself — once the config is confirmed, it hands off to `ftc-construct` for the actual generation. |
| **`ftc-construct`** | Writes new code — a new OpMode, subsystem, or mechanism feature, from scratch. Reads your confirmed config, scaffolds from an interface-based template, and grounds every API call and tuning value in real library docs and the hardware catalog. Runs a mandatory rules-and-review check on its own output before calling anything done. Hands back to `ftc-team-config` if the config isn't confirmed yet. |
| **`ftc-hardware-lookup`** | Spec and math questions — motor specs, gear ratios, part compatibility, encoder ticks. |
| **`ftc-rule-check`** | "Is X legal," rule citations, Team Update questions. |
| **`ftc-code-review`** | Reviewing, auditing, or debugging code that **already exists** in your repo. Does not write new code. |

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
        undeclared-mechanism or known-failure-mode findings, no legality issues.
```

## What's in this repo

**`refract-suite/`** is the plugin — that's the only thing that gets installed. Everything else
(`PLAN.md`, `TRACEABILITY.md`, the elite-team pattern corpus, mining scripts, session records) is
the full development record: how the suite was designed, mined, and verified. It's kept for
transparency — you don't need any of it to just use the plugin.

## Current season

**DECODE (2025-26).** The rules corpus and hardware references reflect this season specifically;
the suite is built to carry forward when the season changes, but the shipped data is DECODE's.

## Credits

Team 19859 Reflection.

## License

[MIT](./LICENSE)
