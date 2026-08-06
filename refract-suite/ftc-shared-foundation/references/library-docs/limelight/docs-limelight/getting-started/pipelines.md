> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/pipelines · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Pipeline Setup | Limelight Documentation

 Skip to main content

 On this page

# Pipeline Setup

LimelightOS stores up to 10 unique vision pipelines.
A pipeline is like a small program that takes an image, processes the image, and provides a results object for you to use in your robot code.
Pipelines run anywhere from 10fps (CPU Neural Networks) to 90fps (Color-based object tracking).

To start tuning pipelines, connect to the web interface over ethernet, wifi, or usb as described in your unit's quick start guide.

If you are an advanced user and have changed the USB Index or Hostname of your LL, you can access the web interface at
http://172.28.(usb_index).1:5801, http://172.29.(usb_index).1:5801, or http://.local:5801

 info
To edit multiple pipelines, you must first check the “Ignore NetworkTables Index” checkbox in the web interface. This tells the camera to ignore any code telling it to change pipelines.

To download your pipelines for backups and sharing, simply click the “download” button next to your pipeline’s name. To upload a pipeline, click the “upload” button.

Here’s an example of a robot that utilizes two pipelines:

https://thumbs.gfycat.com/UnfitLankyHadrosaurus-size_restricted.gif
The first pipeline is tuned to target single vertical stripes. The second pipeline is tuned to find a combo of two horizontal stripes. The code for this robot is available in the “Aim and Range” case study.

Notice that when the robot switches pipelines, the web interface auto-loads the new pipeline.

## Input Tab​

The Input Tab hosts controls to change the raw camera image before it is passed through the processing pipeline.

### Pipeline Type​

Controls the desired pipeline type (AprilTags, Neural Networks, Python, etc.)

### Source Image​

Controls the source of the image that is passed through the pipeline. Switch to “Snapshot” to test your vision pipelines on stored Snapshots.

This control auto-resets to “Camera” when the GUI is closed.

### Resolution + Zoom​

Controls the resolution of the camera and vision pipeline. We recommend using the 320x240 pipeline unless you are utilizing 3D functionality.

320x240 pipelines execute at 90fps, while 960x720 pipelines execute at 22 fps. In 2020, 2x and 3x Hardware Zoom options were added to this field. The zoom options are not digital and use 100% real sensor pixels.

### LEDs​

Controls the default LED mode for this pipeline. This may be overridden during a match with the “LED” network table option.

Limelight 2+ users have access to an “LED Brightness” Slider which allows for LED dimming.

### Stream Orientation​

Controls the orientation of the stream after all processing. This does not affect results data in any way.

### Exposure​

Controls the camera’s exposure setting in .01 millisecond intervals. Think of a camera as a grid of light-collecting buckets - exposure time controls how long your camera’s “buckets” are open per frame. Lowering the exposure time will effectively darken your image. Low and fixed exposure times are crucial in FRC, as they black-out the bulk of incoming image data. Well-lit retroreflective tape will stand out in a mostly black image, turning vision processing into a straightforward process.

### Black Level Offset​

Increasing the black level offset can significantly darken your camera stream. This should be increased to further remove arena lights and bright spots from your image. This is a sensor-level setting, and not a fake digital brightness setting.

### Sensor Gain​

Increasing sensor gain will effectively increase the brightness of the image, but it will usually add noise to the image as well. You can use Sensor Gain and Black level offset to brighten the image without increasing exposure time. This will minimize motion blur for high-speed tracking applications.

### Red Balance, Blue Balance​

Controls the intensity of Red and Blue color components in your image. These collectively control your Limelight’s white balance. We recommend leaving these untouched

- Input Tab- Pipeline Type
- Source Image
- Resolution + Zoom
- LEDs
- Stream Orientation
- Exposure
- Black Level Offset
- Sensor Gain
- Red Balance, Blue Balance