# Flywheel "flake" — it's the code, not the motor

Short version: swapping the motor was never going to fix this. The thing that changes match-to-match isn't your hardware — it's a piece of state in the code that survives between OpMode runs and only resets when the Robot Controller app restarts. So your tune "randomly" being right or way off actually tracks *whether the phone/Control Hub got restarted between matches*, not anything physical.

## The root cause

`MainTeleOp.java`, line 4:

```java
public static double flywheelOffset = 0.0;  // non-final public static
```

This is a **mutable `public static` field** — a global variable that lives on the *class*, not on the OpMode instance. On the Robot Controller, the app's JVM stays alive across OpMode runs. When you INIT/STOP an OpMode, `runOpMode()` ends but the class (and its static fields) does **not** get re-created. `flywheelOffset` keeps whatever value it had until:

- you re-select and the code re-assigns it, **or**
- the RC app is restarted / redeployed / the hub is power-cycled (which resets it back to `0.0`).

That is exactly the profile of your symptom:

- **Match A:** app was fresh (just deployed / hub rebooted) → offset starts at `0.0` → tune is off.
- **Match B:** app had been running, a prior OpMode left offset at `0.25` → tune is right.
- Nobody "changed anything" between them — the only variable was an app restart, which is invisible and easy to miss.

Right now line 12 (`flywheelOffset = 0.25;`) happens to re-set it every run, but this is the dangerous pattern regardless: **any shooter parameter that lives in mutable static state will drift depending on run history and app lifecycle.** The moment that assignment is behind a condition, a button, a different OpMode, or a tuning routine, you get non-reproducible behavior that looks *exactly* like a flaky motor.

## The fix

Make shooter state instance state, not class state. Two options:

1. **Simplest:** drop `static`. Store the offset as a normal field (or local) that is set from a single known-good constant every INIT.

   ```java
   // constant, can't drift:
   private static final double FLYWHEEL_OFFSET = 0.25;
   ```

   `static final` is fine — a constant never changes, so it can't cause this. It's *mutable* `static` that bites you.

2. **If you genuinely need a tunable value that persists on purpose** (e.g. a dashboard/FTC-Dashboard knob you adjust between matches): keep it explicit and re-initialize it to a known value in `runOpMode()` *before* `waitForStart()`, and show it on telemetry so you can *see* the current value before every match. Never rely on "it was probably still 0.25 from last time."

Either way: put the shooter's numbers in one place, set them deterministically at INIT, and print the active value to the Driver Station so a wrong tune is visible instead of mysterious.

## While I was in there (not your flake, but worth cleaning up before comp)

- **`TurretAimer.java` is dead code.** Your `team-config.yaml` declares `turret: none`, and nothing references `TurretAimer`. It won't hurt the flywheel, but delete it so nobody wires it up by accident.
- **`Shooter.java` is an empty shell.** It extends a SolversLib `SubsystemBase` and has an empty `spinUp()`, but `MainTeleOp` is a raw `LinearOpMode` that never uses it. So there's actually **no real flywheel control logic here** — no velocity control, no `setVelocity`/`RUN_USING_ENCODER`. If your flywheel is running open-loop on raw power, battery sag between matches will *also* make it shoot short as the match goes on. Once the static bug is fixed, run the flywheel with velocity control (encoder + `setVelocity`) so it holds RPM regardless of battery state.
- **`MainTeleOp` is a 300+ line "god" OpMode.** Most of it is filler telemetry here, but as a habit, keep OpModes thin and push mechanism logic into subsystems — it makes exactly this kind of bug easier to spot.

## What to do next

1. Remove `static` from `flywheelOffset` (or make the real tune value `static final`).
2. Set the shooter's numbers deterministically at INIT and print the active offset/target RPM to telemetry.
3. Add closed-loop velocity control to the flywheel so battery voltage doesn't move your shot.
4. Delete `TurretAimer.java`.

Do #1 first — that alone stops the "different every match" behavior. The motor was innocent.
