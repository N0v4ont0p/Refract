> Source: https://docs.limelightvision.io/docs/docs-limelight/software-change-log · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Software Change Log & Feedback | Limelight Documentation

 Skip to main content

 On this page

# Software Change Log & Feedback

Submit issues and feature requests over email or to the Limelight Feedback Repo

## Limelight OS 2026.1 (4/17/26)​

2026.1 features several critical bugfixes and new features.

### MegaTag2 Output Bugfix [CRITICAL]​

In some instances, MT2 would produce an empty pose or a pose at the center of the field instead of 0,0,0.
MT2 will now always produce a 0,0,0 pose across coordinate systems when it cannot compute a geometrically valid solution.

### MegaTag2 IMU Modes 3, 4 Bugfix [CRITICAL]​

After transitioning from IMU mode 1 to mode 3 or 4, MT2 pose output would sometimes correct in the wrong direction, taking 1–5 seconds to converge on the correct solution depending on the configured alpha value.
This has been fixed and extensively tested.

### IMU Acquisition, Initialization, and Reliability [CRITICAL]​

Significantly improved IMU initialization, acquisition, and fault prevention.
Some of these upgrades have been pulled-in from Systemcore, and a new feature that prevents certain fault conditions has been added to the firmware.

### Calibration Improvements and Bugfixes [CRITICAL]​

- Fix crash caused by incorrect family selection. Warnings are displayed if a larger family needs to be selected for the current Charuco Board

- Fix crash caused by calibration images in which all detected corner points are collinear

- Teams no longer need to click "Update Settings" in the Charuco preview pipeline. Settings are updated live as they are changed in the UI

- A warning is displayed for calibrations with non-square pixels.

If the calibration procedure detects non-square pixels, this is a sign that your computer monitor or printer is applying a stretch to your board, causing markers to be non-square.
A stretched board, even with an imperceptable 5% stretch on one axis, can ruin calibration results no matter how many images are taken.

### Increased AprilTag Range with Black Level Base Profiles and Focusing Updates​

Recent updates to the camera driver have darkened images to an extent that significantly reduces AprilTag detection range. Deep in the ISP layer, pixels were essentially being "rounded" to black far too early.
In most competition environments, this squashed the contrast necessary for AprilTag decoding at long range.
With the new black level base profile, you can switch from "Dark" to "Light" or "Medium" to restore detail in darker regions and gain AprilTag detection range. Another benefit of changing to the light or medium profile is that you can further reduce both exposure and sensor gain for higher precision tracking.

In addition, while using a "Focus" pipeline, your video stream quality will increase to make it easier to hand-focus your Limelights as long as "HQ Mode" is kept enabled within the pipeline.
The HQ streams are tuned for survivability on robot networks.

### H.264, UDP Video Streaming with WebRTC and WHEP signaling​

This is the new standard streaming appraoch for Limelight cameras. You can easily switch between WebRTC and MJPEG streams in the web UI with the new toggle button to compare the two stream types yourself, and we have submitted a PR adding WebRTC support to Elastic Dashboard.

With H.264 encoding, teams can expect improved quality video at lower bandwidth (35%-10x improvement depending on image detail and robot motion). The use of UDP streaming means you don't have to worry about retransmission attempts bogging down your network. The H.264 stream, like our older MJPEG stream, is tuned for minimal latency over everything else and is suitable for live driver cameras.

WHEP is an emerging standard for WebRTC signaling that anyone can implement. It is a massive improvement over the previous solution, which was asking every WebRTC developer to build a custom signaling solution.

In the below image, the first row shows a bandwidth reduction of 46% for an in-motion, medium detail image with similar quality settings. The second image shows a difference of 91% in a high frame-rate, high-res, and high-quality streaming mode (unreleased).

Over time, we will enable higher-quality and/or higher-framerate default streaming modes for WebRTC streams.

### Per-Tag Point of Interest Defined in Fmap​

The Point-of-Interest feature allows you to take advantage of 3D transformations while targeting with tx/ty in robot code. This year, there are six tags a robot might use to directly "point" at the Hub. With this new feature and the new default 2026 fmap, each of those tags has a point of interest that lies at the center of the Hub. This means you can power on your Limelight, enable "Use Map POI Offsets", and always aim at the center of the Hub regardless of the currently-targeted tag.

The map builder has a new per-tag "POI" tab that allows you to define the POI and visualize it in realtime. If you upload the new default FRC2026 fmap, you will see POIs for the Hub and Outpost.

POI selection priority:

- UI 3D offset (highest priority) — if non-zero, used as the POI for all tags in the pipeline

- NT 3D offset (fiducial_offset_set) — used if UI offset is zero and NT override is non-zero

- Per-Tag POI from fmap — used only when UI and NT offsets are both zero and use_fmap_poi is enabled

Fmap addition (per fiducial):

- poi — optional [forward, left, down] array in meters, tag-relative. Used by pipelines with use_fmap_poi enabled.

{
 "id": 1,
 "size": 165.1,
 "transform": [...],
 "poi": [0.5, 0.0, 0.1]
}

### tDist​

tDist, available in NetworkTables and JSON results, simply provides the distance from the camera to the current target if a 3D distance can be computed. This works for AprilTags if 3D mode is enabled, and it works for any point of interest.
This means teams can combine the Per-Tag Point of Interest feature and tDist to build a highly performant robot without any complex robot code. Servo on TX, build a flywheel RPM lookup table with tDist, and you're done.

tDist respects the selected POI — if a POI is active, the distance is computed to the POI, not the tag center.

### Default Hailo 8L Detector​

LLOS 2026.0 added Hailo 8L support but shipped without a default 8L detector model. 2026.1 ships a default 8L detector and labels file which makes it easier to test your Hailo 8L.

### Hailo UX​

The top-right corner of the UI will indicate a detected Hailo module if any Hailo device is attached. Previously, this text did not reliably appear on startup.

### Hailo-Accelerated AprilTags​

Hailo-Accelerated Apriltags have returned. With Hailo 8L, teams will see up to a 50% performance improvement at 1x downscaling. There are diminishing returns at 2x downscaling and beyond.

### Language-Based, Zero-Shot Classification with Hailo and Transformers​

Tell your Limelight how you want to classify images, and our new transformer-based backend will take care of the rest. No training is required. Edit the label list at runtime and Limelight will immediately begin classifying against your new labels.

- Results appear in the existing Classifier JSON array and classifier NT outputs (tcclass, classifier class name/ID)

### Learning-Based OCR (CPU RUNTIME)​

Define any number of OCR regions, and the new OCR model will read the text inside each region and populate both JSON and NetworkTables results.

- NT key: rawocr — array output for downstream dashboards

- JSON results: new OCR array (see below)

### Neural Detector Clustering​

