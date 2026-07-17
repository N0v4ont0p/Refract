> Source: https://raw.githubusercontent.com/FTCLib/FTCLib-Docs/v2.1.0/features/drivebases.md · Fetched: 2026-07-17
> Note: docs.ftclib.org (GitBook) returned HTTP 403 to automated fetch tools; content below is
> pulled from the FTCLib-Docs GitHub source at tag v2.1.0 — same discipline as this corpus's other
> FTCLib files.
> Completeness-audit addition: a real, GitHub-confirmed 49-file FTCLib docs tree exists; this
> corpus stored only the command-framework subset (fully complete) plus geometry/control/
> gamepad-triggers/hardware-wrappers before this pass. This is the highest-value single remaining
> gap — FTCLib's own drivebase abstraction classes, directly relevant to drivetrain code
> generation. Remaining known gaps (kinematics/odometry.md + the 6 wpilib-kinematics files,
> features/trajectory.md + its 6 sub-pages, features/pure-pursuit.md, features/util.md,
> features/commands.md, vision/* — season-specific detection, likely deliberately out of scope) are
> logged, not silently dropped.

# FTCLib — Drivebases

All FTCLib drivebase classes extend the abstract `RobotBase`, which provides shared functionality
(motor-type enumeration, speed normalization, input handling) across every concrete drivebase type
below.

## Differential drive

Two motor groups, one per side. Two control schemes:

```java
m_drive.arcadeDrive(forwardSpeed, turnSpeed);   // one stick: forward speed + turn
m_drive.tankDrive(leftSpeed, rightSpeed);        // each stick drives its own side
```

## Holonomic drive (H-Drive)

Omnidirectional movement, several wheel-configuration variants:

- **Three-wheel (Kiwi/Killough)** — three omniwheels at different angles:
  `HDrive kiwi = new HDrive(left, right, slide);`
- **X-Drive** — four omniwheels in an X pattern:
  `HDrive xDrive = new HDrive(frontLeft, frontRight, backLeft, backRight);`
- **Mecanum** — FTCLib's own `MecanumDrive` class:
  `MecanumDrive mecanum = new MecanumDrive(frontLeft, frontRight, backLeft, backRight);`

Control schemes for holonomic drives:

```java
m_drive.driveRobotCentric(strafeSpeed, forwardSpeed, turnSpeed);           // relative to robot orientation
m_drive.driveFieldCentric(strafeSpeed, forwardSpeed, turn, heading);       // relative to field, heading-adjusted
```
