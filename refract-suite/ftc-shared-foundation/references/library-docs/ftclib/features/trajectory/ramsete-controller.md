> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/features/trajectory/ramsete-controller.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.controller.wpilibcontroller.RamseteController
---

# Ramsete Controller

The Ramsete Controller is a trajectory tracker that is built in to FTCLib. This tracker can be used to accurately track trajectories with correction for minor disturbances.

Ramsete is a nonlinear time-varying feedback controller for unicycle models
 that drives the model to a desired pose along a two-dimensional trajectory.
 Why would we need a nonlinear control law in addition to the linear ones we
 have used so far like PID? If we use the original approach with PID
 controllers for left and right position and velocity states, the controllers
 only deal with the local pose. If the robot deviates from the path, there is
 no way for the controllers to correct and the robot may not reach the desired
 global pose. This is due to multiple endpoints existing for the robot which
 have the same encoder path arc lengths.

Instead of using wheel path arc lengths \(which are in the robot's local
 coordinate frame\), nonlinear controllers like pure pursuit and Ramsete use
 global pose. The controller uses this extra information to guide a linear
 reference tracker like the PID controllers back in by adjusting the
 references of the PID controllers.

## Constructing the Ramsete Controller Object

The Ramsete controller should be initialized with two gains, namely `b` and `zeta`. Larger values of `b` make convergence more aggressive like a proportional term whereas larger values of `zeta` provide more damping in the response. These controller gains only dictate how the controller will output adjusted velocities. It does NOT affect the actual velocity tracking of the robot. This means that these controller gains are generally robot-agnostic.

## Getting Adjusted Velocities

The Ramsete controller returns “adjusted velocities” so that the when the robot tracks these velocities, it accurately reaches the goal point. The controller should be updated periodically with the new goal. The goal comprises of a desired pose, desired linear velocity, and desired angular velocity. Furthermore, the current position of the robot should also be updated periodically. The controller uses these four arguments to return the adjusted linear and angular velocity. Users should command their robot to these linear and angular velocities to achieve optimal trajectory tracking.

The “goal pose” represents the position that the robot should be at at a particular timestep when tracking the trajectory. It does NOT represent the final endpoint of the trajectory.

The controller can be updated using the `calculate` method. There are two overloads for this method. Both of these overloads accept the current robot position as the first parameter. For the other parameters, one of these overloads takes in the goal as three separate parameters \(pose, linear velocity, and angular velocity\) whereas the other overload accepts a `Trajectory.State` object, which contains information about the goal pose. For its ease, users should use the latter method when tracking trajectories.

```java
Trajectory.State goal = trajectory.sample(3.4); // sample the trajectory at 3.4 seconds from the beginning
ChassisSpeeds adjustedSpeeds = controller.calculate(currentRobotPose, goal);
```

These calculations should be performed at every loop iteration, with an updated robot position and goal.

## Using the Adjusted Velocities

The adjusted velocities are of type `ChassisSpeeds`, which contains a `vx` \(linear velocity in the forward direction\), a `vy` \(linear velocity in the sideways direction\), and an `omega` \(angular velocity around the center of the robot frame\). Because the Ramsete controller is a controller for non-holonomic robots \(robots which cannot move sideways\), the adjusted speeds object has a `vy` of zero.

The returned adjusted speeds can be converted to usable speeds using the kinematics classes for your [drivetrain](../drivebases.md) type. For example, the adjusted velocities can be converted to left and right velocities for a differential drive using a `DifferentialDriveKinematics` object.

```java
ChassisSpeeds adjustedSpeeds = controller.calculate(currentRobotPose, goal);
DifferentialDriveWheelSpeeds wheelSpeeds = kinematics.toWheelSpeeds(adjustedSpeeds);
double left = wheelSpeeds.leftMetersPerSecond;
double right = wheelSpeeds.rightMetersPerSecond;
```

Because these new left and right velocities are still speeds and not voltages, two PID controllers, one for each side, may be used to track these velocities.

