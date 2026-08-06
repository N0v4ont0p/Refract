> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/examples/auto.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Example Auto
---

This pages gives an overview of how to create an autonomous routine using PedroPathing. In this example, we write an autonomous for the 25-26 season DECODE. The robot starts against the blue goal, scores its preloads and completes three cycles of picking up and scoring, and showcases several different methods for building paths. A path progression system is  also implemented, allowing the routine to advance based on time, position, or other custom conditions.

## Step One: Setting up imports and variables
Ensure to include the required imports for the autonomous. **Note: Make sure the package statement aligns
with that of where your class files are actually located. Android Studio should automatically generate it when
creating a class**

```java title="ExampleAuto.java"
package org.firstinspires.ftc.teamcode.pedroPathing; // make sure this aligns with class location

import com.pedropathing.follower.Follower;
import com.pedropathing.geometry.BezierCurve;
import com.pedropathing.geometry.BezierLine;
import com.pedropathing.geometry.Pose;
import com.pedropathing.ivy.Command;
import com.pedropathing.ivy.Scheduler;
import com.pedropathing.paths.PathChain;
import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;

import static com.pedropathing.ivy.Scheduler.*;
import static com.pedropathing.ivy.pedro.PedroCommands.*;
import static com.pedropathing.ivy.groups.Groups.*;

@Autonomous(name = "Example Auto", group = "Examples")
public class ExampleAuto extends LinearOpMode {

    private Follower follower;
```

## Step Two: Initializing poses
Poses are points on the field coordinate system that define the (`x`, `y`, `heading`) of your robot during the autonomous. Pedro’s coordinate system spans an interval of [0, 144] on both the x and y axes, with (0, 0) defined as the bottom-left corner of the field. To see more about the coordinate system, navigate to: [Coordinates](/docs/pathing/reference/coordinates). Even though Pedro uses a different coordinate system than RR, you can convert any roadrunner pose by adding +72 both the x and y. Below are the poses for our example autonomous:

```java title="ExampleAuto.java"
private final Pose startPose = new Pose(22, 122, Math.toRadians(324)); // Start Pose of our robot. This is against the goal facing AWAY
private final Pose scorePose = new Pose(60, 84, Math.toRadians(135)); // Scoring Pose of our robot.
private final Pose pickup1Pose = new Pose(17, 84, Math.toRadians(180)); // Highest (First Set) of Artifacts from the Spike Mark.
private final Pose pickup2Pose = new Pose(12, 60, Math.toRadians(180)); // Middle (Second Set) of Artifacts from the Spike Mark.
private final Pose pickup3Pose = new Pose(12, 36, Math.toRadians(180)); // Lowest (Third Set) of Artifacts from the Spike Mark.
private final Pose endPose = new Pose (60, 105); // Final Pose of our robot, off the starting line
```

## Step Three: Path Initializing
Now we need to build the paths for the auto, while setting the desired path constraints. Below is our example on initializing paths. It is necessary to do this so that all the paths are built before the auto starts.

There are two major types of paths components: BezierCurves and BezierLines.
 - BezierCurves are curved, and require >= 3 points. There are the start and end points, and the control points. Control points manipulate the curve between the start and end points.
 - BezierLines are straight, and require 2 points. There are the start and end points.

There are also constraints which you can add to modify how your robot follows a path. To understand all of them, navigate to [Constraints](/docs/pathing/reference/constraints).

We also add **heading interpolation** to our paths. Heading interpolation handles where our robot is facing when we drive along a path.
If you don't set an interpolation for a path, it will default to tangential (driving along a path like a car or tank drive).
To understand how heading interpolation works, and the different types, navigate to [Interpolation](/docs/pathing/reference/interpolation).

When using PedroPathing, it's recommended to make all your paths into PathChains, even if it is only a single line. This is because PathChains have more features, such as controlling the max power and holding the end of the path. 