Increase Cluster Strength in neural detector pipelines to cluster detections into larger grouped detections.
A team might use this feature to cluster groups of fuel into a smaller number of targets to help a robot drive towards a particular cluster of fuel rather than an individual fuel.

- Clustering runs on raw detections before filtering, so filters and crosshair logic operate on the clustered targets.

### New IP Address Warning​

Some teams were configuring static IPs that would conflict with FRC Field Network setups. There is now a second warning and confirmation window for users configuring an IP address ending in the .1-.10 range.

### New NT Keys​

KeyTypeDescription
tdistdouble3D distance from the camera to the current target (or active POI) in meters
rawocrdoubleArrayRaw OCR output for each region
imu_yaw_offsetdoubleInternal IMU yaw offset (diagnostics)

### New JSON Results Fields​

Top-level:

- tdist — 3D distance from camera to target (or POI) in meters

- OCR — array of OCRResult objects (new in 2026.1)

## Limelight OS 2026.0 (1/22/26)​

2026.0 Focuses on core improvements to accuracy and latency, and introduces Limelight Rewind.

### Rewind (Only on Limelight 4)​

Rewind allows you to save video, alongside synchronized targeting, hardware, and configuration data to a .rwnd file after an event has occured, or *after a match has ended.

Video and targeting data can be scrubbed, frame-by-frame, right in the Limelight UI as well as the Limelight Tools website.

If you've ever run an autonomous mode in which your Limelights didn't work as expected, it can be hard to understand exactly what happened without an advanced logging infrastructure and screen recording.
With Rewind, you can you see exactly when and how AprilTags are occluded by things like stray zip ties, game pieces, and glare.
Rewind videos include visual targeting overlays, the full json dump per frame, and the entire hardware boot log for that session.
It is now easier than ever to understand the root cause of vision issues. Scrub the rewind log after your match, or send your Rewind file to Limelight support for diagnosis.
Each frame includes three new timestamps (LL boot, NT4, and LL wall clock) for integration into other logging and playback tools.

Rewind videos are captured at full frame rate (Up to 240FPS on Limelight 4) at a reduced resolution. Rewind is always-on by default, but nothing is flushed to disk unless a "save" command is issued via the NetworkTables or REST APIs. This means you can record an entire match's worth of video and targeting data without incurring disk access penalties during your matches.

In addition, the web UI now has three Rewind buttons. If you don't want to write any match/autonomous recording code, you can go to the web interface after a noteworthy event occurs and record the video right from the web interface. At the end of a match, for example, you can click the "Record last 2m 50s" button.

Memory and Disk space are managed for you. If you request a recording and the allocated disk pool for rwnd files is full, old videos are deleted until enough space is available for the current recording. You don't need to think about anything except requesting recordings at the end of auto/telep and periodically downloading the .rwnd files.
Rewind has a latency penalty of 500us-1ms. This latency penalty is listed in the resultsjson rewind object as "latpen" in integer microseconds. The capture and AprilTag pipelines have been optimized to make Rewind an almost-free feature addition.

Also, you can upload and view Rewind files at tools.limelightvision.io. There's an example Rewind file baked into the site if you want to test the feature.

### Calibration Overhaul​

First, Limelight's internal Charuco detector has been upgraded. The number of detected corners was tripled in one of our datasets. Many of our test with zero detected corners now have 40+ detected corners.

Second, the calibration workflow has been streamlined with a live video preview:

- Enter a "Charuco Calibration Preview" pipeline.

- Configure charuco board settings and see a live preview of your detections

- Save screenshots.

- Go to the calibration page

- Click calibrate.

- Download your latest calibration result, and upload it back to the camera.

- Inspect the mosaic, point cloud, and snapshots using the charuco preview pipeline with snapshot image sources

You no longer need to select a calibration (default, custom) to use. If a custom calibration has been uploaded, it is used for all targeting pipelines.

- 
If the default calibration is being used, you will see a yellow warning header.

- 
If a custom calibration has been uploaded, you will see a bright green header at the top of the calibration tab.

This new approach eliminates several footguns:

- Not knowing if there exists a discrepancy between the board and your configuration before you start collecting images.

- Not knowing if your images are producing valid charuco corner detections

- Uploading a valid calibration and forgetting to change the selected calibration

Finally, you can view a 3D point cloud and a 2D mosaic of all detected charuco board corners right in the web interface.

### Capture Latency Accuracy​

- Alongside improved calibration accuracy, 2026.0 includes a more accurate capture latency metric. The capture time stamp is now the start of frame exposure + (exposure time / 2). This is a convention for global shutter capture (middle of exposure) and rolling shutter capture (middle row) in several applications such as visual-intertial odometry.

### New All-in-one flash tool​

The new Limelight Hardware Manager ships with drivers and flash capabilities. See the video below:

### Live Data View​

A live data view is accessible under the live video stream. This captures the complete per-frame output, which means you no longer need to write code or interact with a dashboard to see what your camera is outputting.

### Log Viewing​

Limelight has some carryover features from Systemcore, such as the boot log and service log viewer.

### Skewed Crop Windows​

Apriltag pipelines can now utilize skewed crop windows. Configure this faux perspective crop in the web UI or in realtime over NT.

### Limelight OS Bugfixes​

- A team reported a NAN in a pose result. The root cause has been fixed, and NAN guards have been added across the board to all NT and JSON results outputs.

- The Limelight field space viewer properly displays wall-mounted apriltags.

- Between web UI refreshes, the live video stream could break after navigating the high-level tabs several times. The video stream connection is more robust and survives any number of tab changes.

- The IMU subsystem features several new watchdogs (carried over from Systemcore) to ensure a successful connection to the IMU subsystem

### Map Builder Improvements​

- The Map Builder now supports png upload to build fully-featured maps.

- Several map builder bugs have been fixed. Tags are far easier to manipulate via textbox and the 3D handles.

### Neural Network Trainer​

Our Google CoLab detector training notebook has become increasingly unstable as the underlying CoLab environment has changed over time, and adding stable Hailo support to such an environment would have been all but impossible.

The new Neural Network Trainer at tools.limelightvision.io is easy to use, and we have full control over the backend.

Paste a google drive link to your roboFlow dataset, configure a few options, and click train. Each training session gets its own dedicated Nvidia H100 GPU. We're offering this for free, although GPU selection and other parameters may change in the future based on usage. It looks like a few dozen neural networks have been trained by teams already. To those who experienced a timeout when we initially posted the tool a few days ago, the timeout limits have been lifted to allow for far longer training sessions.

The tool can generate models for

- Limelight CPU

- Google Coral

- Hailo 8 (default and turbo model types)

- Hailo 8L (default and turbo model types)

2026.0 is required for Hailo models produced by the new tool.

### Hailo Overhaul​

- Add support for Hailo 8L

- Faster model execution across the board

- Faster, higher-accuracy models from the new Neural Network Trainer

- Support for Limelight turbo models

