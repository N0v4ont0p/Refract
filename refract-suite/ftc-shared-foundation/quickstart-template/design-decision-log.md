# Design Decision Log

An engineering-notebook-style record of decisions, not a changelog (git
already has that). Add an entry whenever you choose between real
alternatives -- especially anything a future teammate (or you, next season)
would otherwise have to reverse-engineer from the code. This is what
`known-failure-modes.md` calls "no engineering-notebook discipline": design
decisions untraceable, so knowledge leaves with whoever made them.

Keep entries even after a decision is later reversed -- the reversal is its
own entry that references the original, not a deletion. A log with only the
current "right answer" in it hides exactly the reasoning a future reader
needs when they're tempted to make the same reversed choice again.

## Entry format

```
## <ID> - <short title>
Date: YYYY-MM-DD
Status: proposed | accepted | superseded by #<ID>

**Context.** What problem or constraint forced a decision here.

**Options considered.** The real alternatives, briefly -- not just the one
you picked.

**Decision.** What you chose.

**Rationale.** Why, specifically -- tie it to a concrete constraint
(mechanical, rules, prior failure) rather than "seemed better."

**Consequences.** What this makes easier, what it makes harder, what to
revisit if a constraint changes.
```

---

## 0001 - Interface-based mechanism architecture (Drivetrain/Shooter/Turret/Intake)

Date: 2026-07-12
Status: accepted

**Context.** `known-failure-modes.md` names the God-OpMode / programming-
mechanical silo pattern as one of its two highest-leverage structural
failures (severity-high, frequency-high, and the root cause of several other
listed pain points). Concretely, this shows up as one TeleOp file that grows
past 500 lines because every mechanism's control logic gets added inline as
the season goes on -- there's no natural seam forcing it elsewhere.

**Options considered.**
- A single `Robot.java` god-class holding all hardware, called from a thin
  OpMode -- still one place for everything to accumulate, just moved one
  file over.
- Copy FTCLib-Quickstart's own convention as-is: one example `DriveSubsystem`
  extending FTCLib's `SubsystemBase`, no equivalent structure for
  shooter/turret/intake, and no enforced boundary stopping an OpMode from
  reaching past it.
- Per-mechanism interfaces (`Drivetrain`, `Shooter`, `Turret`, `Intake`) each
  with a `SubsystemBase`-extending example implementation, so every
  mechanism -- not just the drivetrain -- gets the same seam.

**Decision.** Per-mechanism interfaces, extending the upstream quickstart's
own `DriveSubsystem`/`SubsystemBase` convention to every mechanism instead of
leaving it drivetrain-only.

**Rationale.** An interface with 2-4 methods (`init`, plus the mechanism's
verbs) gives an OpMode nothing to reach past -- there's no seam for "just
quickly read this sensor here too" to sneak into the OpMode instead of into
the subsystem that owns that hardware. This is a structural fix, not a style
preference: a team following this pattern cannot easily produce the
696-line do-everything TeleOp the corpus's deterministic linter flags on
rookie repos, because there's no file where that logic naturally belongs.

**Consequences.** Adding a new mechanism means adding an interface + impl,
not editing an OpMode in place -- slightly more files up front, in exchange
for OpModes that stay thin for the life of the season. If a mechanism
genuinely needs cross-cutting state (e.g. a turret that must know the
shooter's spin-up state to decide when it's safe to move), that coordination
belongs in a command or a thin orchestrating class that depends on both
interfaces -- not in either mechanism's own class, and not in the OpMode.
