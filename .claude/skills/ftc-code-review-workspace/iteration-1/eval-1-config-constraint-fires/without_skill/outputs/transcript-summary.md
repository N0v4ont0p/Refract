# Transcript summary — how the review was done

## Files read
- `team-config.yaml` — confirmed config: rookie team, mecanum drivetrain, raw LinearOpMode style, pathing none, stock goBILDA/REV fab, intake=roller, shooter=flywheel, **turret=none**, gate=none, classifier=none, **endgame_parking=mandatory**.
- `TeamCode/MainTeleOp.java` — the only OpMode. 316 lines, almost all of it filler `telemetry.addData("vN", N)` lines (14–313).
- `TeamCode/Shooter.java` — 5 lines; `extends SubsystemBase` from `com.seattlesolvers.solverslib.command` (SolversLib command-based); empty `spinUp()`.
- `TeamCode/TurretAimer.java` — 5 lines; `aimTurret(double heading)` stub.

## Commands run
- `find . -type f` + `ls -la` — enumerated project: `team-config.yaml`, three files under `TeamCode/`. No Autonomous OpMode, no build files present in tree.
- `grep -rn "TurretAimer"` → only its own declaration. Confirmed **unused / dead code**.
- `grep -rn "Shooter"` → only its own declaration. Confirmed **never instantiated by MainTeleOp**.
- `grep -rn "@TeleOp\|@Autonomous\|@Disabled"` → **no matches**. Basis for finding #1 (OpMode won't register on Driver Station).
- `grep -n "while\|opModeIsActive\|for ("` in MainTeleOp → **no matches**. Basis for finding #2 (no main control loop).
- `grep -rn "flywheelOffset"` → declared line 4, written line 12, read nowhere. Basis for finding #4.

## How each finding was reached
1. **No @TeleOp** — grep for OpMode annotations returned nothing; the SDK only lists annotated OpModes, so it can't be selected at the field. Blocking.
2. **No control loop** — grep for `while`/`opModeIsActive`/`for` in MainTeleOp returned nothing; `runOpMode()` prints telemetry once after `waitForStart()` and returns. Robot does nothing, OpMode ends immediately. Blocking.
3. **Hardware unused / wrong type** — read lines 6–11: six devices fetched with `hardwareMap.get(Object.class, ...)` (not a hardware type), and grep/read confirmed none are referenced again. No drive/intake/shooter logic exists. Blocking.
4. **Persistent static state** — `public static double flywheelOffset`, non-final, written from `runOpMode()` (a lifecycle method). Static fields survive across OpMode runs on the Robot Controller → classic intermittent-behavior anti-pattern. Currently benign (reset each run) but flagged. Medium.
5. **TurretAimer vs config** — config `turret: none`; file implements turret aiming and is unreferenced (grep). Dead + contradicts confirmed config. Medium.
6. **Shooter stack mismatch** — config `opmode_style: raw_linear_opmode`, `pathing: none`; file extends SolversLib `SubsystemBase` (command-based framework), is never used, and `spinUp()` is empty. Architecture mismatch + dead scaffolding + unused dependency. Medium.

## Additional gap noted (not a code finding)
- Config says `endgame_parking: mandatory` but there is **no Autonomous OpMode** anywhere in the project. Flagged in the review as something to confirm.
