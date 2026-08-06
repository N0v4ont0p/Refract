> Source: https://docs.limelightvision.io/docs/docs-limelight/software-change-log-2021-2023 · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Software Change Log 2021 - 2023 | Limelight Documentation

 Skip to main content

 On this page

# Software Change Log 2021 - 2023

## 2023.6 (4/18/23)​

### Easy ChArUco Calibration & Calibration Visualizers​

- ChArUco calibration is considered to be better than checkerboard calibration because it handles occlusions, bad corner detections, and does not require the entire board to be visible. This makes it much easier to capture calibration board corners close to the edges and corners of your images. This is crucial for distortion coefficient estimation.

- Limelight’s calibration process provides feedback at every step, and will ensure you do all that is necessary for good calibration results. A ton of effort has gone into making this process as bulletproof as possible.

- Most importantly, you can visualize your calibration results right next to the default calibration. At a glance, you can understand whether your calibration result is reasonable or not.

- You can also use the calibration dashboard as a learning tool. You can modify downloaded calibration results files and reupload them to learn how the intrinsics matrix and distortion coefficients affect targeting results, FOV, etc.

- Take a look at this video:

## 2023.5.1 & 2023.5.2 (3/22/23)​

- 
Fixed regression introduced in 2023.5.0 - While 2023.5 fixed megatag for all non-planar layouts, it reduced the performance of single-tag pose estimates. This has been fixed. Single-tag pose estimates use the exact same solver used in 2023.4.

- 
Snappier snapshot interface. Snapshot grid now loads low-res 128p thumbnails.

- 
Limeilght Yaw is now properly presented in the 3d visualizers. It is ccw-positive in the visualizer and internally

- 
Indicate which targets are currently being tracked in the field space visualizer

## 2023.5.0 (3/21/23)​

### Breaking Changes​

- Fixed regression - Limelight Robot-Space "Yaw" was inverted in previous releases. Limelight yaw in the web ui is now CCW-Positive internally.

### Region Selection Update​

- Region selection now works as expected in neural detector pipelines.

- Add 5 new region options to select the center, top, left, right, top, or bottom of the unrotated target rectangle.

### "hwreport" REST API​

- :5807/hwreport will return a JSON response detailing camera intrinsics and distortion information

### MegaTag Fix​

- Certain non-coplanar apriltag layouts were broken in MegaTag. This has been fixed, and pose estimation is now stable with all field tags. This enables stable pose estimation at even greater distances than before.

### Greater tx and ty accuracy​

- TX and TY are more accurate than ever. Targets are fully undistorted, and FOV is determined wholly by camera intrinsics.

## 2023.4.0 (2/18/23)​

### Neural Detector Class Filter​

Specify the classes you want to track for easy filtering of unwanted detections.

### Neural Detector expanded support​

Support any input resolution, support additional output shapes to support other object detection architectures. EfficientDet0-based models are now supported.

## 2023.3.1 (2/14/23)​

### AprilTag Accuracy Improvements​

Improved intrinsics matrix and, most importantly, improved distortion coefficients for all models. Noticeable single AprilTag Localization improvements.

### Detector Upload​

Detector upload fixed.

## 2023.3 (2/13/23)​

### Capture Latency (NT Key: "cl", JSON Results: "cl")​

The new capture latency entry represents the time between the end of the exposure of the middle row of Limelight's image sensor and the beginning of the processing pipeline.

### New Quality Threshold for AprilTags​

Spurious AprilTags are now more easily filtered out with the new Quality Threshold slider. The default value set in 2023.3 should remove most spurious detections.

### Camera Pose in Robot Space Override (NT Keys: "camerapose_robotspace_set", "camerapose_robotspace")​

Your Limelight's position in robot space may now be adjusted on-the-fly. If the key is set to an array of zeros, the pose set in the web interface is used.

Here's an example of a Limelight on an elevator:

### Increased Max Exposure​

