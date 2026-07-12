# Pre-Competition Sanity Check — Team 45021

Short version: **this code is not competition-ready, and it's not close.** I know that's not what you want to hear two days out, but a "sanity check" that told you otherwise would be doing you a disservice. As written, this robot will not drive, autonomous does nothing, and none of the subsystems actually keep the motors they grab. Below is the honest breakdown, ordered by how badly it will hurt you at the event.

I looked at all 23 files (every subsystem, every control class, all 5 opmodes, and `team-config.yaml`).

---

## Blocking issues (robot does not function)

### 1. No opmode will appear on the Driver Station — missing registration annotations
`TeleOpMain`, `AutoBlueLeft`, `AutoBlueRight`, `AutoRedLeft`, `AutoRedRight` are all plain `LinearOpMode` subclasses with **no `@TeleOp` / `@Autonomous` annotation**. Without those, the SDK never lists them, so you literally cannot select and run any of them at the field. This alone makes the robot inoperable in a match.

### 2. Every subsystem throws away all but one of its motors
Every subsystem has the same copy-paste bug. Example, `Drivetrain.init()`:
```java
private DcMotor a, b;
public void init(HardwareMap hw) {
    a = hw.get(DcMotor.class, "drivetrain0");
    a = hw.get(DcMotor.class, "drivetrain1");
    a = hw.get(DcMotor.class, "drivetrain2");
    a = hw.get(DcMotor.class, "drivetrain3");
}
```
All four handles are assigned to the **same field `a`**, so only the last one (`drivetrain3`) survives; `drivetrain0/1/2` are fetched and discarded. `b` is declared but never assigned. Same pattern in `Intake`, `Deposit`, `Climber`, `Hang`, `Vision`, `Odometry`, `Sensors`, `Lighting`. For a mecanum drive you need to hold all four motors — right now you hold one. This is the single most repeated defect in the repo.

### 3. Nothing in any opmode actually controls the robot
- `TeleOpMain` fetches `fl, fr, bl, br, intake, shoot, climb` as `hardwareMap.get(Object.class, ...)` — generic `Object`, not motors. It never reads a gamepad, never sets a motor power, and never instantiates any of the subsystem classes. The entire loop body is 360 `telemetry.addData` lines and nothing else. The robot will sit still.
- All four autos fetch a single `Object` named `"drive"`, then just push 40 `telemetry` lines and exit. No movement, no parking.

### 4. Autonomous does not park — and parking is mandatory
`team-config.yaml` has `endgame_parking: mandatory`. None of the four autos move the robot at all, so you score zero auto/parking points. (See also #8 — the four autos are byte-for-byte identical, so there is no red/blue or left/right behavior either.)

### 5. `Shooter` will crash the instant you use it
```java
private DcMotorEx fly;                       // never assigned
public void spinUp(double rpm){ fly.setVelocity(rpm); }
```
There is no `init()` that does `fly = hw.get(...)`, so `fly` is `null` → `NullPointerException` on first `spinUp()`. Separately, `setVelocity()` expects **encoder ticks per second, not RPM**; passing a raw RPM number will spin the flywheel to the wrong speed even after you fix the null. Note also `Shooter` imports `com.seattlesolvers.solverslib` (SolversLib command framework), which nothing else in the project uses and which your config doesn't list — that's an odd, isolated dependency.

---

## Serious issues

### 6. Hardware config names are inconsistent across the codebase
Three different naming schemes for the same hardware:
- Subsystems: `"drivetrain0..3"`, `"intake0/1"`, `"deposit0/1"`, `"shoot"`-implied, etc.
- `TeleOpMain`: `"fl"`, `"fr"`, `"bl"`, `"br"`, `"intake"`, `"shoot"`, `"climb"`.
- Autos: `"drive"`.

At most one of these can match the names in your Robot Controller configuration. Any name that doesn't match throws at `init` and aborts the opmode. Pick one canonical set and make the RC config, the subsystems, and the opmodes all agree.

### 7. `autoAlignOffset` is mutable static state that persists (and drifts) across runs
```java
public static double autoAlignOffset = 0.0;
...
autoAlignOffset += 0.05;   // runs once every time the opmode INITs, never reset
```
Because it's a non-final `static`, its value survives from one opmode run to the next within the same app session, and it grows `+0.05` every time you re-init. If you ever wire it into aiming/driving, the robot behaves slightly differently every match "for no reason," and worse after you've re-inited a few times in the pits. Make it an instance field (reset every run), or reset it in `runOpMode()` before use.

### 8. The four autonomous opmodes are identical
`AutoBlueLeft`, `AutoBlueRight`, `AutoRedLeft`, `AutoRedRight` are literally the same code. Four separate files that do the same (nothing) — no alliance or start-position logic. Even once they do something, this is four copies to keep in sync.

---

## Dead / placeholder code (won't fail inspection, but there's no real logic here)

Every "logic" method in the repo is filler that computes a fixed multiple of its input and returns it — it does not do what its name says and **nothing calls any of it**:
- `control/PIDController.java` — `step0..15` are not a PID; they're `Σ e*n/k`. No P, I, or D, no setpoint, no clamp.
- `control/FeedForward`, `Filters`, `Kinematics`, `Localizer`, `MotionProfile`, `PathFollower` — same filler shape, all unused.
- `Shooter.ff()`, `TurretController.solveLead()`, and every `computeN()` in the subsystems — filler, unused.

Two of these also contradict your config:
- `control/PathFollower.java` exists but `pathing: none` — dead.
- `hardware/TurretController.java` exists but `turret: none`. Its `azimuth` servo is never initialized (same null-crash risk as Shooter), and `pointAt(headingDeg)` maps 0–360° linearly to a 0–1 servo position, which a standard 180°/300° servo can't physically do. Since you have no turret, delete this file.

`subsystems/Deposit.java` also doesn't correspond to anything in your season-mechanism config (intake + shooter). If there's no deposit on the robot, drop it.

---

## What I'd actually do with the time you have

You're rushed, so triage rather than polish:

1. **Add annotations** (`@TeleOp`, `@Autonomous`) to all five opmodes — otherwise you can't run anything. (#1)
2. **Fix the motor init** in at least `Drivetrain` (assign the four motors to four distinct fields), plus any subsystem you actually run. (#2)
3. **Write real teleop drive**: get the four drive motors as `DcMotor`, read `gamepad1` sticks, set mecanum powers. Right now there is zero drive code. (#3)
4. **Reconcile hardware names** between the RC config and the code so `init` doesn't throw. (#6)
5. **Give auto a parking move** so you're not leaving mandatory points on the table. (#4)
6. **Fix or stub `Shooter`** so it initializes `fly` and doesn't NPE, and convert RPM→ticks/s. (#5)
7. Delete the dead/contradicting files (`TurretController`, `PathFollower`, unused control classes, `Deposit` if not on the robot) so they don't distract you during a pit debug. (#9-ish / cleanup)

I'd honestly focus on 1–4 first — those are the difference between "robot moves and can be driven" and "robot does nothing at the field." The rest is upside once the basics work.

Happy to write the corrected `Drivetrain`, a minimal working `TeleOpMain`, and a park-only auto if you want them — say the word and I'll draft them.
