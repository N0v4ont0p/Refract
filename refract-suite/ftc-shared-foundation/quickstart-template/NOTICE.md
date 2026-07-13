# NOTICE

This template is derived from **FTCLib/FTCLib-Quickstart**
(https://github.com/FTCLib/FTCLib-Quickstart), fetched as a shallow clone at
commit `c73ff8ba3b20aa3aca2b364e15153073a6cd30c2` (committed 2023-08-09,
fetched 2026-07-12). It is itself the official FIRST FTC SDK app template
with FTCLib added as a Gradle dependency -- not an FTCLib-original repo.

## License

FTCLib-Quickstart's `LICENSE` file is FIRST's own BSD-3-Clause-style SDK
license (copyright FIRST, 2014-2022), **not** FTCLib's own MIT license. It
reads, verbatim:

> Copyright (c) 2014-2022 FIRST.  All rights reserved.
>
> Redistribution and use in source and binary forms, with or without
> modification, are permitted (subject to the limitations in the disclaimer
> below) provided that the following conditions are met:
>
> Redistributions of source code must retain the above copyright notice,
> this list of conditions and the following disclaimer.
>
> Redistributions in binary form must reproduce the above copyright notice,
> this list of conditions and the following disclaimer in the documentation
> and/or other materials provided with the distribution.
>
> Neither the name of FIRST nor the names of its contributors may be used to
> endorse or promote products derived from this software without specific
> prior written permission.
>
> NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
> THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
> CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
> NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
> PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
> CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
> EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
> PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
> OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
> WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
> OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
> ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Separately: the FTCLib *library itself* (`org.ftclib.ftclib:core`,
`org.ftclib.ftclib:vision`, pulled in as ordinary Gradle dependencies, not
vendored into this template) is MIT-licensed by the FTCLib project
(`com.arcrobotics.ftclib.*` classes referenced throughout this template --
`CommandOpMode`, `SubsystemBase`, `Motor`, `MotorGroup`, `SimpleServo`,
`MecanumDrive`, `GamepadEx`, etc.). Two different licenses apply to two
different things: the quickstart *scaffold* FIRST publishes (BSD-3-Clause-
style, above) versus the FTCLib *library* it depends on (MIT, upstream at
https://github.com/FTCLib/FTCLib). Neither license text is reproduced here
in full for FTCLib's MIT license since no FTCLib source was copied into this
template -- only its published Maven coordinates are referenced, the normal
way any Gradle dependency is used.

## What was carried over verbatim / near-verbatim (convention, not code copy)

- Package root `org.firstinspires.ftc.teamcode` and the `TeamCode` module
  Gradle wiring (`apply from: '../build.common.gradle'` /
  `'../build.dependencies.gradle'`, `implementation project(':FtcRobotController')`,
  the `OpModeAnnotationProcessor.jar` annotation processor).
- The FTCLib Maven coordinates (`org.ftclib.ftclib:core:2.1.1`,
  `org.ftclib.ftclib:vision:2.1.0`) and the FTC Dashboard coordinate
  (`com.acmerobotics.dashboard:dashboard:0.4.10`).
- The FTCLib command-based idiom itself: `CommandOpMode` as the OpMode base,
  `SubsystemBase` for hardware-owning classes, FTCLib's `Motor`/`MotorGroup`/
  `SimpleServo`/`RevIMU` hardware wrappers in place of raw SDK `DcMotor`/
  `Servo`. Upstream's own example is `TeamCode/.../AutonomousOpMode.java` +
  `subsystems/DriveSubsystem.java`.
- The FTC Dashboard `@Config` tunable-constants idiom, from upstream's
  `DriveConstants.java` -- carried into this template's `RobotConstants.java`
  with an added caveat comment (see that file) about the mutable-static-state
  failure mode `@Config` does not by itself prevent.

## What was adapted (this template's actual contribution)

None of the following exists in upstream FTCLib-Quickstart, which ships
exactly one example subsystem (`DriveSubsystem`, differential-drive-shaped,
used from one `AutonomousOpMode`) and no per-mechanism structure, no
telemetry-by-default wiring, and no documentation scaffolding:

- The interface-based restructuring itself -- `Drivetrain` / `Shooter` /
  `Turret` / `Intake` as the unit of architecture, each with an example
  concrete implementation (`MecanumDrivetrain`, `FlywheelShooter`,
  `SingleAxisTurret`, `RollerIntake`) chosen to match this season's actual
  mechanism options (`season-extensions/decode-2025-26.yaml`).
- `opmodes/TeamOpMode.java`: a base OpMode class that seals FTCLib's
  `CommandOpMode.initialize()`/`run()` so telemetry wiring can't be skipped
  or bypassed, and so there's no override point left for mechanism logic to
  accumulate in.
- `telemetry/RobotTelemetry.java` and the "telemetry on by default, not
  opt-in" wiring through `TeamOpMode` -- upstream has no telemetry scaffolding
  at all.
- `design-decision-log.md` and this `NOTICE.md`/README's documentation
  scaffolding -- upstream ships only its own generic `readme.md` explaining
  how to copy sample OpModes from `FtcRobotController`.

## Deviations from design-notes.md's original intent

None. Studying the real upstream repo did not force a change to the
design-notes.md requirements (telemetry-on-by-default, engineering-notebook
docs, interface-based Drivetrain/Shooter/Turret/Intake architecture) -- it
confirmed there was nothing upstream to reuse for the interface layer or the
telemetry-by-default wiring (both had to be built from scratch), while the
Gradle/package/command-based-framework conventions above carried over
directly.
