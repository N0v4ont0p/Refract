> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/limelightlib-python · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Limelight Lib Python | Limelight Documentation

 Skip to main content

 On this page

# Limelight Lib Python

limelightlib-python is the easiest way to interface with Limelight devices. It works on all operating systems
(MacOS, Windows, Linux) and architectures (x86, ARM).

- https://github.com/LimelightVision/limelightlib-python

- https://pypi.org/project/limelightlib-python/

## Installation​

pip install limelightlib-python

## Usage​

import limelight
import limelightresults
import json
import time

discovered_limelights = limelight.discover_limelights(debug=True)
print("discovered limelights:", discovered_limelights)

if discovered_limelights:
 limelight_address = discovered_limelights[0] 
 ll = limelight.Limelight(limelight_address)
 results = ll.get_results()
 status = ll.get_status()
 print("-----")
 print("targeting results:", results)
 print("-----")
 print("status:", status)
 print("-----")
 print("temp:", ll.get_temp())
 print("-----")
 print("name:", ll.get_name())
 print("-----")
 print("fps:", ll.get_fps())
 print("-----")
 print("hwreport:", ll.hw_report())

 ll.enable_websocket()
 
 # print the current pipeline settings
 print(ll.get_pipeline_atindex(0))

 # update the current pipeline and flush to disk
 pipeline_update = {
 'area_max': 98.7,
 'area_min': 1.98778
 }
 ll.update_pipeline(json.dumps(pipeline_update),flush=1)

 print(ll.get_pipeline_atindex(0))

 # switch to pipeline 1
 ll.pipeline_switch(1)

 # update custom user data
 ll.update_python_inputs([4.2,0.1,9.87])

 try:
 while True:
 result = ll.get_latest_results()
 parsed_result = limelightresults.parse_results(result)
 if parsed_result is not None:
 print("valid targets: ", parsed_result.validity, ", pipelineIndex: ", parsed_result.pipeline_id,", Targeting Latency: ", parsed_result.targeting_latency)
 #for tag in parsed_result.fiducialResults:
 # print(tag.robot_pose_target_space, tag.fiducial_id)
 time.sleep(1) # Set this to 0 for max fps

 except KeyboardInterrupt:
 print("Program interrupted by user, shutting down.")
 finally:
 ll.disable_websocket()

## Methods​

### REST-based​

- get_results(): Fetches latest results via HTTP GET.

- capture_snapshot(snapname): Captures a snapshot with a given name.

- upload_snapshot(snapname, image_path): Uploads a snapshot with a given name and image file.

- snapshot_manifest(): Retrieves the snapshot manifest via HTTP GET.

- delete_snapshots(): Deletes all snapshots via HTTP GET.

- upload_neural_network(nn_type, file_path): Uploads a neural network file with a specified type.

- hw_report(): Fetches hardware report via HTTP GET.

- cal_default(): Fetches default calibration data via HTTP GET.

- cal_file(): Fetches calibration data from file via HTTP GET.

- cal_eeprom(): Fetches calibration data from EEPROM via HTTP GET.

- cal_latest(): Fetches the latest calibration data via HTTP GET.

- update_cal_eeprom(cal_data): Updates calibration data in EEPROM via HTTP POST.

- update_cal_file(cal_data): Updates calibration data in file via HTTP POST.

- delete_cal_latest(): Deletes the latest calibration data via HTTP DELETE.

- delete_cal_eeprom(): Deletes calibration data from EEPROM via HTTP DELETE.

- delete_cal_file(): Deletes calibration data from file via HTTP DELETE.

### Websocket-based​

- enable_websocket(): Initializes and starts a WebSocket connection in another thread.

- disable_websocket(): Closes the WebSocket connection and joins the thread.

- get_latest_results(): Returns the latest results received from the WebSocket.

### Parsing​

- limelightresults.parse_results(): Parse results and return a GeneralResult object

## Result Class Spec​

class GeneralResult:
 def __init__(self, results):
 self.barcode = results.get("Barcode", [])
 self.classifierResults = [ClassifierResult(item) for item in results.get("Classifier", [])]
 self.detectorResults = [DetectorResult(item) for item in results.get("Detector", [])]
 self.fiducialResults = [FiducialResult(item) for item in results.get("Fiducial", [])]
 self.retroResults = [RetroreflectiveResult(item) for item in results.get("Retro", [])]
 self.botpose = results.get("botpose", [])
 self.botpose_wpiblue = results.get("botpose_wpiblue", [])
 self.botpose_wpired = results.get("botpose_wpired", [])
 self.capture_latency = results.get("cl", 0)
 self.pipeline_id = results.get("pID", 0)
 self.robot_pose_target_space = results.get("t6c_rs", [])
 self.targeting_latency = results.get("tl", 0)
 self.timestamp = results.get("ts", 0)
 self.validity = results.get("v", 0)
 self.parse_latency = 0.0

class RetroreflectiveResult:
 def __init__(self, retro_data):
 self.points = retro_data["pts"]
 self.camera_pose_target_space = retro_data["t6c_ts"]
 self.robot_pose_field_space = retro_data["t6r_fs"]
 self.robot_pose_target_space = retro_data["t6r_ts"]
 self.target_pose_camera_space = retro_data["t6t_cs"]
 self.target_pose_robot_space = retro_data["t6t_rs"]
 self.target_area = retro_data["ta"]
 self.target_x_degrees = retro_data["tx"]
 self.target_x_pixels = retro_data["txp"]
 self.target_y_degrees = retro_data["ty"]
 self.target_y_pixels = retro_data["typ"]

class FiducialResult:
 def __init__(self, fiducial_data):
 self.fiducial_id = fiducial_data["fID"]
 self.family = fiducial_data["fam"]
 self.points = fiducial_data["pts"]
 self.skew = fiducial_data["skew"]
 self.camera_pose_target_space = fiducial_data["t6c_ts"]
 self.robot_pose_field_space = fiducial_data["t6r_fs"]
 self.robot_pose_target_space = fiducial_data["t6r_ts"]
 self.target_pose_camera_space = fiducial_data["t6t_cs"]
 self.target_pose_robot_space = fiducial_data["t6t_rs"]
 self.target_area = fiducial_data["ta"]
 self.target_x_degrees = fiducial_data["tx"]
 self.target_x_pixels = fiducial_data["txp"]
 self.target_y_degrees = fiducial_data["ty"]
 self.target_y_pixels = fiducial_data["typ"]

class DetectorResult:
 def __init__(self, detector_data):
 self.class_name = detector_data["class"]
 self.class_id = detector_data["classID"]
 self.confidence = detector_data["conf"]
 self.points = detector_data["pts"]
 self.target_area = detector_data["ta"]
 self.target_x_degrees = detector_data["tx"]
 self.target_x_pixels = detector_data["txp"]
 self.target_y_degrees = detector_data["ty"]
 self.target_y_pixels = detector_data["typ"]

class ClassifierResult:
 def __init__(self, classifier_data):
 self.class_name = classifier_data["class"]
 self.class_id = classifier_data["classID"]
 self.confidence = classifier_data["conf"]

- Installation
- Usage
- Methods- REST-based
- Websocket-based
- Parsing

- Result Class Spec