- Show installed Hailo version in the UI Header

- Add temp and power draw for Hailo 8 to the settings tab

- Add temp for Hailo 8L to the settings tab

- Hailo Atags disabled for now.

### Improved 3A Experience on RoboRio​

USB-connected Limelight 3A and 3G cameras now have a streamlined setup for FRC. Use the new setupPortForwardingUSB() method to automatically configure port forwarding, enabling access to the web interface and video stream while connected to your robot's network.

// Call once in robotInit()
LimelightHelpers.setupPortForwardingUSB(0); // First camera (USB index 0)
LimelightHelpers.setupPortForwardingUSB(1); // Second camera (USB index 1)

After calling this method, you can access:

USB IndexWeb InterfaceVideo Stream
0http://(robotIP):5801http://(robotIP):5800
1http://(robotIP):5811http://(robotIP):5810

### Documentation​

- The snapscript helper and QA page have been updated to use state-of-the-art LLMs.

- JSON Results Specification updated with imu, hw, rewind objects and status fields (imgsrc, hwtype, uirefresh, ignorent)

- NetworkTables API documentation updated with new snapshot counter-based trigger behavior and capture_rewind rate limiting info

### New NT Keys​

KeyTypeDescription
imudoubleArrayIMU data: [robot_yaw, roll, pitch, internal_yaw, roll_rate, pitch_rate, yaw_rate, accel_x, accel_y, accel_z]
rewind_enable_setdoubleControls rewind buffer recording. 1 = recording enabled, 0 = recording paused
capture_rewinddoubleArrayTriggers rewind capture [counter, duration_seconds]. Increment counter to trigger. Max 165s via NT. Rate-limited to once every 2 seconds; dropped if flush in progress
keystone_setdoubleArrayKeystone perspective correction [horizontal, vertical] (-0.95 to 0.95)
throttle_setintFrames to skip between processed frames for thermal management
imumode_setintIMU mode selection (0-4)
imuassistalpha_setdoubleIMU assist complementary filter alpha (default 0.001)

### Changed NT Keys​

KeyChange
snapshotNow uses counter-based rising edge detection. Increment value (0→1→2→3) to trigger snapshots. Rate-limited to once per 10 frames

### New JSON Results Fields​

The JSON results output now includes additional objects:

IMU Object (imu):

- quat: Orientation quaternion [w, x, y, z]

- yaw: Final fused yaw (degrees)

- data: Raw IMU array [roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate, accel_x, accel_y, accel_z]

Hardware Object (hw):

- temp: CPU temperature (Celsius)

- cpu: CPU usage (%)

- ram: RAM usage (%)

- dfree: Disk free (MB)

- dtot: Disk total (MB)

- cid: Camera sensor ID

- hailo: Hailo stats object (present, type, temp, power, throttle)

Rewind Object (rewind): (Limelight 4 only)

- enabled: 1 if recording, 0 if paused

- storedSeconds: Seconds of video in buffer

- frameCount: Frames in buffer

- bufferUsage: Buffer usage (0.0 to 1.0)

- flushing: 1 if currently flushing to disk

Status Fields:

- imgsrc: Image source setting

- hwtype: Hardware type identifier

- uirefresh: 1 if web UI needs refresh

- ignorent: 1 if NetworkTables pipeline control is disabled

### LimelightLib 1.13 (Java/C++) (Requires LLOS 2026.0)​

#### New Classes​

- RawTarget - Represents raw target/contour results with txnc, tync, and ta fields

#### New Methods​

MethodDescription
getRawTargets()Retrieves ungrouped contours in normalized screen space (-1 to 1). Returns up to 3 RawTarget objects.
getCornerCoordinates()Fetches corner coordinates of detected targets. Requires "send contours" enabled. Returns [x0, y0, x1, y1, ...]
getHeartbeat()Returns a heartbeat value that increments each frame for connection status detection
setKeystone()Applies keystone modification to the crop window (horizontal, vertical: -0.95 to 0.95)
triggerSnapshot()Triggers snapshot capture. Rate-limited to once per 10 frames.
setRewindEnabled()Enables or pauses rewind buffer recording
triggerRewindCapture()Captures rewind footage with specified duration (max 165 seconds). Rate-limited.
setupPortForwardingUSB()Configures port forwarding for USB-connected Limelight 3A/3G cameras

## Limelight OS 2025.1 (FINAL RELEASE - 2/24/25 TEST RELEASE - 2/18/25)​

2/24/25 - Fix connectivity issue introduced in 2025.1 test release.

### LL4 IMU Updates​

- Improved IMU sensor fusion

- Significantly better performance under vibration and FRC-level impacts. Major changes to fusion approach.

The above image shows the result of a fairly violent ~5 minute practice session with an FRC robot. In this session, we measured the headings of

- A Limelight 4 running 2025.0 (llyawOLD)

- A Limelight 4 running 2025.1 (llyaw)

- A Pigeon 2.0

The two LL4s are mounted in identical orientations. Note the massive imprvement in overall accuracy from the LL4 running 2025.1

- 
IMU Mode 3 - IMU_ASSIST_MT1 - The internal IMU will utilize filtered MT1 yaw estimates for continuous heading correction

- 
IMU Mode 4 - IMU_ASSIST_EXTERNALIMU - The internal IMU will utilize the external IMU for continuous heading correction

- 
Add imuassistalpha_set NT Key (default 0.001) - Complementary filter alpha / strength. Higher values will cause the internal imu to converge on assist source more rapidly

- 
The default is set to a low value 0.001 because we now trust the internal IMU more than before. Assist modes are built to very gently "tug" the internal imu towards the chosen assist source without hurting the internal IMUs responsiveness during rapid movements.

### LL4 Thermal Performance Updates​

- 
Add 'throttle_set'. Processes one frame after every N skipped frames. Example patterns:

- throttle_set=1: [skip, process, skip, process]

- throttle_set=2: [skip, skip, process, skip, skip, process]

- 
Outputs are not zeroed/reset during skipped frames.

- 
Set this to a high number while disabled (50-200) to manage your LL4's temperature.

- 
Optionally, you can configure a pipeline as a viewfinder and switch to this pipeline while disabled.

### New FPS Options for LL4 and LL3G​

- Add 1280x800 at 60FPS, 55FPS, 45FPS, and 30FPS.

- Using lower capture rates will allow you to increase exposure time to avoid image blooming/breathing due to AC lighting.

### REST API Updates​

- Add IMU Mode REST API - 'update-imumode'

- Add Throttle REST API - 'update-throttle'

- Add IMU ASSIST ALPHA REST API - 'update-imuassistalpha'

### FMap Updates​

- FMap Json files can now optionally embed a base64-encoded SVG

- FMap Json files can now optionally embed a base64-encoded PNG

### ReefScape Neural Networks Uploaded​

