> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/ftc-programming · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

FTC Java & Blockly Programming Guide | Limelight Documentation

 Skip to main content

 On this page

# FTC Java & Blockly Programming Guide

(Blockly screenshots coming soon!)

Make sure you've read the FTC Programming Quick Start.

FTC Limelight Javadoc: Javadoc

Basic FTC Example: FTC Sample

Complete Examples Repo: Limelight FTC Examples Repo

## Tips for Success​

- Do the simple thing first. In FRC, we've learned that the best software teams often use the simplest approaches. For example, FRC Team 2056 in 2024 used a standard 90FPS color pipeline instead of a neural network to track game pieces.

Here's an example of the type question to ask as you start programming: In teleop, do you need to know your robot's position on the field, or do you simply need to strafe until your crosshair is centered on a specific tag (strafeSpeed = result.getTx()*.03)?

## Key Concepts​

### 1. Initialization​

We need to set up our Limelight3A in our robot code.

import com.qualcomm.hardware.limelightvision.LLResult;
import com.qualcomm.hardware.limelightvision.LLResultTypes;
import com.qualcomm.hardware.limelightvision.LLStatus;
import com.qualcomm.hardware.limelightvision.Limelight3A;

Limelight3A limelight;

@Override
public void init() {
 limelight = hardwareMap.get(Limelight3A.class, "limelight");
 limelight.setPollRateHz(100); // This sets how often we ask Limelight for data (100 times per second)
 limelight.start(); // This tells Limelight to start looking!
}

### 2. Pipeline Management​

Pipelines are like small, instantly swappable programs that change how Limelight looks at the world. You can set up 10 different pipelines in the Limelight web interface, each for a different task. Here's how you switch between them:

limelight.pipelineSwitch(0); // Switch to pipeline number 0

This is fire-and-forget. Limelight will change its pipeline in a matter of milliseconds, but your code will not wait for this before continuing. If you want to check the current pipeline index, call

result.getPipelineIndex()

See the next section to learn about getting the LLResult object.

### 3. Getting and Using Results​

LLResult is like a container full of information about what Limelight sees. Here's how we acquire and use that information:

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

### 4. Talking to Python SnapScripts​

You can write your own Python SnapScript pipelines in the web interface. Use our LLM-based SnapScript generator to help you write your code.

Here's how you send numbers from Robot Code to Python and get numbers back:

// Sending numbers to Python
double[] inputs = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0};
limelight.updatePythonInputs(inputs);

// Getting numbers from Python
double[] pythonOutputs = result.getPythonOutput();
if (pythonOutputs != null && pythonOutputs.length > 0) {
 double firstOutput = pythonOutputs[0];
 telemetry.addData("Python output:", firstOutput);
}

### 5. Where's My Robot? (MegaTag 1)​

Limelight can help figure out where your robot is on the field using AprilTags. Your Limelight comes pre-installed with an AprilTag Map for the current game, but you can design and upload your own maps using our 3D Map Builder.

Before your try to get your robot's position, do the following:

- Enable "Full 3D" in your AprilTag pipeline's "Advanced" tab in the web interface.

- Use the web interface to position your camera relative to the center of your robot's footprint.

The coordinate system for botPose matches the standard FTC coordinate system.

- (0,0,0) is the center of the field floor

- For non-diamond configurations, 0 degrees Yaw means the blue alliance is on the left side of your robot, and the red alliance is on the right side of your robot.

if (result != null && result.isValid()) {
 Pose3D botpose = result.getBotpose();
 if (botpose != null) {
 double x = botpose.getPosition().x;
 double y = botpose.getPosition().y;
 telemetry.addData("MT1 Location", "(" + x + ", " + y + ")");
 }
}

### 6. Where's My Robot? (MegaTag 2)​

MegaTag 2 is like MegaTag 1, but it fuses your IMU data for increased accuracy:

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

### 7. Inner Results Types​

Depending on how you've configured your pipelines, you will have access to different types of detailed Results Lists within the parent LLResults Object.

You probably won't need to use these Results Lists. We recommend using the base getTx(), getTy() whenever you can.

#### 7.1 Color Results​

Color results help find colored targets:

