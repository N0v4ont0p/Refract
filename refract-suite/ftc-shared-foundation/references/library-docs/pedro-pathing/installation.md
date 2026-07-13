> Source: https://pedropathing.com/docs/pathing · Fetched: 2026-07-12

# Pedro Pathing — Introduction & Installation

> Source: https://pedropathing.com/docs/pathing · Fetched: 2026-07-12

## Introduction

Pedro Pathing is a **path follower** initially developed by [FTC
team 10158](https://ftcscout.org/teams/10158?season=2023) to revolutionize
autonomous navigation in robotics. Pedro Pathing uses Bézier curves, PIDF
control, centripetal force correction, and more to provide smooth, fast, and
accurate path following.

Using Pedro Pathing for your autonomous routines allows for:

- **Faster path execution:** Pedro Pathing uses four vectors to calculate
optimal wheel powers.
- **Correction for disturbances:** Since localization allows Pedro Pathing
to know your robot's position, it can correct for disturbances and get back
on the path.
- **Creating paths on-the-fly:** Since Pedro Pathing uses PID control, it
can instantly go to any position.

No matter how good your team is, Pedro Pathing can give you the tools
necessary to create high-quality, fast, consistent autos.

### Prerequisites

To use Pedro Pathing, you must:

- **Have an omnidirectional drive**, such as mecanum, x-drive, or swerve.
This is most drives except for tank.
- **Have some form of localization**. This can be dead wheels, the goBILDA
Pinpoint,
the SparkFun OTOS, or more. If you don't want to buy anything, you can use
your drive motor encoders.
- **Be using Android Studio**. Pedro Pathing does not work with OnBot Java
or Blocks. If you are not using Android Studio, you should give it a try!

### Tuning

For Pedro Pathing to work properly with your robot, it must be tuned first.
This process is designed to be very approachable and should take at most a
few days.

Pedro Pathing also requires localization, or knowing where your robot is on
the field. There are many forms of localization for you to choose from.

---

> Source: https://pedropathing.com/docs/pathing/installation · Fetched: 2026-07-12

## Installation

There are two ways to install Pedro Pathing.

### Using the Quickstart

The quickstart is the easiest way to install Pedro Pathing.

1. In Android Studio, go to `Main Menu -> File -> New -> Project from
Version Control`. For the URL, enter
`https://github.com/Pedro-Pathing/Quickstart.git`.
2. **OR** run `git clone https://github.com/Pedro-Pathing/Quickstart.git`.
Make sure you have [git](https://git-scm.com/) installed first.

That's it! You have now installed Pedro Pathing.

### Manually

In your `build.dependencies.gradle`, add the following to the `repositories
{ }` block:

```groovy
maven { url = "https://mymaven.bylazar.com/releases" }
```

Then, add the following to the `dependencies { }` block:

_(Note: the live docs site injects the current Pedro Pathing Maven coordinate here via a dynamic component; the exact version string is not present in the static source. See https://pedropathing.com/docs/pathing/installation for the current version, or the Quickstart repo's build.gradle.)_

```groovy
implementation 'com.bylazar:fullpanels:1.0.12'
```

Next, perform a Gradle sync by pressing "sync now" in the blue banner that
has appeared.

Then, navigate to `File > Project Structure > Modules` and change the `Compile Sdk Version` to 34 for `FtcRobotController` and `TeamCode`.
Then press `Apply` and `OK`.

Lastly, copy the files from the [`pedroPathing` package in the quickstart](https://github.com/Pedro-Pathing/Quickstart/tree/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedroPathing)
into your code.

---

> Source: https://pedropathing.com/docs/pathing/dashboard · Fetched: 2026-07-12

## Choosing a Dashboard

It is best to use Pedro Pathing with a dashboard to assist in tuning and
viewing paths live. You may use either [Panels](https://panels.bylazar.com)
or the [FTC Dashboard](https://acmerobotics.github.io/ftc-dashboard). The
quickstart comes with Panels installed by default. If you are not using the
quickstart or would like to use FTC Dashboard instead, follow the
installation instructions on the dashboard of your choice.

### Panels

Panels is an intuitive, real-time dashboard for FTC. It supports live tuning
of constants, visualizing the robot on the field, and logging & graphing the
robot's state live. It is fully supported by Pedro Pathing and accessible at the ip address
`192.168.43.1:8001` when connected to robot wifi.

### FTC Dashboard

The FTC Dashboard is a web app for monitoring FTC robots during operation.
Like Panels, it supports visualizing the robot on the field and logging &
graphing the robot's state live. However, because of the complexity of Pedro
Pathing's constants, it does not support live tuning of Pedro Pathing.

### Drawing Class
For either option, it is likely that you will want to use the field view optionality.
Built in to the Quickstart is the Drawing class for Panels, located in the `Tuning.java` file.
This class is in charge of drawing the robot and its paths on to the field view to show live position and desired position and path.
You should be able to copy and paste either of these two for your selected dashboard of choice.

#### FTC Dash

You will have to remove the @Configurable annotations from the Tuning class in favor for the @Config annotation.
Also remove any @IgnoreConfigurable annotations.
All of the Tuning classes use Panels `telemetryM.debug()` and `telemetryM.update()` methods, those will have to be replaced by `telemetryA.addLine()` and `telemetryA.update()`.

At the top of the file, add these imports:
```java
import com.acmerobotics.dashboard.FtcDashboard;
import com.acmerobotics.dashboard.canvas.Canvas;
import com.acmerobotics.dashboard.telemetry.TelemetryPacket;
import com.acmerobotics.dashboard.config.Config;
import com.acmerobotics.dashboard.telemetry.MultipleTelemetry;
```

Replace or add this code as the Drawing class:
```java
/**
 * This is the Drawing class. It handles the drawing of stuff on FTC Dashboard, like the robot.
 *
 * @author Logan Nash
 * @author Anyi Lin - 10158 Scott's Bots
 * @version 2.0, 11/03/2025
 */
class Drawing {
    public static final double ROBOT_RADIUS = 9;
    private static TelemetryPacket packet;

    /**
     * This draws everything that will be used in the Follower's telemetryDebug() method. This takes
     * a Follower as an input, so an instance of the DashboardDrawingHandler class is not needed.
     *
     * @param follower
     */
    public static void drawDebug(Follower follower) {
        if (follower.getCurrentPath() != null) {
            drawPath(follower.getCurrentPath(), "#3F51B5");
            Pose closestPoint = follower.getPointFromPath(follower.getCurrentPath().getClosestPointTValue());
            drawRobot(new Pose(closestPoint.getX(), closestPoint.getY(), follower.getCurrentPath().getHeadingGoal(follower.getCurrentPath().getClosestPointTValue())), "#3F51B5");
        }
        drawPoseHistory(follower.getPoseHistory(), "#4CAF50");
        drawRobot(follower.getPose(), "#4CAF50");
        sendPacket();
    }

    /**
     * This adds instructions to the current packet to draw a robot at a specified Pose with a specified
     * color. If no packet exists, then a new one is created.
     *
     * @param pose the Pose to draw the robot at
     * @param color the color to draw the robot with
     */
    public static void drawRobot(Pose pose, String color) {
        if (packet == null) packet = new TelemetryPacket();
        packet.fieldOverlay().setStroke(color);
        Drawing.drawRobotOnCanvas(packet.fieldOverlay(), pose.copy());
    }

    /**
     * This adds instructions to the current packet to draw a Path with a specified color. If no
     * packet exists, then a new one is created.
     *
     * @param path the Path to draw
     * @param color the color to draw the Path with
     */
    public static void drawPath(Path path, String color) {
        if (packet == null) packet = new TelemetryPacket();
        packet.fieldOverlay().setStroke(color);
        Drawing.drawPath(packet.fieldOverlay(), path.getPanelsDrawingPoints());
    }

    /**
     * This adds instructions to the current packet to draw all the Paths in a PathChain with a
     * specified color. If no packet exists, then a new one is created.
     *
     * @param pathChain the PathChain to draw
     * @param color the color to draw the PathChain with
     */
    public static void drawPath(PathChain pathChain, String color) {
        for (int i = 0; i < pathChain.size(); i++) {
            drawPath(pathChain.getPath(i), color);
        }
    }

    /**
     * This adds instructions to the current packet to draw the pose history of the robot. If no
     * packet exists, then a new one is created.
     *
     * @param poseTracker the DashboardPoseTracker to get the pose history from
     * @param color the color to draw the pose history with
     */
    public static void drawPoseHistory(PoseHistory poseTracker, String color) {
        if (packet == null) packet = new TelemetryPacket();
        packet.fieldOverlay().setStroke(color);
        packet.fieldOverlay().strokePolyline(poseTracker.getXPositionsArray(), poseTracker.getYPositionsArray());
    }

    /**
     * This tries to send the current packet to FTC Dashboard.
     *
     * @return returns if the operation was successful.
     */
    public static boolean sendPacket() {
        if (packet != null) {
            FtcDashboard.getInstance().sendTelemetryPacket(packet);
            packet = null;
            return true;
        }
        return false;
    }

    /**
     * This draws a robot on the Dashboard at a specified Pose. This is more useful for drawing the
     * actual robot, since the Pose contains the direction the robot is facing as well as its position.
     *
     * @param c the Canvas on the Dashboard on which this will draw at
     * @param t the Pose to draw at
     */
    public static void drawRobotOnCanvas(Canvas c, Pose t) {
        if (t == null || Double.isNaN(t.getX()) || Double.isNaN(t.getY()) || Double.isNaN(t.getHeading())) {
            return;
        }

        c.strokeCircle(t.getX(), t.getY(), ROBOT_RADIUS);
        Vector v = t.getHeadingAsUnitVector();
        v.setMagnitude(v.getMagnitude() * ROBOT_RADIUS);
        double x1 = t.getX() + v.getXComponent() / 2, y1 = t.getY() + v.getYComponent() / 2;
        double x2 = t.getX() + v.getXComponent(), y2 = t.getY() + v.getYComponent();
        c.strokeLine(x1, y1, x2, y2);
    }

    /**
     * This draws a Path on the Dashboard from a specified Array of Points.
     *
     * @param c the Canvas on the Dashboard on which this will draw
     * @param points the Points to draw
     */
    public static void drawPath(Canvas c, double[][] points) {
        c.strokePolyline(points[0], points[1]);
    }
}
```

#### Panels
The Quickstart comes preinstalled with Panels and already holds the Panels Drawing class.
If you want to revert back to Panels from dashboard, follow the steps for Dashboard in reverse or redownload the `Tuning.java` from the Quickstart.

Add these imports at the top of the `Tuning.java` file:
```java
import com.bylazar.configurables.annotations.Configurable;
import com.bylazar.configurables.annotations.IgnoreConfigurable;
import com.bylazar.configurables.PanelsConfigurables;
import com.bylazar.field.FieldManager;
import com.bylazar.field.PanelsField;
import com.bylazar.field.Style;
import com.bylazar.telemetry.PanelsTelemetry;
import com.bylazar.telemetry.TelemetryManager;
```

Replace or add this code as the Drawing class:
```java
/**
 * This is the Drawing class. It handles the drawing of stuff on Panels Dashboard, like the robot.
 *
 * @author Lazar - 19234
 * @version 1.1, 5/19/2025
 */
class Drawing {
    public static final double ROBOT_RADIUS = 9; // woah
    private static final FieldManager panelsField = PanelsField.INSTANCE.getField();

    private static final Style robotLook = new Style(
            "", "#3F51B5", 0.0
    );
    private static final Style historyLook = new Style(
            "", "#4CAF50", 0.0
    );

    /**
     * This prepares Panels Field for using Pedro Offsets
     */
    public static void init() {
        panelsField.setOffsets(PanelsField.INSTANCE.getPresets().getPEDRO_PATHING());
    }

    /**
     * This draws everything that will be used in the Follower's telemetryDebug() method. This takes
     * a Follower as an input, so an instance of the DashboardDrawingHandler class is not needed.
     *
     * @param follower Pedro Follower instance.
     */
    public static void drawDebug(Follower follower) {
        if (follower.getCurrentPath() != null) {
            drawPath(follower.getCurrentPath(), robotLook);
            Pose closestPoint = follower.getPointFromPath(follower.getCurrentPath().getClosestPointTValue());
            drawRobot(new Pose(closestPoint.getX(), closestPoint.getY(), follower.getCurrentPath().getHeadingGoal(follower.getCurrentPath().getClosestPointTValue())), robotLook);
        }
        drawPoseHistory(follower.getPoseHistory(), historyLook);
        drawRobot(follower.getPose(), historyLook);

        sendPacket();
    }

    /**
     * This draws a robot at a specified Pose with a specified
     * look. The heading is represented as a line.
     *
     * @param pose  the Pose to draw the robot at
     * @param style the parameters used to draw the robot with
     */
    public static void drawRobot(Pose pose, Style style) {
        if (pose == null || Double.isNaN(pose.getX()) || Double.isNaN(pose.getY()) || Double.isNaN(pose.getHeading())) {
            return;
        }

        panelsField.setStyle(style);
        panelsField.moveCursor(pose.getX(), pose.getY());
        panelsField.circle(ROBOT_RADIUS);

        Vector v = pose.getHeadingAsUnitVector();
        v.setMagnitude(v.getMagnitude() * ROBOT_RADIUS);
        double x1 = pose.getX() + v.getXComponent() / 2, y1 = pose.getY() + v.getYComponent() / 2;
        double x2 = pose.getX() + v.getXComponent(), y2 = pose.getY() + v.getYComponent();

        panelsField.setStyle(style);
        panelsField.moveCursor(x1, y1);
        panelsField.line(x2, y2);
    }

    /**
     * This draws a robot at a specified Pose. The heading is represented as a line.
     *
     * @param pose the Pose to draw the robot at
     */
    public static void drawRobot(Pose pose) {
        drawRobot(pose, robotLook);
    }

    /**
     * This draws a Path with a specified look.
     *
     * @param path  the Path to draw
     * @param style the parameters used to draw the Path with
     */
    public static void drawPath(Path path, Style style) {
        double[][] points = path.getPanelsDrawingPoints();

        for (int i = 0; i < points[0].length; i++) {
            for (int j = 0; j < points.length; j++) {
                if (Double.isNaN(points[j][i])) {
                    points[j][i] = 0;
                }
            }
        }

        panelsField.setStyle(style);
        panelsField.moveCursor(points[0][0], points[0][1]);
        panelsField.line(points[1][0], points[1][1]);
    }

    /**
     * This draws all the Paths in a PathChain with a
     * specified look.
     *
     * @param pathChain the PathChain to draw
     * @param style     the parameters used to draw the PathChain with
     */
    public static void drawPath(PathChain pathChain, Style style) {
        for (int i = 0; i < pathChain.size(); i++) {
            drawPath(pathChain.getPath(i), style);
        }
    }

    /**
     * This draws the pose history of the robot.
     *
     * @param poseTracker the PoseHistory to get the pose history from
     * @param style       the parameters used to draw the pose history with
     */
    public static void drawPoseHistory(PoseHistory poseTracker, Style style) {
        panelsField.setStyle(style);

        int size = poseTracker.getXPositionsArray().length;
        for (int i = 0; i < size - 1; i++) {

            panelsField.moveCursor(poseTracker.getXPositionsArray()[i], poseTracker.getYPositionsArray()[i]);
            panelsField.line(poseTracker.getXPositionsArray()[i + 1], poseTracker.getYPositionsArray()[i + 1]);
        }
    }

    /**
     * This draws the pose history of the robot.
     *
     * @param poseTracker the PoseHistory to get the pose history from
     */
    public static void drawPoseHistory(PoseHistory poseTracker) {
        drawPoseHistory(poseTracker, historyLook);
    }

    /**
     * This tries to send the current packet to FTControl Panels.
     */
    public static void sendPacket() {
        panelsField.update();
    }
}
```

---

> Source: https://pedropathing.com/docs/pathing/constants · Fetched: 2026-07-12

## Constants

You may have noticed that there is a `Constants` file in the `pedroPathing`
package. This is where you configure all your constants for Pedro. It
contains four types of constants:

1. **Follower constants** consist of values from the
automatic, PID, and centripetal tuners.
2. **Drivetrain constants** contain constants specific to your drivetrain
type. For example, mecanum drivetrain constants contain the motor names.
3. **Localizer constants** contain constants specific to your localizer. For
example, OTOS constants include the hardware map name of the OTOS and the
offset.
4. **Path constraints** determine under what conditions a path may end.

There is also a `createFollower` method that constructs the follower. You
will call this method in your OpModes.

Below is a starting `Constants` file. The different tuning pages will guide
you through modifying it to suit your robot.

```java title="Constants.java"
public class Constants {
    public static FollowerConstants followerConstants = new FollowerConstants();

    public static PathConstraints pathConstraints = new PathConstraints(0.99, 100, 1, 1);

    public static Follower createFollower(HardwareMap hardwareMap) {
        return new FollowerBuilder(followerConstants, hardwareMap)
                .pathConstraints(pathConstraints)
                .build();
    }
}
```

---

> Source: https://pedropathing.com/docs/pathing/faq · Fetched: 2026-07-12

## FAQ

---

> Source: https://pedropathing.com/docs/pathing/troubleshooting · Fetched: 2026-07-12

## Troubleshooting

If you have trouble during your tuning, this page may cover some common issues that are had, just click to expand the dropdown.
Otherwise, join the [Pedro Pathing Discord](https://discord.gg/2GfC4qBP5s) and ask in #general or in the #tuning-help channels. When asking in #tuning-help, please provide additional infomation other than your issue. This could be a video, your constants, telemetry outputs, logcat, or any other infomation.

##### Bad Localization

**If you're using a two wheel localizer:**

Check whether:
- Your encoder's `HardwareMapName` is incorrect or if the parallel & perpendicular odometry pods' names are swapped.
- Your encoders directions are reversed.
- Your IMU orientations (`LogoFacingDirection`, `UsbFacingDirection`) are incorrect.
- Your odometry pod offests are inaccurate

Try also running `Forward Tuner` and `Lateral Tuner` more times to get more accurate results for `forwardTicksToInches` and `strafeTicksToInches`.

**If you're using a three wheel localizer:**

Check whether:
- Your encoder's `HardwareMapName` is incorrect or if a parallel & perpendicular odometry pods' names are swapped (will result in robot rotating and translating if swapped).
- Your encoders directions are reversed.
- Your IMU orientations (`LogoFacingDirection`, `UsbFacingDirection`) are incorrect (only for Three Wheel IMU).
- Your odometry pod offests are inaccurate

##### Robot Turns 180 and Oscillates During Heading Tuner

This behavior is due to incorrect motor hardwareMap associations.
Usually, this means that the front motors need to be swapped with the rear motors.
Or that your odometry offsets offsets have the wrong sign.
Try testing that the motors are correctly associated with their hardwareMap names by running the Tuning OpMode and navigating `Localization > Motor Directions` to test.
It may require you to swap hardwareMap names or the ports in which motors are plugged into.

##### Robot Drifts Turning Drive Tuner

**If you're using a drive encoders, two wheel, three wheel, or OTOS,** a small amount of drift will happen over time, as these localizer's aren't perfect.
However, the tolerence should remain manageable for the entire 30 second autonomous period.

##### Robot Movements are Too Jittery

Check your `brakingStrength` in `PathConstraints` and try decreasing it slightly. This will make the braking smoother and reduce the
oscillations.

##### Robot Never Stops during ForwardVelocityTest or StrafeVelocityTest

- This usually happens when your localization is inaccurate, causing the robot to think that it's driving in the opposite direction that it is actually moving in.
- Run `LocalizationTest` and check:
    - when you move the robot forward, does the x-value increase?
    - when you move the robot to the left, does the y-value increase?
    - is the reported heading accurate?
- If not, head over back to the localization section and double check your steps. You most likely need to reverse one or more of your encoders.
Ensure that your localization is fully accurate before running automatic tuners and tuning PIDFs.

##### Robot Moves in the Wrong Direction during a Tuning Program

**Check if:**
- Your localization is inaccurate. Run `LocalizationTest` and check:
    - when you move the robot forward, does the x-value increase?
    - when you move the robot to the left, does the y-value increase?
    - is the reported heading accurate?
If not, head over back to the localization section and double check your steps.
Ensure that your localization is fully accurate before running automatic tuners and tuning your PIDFs.
- Your motor directions are reversed.
- Your motor configurations are incorrect.

##### Robot Never Moves During TranslationalTuner or HeadingTuner

**If you are tuning for Translational or Heading PIDF, it is intentional that the robot doesn't initially move.**
However, if you push/turn the robot and it still doesn't move, check whether your P value in the PIDF is too low. Increasing it may give more power for your robot to correct back to its original position.

##### Cannot See the Constants in Panels

    If the Tuning class dropdown in the Panels Configurables is empty, double check that you have selected an OpMode in the Tuning OpMode using the gamepad before reloading the Panels website. The Panels website is accessible at the ip address
`192.168.43.1:8001` when connected to robot wifi.

##### Robot Moves in Wrong Direction or Robot Encoder Counting Inaccurately

**My robot drives infinitely in automatic tuners:**
- If your robot drives forever in a direction, reverse the respective encoder to that direction.

**My robot does not drive the correct way in TeleOp / Localization is not working:**
    1. Run the LocalizationTest OpMode
    2. Use gamepad1 joysticks to move around:
        - Left Stick Y: Forward and Backwards
        - Left Stick X: Strafe Left and Right
        - Right stick: Rotation
    3. If movement directions are wrong then run the Motor Directions OpMode, there is a button to make the motors spin forward, if it spins backwards instead then change the reversal.

For more information on how mecanum wheels move, refer to [this image](https://cdn11.bigcommerce.com/s-x56mtydx1w/images/stencil/original/products/2005/10985/3213-3606-0003-Product-Insight-4__96315__10052.1701994274.png?c=1) provided by goBILDA®.

---

> Source: https://pedropathing.com/docs/pathing/pedro-v-roadrunner · Fetched: 2026-07-12

## PedroPathing vs Roadrunner

For FTC when it comes to path following, there are two main solutions, **Road Runner 1.0** and **Pedro Pathing**.
Although both are designed to achieve the same task, each has its own benefits and tradeoffs. The table provides an abbreviated list of features. For more information, read the *paragraphs* provided below.

### Table

| Aspect                  | Pedro Pathing                                                                                                                                                                                                                                                                                                                               | RoadRunner                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Following Strategy      | Uses three PID controllers: translational, heading, and drive, along with centripetal force correction.                                                                                                                                                                                                                                     | Generates and follows motion-profiled trajectories by using a combination of feedforward and feedback control.                                                                                                                                                             |
| Visualizer              | Has a no-code, web-based [path generator and visualizer](https://visualizer.pedropathing.com) that can export code for paths.                                                                                                                                                                                                               | Has a code-based [path visualizer](https://github.com/acmerobotics/meepmeep) that visualizes paths defined in code.                                                                                                                                                        |
| Tuning                  | Half automatic and half manual. Has six automatic tuning steps and four manual tuning steps, although the manual steps take slightly longer.                                                                                                                                                                                                | Mostly automatic. Has four automatic tuning steps and two manual tuning steps, although the manual steps take slightly longer. If using the SparkFun OTOS for localization there are four additional automatic tuning steps.                                               |
| Loop Time Optimizations | Automatically implements motor write caching with a configurable cache tolerance.                                                                                                                                                                                                                                                           | Automatically implements bulk reading.                                                                                                                                                                                                                                     |
| Good At                 | Correction for unexpected disturbances.                                                                                                                                                                                                                                                                                                     | Time-consistent trajectory following.                                                                                                                                                                                                                                      |
| Coordinate System       | Custom coordinate system. Provides a `PoseConverter` for converting to and from the official FIRST coordinate system.                                                                                                                                                                                                                       | Uses the official FIRST coordinate system.                                                                                                                                                                                                                                 |
| Command System          | [Ivy](/docs/ivy) is the official command library for Pedro Pathing. Since Ivy is a separate library, Pedro also remains compatible with other command bases like [NextFTC](https://nextftc.dev), [SolversLib](https://docs.seattlesolvers.com), and [Mercurial](https://docs.dairy.foundation/Samples/user_samples). | Has a built-in actions system. Also has an example on the docs for usage with FTCLib. [NextFTC](https://nextftc.dev) provides built-in integration with RoadRunner. Mercurial has [two sample repos](https://docs.dairy.foundation/Samples/user_samples) using RoadRunner. |
| Logging                 | Automatically logs many values to telemetry, but does not log to a file. Data such as current position can be logged by the user by using a third-party library such as [PsiKit](https://psilynx.github.io/PsiKit) for replay with [AdvantageScope](https://advantagescope.org).                                                            | Logs many values automatically to telemetry and to a file during every OpMode run. Uses a custom log format that is supported by [AdvantageScope](https://advantagescope.org).                                                                                             |
| Drivetrain Support      | Has built-in support for mecanum drivetrains. Users can provide a custom implementation of the `Drivetrain` interface to use another drivetrain, but does not support nonholonomic drivetrains such as tank.                                                                                                                                | Has built-in support for mecanum and tank drivetrains. Does not support any other drivetrains.                                                                                                                                                                             |

### In-depth Information
**Pros and Cons of Road Runner:**
Road Runner typically prioritizes time consistency above all else, using pre-planned motion profiling.
This allows the following of full trajectories with preset speed and acceleration constraints created by the user.
The Road Runner tuning pass is nearly automatic, making it more accessible for many users (although the actual
tuning time doesn't necessarily vary too much from Pedro Pathing).
Due to prioritizing time-consistency, Road Runner defaults to about 80% of the robot's maximum speed when path-following,
a major drawback. Furthermore, the motion model doesn't account for the reduced speed due to strafing which can often
produce inaccurate motion. Road Runner has a built-in action system, but you cannot use any other action system in
conjunction with Road Runner. If a user uses a certain external command-base in their TeleOp, they cannot use it in auto.

**Pros and Cons of Pedro Pathing:**
Pedro Pathing typically prioritizes speed and precision while following the path. The follower corrects the robot
back to the target position when outside forces create inaccuracies in the robot's position or heading, while still
following the path. Pedro Pathing also uses centripetal force correction, so it is able to follow curved paths better.
Similar to custom p2p and Pure Pursuit algorithms, Pedro Pathing typically moves the robot along the path much faster than Road Runner.
[Ivy](/docs/ivy) is the official command library for Pedro Pathing, providing a concise, flexible, and
powerful way to organize autonomous routines and manage teleop actions. Since Ivy is a separate dependency rather than
built into Pedro, users are also free to use other command bases like NextFTC, SolversLib, or Mercurial if they prefer.
A major advantage of Pedro Pathing is its path visualizer. The visualizer is web-based, doesn't require the user to write
any code, and even generates code for the user. The visualizer is also typically considered to be easier to use, since
"eyeballing paths" can be done by arbitrarily dragging control points until a desired path is achieved. To assist in storage,
these paths can then be exported concisely into a single, re-uploadable file.

{/* Thanks to Davis for the table */}

