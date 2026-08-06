> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/complete-networktables-api · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

NetworkTables API | Limelight Documentation

 Skip to main content

 On this page

# NetworkTables API

Limelight OS features a NetworkTables 4 Client. It auto-connects
to the NetworkTables 4 Server running on FRC Robots based on the Team Number / ID configured
in the Settings UI.

All data is published to a table that matches the device name (e.g. "limelight"). If a hostname / nickname is assigned to your camera,
the table name will match the full limelight name (e.g. "limelight-top").

LimelightLib WPIJava and LimelightLib WPICPP interact with Limelight devices via NetworkTables.

## Basic Targeting Data​

Use the following code:

- Java
- LabView
- C++
- Python
NetworkTableInstance.getDefault().getTable("limelight").getEntry("<variablename>").getDouble(0);

nt::NetworkTableInstance::GetDefault().GetTable("limelight")->GetNumber("<variablename>",0.0);

NetworkTables.getTable("limelight").getNumber('<variablename>');

to retrieve this data:

keytypedescription
tvint1 if valid target exists. 0 if no valid targets exist
txdoubleHorizontal Offset From Crosshair To Target (LL1: -27 degrees to 27 degrees / LL2: -29.8 to 29.8 degrees)
tydoubleVertical Offset From Crosshair To Target (LL1: -20.5 degrees to 20.5 degrees / LL2: -24.85 to 24.85 degrees)
txncdoubleHorizontal Offset From Principal Pixel To Target (degrees)
tyncdoubleVertical Offset From Principal Pixel To Target (degrees)
tadoubleTarget Area (0% of image to 100% of image)
tldoubleThe pipeline's latency contribution (ms). Add to "cl" to get total latency.
cldoubleCapture pipeline latency (ms). Time between the end of the exposure of the middle row of the sensor to the beginning of the tracking pipeline.
t2ddoubleArray containing several values for matched-timestamp statistics: [targetValid, targetCount, targetLatency, captureLatency, tx, ty, txnc, tync, ta, tid, targetClassIndexDetector , targetClassIndexClassifier, targetLongSidePixels, targetShortSidePixels, targetHorizontalExtentPixels, targetVerticalExtentPixels, targetSkewDegrees]
getpipeintTrue active pipeline index of the camera (0 .. 9)
getpipetypestringPipeline Type e.g. "pipe_color"
jsonstringFull JSON dump of targeting results. Must be enabled per-pipeline in the 'output' tab
tcdoubleArrayGet the average BGR color underneath the crosshair region as a NumberArray [B, G, R]
hbdoubleheartbeat value. Increases once per frame, resets at 2 billion
hwdoubleArrayHardware metrics [cpu_temp_celsius, cpu_usage, ram_usage_percent, fps]
crosshairsdoubleArray2D Crosshairs [cx0, cy0, cx1, cy1]
tcclassstringName of classifier pipeline's computed class
tdclassstringName of detector pipeline's primary detection

## AprilTag and 3D Data​

Use the following code:

- Java
- C++
NetworkTableInstance.getDefault().getTable("limelight").getEntry("<variablename>").getDoubleArray(new double[6]);

nt::NetworkTableInstance::GetDefault().GetTable("limelight")->GetNumberArray("<variablename>",std::vector<double>(6));

to retrieve this data:

keytypedescription
botposedoubleArrayRobot transform in field-space. Translation (X,Y,Z) in meters Rotation(Roll,Pitch,Yaw) in degrees, total latency (cl+tl), tag count, tag span, average tag distance from camera, average tag area (percentage of image)
botpose_wpibluedoubleArrayRobot transform in field-space (blue driverstation WPILIB origin). Translation (X,Y,Z) in meters Rotation(Roll,Pitch,Yaw) in degrees, total latency (cl+tl), tag count, tag span, average tag distance from camera, average tag area (percentage of image)
botpose_wpireddoubleArrayRobot transform in field-space (red driverstation WPILIB origin). Translation (X,Y,Z) in meters, Rotation(Roll,Pitch,Yaw) in degrees, total latency (cl+tl), tag count, tag span, average tag distance from camera, average tag area (percentage of image)
botpose_orbdoubleArrayRobot transform in field-space (Megatag2). Translation (X,Y,Z) in meters Rotation(Roll,Pitch,Yaw) in degrees, total latency (cl+tl), tag count, tag span, average tag distance from camera, average tag area (percentage of image)
botpose_orb_wpibluedoubleArrayRobot transform in field-space (Megatag2) (blue driverstation WPILIB origin). Translation (X,Y,Z) in meters Rotation(Roll,Pitch,Yaw) in degrees, total latency (cl+tl), tag count, tag span, average tag distance from camera, average tag area (percentage of image)
botpose_orb_wpireddoubleArrayRobot transform in field-space (Megatag2) (red driverstation WPILIB origin). Translation (X,Y,Z) in meters, Rotation(Roll,Pitch,Yaw) in degrees, total latency (cl+tl), tag count, tag span, average tag distance from camera, average tag area (percentage of image)
camerapose_targetspacedoubleArray3D transform of the camera in the coordinate system of the primary in-view AprilTag (array (6)) [tx, ty, tz, pitch, yaw, roll] (meters, degrees)
targetpose_cameraspacedoubleArray3D transform of the primary in-view AprilTag in the coordinate system of the Camera (array (6)) [tx, ty, tz, pitch, yaw, roll] (meters, degrees)
targetpose_robotspacedoubleArray3D transform of the primary in-view AprilTag in the coordinate system of the Robot (array (6)) [tx, ty, tz, pitch, yaw, roll] (meters, degrees)
botpose_targetspacedoubleArray3D transform of the robot in the coordinate system of the primary in-view AprilTag (array (6)) [tx, ty, tz, pitch, yaw, roll] (meters, degrees)
camerapose_robotspacedoubleArray3D transform of the camera in the coordinate system of the robot (array (6))
tidintID of the primary in-view AprilTag
stddevsdoubleArrayMegaTag Standard Deviations [MT1x, MT1y, MT1z, MT1roll, MT1pitch, MT1Yaw, MT2x, MT2y, MT2z, MT2roll, MT2pitch, MT2yaw]

camerapose_robotspace_setdoubleArraySET the camera's pose in the coordinate system of the robot.
priorityidintSET the required ID for tx/ty targeting. Ignore other targets. Does not affect localization
robot_orientation_setdoubleArraySET Robot Orientation and angular velocities in degrees and degrees per second[yaw,yawrate,pitch,pitchrate,roll,rollrate]
fiducial_id_filters_setdoubleArrayOverride valid fiducial ids for localization (array) 
fiducial_offset_setdoubleArraySET the 3D Point of Interest Offset [x,y,z]
fiducial_downscale_setintOverride AprilTag detection downscale. 0=pipeline control, 1=1x (no downscale), 2=1.5x, 3=2x, 4=3x, 5=4x

## Camera Controls​

Use the following code:

- Java
- LabView
- C++
- Python
NetworkTableInstance.getDefault().getTable("limelight").getEntry("<variablename>").setNumber(<value>);

nt::NetworkTableInstance::GetDefault().GetTable("limelight")->PutNumber("<variablename>",<value>);

NetworkTables.getTable("limelight").putNumber('<variablename>',<value>)

to set this data:

ledModeSets limelight's LED state
[0]use the LED Mode set in the current pipeline
[1]force off
[2]force blink
[3]force on
[4]force on (left LEDs only)
[5]force on (right LEDs only)
[6]bounce halves
[7]force blink (left LEDs only)
[8]force blink (right LEDs only)

pipelineSets limelight's current pipeline
0 .. 9Select pipeline 0..9

streamSets limelight's streaming mode
0Standard - Side-by-side streams if a webcam is attached to Limelight
1PiP Main - The secondary camera stream is placed in the lower-right corner of the primary camera stream
2PiP Secondary - The primary camera stream is placed in the lower-right corner of the secondary camera stream

snapshotTakes a snapshot. Increment this value to trigger a capture (e.g., 0→1→2→3). Rate-limited to once every 10 frames.

