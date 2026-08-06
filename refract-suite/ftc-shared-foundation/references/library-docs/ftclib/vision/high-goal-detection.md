> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/vision/high-goal-detection.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: Page in progress
---

# High Goal Detection

## `UGBasicHighGoalPipeline`

To use the pipeline, you simply have to call the constructor and have the camera run the pipeline. Ensure that you are still able to access the pipeline object that you have passed into the camera. Refer to [EasyOpenCV](https://github.com/OpenFTC/EasyOpenCV)'s references to using pipelines with your camera device, whether that be the phone camera or an external webcam. For example, creating the pipeline can be seen below:

```java
UGBasicHighGoalPipeline pipeline = new UGBasicHighGoalPipeline();
camera.setPipeline(pipeline);
```

Once the pipeline has been set, in your program, you can then start calling the methods in the pipeline. A very simple way of using the pipeline in your program can be seen below:

```java
// Red Goal
if (pipeline.isRedVisible()) {
    Rect redRect = pipeline.getRedRect();
    Point centerOfRedGoal = pipeline.getCenterofRect(redRect);
    
    telemetry.addData("Red goal position",
                        centerOfRedGoal.toString());
}

// Blue Goal
if (pipeline.isBlueVisible()) {
    Rect blueRect = pipeline.getBlueRect();
    Point centerOfBlueGoal = pipeline.getCenterofRect(blueRect);
    
    telemetry.addData("Blue goal position",
                        centerOfBlueGoal.toString());
}
```

Using these methods given, you can use this point to line your robot up with the goal, as seen in the following sample:

```java
// say we have a point called 'centerOfCamera'
double xDist = Math.abs(centerOfCamera.x - centerOfBlueGoal.x);
double yDist = Math.abs(centerOfCamera.y - centerOfBlueGoal.y);
double dist = Math.hypot(xDist, yDist);

// assume we have a method that turns the robot at some speed,
// but clamps it to [-1, 1]
while (true) {
    if (centerOfCamera.x < centerOfBlueGoal.x - TOLERANCE) {
        turn(dist);    // turning right is positive input
    } else if (centerOfCamera.x > centerOfBlueGoal.x + TOLERANCE) {
        turn(-dist);
    } else {
        turn(0);
        break;
    }
}
```

This is a very rudimentary and crude way of utilizing the pipeline.

## `UGAngleHighGoalPipeline`

Now we get into a more advanced pipeline, the angle pipeline. Its utility is the same as we saw with the basic one. However, this pipeline also allows you to calculate the yaw and pitch of the goal with reference to the camera. Below shows a very simple way of utilizing the pipeline.

```java
// assume we have a PID controller called 'angleController'
while (!angleController.atSetPoint()) {
    double angle = pipeline.calculateYaw(Target.RED);
    double output = angleController.calculate(-angle, 0);
    
    turn(output);
}
turn(0);
```



