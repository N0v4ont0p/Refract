> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-3a · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Limelight 3A Quick-Start | Limelight Documentation

 Skip to main content

 On this page

# Limelight 3A Quick-Start

## Hardware Specifications​

- Footprint: 2.839in x 1.894in (72.11mm x 48.11mm)

- Thickness: 0.661in (16.80mm)

- Mass: 0.20 lb

- Mounting: 4x #10 THRU, 4x M3, 6x M4 threaded mounting holes

- Power Input: 4.1V-5.75V via USB

- Maximum Power Consumption: 4W

- Sensor: OV5647 Color Rolling Shutter (640x480 @ 90FPS)

- No built-in LED illumination

- Field of View: H:54.5° V:42°

- USB-C connectivity only (no RJ45 port)

- Status Light: Green (target detection)

- Optimized for FTC compatibility

## Software Capabilities (Limelight OS)​

- Plug-and-Play high-performance vision. No experience required.

- Self-hosted browser-based UI for vision pipeline configuration

- Support for FTC (direct Java integration) and FRC (NetworkTables interface)

- Configurable exposure, sensor gain, resolution, and framerate

- Configure 10 Hot-swappable Vision Pipelines:

- Custom Python Pipelines with OpenCV 4.10, numpy, etc.

- 2D, 3D AprilTag Tracking and Robot Localization

- Full 3D Localization (Robot GPS) with MegaTag1

- Higher-Accuracy Full 3D Localization (Robot GPS) with External IMU Fusion with MegaTag2

- 20fps @ 1280x960 (2x downscale), 50fps @ 640x480 (2x downscale)

- Full 3D Visualizer in web interface

- 90FPS Color Blob pipelines

- Neural Object Detection Pipelines (CPU Inferenace only)

- Neural Image Classification Pipelines (CPU Inferenace only)

- Barcode Tracking Pipelines

- Built-in Charuco Intrinsics Calibration interface

- Built-in low-latency MJPEG Streaming

## 1. Mounting Limelight 3A​

#### Threaded Mounting (Recommended)​

- Use at least 2 M3 or M4 screws to mount your LL3A to Rev or GoBilda Channel using the threaded mount holes

- You can also use VHB tape or zip ties to constrain your Limelight

#### Thru-Hole Mounting​

- Use 1 1/4" #10-32 or #10-24 bolts with nylock nuts

- Alternatively, use 28mm M4 bolts with nylock nuts

## 2. Wiring Limelight 3A​

When you're ready to use your Limelight on your robot:

### For FTC​

- Run a USBC to USBA cable from your Limelight 3A to your Control Hub's USB 3.0 Port

- Connect to your Control Hub by plugging into a USB 3.0 port (blue port)

### For FRC​

- Connect your Limelight 3A to your roboRIO USB port

- Use a USB-C to USB-A cable

Limelight 3A does not support Google Coral. You can still use neural detection and classification pipelines by setting the neural network runtime engine to "CPU".

## 3. Accessing the Web Interface​

After connecting your Limelight 3A to your computer via USB:

- Wait for the green status light to become active (about 15-20 seconds)

- Use one of these methods to access the web interface:

- Method 1: Open the Limelight Hardware Manager application, scan for Limelights, and double-click on your Limelight 3A when it appears

- Method 2: Open a web browser and navigate to http://limelight.local:5801

Once connected, you'll have access to:

- Settings tab - Configure team number, hostname, and other system settings

- Vision Pipeline tabs - Set up and tune your vision processing pipelines

- Camera & Crosshair tab - Adjust camera settings and crosshair parameters

- 3D Visualization tab - View real-time AprilTag detection and localization

All configuration is done through this web interface. Changes are saved automatically to your Limelight.

## 4. Updating LimelightOS​

 caution
Backup your pipelines and scripts before upgrading - they will be erased during this process!

- Power off your Limelight

- Download the latest Limelight Hardware Manager and Limelight OS image

- Hold the blue config button while connecting a USB-C cable from your laptop to your Limelight

- Open Limelight Hardware Manager

- Navigate to the "Flash OS" tab

- Select the OS image file and wait for extraction to complete

- Click "Refresh Device List"

- Select your Limelight device from the list

- Click "Flash Device" and wait for completion

- Remove the USB cable after completion

Legacy Update Instructions (macOS & Linux) warning
Save your pipelines before updating LimelightOS. They will be deleted during the update.

- Download the Limelight OS image and Balena Flash tool from the Downloads Page

- Build the USB Boot driver yourself:

brew install libusb
brew install pkg-config
git clone --recurse-submodules --shallow-submodules --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot
make
cd mass-storage-gadget64
sudo ../rpiboot -d .
# As long as rpiboot is running, your camera will properly enumerate on macOS and Linux
# You need to run rpiboot every time you want to flash.

