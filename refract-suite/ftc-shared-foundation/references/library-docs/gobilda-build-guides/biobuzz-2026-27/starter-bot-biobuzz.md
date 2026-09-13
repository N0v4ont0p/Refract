> AUTHORED BY REFRACT: a structured summary in Refract's own words, not a copy of goBILDA material.
> Tier 2 (ecosystem partner), not a rule; verify against the BIOBUZZ manual.
> Sources (Retrieved: 2026-09-13):
> - Resource guide page: https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/
> - Assembly PDF: https://www.gobilda.com/content/user_manuals/3200-2627-0003_assembly-instructions.min.pdf
> - Example code zip: https://www.gobilda.com/content/downloads/3200-2627-0003_example-code.zip
>   (re-downloaded 2026-09-13 to a scratch directory only; byte-identical to the copy retrieved the
>   same morning; not stored in this repo)
> Header says "Retrieved", not "Fetched", on purpose: `corpus-input-scan.py` reads the newest
> `Fetched:` date per library as its staleness stamp, and a Refract summary must not move it.
> Season facts (field, elements, scoring) come from
> `ftc-shared-foundation/season-extensions/biobuzz-2026-27.yaml`, never from this file.

# goBILDA FTC StarterBot, BIOBUZZ 2026-27 (summary)

The page heading currently reads "FTC StarterBot Base Resource Guide (2026-2027 Season)". The
previous season's robot is documented in `../ftc-starter-bot-full-build.md` (DECODE, do not mix).

## What goBILDA says it does

- Mechanism list in their words: "a drop-center 6WD chassis, a GripForce Gecko Wheel intake, and a
  shooter mechanism to launch POLLEN".
- Stated capabilities: pull POLLEN out of a FLOWER straight into the intake; collect POLLEN from
  the floor, corners included; carry up to **four** POLLEN; launch up to **four** POLLEN into the
  HIVE in quick succession.
- No NECTAR handling is claimed. No autonomous capability is claimed.

## Mechanisms

| Subsystem | What the sources show |
|---|---|
| Drivetrain | Drop-center 6-wheel differential (skid-steer per the code header). Assembly PDF uses Drop-Center Bearing Plates and omni wheels. Yellow Jacket 19.2:1 (5203-2402-0019) and 50.9:1 (5203-2402-0051) motors appear in the parts list; the extracted PDF text does not assign every motor a role. |
| Intake | One DC motor driving an intake roller plus two continuous-rotation servos that, per the code comment, pull elements out of corners. 72 mm and 48 mm GripForce Gecko wheels are in the build. |
| Storage | Capacity four POLLEN (page claim). |
| Feeder | A continuous-rotation "windmill" servo (the PDF calls it the Windmill (Torque) Servo) indexes POLLEN into the launcher. |
| Launcher | A single "high-speed launcher motor" under closed-loop velocity control (code). Assembly Step 44 converts one 19.2:1 Yellow Jacket to 1:1; that this is the launcher motor is Refract's inference, not stated in the extracted text. |
| FLOWER | Handled by the intake itself (page claim); no separate mechanism named. |

## Control approach and stated constants (from `BioBuzzStarterbotTeleop.java`)

- Iterative `OpMode`, TeleOp only, single gamepad.
- Drive: arcade. Left stick Y is forward and right stick X is rotate; drive and intake motors use
  BRAKE zero-power behavior.
- Intake: power = right trigger minus left trigger, applied to the intake motor and both intake
  servos together.
- Launcher: `RUN_USING_ENCODER` with custom `PIDFCoefficients(40, 0, 0, 12.5)`
  (P=40, I=0, D=0, F=12.5). Holding the right bumper commands `LAUNCHER_TARGET_VELOCITY = 1250`
  ticks/s. Releasing it commands 0.
- Feed gate: the windmill servo runs at full power, and the intake gets +0.5 power, only while the
  bumper is held **and** measured velocity is above `LAUNCHER_MIN_VELOCITY = 1200` ticks/s.
- The code comment says goBILDA motors have 28 encoder ticks per motor revolution, so 1250 ticks/s
  is about 2,680 RPM at the motor (Refract arithmetic: 1250 / 28 x 60).
- Hardware-map names: `left_drive`, `right_drive`, `intake`, `launcher`, `windmill`,
  `left_intake_servo`, `right_intake_servo`.

## What code is published, and where

- One Java file, `BioBuzzStarterbotTeleop.java` (MIT license, Base 10 Assets, LLC), inside the
  example-code zip above. No Blocks file and no autonomous OpMode in the zip.
- No GitHub repository is linked.
- Also on the page: STEP CAD zip (https://www.gobilda.com/content/step_files/3200-2627-0003.zip,
  not downloaded) and the assembly PDF.

## Build inputs and variants

- Needs the 2026-2027 FTC Starter Kit (3200-4008-2627), or the FTC Starter Kit Upgrade Pack
  (3200-0101-2627) on top of a 2025-26 kit, plus a REV Control Hub.
- Teams that built the summer "StarterBot Base" can start at Step 41 (page 24) of the assembly PDF.
- Mecanum version: https://www.gobilda.com/ftc-starterbot-base-with-mecanum-wheels-resource-guide-2026-2027/
  (linked, not summarized here).

## Caveats for Refract use

- Velocity targets are tuned for goBILDA's geometry and launch spot. They say nothing about what
  a HIVE CELL needs. The TIP calibration target is in the season yaml (`field.hive.tip_threshold`).
- The feed gate checks only a lower bound (velocity above MIN), not a window.
