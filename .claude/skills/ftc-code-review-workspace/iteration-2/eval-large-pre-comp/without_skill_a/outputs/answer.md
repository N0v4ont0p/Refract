# Pre-Competition Sanity Check — Team 45021

I read all 23 files in the repo plus `team-config.yaml`. I have to be blunt because you're short on time and the weekend is close: **this codebase will not run your robot.** Nothing in it commands a single motor or servo, none of your OpModes will even show up on the Driver Station, and every subsystem's hardware setup is broken by the same copy-paste bug. Below is the honest picture, worst-first.

## Blocking issues (robot cannot compete as-is)

### 1. No OpMode will appear on the Driver Station
`TeleOpMain` has no `@TeleOp` annotation, and `AutoBlueLeft/AutoBlueRight/AutoRedLeft/AutoRedRight` have no `@Autonomous` annotation. Without those annotations the SDK never registers them, so you will have **nothing to select** on the Driver Station. This alone stops you from running at the event. Add `@TeleOp(name=...)` / `@Autonomous(name=...)` to each.

### 2. Nothing actually drives any actuator
Every subsystem (`Drivetrain`, `Intake`, `Deposit`, `Climber`, `Hang`, `Odometry`, `Sensors`, `Vision`, `Lighting`) exposes only `computeN(double x)` methods that add up a meaningless constant series and return a number. **None of them ever call `setPower`, `setVelocity`, `setPosition`, or read anything.** The control classes (`PIDController`, `FeedForward`, `Filters`, `Kinematics`, `Localizer`, `MotionProfile`, `PathFollower`) are the same: `stepN(double e)` filler math. This is scaffolding, not robot code — there is no logic that would move the robot.

### 3. Motor handles are thrown away in every `init()`
In every subsystem, `init()` assigns *every* motor to the same field `a`, overwriting the previous one:
```java
a = hw.get(DcMotor.class, "drivetrain0");
a = hw.get(DcMotor.class, "drivetrain1");  // overwrites a
a = hw.get(DcMotor.class, "drivetrain2");  // overwrites a
a = hw.get(DcMotor.class, "drivetrain3");  // overwrites a
```
Only the last motor survives; the other handles are lost and the second field `b` is never assigned at all. So even if you wrote drive logic, you could only ever command one of the four drive motors. Same bug in `Intake`, `Deposit`, `Climber`, `Hang`, `Odometry`, `Sensors`, `Vision`, `Lighting`.

### 4. TeleOp does nothing but spam telemetry
`TeleOpMain.runOpMode()` grabs hardware as `Object.class` (wrong type — unusable as motors), never reads a gamepad, never sets a power. Its `while (opModeIsActive())` loop only pushes 360 telemetry lines (`d0`..`d359`) and **never calls `telemetry.update()`**, so even the telemetry won't render. It's a tight busy-loop that moves nothing. Drivers will have zero control.

### 5. Autos don't move and don't park — parking is mandatory for you
All four autos fetch `"drive"` as `Object.class`, `waitForStart()`, dump 40 telemetry lines once (no `telemetry.update()`), and end. Zero motor commands, no trajectory, no park. Your `team-config.yaml` marks `endgame_parking: mandatory`, so this leaves guaranteed auto points and the park on the table.

### 6. All four autos are byte-for-byte identical
`AutoBlueLeft`, `AutoBlueRight`, `AutoRedLeft`, `AutoRedRight` are the same file with a different class name. Alliance and starting position are not handled anywhere. Whenever you do write real auto paths, three of the four will run the wrong routine.

## Correctness issues

### 7. `autoAlignOffset` persists and grows across runs ("random" behavior)
`TeleOpMain` has `public static double autoAlignOffset = 0.0;` and does `autoAlignOffset += 0.05;` inside `runOpMode()`. A non-final `static` lives for the whole app process, so every time you INIT the OpMode the value climbs (0.05, 0.10, 0.15, ...) and is never reset. This is exactly the kind of thing that makes a robot "behave differently every match for no reason." Make it a non-static instance field, or reset it at the top of `runOpMode()`.

### 8. `Shooter.fly` is never initialized → NullPointerException
`Shooter.spinUp()` calls `fly.setVelocity(rpm)`, but `fly` is never fetched from the hardware map (there's no `init()` here). First call crashes with an NPE. Also `Shooter` extends solverslib `SubsystemBase` (a command-based dependency) while your config says `raw_linear_opmode` with no command framework — that's an inconsistent stack.

### 9. OpModes and subsystems are completely disconnected
No OpMode ever constructs `Drivetrain`, `Intake`, `Shooter`, etc. The subsystem classes are orphaned. The hardware-map names don't even agree: subsystems expect `"drivetrain0".."drivetrain3"`, but `TeleOpMain` expects `"fl"/"fr"/"bl"/"br"/"intake"/"shoot"/"climb"` and the autos expect `"drive"`. Nothing lines up with an actual robot configuration.

## Config mismatches (dead / contradictory code)

- **Turret:** `hardware/TurretController.java` drives a turret azimuth servo, but `team-config.yaml` says `turret: none`. Dead, contradictory code.
- **Pathing/localization:** `PathFollower`, `MotionProfile`, `Kinematics`, `Localizer`, `Odometry` all exist, but config says `pathing: none` and `raw_linear_opmode`. All are unused filler.
- **Unlisted subsystems:** Your config's mechanisms are intake (roller), shooter (flywheel), and mandatory parking. But the repo also carries `Deposit`, `Climber`, **and** `Hang` (two separate endgame mechanisms), plus `Vision`, `Lighting`, `Sensors` — none referenced by any OpMode and none in the config. Either they belong in the config or they should be deleted so they stop hiding the real code.

## Bottom line

Right now there is no runnable robot program here — it's a tree of stub classes full of placeholder math with a few real-looking method names. Before the weekend, the realistic minimum to compete is:

1. Add `@TeleOp` / `@Autonomous` annotations so OpModes register.
2. Fix the `init()` methods to store each motor in its own field (and set directions/zero-power behavior).
3. Write a real TeleOp loop: read gamepad, compute mecanum powers, `setPower`, `telemetry.update()`.
4. Write at least one auto that drives and parks (parking is mandatory for you), then branch it per alliance/side.
5. Initialize `Shooter.fly`; fix the `autoAlignOffset` static persistence.
6. Delete or reconcile the turret/pathing/extra-subsystem code that contradicts your config.

If you have a working version of this code elsewhere and this repo is a stale or generated copy, confirm that first — it would explain why the whole thing is placeholder. But if this is what you plan to deploy, it needs the items above before it can score (or move) at all.
