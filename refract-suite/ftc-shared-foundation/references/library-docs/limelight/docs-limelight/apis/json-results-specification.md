> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/json-results-specification · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

JSON Results Specification | Limelight Documentation

 Skip to main content

 On this page

# JSON Results Specification

Limelight's JSON results output is a collection of arrays containing targeting results. Separate arrays exist for retroreflective, fiducial, neural classifier, and neural detector results.
JSON is human-readable and easy to parse in any language on any platform, so it is perfect for most use-cases.

The same JSON results output may be retrieved using the REST/HTTP, Websocket, and NetworkTables APIs.

Parsing this JSON output is incredibly easy with our FRC libraries.

Limelightlib has built-in functionality that parses the JSON Dump into a LimelightResults object.

https://github.com/LimelightVision/limelightlib-wpijava

https://github.com/LimelightVision/limelightlib-wpicpp

Every JSON result contains the following entries:

Key NameValue Description
vValidity indicator. 1 = valid targets, 0 = no valid targets
tsTimestamp in milliseconds from boot (legacy).
ts_usTimestamp in microseconds since application start.
ts_sysSystem wall clock timestamp in microseconds since epoch.
ts_ntNetworkTables server time in microseconds (0 if not connected).
fidxFrame index (counter starting at 0).
tlTargeting latency (milliseconds consumed by tracking loop this frame).
clCapture latency (milliseconds between the end of the exposure of the middle row to the beginning of the tracking loop).
pIDCurrent Pipeline index.
pTYPECurrent Pipeline Type e.g. "pipe_color".
txHorizontal Offset From Crosshair To Target (LL1: -27 degrees to 27 degrees / LL2: -29.8 to 29.8 degrees).
tyVertical Offset From Crosshair To Target (LL1: -20.5 degrees to 20.5 degrees / LL2: -24.85 to 24.85 degrees).
txncHorizontal Offset From Principal Pixel To Target (degrees).
tyncVertical Offset From Principal Pixel To Target (degrees).
taUndistorted, normalized area of target (0-100).
focus_metricFocus quality metric.
PythonOutOutput data from python SnapScript Pipelines (array of 8 doubles).
stdev_mt1MT1 Standard Deviation [x, y, z, roll, pitch, yaw] (meters, degrees).
stdev_mt2MT2 Standard Deviation [x, y, z, roll, pitch, yaw] (meters, degrees).
t6c_rsCamera pose in robot space [x, y, z, roll, pitch, yaw] (meters, degrees).
botposeBotpose (MegaTag): x,y,z, roll, pitch, yaw (meters, degrees).
botpose_wpiredBotpose (MegaTag, WPI Red driverstation): x,y,z, roll, pitch, yaw (meters, degrees).
botpose_wpiblueBotpose (MegaTag, WPI Blue driverstation): x,y,z, roll, pitch, yaw (meters, degrees).
botpose_orbBotpose (MegaTag2): x,y,z, roll, pitch, yaw (meters, degrees).
botpose_orb_wpiredBotpose (MegaTag2, WPI Red driverstation): x,y,z, roll, pitch, yaw (meters, degrees).
botpose_orb_wpiblueBotpose (MegaTag2, WPI Blue driverstation): x,y,z, roll, pitch, yaw (meters, degrees).
botpose_tagcountNumber of tags used to compute botpose.
botpose_spanMax distance between tags used to compute botpose (meters).
botpose_avgdistAverage distance from camera to tags used to compute botpose (meters).
botpose_avgareaAverage area of tags used to compute botpose (percentage of image).
RetroColor/Retroreflective pipeline results array.
FiducialAprilTag pipeline results array.
DetectorNeural Detector pipeline results array.
ClassifierClassifier pipeline results array.
BarcodeBarcode pipeline results array.
imgsrcImage source setting value.
hwtypeHardware type identifier.
uirefresh1 if web UI needs refresh, 0 otherwise.
ignorent1 if NetworkTables pipeline control is disabled, 0 otherwise.
imuIMU data object. See IMU Object below.
hwHardware stats object. See Hardware Object below.
rewindRewind buffer stats object (supported hardware only). See Rewind Object below.

## IMU Object​

The "imu" object contains IMU sensor data:

Key NameValue Description
quatOrientation quaternion array [w, x, y, z]
yawFinal fused yaw (degrees)
dataRaw IMU data array [roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate, accel_x, accel_y, accel_z] (degrees, deg/s)

## Hardware Object​

The "hw" object contains hardware diagnostics:

Key NameValue Description
tempCPU temperature (Celsius)
cpuCPU usage (percentage)
ramRAM usage (percentage)
dfreeDisk free space (MB)
dtotDisk total space (MB)
cidCamera sensor ID
hailoHailo accelerator stats object (if present). See Hailo Object below.

### Hailo Object​

The "hailo" sub-object (inside "hw") contains Hailo accelerator info:

Key NameValue Description
present1 if Hailo accelerator detected, 0 otherwise
typeHailo device type string
tempHailo temperature (Celsius)
powerHailo power consumption (watts)
throttleThrottle capability enabled

## Rewind Object​

The "rewind" object contains rewind buffer stats (supported hardware only):

Key NameValue Description
enabled1 if rewind recording is enabled, 0 if paused
storedSecondsSeconds of video currently stored in buffer
frameCountNumber of frames in buffer
bufferUsageBuffer usage (0.0 to 1.0)
flushing1 if currently flushing to disk, 0 otherwise

## Color/Retroreflective Results​

The "Retro" array contains entries with the following structure:

Key NameValue Description
t6c_tsCamera Pose in target space as computed by solvepnp (x,y,z,rx,ry,rz)
t6r_fsRobot Pose in field space as computed by solvepnp (x,y,z,rx,ry,rz)
t6r_tsRobot Pose in target space as computed by solvepnp (x,y,z,rx,ry,rz)
t6t_csTarget Pose in camera space as computed by solvepnp (x,y,z,rx,ry,rz)
t6t_rsTarget Pose in robot space as computed by solvepnp (x,y,z,rx,ry,rz)
taThe size of the target as a percentage of the image (0-1)
txX-coordinate of the center of the target in degrees relative to crosshair. Positive-right, center-zero
tx_nocrossX-coordinate of the center of the target in degrees relative to principal piexel. Positive-right, center-zero
txpX-coordinate of the center of the target in pixels relative to crosshair. Positive-right, center-zero
tyY-coordinate of the center of the target in degrees relative to crosshair. Positive-down, center-zero
ty_nocrossY-coordinate of the center of the target in degrees relative to principal pixel. Positive-right, center-zero
typY-coordinate of the center of the target in pixels relative to crosshair. Positive-down, center-zero
ptsCorners array (pixels) [x0,y0,x1,y1.....]. Must be enabled in output tab

Example JSON for Color / Retroreflective Pipelines{
 "Barcode": [],
 "Classifier": [],
 "Detector": [],
 "Fiducial": [],
 "PythonOut": [],
 "Retro": [
 {
 "pts": [],
 "t6c_ts": [],
 "t6r_fs": [],
 "t6r_ts": [],
 "t6t_cs": [],
 "t6t_rs": [],
 "ta": 0.00531171215698123,
 "tx": -4.535492777705656,
 "tx_nocross": -4.428826910553056,
 "txp": 542.53076171875,
 "ty": -1.1722867231218714,
 "ty_nocross": -0.09285491974145543,
 "typ": 504.5538635253906
 },
 {
 "pts": [],
 "t6c_ts": [],
 "t6r_fs": [],
 "t6r_ts": [],
 "t6t_cs": [],
 "t6t_rs": [],
 "ta": 0.005779948551207781,
 "tx": 8.465099348209478,
 "tx_nocross": 8.571765215362078,
 "txp": 822.1087036132812,
 "ty": -2.524207730360601,
 "ty_nocross": -1.444775926980185,
 "typ": 533.6112060546875
 },
 ],
 "botpose": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "botpose_avgarea": 0,
 "botpose_avgdist": 0,
 "botpose_orb": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "botpose_orb_wpiblue": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "botpose_orb_wpired": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "botpose_span": 0,
 "botpose_tagcount": 0,
 "botpose_wpiblue": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "botpose_wpired": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "cl": 37.619998931884766,
 "fidx": 1234,
 "focus_metric": 0,
 "pID": 0,
 "pTYPE": "pipe_color",
 "stdev_mt1": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "stdev_mt2": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "t6c_rs": [
 0,
 0,
 0,
 0,
 0,
 0
 ],
 "ta": 0.39156023412942886,
 "tl": 22.64053726196289,
 "ts": 215248.979204,
 "ts_us": 215248979204,
 "ts_sys": 1705432800000000,
 "ts_nt": 12345678901234,
 "tx": -4.3848327488723555,
 "txnc": -4.278166881719756,
 "ty": -1.1144596937982527,
 "tync": -0.035027890417836716,
 "v": 1,
 "imgsrc": 0,
 "hwtype": 7,
 "uirefresh": 0,
 "ignorent": 0,
 "imu": {
 "quat": [1, 0, 0, 0],
 "yaw": 0,
 "data": [0, 0, 0, 0, 0, 0, 0, 0, 0]
 },
 "hw": {
 "temp": 57.9,
 "cpu": 45.2,
 "ram": 32.1,
 "dfree": 12500,
 "dtot": 28000,
 "cid": 9281,
 "hailo": {
 "present": 1,
 "type": "HAILO8L",
 "temp": 52.3,
 "power": 3.2,
 "throttle": 0
 }
 },
 "rewind": {
 "enabled": 1,
 "storedSeconds": 45.2,
 "frameCount": 1356,
 "bufferUsage": 0.35,
 "flushing": 0
 }
}

