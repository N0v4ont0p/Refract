> Source: https://pedropathing.com/docs/pathing/examples/auto · Fetched: 2026-07-12

# Pedro Pathing — Example OpModes

> Source: https://pedropathing.com/docs/pathing/examples/auto · Fetched: 2026-07-12

## Example Auto

This pages gives an overview of how to create an autonomous routine using PedroPathing. In this example, we write an autonomous for the 25-26 season DECODE. The robot starts against the blue goal, scores its preloads and completes three cycles of picking up and scoring, and showcases several different methods for building paths. A path progression system is  also implemented, allowing the routine to advance based on time, position, or other custom conditions.

### Step One: Setting up imports and variables
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

### Step Two: Initializing poses
Poses are points on the field coordinate system that define the (`x`, `y`, `heading`) of your robot during the autonomous. Pedro’s coordinate system spans an interval of [0, 144] on both the x and y axes, with (0, 0) defined as the bottom-left corner of the field. To see more about the coordinate system, navigate to: [Coordinates](/docs/pathing/reference/coordinates). Even though Pedro uses a different coordinate system than RR, you can convert any roadrunner pose by adding +72 both the x and y. Below are the poses for our example autonomous:

```java title="ExampleAuto.java"
private final Pose startPose = new Pose(22, 122, Math.toRadians(324)); // Start Pose of our robot. This is against the goal facing AWAY
private final Pose scorePose = new Pose(60, 84, Math.toRadians(135)); // Scoring Pose of our robot.
private final Pose pickup1Pose = new Pose(17, 84, Math.toRadians(180)); // Highest (First Set) of Artifacts from the Spike Mark.
private final Pose pickup2Pose = new Pose(12, 60, Math.toRadians(180)); // Middle (Second Set) of Artifacts from the Spike Mark.
private final Pose pickup3Pose = new Pose(12, 36, Math.toRadians(180)); // Lowest (Third Set) of Artifacts from the Spike Mark.
private final Pose endPose = new Pose (60, 105); // Final Pose of our robot, off the starting line
```

### Step Three: Path Initializing
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

### Step Four: Building the Autonomous Routine

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

### Step Five: Init and Loop Methods
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

### Alternative: Finite State Machine

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

---

> Source: https://pedropathing.com/docs/pathing/examples/teleop · Fetched: 2026-07-12

## Example TeleOp