- Hold the blue config button on your Limelight

- While holding, run a USB-C cable from your laptop to your Limelight (your Limelight will power on automatically)

- After you've plugged your LL into your laptop, you can release the blue config button

- Your Limelight is now in flash mode, and its LEDs will not blink

- Run "Balena Etcher"

- It may take up to 20 seconds for your machine to recognize the camera

- Select the latest .zip image in your downloads folder

- Select a "Compute Module" device in the "Drives" menu

- Click "Flash"

- Once flashing is complete, remove the USB cable from your Limelight

Legacy Update Instructions (Windows) warning
Save your pipelines before updating LimelightOS. They will be deleted during the update.

- Download the latest USB drivers, Limelight OS image, and Balena Flash tool from the Downloads Page

- Reboot your machine after installing drivers

- Hold the blue config button on your Limelight

- While holding, run a USB-C cable from your laptop to your Limelight (your Limelight will power on automatically)

- After you've plugged your LL into your laptop, you can release the blue config button

- Your Limelight is now in flash mode, and its LEDs will not blink

- Run "Balena Etcher" as an administrator

- It may take up to 20 seconds for your machine to recognize the camera

- Select the latest .zip image in your downloads folder

- Select a "Compute Module" device in the "Drives" menu

- Click "Flash"

- Once flashing is complete, remove the USB cable from your Limelight

## 5. Setup Process​

### For FTC​

- Connect your Limelight to your laptop with a USB cable

- Access the web interface as described in section 3

- Go to the Settings tab and set your team number, then click "Restart Vision Client"

- Configure your pipelines as desired (AprilTag, Neural Networks, Custom Python, etc.)

- When ready for competition, plug your Limelight 3A into your Control Hub's USB 3.0 port

- In the FTC DriverStation App, click "Configure Robot"

- If you don't have an active configuration, you may need to make a new one

- Click the "scan" button

- You should see an "Ethernet Device" appear

- You can edit the name of this device to "limelight" for clarity

- Now you can initialize a Limelight3A object in your code using the hardware map

### For FRC​

- Connect your Limelight 3A to your laptop, wait for status light activity

- Access the web interface as described in section 3

- In Settings tab, set your team number and click "Restart Vision Client"

- Configure your pipelines as desired

- When ready, plug your Limelight 3A into your roboRIO's USB port

- Open your preferred dashboard to make sure your 3A is submitting data to your roboRIO's NetworkTables

- Add Port Forwarding to enable live pipeline editing while connected to your robot's network:

- Java
- CPP
// (robotIP):5801 will now point to a Limelight3A's (id 0) web interface stream:
// (robotIP):5800 will now point to a Limelight3A's (id 0) video stream:
PortForwarder.getInstance().add(5801, "172.29.0.1", 5801);
PortForwarder.getInstance().add(5802, "172.29.0.1", 5802);
PortForwarder.getInstance().add(5803, "172.29.0.1", 5803);
PortForwarder.getInstance().add(5804, "172.29.0.1", 5804);
PortForwarder.getInstance().add(5805, "172.29.0.1", 5805);
PortForwarder.getInstance().add(5806, "172.29.0.1", 5806);
PortForwarder.getInstance().add(5807, "172.29.0.1", 5807);
PortForwarder.getInstance().add(5808, "172.29.0.1", 5808);
PortForwarder.getInstance().add(5809, "172.29.0.1", 5809);

// (robotIP):5811 will now point to a Limelight3A's (id 1) web interface stream:
// (robotIP):5810 will now point to a Limelight3A's (id 1) video stream:
PortForwarder.getInstance().add(5811, "172.29.1.1", 5801);
PortForwarder.getInstance().add(5812, "172.29.1.1", 5802);
PortForwarder.getInstance().add(5813, "172.29.1.1", 5803);
PortForwarder.getInstance().add(5814, "172.29.1.1", 5804);
PortForwarder.getInstance().add(5815, "172.29.1.1", 5805);
PortForwarder.getInstance().add(5816, "172.29.1.1", 5806);
PortForwarder.getInstance().add(5817, "172.29.1.1", 5807);
PortForwarder.getInstance().add(5818, "172.29.1.1", 5808);
PortForwarder.getInstance().add(5819, "172.29.1.1", 5809);

