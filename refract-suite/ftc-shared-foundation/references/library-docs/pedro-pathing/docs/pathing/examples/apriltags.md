> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/examples/apriltags.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Example AprilTag Usage
description: How to use AprilTags with Pedro Pathing
---

This page gives pseudocode for using AprilTags in conjunction with Pedro Pathing's follower. The easiest way to do this is using a custom localizer or relocalization (as shown below). We look forward to seeing what teams are able to accomplish with AprilTags!

## Step One: Setting up imports and variables
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