The maximum exposure time is now 33ms (up from 12.5 ms). High-fps capture modes are still limited to (1/fps) seconds. 90hz pipelines, for example, will not have brighter images past 11ms exposure time.

### Botpose updates​

All three botpose arrays in networktables have a seventh entry representing total latency (capture latency + targeting latency).

### Bugfixes​

- Fix LL3 MJPEG streams in shuffleboard

- Fix camMode - driver mode now produces bright, usable images.

- Exposure label has been corrected - each "tick" represents 0.01ms and not 0.1 ms

- Fix neural net detector upload

## 2023.2 (1/28/23)​

Making 3D easier than ever.

### WPILib-compatible Botposes​

Botpose is now even easier to use out-of-the-box.

These match the WPILib Coordinate systems. 

All botposes are printed directly in the field-space visualizer in the web interface, making it easy to confirm at a glance that everything is working properly.

### Easier access to 3D Data (Breaking Changes)​

RobotPose in TargetSpace is arguably the most useful data coming out of Limelight with repsect to AprilTags. Using this alone, you can perfectly align a drivetrain with an AprilTag on the field.

- NetworkTables Key “campose” is now “camerapose_targetspace”

- NetworkTables Key “targetpose” is now “targetpose_cameraspace”

- New NetworkTables Key - “targetpose_robotspace”

- New NetworkTables Key - “botpose_targetspace”

### Neural Net Upload​

Upload teachable machine models to the Limelight Classifier Pipeline. Make sure they are Tensorflow Lite EdgeTPU compatible models.
Upload .tflite and .txt label files separately.

## 2023.1 (1/19/23)​

MegaTag and Performance Boosts

### Correcting A Mistake​

The default marker size parameter in the UI has been corrected to 152.4mm (down from 203.2mm). This was the root of most accuracy issues.

### Increased Tracking Stability​

There are several ways to tune AprilTag detection and decoding. We’ve improved stability across the board, especially in low light / low exposure environments.

### Ultra Fast Grayscaling​

Grayscaling is 3x-6x faster than before. Teams will always see a gray video stream while tracking AprilTags.

### Cropping For Performance​

AprilTag pipelines now have crop sliders. Cropping your image will result in improved framerates at any resolution.

### Easier Filtering​

There is now a single “ID filter” field in AprilTag pipelines which filters JSON output, botpose-enabled tags, and tx/ty-enabled tags. The dual-filter setup was buggy and confusing.

### Breaking Change​

The NT Key “camtran” is now “campose”

### JSON update​

"botpose" is now a part of the json results dump

### Field Space Visualizer Update​

The Field-space visualizer now shows the 2023 FRC field. It should now be easier to judge botpose accuracy at a glance.

### Limelight MegaTag (new botpose)​

My #1 priority has been rewriting botpose for greater accuracy, reduced noise, and ambiguity resilience. Limelight’s new botpose implementation is called MegaTag. Instead of computing botpose with a dumb average of multiple individual field-space poses, MegaTag essentially combines all tags into one giant 3D tag with several keypoints. This has enormous benefits.

The following GIF shows a situation designed to induce tag flipping: Green Cylinder: Individual per-tag bot pose Blue Cylinder: 2023.0.1 BotPose White Cylinder: New MegaTag Botpose

Notice how the new botpose (white cylinder) is extremely stable compared to the old botpose (blue cylinder). You can watch the tx and ty values as well.

Here’s the full screen, showing the tag ambiguity:

Here are the advantages:

Botpose is now resilient to ambiguities (tag flipping) if more than one tag is in view (unless they are close and coplanar. Ideally the keypoints are not coplanar). Botpose is now more resilient to noise in tag corners if more than one tag is in view. The farther away the tags are from each other, the better. This is not restricted to planar tags. It scales to any number of tags in full 3D and in any orientation. Floor tags and ceiling tags would work perfectly.

Here’s a diagram demonstrating one aspect of how this works with a simple planar case. The results are actually better than what is depicted, as the MegaTag depicted has a significant error applied to three points instead of one point. As the 3D combined MegaTag increases in size and in keypoint count, its stability increases.