- The B2 Hailo Model is our best-performing model for FRC2025. It was trained on monochrome images to better accomodate LL4.

### LL3A Updates​

- 3A fully supported with 2025 updates

### Bugfixes​

- Limelights without internal IMUs ignore imumode_set

- Limelight 3s that have been upgraded to Limelight 3Gs will properly utilize the built-in fan

- Fix Cropping in Hailo-based Neural Detector pipelines

- Fix Cropping in Hailo-based AprilTag pipelines

## Limelight OS 2025.0 (1/15/24)​

### LL4 Support​

- Add support for Hailo object detection and Hailo-accelerated AprilTags

- Add support for LL4's internal IMU.

- Add "imumode_set" NT Key

- 0 - Use external IMU, do not seed internal IMU

- 1 - Use external IMU, seed internal IMU

- 2 - Use internal IMU

### 2025 Field Updates​

- Field width and field height are now part of .fmap files

- Update default .fmap to match 2025 field

- Update default field image

- The online map builder now allows you to configure field width and field height

- the 2025 fmap link on the downloads page has been updated.

## Bugfixes​

- Fix "delete all snapshots" button

## Limelight OS 2024.10.2 (10/28/24)​

### Python Snapscript Fix (CREDIT - FTC TEAM 23251 TRIPLE FAULT)​

- Python Outputs will no longer freeze while using the Control Hub with Limelight3A

- Python Outputs will no longer freeze while switching between python pipelines

### MT2 Edge case​

https://github.com/LimelightVision/limelight-feedback/issues/23

- While testing MT2 without a robot, it is easy to generate a geometric impossibility.

- This edge case wouldn't zero-out the mt2 botpose - it would zero-out the camera pose.

- The robot is now placed at (0,0,0) whenever this edge case is detected

### Static IP Addressing​

https://github.com/LimelightVision/limelight-feedback/issues/25

- Add a warning to the IP Address setter if the address ends in .1-.10 or .20-.255 as these addresses may interfere with the FMS or other devices

- In 2024.10.1, the UI would sometimes suggest that a static IP was configured when the addressing scheme was set to "automatic"

### STDDevs NetworkTables​

https://github.com/LimelightVision/limelight-feedback/issues/24

- "stddevs" in networktables contains all stddevs for mt1 and mt2 (double array, 12 elements)

### Model Upload Edge case​

- If a classifier model is uploaded to a detector pipeline, "check model" will be displayed on the image

- If a detector model is uploaded to a classifier pipeline, "check model" will be displayed on the image

## Limelight OS 2024.10.1 (9/15/24)​

### Limelight 3A Updates​

- Update default color balance values

- Update default AprilTag size configuration to 101.6 mm

- Reduce default video stream framerate to 30FPS

- Slightly increase video stream compression to reduce stream bitrate

### AprilTag Size Warning​

- Add a warning to the field space visualizer if the configured AprilTag size does not match the sizes in the uploaded field map.

### CameraPose_RobotSpace Bugfix​

- Overriding the UI's configued Camera Pose from NetworkTables/LimelightLib/REST works properly again.

## Limelight OS 2024.10 (9/4/24)​

### Limelight 3A for FTC Support​

- Limelight3A is fully supported

- 3A is usable in both FTC and FRC

### AprilTag Map Updates​

- The map editor now supports standard and diamond FTC map generation

- The LLOS web interface will automatically display the correct field type based on the uploaded map

- All field visualizers across tools and interfaces show alliance zones and ftc tile grids.

- 3D visualizer performance has been improved.

### USB Limelight Support on ControlHub and RoboRio.​

- FTC teams can use a single USB-capable Limelight on the Control Hub

- FRC teams can use up to 16 USB-capable Limelights on the RoboRio. USB limelights auto-populate networktables just like ethernet limelights.

- To use multiple USB Limelights, give each LL a unique USB index and a unique hostname.

### USB Connectivity Upgrades​

- MacOS no longer uses the USB Ethernet Limelight interface for internet access

- Windows no longer attempts to use the USB Ethernet Limelight interface for internet access

### REST API Updates​

- Fix update-robotorientation POST request.

- MT2 is now fully accessible without NetworkTables.

- Once the update-robotorientation route is used, NetworkTables orientation updates are disabled until reboot.

## Limelight OS 2024.9.1 (7/7/24)​

- The Map Builder Tool now accepts/converts WPILib .json apriltag layouts

- Add AprilTag3 to Python Snapscripts (from apriltag import apriltag)

- See example in examples github repo

- Fix USB connectivity gateway issue on Windows.

## Limelight OS 2024.9 (7/5/24)​

### MegaTag Upgrades​

- 
Limelight OS has transitioned to NetworkTables 4.0

- 
MegaTag2 now uses NT4's getAtomic() to retrieve timestamped IMU updates from the roboRIO.

- 
Our timestamped image frames are matched to the two most relevant IMU samples before interpolation is performed.

- 
NT4 flush() has been added to LimelightLib. Adding Flush() to older versions of Limelight OS will get you quite close to 2024.9 performance, but NT4 ensures accuracy is always high.

- 
The MT2 visualizer robot now has green bumpers, and MT1's visualizer robot uses yellow bumpers.

- 
Metrics are now collapsible, and the virtual robots can be hidden.

- 
The following video demonstrates how 2024.9's MegaTag 2 (green robot) with robot-side flush() is more robust than 2024.5's MegaTag2 without Flush() (red robot)

### USB ID and New USB IP Addresses​

- Set the "USB ID" in the settings page to use multiple USB Limelights on any system.

- The USB-Ethernet interface that appears on your system will utilize an IP address that is determined by the USB ID

- Linux/Android/Mac Systems will now utilize the 172.29.0.0/24 subnet by default

- Windows systems will now utilize the 172.28.0.0/24 subnet by default.

- If the USBID is set, the subnet changes to 172.29.(USBID).0/24 for Linux/Android/Mac and 172.28.(USBID).0/24 for Windows.

- You can now, for example, attach four Limelight devices to a single USB Hub by adjusting their hostnames and USB IDs

### CPU Neural classifiers​

- Upload a CPU .tflite classifier to enable neural classification without Google Coral. You can expect 15-18 FPS on LL3 variants.

- 2024.9 comes with a default CPU classifier.

- Set the classifier runtime to "CPU" to enable this feature

### CPU Neural detectors​

- Upload a CPU .tflite detector to enable neural detecyion without Google Coral. You can expect 10 FPS on LL3 variants.

- 2024.9 comes with a default CPU detector.

- Set the detector runtime to "CPU" to enable this feature

## Limelight OS 2024.8 (7/3/24)​

- Add python output (PythonOut), tx, ty, txnc, tync, ta to json results object

- Further improved MT2 latency compensation

## Limelight OS 2024.7 (5/21/24)​

- Upgrade to Linux 6.6

