> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/ftc-programming · Fetched: 2026-07-12

# FTC Java & Blockly Programming Guide

(Blockly screenshots coming soon, per the source page.)

FTC Limelight Javadoc: [Javadoc](https://javadoc.io/doc/org.firstinspires.ftc/Hardware/latest/com/qualcomm/hardware/limelightvision/package-summary.html)

Basic FTC Example: [FTC Sample](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/SensorLimelight3A.java)

Complete Examples Repo: [Limelight FTC Examples Repo](https://github.com/LimelightVision/limelight-examples)

## Tips for Success

- Do the simple thing first. In FRC, the best software teams often use the simplest approaches. For example, FRC Team 2056 in 2024 used a standard 90FPS color pipeline instead of a neural network to track game pieces.

Here's an example of the type of question to ask as you start programming: in teleop, do you need to know your robot's position on the field, or do you simply need to strafe until your crosshair is centered on a specific tag (`strafeSpeed = result.getTx()*.03`)?

## Key Concepts

### 1. Initialization

We need to set up our Limelight3A in our robot code.

```java
import com.qualcomm.hardware.limelightvision.LLResult;
import com.qualcomm.hardware.limelightvision.LLResultTypes;
import com.qualcomm.hardware.limelightvision.LLStatus;
import com.qualcomm.hardware.limelightvision.Limelight3A;
```

```java
Limelight3A limelight;

@Override
public void init() {
    limelight = hardwareMap.get(Limelight3A.class, "limelight");
    limelight.setPollRateHz(100); // This sets how often we ask Limelight for data (100 times per second)
    limelight.start(); // This tells Limelight to start looking!
}
```

### 2. Pipeline Management

Pipelines are like small, instantly swappable programs that change how Limelight looks at the world. You can set up 10 different pipelines in the Limelight web interface, each for a different task. Here's how you switch between them:

```java
limelight.pipelineSwitch(0); // Switch to pipeline number 0
```

This is fire-and-forget. Limelight will change its pipeline in a matter of milliseconds, but your code will not wait for this before continuing. If you want to check the current pipeline index, call:

```text
result.getPipelineIndex()
```

### 3. Getting and Using Results

LLResult is like a container full of information about what Limelight sees. Here's how we acquire and use that information:

```java
LLResult result = limelight.getLatestResult();
if (result != null && result.isValid()) {
    double tx = result.getTx(); // How far left or right the target is (degrees)
    double ty = result.getTy(); // How far up or down the target is (degrees)
    double ta = result.getTa(); // How big the target looks (0%-100% of the image)

    telemetry.addData("Target X", tx);
    telemetry.addData("Target Y", ty);
    telemetry.addData("Target Area", ta);
} else {
    telemetry.addData("Limelight", "No Targets");
}
```

### 4. Talking to Python SnapScripts

You can write your own Python SnapScript pipelines in the web interface. Limelight's LLM-based SnapScript generator can help you write your code.

Here's how you send numbers from robot code to Python and get numbers back:

```java
// Sending numbers to Python
double[] inputs = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0};
limelight.updatePythonInputs(inputs);

// Getting numbers from Python
double[] pythonOutputs = result.getPythonOutput();
if (pythonOutputs != null && pythonOutputs.length > 0) {
    double firstOutput = pythonOutputs[0];
    telemetry.addData("Python output:", firstOutput);
}
```

### 5. Where's My Robot? (MegaTag 1)

Limelight can help figure out where your robot is on the field using AprilTags. Your Limelight comes pre-installed with an AprilTag Map for the current game, but you can design and upload your own maps using the 3D Map Builder (see [localization.md](./localization.md)).

Before you try to get your robot's position, do the following:

1. Enable "Full 3D" in your AprilTag pipeline's "Advanced" tab in the web interface.
2. Use the web interface to position your camera relative to the center of your robot's footprint.

The coordinate system for botPose matches the standard FTC coordinate system.

- (0,0,0) is the center of the field floor
- For non-diamond configurations, 0 degrees Yaw means the blue alliance is on the left side of your robot, and the red alliance is on the right side of your robot.

```java
if (result != null && result.isValid()) {
    Pose3D botpose = result.getBotpose();
    if (botpose != null) {
        double x = botpose.getPosition().x;
        double y = botpose.getPosition().y;
        telemetry.addData("MT1 Location", "(" + x + ", " + y + ")");
    }
}
```

### 6. Where's My Robot? (MegaTag 2)

MegaTag 2 is like MegaTag 1, but it fuses your IMU data for increased accuracy:

```java
// First, tell Limelight which way your robot is facing
double robotYaw = imu.getAngularOrientation().firstAngle;
limelight.updateRobotOrientation(robotYaw);
if (result != null && result.isValid()) {
    Pose3D botpose_mt2 = result.getBotpose_MT2();
    if (botpose_mt2 != null) {
        double x = botpose_mt2.getPosition().x;
        double y = botpose_mt2.getPosition().y;
        telemetry.addData("MT2 Location:", "(" + x + ", " + y + ")");
    }
}
```

### 7. Inner Results Types

Depending on how you've configured your pipelines, you will have access to different types of detailed Results Lists within the parent LLResult object.

You probably won't need to use these Results Lists. It's recommended to use the base `getTx()`, `getTy()` whenever you can.

#### 7.1 Color Results

Color results help find colored targets:

```java
List<ColorResult> colorTargets = result.getColorResults();
for (ColorResult colorTarget : colorTargets) {
    double x = detection.getTargetXDegrees(); // Where it is (left-right)
    double y = detection.getTargetYDegrees(); // Where it is (up-down)
    double area = colorTarget.getTargetArea(); // size (0-100)
    telemetry.addData("Color Target", "takes up " + area + "% of the image");
}
```

#### 7.2 Fiducial/AprilTag Results

Fiducials are special markers (like AprilTags) that help Limelight figure out where it is:

```java
List<FiducialResult> fiducials = result.getFiducialResults();
for (FiducialResult fiducial : fiducials) {
    int id = fiducial.getFiducialId(); // The ID number of the fiducial
    double x = detection.getTargetXDegrees(); // Where it is (left-right)
    double y = detection.getTargetYDegrees(); // Where it is (up-down)
    double StrafeDistance_3D = fiducial.getRobotPoseTargetSpace().getY();
    telemetry.addData("Fiducial " + id, "is " + distance + " meters away");
}
```

If you want to utilize the 3D pose information within each FiducialResult, you can use the following methods:

```java
fiducial.getRobotPoseTargetSpace(); // Robot pose relative to the AprilTag Coordinate System (Most Useful)
fiducial.getCameraPoseTargetSpace(); // Camera pose relative to the AprilTag (useful)
fiducial.getRobotPoseFieldSpace(); // Robot pose in the field coordinate system based on this tag alone (useful)
fiducial.getTargetPoseCameraSpace(); // AprilTag pose in the camera's coordinate system (not very useful)
fiducial.getTargetPoseRobotSpace(); // AprilTag pose in the robot's coordinate system (not very useful)
```

#### 7.3 Barcode Results

Limelight's barcode pipeline is good at detecting and tracking QR Codes.

```java
List<BarcodeResult> barcodes = result.getBarcodeResults();
for (BarcodeResult barcode : barcodes) {
    String data = barcode.getData(); // What the barcode says
    String family = barcode.getFamily(); // What type of barcode it is
    telemetry.addData("Barcode", data + " (" + family + ")");
}
```

#### 7.4 Classifier Results

Neural Classifiers allow Limelight to say "I think this is an image of a...".

```java
List<ClassifierResult> classifications = result.getClassifierResults();
for (ClassifierResult classification : classifications) {
    String className = classification.getClassName(); // What Limelight thinks it sees
    double confidence = classification.getConfidence(); // Confidence Score
    telemetry.addData("I see a", className + " (" + confidence + "%)");
}
```

#### 7.5 Detector Results

Detectors find specific objects and tell us where they are:

```java
List<DetectorResult> detections = result.getDetectorResults();
for (DetectorResult detection : detections) {
    String className = detection.getClassName(); // What was detected
    double x = detection.getTargetXDegrees(); // Where it is (left-right)
    double y = detection.getTargetYDegrees(); // Where it is (up-down)
    telemetry.addData(className, "at (" + x + ", " + y + ") degrees");
}
```

### 8. Is The Data Fresh?

Sometimes we want to know the age (in milliseconds) of our results data.

```java
long staleness = result.getStaleness();
if (staleness < 100) { // Less than 100 milliseconds old
    telemetry.addData("Data", "Good");
} else {
    telemetry.addData("Data", "Old (" + staleness + " ms)");
}
```

### 9. Custom Field Maps

You can tell Limelight about your specific field layout:

```java
LLFieldMap fieldMap = new LLFieldMap(); // You'll need to fill this with field data
boolean success = limelight.uploadFieldmap(fieldMap, null); // null means use the default slot
if (success) {
    telemetry.addData("Field Map", "Uploaded successfully!");
} else {
    telemetry.addData("Field Map", "Oops, upload failed");
}
```

See [localization.md](./localization.md) for the `.fmap` file format.

### 10. Taking Snapshots

Limelight can take snapshots to help you debug pipelines off the field:

```java
limelight.captureSnapshot("auto_pov_10s");
```

In the web interface's Input Tab, you can select this snapshot as the "image source" to check/tune your pipelines.

To clear out old snapshots:

```java
limelight.deleteSnapshots();
telemetry.addData("Snapshots", "All cleared out!");
```
