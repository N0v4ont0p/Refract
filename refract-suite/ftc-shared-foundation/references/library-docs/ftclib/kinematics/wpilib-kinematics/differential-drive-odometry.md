> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/kinematics/wpilib-kinematics/differential-drive-odometry.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: >-
  import
  com.arcrobotics.ftclib.kinematics.wpilibkinematics.DifferentialDriveOdometry
---

# Differential Drive Odometry

A user can use the differential drive kinematics classes in order to perform [odometry](./#what-is-odometry). WPILib/FTCLib contains a `DifferentialDriveOdometry` class that can be used to track the position of a differential drive robot on the field.

**Note**:  
Because this method only uses encoders and a gyro, the estimate of the robot’s position on the field will drift over time, especially as your robot comes into contact with other robots during gameplay. However, odometry is usually very accurate during the autonomous period.

## Creating the Odometry Object

The `DifferentialDriveOdometry` class requires one mandatory argument and one optional argument. The mandatory argument is the angle reported by your gyroscope \(as a Rotation2d\). The optional argument is the starting pose of your robot on the field \(as a `Pose2d`\). By default, the robot will start at $$\begin{pmatrix} x\\ y\\ \theta \end{pmatrix} = \begin{pmatrix} 0\\ 0\\ 0 \end{pmatrix}$$ .

0 degrees / radians represents the robot angle when the robot is facing directly toward your opponent’s alliance station. As your robot turns to the left, your gyroscope angle should increase.

The encoder positions **must** be reset to zero before constructing the `DifferentialDriveOdometry` class.

```java
// Creating my odometry object. Here,
// our starting pose is 5 meters along the long end of the field
// and in the center of the field along the short end,
// facing forward.
DifferentialDriveOdometry m_odometry = new DifferentialDriveOdometry
(
    getGyroHeading(), new Pose2d(5.0, 13.5, new Rotation2d()
);
```

## Updating the Robot Pose

The `update` method can be used to update the robot’s position on the field. This method must be called periodically, preferably in the `periodic()` method of a [Subsystem](../../command-base/command-system/subsystems.md). The `update` method returns the new updated pose of the robot. This method takes in the gyro angle of the robot, along with the left encoder distance and right encoder distance.

Ensure your encoder distances are in meters!

### Resetting the Robot Pose

The robot pose can be reset via the `resetPose` method. This method accepts two arguments – the new field-relative pose and the current gyro angle.

If at any time, you decide to reset your gyroscope, the `resetPose` method MUST be called with the new gyro angle. Furthermore, the encoders must also be reset to zero when resetting the pose.