### Bugfixes​

- Fix vision pipeline conversion

- Fix calibration uploads, snapshot uploads, and nn uploads

## Limelight OS 2024.6 (5/8/24)​

### LimelightLib Python​

- pip install limelightlib-python

- Our Python library allows you to interact with USB and Ethernet Limelights on any platform.

- It allows for complete Limelight configuration without web UI interaction.

- Upload pipelines, neural networks, field maps, etc

- Make realtime changes to any pipeline parameter with an optional "flush to disk" option

- Post custom python input data, set robot orientation, etc.

### MegaTag2 Upgrades​

- MegaTag2 Gyro latency compensation been improved. Look out for more improvements soon!

- Add "Gyro latency adjustment" slider to the UI. To manually tune MegaTag 2 latency compensation, you can spin your robot and adjust the slider until localization results are perfect while rotating.

### Standard Deviation Metrics​

- The 3D Field visualizer now includes MegaTag1 and Megatag2 standard deviations for x, y, and yaw.

### New "Focus" Pipeline Type​

- While in "focus" mode, you will have access to a stream quality slider and a crop box slider

- Spin the lens to maximize the "focus" score.

- If your camera is in a fixed location, this takes less than one minute. We recommend focusing with a fixed / mounted Limelight.

### New "Barcodes" Pipeline Type​

- 50-60FPS Multi QR Code Detection and Decoding at 1280x800

- 50-60FPS Multi DataMatrix Detection and Decoding at 1280x800

- 30FPS Multi UPC, EAN, Code128, and PDF417 at 1280x800

- Barcode data strings are posted to the "rawbarcodes" nt array.

- The Barcodes pipeline will populate all 2D metrics such as tx, ty, ta, tcornxy, etc.

### All-New REST API​

- https://docs.limelightvision.io/docs/docs-limelight/apis/rest-http-api

- Our REST / HTTP API has been rebuilt from the ground up.

- The REST API allows for complete Limelight configuration without web UI interaction.

- Upload pipelines, neural networks, field maps, etc

- Make realtime changes to any pipeline parameter with an optional "flush to disk" option

- Post python input data, set robot orientation, etc.

### Remove Camera Orientation Setting From UI (BREAKING CHANGE)​

- This has been replaced by the "stream orientation" option. Calibration and targeting are never affecting by this option.

- The new option only affects the stream. Upside-down, 90 Degree Clockwise, 90 Degree Counter-Clockwise, Horizontal Mirror, and Vertical Mirror

- Teams will now need to manually invert tx and ty as required while using rotated cameras.

### Remove GRIP Support (BREAKING CHANGE)​

### Remove "Driver" zero-processing mode (BREAKING CHANGE)​

- This has been replaced by the "Viewfinder" pipeline type

### Add "Viewfinder" Pipeline type​

- The viewfinder pipeline disables all processing for minimal latency

- This allows teams to design their own "Driver" pipelines for view-only modes

### Pipeline Files now Use JSON format (BREAKING CHANGE)​

- Pipelines still use the .vpr file extension

- (Broken in some cases in 2024.6) The UI will auto-convert pipelines to JSON when you use the "upload" button.

- (Fully functional) You may also https://tools.limelightvision.io/pipeline-upgrade to upgrade your pipelines

### Calibration UX Improvement​

- Calibration settings are now cached. You no longer need to enter your calibration settings every time you want to calibrate.

- The default calibration dictionary has been updated to work with the recommended 800x600mm coarse board from Calib.io.

### Calibration Mosaic​

- Previously, it was difficult to determine the quality of calibration images

- The calibration tab now has a "Download Calibration Mosaic" button. The mosaic will show you exactly what each image is contributing to your calibration.

### "Centroid" targeting region​

- Centroid targeting mode has been added to the "Output" tab to improve object tracking with color pipelines

### Dynamic 3D Offset (NT: fiducial_offset_set)​

- It is now possible to adjust the 3D Offset without changing pipelines. This is useful for situations in which your "aim point" needs to change based on distance or other properties.

### Add Modbus Support​

- Limelight OS now has an always-on modbus server for inspection, logistics, and industrial applications

- See the modbus register spec here: https://docs.limelightvision.io/docs/docs-limelight/apis/modbus

- The default modbus server port may be changed in the UI's settings tab

- Through modbus and snapscript python pipelines, completely custom vision applications with bi-directional communication are now supported.

### Custom NT server​

- The settings tab now contains an entry for a custom NT server.

- This enables a new workflow which includes a glass NT server running on a PC, and Limelight 3G communicating over USB.

### Rawfiducial changes​

- The "area" value of raw fiducials is now a calibrated, normalized value ranging from ~0-1

### All NetworkTables and JSON Changes​

- 
Add NT getpipetype - Get the current pipeline type string (eg pipe_color, pipe_fiducial)

- 
Add NT tcclass - Classifier pipeline detected class name

- 
Add NT tdclass - Detector pipeline detected class name

- 
Add NT t2d for guaranteed atomic 2d targeting - [valid,targetcount, targetlatency, capturelatency, tx, ty, txnc, tync, ta, targetid, classifierID, detectorID, tlong, tshort, thor, tvert, ts(skew)]

- 
Remove NT tlong, tshort, thor, tvert, and ts

- 
Add NT 'crosshairs' array [cx0,cy0,cx1,cy1]

- 
Remove NT cx0, cy0, cx1, and cy1

- 
Add NT rawbarcodes - NT String Array of barcode data. Up to 32 entries.

- 
All "raw" arrays allow for up to 32 targets (up from 8)

- 
Add fiducial_offset_set dynamic 3d Offset setter

- 
Add "pType" to json top-level result

- 
Add "stdev_mt1" and "stdev_mt2" to json top-level result (x,y,z,roll,pitch,yaw) (meters, degrees)

### Changes to Other File Formats and JSON Dumps​

- The calibration file format has been simplified. Old calibrations are auto-converted to the new format upon upload

- One layer of nesting has been removed from Results and Status JSON dumps

### Bugfixes​

- Previously, if a Google Coral was unplugged while a Neural pipeline was active, the pipeline would permanently revert to "color/retro" mode

- Now, "CHECK CORAL" or "CHECK MODEL" will be printed to the image. The pipeline type will never change

- Previously, tags that successfully passed through the fiducial ID filter were sometimes drawn with a red outline instead of a green outline. This visualization problem has been fixed.

- Apriltag pipelines populate the tcornxy NT array

- Apriltag pipelines now fully respect the min-max area slider. Previously, AprilTag pipelines would filter 2D results based on Tag Area, but not 3D / Localization Results.

## Limelight OS 2024.5.0 (4/9/24)​

- Upgrade to Linux 6.1

### Camera Stack Update​

- The entire camera stack has been updated to fix a camera peripheral lock-up on Limelight3G.

- Symptoms include

