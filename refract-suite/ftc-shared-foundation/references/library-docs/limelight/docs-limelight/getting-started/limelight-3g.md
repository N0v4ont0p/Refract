> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-3g · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Limelight 3G Quick-Start | Limelight Documentation

 Skip to main content

 On this page

# Limelight 3G Quick-Start

## Hardware Specifications​

- Footprint: 3.154in x 1.894in (80.11mm x 48.11mm)

- Thickness: 1.160in (29.46mm)

- Mass: 0.24 lb

- #10 / M4 Thru-Hole Mounting

- M3 Threaded mounting holes

- Power Input: 4.1V-16V (4.1V-24V for red button variant, 30V absolute maximum)

- 4W maximum power consumption

- Sensor: OV9281 Global Shutter Monochrome (1280x800 @ 120FPS, 640x480 @ 240FPS)

- Replaceable M12 Lens

- 82 deg Horizontal FOV, 56.2 deg Vertical FOV

- Black-Anodized, All-Aluminium Enclosure

- Gigabit Ethernet RJ45 Port

- USB C Imaging and Connectivity Port

## Software Capabilities (Limelight OS)​

- Plug-and-Play high-performance vision. No experience required.

- Self-hosted browser-based UI for vision pipeline configuration

- REST/HTTP, Websocket, NetworkTables, ModbusTCP, and ROS support

- USB connectivity with plug-and-play USB-Ethernet Driver support on Windows, Linux, MacOS, and Android

- Drag-and-Drop 20FPS MobileNetSSD object detector neural network support

- Configurable Fixed exposure, sensor gain, resolution, and framerate.

- Configure 10 Hot-swappable Vision Pipelines:

- Custom Python Pipelines with OpenCV 4.10, numpy, etc.

- 2D, 3D AprilTag Tracking and Robot Localization

- Full 3D Localization (Robot GPS) with MegaTag1

- Higher-Accuracy Full 3D Localization (Robot GPS) with External IMU Fusion with MegaTag2

- Up to 50fps performance at 640x480 with detector Downscaling

- Full 3D Visualizer in web interface

- 120-240FPS Color Blob pipelines

- Neural Object Detection Pipelines

- Neural Image Classification Pipelines

- Barcode Tracking Pipelines

- Lens Focusing Pipeline

- Viewfinder pipeline for low-latency streaming

- Built-in Charuco Intrinsics Calibration interface for high-accuracy vision pipelines.

- Intrinsics Calibration visualization

- Built-in low-latency MJPEG Streaming. Configurable stream orientation

## 1. Mounting Limelight 3G​

#### Thru-Hole Mounting​

- Use 1 1/4" #10-32 or #10-24 screws with nylock nuts

- Alternatively, use 38mm M4 bolts with nylock nuts

- Use plastic washers to preserve anodization

#### Threaded Mounting (Backside)​

- 2x M3 threaded mounting points

- Consider light application of threadlocker (Vibratite or blue Loctite)

## 2. Wiring Limelight 3G​

#### Power​

- Run two 18-20AWG wires from your Limelight to a slot on your PDP/PDH

- Add a 5A breaker to the same slot

- Important: A dedicated VRM is strongly recommended for pre-2025 LL3G (white button) protection against load dumps due to swerve drive regenerative braking + battery disconnection events

- (Not Required) Use Weidmuller ferrules for optimal results (Pictured, 20AWG Wire with Weidmuller 20AWG Orange ferrules)

- Ferrules:

- https://www.digikey.com/en/products/detail/weidm%C3%BCller/0409500000/491834

- https://store.ctr-electronics.com/products/weidmuller-ferrule-pack-of-20?variant=43631135195309

- Low-cost Ferrule crimp tools:

- https://store.ctr-electronics.com/products/ferrule-crimper-by-iwiss?_pos=2&_sid=616edc4f4&_ss=r

- https://www.amazon.com/Ferrule-Crimping-Hexagonal-Ferrules-Connectors/dp/B09724DCJH?th=1

#### Ethernet​

- Run an ethernet cable from your Limelight to your robot radio

- Use twisted Cat6 cables with stranded wires (ideally 20AWG)

- Add a strain relief to your ethernet cable

#### USB Flashing​

- To enter flash mode, hold the configuration while plugging-in over USB C

- While flashing, it is safe to power over USB.

#### USB-Ethernet Interface​

- Limelight 3G has USB-Ethernet funcitonality that allows for plug-and-play connectivity with Windows, Linux, and MacOS. You can use the web interface and all other features over USB.

- Limelight 3G will generally fit within the power budget of most USB ports - you can safely use USB-Ethernet without external power.

- Limelight configuration UI on Windows (USB-Ethernet): http://172.28.0.1:5801

- Limelight configuration UI on Linux (USB-Ethernet): http://172.29.0.1:5801

## 3. Accessing the Web Interface​

After connecting your Limelight 3G to your network:

- Power up your robot and connect your laptop to your robot's network

- Use one of these methods to access the web interface:

