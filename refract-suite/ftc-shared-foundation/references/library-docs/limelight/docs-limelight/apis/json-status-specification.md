> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/json-status-specification · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

JSON Status Specification | Limelight Documentation

 Skip to main content

# JSON Status Specification

Limelight's JSON status output is useful for general diagnostic information
The same JSON status output may be retrieved using one of our libraries, or via GET request at (ipaddress):5807/status

Every JSON status object contains the following entries:

Key NameValue Description
pipelineIndexCurrent pipeline index (0-9)
pipelineTypeCurrent pipeline type e.g. "pipe_color", "pipe_fiducial"
ignoreNT1 if NetworkTables pipeline control is disabled
interfaceNeedsRefresh1 if web interface needs refresh
pipeImgCountNumber of images in current pipeline
snapshotModeSnapshot mode flag
hwTypeHardware type identifier
nameDevice hostname
cidCamera Sensor ID
tempCPU temperature (Celsius)
cpuCPU usage (percentage)
ramRAM usage (percentage)
fpsCurrent processing FPS
finalYawFinal fused yaw from IMU (degrees)
cameraQuatCamera orientation quaternion (w, x, y, z)
finalimuIMU data array: [robot_yaw, roll, pitch, internal_yaw, roll_rate, pitch_rate, yaw_rate, accel_x, accel_y, accel_z] (degrees, deg/s)

{
 "pipelineIndex": 0,
 "pipelineType": "pipe_color",
 "ignoreNT": 0,
 "interfaceNeedsRefresh": 0,
 "pipeImgCount": 2,
 "snapshotMode": 0,
 "hwType": 7,
 "name": "limelight",
 "cid": 5647,
 "temp": 57.93899917602539,
 "cpu": 47.208126068115234,
 "ram": 75.23017120361328,
 "fps": 63.55415344238281,
 "finalYaw": 0,
 "cameraQuat": {
 "w": 1,
 "x": 0,
 "y": 0,
 "z": 0
 },
 "finalimu": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}