```java
package org.firstinspires.ftc.teamcode.pedroPathing;
import com.bylazar.configurables.annotations.Configurable;
import com.bylazar.telemetry.PanelsTelemetry;
import com.bylazar.telemetry.TelemetryManager;
import com.pedropathing.follower.Follower;
import com.pedropathing.geometry.BezierLine;
import com.pedropathing.geometry.Pose;
import com.pedropathing.paths.HeadingInterpolator;
import com.pedropathing.paths.Path;
import com.pedropathing.paths.PathChain;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

import java.util.function.Supplier;

@Configurable
@TeleOp
public class ExampleTeleOp extends OpMode {
    private Follower follower;
    public static Pose startingPose; //See ExampleAuto to understand how to use this
    private boolean automatedDrive;
    private Supplier<PathChain> pathChain;
    private TelemetryManager telemetryM;
    private boolean slowMode = false;
    private double slowModeMultiplier = 0.5;

    @Override
    public void init() {
        follower = Constants.createFollower(hardwareMap);
        follower.setStartingPose(startingPose == null ? new Pose() : startingPose);
        follower.update();
        telemetryM = PanelsTelemetry.INSTANCE.getTelemetry();

        pathChain = () -> follower.pathBuilder() //Lazy Curve Generation
                .addPath(new Path(new BezierLine(follower::getPose, new Pose(54, 94))))
                .setHeadingInterpolation(HeadingInterpolator.linearFromPoint(follower::getHeading, Math.toRadians(135), 0.8))
                .build();
        //Lazy curve generation might look a little different to how we usually make paths,
        //This is because we are using a Lambda expression instead of calling follower.pathbuilder()
        //To use this though, we declare this as a Supplier<PathChain>. And we to call the path chain we instead do pathChain.get()
    }

    @Override
    public void start() {
        //The parameter controls whether the Follower should use break mode on the motors (using it is recommended).
        //In order to use float mode, add .useBrakeModeInTeleOp(true); to your Drivetrain Constants in Constant.java (for Mecanum)
        //If you don't pass anything in, it uses the default (false)
        follower.startTeleopDrive();
    }

    @Override
    public void loop() {
        //Call this once per loop
        follower.update();
        telemetryM.update();

        if (!automatedDrive) {
            //Make the last parameter false for field-centric
            //In case the drivers want to use a "slowMode" you can scale the vectors

            //This is the normal version to use in the TeleOp
            if (!slowMode) follower.setTeleOpDrive(
                    -gamepad1.left_stick_y,
                    -gamepad1.left_stick_x,
                    -gamepad1.right_stick_x,
                    true // Robot Centric
            );

            //This is how it looks with slowMode on
            else follower.setTeleOpDrive(
                    -gamepad1.left_stick_y * slowModeMultiplier,
                    -gamepad1.left_stick_x * slowModeMultiplier,
                    -gamepad1.right_stick_x * slowModeMultiplier,
                    true // Robot Centric
            );
        }

        //Automated PathFollowing
        if (gamepad1.aWasPressed()) {
            follower.followPath(pathChain.get());
            automatedDrive = true;
        }

        //Stop automated following if the follower is done
        if (automatedDrive && (gamepad1.bWasPressed() || !follower.isBusy())) {
            follower.startTeleopDrive();
            automatedDrive = false;
        }

        //Slow Mode
        if (gamepad1.rightBumperWasPressed()) {
            slowMode = !slowMode;
        }

        //Optional way to change slow mode strength
        if (gamepad1.xWasPressed()) {
            slowModeMultiplier += 0.25;
        }

        //Optional way to change slow mode strength
        if (gamepad2.yWasPressed()) {
            slowModeMultiplier -= 0.25;
        }

        telemetryM.debug("position", follower.getPose());
        telemetryM.debug("velocity", follower.getVelocity());
        telemetryM.debug("automatedDrive", automatedDrive);
    }
}
```

---

> Source: https://pedropathing.com/docs/pathing/examples/apriltags · Fetched: 2026-07-12

## Example AprilTag Usage

This page gives pseudocode for using AprilTags in conjunction with Pedro Pathing's follower. The easiest way to do this is using a custom localizer or relocalization (as shown below). We look forward to seeing what teams are able to accomplish with AprilTags!

### Step One: Setting up imports and variables
Ensure to include the required imports for the autonomous. **Note: Make sure the package statement aligns
with that of where your class files are actually located. Android Studio should automatically generate it when
creating a class**

