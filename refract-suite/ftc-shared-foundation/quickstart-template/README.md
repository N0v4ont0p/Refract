# Team Quickstart Template

An FTC TeamCode starting point built around interfaces, not a starting point
built around one big TeleOp. It is derived from
[FTCLib/FTCLib-Quickstart](https://github.com/FTCLib/FTCLib-Quickstart) --
see `NOTICE.md` at the repo root for the license and exactly what was carried
over versus adapted.

This is a **TeamCode-module overlay**, not a standalone buildable repo. Drop
the `TeamCode/` folder here into a full FTC SDK or FTCLib-Quickstart checkout
(which supplies `FtcRobotController`, the root `build.gradle`,
`build.common.gradle`, `build.dependencies.gradle`, `settings.gradle`, the
Gradle wrapper, etc.) -- those files aren't duplicated here because nothing
about them changes for this template.

## Why it's laid out this way

Two failure modes from `known-failure-modes.md` are the reason this template
looks the way it does, not incidental style choices:

1. **God-OpMode / programming silo.** The taxonomy's highest-leverage
   structural failure is a single TeleOp that grows to hundreds of lines
   mixing drivetrain, shooter, turret, and intake logic together (the exact
   shape `ftc-code-review`'s `failure_mode_lint.py` flags as `god_opmode`).
   This template gives every mechanism its own interface
   (`Drivetrain`, `Shooter`, `Turret`, `Intake`) and one example concrete
   implementation. An OpMode built on `TeamOpMode` (see
   `opmodes/TeamOpMode.java`) has nowhere to put per-mechanism logic inline --
   it constructs subsystems in `onInit()` and lets the FTCLib
   `CommandScheduler` run them. See `opmodes/ExampleTeleOp.java` for what
   that looks like in practice: it stays small on purpose.
2. **No telemetry.** The taxonomy calls this out as the failure that makes
   every other one undiagnosable -- an intermittent fault (brownout, stale
   static, dropped sensor read) looks like an unreproducible hardware flake
   unless something recorded state at the time. `TeamOpMode` wires
   `telemetry/RobotTelemetry.java` (Driver Station + FTC Dashboard, via FTC
   Dashboard's own `MultipleTelemetry`) into every OpMode automatically and
   flushes it every loop. A subclass has to actively avoid using
   `telemetry` to end up with none -- not the other way around.

## Layout

```
TeamCode/src/main/java/org/firstinspires/ftc/teamcode/
├── RobotConstants.java          -- @Config tunables (read-only from code; see the class's own doc comment)
├── telemetry/
│   └── RobotTelemetry.java      -- Driver Station + FTC Dashboard fan-out
├── drivetrain/
│   ├── Drivetrain.java          -- interface
│   └── MecanumDrivetrain.java   -- example implementation (FTCLib MecanumDrive)
├── mechanisms/
│   ├── shooter/
│   │   ├── Shooter.java         -- interface
│   │   └── FlywheelShooter.java -- example implementation (FTCLib Motor, velocity control)
│   ├── turret/
│   │   ├── Turret.java          -- interface
│   │   └── SingleAxisTurret.java -- example implementation (FTCLib SimpleServo)
│   └── intake/
│       ├── Intake.java          -- interface
│       └── RollerIntake.java    -- example implementation (FTCLib Motor, raw power)
└── opmodes/
    ├── TeamOpMode.java          -- base class: wires telemetry, seals the FTCLib CommandOpMode lifecycle
    └── ExampleTeleOp.java       -- example OpMode: construct subsystems, bind gamepad, done
```

## Adding a mechanism your robot actually has

1. If it's a shape covered here (roller/claw intake, flywheel shooter,
   single/multi-axis turret, mecanum/other drivetrain), write a new class
   implementing the matching interface -- don't touch the interface itself
   unless it's genuinely missing a method every implementation would need.
2. If it's a genuinely new mechanism type, add a new interface next to the
   existing ones (small: init + the 2-4 verbs an OpMode needs) and one
   concrete implementation.
3. Wire it into an OpMode's `onInit()` exactly like the existing subsystems.
   If you find yourself writing more than a few lines of mechanism-specific
   logic directly in an OpMode file, that logic belongs in the subsystem
   class instead -- that's the whole point of this structure.

## RobotConstants and static tunables

`RobotConstants.java` uses the FTC Dashboard `@Config` idiom (carried over
from FTCLib-Quickstart's `DriveConstants.java`). Read that file's doc comment
before adding a field: these are for the **dashboard** to write between runs
and for **code to only read** -- writing to a mutable static field from
OpMode/subsystem lifecycle code is exactly the failure class
`known-failure-modes.md` documents under "global mutable static state" (a
write in run N silently leaks into run N+1, and passes clean in any single
tuning run because it only breaks when a run follows a run with the wrong
prior state).

## Engineering notebook

`design-decision-log.md` at the repo root is a running log, not a one-time
form -- add an entry whenever you make a decision future-you (or your
replacement, after graduation) will need the reasoning for, not just the
result. See that file for the format and a worked example.

**Commit convention:** `type(scope): summary`, where `type` is one of
`feat` / `fix` / `refactor` / `tune` / `docs`, and `scope` is the
mechanism/subsystem touched (e.g. `feat(shooter): add distance-based velocity
lookup`). Reference the decision-log entry ID in the commit body when a
commit implements a decision recorded there (`See decision-log #0002.`). This
is what makes `git blame`/`git log` answer "why is this here" instead of just
"what changed" -- the gap `known-failure-modes.md` names as the concrete cost
of skipping version-control discipline.
