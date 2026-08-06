> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/pathing/pure-pursuit.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.purepursuit
---
# This is buggy and is being replaced in the next version of FTCLib. Its use is currently not recommend

# Pure Pursuit

The pure pursuit algorithm in FTCLib is developed so that the user only needs to add the desired waypoints and call the `followPath()` method in the [Path](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/purepursuit/Path.java) class. To use this, you need to pass the [mecanum](https://docs.ftclib.org/ftclib/features/drivebases#mecanum) drivetrain as well as the odometry for the robot. Once the method is finished, it will return true or false depending on if it was successful or not.

As an alternative, you can call the `loop()` method and directly input your odometry positions there. Make sure you update the odometry positions with each iteration of the loop.

## What is Pure Pursuit?

Pure pursuit, otherwise designated as "PP," is a path tracking algorithm that calculates the robot velocity in order to reach a designated look-ahead point from the current position. It loosely follows a path determined by a set of waypoints, which are coordinates on the field. What the pure pursuit controller does is create a circle of determined radius and follow the path by "looking ahead" with the circle and seeing where it intersects with the path. The robot's heading orientation is then compared to the radius that connects the center of the robot to that intersection. It then moves in correspondence. The radius size can be updated for each waypoint you enter into the path for specificity.

![A visual representation of look-ahead](../.gitbook/assets/look-ahead.png)

The robot continues to follow this intersection at real-time. This is how the robot "follows" the designated path. It is essentially a p controller for the heading that has the robot move at the fastest possible speed around some path.

### Waypoints

There are five types of waypoints: start, general, interrupted, point-turn, and end. The starting waypoint represents the first point in the path; conversely, the ending waypoint is the last point in the path.

A general waypoint is a point where the robot performs its ordinary pursuit algorithm with the look-ahead method. A point-turn waypoint is a type of general waypoint that stops at the given point, turns, and then traverses to the next waypoint. An interrupted waypoint is a type of point-turn waypoint where other actions can occur, such as picking up a skystone.

#### Creating Waypoints

You can create a waypoint by calling the various constructors.

**StartWaypoint**

```java
// Empty constructor. Note: Only use this constructor
// if you plan on setting the values later.
Waypoint p1 = new StartWaypoint();

// With Pose2d.
Waypoint p1 = new StartWaypoint(pose2d);
// With X and Y coordinates.
Waypoint p1 = new StartWaypoint(x, y);
// With Translation2d.
Waypoint p1 = new StartWaypoint(translation2d);
```

**GeneralWaypoint**

Each general waypoint inherits from the previous general waypoint in the path. The only parameters that will need to be specified are the x and y coordinates of the point. Each point has the option to update the different parameters across the path \(which is meant for user-end customization of the path\). Point-turn waypoints, interrupted waypoints, and end waypoints are all subclasses of a general waypoint, so they will also have this feature. This inheritance is performed in the `init()` method of the path.

```java
// Empty constructor. Note: Only use this constructor
// if you plan on setting the values later.
Waypoint p2 = new GeneralWaypoint();

// With X and Y coordinates. This waypoint will inherit
// its settings from the previous waypoint.
// Useful for long strings of waypoints.
// Note: Will not work if the waypoint preceding
// this is not an instance of GeneralWaypoint. 
Waypoint p2 = new GeneralWaypoint(x, y);

/**
 * Normal constructors.
 */
// With Translation2d and Rotation2d.
Waypoint p2 = new GeneralWaypoint(
    translation2d, rotation2d,
    movementSpeed, turnSpeed,
    followRadius
);
// With Pose2D.
Waypoint p2 = new GeneralWaypoint(
    pose2d, movementSpeed, turnSpeed,
    followRadius
);
// With X and Y coordinates.
Waypoint p2 = new GeneralWaypoint(
    x, y, movementSpeed,
    turnSpeed, followRadius
);
// With a preferred angle.
Waypoint p2 = new GeneralWaypoint(
    x, y, rotationRadians,    
    movementSpeed, turnSpeed,
    followRadius
);
```

**PointTurnWaypoint**

As you will see here, a "buffer" is a sort of expected error. This sets up a tolerance given that the robot might be a bit offset from the desired position or rotation.

```java
// Empty constructor. Note: Only use this constructor
// if you plan on setting the values later.
Waypoint p3 = new PointTurnWaypoint();

/**
 * Normal constructors.
 */
// With Translation2d and Rotation2d.
Waypoint p3 = new PointTurnWaypoint(
    translation2d, rotation2d,
    movementSpeed, turnSpeed,
    followRadius, positionBuffer,
    rotationBuffer
);
// With Pose2D.
Waypoint p3 = new PointTurnWaypoint(
    pose2d, movementSpeed,
    turnSpeed, followRadius,
    positionBuffer, rotationBuffer
);
// With X and Y coordinates and preferred angle.
Waypoint p3 = new PointTurnWaypoint(
    x, y, rotationRadians, movementSpeed,
    turnSpeed, followRadius,
    positionBuffer, rotationBuffer
);
// With X and Y coordinates.
Waypoint p3 = new PointTurnWaypoint(
    x, y, movementSpeed,
    turnSpeed, followRadius,
    positionBuffer, rotationBuffer
);
```

**InterruptWaypoint**

The `action` here is an [InterruptAction](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/purepursuit/actions/InterruptAction.java), which is an interface that the user can implement to create a custom action to occur at this point. A recommendation is to pair this with the [command paradigm](../command-base/command-system/) that FTCLib provides.

```java
// Empty constructor. Note: Only use this constructor
// if you plan on setting the values later.
Waypoint p4 = new InterruptWaypoint();

/**
 * Normal constructors.
 */
// With Translation2d and Rotation2d.
Waypoint p4 = new InterruptWaypoint(
    translation2d, rotation2d,
    movementSpeed, turnSpeed,
    followRadius, positionBuffer,
    rotationBuffer, action
);
// With Pose2D.
Waypoint p4 = new InterruptWaypoint(
    pose2d, movementSpeed, turnSpeed,
    followRadius, positionBuffer,
    rotationBuffer, action
);
// With X and Y coordinates and preferred angle.
Waypoint p4 = new InterruptWaypoint(
    x, y, rotationRadians,
    movementSpeed, turnSpeed,
    followRadius, positionBuffer,
    rotationBuffer, action
);
// With X and Y coordinates.
Waypoint p4 = new InterruptWaypoint(
    x, y, movementSpeed,
    turnSpeed, followRadius,
    positionBuffer, rotationBuffer,
    action
);

// With java 8 you can use a lambda expression to easily
// add an action. For example:
Waypoint p4 = new InterruptWaypoint(
    x, y, movementSpeed, turnSpeed,
    followRadius, positionBuffer,
    rotationBuffer, grabSubsystem::grabBlock
);
```

**EndWaypoint**

```java
// Empty constructor. Note: Only use this constructor
// if you plan on setting the values later.
Waypoint p5 = new EndWaypoint();

/**
 * Normal constructors.
 */
// With Translation2d and Rotation2d.
Waypoint p5 = new PointTurnWaypoint(
    translation2d, rotation2d,
    movementSpeed, turnSpeed,
    followRadius, positionBuffer,
    rotationBuffer
);
// With Pose2D.
Waypoint p5 = new PointTurnWaypoint(
    pose2d, movementSpeed,
    turnSpeed, followRadius,
    positionBuffer, rotationBuffer
);
// With X and Y coordinates and preferred angle
// (A preferred angle is needed for an EndWaypoint).
Waypoint p5 = new PointTurnWaypoint(
    x, y, rotationRadians, movementSpeed,
    turnSpeed, followRadius,
    positionBuffer, rotationBuffer
);
```

## Creating the Path

Before you can call the `loop()` or `followPath()` method, you need to follow the proper procedure. If you are using `loop()`, you need to call the `init()` method to ensure your path is legal and set up the unconfigured waypoints.

```java
// we are using the waypoints we made in the above examples
Path m_path = new Path(p1, p2, p3, p4, p5);

m_path.init(); // initialize the path
```

If the path is not legal, an exception will be thrown.

### Intersections

An intersection is the point where the follow distance represented by a circle around the robot meets the drawn path derived from the waypoints. The "best intersection" is determined by either waypoint order or heading. This intersection point where the circle meets the path is where the robot will move to. The pure pursuit algorithm determines the best intersection and calculates the motor powers needed to reach said position. This updates with each loop, so the intersection point can change with each step due to the movement of the robot. While the conventional pure pursuit algorithm used heading controlled waypoints, FTCLib features a custom type of intersection control we call "order controlled". This type of control is more powerful and less prone to errors then heading controlled and is enabled by default. If you wish to use heading controlled instead, use this \(not recommended\):

```java
m_path.setPathType(PathType.HEADING_CONTROLLED);
```

### Retrace

FTCLib's pure pursuit implementation includes a unique feature we call retrace. One common issue with pure pursuit is that the robot can lose it's path. Retrace solves this issue. If enabled \(retrace is enabled by default\) and the robot loses it's path, the software will automatically plot a temporary path back to it's last known path position. Once the robot finds the path again it will continue on as normal. If you wish to disable retrace \(not recommended\), do this:

```java
m_path.disableRetrace();
```

### Timeouts

Advanced teams may want to have more control over how long the robot get to have to complete a path. If the robot is stuck on a path/waypoint for too long, you may want to stop the path to avoid accidental penalties. To set timeouts do the following:

```java
// For an entire path
m_path.setWaypointTimeouts(timeout);

// For individual waypoints
m_path.setWaypointTimeouts(p1_timeout, p2_timeout, p3_timeout, ...);

// Reset timeouts.
m_path.resetTimeouts();
```

### Resetting the Path

If you want to use a path more than once in the same opmode, make sure to reset between uses. You can do this as follows:

```java
m_path.reset();
```

## Using `followPath()`

The `followPath()` method is the automatic implementation of pure pursuit for FTCLib. For teams that want to use all of FTCLib's features to the fullest, this is the recommended process.

An important note for the pure pursuit algorithm is that it only works well with odometry. You can use the various odometry systems provided by FTCLib. An important thing to note is that `followPath()` makes use of the [Odometry](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/kinematics/Odometry.java) abstract class and the [mecanum drivebase](https://docs.ftclib.org/ftclib/features/drivebases#mecanum). Then, the method will call the loop method and do everything for you.

```java
// follow path
m_path.followPath(m_robotDrive, m_robotOdometry);
```

An issue this method has is that we cannot directly access the hardware of the robot. As a result, the `update()` method for the odometry is not called in `followPath()`. Instead, we call `updatePose()`.

### Creating Your Odometry

As a way of working around this issue, the odometry needs to be setup in a particular way with [Suppliers](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html). A supplier is a functional interface that uses lambdas to reference a certain value. Let's work with the [HolonomicOdometry](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/kinematics/HolonomicOdometry.java) class for these examples.

You're going to want to instantiate your odometry using this constructor:

```java
HolonomicOdometry m_robotOdometry = new HolonomicOdometry(
    leftValue, rightValue, horizontalValue, trackWidth,
    centerWheelOffset
);
```

#### Creating the Suppliers

Before we can create the object, we need to make our suppliers. We will do this by using the [DoubleSupplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/DoubleSupplier.html) implementation. We need to create three of these objects: one for each odometer. Let's assume the user has created a method that automatically converts ticks to inches for an external encoder.

```java
DoubleSupplier leftValue, rightValue, horizontalValue;

leftValue = () -> ticksToInches(m_lOdom.getCurrentPosition());
rightValue = () -> ticksToInches(m_rOdom.getCurrentPosition());
horizontalValue = () -> ticksToInches(m_hOdom.getCurrentPosition());
```

## Using `loop()`

The alternative to the `followPath()` method is the `loop()` method. For teams that want to use solely the FTCLib implementation of pure pursuit and perform the rest of the actions themselves, then this is the more appealing method.

The use of suppliers can be avoided using this method since it can be called in your own class with access to the hardware directly.

### Odometry Options

The odometry is much more open for this. You can use whatever constructor you desire for it. Since the method parameters only take x, y, and heading values, you can use whatever odometry system you desire as long as it produces such values. This is one of the more appealing aspects of the `loop()` method.

The important thing for odometry is to remember to update the position of the robot after each iteration after manually inputting the motor speeds.

### Calling the Method

This is the principle path method. After everything is configured and initiated, this method can be used. Using the robot's x, y, and rotation, this method calculates the appropriate motor powers for the robot to follow the path. This method calls all triggered/interrupted actions automatically. If this returns zero motor speeds `{0, 0, 0}` that means the path has either \(1\) timed out, \(2\) lost the path and retrace was disabled, or \(3\) reached the destination. Use `isFinished()` and `timedOut()` to troubleshoot.

Below is an example using a custom robot class that includes the drivebase and odometry:

```java
while (!m_path.isFinished()) {
    if (m_path.timedOut())
        throw new InterruptedException("Timed out");

    // return the motor speeds
    double speeds[] = m_path.loop(m_robot.getX(), m_robot.getY(),
                                  m_robot.getHeading());

    m_robot.drive(speeds[0], speeds[1], speeds[2]);
    m_robot.updatePose();
}
m_robot.stop();
```

## Using the Pure Pursuit Command

If you're using your odometry for multiple subsystems, you're likely going to want to make use of the [PurePursuitCommand](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/command/PurePursuitCommand.java) due to the shared odometry \(as we only want to update it once per cycle\). This is actually the recommended method of using pure pursuit, especially if you want to use it with the command-based paradigm that FTCLib has to offer.

### Creating an Odometry Subsystem

The pre-built PurePursuitCommand requires the use of FTCLib's [OdometrySubsystem](https://docs.ftclib.org/ftclib/kinematics/odometry#using-the-odometry-subsystem). It is fairly easy to set up. All that is needed is for the user to pass in their odometry class into the constructor of the subsystem.

```java
// create the odometry object
HolonomicOdometry m_robotOdometry = new HolonomicOdometry(
    leftValue, rightValue, horizontalValue, TRACKWIDTH,
    CENTER_WHEEL_OFFSET
);

// pass the odometry object into the subsystem constructor
OdometrySubsystem m_odometry = new OdometrySubsystem(
    m_robotOdometry
);
```

#### Using the Odometry Subsystem

Users can make use of the odometry subsystem in the exact same way as the Odometry class.

```java
// retrieve the current saved pose of the robot
Pose2d robotPose = m_odometry.getPose();

// update the pose manually
m_odometry.update();
```

The odometry subsystem updates the position of the robot in its `periodic()` method, so it will update every time the CommandScheduler is run. This effectively means that the position does not need to be updated manually unless desired by the user.

### Creating a PurePursuitCommand

Creating the command is simple. Note that this implementation of the command does not utilize every feature of the Path and is relatively simplistic. It is designed to be a simple template for the user and not an end-all-be-all for every possible desired activity.

To create the object, pass in the drivebase object, the odometry subsystem, and the desired waypoints.

```java
PurePursuitCommand ppCommand = new PurePursuitCommand(
    m_robotDrive, m_odometry,
    p1, p2, p3, p4, p5
);

// schedule the command
ppCommand.schedule();

// remove waypoint at specified index
ppCommand.removeWayPointAtIndex(4);
ppCommand.removeWayPointAtIndex(3);
ppCommand.removeWayPointAtIndex(2);

// add waypoints to the path
ppCommand.addWaypoint(p3);
ppCommand.addWaypoints(p4, p5);
```

The rest of the class does everything for you through the command-based paradigm. Using the `execute()`, `end(interrupted)`, and `isFinished()` methods allows for the command to be run simply by running the scheduler in a loop.

### Running the Command

It is run the exact same way everything else is run in the paradigm: by running the scheduler. Take a look at [this sample](https://github.com/FTCLib/FTCLib/blob/v2.1.1/examples/src/main/java/com/example/ftclibexamples/PurePursuitSample.java) to see how everything works together.