```java title="ExampleRobotCentricTeleOp"
package org.firstinspires.ftc.teamcode.pedroPathing;

import com.pedropathing.follower.Follower;
import com.pedropathing.ftc.FTCCoordinates;
import com.pedropathing.geometry.BezierLine;
import com.pedropathing.geometry.PedroCoordinates;
import com.pedropathing.geometry.Pose;
import com.qualcomm.hardware.limelightvision.Limelight3A;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

@TeleOp
public class ExampleAprilTagUsage extends OpMode {
    private Limelight3A camera; //any camera here
    private Follower follower;
    private boolean following = false;
    private final Pose TARGET_LOCATION = new Pose(); //Put the target location here

    @Override
    public void init() {
        camera = hardwareMap.get(Limelight3A.class, "limelight");
        follower = Constants.createFollower(hardwareMap);
        follower.setStartingPose(new Pose()); //set your starting pose
    }

    @Override
    public void start() {
        camera.start();
    }

    @Override
    public void loop() {
        follower.update();

        //if you're not using limelight you can follow the same steps: build an offset pose, put your heading offset, and generate a path etc

        if (!following) {
            follower.followPath(
                    follower.pathBuilder()
                            .addPath(new BezierLine(follower.getPose(), TARGET_LOCATION))
                            .setLinearHeadingInterpolation(follower.getHeading(), TARGET_LOCATION.minus(follower.getPose()).getAsVector().getTheta())
                            .build()
            );
        }

        //This uses the aprilTag to relocalize your robot
        //You can also create a custom AprilTag fusion Localizer for the follower if you want to use this by default for all your autos
        follower.setPose(getRobotPoseFromCamera());

        if (following && !follower.isBusy()) following = false;
    }

    private Pose getRobotPoseFromCamera() {
        //Fill this out to get the robot Pose from the camera's output (apply any filters if you need to using follower.getPose() for fusion)
        //Pedro Pathing has built-in KalmanFilter and LowPassFilter classes you can use for this

        //Use this to convert standard FTC coordinates to standard Pedro Pathing coordinates
        //Don't forget to convert any units beforehand to inches
        return new Pose(0, 0, 0, FTCCoordinates.INSTANCE).getAsCoordinateSystem(PedroCoordinates.INSTANCE);
    }
}
```

---

> Source: https://pedropathing.com/docs/pathing/examples/apriltagpatternauto · Fetched: 2026-07-12

## Example Motif Usage

This page gives an example code of how to do one of three patterns based off the MOTIF during autonomous. It responds by moving to the position of one of the three rows of elements. It then will move to the farther triangle to shoot in the goal at a 115 degree angle. Majority of how the code works is explained in the comments, and anything else you can ask about in the official PedroPathing Discord.

