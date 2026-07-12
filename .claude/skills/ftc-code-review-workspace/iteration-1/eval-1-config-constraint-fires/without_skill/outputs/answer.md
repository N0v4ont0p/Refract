# Robot code review — pre-competition sanity check

Team 12345 (rookie) · mecanum · raw LinearOpMode · intake (roller) + shooter (flywheel) · no turret · parking mandatory

Short version: this will not work at competition as written. `MainTeleOp` won't even show up on the Driver Station, and even if it did, the robot does nothing. There are a few blocking issues to fix before this weekend, plus some cleanup. Details below, most important first.

---

## Blocking — fix before you compete

### 1. `MainTeleOp` has no `@TeleOp` annotation → it won't appear on the Driver Station
`TeamCode/MainTeleOp.java` has no `@TeleOp` (or `@Autonomous`) annotation. The FTC SDK only lists OpModes that carry one of those annotations. As written, you will not be able to select this OpMode at the field — there is nothing to run.

Fix: add above the class declaration:
```java
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

@TeleOp(name = "Main TeleOp")
public class MainTeleOp extends LinearOpMode {
```

### 2. There is no main control loop → the robot does nothing, then the OpMode ends
After `waitForStart()` the code prints telemetry once and `runOpMode()` returns. There is no `while (opModeIsActive()) { ... }` loop, so:
- the OpMode ends the instant the match starts,
- no gamepad input is ever read,
- no motor is ever commanded.

Every TeleOp needs a loop that reads the gamepads and drives the hardware. Skeleton:
```java
waitForStart();
while (opModeIsActive()) {
    // read gamepad1, compute mecanum powers, set motor powers, run intake/shooter
    telemetry.update();
}
```

### 3. Hardware is fetched as `Object.class` and never used → nothing is actually wired
Lines 6–11 do:
```java
var fl = hardwareMap.get(Object.class, "fl");   // and fr, bl, br, intake, shoot
```
Two problems:
- `Object.class` is not a hardware type. These need to be the real SDK types (`DcMotor`/`DcMotorEx` for the four drive motors, the intake, and the shooter flywheel), or you get no usable device handle and no way to command it.
- Even so, none of `fl/fr/bl/br/intake/shoot` are referenced anywhere after they're fetched. There is **zero** drive code, **zero** intake code, and **zero** shooter code in the OpMode.

Fix (typical mecanum setup):
```java
DcMotor fl = hardwareMap.get(DcMotor.class, "fl");
DcMotor fr = hardwareMap.get(DcMotor.class, "fr");
DcMotor bl = hardwareMap.get(DcMotor.class, "bl");
DcMotor br = hardwareMap.get(DcMotor.class, "br");
DcMotor intake = hardwareMap.get(DcMotor.class, "intake");
DcMotor shoot  = hardwareMap.get(DcMotor.class, "shoot");
```
then, inside the loop, actually compute mecanum powers from `gamepad1` and set them, plus intake/shooter controls. Remember to reverse one side of the drivetrain and confirm each motor spins the correct direction on the actual robot before you trust it.

> Net effect of 1–3: as it stands there is no runnable, functioning TeleOp. This is the thing to spend your time on before the event. Get a basic drive + intake + shooter loop working and test it on the real robot.

---

## Should fix — cleanup and config mismatches

### 4. `public static double flywheelOffset` is persistent cross-OpMode state
```java
public static double flywheelOffset = 0.0;   // line 4
flywheelOffset = 0.25;                        // line 12, written from runOpMode()
```
A non-final `public static` field lives on the loaded class, not on the OpMode instance, so its value survives between OpMode runs on the Robot Controller. Today you happen to reset it to `0.25` at the top of every run so it's harmless — but this is exactly the pattern that later produces "the robot behaves differently for no reason" bugs, where a value left over from a previous run leaks into the next. Make it a normal instance field (`double flywheelOffset = 0.25;` inside `runOpMode`) unless you have a specific reason to share it, and if you do, `static final` for a true constant.

### 5. `TurretAimer.java` exists but your config says you have no turret
`TeamCode/TurretAimer.java` implements turret-aiming logic, but your confirmed config is `turret: none`, and nothing in the project references the class. It's dead code for a mechanism the robot doesn't have. Delete it so it can't confuse inspection or a future teammate. If you *do* have a turret, then the config is wrong — but based on what you told me, this file shouldn't be here.

### 6. `Shooter.java` uses a command-based library that doesn't match your stack, and is never used
`TeamCode/Shooter.java` extends `SubsystemBase` from SolversLib (`com.seattlesolvers.solverslib.command`), a command-based framework. Your confirmed software stack is `raw_linear_opmode` with `pathing: none`. Mixing a command-based subsystem into a raw LinearOpMode project is an architecture mismatch, and on top of that:
- `Shooter` is never instantiated or referenced by `MainTeleOp`,
- its only method `spinUp()` is empty.

So right now it's dead, empty scaffolding that also pulls in a library dependency you otherwise aren't using. For a rookie team on raw LinearOpMode, the simplest path is to delete this and control the flywheel directly in the TeleOp loop (set `shoot` motor power on a button). If you deliberately want to adopt SolversLib command-based, that's a bigger decision to make as a team — don't half-adopt it right before a competition.

---

## Not seen — worth confirming yourself
- **Autonomous / parking.** Your config lists `endgame_parking: mandatory`, but there is no Autonomous OpMode in the project at all. If parking (or any auto) matters for your match plan, that code doesn't exist yet.
- **On-robot testing.** None of the above substitutes for driving the actual robot. Once you have a working loop, confirm motor directions, that the intake and shooter spin the right way, and that nothing browns out.

## Bottom line
This is not competition-ready yet. The core TeleOp needs an `@TeleOp` annotation, a real control loop, and real hardware types + drive/intake/shooter logic (items 1–3) — without those the robot literally does nothing. Then delete the turret and Shooter files that don't match your setup (5, 6) and fix the static field (4). Prioritize getting a basic tested drive-and-shoot loop running on the real robot before this weekend.
