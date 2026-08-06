> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/kinematics/wpilib-kinematics/swerve-drive-odometry.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.kinematics.wpilibkinematics.SwerveDriveOdometry
---

# Swerve Drive Odometry

A user can use the swerve drive kinematics classes in order to perform [odometry](./#what-is-odometry). WPILib/FTCLib contains a `SwerveDriveOdometry` class that can be used to track the position of a swerve drive robot on the field.

**Note**:  
Because this method only uses encoders and a gyro, the estimate of the robot’s position on the field will drift over time, especially as your robot comes into contact with other robots during gameplay. However, odometry is usually very accurate during the autonomous period.

## Creating the Odometry Object

The `SwerveDriveOdometry` class requires two mandatory arguments, and one optional argument. The mandatory arguments are the kinematics object that represents your swerve drive \(in the form of a `SwerveDriveKinematics` class\) and the angle reported by your gyroscope \(as a Rotation2d\). The third optional argument is the starting pose of your robot on the field \(as a `Pose2d`\). By default, the robot will start at $$\begin{pmatrix} x\\ y\\ \theta \end{pmatrix} = \begin{pmatrix} 0\\ 0\\ 0 \end{pmatrix}$$ .

0 degrees / radians represents the robot angle when the robot is facing directly toward your opponent’s alliance station. As your robot turns to the left, your gyroscope angle should increase.

```java
// Locations for the swerve drive modules relative to the
// robot center.
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

// Creating my odometry object from the kinematics object. Here,
// our starting pose is 5 meters along the long end of the
// field and in the
// center of the field along the short end, facing forward.
SwerveDriveOdometry m_odometry = new SwerveDriveOdometry
(
  m_kinematics, getGyroHeading(),
  new Pose2d(5.0, 13.5, new Rotation2d()
);
```

## Updating the Robot Pose

The `update` method of the odometry class updates the robot position on the field. The update method takes in the gyro angle of the robot, along with a series of module states \(speeds and angles\) in the form of a `SwerveModuleState` each. It is important that the order in which you pass the `SwerveModuleState` objects is the same as the order in which you created the kinematics object.

This `update` method must be called periodically, preferably in the `periodic()` method of a [Subsystem](../../command-base/command-system/subsystems.md). The `update` method returns the new updated pose of the robot.

```java
@Override
public void periodic() {
  // Get my gyro angle.
  Rotation2d gyroAngle = Rotation2d.fromDegrees(m_gyro.getHeading());

  // Update the pose
  m_pose = m_odometry.update
  (
    gyroAngle, m_frontLeftModule.getState(),
    m_frontRightModule.getState(),
    m_backLeftModule.getState(), m_backRightModule.getState()
  );
}
```

### Resetting the Robot Pose

The robot pose can be reset via the `resetPose` method. This method accepts two arguments – the new field-relative pose and the current gyro angle.

If at any time, you decide to reset your gyroscope, the `resetPose` method MUST be called with the new gyro angle.

The implementation of `getState()` above is left to the user. The idea is to get the module state \(speed and angle\) from each module.

In addition, the `getPoseMeters()` method can be used to retrieve the current robot pose without an update.

