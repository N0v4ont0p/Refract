# Transcript Summary — Team 45021 Pre-Comp Review

## Files actually read (all 23 source files + config)

Config:
- `team-config.yaml`

OpModes:
- `TeamCode/opmodes/TeleOpMain.java`
- `TeamCode/opmodes/AutoBlueLeft.java`
- `TeamCode/opmodes/AutoBlueRight.java`
- `TeamCode/opmodes/AutoRedLeft.java`
- `TeamCode/opmodes/AutoRedRight.java`

Subsystems:
- `TeamCode/subsystems/Drivetrain.java`
- `TeamCode/subsystems/Intake.java`
- `TeamCode/subsystems/Deposit.java`
- `TeamCode/subsystems/Shooter.java`
- `TeamCode/subsystems/Climber.java`
- `TeamCode/subsystems/Hang.java`
- `TeamCode/subsystems/Odometry.java`
- `TeamCode/subsystems/Sensors.java`
- `TeamCode/subsystems/Vision.java`
- `TeamCode/subsystems/Lighting.java`

Control:
- `TeamCode/control/PIDController.java`
- `TeamCode/control/FeedForward.java`
- `TeamCode/control/Filters.java`
- `TeamCode/control/Kinematics.java`
- `TeamCode/control/Localizer.java`
- `TeamCode/control/MotionProfile.java`
- `TeamCode/control/PathFollower.java`

Hardware:
- `TeamCode/hardware/TurretController.java`

## Complete list of issues found

### Blocking (cannot compete as-is)
1. **No OpMode registration.** `TeleOpMain` lacks `@TeleOp`; all four autos lack `@Autonomous`. Nothing will appear on the Driver Station.
2. **No actuator commands anywhere.** Every subsystem/control class exposes only `computeN`/`stepN` filler-math methods; nothing calls `setPower`/`setVelocity`/`setPosition` or reads sensors. No robot motion logic exists.
3. **Motor-init copy-paste bug.** Every `init()` reassigns the same field `a` for every motor, discarding all but the last handle; field `b` is never assigned. Affects Drivetrain (4→1), Intake, Deposit, Climber, Hang, Vision (2→1 each), Odometry, Sensors (3→1 each), Lighting.
4. **TeleOp is inert.** Grabs hardware as `Object.class`, never reads gamepad, never sets power; loop only spams 360 telemetry lines with no `telemetry.update()`. Robot won't move in TeleOp.
5. **Autos don't move or park.** All four fetch `"drive"` as `Object.class`, dump 40 telemetry lines once (no `telemetry.update()`), exit. No trajectory, no park — yet config marks parking mandatory.
6. **All four autos are byte-for-byte identical.** Alliance/start-position never handled.

### Correctness
7. **`autoAlignOffset` static persistence.** Non-final `public static double` incremented `+= 0.05` every `runOpMode()`, never reset; accumulates across INITs within the app process → nondeterministic per-match behavior.
8. **`Shooter.fly` never initialized.** `spinUp()` calls `fly.setVelocity()` on a null handle → NPE. Also `Shooter` extends solverslib `SubsystemBase` (command-based) while config is `raw_linear_opmode` — inconsistent stack.
9. **OpModes and subsystems fully disconnected.** No OpMode instantiates any subsystem, and hardware-map names disagree (subsystems expect `"drivetrain0..3"`; TeleOp expects `"fl/fr/bl/br/intake/shoot/climb"`; autos expect `"drive"`).

### Config mismatches / dead code
10. **Turret code vs `turret: none`.** `TurretController.java` drives a turret servo not present in config.
11. **Pathing/localization stack vs `pathing: none` + `raw_linear_opmode`.** `PathFollower`, `MotionProfile`, `Kinematics`, `Localizer`, `Odometry` are unused and contradict config.
12. **Unlisted/duplicate subsystems.** `Deposit`, `Climber` AND `Hang` (two endgame mechs), `Vision`, `Lighting`, `Sensors` are not in config and unreferenced by any OpMode.
13. **Whole repo is placeholder/stub code.** Every file is dominated by identical dead `computeN`/`stepN` math with no callers; no working robot program is present.