- Be sure to retune exposure and gain settings after applying this update.

### Dynamic Downscaling​

- Teams may now set "fiducial_downscale_set" to override the current pipeline's downscale setting

- 0:UI control, 1:1x, 2:1.5x, 3:2x, 4:3x, 5:4x

- Use the new Helpers method with 0.0 (UI Control), 1.0, 1.5, 2.0, 3.0, 4.0

- This is a zero-overhead operation.

- By combining dynamic downscale and dynamic crop, teams can maximize FPS without managing multiple pipelines

### MegaTag2 Improvements​

- MT2 now works no matter the Limelight orientation, including "portrait" modes with 90 degree and -90 degree rolls

### "rawdetections" nt array​

- [classID, txnc, tync, ta, corner0x, corner0y, corner1x, corner2y, corner3x, corner3y, corner4x, corner4y]

- corners are in pixel-space without calibration applied

### Erode/Dilate Update​

- Color pipelines now support up to 10 steps of dilation and 10 steps of erosion

- Color pipelines now have a "reverse morpho" option to reverse the order of the dilation and erosion steps

## LimelightLib 1.6 (4/9/24)​

- Add void SetFiducialDownscalingOverride(float downscale)

Set to 0 for pipeline control, or one of the following to override your pipeline's downscale setting:
1, 1.5, 2, 3, 4

- Add RawFiducial[] GetRawFiducials()

- Add RawDetection[] GetRawDetections()

## Limelight OS 2024.4.0 (4/3/24)​

Thanks to all of the teams who contributed ideas for this update.

### Megatag 2​

Megatag 2 is an ambiguity-free localizer. It has higher accuracy and higher precision than Megatag1, and it was built with the following requirements:

- Eliminate the pose ambiguity problem and increase robustness against image/corner noise.

- Provide excellent pose estimates given one or more tags, no matter the perspective.

- Increase robustness against physical AprilTag placement inaccuracies

- Reduce the amount of robot-side filtering necessary for good pose estimation results

Notice the difference between MegaTag2 (red robot) and Megatag (blue robot) in this highly ambiguous single-tag case:

Megatag2 requires you to set your robot's heading with a new method call. Here's a complete example:

 LimelightHelpers.SetRobotOrientation("limelight", m_poseEstimator.getEstimatedPosition().getRotation().getDegrees(), 0, 0, 0, 0, 0);
 LimelightHelpers.PoseEstimate mt2 = LimelightHelpers.getBotPoseEstimate_wpiBlue_MegaTag2("limelight");
 if(Math.abs(m_gyro.getRate()) > 720) // if our angular velocity is greater than 720 degrees per second, ignore vision updates
 {
 doRejectUpdate = true;
 }
 if(mt2.tagCount == 0)
 {
 doRejectUpdate = true;
 }
 if(!doRejectUpdate)
 {
 m_poseEstimator.setVisionMeasurementStdDevs(VecBuilder.fill(.6,.6,9999999));
 m_poseEstimator.addVisionMeasurement(
 mt2.pose,
 mt2.timestampSeconds);
 }

Megatag2 provides excellent, ambiguity-free results at any distance given a single tag.
This means it is perfectly viable to focus only on tags that are relevant and within your desired placement tolerance.
If a tag is not in the correct location or irrelevant, filter it out with the new dynamic filter feature.

### Dynamic Apriltag Filtering​

- Because MegaTag2 is not desperate to accumulate as many AprilTags as possible, you can safely filter for well-placed and relevant tags:

int[] validIDs = {3,4};
LimelightHelpers.SetFiducialIDFiltersOverride("limelight", validIDs);

### Transitioning to MegaTag2​

Megatag2 requires your robot heading to work properly. A heading of 0 degrees, 360 degrees, 720 degrees, etc means your robot is facing the red alliance wall.
This is the same convention used in PathPlanner, Chorero, Botpose, and Botpose_wpiblue.

Once you have added SetRobotOrientation() to your code, check the built-in 3D visualizer. At close range, Megatag2 and Megatag1 should match closely if not exactly. At long range, Megatag 2 (red robot) should be more accurate and more stable than Megatag1 (blue robot).

Once the built-in visualizer is showing good results, you can safely use Megatag2 to guide your robot during the autonomous period.

The only filter we recommend adding is a "max angular velocity" filter. You may find that at high angular velocities, your pose estimates become slightly less trustworthy.

The examples repo has a Megatag2 example with this filter.

 if(Math.abs(m_gyro.getRate()) > 720) // if our angular velocity is greater than 720 degrees per second, ignore vision updates
 {
 doRejectUpdate = true;
 }
 if(mt2.tagCount == 0)
 {
 doRejectUpdate = true;
 }

## LimelightLib 1.5 (4/3/24)​

Add

getBotPoseEstimate_wpiRed_MegaTag2()
getBotPoseEstimate_wpiBlue_MegaTag2()
SetRobotOrientation()

## Limelight OS 2024.3.4 (3/20/24)​

Thanks to all of the teams who contributed ideas for this update.

### Higher-Precision Single Tag Solver​

MegaTag's single tag 3D solver has been improved. It is far more stable than before at long range.

### JSON Disabled by Default (Breaking Change)​

- JSON has been disabled by default to reduce bandwidth usage and across the board for teams using auto-subscribing dashboards such as Shuffleboard.

- This should also reduce RoboRIO NT load and CPU usage.

- Re-enable json per-pipeline in the output tab.

- This updates includes changes that should allow even more teams to transition away from JSON for pose estimation.

### Undistorted Area (Breaking Change)​

Corners are undistorted before computing the area of any target.

### Include Per-Fiducial Metrics in botpose, botpose_wpiblue, and botpose_wpired​

[tx, ty, tz, roll, pitch, yaw, tagCount, tagSpan (meters), averageDistance (meters), averageArea (percentage of image), (tags) ]

For every tag used by megatag localization, the above arrays now include (tagID, txnc, tync, ta, distanceToCamera, distanceToRobot, ambiguity)

Ambiguity is a new metric ranging from 0-1 that indicates the ambiguity of the current perspective of the tag. Single-tag-updates with tag ambiguities > .9 should probably be rejected.

### "rawtargets" and "rawfiducials" nt arrays (Breaking Change)​

- rawtargets - (txnc,tync,ta) per target

- rawfiducials - (tagID, txnc, tync, ta, distanceToCamera, distanceToRobot, ambiguity) per target

- The previous rawtargets NT entries (tx0,ty0, etc) have been removed.

### Bugfixes​

- Zero-out all single-tag 3D information if the priorityID has not been found. Previously, only Tx, Ta, Ty, and Tv were zeroed-out when the priorityTag was not found

- Zero-out botpose if the only visible tag has been filtered by the UI's "ID Filters" features. Previously, botposes would reset to the center of the field rather than (0,0,0) if the only visible tag was a filtered tag;