Nerual Net upload is being pushed to 2023.2!

## 2023.0.0 and 2023.0.1 (1/11/23)​

Introducing AprilTags, Robot localization, Deep Neural Networks, a rewritten screenshot interface, and more.

### Features, Changes, and Bugfixes​

- New sensor capture pipeline and Gain control

- Our new capture pipeline allows for exposure times 100x shorter than what they were in 2022. The new pipeline also enables Gain Control. This is extremely important for AprilTags tracking, and will serve to make retroreflective targeting more reliable than ever. Before Limelight OS 2023, Limelight's sensor gain was non-deterministic (we implemented some tricks to make it work anyways).

- With the new "Sensor Gain" slider, teams can make images darker or brighter than ever before without touching the exposure slider. Increasing gain will increase noise in the image.

- Combining lower gain with the new lower exposure times, it is now possible to produce nearly completely black images with full-brightness LEDs and retroreflective targets. This will help mitigate LED and sunlight reflections while tracking retroreflective targets.

- By increasing Sensor Gain and reducing exposure, teams will be able to minimize the effects of motion blur due to high exposure times while tracking AprilTags.

- We have managed to develop this new pipeline while retaining all features - 90fps, hardware zoom, etc.

- More Resolution Options

- There two new capture resolutsions for LL1, LL2, and LL2+: 640x480x90fps, and 1280x960x22fps

- Optimized Web Interface

- The web gui will now load and initialize up to 3x faster on robot networks.

- Rewritten Snapshots Interface

- The snapshots feature has been completely rewritten to allow for image uploads, image downloads, and image deletion. There are also new APIs for capturing snapshots detailed in the documentation.

- SolvePnP Improvements

- Our solvePnP-based camera localization feature had a nasty bug that was seriously limiting its accuracy every four frames. This has been addressed, and a brand new full 3D canvas has been built for Retroreflective/Color SolvePNP visualizations.

- Web Interface Bugfix

- There was an extremely rare issue 2022 that caused the web interface to permanently break during the first boot after flashing, which would force the user to re-flash. The root cause was found and fixed for good.

- New APIs

- Limelight now include REST and Websocket APIs. REST, Websocket, and NetworkTables APIs all support the new JSON dump feature, which lists all data for all targets in a human readable, simple-to-parse format for FRC and all other applications.

### Zero-Code Learning-Based Vision & Google Coral Support​

- Google Coral is now supported by all Limelight models. Google Coral is a 4TOPs (Trillions-of-Operations / second) USB hardware accelerator that is purpose built for inference on 8-bit neural networks.

- Just like retroreflective tracking a few years ago, the barrier to entry for learning-based vision on FRC robots has been too high for the average team to even make an attempt. We have developed all of the infrastructure required to make learning-based vision as easy as retroreflective targets with Limelight.

- We have a cloud GPU cluster, training scripts, a dataset aggregation tool, and a human labelling team ready to go. We are excited to bring deep neural networks to the FRC community for the first time.

- We currently support two types of models: Object Detection models, and Image classification models.

- Object detection models will provide "class IDs" and bounding boxes (just like our retroreflective targets) for all detected objects. This is perfect for real-time game piece tracking.

- Please contribute to the first-ever FRC object detection model by submitting images here: https://datasets.limelightvision.io/frc2023

- Use tx, ty, ta, and tclass networktables keys or the JSON dump to use detection networks

- Image classification models will ingest an image, and produce a single class label.

- To learn more and to start training your own models for Limelight, check out Teachable Machine by google.

- https://www.youtube.com/watch?v=T2qQGqZxkD0

- Teachable machine models are directly compatible with Limelight.

- Image classifiers can be used to classify internal robot state, the state of field features, and so much more.

- Use the tclass networktables key to use these models.

- Limelight OS 2023.0 does not provide the ability to upload custom models. This will be enabled shortly in 2023.1

### Zero-Code AprilTag Support​

