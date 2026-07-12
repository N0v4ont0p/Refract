# Verbatim message to the user (session stopped here awaiting reply)

Before I set anything up, there's a conflict in the request I can't resolve for you.

**The `fixed_shooter_on_swerve` archetype requires a swerve drivetrain, and you run mecanum.** That's not my judgment call — it's a hard constraint in this season's extension (decode-2025-26 `constraints_on_core`), and the validator rejects the combination:

```
constraint violated: archetype 'fixed_shooter_on_swerve' requires
core.drivetrain.type='swerve', config has 'mecanum'
```

The reason it's a constraint and not a style preference: in that archetype the drivetrain *itself* provides aim — the whole point is that swerve can hold a heading toward the goal independently of translation. A mecanum robot with a fixed (non-turreted) shooter has to rotate the entire chassis to aim, which is a different robot with different code.

So which of these describes what you actually want? The season's known archetypes give you three coherent paths:

1. **Keep mecanum, add a turret** → the `turreted_shooter` archetype. The turret decouples aim from drivetrain heading (and enables shoot-while-moving). This is the closest match to "fixed-shooter-on-swerve behavior" on a mecanum base.
2. **Keep mecanum with a genuinely fixed shooter** (no turret) → not one of the named archetypes; aiming means rotating the whole robot. Doable, but I want you choosing it knowingly.
3. **You're actually building/switching to swerve** → then `fixed_shooter_on_swerve` is valid as requested, but "we run mecanum" would be wrong and I'd need module count (3 or 4) and module source (off-shelf or custom).

I won't generate anything until this is settled — a config that's physically incoherent fails here, at entry, not later as deployed code that can't work.

**While you're answering, two more things I have to confirm regardless** (they gate too much downstream to guess, and your repo is empty so I couldn't infer them):

- **OpMode style** — FTCLib command-based, or raw LinearOpMode? (This is the single highest-leverage question: 15 of the 61 mined patterns branch on it.)
- **Season mechanisms** — for DECODE: intake type (roller / claw / other), shooter type (flywheel / elastic catapult / none), turret (none / single-axis / multi-axis — your answer above decides this), gate mechanism (present / none), classifier interaction (present / none).

What I have recorded so far, none of it confirmed yet: **team 99903, mecanum drivetrain, RoadRunner pathing** — I'll confirm the full picture back to you before anything generates.

(No question needed on the control hub: through this season the REV Control Hub is the only legal control system, so it's recorded as inferred.)