- 2024.2 would post NANs to certain networktables entries in some rare instances. This will no longer happen.

## LimelightLib 1.4 (3/21/24)​

- Add support for 2024.3.4 Raw Fiducials. PoseEstimates now include an array of rawFiducials which contain id, txnc, tync, ta, distanceToCamera, distanceToRobot, and ambiguity

## Limelight Hardware Manager 1.4 (3/18/24)​

### Bugfix​

Disovered USB Limelights are properly displayed as a single entry rather than two partial entries.

## Limelight OS 2024.2.2 (3/17/24)​

### Bugfix​

TX and TY properly respect the crosshair in NT entries.

## Limelight OS 2024.2 (3/8/24)​

### Zero-Crosshair targeting with Json (tx_nocross, ty_nocross) and NT (txnc, tync)​

If you are using tx/ty targeting with custom intrinsics calibration, you are likely still seeing camera-to-camera variation because the Limelight crosshair is not aligned with the principal pixel of the camera. Teams that require greater tx/ty accuracy can either configure the crosshair to match the principal pixel, or use these new metrics.

### Potentially breaking change in tx/ty​

A bug was introduced earlier this season that broke custom calibration specifically for tx, ty, and tx + ty in json. Limelight OS was reverting to default calibrations in several cases.

### Calibration Upgrades​

Calibration is now nearly instantaneous, now matter how many images have been captured. We've also fixed a crash caused by having more than around 30 images under certain circumstances.

We're consistently getting a reprojection error of around 1 pixel with 15-20 images of paper targets, and an error of .3 pixels with our high-quality calib.io targets.

### Fiducial Filters UI Fix​

Fiducial filter textbox now accepts any number of filters.

### Misc​

Apriltag Generator defaults to "no border" to prevent scaling with 165.1 mm tags.

## Limelight OS 2024.1.1 (2/24/24)​

- Fix priorityID

## Limelight OS 2024.1 (2/24/24)​

### HW Metrics (hw key in networktables, /status GET request)​

- Teams now have the ability to log FPS, CPU Load, RAM usage, and CPU Temp.

- Addresses https://github.com/LimelightVision/limelight-feedback/issues/5

### Calibration Improvement​

- Fix crash that could occur if a calibration image contained exactly one valid detection. Improve web ui feedback.

### Robot Localization Improvement (tag count and more)​

- 
All networktables botpose arrays (botpose, botpose_wpiblue, and botpose_wpired) now include Tag Count, Tag Span (meters), Average Distance (meters), and Average Area (percentage of image)

- 
These metrics are computed with tags that are included in the uploaded field map. Custom and/or mobile AprilTags will not affect these metrics.

- 
With device calibration and this botpose array upgrade, we do not believe JSON is necessary for the vast majority of use-cases this year.

- 
JSON dump now includes botpose_avgarea, botpose_avgdist, botpose_span, and botpose_tagcount for convenience.

[tx,ty,tz,rx,ry,rz,latency,tagcount,tagspan,avgdist,avgarea]

### New Feature: Priority ID (NT Key priorityid)​

- 
If your robot uses both odometry-based features and tx/ty-based features, you've probably encountered the following UX problem:

- 
Before this update, there was no way to easily switch the preferred tag ID for tx/ty targeting.

- 
While there is an ID filter in the UI, it

- is not dynamic

- removes tags from megaTag localization.

- 
This meant teams were creating several pipelines: one for 3D localization, and one per tx/ty tag (one pipeline for blue-side shooting with tag 7, one for blue-side amping with tag 6, etc.).

- 
The new priority ID feature (NT Key priorityid) allows you to tell your Limelight "After all tag detection, filtering, and sorting is complete, focus on the tag that matches the priority ID."

- 
This does not affect localization in any way, and it only slightly changes the order of tags in JSON results.

- 
If your priority id is not -1, tx/ty/ta will return 0 unless the chosen tag is visible.

- 

### Misc​

- Fix "x" across the screen while using dual-target mode in a 3D apriltag pipeline

- REST API expanded with neural network label uploads (/uploadlabels)

- Include device nickname in /status json

## LimelightLib 1.3​

- LimelightLib (Java and CPP) have been updated to make localization easier than ever.

 LimelightHelpers.PoseEstimate limelightMeasurement = LimelightHelpers.getBotPoseEstimate_wpiBlue("limelight");
 if(limelightMeasurement.tagCount >= 2)
 {
 m_poseEstimator.setVisionMeasurementStdDevs(VecBuilder.fill(.7,.7,9999999));
 m_poseEstimator.addVisionMeasurement(
 limelightMeasurement.pose,
 limelightMeasurement.timestampSeconds);
 }

## New resources for Teams​

### Limelight Feedback and Issue Tracker: https://github.com/LimelightVision/limelight-feedback/issues​

### Examples Repo: https://github.com/LimelightVision/limelight-examples​

### Aiming and Ranging with Swerve Example: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-swerve-aiming-and-ranging​

### MegaTag Localization Example: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-swerve-pose-estimation​

Thanks to recent contributors jasondaming, Gold876, JosephTLockwood, Andrew Gasser, and virtuald

# Limelight 2024 Updates (2/6/24)

## Limelight Documentation Upgrade​

- The documentation has been rewritten to streamline the setup process

## Limelight AprilTag Generator​

- https://tools.limelightvision.io/ now features the first-ever online AprilTag generator.

- Select your paper size, marker size, and tag IDs to generate a printable PDF.

- Safari may not properly display tags at the moment.

## Limelight Map Builder​

- https://tools.limelightvision.io/map-builder

- You can now build custom AprilTag maps with an intuitive UI.

- The default family and tag size have been updated to match the 2024 field.

## New Hardware Manager​

- The Finder Tool is now the Limelight Hardware Manager

- It has been rewritten from scratch. It now reliably detects Limelights, provides more useful diagnostic information, and does not require restarts to work properly.

- Get it now from the downloads page

## Train your own Neural Networks​

- You can train your very own detection models for free with RoboFlow, the Limelight Detector Training Notebook,
and our new tutorial

## 2024 AprilTag Map and Note Detector​

- The map and detector model have been added to the downloads page and the latest Limelight OS image.

## Limelight OS 2024.0 (2/6/24)​

### ChArUco Calibration Fixes​

- Our ChArUco detector's subpixel accuracy has been increased. A reprojection error of 1-2 pixels is now achievable with clipboard targets and 20 images.

- Using the same camera and the same target, 2023.6 achieved an RPE of 20 pixels, and 2024.0 achieved an RPE of 1.14 pixels.

- Input fields no longer accept letters and special characters. This eliminates the potential for a crash.

### Out-Of-The-Box Megatag Accuracy Improvement​

- Before this update, Limelight's internal Megatag map generator referenced the UI's tag size slider instead of the tag sizes supplied by the .fmap file.