```java title="ExampleAuto.java"
//defining our PathChains
private PathChain scorePreload, grabPickup1, scorePickup1, grabPickup2, scorePickup2, grabPickup3, scorePickup3, leave;

public void buildPaths() {
    scorePreload = follower.pathBuilder()
            .addPath(new BezierLine(startPose, scorePose))
            .setLinearHeadingInterpolation(startPose.getHeading(), scorePose.getHeading())
            .build();


    /* This is our grabPickup1 PathChain. We are using a single path with a BezierLine, which is a straight line. */
    grabPickup1 = follower.pathBuilder()
            .addPath(new BezierLine(scorePose, pickup1Pose))
            .setLinearHeadingInterpolation(scorePose.getHeading(), pickup1Pose.getHeading())
            .build();

    /* This is our scorePickup1 PathChain. We are using a single path with a BezierLine, which is a straight line. */
    scorePickup1 = follower.pathBuilder()
            .addPath(new BezierLine(pickup1Pose, scorePose))
            .setLinearHeadingInterpolation(pickup1Pose.getHeading(), scorePose.getHeading())
            .build();

    /* This is our grabPickup2 PathChain. We are using a single path with a BezierCurve (curved line). */
    grabPickup2 = follower.pathBuilder()
            .addPath(new BezierCurve(scorePose, new Pose(60, 54), pickup2Pose))
            .setLinearHeadingInterpolation(scorePose.getHeading(), pickup2Pose.getHeading())
            .build();

    /* This is our scorePickup2 PathChain. We are using a single path with a BezierCurve (curved line). */
    scorePickup2 = follower.pathBuilder()
            .addPath(new BezierCurve(pickup2Pose, new Pose(60, 54), scorePose))
            .setLinearHeadingInterpolation(pickup2Pose.getHeading(), scorePose.getHeading())
            .build();

    /* This is our grabPickup3 PathChain. We are using a single path with a BezierCurve (curved line). */
    grabPickup3 = follower.pathBuilder()
            .addPath(new BezierCurve(scorePose, new Pose(60, 30), pickup3Pose))
            .setLinearHeadingInterpolation(scorePose.getHeading(), pickup3Pose.getHeading())
            .build();

    /* This is our scorePickup3 PathChain. We are using a single path with a BezierCurve (curved line). */
    scorePickup3 = follower.pathBuilder()
            .addPath(new BezierCurve(pickup3Pose,new Pose(60, 30), scorePose))
            .setLinearHeadingInterpolation(pickup3Pose.getHeading(), scorePose.getHeading())
            .build();

    /* This is our leave PathChain. We are using a single path using a BezierLine (straight line).
     * We use Constant Interpolation here instead of Linear*/
    leave = follower.pathBuilder()
            .addPath(new BezierLine(scorePose, endPose))
            .setConstantHeadingInterpolation(scorePose.getHeading())
            .build();
}
```

## Step Four: Building the Autonomous Routine

We strongly recommend using [**Ivy**](/docs/ivy), the official command library for Pedro Pathing,
to build your autonomous routine, although an alternative is provided below.
Ivy lets you describe your entire auto as a composition of follow commands and
commands for your other subsystems, which is far more concise, flexible, and less error-prone than managing 
states manually. To learn more about Ivy, check out the [Ivy documentation](/docs/ivy).

With Ivy, the entire autonomous logic is a single `sequential` command composition. Each `follow` command
doesn't complete until follower.isBusy() returns false, meaning you don't need to manually manage that.
If you want to do commands in between paths, you can just add a command in between the follow commands.
You can also use `parallel` compositions to run commands while following paths or to run other sets of commands
together.

```java title="ExampleAuto.java"
public Command autoRoutine() {
    return sequential(
            /* Go To Score Command*/
            follow(follower, scorePreload),
            /* Collect 3 Artifacts Command*/
            follow(follower, grabPickup1, true),
            /* Go Back To Score Command*/
            follow(follower, scorePickup1, true),
            /* Collect 3 Artifacts Command*/
            follow(follower, grabPickup2, true),
            /* Go Back To Score Command*/
            follow(follower, scorePickup2, true),
            /* Collect 3 Artifacts Command*/
            follow(follower, grabPickup3, true),
            /* Go Back To Score Command*/
            follow(follower, scorePickup3, true),
            /* Leave Start Line Command*/
            follow(follower, leave, true)
    );
}
```

## Step Five: Init and Loop Methods
The initialization phase sets up our paths and builds the auto command, while the loop runs the
scheduler and updates the follower.

