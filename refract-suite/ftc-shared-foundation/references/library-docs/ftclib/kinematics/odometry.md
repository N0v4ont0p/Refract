> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/kinematics/odometry.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.kinematics
---

# Odometry

FTCLib offers its own odometry classes for the use of differential and holonomic drives. The odometry classes track the robot position as a `Pose2d`, which means it is represented using the vector $$\begin{pmatrix} x\\ y\\ \theta \end{pmatrix}$$ . $$x$$ is the distance in the forward direction of the robot, $$y$$ is the horizontal distance, and $$\theta$$ is the heading of the robot.

When using these classes, it is important to keep angles in radians. Distances should be consistent.

## Pose Exponential

Pose Exponential is a general FRC term for the constant velocity method of odometry utilized in FTC. We use pose exponentials because the cycle times of control loops in FTC can vary significantly.

This method uses differential equations to solve the nonlinear position of the robot given constant curvature. As such, we will not explain the math here. If you are interested in the math behind it, we suggest you read up on [Tyler's book](https://tavsys.net/controls-in-frc).

### Offsets and Trackwidth

The trackwidth is the distance between parallel encoders. This value should be tuned so that a precise calculation can be made. This value is a required pass into the constructor.

The center wheel offset accounts for the distance between the center of rotation of the robot and the position of the horizontal encoder. This is only necessary for the holonomic odometry.

To tune these values, make a rough estimate with a measured value and then use some sort of method for testing and updating the values until the outputs become reliable. Alternatively to beginning with a measured value, you can start at 18. Your value should then converge to some smaller distance.

## Creating the Odometry

A sample usage of FTCLib odometry can be found in this [sample folder](https://github.com/FTCLib/FTCLib/tree/v2.0.1/examples/src/main/java/com/example/ftclibexamples/SharedOdometry). A sample for dead wheels can be found [here](https://github.com/FTCLib/FTCLib/blob/v2.0.1/examples/src/main/java/com/example/ftclibexamples/DeadWheelsSample.java).

### Using the Odometry Class

To use the odometry class, there are three different constructors depending on how you want to run your odometry. One method of running the odometry is using suppliers to have the class update your positions for you. The other is to manually input the sensor data into the `update()` method, which has parameters of the left encoder value, right encoder value, and horizontal encoder value \(which is only used for holonomic\). If you use suppliers, you can just call the `updatePose()` method which uses the suppliers to call the `update()` method.

```java
// define our trackwidth
static final double TRACKWIDTH = 13.7;

// convert ticks to inches
static final double TICKS_TO_INCHES = 15.3;

// create our encoders
MotorEx encoderLeft, encoderRight;
encoderLeft = new MotorEx(hardwareMap, "left_encoder");
encoderRight = new MotorEx(hardwareMap, "right_encoder");

// create our odometry
DifferentialOdometry diffOdom = new DifferentialOdometry(
    () -> encoderLeft.getCurrentPosition() * TICKS_TO_INCHES,
    () -> encoderRight.getCurrentPosition() * TICKS_TO_INCHES,
    TRACKWIDTH
);

// update the initial position
diffOdom.updatePose(new Pose2d(1, 2, 0));

// control loop
while (!isStopRequested()) {
    /* implementation */

    // update the position
    diffOdom.updatePose();
}
```

You should call the respective update method once every cycle of the control loop.

### Using the Odometry Subsystem

The [OdometrySubsystem](https://github.com/FTCLib/FTCLib/blob/v2.0.1/core/src/main/java/com/arcrobotics/ftclib/command/OdometrySubsystem.java) class is a template subsystem meant to make command-based programming around odometry much simpler and functional. Using the odometry subsystem makes it more accurate because the position will update itself through the scheduler's call to its `periodic()` method, which updates the position. The subsystem makes use of the suppliers, so you will **need** to use that constructor instead of the other for the FTCLib subsystem. Alternatively, you can create your own odometry subsystem.

```java
// define our constants
static final double TRACKWIDTH = 13.7;
static final double TICKS_TO_INCHES = 15.3;
static final double CENTER_WHEEL_OFFSET = 2.4;

// create our encoders
MotorEx encoderLeft, encoderRight, encoderPerp;
encoderLeft = new MotorEx(hardwareMap, "left_encoder");
encoderRight = new MotorEx(hardwareMap, "right_encoder");
encoderPerp = new MotorEx(hardwareMap, "center_encoder");

encoderLeft.setDistancePerPulse(TICKS_TO_INCHES);
encoderRight.setDistancePerPulse(TICKS_TO_INCHES);
encoderPerp.setDistancePerPulse(TICKS_TO_INCHES);

// create the odometry object
HolonomicOdometry holOdom = new HolonomicOdometry(
    encoderLeft::getDistance,
    encoderRight::getDistance,
    encoderPerp::getDistance,
    TRACKWIDTH, CENTER_WHEEL_OFFSET
);

// create the odometry subsystem
OdometrySubsystem odometry = new OdometrySubsystem(holOdom);
```

The [PurePursuitCommand](https://docs.ftclib.org/ftclib/pathing/pure-pursuit#using-the-pure-pursuit-command) makes use of the OdometrySubsystem class.