List<ColorResult> colorTargets = result.getColorResults();
for (ColorResult colorTarget : colorTargets) {
 double x = detection.getTargetXDegrees(); // Where it is (left-right)
 double y = detection.getTargetYDegrees(); // Where it is (up-down)
 double area = colorTarget.getTargetArea(); // size (0-100)
 telemetry.addData("Color Target", "takes up " + area + "% of the image");
}

#### 7.2 Fiducial/AprilTag Results​

Fiducials are special markers (like AprilTags) that help Limelight figure out where it is:

List<FiducialResult> fiducials = result.getFiducialResults();
for (FiducialResult fiducial : fiducials) {
 int id = fiducial.getFiducialId(); // The ID number of the fiducial
 double x = detection.getTargetXDegrees(); // Where it is (left-right)
 double y = detection.getTargetYDegrees(); // Where it is (up-down)
 double StrafeDistance_3D = fiducial.getRobotPoseTargetSpace().getY(); 
 telemetry.addData("Fiducial " + id, "is " + distance + " meters away");
}

If you want to utilize the 3D pose information within each FiducialResult, you can use the following methods:

fiducial.getRobotPoseTargetSpace(); // Robot pose relative it the AprilTag Coordinate System (Most Useful)
fiducial.getCameraPoseTargetSpace(); // Camera pose relative to the AprilTag (useful)
fiducial.getRobotPoseFieldSpace(); // Robot pose in the field coordinate system based on this tag alone (useful)
fiducial.getTargetPoseCameraSpace(); // AprilTag pose in the camera's coordinate system (not very useful)
fiducial.getTargetPoseRobotSpace(); // AprilTag pose in the robot's coordinate system (not very useful)

#### 7.3 Barcode Results​

Limelight's barcode pipeline is good at detecting and tracking QR Codes.

List<BarcodeResult> barcodes = result.getBarcodeResults();
for (BarcodeResult barcode : barcodes) {
 String data = barcode.getData(); // What the barcode says
 String family = barcode.getFamily(); // What type of barcode it is
 telemetry.addData("Barcode", data + " (" + family + ")");
}

#### 7.4 Classifier Results​

Neural Classifiers allow Limelight to say "I think this is an image of a...".

List<ClassifierResult> classifications = result.getClassifierResults();
for (ClassifierResult classification : classifications) {
 String className = classification.getClassName(); // What Limelight thinks it sees
 double confidence = classification.getConfidence(); // Confidence Score
 telemetry.addData("I see a", className + " (" + confidence + "%)");
}

#### 7.5 Detector Results​

Detectors find specific objects and tell us where they are:

List<DetectorResult> detections = result.getDetectorResults();
for (DetectorResult detection : detections) {
 String className = detection.getClassName(); // What was detected
 double x = detection.getTargetXDegrees(); // Where it is (left-right)
 double y = detection.getTargetYDegrees(); // Where it is (up-down)
 telemetry.addData(className, "at (" + x + ", " + y + ") degrees");
}

### 8. Is The Data Fresh?​

Sometimes, we want to know the age (in milliseconds) of our results data.

long staleness = result.getStaleness();
if (staleness < 100) { // Less than 100 milliseconds old
 telemetry.addData("Data", "Good");
} else {
 telemetry.addData("Data", "Old (" + staleness + " ms)");
}

### 9. Custom Field Maps​

You can tell Limelight about your specific field layout:

LLFieldMap fieldMap = new LLFieldMap(); // You'll need to fill this with field data
boolean success = limelight.uploadFieldmap(fieldMap, null); // null means use the default slot
if (success) {
 telemetry.addData("Field Map", "Uploaded successfully!");
} else {
 telemetry.addData("Field Map", "Oops, upload failed");
}

### 10. Taking Snapshots:​

Limelight can take snapshots to help you debug pipelines off the field:

limelight.captureSnapshot("auto_pov_10s");

In the web interface's Input Tab, you can select this snapshot as the "image source" to check/tune your pipelines.

To clear out old snapshots:

limelight.deleteSnapshots();
telemetry.addData("Snapshots", "All cleared out!");

- Tips for Success
- Key Concepts- 1. Initialization
- 2. Pipeline Management
- 3. Getting and Using Results
- 4. Talking to Python SnapScripts
- 5. Where's My Robot? (MegaTag 1)
- 6. Where's My Robot? (MegaTag 2)
- 7. Inner Results Types
- 8. Is The Data Fresh?
- 9. Custom Field Maps
- 10. Taking Snapshots: