> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/rest-http-api · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

REST/HTTP API | Limelight Documentation

 Skip to main content

 On this page

# REST/HTTP API

Limelight OS features a REST/HTTP server running at (ipaddress):5807

LimelightLib Python is an open-source library that utilizes the Limelight HTTP/REST API.

Note: e.g. http://(limelight-ip-address):5807/results

## General​

MethodRouteDescription
GET/resultsReturns full JSON dump of current targeting results.
GET/statusReturns JSON status object with temperature, fps, device name, pipeline index, cpu usage, ram usage.
GET/hwreportReturns JSON array of full hardware reports with FOV, principal offset, calibration info, etc.

## Pipeline Management​

MethodRouteDescription
GET/pipeline-defaultGet default pipeline (JSON)
GET/pipeline-atindexGet pipeline[n] from the camera (JSON). Loads pipeline from disk. Include an 'index' url parameter in the request.
POST/pipeline-switchSwitch to a different pipeline. Include an 'index' url parameter in the request.
POST/reload-pipelineForce the camera to reload the current pipeline and all pipeline resources
POST/update-pipelineAccepts JSON with one or more settings updates. Set url parameter "flush" to 1 to save these settings to disk.
POST/upload-pipelineUpload a pipeline. Send JSON data in the request body. Optionally include an 'index' parameter. Overwrites pipeline on disk

## Camera Management​

MethodRouteDescription
POST/update-imumodeSet IMU Mode. Request body: JSON integer.
POST/update-throttleSet number of frames to skip between processed frames for thermal management. Request body: JSON integer.
POST/update-imuassistalphaSet IMU Assist Mode complementary filter alpha (default 0.001). Request body: JSON double.

## Resource Management​

MethodRouteDescription
POST/upload-fieldmapUpload a field map. Send JSON data in the request body. Optionally include an 'index' parameter.
POST/upload-pythonUpload Python code. Send the code as plain text in the request body. Optionally include an 'index' parameter.
POST/upload-nnUpload a neural network model. Query params: type ("detector" or "classifier"), format ("tflite" or "hef", default "tflite", detectors only), index (optional, 0-9). Request body: binary model file. Detectors support TFLite (.tflite) and Hailo (.hef) formats. Classifiers support TFLite only.
POST/upload-nnlabelsUpload neural network labels. Query params: type ("detector" or "classifier"), index (optional, 0-9). Request body: plain text file with one label per line.
GET/getsnapscriptnamesReturns JSON array of available SnapScript Python script names.

## Python and Robot Orientation​

MethodRouteDescription
POST/update-pythoninputsUpdate Python inputs for SnapScript pipelines. Send JSON data (array) in the request body.
POST/update-robotorientationUpdate robot orientation. Send JSON data (array) in the request body. EG "[45,0,0,0,0,0]. Use of this method disables NetworkTables-based orientation updates until restart/reboot

## Calibration​

MethodRouteDescription
GET/cal-defaultReturns JSON of default calibration result.
GET/cal-fileReturns JSON of custom calibration result (file system).
GET/cal-eepromReturns JSON of custom calibration result (eeprom).
GET/cal-latestReturns JSON of latest custom calibration result. This result is not used unless it is saved to the file system or the eeprom.
GET/cal-pointcloudDownloads the calibration point cloud as a PLY file (binary).
GET/cal-statsReturns JSON with calibration statistics including reprojection errors and point counts.
POST/cal-fileUpdate the filesystem calibration result. Request body: JSON calibration data.
DELETE/cal-latestDelete latest calibration result.
DELETE/cal-eepromDelete eeprom calibration result.
DELETE/cal-fileDelete filesystem calibration result.

## Snapshots​

MethodRouteDescription
POST/capture-snapshotCapture a snapshot. Include a 'snapname' url parameter to name the snapshot.
POST/upload-snapshotUpload a named snapshot image. Query param: snapname. Request body: image file (JPEG/PNG binary).
GET/snapshotmanifestReturns JSON array of snapshot file names.
DELETE/delete-snapshotsDeletes all snapshots.
DELETE/delete-snapshotDelete a specific snapshot. Include a 'snapname' parameter in the request.

## Rewind Video Recording​

Limelight continuously records frames into a rewind buffer. When flushed, recordings are saved as:

- .avi - MJPEG video file

- _manifest.jsonl - Frame-by-frame JSON results (one JSON object per line, matching each video frame)

- _bootlog.txt.gz - Gzipped system journal logs from the current boot session (for debugging)

MethodRouteDescription
GET/videolistReturns JSON array of recorded videos. Each entry has name (string) and size (number, combined bytes of video + manifest). Sorted oldest to newest by creation order.
GET/recording-listReturns JSON with detailed recording info. Each entry has video, manifest, bootlog (or null), and size fields. Sorted by filename.
GET/recording/filenameDownloads a recording file by name. Supports .avi, _manifest.jsonl, and _bootlog.txt.gz files. Returns binary file data with appropriate Content-Type.
POST/recording-flushSaves the rewind buffer to disk. Query parameter: duration (1-500 seconds, default 10). Returns JSON with success and message fields.
DELETE/delete-videoDeletes a specific recording and its associated manifest. Query parameter: name (the video filename).
DELETE/delete-videosDeletes all recorded videos and manifests.

- General
- Pipeline Management
- Camera Management
- Resource Management
- Python and Robot Orientation
- Calibration
- Snapshots
- Rewind Video Recording