## AprilTag/Fiducial Results​

The "Fiducial" array contains entries with the following structure:

Key NameValue Description
fIDFiducial tag ID
famFiducial Family (16H5C, 25H9C, 36H11C, etc)
ptsReturn individual corner points. Must be enabled.
skewCurrently unused
t6c_tsCamera Pose in target space as computed by this fiducial (x,y,z,pitch,yaw,roll) (meters, degrees)
t6r_fsRobot Pose in field space as computed by this fiducial (x,y,z,pitch,yaw,roll) (meters, degrees)
t6r_fs_orbRobot Pose in field space as computed by this fiducial (Megatag2) (x,y,z,pitch,yaw,roll) (meters, degrees)
t6r_tsRobot Pose in target space as computed by this fiducial (x,y,z,pitch,yaw,roll) (meters, degrees)
t6t_csTarget Pose in camera space as computed by this fiducial (x,y,z,pitch,yaw,roll) (meters, degrees)
t6t_rsTarget Pose in robot space as computed by this fiducial (x,y,z,pitch,yaw,roll) (meters, degrees)
taThe size of the target as a percentage of the image (0-1)
txX-coordinate of the center of the target in degrees relative to crosshair. Positive-right, center-zero
tx_nocrossX-coordinate of the center of the target in degrees relative to principal piexel. Positive-right, center-zero
txpX-coordinate of the center of the target in pixels relative to crosshair. Positive-right, center-zero
tyY-coordinate of the center of the target in degrees relative to crosshair. Positive-down, center-zero
ty_nocrossY-coordinate of the center of the target in degrees relative to principal pixel. Positive-right, center-zero
typY-coordinate of the center of the target in pixels relative to crosshair. Positive-down, center-zero
ptsCorners array (pixels) [x0,y0,x1,y1.....]. Must be enabled in output tab

Example JSON for AprilTag Pipelines{
 "Classifier": [],
 "Detector": [],
 "Fiducial": [
 {
 "fID": 2,
 "fam": "16H5C",
 "pts": [],
 "skew": [],
 "t6c_ts": [
 0.33247368976801916,
 -0.05672695778305914,
 -2.5042031405987144,
 -4.680849607956358,
 -5.171154989721864,
 4.528697946312339
 ],
 "t6r_fs": [
 4.738896418276903,
 -1.5926603672041666,
 0.5194469577830592,
 4.522658587661256,
 4.258580454853879,
 5.5236539893713275
 ],
 "t6r_ts": [
 0.33247368976801916,
 -0.05672695778305914,
 -2.5042031405987144,
 -4.680849607956358,
 -5.171154989721864,
 4.528697946312339
 ],
 "t6t_cs": [
 -0.09991902572799474,
 -0.1234042720218289,
 2.5218203039582496,
 4.278368708252767,
 5.508508005282244,
 -4.1112864453027775
 ],
 "t6t_rs": [
 -0.09991902572799474,
 -0.1234042720218289,
 2.5218203039582496,
 4.278368708252767,
 5.508508005282244,
 -4.1112864453027775
 ],
 "ta": 0.005711808800697327,
 "tx": -2.0525293350219727,
 "txp": 149.4874725341797,
 "ty": 2.7294836044311523,
 "typ": 107.14710235595703
 }
 ],
 "Retro": [],
 "pID": 0,
 "tl": 19.78130340576172,
 "ts": 3284447.910569,
 "v": 1
}