```java title="AprilTagPatternAuto"

/*
Hello :D my names mikey and i'm the head of software on team 21721. I was looking at the april tag sample code on the PP (pedro pathing) website and it kinda confused me or just wasn't
what I needed to do, so I decided to make my own! Before you worry about the code itself u need to know a bit about April tags. April tags are basically just QR codes; in the sense
that when you scan them they give u a numerical value. the april tag values for this season are as the following-

Blue Goal: 20
Motif GPP: 21
Motif PGP: 22
Motif PPG: 23
Red Goal: 24

So basically, you lineup your robot in front of the motif april tag. It scans said April Tag and then gives you a value back. You then have three if/then statements where you pretty much
say "if the numeric value is 21, then run the GPP pathbuilder" and so on. Right now, though, the code just has movement. So whenever you get your shooting and intake mechanisms figured out, just add that code in the
designated function and call the function in whichever part of the pathbuilder it is needed. I hope this helps!
*/

package org.firstinspires.ftc.teamcode.examples;

// FTC SDK

import com.bylazar.configurables.annotations.Configurable;
import com.bylazar.telemetry.PanelsTelemetry;
import com.bylazar.telemetry.TelemetryManager;
import com.pedropathing.follower.Follower;
import com.pedropathing.geometry.BezierLine;
import com.pedropathing.geometry.Pose;
import com.pedropathing.paths.PathChain;
import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.util.ElapsedTime;
import org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection;
import org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName;
import org.firstinspires.ftc.teamcode.pedroPathing.Constants;
import org.firstinspires.ftc.vision.VisionPortal;
import org.firstinspires.ftc.vision.apriltag.AprilTagDetection;
import org.firstinspires.ftc.vision.apriltag.AprilTagProcessor;

import java.util.List;

@Autonomous(name = "April Tag with PP test", group = "Opmode")
@Configurable // Panels
@SuppressWarnings("FieldCanBeLocal") // Stop Android Studio from bugging about variables being predefined
public class AprilTagPatternAuto extends LinearOpMode {
    // Initialize elapsed timer
    private final ElapsedTime runtime = new ElapsedTime();

    // Initialize poses
    private final Pose startPose = new Pose(72, 120, Math.toRadians(90)); // Start Pose of our robot.
    private final Pose scorePose = new Pose(72, 20, Math.toRadians(115)); // Scoring Pose of our robot. It is facing the goal at a 115 degree angle.
    private final Pose PPGPose = new Pose(100, 83.5, Math.toRadians(0)); // Highest (First Set) of Artifacts from the Spike Mark.
    private final Pose PGPPose = new Pose(100, 59.5, Math.toRadians(0)); // Middle (Second Set) of Artifacts from the Spike Mark.
    private final Pose GPPPose = new Pose(100, 35.5, Math.toRadians(0)); // Lowest (Third Set) of Artifacts from the Spike Mark.

    // Initialize variables for paths

    private PathChain grabPPG;
    private PathChain scorePPG;
    private PathChain grabPGP;
    private PathChain scorePGP;
    private PathChain grabGPP;
    private PathChain scoreGPP;

    //set April Tag values to specific patterns
    private static final int PPG_TAG_ID = 23;
    private static final int PGP_TAG_ID = 22;
    private static final int GPP_TAG_ID = 21;
    private static final boolean USE_WEBCAM = true;  // Set true to use a webcam, or false for a phone camera
    private VisionPortal visionPortal;               // Used to manage the video source.
    private AprilTagProcessor aprilTag;              // Used for managing the AprilTag detection process.
    private AprilTagDetection desiredTag = null;     // Used to hold the data for a detected AprilTag

    // Other variables
    private Pose currentPose; // Current pose of the robot
    private Follower follower; // Pedro Pathing follower
    private TelemetryManager panelsTelemetry; // Panels telemetry
    private int pathStatePPG; // Current state machine value
    private int pathStatePGP; // Current state machine value
    private int pathStateGPP; // Current state machine value

    private int foundID; // Current state machine value, dictates which one to run

    // Custom logging function to support telemetry and Panels
    private void log(String caption, Object... text) {
        if (text.length == 1) {
            telemetry.addData(caption, text[0]);
            panelsTelemetry.debug(caption + ": " + text[0]);
        } else if (text.length >= 2) {
            StringBuilder message = new StringBuilder();
            for (int i = 0; i < text.length; i++) {
                message.append(text[i]);
                if (i < text.length - 1) message.append(" ");
            }
            telemetry.addData(caption, message.toString());
            panelsTelemetry.debug(caption + ": " + message);
        }
    }

// a place to put your intake and shooting functions
    public void intakeArtifacts() {
        // Put your intake logic/functions here
    }

    public void shootArtifacts() {
        // Put your shooting logic/functions here
    }

    @Override
    public void runOpMode() {
        // Initialize Panels telemetry
        panelsTelemetry = PanelsTelemetry.INSTANCE.getTelemetry();

        // Initialize Pedro Pathing follower
        follower = Constants.createFollower(hardwareMap);
        follower.setStartingPose(startPose);

        boolean targetFound = false;    // Set to true when an AprilTag target is detected
        initAprilTag();

        if (USE_WEBCAM) {
            setManualExposure(6, 250);  // Use low exposure time to reduce motion blur
        }

        // Log completed initialization to Panels and driver station (custom log function)
        log("Status", "Initialized");
        telemetry.update(); // Update driver station after logging

        // Wait for the game to start (driver presses START)
        waitForStart();
        runtime.reset();

        setpathStatePPG(0);
        setpathStatePGP(0);
        setpathStateGPP(0);
        runtime.reset();

        while (opModeIsActive()) {
            // Update Pedro Pathing and Panels every iteration
            follower.update();
            panelsTelemetry.update();
            currentPose = follower.getPose(); // Update the current pose
            targetFound = false;
            desiredTag = null;

            // Step through the list of detected tags and look for a matching tag
            List<AprilTagDetection> currentDetections = aprilTag.getDetections();
            for (AprilTagDetection detection : currentDetections) {
                // Look to see if we have size info on this tag.
                if (detection.metadata != null) {
                    //  Check to see if we want to track towards this tag.
                    if (detection.id == PPG_TAG_ID) {
                        // call lines for the PGP pattern
                        buildPathsPPG();
                        targetFound = true;
                        desiredTag = detection;
                        foundID = 21; // This should likely be PPG_TAG_ID or the corresponding state machine ID
                        break;  // don't look any further.
                    } else if (detection.id == PGP_TAG_ID) {
                        // call lines for the PGP pattern
                        buildPathsPGP();
                        targetFound = true;
                        desiredTag = detection;
                        foundID = 22; // This should likely be PGP_TAG_ID or the corresponding state machine ID
                        break;  // don't look any further.

                    } else if (detection.id == GPP_TAG_ID) {
                        // call lines for the GPP pattern
                        buildPathsGPP();
                        targetFound = true;
                        desiredTag = detection;
                        foundID = 23; // This should likely be GPP_TAG_ID or the corresponding state machine ID
                        break;  // don't look any further.
                    }
                } else {
                    // This tag is NOT in the library, so we don't have enough information to track to it.
                    telemetry.addData("Unknown", "Tag ID %d is not in TagLibrary", detection.id);
                }
            }

            // Update the state machine
            if (foundID == 21) { // Consider using the TAG_ID constants or a dedicated variable for which path was found
                updateStateMachinePPG();
            } else if (foundID == 22) {
                updateStateMachinePGP();
            } else if (foundID == 23) {
                updateStateMachineGPP();
            }

            // Log to Panels and driver station (custom log function)
            log("Elapsed", runtime.toString());
            log("X", currentPose.getX());
            log("Y", currentPose.getY());
            log("Heading", currentPose.getHeading());
            telemetry.update(); // Update the driver station after logging
        }
    }

    public void buildPathsPPG() {
        // basically just plotting the points for the lines that score the PPG pattern

        grabPPG = follower.pathBuilder() //
                .addPath(new BezierLine(startPose, PPGPose))
                .setLinearHeadingInterpolation(startPose.getHeading(), PPGPose.getHeading())
                .build();

        // Move to the scoring pose from the first artifact pickup pose
        scorePPG = follower.pathBuilder()
                .addPath(new BezierLine(PPGPose, scorePose))
                .setLinearHeadingInterpolation(PPGPose.getHeading(), scorePose.getHeading())
                .build();
    }

    public void buildPathsPGP() {
        // basically just plotting the points for the lines that score the PGP pattern

        // Move to the first artifact pickup pose from the start pose
        grabPGP = follower.pathBuilder() // Changed from scorePGP to grabPGP
                .addPath(new BezierLine(startPose, PGPPose))
                .setLinearHeadingInterpolation(startPose.getHeading(), PGPPose.getHeading())
                .build();

        // Move to the scoring pose from the first artifact pickup pose
        scorePGP = follower.pathBuilder()
                .addPath(new BezierLine(PGPPose, scorePose))
                .setLinearHeadingInterpolation(PGPPose.getHeading(), scorePose.getHeading())
                .build();
    }

    public void buildPathsGPP() {
        // basically just plotting the points for the lines that score the GPP pattern

        // Move to the first artifact pickup pose from the start pose
        grabGPP = follower.pathBuilder()
                .addPath(new BezierLine(startPose, GPPPose))
                .setLinearHeadingInterpolation(startPose.getHeading(), GPPPose.getHeading())
                .build();

        // Move to the scoring pose from the first artifact pickup pose
        scoreGPP = follower.pathBuilder()
                .addPath(new BezierLine(GPPPose, scorePose))
                .setLinearHeadingInterpolation(GPPPose.getHeading(), scorePose.getHeading())
                .build();
    }

    //below is the state machine or each pattern

    public void updateStateMachinePPG() {
        switch (pathStatePPG) {
            case 0:
                // Move to the scoring position from the start position
                follower.followPath(grabPPG);
                setpathStatePPG(1); // Call the setter method
                break;
            case 1:
                // Wait until we have passed all path constraints
                if (!follower.isBusy()) {

                    // Move to the first artifact pickup location from the scoring position
                    follower.followPath(scorePPG);
                    setpathStatePPG(-1); //set it to -1 so it stops the state machine execution
                }
                break;
        }
    }

    public void updateStateMachinePGP() {
        switch (pathStatePGP) {
            case 0:
                // Move to the scoring position from the start position
                follower.followPath(grabPGP);
                setpathStatePGP(1); // Call the setter method
                break;
            case 1:
                // Wait until we have passed all path constraints
                if (!follower.isBusy()) {

                    // Move to the first artifact pickup location from the scoring position
                    follower.followPath(scorePGP);
                    setpathStatePGP(-1); // Call the setter for PGP
                }
                break;
        }
    }

    public void updateStateMachineGPP() {
        switch (pathStateGPP) {
            case 0:
                // Move to the scoring position from the start position
                follower.followPath(grabGPP);
                setpathStateGPP(1); // Call the setter method
                break;
            case 1:
                // Wait until we have passed all path constraints
                if (!follower.isBusy()) {

                    // Move to the first artifact pickup location from the scoring position
                    follower.followPath(scoreGPP);
                    setpathStateGPP(-1); //set it to -1 so it stops the state machine execution
                }
                break;
        }
    }

    // Setter methods for pathState variables placed at the class level
    void setpathStatePPG(int newPathState) {
        this.pathStatePPG = newPathState;
    }

    void setpathStatePGP(int newPathState) {
        this.pathStatePGP = newPathState;
    }

    void setpathStateGPP(int newPathState) {
        this.pathStateGPP = newPathState;
    }

    /**
     * start the AprilTag processor.
     */
    private void initAprilTag() {
        // Create the AprilTag processor by using a builder.
        aprilTag = new AprilTagProcessor.Builder().build();

        // Adjust Image Decimation to trade-off detection-range for detection-rate.
        aprilTag.setDecimation(2);

        // Create the vision portal by using a builder.
        if (USE_WEBCAM) {
            visionPortal = new VisionPortal.Builder()
                    .setCamera(hardwareMap.get(WebcamName.class, "Webcam 1"))
                    .addProcessor(aprilTag)
                    .build();
        } else {
            visionPortal = new VisionPortal.Builder()
                    .setCamera(BuiltinCameraDirection.BACK)
                    .addProcessor(aprilTag)
                    .build();
        }
    }

    /*
     Manually set the camera gain and exposure.
     This can only be called AFTER calling initAprilTag(), and only works for Webcams;
    */
    private void setManualExposure(int exposureMS, int gain) {
        // Wait for the camera to be open, then use the controls

        if (visionPortal == null) {
            return;
        }

        // Make sure camera is streaming before we try to set the exposure controls
        if (visionPortal.getCameraState() != VisionPortal.CameraState.STREAMING) {
            telemetry.addData("Camera", "Waiting");
            telemetry.update();
            while (!isStopRequested() && (visionPortal.getCameraState() != VisionPortal.CameraState.STREAMING)) {
                sleep(20);
            }
            telemetry.addData("Camera", "Ready");
            telemetry.update();
        }
        // ExposureControl exposureControl = visionPortal.getCameraControl(ExposureControl.class);
        // if (exposureControl.getMode() != ExposureControl.Mode.Manual) {
        //     exposureControl.setMode(ExposureControl.Mode.Manual);
        //     sleep(50);
        // }
        // exposureControl.setExposure((long)exposureMS, TimeUnit.MILLISECONDS);
        // sleep(20);
        // GainControl gainControl = visionPortal.getCameraControl(GainControl.class);
        // gainControl.setGain(gain);
        // sleep(20);
    }
}
```