// (robotIP):5801 will now point to a Limelight3A's (id 0) web interface stream:
// (robotIP):5800 will now point to a Limelight3A's (id 0) video stream:
wpi::PortForwarder::GetInstance().Add(5801,"172.29.0.1",5801); 
wpi::PortForwarder::GetInstance().Add(5802,"172.29.0.1",5802);
wpi::PortForwarder::GetInstance().Add(5803,"172.29.0.1",5803); 
wpi::PortForwarder::GetInstance().Add(5804,"172.29.0.1",5804);
wpi::PortForwarder::GetInstance().Add(5805,"172.29.0.1",5805); 
wpi::PortForwarder::GetInstance().Add(5806,"172.29.0.1",5806);
wpi::PortForwarder::GetInstance().Add(5807,"172.29.0.1",5807);
wpi::PortForwarder::GetInstance().Add(5808,"172.29.0.1",5808);
wpi::PortForwarder::GetInstance().Add(5809,"172.29.0.1",5809);

// (robotIP):5811 will now point to a Limelight3A's (id 1) web interface stream:
// (robotIP):5810 will now point to a Limelight3A's (id 1) video stream:
wpi::PortForwarder::GetInstance().Add(5811,"172.29.1.1",5801); 
wpi::PortForwarder::GetInstance().Add(5812,"172.29.1.1",5802);
wpi::PortForwarder::GetInstance().Add(5813,"172.29.1.1",5803); 
wpi::PortForwarder::GetInstance().Add(5814,"172.29.1.1",5804);
wpi::PortForwarder::GetInstance().Add(5815,"172.29.1.1",5805); 
wpi::PortForwarder::GetInstance().Add(5816,"172.29.1.1",5806);
wpi::PortForwarder::GetInstance().Add(5817,"172.29.1.1",5807);
wpi::PortForwarder::GetInstance().Add(5818,"172.29.1.1",5808);
wpi::PortForwarder::GetInstance().Add(5819,"172.29.1.1",5809);

## 6. Available Pipeline Types​

The Limelight 3A offers the same vision processing features as other Limelight models:

- AprilTag tracking and robot localization

- Color blob tracking

- Neural network object detection (CPU only)

- Neural network classification

- Barcode tracking

- Custom Python pipelines

Each 3A ships with a built-in Into The Deep field map for FTC.

## 7. FTC Programming​

Basic FTC Example: FTC Sample

Most applications require less than 10 lines of code:

public class Teleop extends LinearOpMode {

 private Limelight3A limelight;

 @Override
 public void runOpMode() throws InterruptedException
 {
 limelight = hardwareMap.get(Limelight3A.class, "limelight");

 telemetry.setMsTransmissionInterval(11);

 limelight.pipelineSwitch(0);

 /*
 * Starts polling for data.
 */
 limelight.start();
 
 while (opModeIsActive()) {
 LLResult result = limelight.getLatestResult();
 if (result != null) {
 if (result.isValid()) {
 Pose3D botpose = result.getBotpose();
 telemetry.addData("tx", result.getTx());
 telemetry.addData("ty", result.getTy());
 telemetry.addData("Botpose", botpose.toString());
 }
 }
 }
 }
}

For maximum 3D localization accuracy, call updateRobotOrientation() and use getBotPose_MT2():

while (opModeIsActive()) {
 YawPitchRollAngles orientation = imu.getRobotYawPitchRollAngles();
 limelight.updateRobotOrientation(orientation.getYaw(AngleUnit.DEGREES));
 LLResult result = limelight.getLatestResult();
 if (result != null) {
 if (result.isValid()) {
 Pose3D botpose = result.getBotpose_MT2();
 // Use botpose data
 }
 }
}

For more information, see the FTC Programming page

## 8. Troubleshooting​

### Status Light Indicators​

- Green Light: Blinks slowly (no targets), blinks quickly (targets detected)

### FAQ​

- 
Why does my Limelight feel so hot?
For Limelight to run as cool as possible, it necessarily needs to feel as hot as possible/as is safe to the touch. Its enclosure is a highly conductive heatsink that helps keep the CPU at a reasonably cool temperature.

- 
Why does the image look so grainy?
To minimize latency, several filters normally present on commercial cameras are skipped. The stream is also compressed to minimize bitrate. In 2024.10.1, we changed the default color balance values to make images look more natural and vibrant to the human eye.

- 
What does Limelight offer over OpenCV on the Control Hub?
An out-of-the-box, zero-code, multi-tag localization algorithm with robot IMU sensor fusion, neural networks, and more.

- Hardware Specifications
- Software Capabilities (Limelight OS)
- 1. Mounting Limelight 3A
- 2. Wiring Limelight 3A- For FTC
- For FRC

- 3. Accessing the Web Interface
- 4. Updating LimelightOS
- 5. Setup Process- For FTC
- For FRC

- 6. Available Pipeline Types
- 7. FTC Programming
- 8. Troubleshooting- Status Light Indicators
- FAQ