```java title="ExampleAuto.java"
@Override
public void runOpMode() {
    //These will run when the OpMode is initiated
    Scheduler.reset();
    follower = Constants.createFollower(hardwareMap);
    buildPaths();
    follower.setStartingPose(startPose);

    waitForStart();
    //We schedule all our commands when we start the OpMode
    schedule(autoRoutine());
    while (opModeIsActive()) {
        //Update the follower and execute the scheduler every loop
        follower.update();
        Scheduler.execute();

        // Feedback to Driver Hub for debugging
        telemetry.addData("x", follower.getPose().getX());
        telemetry.addData("y", follower.getPose().getY());
        telemetry.addData("heading", follower.getPose().getHeading());
        telemetry.update();
    }
}
```

---

## Alternative: Finite State Machine

If you prefer not to use Ivy or any command base, you can manage path progression manually using a
finite state machine (FSM). The `pathState` variable tracks where the robot is in the routine, and
the switch statement transitions between states based on conditions like `!follower.isBusy()`.

This approach requires additional imports and variables:

```java title="ExampleAuto.java"
import com.pedropathing.util.Timer;

private Timer pathTimer, opmodeTimer;
private int pathState;
```

Below is the state manager. The `followPath()` function tells the follower to run a path but does
NOT wait for it to finish. Instead, the robot transitions between states based on conditions in
each `if` statement.

```java title="ExampleAuto.java"
public void autonomousPathUpdate() {
    switch (pathState) {
        case 0:
            follower.followPath(scorePreload);
            setPathState(1);
            break;
        case 1:

            /* You could check for
            - Follower State: "if(!follower.isBusy()) {}"
            - Time: "if(pathTimer.getElapsedTimeSeconds() > 1) {}"
            - Robot Position: "if(follower.getPose().getX() > 36) {}"
            */

            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the scorePose's position */
            if(!follower.isBusy()) {
                /* Score Preload */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are grabbing the sample */
                follower.followPath(grabPickup1,true);
                setPathState(2);
            }
            break;
        case 2:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the pickup1Pose's position */
            if(!follower.isBusy()) {
                /* Grab Sample */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are scoring the sample */
                follower.followPath(scorePickup1,true);
                setPathState(3);
            }
            break;
        case 3:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the scorePose's position */
            if(!follower.isBusy()) {
                /* Score Sample */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are grabbing the sample */
                follower.followPath(grabPickup2,true);
                setPathState(4);
            }
            break;
        case 4:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the pickup2Pose's position */
            if(!follower.isBusy()) {
                /* Grab Sample */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are scoring the sample */
                follower.followPath(scorePickup2,true);
                setPathState(5);
            }
            break;
        case 5:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the scorePose's position */
            if(!follower.isBusy()) {
                /* Score Sample */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are grabbing the sample */
                follower.followPath(grabPickup3,true);
                setPathState(6);
            }
            break;
        case 6:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the pickup3Pose's position */
            if(!follower.isBusy()) {
                /* Grab Sample */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are scoring the sample */
                follower.followPath(scorePickup3, true);
                setPathState(7);
            }
            break;
        case 7:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the pickup3Pose's position */
            if(!follower.isBusy()) {
                /* Grab Sample */

                /* Since this is a pathChain, we can have Pedro hold the end point while we are scoring the sample */
                follower.followPath(leave, true);
                setPathState(8);
            }
            break;
        case 8:
            /* This case checks the robot's position and will wait until the robot position is close (1 inch away) from the scorePose's position */
            if(!follower.isBusy()) {
                /* Set the state to a Case we won't use or define, so it just stops running an new paths */
                setPathState(-1);
            }
            break;
    }
}

/** These change the states of the paths and actions. It will also reset the timers of the individual switches **/
public void setPathState(int pState) {
    pathState = pState;
    pathTimer.resetTimer();
}
```

The FSM init and loop methods look like this:

```java title="ExampleAuto.java"
@Override
public void runOpMode {
    pathTimer = new Timer();
    opmodeTimer = new Timer();
    opmodeTimer.resetTimer();

    follower = Constants.createFollower(hardwareMap);
    buildPaths();
    follower.setStartingPose(startPose);

    waitForStart();
    //on start
    opmodeTimer.resetTimer();
    setPathState(0);

    while (opModeIsActive) {
        follower.update();
        autonomousPathUpdate();
    
        // Feedback to Driver Hub for debugging
        telemetry.addData("path state", pathState);
        telemetry.addData("x", follower.getPose().getX());
        telemetry.addData("y", follower.getPose().getY());
        telemetry.addData("heading", follower.getPose().getHeading());
        telemetry.update();
    }
}
```