crop(Array) Sets the crop rectangle. All web UI crop settings must be set to 0 for this to work. The array must have exactly 4 entries.
[0]X0 - Min or Max X value of crop rectangle (-1 to 1)
[1]X1 - Min or Max X value of crop rectangle (-1 to 1)
[2]Y0 - Min or Max Y value of crop rectangle (-1 to 1)
[3]Y1 - Min or Max Y value of crop rectangle (-1 to 1)

keystone_set(Array) Keystone modification for the crop window. All web UI crop settings must be set to 0 for this to work. The array must have exactly 2 entries.
[0]Horizontal keystone (-0.95 to 0.95)
[1]Vertical keystone (-0.95 to 0.95)

throttle_set(int) We recommend setting this to 100-200 while disabled. Sets number of frames to skip between processed frames to reduce temperature rise. Outputs are not zeroed during skipped frames.

## Video Recording Controls​

rewind_enable_set(double) Controls rewind buffer recording. 1 = recording enabled, 0 = recording paused.

capture_rewind(Array) Triggers rewind capture [counter, duration_seconds]. Increment counter to trigger a capture. Max duration via NetworkTables is 165 seconds. Rate-limited to once every 2 seconds; requests are also dropped if a flush is already in progress.
[0]Counter - increment this value to trigger a capture
[1]Duration in seconds (max 165 via NT)

- Java
- C++
double[] cropValues = new double[4];
cropValues[0] = -1.0;
cropValues[1] = 1.0;
cropValues[2] = -1.0;
cropValues[3] = 1.0;
NetworkTableInstance.getDefault().getTable("limelight").getEntry("crop").setDoubleArray(cropValues);

wip

## IMU Data​

keytypedescription
imudoubleArrayIMU data output [robot_yaw, roll, pitch, internal_yaw, roll_rate, pitch_rate, yaw_rate, accel_x, accel_y, accel_z] (10 elements). Angles in degrees, rates in deg/s.

## IMU Controls​

keytypedescription
imumode_setintSet the imumode. 0 - use external imu, 1 - use external imu, seed internal imu, 2 - use internal, 3 - use internal with MT1 assisted convergence, 4 - use internal IMU with external IMU assisted convergence
imuassistalpha_setdoubleComplementary filter alpha / strength. Higher values will cause the internal imu to converge on assist source more rapidly. The default is set to a low value 0.001 because we now trust the internal IMU more than before. Assist modes are built to very gently "tug" the internal imu towards the chosen assist source.

## Python​

Python scripts allow for arbitrary inbound and outbound data.

llpythonNumberArray sent by python scripts. This is accessible within robot code.
llrobotNumberArray sent by the robot. This is accessible within python SnapScripts.

## Raw Data​

Corners:

Enable "send contours" in the "Output" tab to stream corner coordinates:

tcornxyNumber array of corner coordinates [x0,y0,x1,y1......]

Raw Targets:

Limelight posts three raw contours to NetworkTables that are not influenced by your grouping mode. That is, they are filtered with your pipeline parameters, but never grouped. X and Y are returned in normalized screen space (-1 to 1) rather than degrees.

rawtargets[txnc,tync,ta,txnc2,tync2,ta2....]

Raw Fiducials:

Get all valid (unfiltered) fiducials

rawfiducials [id, txnc, tync, ta, distToCamera, distToRobot, ambiguity, id2.....]

Raw Detections:

Get all valid (unfiltered) neural detection results

rawdetections [id, txnc, tync, ta, corner0x, corner0y, corner1x, corner1y, corner2x, corner2y, corner3x, corner3y, id2.....]

Raw Barcodes:

Get all valid (unfiltered) barcode results

rawbarcodes string array of barcode data

## SmartDashboard Entries​

Limelight publishes convenience entries to the SmartDashboard table:

(hostname)_InterfaceWeb interface URL (e.g., http://10.0.0.2:5801)
(hostname)_StreamCamera stream URL (e.g., http://10.0.0.2:5800)
(hostname)_PipelineNameCurrent pipeline description name

- Basic Targeting Data
- AprilTag and 3D Data
- Camera Controls
- Video Recording Controls
- IMU Data
- IMU Controls
- Python
- Raw Data
- SmartDashboard Entries