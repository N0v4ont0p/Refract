> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/dashboard.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Choosing a Dashboard
description: Panels or the FTC Dashboard
---

It is best to use Pedro Pathing with a dashboard to assist in tuning and
viewing paths live. You may use either [Panels](https://panels.bylazar.com)
or the [FTC Dashboard](https://acmerobotics.github.io/ftc-dashboard). The
quickstart comes with Panels installed by default. If you are not using the
quickstart or would like to use FTC Dashboard instead, follow the
installation instructions on the dashboard of your choice.

## Panels

Panels is an intuitive, real-time dashboard for FTC. It supports live tuning
of constants, visualizing the robot on the field, and logging & graphing the
robot's state live. It is fully supported by Pedro Pathing and accessible at the ip address
`192.168.43.1:8001` when connected to robot wifi.


## FTC Dashboard

The FTC Dashboard is a web app for monitoring FTC robots during operation.
Like Panels, it supports visualizing the robot on the field and logging &
graphing the robot's state live. However, because of the complexity of Pedro
Pathing's constants, it does not support live tuning of Pedro Pathing.


## Drawing Class
For either option, it is likely that you will want to use the field view optionality.  
Built in to the Quickstart is the Drawing class for Panels, located in the `Tuning.java` file.  
This class is in charge of drawing the robot and its paths on to the field view to show live position and desired position and path.
You should be able to copy and paste either of these two for your selected dashboard of choice.

### FTC Dash 

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

### Panels
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

