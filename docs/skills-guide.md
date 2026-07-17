# Skills guide

Real depth on each of the 5 skills — what it actually does, how it decides to act, and a real
example interaction. For which one to reach for, see the table in [`README.md`](../README.md);
this page is for once you know which one you need and want to see it work.

## `ftc-team-config`

**Job**: establish and maintain a *confirmed* picture of the robot before any code generation. It
does not write code — it hands off to `ftc-construct` once the config is confirmed.

**How it decides what to ask**: it runs a deterministic feature-vector extractor over your repo
first (import signatures, hardware-map declarations, OpMode base classes), so inference fills in
what code can prove before a single question gets asked. Three things get asked and confirmed
*regardless* of how good the inference looks — drivetrain topology, the season's mechanism set, and
the software stack — because a wrong guess there gates too much downstream. Everything else is
ranked by how many corpus patterns actually branch on it, so the questions that matter most get
asked first if your patience runs out before the list does.

**Example**:

```
You:    write a teleop opmode for our shooter

Claude: (ftc-team-config) I don't see a confirmed config for this repo yet. A couple of questions:
        1. What's your software stack — raw LinearOpMode, or a command-based framework?
        2. Shooter mechanism — flywheel or something else, variable RPM or fixed?

You:    raw linear opmode, flywheel, variable RPM based on distance to goal

Claude: Confirming: mecanum drivetrain (inferred from hardware map), raw LinearOpMode, flywheel
        shooter with distance-based RPM control. Sound right?

You:    yep

Claude: Confirmed — handing off to ftc-construct.
```

## `ftc-construct`

**Job**: write new code — OpModes, subsystems, mechanism features — grounded in real library docs,
the hardware catalog, and the pattern corpus. Reads the confirmed config by reference; if it isn't
confirmed, hands back to `ftc-team-config` rather than generating against a guess.

**How it grounds a generation**: every API call against a library the config selects gets checked
against that library's actual fetched docs before being written, not recalled. Every hardware value
comes from `ftc-hardware-lookup`'s catalog and scripts. A corpus pattern only gets cited if its
`applicable_when` genuinely matches the confirmed config — and its confidence/provenance tags
display exactly as stored, never inflated. Before calling anything done, it re-runs the same
rules-and-review scripts `ftc-rule-check` and `ftc-code-review` use directly.

**Example** (continuing from the config above):

```
Claude: (ftc-construct) Generating ShooterOpMode.java against the confirmed config — grounding
        the velocity-PIDF setup against your library docs...
        [creates the file]
        Running the mandatory verification: config_lint.py clean, failure_mode_lint.py clean,
        rule-check verdict legal (freshness checked, citation R303 — single-DoF COTS mechanisms
        allowed). Done.
```

## `ftc-hardware-lookup`

**Job**: answer spec and math questions — motor specs, gear ratios, part compatibility, encoder
ticks, projectile trajectory — from structured catalog tables and deterministic scripts. Never
from memory, even for a spec that sounds well-known.

**How it decides to abstain**: if a part isn't in the seeded catalog, the answer is an explicit
abstention with the reason and a pointer to the manufacturer page — not a plausible-sounding guess.
This is checked, not assumed: a hardcoded goBILDA wheel size, asked for during a real config
confirmation session for this project, was deliberately *not* answered from a strongly-remembered
number — it was looked up on the actual product page instead, specifically because no catalog entry
existed to check the number against.

**Example**:

```
You:    what's the free speed and gear ratio I need for ~200 RPM output from a goBILDA 5203-2402-0019?

Claude: (ftc-hardware-lookup) Free speed at the 19.2:1 internal ratio: 312 RPM (goBILDA product
        page, tier-1). External ratio for ~200 RPM: 1.56:1 (312 / 1.56 = 200.0 exactly).
```

## `ftc-rule-check`

**Job**: deliver legal/illegal/ambiguous verdicts with citations verified against the tagged
Competition Manual. Every verdict runs a freshness check first.

**How a verdict actually forms**: freshness gate first (flags if the corpus might be behind the
live manual); rule lookup with one-hop cross-reference traversal (not just the first rule that
matches keywords); an explicit reasoning step from the retrieved text to a verdict; a final
citation-existence check. "Ambiguous" is a real, valid outcome — not a failure to decide.

**Example**:

```
You:    can our expansion hub run off its own separate battery instead of the main one?

Claude: (ftc-rule-check) Freshness check: UNVERIFIABLE (couldn't confirm a live Team Update number)
        — noting that caveat below.
        Verdict: illegal. R601 requires exactly one main 12V battery as the sole power source for
        the robot's control system; R602 requires any device receiving Control/Expansion Hub
        signals to run off that same main battery. A separate battery for the expansion hub is a
        second main-scale battery, which R601/R605 forbid outright.
```

## `ftc-code-review`

**Job**: review code that already exists — deterministic anti-pattern linting plus structural
review grounded in the pattern corpus. Does not write new code.

**How it stays deterministic where it can**: two linters (`config_lint.py`,
`failure_mode_lint.py`) catch specific known-failure-mode patterns — stale mutable static state
written from an OpMode lifecycle method, a mechanism referenced in code the confirmed config
declares absent — at O(1) script-call cost, not by reading the whole repo. If a review question
turns out to be a legality question in disguise, it's resolved through `ftc-rule-check`'s own real
flow, not approximated.

**Example**:

```
You:    review our Shooter.java, something feels off with the flywheel

Claude: (ftc-code-review) failure_mode_lint.py found a mutable static field (flywheelOffset)
        written from inside the OpMode lifecycle — this persists across a stop/restart and is a
        real, corpus-documented failure mode (a match that starts with the wrong offset carried
        over from a prior run). Recommend making it instance-scoped, reset in init().
```
