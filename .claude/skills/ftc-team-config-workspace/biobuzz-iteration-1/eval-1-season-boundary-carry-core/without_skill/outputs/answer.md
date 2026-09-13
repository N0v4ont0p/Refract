Happy kickoff! I read your DECODE config. Before I write any BIOBUZZ code, we need to redo part of it. Here's why, and the questions I need answered first.

## 1. What this file is
- The header says `season: decode-2025-26` and `fixture: true`, and the team number 99901 looks made up. The file even calls itself a "synthetic config". So either it's a test file or someone reused a template. **I can't treat it as your real robot until you confirm it.**
- It contradicts itself. `archetypes: [fixed_shooter_on_swerve]` says the shooter is fixed, but `turret: single_axis` says it turns. One of them is wrong.
- `tuning_status: untuned` with no values saved. Even the DECODE numbers (swerve steering PID, flywheel speed gains, Pedro Pathing gains) aren't recorded, so nothing tuned carries over.

## 2. What probably carries over (please confirm each one)
| Item | Last season | Why I'm asking |
|---|---|---|
| Drivetrain | 4-module custom swerve | Are you keeping it, or rebuilding for the new field? |
| Hubs | Control Hub + 1 Expansion Hub | Same port layout? The hardware map follows from it. |
| Vision | Limelight 3A | Same camera and mount? AprilTag pipelines need redoing either way. |
| Odometry | goBILDA Pinpoint | Same pod offsets? |
| Pathing | Pedro Pathing | Are you staying on it? Which version? |
| Code style | FTCLib command-based | FTCLib gets few updates now. Some teams moved to SolversLib (a fork) or NextFTC. Staying or switching? |
| Fabrication | CNC aluminum/carbon | Affects nothing in code. |

Also: when did you last update the FTC SDK and your libraries? Start the season on the new SDK release before writing code.

## 3. What does NOT carry over
Every `season_mechanisms` entry was written for DECODE: roller intake, flywheel, turret, gate `none`, classifier `none`, parking `mandatory`. "Classifier" and "gate" are DECODE field elements, and the parking rule was a DECODE rule. **I'm clearing all of these.**

FIRST says BIOBUZZ uses Pollen, plastic balls about 3 in. across that behave much like DECODE's Artifacts. So a roller intake, flywheel and turret *might* make sense again. But that is a guess based on the ball, not a design. I haven't checked the BIOBUZZ manual, so I'm not assuming anything about scoring goals, endgame, size limits, or whether a turret or swerve is still worth it. Anything that depends on the rules should be checked against the actual manual and Team Updates before we build.

## 4. Questions I need answered (and what each answer changes)
1. **Is this your real team config, and what's your team number?** If yes, I keep the carry-over items as drafts to confirm. If it's a template, we start from scratch and I ask about the drivetrain and hubs first.
2. **Are you keeping the 4-module swerve?** If yes, I scaffold the swerve drive subsystem with blank tuning values. If you switch to mecanum or tank, the drive code is completely different.
3. **Same hubs, Limelight 3A and Pinpoint, with the same ports and mounting?** If yes, I reuse the hardware-map names. If not, I list the new devices before writing the hardware map.
4. **Staying on Pedro Pathing and FTCLib command-based, or switching (SolversLib, NextFTC, Road Runner)?** This decides how every subsystem and OpMode is structured, so it's the one answer I can't work around.
5. **What mechanisms has your team picked for BIOBUZZ?** Intake type, how you score Pollen (flywheel, arm, something else), turret or fixed, and any endgame mechanism. Each confirmed mechanism becomes one subsystem. Anything still "undecided" gets no code yet, so I don't build a guess you'll have to throw away.
6. **Was last season's shooter fixed or on a turret?** This only fixes the history. If you're reusing the old shooter, it decides whether I bring back turret aiming code.
7. **Do you have any real tuning numbers written down** (swerve steering PID and angle offsets, flywheel speed gains, Pedro gains)? If yes, I record them as "measured, needs re-checking". If no, every field starts blank and your first tasks are tuning OpModes.

## 5. What happens after you answer
I rewrite the config for `biobuzz-2026-27` with every field marked confirmed or unconfirmed and show it back to you. Once you approve it, the first code will be a drivetrain-only TeleOp plus a hardware-map and Pinpoint/Limelight test OpMode. That code works whatever game mechanisms you choose, so you can drive on day one. Mechanism subsystems come once your design is decided. Until then I'm not generating robot code, and I haven't changed any files.

Sources:
- [BIOBUZZ Game & Season | FIRST Tech Challenge](https://www.firstinspires.org/programs/ftc/game-and-season)
- [2026-2027 BIOBUZZ resources](https://ftc-resources.firstinspires.org/ftc/archive/2027)
- [Game Preview 2027: StarterBots, Skill Builders, Field Elements](https://community.firstinspires.org/game-preview-field-elements)