---

> Source: https://pedropathing.com/docs/pathing/examples/constants · Fetched: 2026-07-12

## Example Constants

This pages gives an example Pedro Pathing constants file, so you can see where each constant is defined.

```java title="Constants"
package org.firstinspires.ftc.teamcode.pedroPathing;

import com.pedropathing.control.PIDFCoefficients;
import com.pedropathing.control.FilteredPIDFCoefficients;
import com.pedropathing.follower.Follower;
import com.pedropathing.follower.FollowerConstants;
import com.pedropathing.ftc.FollowerBuilder;
import com.pedropathing.ftc.drivetrains.MecanumConstants;
import com.pedropathing.ftc.localization.constants.PinpointConstants;
import com.pedropathing.paths.PathConstraints;
import com.qualcomm.hardware.gobilda.GoBildaPinpointDriver;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.hardware.HardwareMap;

public class Constants {
    public static FollowerConstants followerConstants = new FollowerConstants()
            .mass(16.2)
            .forwardZeroPowerAcceleration(-25.9346931313679598)
            .lateralZeroPowerAcceleration(-67.342491844080064)
            .translationalPIDFCoefficients(new PIDFCoefficients(
                    0.03,
                    0,
                    0,
                    0.015
            ))
            .translationalPIDFSwitch(4)
            .secondaryTranslationalPIDFCoefficients(new PIDFCoefficients(
                    0.4,
                    0,
                    0.005,
                    0.0006
            ))
            .headingPIDFCoefficients(new PIDFCoefficients(
                    0.8,
                    0,
                    0,
                    0.01
            ))
            .secondaryHeadingPIDFCoefficients(new PIDFCoefficients(
                            2.5,
                            0,
                            0.1,
                            0.0005
            ))
            .drivePIDFCoefficients(new FilteredPIDFCoefficients(
                            0.1,
                            0,
                            0.00035,
                            0.6,
                            0.015
            ))
            .secondaryDrivePIDFCoefficients(new FilteredPIDFCoefficients(
                    0.02,
                    0,
                    0.000005,
                    0.6,
                    0.01
            ))
            .drivePIDFSwitch(15)
            .centripetalScaling(0.0005);

    public static MecanumConstants driveConstants = new MecanumConstants()
            .leftFrontMotorName("motor_lf")
            .leftRearMotorName("motor_lb")
            .rightFrontMotorName("motor_rf")
            .rightRearMotorName("motor_rb")
            .leftFrontMotorDirection(DcMotorSimple.Direction.REVERSE)
            .leftRearMotorDirection(DcMotorSimple.Direction.REVERSE)
            .rightFrontMotorDirection(DcMotorSimple.Direction.FORWARD)
            .rightRearMotorDirection(DcMotorSimple.Direction.FORWARD)
            .xVelocity(78.261926752421046666666666666667)
            .yVelocity(61.494551922189565);

    public static PinpointConstants localizerConstants = new PinpointConstants()
            .forwardPodY(0.75)
            .strafePodX(-6.6)
            .forwardEncoderDirection(GoBildaPinpointDriver.EncoderDirection.FORWARD)
            .strafeEncoderDirection(GoBildaPinpointDriver.EncoderDirection.REVERSED);

    /**
    These are the PathConstraints in order:
    tValueConstraint, velocityConstraint, translationalConstraint, headingConstraint, timeoutConstraint,
    brakingStrength, BEZIER_CURVE_SEARCH_LIMIT, brakingStart

    The BEZIER_CURVE_SEARCH_LIMIT should typically be left at 10 and shouldn't be changed.
    */

    public static PathConstraints pathConstraints = new PathConstraints(
            0.995,
            0.1,
            0.1,
            0.009,
            50,
            1.25,
            10,
            1
    );

    //Add custom localizers or drivetrains here
    public static Follower createFollower(HardwareMap hardwareMap) {
        return new FollowerBuilder(followerConstants, hardwareMap)
                .mecanumDrivetrain(driveConstants)
                .pinpointLocalizer(localizerConstants)
                .pathConstraints(pathConstraints)
                .build();
    }
}
```