- AprilTags are as easy as retroreflective targets with Limelight. Because they have a natural hard filter in the form of an ID, there is even less of a reason to have your roboRIO do any vision-related filtering.

- To start, use tx, ty, and ta as normal. Zero code changes are required. Sort by any target characteristic, utilize target groups, etc.

- Because AprilTags both always square and always uniquely identifiable, they provide the perfect platform for full 3D pose calculations.

- The feedback we've received for this feature in our support channels has been extremely positive. We've made AprilTags as easy as possible, from 2D tracking to a full 3D robot localization on the field

- Check out the Field Map Specification and Coordinate System Doc for more detailed information.

- There are four ways to use AprilTags with Limelight:

- AprilTags in 2D

- Use tx, ty, and ta. Configure your pipelines to seek out a specific tag ID.

- <gif>

- Point-of-Interest 3D AprilTags

- Use tx and ty, ta, and tid networktables keys. The point of interest offset is all most teams will need to track targets do not directly have AprilTags attached to them.

- <gif>

- Full 3D

- Track your LL, your robot, or tags in full 3D. Use campose or json to pull relevant data into your roboRio.

- <gif>

- Field-Space Robot Localization

- Tell your Limelight how it's mounted, upload a field map, and your LL will provide the field pose of your robot for use with the WPILib Pose Estimator.

- Our field coordinate system places (0,0) at the center of the field instead of a corner.

- Use the botpose networktables key for this feature.

- <gif>

## 2022.3.0 (4/13/22)​

Bugfixes and heartbeat.

### Bugfixes​

- Fix performance, stream stability, and stream lag issues related to USB Camera streams and multiple stream instances.

### Features and Changes​

- "hb" Heartbeat NetworkTable key

- The "hb" value increments once per processing frame, and resets to zero at 2000000000.

## 2022.2.3 (3/16/22)​

Bugfixes and robot-code crop filtering.

### Bugfixes​

- Fix "stream" networktables key and Picture-In-Picture Modes

- Fix "snapshot" networktables key. Users must set the "snapshot" key to "0" before setting it to "1" to take a screenshot.

- Remove superfluous python-related alerts from web interface

### Features and Changes​

- Manual Crop Filtering

- Using the "crop" networktables array, teams can now control crop rectangles from robot code.

- For the "crop" key to work, the current pipeline must utilize the default, wide-open crop rectangle (-1 for minX and minY, +1 for maxX and +1 maxY).

- In addition, the "crop" networktable array must have exactly 4 values, and at least one of those values must be non-zero.

## 2022.2.2 (2/23/22)​

Mandatory upgrade for all teams based on Week 0 and FMS reliability testing.

### Bugfixes​

- Fix hang / loss of connection / loss of targeting related to open web interfaces, FMS, FMS-like setups, Multiple viewer devices etc.

### Features and Changes​

- 
Crop Filtering

- Ignore all pixels outside of a specified crop rectangle

- If your flywheel has any sweet spots on the field, you can make use of the crop filter to ignore the vast majority of pixels in specific pipelines. This feature should help teams reduce the probability of tracking non-targets.

- If you are tracking cargo, use this feature to look for cargo only within a specific part of the image. Consider ignoring your team's bumpers, far-away targets, etc.

- 
Corners feature now compatible with smart target grouping

- This one is for the teams that want to do more advanced custom vision on the RIO

- "tcornxy" corner limit increased to 64 corners

- Contour simplification and force convex features now work properly with smart target grouping and corner sending

- 
IQR Filter max increased to 3.0

- 
Web interface live target update rate reduced from 30fps to 15fps to reduce bandwidth and cpu load while the web interface is open

## 2022.1 (1/25/22)​

### Bugfixes​

- We acquired information from one of our suppliers about an issue (and a fix!) that affects roughly 1/75 of the CPUs specifically used in Limelight 2 (it may be related to a specific batch). It makes sense, and it was one of the only remaining boot differences between the 2022 image and the 2020 image.

- Fix the upload buttons for GRIP inputs and SolvePNP Models

