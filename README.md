# Refract

A Claude Code plugin suite for FTC robotics: citation-grounded rules compliance, structured
hardware lookup, elite-team-pattern-aware code review, and config-gated code generation — built
so Claude never guesses at a rule number, a motor spec, or what your robot actually has on it.

## Install

```
/plugin marketplace add N0v4ont0p/Refract
/plugin install refract-suite@refract
```

That's it. Requirements: Claude Code, and an FTC robot code repo to run it in.

## Which skill do I use?

This is the one thing to get right before anything else — the four skills split the work cleanly,
and picking the wrong one is the most common way to get confused.

| Skill | Use it for |
|---|---|
| **`ftc-team-config`** | **Start here for anything code-related.** Confirms your robot's config (drivetrain, mechanisms, software stack) and is the only skill authorized to generate new code once that config is confirmed. Writing a new OpMode, subsystem, or feature from scratch goes through this one. |
| **`ftc-hardware-lookup`** | Spec and math questions — motor specs, gear ratios, part compatibility, encoder ticks. |
| **`ftc-rule-check`** | "Is X legal," rule citations, Team Update questions. |
| **`ftc-code-review`** | Reviewing, auditing, or debugging code that **already exists** in your repo. Does not write new code. |

**Code review and code generation are different skills.** If you want something written from
scratch, start with `ftc-team-config`, not `ftc-code-review` — the review skill's job is to look
at code you already have, not to produce new code for you.

## Example

```
You:    write a teleop opmode for our shooter

Claude: (ftc-team-config) Quick check before I generate anything — I don't see a confirmed
        config for this repo yet. A couple of questions:
        1. What's your software stack — raw LinearOpMode, or a command-based framework
           (FTCLib/SolversLib)?
        2. Shooter mechanism — flywheel or something else, and is it single-speed or does
           it need variable RPM for distance?

You:    raw linear opmode, flywheel, variable RPM based on distance to goal

Claude: Confirming: mecanum drivetrain (inferred from hardware map), raw LinearOpMode,
        flywheel shooter with distance-based RPM control. Sound right?

You:    yep

Claude: Generating ShooterOpMode.java against that config now...
        [creates the file]
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
