> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/pipelines · Fetched: 2026-07-12
> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltags · Fetched: 2026-07-12

# Pipeline Setup

LimelightOS stores up to 10 unique vision pipelines. A pipeline is like a small program that takes an image, processes the image, and provides a results object for you to use in your robot code. Pipelines run anywhere from 10fps (CPU Neural Networks) to 90fps (Color-based object tracking).

To start tuning pipelines, connect to the web interface over ethernet, wifi, or usb as described in your unit's quick start guide (for FTC's Limelight 3A, see [setup.md](./setup.md)).

If you are an advanced user and have changed the USB Index or Hostname of your LL, you can access the web interface at `http://172.28.(usb_index).1:5801`, `http://172.29.(usb_index).1:5801`, or `http://<hostname>.local:5801`.

> To edit multiple pipelines, you must first check the "Ignore NetworkTables Index" checkbox in the web interface. This tells the camera to ignore any code telling it to change pipelines.

To download your pipelines for backups and sharing, click the "download" button next to your pipeline's name. To upload a pipeline, click the "upload" button. When the robot switches pipelines, the web interface auto-loads the new pipeline.

## Input Tab

The Input Tab hosts controls to change the raw camera image before it is passed through the processing pipeline.

### Pipeline Type

Controls the desired pipeline type (AprilTags, Neural Networks, Python, etc.)

### Source Image

Controls the source of the image that is passed through the pipeline. Switch to "Snapshot" to test your vision pipelines on stored Snapshots.

This control auto-resets to "Camera" when the GUI is closed.

### Resolution + Zoom

Controls the resolution of the camera and vision pipeline. Use the 320x240 pipeline unless you are utilizing 3D functionality.

320x240 pipelines execute at 90fps, while 960x720 pipelines execute at 22 fps. 2x and 3x Hardware Zoom options are available; these are not digital and use 100% real sensor pixels.

### LEDs

Controls the default LED mode for this pipeline. This may be overridden during a match with the "LED" network table option.

Limelight 2+ users have access to an "LED Brightness" slider which allows for LED dimming.

### Stream Orientation

Controls the orientation of the stream after all processing. This does not affect results data in any way.

### Exposure

Controls the camera's exposure setting in .01 millisecond intervals. Think of a camera as a grid of light-collecting buckets — exposure time controls how long your camera's "buckets" are open per frame. Lowering the exposure time will effectively darken your image. Low and fixed exposure times are crucial for reliable tracking, as they black out the bulk of incoming image data.

### Black Level Offset

Increasing the black level offset can significantly darken your camera stream. This should be increased to further remove arena lights and bright spots from your image. This is a sensor-level setting, not a fake digital brightness setting.

### Sensor Gain

Increasing sensor gain will effectively increase the brightness of the image, but it will usually add noise to the image as well. Use Sensor Gain and Black Level Offset together to brighten the image without increasing exposure time — this minimizes motion blur for high-speed tracking applications.

### Red Balance, Blue Balance

Controls the intensity of Red and Blue color components in your image. These collectively control your Limelight's white balance. It's recommended to leave these untouched.

---

# Tracking AprilTags

AprilTags are tracked using the standard "tx", "ty", and "ta" values. No code changes are required to upgrade a color/retroreflective tracking robot to AprilTags. "botpose" and "campose" may also be used for field-space and target-space 3D tracking (see [localization.md](./localization.md)).

For more advanced usage with multiple tags, the JSON results dump may be used.

## Tips

For ideal tracking, consider the following:

- Your tags should be as flat as possible.
- Your Limelight should be mounted above or below tag height and angled up/down such that the target is centered. Your target should look as trapezoidal as possible from your camera's perspective. Avoid having your camera completely "head-on" with a tag if you want to avoid tag flipping.

There is an interplay between the following variables for AprilTag Tracking:

- Increasing capture resolution will always increase 3D accuracy and increase 3D stability. This will also reduce the rate of ambiguity flipping from most perspectives. It will usually increase range. This will reduce pipeline framerate.
- Increasing detector downscale will always increase pipeline framerate. It will decrease effective range, but in some cases this may be negligible. It will not affect 3D accuracy, 3D stability, or decoding accuracy.
- Reducing exposure will always improve motion-blur resilience. This may reduce range.
- Reducing the brightness and contrast of the image will generally improve pipeline framerate and reduce range.
- Increasing Sensor Gain allows you to increase brightness without increasing exposure. It may reduce 3D stability and tracking stability.

## Input Tab

To track AprilTags:

- Change "Pipeline Type" to "Fiducial Markers"
- Set "Black Level" to zero

At this point, it is a matter of balancing sensor gain and exposure time. You want to be able to see the tags with the smallest exposure possible to minimize motion blur. This usually calls for a high sensor gain setting. For simple 2D tracking, it is often advisable to max out your sensor gain, and then increase your exposure from zero until targets are sufficiently tracked. Make sure the correct family is selected in the "Standard" tab if tracking isn't working.

## Standard Tab

### Family

Selects the fiducial/AprilTag family type.

> Note: the source page's Family/Marker Size guidance below ("AprilTag Classic 36h11", 165.1mm / 152.4mm) is written for FRC. FTC teams should set the family and tag size to match the current season's official FTC field AprilTag family/size rather than these FRC values — check the current game manual or the pre-installed field map on your Limelight 3A.

### Marker Size

Sets the expected size of the tags your robot will encounter in mm.

### Detector Downscale

Increasing this number will result in significant performance boosts. This will sometimes result in reduced range, but the cost is usually minimal.

### ID Filters

ID Filters allow you to specify exactly which tags you care about. This is a comma-separated list of numbers (e.g. "0,1"). This feature is important for eliminating the vast majority of false positives.

### Cropping

Cropping removes content from the image for huge performance boosts. Use the NT "crop" key to crop dynamically during matches.

### Multi-Target Sorting and Grouping

This allows for the exact grouping functionality seen in standard retroreflective pipelines. In most games, the only feature to modify is the "Area" filter, which allows you to filter out small tags.
