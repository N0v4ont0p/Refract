> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/kinematics/wpilib-kinematics/mecanum-drive-odometry.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.kinematics.wpilibkinematics.MecanumDriveOdometry
---

# Mecanum Drive Odometry

A user can use the mecanum drive kinematics classes in order to perform [odometry](./#what-is-odometry). WPILib/FTCLib contains a `MecanumDriveOdometry` class that can be used to track the position of a mecanum drive robot on the field.

**Note**:  
Because this method only uses encoders and a gyro, the estimate of the robot’s position on the field will drift over time, especially as your robot comes into contact with other robots during gameplay. However, odometry is usually very accurate during the autonomous period.

## Creating the Odometry Object

The `MecanumDriveOdometry` class requires two mandatory arguments and one optional argument. The mandatory arguments are the kinematics object that represents your mecanum drive \(in the form of a `MecanumDriveKinematics` class\) and the angle reported by your gyroscope \(as a Rotation2d\). The third optional argument is the starting pose of your robot on the field \(as a `Pose2d`\). By default, the robot will start at $$\begin{pmatrix} x\\ y\\ \theta \end{pmatrix} = \begin{pmatrix} 0\\ 0\\ 0 \end{pmatrix}$$ .

0 degrees / radians represents the robot angle when the robot is facing directly toward your opponent’s alliance station. As your robot turns to the left, your gyroscope angle should increase.

```java
// Locations of the wheels relative to the robot center.
Translation2d m_frontLeftLocation =
  new Translation2d(0.381, 0.381);
Translation2d m_frontRightLocation =
  new Translation2d(0.381, -0.381);
Translation2d m_backLeftLocation =
  new Translation2d(-0.381, 0.381);
Translation2d m_backRightLocation =
  new Translation2d(-0.381, -0.381);

// Creating my kinematics object using the wheel locations.
MecanumDriveKinematics m_kinematics = new MecanumDriveKinematics
(
  m_frontLeftLocation, m_frontRightLocation,
  m_backLeftLocation, m_backRightLocation
);

// Creating my odometry object from the kinematics object. Here,
// our starting pose is 5 meters along the long end of the field and in the
// center of the field along the short end, facing forward.
MecanumDriveOdometry m_odometry = new MecanumDriveOdometry
(
  m_kinematics, getGyroHeading(),
  new Pose2d(5.0, 13.5, new Rotation2d()
);
```

## Updating the Robot Pose

The `update` method of the odometry class updates the robot position on the field. The update method takes in the gyro angle of the robot, along with a `MecanumDriveWheelSpeeds` object representing the speed of each of the 4 wheels on the robot. This `update` method must be called periodically, preferably in the `periodic()` method of a [Subsystem](../../command-base/command-system/subsystems.md). The `update` method returns the new updated pose of the robot.

The `MecanumDriveWheelSpeeds` class must be constructed with each wheel speed in meters per second.

```java
@Override
public void periodic() {
  // Get my wheel speeds; assume .getRate() has been
  // set up to return velocity of the encoder
  // in meters per second.
  MecanumDriveWheelSpeeds wheelSpeeds = new MecanumDriveWheelSpeeds
  (
      m_frontLeftEncoder.getRate(), m_frontRightEncoder.getRate(),
      m_backLeftEncoder.getRate(), m_backRightEncoder.getRate()
  );

  // Get my gyro angle.
  Rotation2d gyroAngle = Rotation2d.fromDegrees(m_gyro.getAngle());

  // Update the pose
  m_pose = m_odometry.update(gyroAngle, wheelSpeeds);
}
```

### Resetting the Robot Pose

The robot pose can be reset via the `resetPose` method. This method accepts two arguments – the new field-relative pose and the current gyro angle.

If at any time, you decide to reset your gyroscope, the `resetPose` method MUST be called with the new gyro angle.

In addition, the `getPoseMeters()` method can be used to retrieve the current robot pose without an update.

