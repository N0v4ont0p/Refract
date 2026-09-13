> AUTHORED BY REFRACT: a structured summary in Refract's own words, not a copy of AndyMark material.
> Tier 2 (ecosystem partner), not a rule; verify against the BIOBUZZ manual.
> Sources (Retrieved: 2026-09-13):
> - Explainer page: https://andymark.com/pages/2026-2027-robits-starterbot-base
> - Product page (am-5832): https://andymark.com/products/robits-biobuzz-starterbot (Shopify record
>   updated 2026-09-13T00:09 -04:00)
> - Robot manual PDF: https://cdn.shopify.com/s/files/1/0644/2303/5052/files/FTC_BIOBUZZ_Robits_StarterBot_User_Manual.pdf
> - Example code (Java, re-fetched 2026-09-13; identical to the morning copy apart from line endings):
>   `RobitsStarterBotTeleop` and `RobitsStarterBotAuto` on cdn.shopify.com (links on the explainer page)
> Header says "Retrieved", not "Fetched", on purpose: `corpus-input-scan.py` treats the newest
> `Fetched:` date in a library folder as its staleness stamp.
> Season facts come from `ftc-shared-foundation/season-extensions/biobuzz-2026-27.yaml`.
> New vendor folder: the corpus had no AndyMark docs before this file.

# AndyMark Robits BIOBUZZ StarterBot, 2026-27 (summary)

Heads-up: the robot manual's cover still reads "FTC 2025-2026 DECODE". Its contents are BIOBUZZ.

## What AndyMark says it does

- Drive around the field. Acquire and store POLLEN from the floor. Launch POLLEN into the HIVE.
  Release POLLEN from FLOWERS.
- Built entirely from the Robits Core Kit (am-5000a), plus a control system and a servo programmer.
  AndyMark sells it as kit am-5832 (with battery) or am-5832_NB (without), with extras pack am-5829.
- No NECTAR handling is claimed.

## Mechanisms (robot manual + kit contents)

| Subsystem | What the sources show |
|---|---|
| Drivetrain | Simple skid-steer, belt driven (HTD belts/pulleys), external gearing so the ratio can be changed, powered 3 in omni + 3 in stealth wheels. Kit motors: 2 x NeveRest 19.2:1 (am-5442), and the Auto code's encoder math assumes NeveRest 19.2:1 on the drive. The manual lists 13.7:1 as the faster option. Swapping which wheels are omni vs stealth moves the turning center. |
| Intake | Rubber-band rollers powered by a continuous-rotation servo (needs a servo programmer). The manual calls the bands a consumable and says a second servo adds intake authority. |
| Storage ("Hopper") | Passive, gravity-fed angled ramp that indexes POLLEN from intake to launcher. "Multi game piece capacity"; **no number stated**. |
| Launcher ("Coaxial Flinger", code name `catapult`) | Elastic- or spring-powered flinger. The manual says it is a "coaxial design to allow a one motor wind and fire mechanic", runs continuously, and has an adjustable hood, tension point and cradle. Remaining kit motor: NeveRest 50.9:1 (am-5443); that it drives the launcher is Refract's inference by elimination. |
| FLOWER mechanism | Two versions. Roller: a continuous servo with a trimmed 2 in compliant wheel. Finger ("stick"): a positional servo with longer reach, but the manual warns it is more exposed to shock loads. |

## Control approach and stated constants

- TeleOp (`RobitsStarterBotTeleop`, `LinearOpMode`): open-loop, with no encoder or velocity control
  of the launcher.
  - `DriveStyle` selects `SPLIT_ARCADE` (default), `ARCADE` or `TANK`, with denominator
    normalization.
  - Left bumper runs intake roller + flower roller inward. Right bumper runs both outward.
  - Right trigger > 0 runs the catapult motor at `WIND = 0.65` power (wind and fire). Release sets 0.
  - The flower stick servo goes to `STICKIN = 0.46` on A (also the init default) and `STICKOUT = 0.65` on X.
  - Hardware-map names: `left_drive`, `right_drive`, `catapult`, `rollerI`, `rollerF`, `stick`.
- Auto (`RobitsStarterBotAuto`): static launch from the wall, either side, either alliance.
  - During init, dpad up/down sets a start delay in 1 s steps, shown in telemetry.
  - After start: the delay, then five `launch()` calls (catapult at 0.65 for 1000 ms, then off for
    500 ms), then an 18 in encoder drive forward at 0.5 with a 5 s timeout.
  - Encoder constants: `COUNTS_PER_MOTOR_REV = 537.6`, `WHEEL_DIAMETER_INCHES = 3.0`,
    `DRIVE_GEAR_REDUCTION = 1.0` ("No External Gearing"). The manual describes external drive
    gearing, so the 18 in figure is only right if that gearing is 1:1. Measure it.
  - The manual notes that feeding is timing-based and suggests adding sensors to detect POLLEN position.
- Tuning advice from the manual:
  - Start against the wall with the launcher centered on the goal. The launcher sits off to one
    side of the robot.
  - Let POLLEN settle before firing again.
  - Narrow the 4 in launcher channel to cut side-to-side motion.
  - Expect elastic fatigue; switch to springs for longer life.

## What code is published, and where

- Java and Blocks, for TeleOp and Auto, as file downloads (cdn.shopify.com) linked from the
  explainer page: `RobitsStarterBotTeleop` / `RobitsStarterBotAuto` (.java) and
  `RobitsStarterBotTeleop_Blocks` / `RobitsStarterBotAuto_Blocks` (.blk). AndyMark's own license
  header. No GitHub repository.
- Also linked: assembly guide PDF, robot manual PDF, and three CAD files (standard, alternate flower
  mechanism, mecanum). Videos: https://youtu.be/rmjtBcABNGk and https://youtu.be/HQwDTDON5I4.

## Caveats for Refract use

- The 0.65 wind power and the 1000/500 ms timing belong to this elastic flinger. Do not reuse them
  as flywheel constants.
- Drive options from the manual: swap drive motors/gears for speed vs torque, or convert to mecanum
  by adding a motor pair and shorter belts.
