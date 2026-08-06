> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/kinematics/wpilib-kinematics/swerve-drive-kinematics.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: >-
  import
  com.arcrobotics.ftclib.kinematics.wpilibkinematics.SwerveDriveKinematics
---

# Swerve Drive Kinematics

The `SwerveDriveKinematics` class is a useful tool that converts between a `ChassisSpeeds` object and several `SwerveModuleState` objects, which contains velocities and angles for each swerve module of a swerve drive robot.

## The `SwerveModuleState` Class

The `SwerveModuleState` class contains information about the velocity and angle of a singular module of a swerve drive. The constructor for a `SwerveModuleState` takes in two arguments, the velocity of the wheel on the module, and the angle of the module.

The velocity of the wheel must be in meters per second. An angle of 0 from the module represents the forward-facing direction.

## Constructing the Kinematics Object

The `SwerveDriveKinematics` class accepts a variable number of constructor arguments, with each argument being the location of a swerve module relative to the robot center \(as a `Translation2d`. The number of constructor arguments corresponds to the number of swerve modules. A swerve bot must have AT LEAST two swerve modules.

The locations for the modules must be relative to the center of the robot. Positive x values represent moving toward the front of the robot whereas positive y values represent moving toward the left of the robot.

```java
// Locations for the swerve drive modules
// relative to the robot center.
Translation2d m_frontLeftLocation =
  new Translation2d(0.381, 0.381);
Translation2d m_frontRightLocation =
  new Translation2d(0.381, -0.381);
Translation2d m_backLeftLocation =
  new Translation2d(-0.381, 0.381);
Translation2d m_backRightLocation =
  new Translation2d(-0.381, -0.381);

// Creating my kinematics object using the module locations
SwerveDriveKinematics m_kinematics = new SwerveDriveKinematics
(
  m_frontLeftLocation, m_frontRightLocation,
  m_backLeftLocation, m_backRightLocation
);
```

## Converting Chassis Speeds to Module States

The `toSwerveModuleStates(ChassisSpeeds speeds)` method should be used to convert a `ChassisSpeeds` object to a an array of `SwerveModuleState` objects. This is useful in situations where you have to convert a forward velocity, sideways velocity, and an angular velocity into individual module states.

The elements in the array that is returned by this method are the same order in which the kinematics object was constructed. For example, if the kinematics object was constructed with the front left module location, front right module location, back left module location, and the back right module location in that order, the elements in the array would be the front left module state, front right module state, back left module state, and back right module state in that order.

```java
// Example chassis speeds: 1 meter per second forward, 3 meters
// per second to the left, and rotation at 1.5 radians per second
// counterclockwise.
ChassisSpeeds speeds = new ChassisSpeeds(1.0, 3.0, 1.5);

// Convert to module states
SwerveModuleState[] moduleStates =
    kinematics.toSwerveModuleStates(speeds);

// Front left module state
SwerveModuleState frontLeft = moduleStates[0];

// Front right module state
SwerveModuleState frontRight = moduleStates[1];

// Back left module state
SwerveModuleState backLeft = moduleStates[2];

// Back right module state
SwerveModuleState backRight = moduleStates[3];
```

### Field-Oriented Drive

[Recall](./) that a `ChassisSpeeds` object can be created from a set of desired field-oriented speeds. This feature can be used to get module states from a set of desired field-oriented speeds.

```java
// The desired field relative speed here is 2 meters per second
// toward the opponent's alliance station wall, and 2 meters per
// second toward the left field boundary. The desired rotation
// is a quarter of a rotation per second counterclockwise.
// The current robot angle is 45 degrees.
ChassisSpeeds speeds = ChassisSpeeds.fromFieldRelativeSpeeds(
  2.0, 2.0, Math.PI / 2.0, Rotation2d.fromDegrees(45.0)
);

// Now use this in our kinematics
SwerveModuleState[] moduleStates =
  kinematics.toSwerveModuleStates(speeds);
```

### Using Custom Centers of Rotation

Sometimes, rotating around one specific corner might be desirable for certain evasive maneuvers. This type of behavior is also supported by the WPILib classes. The same `ToSwerveModuleStates()` method accepts a second parameter for the center of rotation \(as a `Translation2d`\). Just like the wheel locations, the `Translation2d` representing the center of rotation should be relative to the robot center.

Because all robots are a rigid frame, the provided `vx` and `vy` velocities from the `ChassisSpeeds` object will still apply for the entirety of the robot. However, the `omega` from the `ChassisSpeeds` object will be measured from the center of rotation.

For example, one can set the center of rotation on a certain module and if the provided `ChassisSpeeds` object has a `vx` and `vy` of zero and a non-zero `omega`, the robot will appear to rotate around that particular swerve module.

## Converting Module States to Chassis Speeds

One can also use the kinematics object to convert an array of `SwerveModuleState` objects to a singular `ChassisSpeeds` object. The `toChassisSpeeds(SwerveModuleState... states)` method can be used to achieve this.

```java
// Example module states
SwerveModuleState frontLeftState =
  new SwerveModuleState(23.43, Rotation2d.fromDegrees(-140.19));
SwerveModuleState frontRightState =
  new SwerveModuleState(23.43, Rotation2d.fromDegrees(-39.81));
SwerveModuleState backLeftState =
  new SwerveModuleState(54.08, Rotation2d.fromDegrees(-109.44));
SwerveModuleState backRightState =
  new SwerveModuleState(54.08, Rotation2d.fromDegrees(-70.56));

// Convert to chassis speeds
ChassisSpeeds chassisSpeeds = kinematics.toChassisSpeeds(
  frontLeftState, frontRightState, backLeftState, backRightState
);

// Getting individual speeds
double forward = chassisSpeeds.vxMetersPerSecond;
double sideways = chassisSpeeds.vyMetersPerSecond;
double angular = chassisSpeeds.omegaRadiansPerSecond;
```