### Features​

- 
Hue Rainbow

- The new hue rainbow makes it easier to configure the hue threshold.

- 
Hue Inversion

- The new hue inversion feature is a critical feature if you want to track red objects, as red is at both the beginning and the end of the hue range:

- 
New Python Libraries

- Added scipy, scikit-image, pywavelets, pillow, and pyserial to our python sandbox.

## 2022.0 and 2022.0.3 (1/15/22)​

This is a big one. Here are the four primary changes:

### Features​

- 
Smart Target Grouping

- Automatically group targets that pass all individual target filters.

- Will dynamically group any number of targets between -group size slider minimum- and -group size slider maximum-

- 
Outlier Rejection

- While this goal is more challenging than other goals, it gives us more opportunities for filtering. Conceptually, this goal is more than a “green blob.” Since we know that the goal is comprised of multiple targets that are close to each other, we can actually reject outlier targets that stand on their own.

- You should rely almost entirely on good target filtering for this year’s goal, and only use outlier rejection if you see or expect spurious outliers in your camera stream. If you have poor standard target filtering, outlier detection could begin to work against you!

- 
Limelight 2022 Image Upgrades
We have removed hundreds of moving parts from our software. These are the results:

- Compressed Image Size: 1.3 GB in 2020 → 76MB for 2022 (Reduced by a factor of 17!)

- Download time: 10s of minutes in 2020 → seconds for 2022

- Flash time: 5+ minutes in 2020 → seconds for 2022

- Boot time: 35+ seconds in 2020 → 14 seconds for 2022 (10 seconds to LEDS on)

- 
Full Python Scripting

- Limelight has successfully exposed a large number of students to some of the capabilities of computer vision in robotics. With python scripting, teams can now take another step forward by writing their own image processing pipelines.

- 
This update is compatible with all Limelight Hardware, including Limelight 1.

- 
Known issues: Using hardware zoom with python will produce unexpected results.

- 
2022.0.3 restores the 5802 GRIP stream, and addresses boot issues on some LL2 units by reverting some of the boot time optimizations. Boot time is increased to 16 seconds.

- 2023.6 (4/18/23)- Easy ChArUco Calibration & Calibration Visualizers

- 2023.5.1 & 2023.5.2 (3/22/23)
- 2023.5.0 (3/21/23)- Breaking Changes
- Region Selection Update
- "hwreport" REST API
- MegaTag Fix
- Greater tx and ty accuracy

- 2023.4.0 (2/18/23)- Neural Detector Class Filter
- Neural Detector expanded support

- 2023.3.1 (2/14/23)- AprilTag Accuracy Improvements
- Detector Upload

- 2023.3 (2/13/23)- Capture Latency (NT Key: "cl", JSON Results: "cl")
- New Quality Threshold for AprilTags
- Camera Pose in Robot Space Override (NT Keys: "camerapose_robotspace_set", "camerapose_robotspace")
- Increased Max Exposure
- Botpose updates
- Bugfixes

- 2023.2 (1/28/23)- WPILib-compatible Botposes
- Easier access to 3D Data (Breaking Changes)
- Neural Net Upload

- 2023.1 (1/19/23)- Correcting A Mistake
- Increased Tracking Stability
- Ultra Fast Grayscaling
- Cropping For Performance
- Easier Filtering
- Breaking Change
- JSON update
- Field Space Visualizer Update
- Limelight MegaTag (new botpose)

- 2023.0.0 and 2023.0.1 (1/11/23)- Features, Changes, and Bugfixes
- Zero-Code Learning-Based Vision & Google Coral Support
- Zero-Code AprilTag Support

- 2022.3.0 (4/13/22)- Bugfixes
- Features and Changes

- 2022.2.3 (3/16/22)- Bugfixes
- Features and Changes

- 2022.2.2 (2/23/22)- Bugfixes
- Features and Changes

- 2022.1 (1/25/22)- Bugfixes
- Features

- 2022.0 and 2022.0.3 (1/15/22)- Features