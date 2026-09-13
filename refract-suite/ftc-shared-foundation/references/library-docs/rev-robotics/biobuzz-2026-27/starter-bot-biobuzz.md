> AUTHORED BY REFRACT: a structured summary in Refract's own words, not a copy of REV material
> (the verbatim REV mirror convention in `../ftc-kickoff-concepts/` does not apply to this file).
> Tier 2 (ecosystem partner), not a rule; verify against the BIOBUZZ manual.
> Sources (Retrieved: 2026-09-13, publisher `.md` endpoints; changelog v1.0.0 dated 9/12/2026):
> - https://docs.revrobotics.com/ftc-kickoff-concepts/home/2026-27-rev-duo-ftc-starter-bot.md
> - https://docs.revrobotics.com/ftc-kickoff-concepts/home/bill-of-materials.md
> - https://docs.revrobotics.com/ftc-kickoff-concepts/home/programming-teleop-and-auto.md
>   plus its sub-pages `programming-overview`, `programming-subsystems`, `programming-flywheel`,
>   `programming-onbot-java-overview`, `programming-auto`
> - https://docs.revrobotics.com/ftc-kickoff-concepts/home/upgrades.md, `build-tips-and-tricks.md`,
>   `starter-bot-changelog-2026-27.md`
> - https://www.revrobotics.com/duo/ftc-starter-bot/ (product landing page)
> Header says "Retrieved", not "Fetched", on purpose: `corpus-input-scan.py` reads the newest
> `Fetched:` date per library as its staleness stamp, and a Refract summary must not move it.
> Season facts come from `ftc-shared-foundation/season-extensions/biobuzz-2026-27.yaml`.

# REV DUO FTC Starter Bot, BIOBUZZ 2026-27 (summary)

The previous season's REV robot is mirrored in `../ftc-kickoff-concepts/decode-2025-26/` (DECODE, do
not mix). REV's BIOBUZZ pages sit under `ftc-kickoff-concepts/home/`, not a season-named folder.

## What REV says it does

- Collects POLLEN from the floor and launches it into the HIVE. A servo-driven "poker" combs
  POLLEN out of FLOWERS.
- TeleOp includes an automatic launch sequence. Auto launches preloads and can start from either side.
- No NECTAR handling is claimed. Storage capacity is **not stated**.

## Mechanisms (configuration table + mechanism BOM)

| Subsystem | Hardware | Config name |
|---|---|---|
| Drivetrain | 2 HD Hex motors (config type: UltraPlanetary HD Hex), #25 chain with 10T sprockets, 90 mm grip, traction and omni wheels (2 each in the full BOM). The 2026-27 build guide PDF (Drivetrain Assembly, p.49) lists 2 x 20:1 UltraPlanetary Gearbox and HD Hex Motor; the web BOM's per-mechanism rows list bare HD Hex motors instead, so trust the build guide. | `leftDrive` (M0), `rightDrive` (M1, reversed) |
| Intake | Core Hex motor, chain (20T sprockets), 8 x 40A Intake Flaps, 2 mm polycarbonate | `intakeMotor` (M2) |
| Feeder | Smart Robot Servo V2 in continuous mode, 60T plastic gears, 1 in soft grip wheels | `crServo` (S0) |
| Launcher | Flywheel: HD Hex motor without gearbox (build guide: 1:1 output), 13T pinion, 90T plastic gears, 2 x 90 mm grip wheels; polycarbonate chute/hood (product page) | `flywheel` (M3, `RUN_USING_ENCODER`) |
| FLOWER "poker" | Smart Robot Servo V2 on an aluminum double servo arm, two preset positions | `pollenServo` (S1) |

Built from FTC Starter Kit V3.1 (REV-45-3529), DUO Control Bundle (REV-35-2709) and a 2 mm
polycarbonate grid sheet (REV-41-7537). Kits bought before summer 2025 need extra 5 mm hex bearing
blocks (build-tips page).

## Control approach and stated constants

- `LinearOpMode`, one gamepad. The loop is split into functions: `intakeControls`, `pollenPoker`,
  `arcadeDrive`, `flywheelControls`. Telemetry shows flywheel velocity.
- Flywheel uses the SDK's built-in velocity PID (no custom PIDF). `targetVelocity = 1160`,
  set with `DcMotorEx.setVelocity`, which takes ticks/s by default. REV describes it as the speed
  for launching from near the field perimeter.
- TeleOp mapping: Y spins the flywheel only. X reverses the flywheel at power -0.55. Holding the left bumper runs the
  auto sequence: spin to target, and run feeder servo + intake at full power only while velocity is
  within **+/-20** of target, otherwise stop them. Right bumper intakes, right trigger outtakes.
  Dpad up/down drives the feeder manually. A sets the poker down (0), B sets it up (1). The poker
  is set to 1 when Play is pressed.
- Auto (`REVStarterBotJavaAuto2026`): optional commented-out `sleep(10000)`. Then drive both sides at
  -0.25 for 700 ms (the robot starts intake-first against the wall, so it backs away). Then, for 15 s,
  hold `targetVelocity` and feed while velocity is within **+/-50**. REV says the delay lets a robot
  wait on the low side of the HIVE until the partner has launched and shifted the HIVE up.
- REV's text says the ranges, 700 ms and 15 s need tuning per robot and launch spot.

## What code is published, and where

- Blocks and OnBot Java, for TeleOp and Auto, as GitBook file attachments on the
  programming-teleop-and-auto page. There is also a robot configuration file download.
- The OnBot Java TeleOp (`REVStarterBotJava2026`) and Auto are printed on the
  `programming-onbot-java-overview` page.
- Upgrades page: split-arcade and dual-gamepad program variants. "Mecanum Drive" and
  "Upgrading Preview Bot to Starter Bot" are marked coming soon.
- CAD (Onshape): https://cad.onshape.com/documents/9cb9eb90e973fd37d10ee178/w/b9c02b0f4e09998f08becbd2/e/a55c018c62564f3ea8812a47
- Build guide PDF: https://www.revrobotics.com/content/technical-resources/DUO/FTC-Kickoff-Concepts/2026-27/2026-27_REV_DUO_FTC_Starter_Bot-Build_Guide_1567.pdf
- No GitHub repository.

## Inconsistencies in REV's own pages (as retrieved)

- Drive style: "Gamepad Setup" calls split arcade the default. The gamepad table, the subsystems
  page and the code use single-stick arcade (left stick), and split arcade is offered as an upgrade.
  The code is the thing that runs.
- Auto: the intro says the robot "move[s] forward", and a code comment says "drives forward", but
  the code applies negative power to back away from the wall.
- The BOM page intro still says "2025-26 REV DUO Starter Bot".
- The poker is described as on the side of the robot, while a code comment says front.