- Megatag now respects the tag sizes configured in fmap files and ignores the size slider.

- If your size slider has not been set to 165.1 mm, you will notice an immediate improvement in localization accuracy

### Performance Upgrades and Bugfixes​

- Higher FPS AprilTag pipelines

- The performance of the Field-Space Visualizer has been significantly improved.

### Bugfixes​

- Apriltags in 3D visualizers were sometimes drawn with incorrect or corrupted tag images. Tags are now always displayed correctly.

- "v" / tv / "valid" will now only return "1" if there are valid detections. Previously, tv was always "1"

- Limelight OS 2026.1 (4/17/26)- MegaTag2 Output Bugfix [CRITICAL]
- MegaTag2 IMU Modes 3, 4 Bugfix [CRITICAL]
- IMU Acquisition, Initialization, and Reliability [CRITICAL]
- Calibration Improvements and Bugfixes [CRITICAL]
- Increased AprilTag Range with Black Level Base Profiles and Focusing Updates
- H.264, UDP Video Streaming with WebRTC and WHEP signaling
- Per-Tag Point of Interest Defined in Fmap
- tDist
- Default Hailo 8L Detector
- Hailo UX
- Hailo-Accelerated AprilTags
- Language-Based, Zero-Shot Classification with Hailo and Transformers
- Learning-Based OCR (CPU RUNTIME)
- Neural Detector Clustering
- New IP Address Warning
- New NT Keys
- New JSON Results Fields

- Limelight OS 2026.0 (1/22/26)- Rewind (Only on Limelight 4)
- Calibration Overhaul
- Capture Latency Accuracy
- New All-in-one flash tool
- Live Data View
- Log Viewing
- Skewed Crop Windows
- Limelight OS Bugfixes
- Map Builder Improvements
- Neural Network Trainer
- Hailo Overhaul
- Improved 3A Experience on RoboRio
- Documentation
- New NT Keys
- Changed NT Keys
- New JSON Results Fields
- LimelightLib 1.13 (Java/C++) (Requires LLOS 2026.0)

- Limelight OS 2025.1 (FINAL RELEASE - 2/24/25 TEST RELEASE - 2/18/25)- LL4 IMU Updates
- LL4 Thermal Performance Updates
- New FPS Options for LL4 and LL3G
- REST API Updates
- FMap Updates
- ReefScape Neural Networks Uploaded
- LL3A Updates
- Bugfixes

- Limelight OS 2025.0 (1/15/24)- LL4 Support
- 2025 Field Updates

- Bugfixes
- Limelight OS 2024.10.2 (10/28/24)- Python Snapscript Fix (CREDIT - FTC TEAM 23251 TRIPLE FAULT)
- MT2 Edge case
- Static IP Addressing
- STDDevs NetworkTables
- Model Upload Edge case

- Limelight OS 2024.10.1 (9/15/24)- Limelight 3A Updates
- AprilTag Size Warning
- CameraPose_RobotSpace Bugfix

- Limelight OS 2024.10 (9/4/24)- Limelight 3A for FTC Support
- AprilTag Map Updates
- USB Limelight Support on ControlHub and RoboRio.
- USB Connectivity Upgrades
- REST API Updates

- Limelight OS 2024.9.1 (7/7/24)
- Limelight OS 2024.9 (7/5/24)- MegaTag Upgrades
- USB ID and New USB IP Addresses
- CPU Neural classifiers
- CPU Neural detectors

- Limelight OS 2024.8 (7/3/24)
- Limelight OS 2024.7 (5/21/24)- Bugfixes

- Limelight OS 2024.6 (5/8/24)- LimelightLib Python
- MegaTag2 Upgrades
- Standard Deviation Metrics
- New "Focus" Pipeline Type
- New "Barcodes" Pipeline Type
- All-New REST API
- Remove Camera Orientation Setting From UI (BREAKING CHANGE)
- Remove GRIP Support (BREAKING CHANGE)
- Remove "Driver" zero-processing mode (BREAKING CHANGE)
- Add "Viewfinder" Pipeline type
- Pipeline Files now Use JSON format (BREAKING CHANGE)
- Calibration UX Improvement
- Calibration Mosaic
- "Centroid" targeting region
- Dynamic 3D Offset (NT: fiducial_offset_set)
- Add Modbus Support
- Custom NT server
- Rawfiducial changes
- All NetworkTables and JSON Changes
- Changes to Other File Formats and JSON Dumps
- Bugfixes

- Limelight OS 2024.5.0 (4/9/24)- Camera Stack Update
- Dynamic Downscaling
- MegaTag2 Improvements
- "rawdetections" nt array
- Erode/Dilate Update

- LimelightLib 1.6 (4/9/24)
- Limelight OS 2024.4.0 (4/3/24)- Megatag 2
- Dynamic Apriltag Filtering
- Transitioning to MegaTag2

- LimelightLib 1.5 (4/3/24)
- Limelight OS 2024.3.4 (3/20/24)- Higher-Precision Single Tag Solver
- JSON Disabled by Default (Breaking Change)
- Undistorted Area (Breaking Change)
- Include Per-Fiducial Metrics in botpose, botpose_wpiblue, and botpose_wpired
- "rawtargets" and "rawfiducials" nt arrays (Breaking Change)
- Bugfixes

- LimelightLib 1.4 (3/21/24)
- Limelight Hardware Manager 1.4 (3/18/24)- Bugfix

- Limelight OS 2024.2.2 (3/17/24)- Bugfix

- Limelight OS 2024.2 (3/8/24)- Zero-Crosshair targeting with Json (tx_nocross, ty_nocross) and NT (txnc, tync)
- Potentially breaking change in tx/ty
- Calibration Upgrades
- Fiducial Filters UI Fix
- Misc

- Limelight OS 2024.1.1 (2/24/24)
- Limelight OS 2024.1 (2/24/24)- HW Metrics (hw key in networktables, /status GET request)
- Calibration Improvement
- Robot Localization Improvement (tag count and more)
- New Feature: Priority ID (NT Key priorityid)
- Misc

- LimelightLib 1.3
- New resources for Teams- Limelight Feedback and Issue Tracker: https://github.com/LimelightVision/limelight-feedback/issues
- Examples Repo: https://github.com/LimelightVision/limelight-examples
- Aiming and Ranging with Swerve Example: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-swerve-aiming-and-ranging
- MegaTag Localization Example: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-swerve-pose-estimation

- Limelight Documentation Upgrade
- Limelight AprilTag Generator
- Limelight Map Builder
- New Hardware Manager
- Train your own Neural Networks
- 2024 AprilTag Map and Note Detector
- Limelight OS 2024.0 (2/6/24)- ChArUco Calibration Fixes
- Out-Of-The-Box Megatag Accuracy Improvement
- Performance Upgrades and Bugfixes
- Bugfixes