> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/example-repos.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Example Repos
---

Here are some example repositories that use Ivy. Each link below
points to a specific file that demonstrates Ivy usage. 

## #365 MOE

[GitHub Repository](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode)

- [Auto.java](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/Auto.java) — autonomous using lots of compositions and Pedro commands
- [Tele.java](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/Tele.java) — teleop example
- [IntakingState.java](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/states/IntakingState.java) — example usage within a finite state machine

## #12649 Code Blooded

[GitHub Repository](https://github.com/BeepBot99/CodeBloodedDecodeV2)

- [RobotOpMode.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/robot/RobotOpMode.java) — base OpMode class that integrates the Scheduler
- [Intake.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/subsystems/Intake.java) — subsystem defining commands with `Commands.*`
- [Turret.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/subsystems/Turret.java) — subsystem using `Commands.infinite` for continuous control
- [BlueClose15Full.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/BlueClose15Full.java) — autonomous OpMode scheduling command sequences
- [CompetitionTeleOp.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/opmodes/teleop/CompetitionTeleOp.java) — teleop OpMode scheduling commands from subsystems

## #22131 Traffic Cones

[GitHub Repository](https://github.com/BaronClaps/22131-Decode)

- [CommandOpMode.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/command/CommandOpMode.java) — base OpMode class wrapping the Scheduler
- [Robot.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/Robot.java) — central robot class building commands with `CommandBuilder`
- [Intake.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/subsystem/Intake.java) — subsystem defining commands with `Commands.*`
- [Shooter.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/subsystem/Shooter.java) — subsystem using `CommandBuilder` and `Commands`
- [Auto15.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmode/auto/Auto15.java) — autonomous OpMode using `Groups.sequential` and `PedroCommands`
