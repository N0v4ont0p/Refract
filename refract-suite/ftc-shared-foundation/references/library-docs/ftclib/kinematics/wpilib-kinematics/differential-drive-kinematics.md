> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/kinematics/wpilib-kinematics/differential-drive-kinematics.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: >-
  import
  com.arcrobotics.ftclib.kinematics.wpilibkinematics.DifferentialDriveKinematics
---

# Differential Drive Kinematics

The `DifferentialDriveKinematics` class is a useful tool that converts between a `ChassisSpeeds` object and a `DifferentialDriveWheelSpeeds` object, which contains velocities for the left and right sides of a differential drive robot.

## Constructing the Kinematics Object

The `DifferentialDriveKinematics` object accepts one constructor argument, which is the trackwidth of the robot. This represents the distance between the two sets of wheels on a differential drive.

**Note**: The trackwidth must be in meters.

## Converting Chassis Speeds to Wheel Speeds

The `toWheelSpeeds(ChassisSpeeds speeds)` method should be used to convert a `ChassisSpeeds` object to a `DifferentialDriveWheelSpeeds` object. This is useful in situations where you have to convert a linear velocity \(`vx`\) and an angular velocity \(`omega`\) to left and right wheel velocities.

```java
// Creating my kinematics object: track width of 15 inches
DifferentialDriveKinematics kinematics =
  new DifferentialDriveKinematics(15.0 / 254.0);

// Example chassis speeds: 2 meters per second linear velocity,
// 1 radian per second angular velocity.
ChassisSpeeds chassisSpeeds = new ChassisSpeeds(2.0, 0, 1.0);

// Convert to wheel speeds
DifferentialDriveWheelSpeeds wheelSpeeds =
  kinematics.toWheelSpeeds(chassisSpeeds);

// Left velocity
double leftVelocity = wheelSpeeds.leftMetersPerSecond;

// Right velocity
double rightVelocity = wheelSpeeds.rightMetersPerSecond;
```

## Converting Wheel Speeds to Chassis Speeds

One can also use the kinematics object to convert individual wheel speeds \(left and right\) to a singular `ChassisSpeeds` object. The `toChassisSpeeds(DifferentialDriveWheelSpeeds speeds)` method should be used to achieve this.

```java
// Creating my kinematics object: track width of 15 inches
DifferentialDriveKinematics kinematics =
  new DifferentialDriveKinematics(15.0 / 254.0);

// Example differential drive wheel speeds: 2 meters per second
// for the left side, 3 meters per second for the right side.
DifferentialDriveWheelSpeeds wheelSpeeds =
  new DifferentialDriveWheelSpeeds(2.0, 3.0);

// Convert to chassis speeds.
ChassisSpeeds chassisSpeeds = kinematics.toChassisSpeeds(wheelSpeeds);

// Linear velocity
double linearVelocity = chassisSpeeds.vxMetersPerSecond;

// Angular velocity
double angularVelocity = chassisSpeeds.omegaRadiansPerSecond;
```