## Neural Detector Results​

The "Detector" array contains entries with the following structure:

Key NameValue Description
classHuman-readable class name string
classIDClassID integer
confConfidence of the predicition
ptsIndividual corner points as an array of [x,y] in pixels. Center-zero, positive right and down. Must be enabled.
taThe size of the target as a percentage of the image (0-1)
txX-coordinate of the center of the target in degrees relative to crosshair. Positive-right, center-zero
tx_nocrossX-coordinate of the center of the target in degrees relative to principal piexel. Positive-right, center-zero
txpX-coordinate of the center of the target in pixels relative to crosshair. Positive-right, center-zero
tyY-coordinate of the center of the target in degrees relative to crosshair. Positive-down, center-zero
ty_nocrossY-coordinate of the center of the target in degrees relative to principal pixel. Positive-right, center-zero
typY-coordinate of the center of the target in pixels relative to crosshair. Positive-down, center-zero
ptsCorners array (pixels) [x0,y0,x1,y1.....]. Must be enabled in output tab

Example JSON for Detector Pipelines{
 "Classifier": [],
 "Detector": [
 {
 "class": "person",
 "classID": 0,
 "conf": 0.83984375,
 "pts": [],
 "ta": 0.2608712911605835,
 "tx": -2.45949649810791,
 "txp": 147.5,
 "ty": -10.066887855529785,
 "typ": 165.5
 }
 ],
 "Fiducial": [],
 "Retro": [],
 "pID": 0,
 "tl": 63.50614547729492,
 "ts": 4932985.266867,
 "v": 1
}

## Neural Classifier Results​

The "Classifier" array contains entries with the following structure:

Key NameValue Description
classHuman-readable class name string
classIDClassID integer
confConfidence of the predicition

Example JSON for Classifier Pipelines{
 "Classifier": [
 {
 "class": "digital clock",
 "classID": 531,
 "conf": 0.16796875
 }
 ],
 "Detector": [],
 "Fiducial": [],
 "Retro": [],
 "pID": 0,
 "tl": 16.704740524291992,
 "ts": 4751332.7542280005,
 "v": 1
}

## Barcode Results​

The "Barcode" array contains entries with the following structure:

Key NameValue Description
famBarcode Family e.g. "qr"
dataDecoded barcode data as string
taThe size of the target as a percentage of the image (0-1)
txX-coordinate of the center of the target in degrees relative to crosshair. Positive-right, center-zero
tx_nocrossX-coordinate of the center of the target in degrees relative to principal piexel. Positive-right, center-zero
txpX-coordinate of the center of the target in pixels relative to crosshair. Positive-right, center-zero
tyY-coordinate of the center of the target in degrees relative to crosshair. Positive-down, center-zero
ty_nocrossY-coordinate of the center of the target in degrees relative to principal pixel. Positive-right, center-zero
typY-coordinate of the center of the target in pixels relative to crosshair. Positive-down, center-zero
ptsCorners array (pixels) [x0,y0,x1,y1.....]. Must be enabled in output tab

Example JSON for Barcode Pipelines{
 "Barcode": [
 {
 "fam": "QR",
 "data": "Hello, World!",
 "txp": 150.5,
 "typ": 120.75,
 "tx": -2.5,
 "ty": 1.8,
 "tx_nocross": -2.3,
 "ty_nocross": 2.0,
 "ta": 0.05,
 "pts": [[140, 110], [160, 110], [160, 130], [140, 130]]
 }
 ],
 "Classifier": [],
 "Detector": [],
 "Fiducial": [],
 "Retro": [],
 "pID": 0,
 "tl": 15.2,
 "ts": 4751332.7542280005,
 "v": 1
}

- IMU Object
- Hardware Object- Hailo Object

- Rewind Object
- Color/Retroreflective Results
- AprilTag/Fiducial Results
- Neural Detector Results
- Neural Classifier Results
- Barcode Results