# Transcript summary

## Files read
- `project/team-config.yaml` — team config. Confirmed: mecanum, raw LinearOpMode style, flywheel shooter, roller intake, **turret: none**.
- `project/TeamCode/MainTeleOp.java` — main TeleOp, raw `LinearOpMode`, ~316 lines (mostly filler telemetry).
- `project/TeamCode/Shooter.java` — SolversLib `SubsystemBase` with an empty `spinUp()`; unused by MainTeleOp.
- `project/TeamCode/TurretAimer.java` — turret aiming class; unreferenced, contradicts config (`turret: none`).

## Root cause of the reported symptom ("flywheel tune different every match, no changes, motor swapped")
**Mutable `public static` field:** `MainTeleOp.java:4` — `public static double flywheelOffset = 0.0;`

Static fields live on the class, not the OpMode instance, and the Robot Controller JVM persists across OpMode INIT/STOP cycles. So shooter state carries over between runs and only resets to its initializer when the RC app is restarted / redeployed / the hub is power-cycled. The match-to-match "flake" tracks invisible app-restart events, not the motor — which is why swapping the motor did nothing. This is a code-structure bug masquerading as a hardware flake.

Written from a lifecycle method at line 12 (`flywheelOffset = 0.25;`), which is precisely the mutable-static-state anti-pattern.

## Fix recommended
1. Remove `static` (or make the constant `static final` — a constant can't drift; only mutable static does).
2. Initialize shooter params deterministically at INIT and print the active value to telemetry so a wrong tune is visible, not mysterious.

## Secondary findings (not the flake, flagged for pre-comp cleanup)
- `TurretAimer.java` = dead code contradicting `turret: none` config → delete.
- `Shooter.java` = empty shell, never used; there is **no real flywheel control** in the code (no velocity/encoder control). Open-loop power means battery sag will also drift the shot → add closed-loop `setVelocity` control.
- `MainTeleOp` is a 300+ line god OpMode (mostly filler here) → keep OpModes thin, push logic into subsystems.

## Conclusion
Primary root cause = mutable `public static double flywheelOffset` cross-OpMode state persistence (MainTeleOp.java:4). Hardware was a red herring.