- Method 1: Open the Limelight Hardware Manager application, scan for Limelights, and double-click on your Limelight when it appears

- Method 2: Open a web browser and navigate to http://limelight.local:5801

- Method 3: Open a web browser and navigate to your Limelight's static IP address with port 5801 (if configured)

- Method 4 (USB): Connect via USB-C and navigate to:

- Windows: http://172.28.0.1:5801

- Linux/Mac: http://172.29.0.1:5801

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

- Hold the config button while connecting a USB-C cable from your laptop to your Limelight

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

- Hold the config button on your Limelight

- While holding, run a USB-C cable from your laptop to your Limelight (your Limelight will power on automatically)

- After you've plugged your LL into your laptop, you can release the config button

- Your Limelight is now in flash mode, and its LEDs will not blink

- Run "Balena Etcher"

- It may take up to 20 seconds for your machine to recognize the camera

- Select the latest .zip image in your downloads folder

- Select a "Compute Module" device in the "Drives" menu

- Click "Flash"

- Once flashing is complete, remove the USB cable from your Limelight

Legacy Update Instructions (Windows) warning
Save your pipelines before updating LimelightOS. They will be deleted during the update.

- Power off your Limelight

- Download the latest USB drivers, Limelight OS image, and Balena Flash tool

- Hold the config button on your Limelight, and while holding, run a USB->USB-C cable from your laptop to your Limelight (your Limelight will power on automatically)

- Run "Balena Etcher" as administrator

- It may take up to 20 seconds for your machine to recognize the camera

- Select the latest .zip image in your downloads folder

- Select a "Compute Module" device in the "Drives" menu

- Click "Flash"

- Once flashing is complete, remove the USB cable from your Limelight

## 5. Focusing Your Limelight 3G​

- Plug your LL3G into your laptop over USB (make sure it is mounted to your robot or to a surface)

- Connect to the web interface as descirbed in section 3

- Click the "Ignore NT pipeline index" to enable pipeline switching, and switch to pipeline 9

- Set the pipeline type to "focus"

- Go to the configuration tab, and increase stream quality to maximum

- Make sure the camera is pointed at something with lots of features and contrast, such as an ARUCO board, a detailed scene, or a siemen's star

- Turn the lens to maximize the on-screen focus score

- Once focused, apply 3-8 dots of super glue or super glue gel around the lens

## 6. Network Configuration​

### Setting the Team Number (Required for FRC / Networktables)​

- Power up your robot and connect your laptop to your robot's network

- Open the Limelight Hardware Manager, scan for Limelights, and double click the entry that appears

- Alternatively, navigate to http://limelight.local:5801

- Go to the "Settings" tab

- Enter your team number and press "Update Team Number"

### Setting a Unique Hostname (Only Required for FRC / Networktables systems with multiple Limelights)​

- If you are using multiple Limelights, each Limelight must have a unique hostname

- In the settings tab, configure a hostname and click the "set hostname" button

### Setting Static IP (Recommended, not required)​

- Change "IP Assignment" to "Static"

- Set IP address to "10.TE.AM.11"

- Team 916 uses 10.9.16.xx

- Team 9106 uses 10.91.6.xx

- Team 9016 uses 10.90.16.xx

- Set Netmask to "255.255.255.0"

- Set Gateway to "10.TE.AM.1"

- Click "Update"

- Power-cycle your robot

- Access your config panel at 10.TE.AM.11:5801 and camera stream at 10.TE.AM.11:5800

- If you are using multiple Limelights, give each Limelight a unique static IP address

Q. Why do we recommend the use of a static IP address?A. It multiple seconds off Limelight's boot time.
Second, teams have historically had issues with DHCP assignment and
mDNS responders on actual FRC fields and with event radio firmware.
We recommend setting static IP addresses on your robo-rio and driverstation as well.
The networking settings to use on all of these devices can be found near the bottom half of
this web page

## 7. Troubleshooting​

### Status Light Indicators​

- Green Light: Blinks slowly (no targets), blinks quickly (targets detected)

- Yellow Light: Blinks (no static IP), solid (static IP assigned)

### If limelight.local:5801 doesn't work​

- Check if you have Bonjour installed (Windows: add/remove programs)

- Uninstall "bonjour print services" if you have two Bonjour items

- Install Bonjour from the Downloads page if missing

### Reset IP address​

- Hold the config button for 10 seconds after your Limelight has booted

- Networking configuration will reset to dynamic addressing on next boot

- Hardware Specifications
- Software Capabilities (Limelight OS)
- 1. Mounting Limelight 3G
- 2. Wiring Limelight 3G
- 3. Accessing the Web Interface
- 4. Updating LimelightOS
- 5. Focusing Your Limelight 3G
- 6. Network Configuration- Setting the Team Number (Required for FRC / Networktables)
- Setting a Unique Hostname (Only Required for FRC / Networktables systems with multiple Limelights)
- Setting Static IP (Recommended, not required)

- 7. Troubleshooting- Status Light Indicators
- If limelight.local:5801 doesn't work
- Reset IP address