> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-4 · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Limelight 4 Quick-Start | Limelight Documentation

 Skip to main content

 On this page

# Limelight 4 Quick-Start

## Hardware Specifications​

- Footprint: 3.154in x 1.894in (80.11mm x 48.11mm)

- Thickness: 1.160in (29.46mm)

- Mass: 0.3 lb

- #10 / M4 Thru-Hole Mounting

- M3 Threaded mounting holes

- Power Input: Buck-Boost with 5V-26V Operation (3.5V - 35V absolute maximum)

- Enhanced transient suppression for robotics applications

- 12W maximum power consumption

- Sensor: OV9281 Global Shutter Monochrome (1280x800 @ 120FPS, 640x400 @ 240FPS)

- IMX462 Back-Illuminated Upgrade Kit coming soon.

- Replaceable M12 Lens

- 82 deg Horizontal FOV, 56.2 deg Vertical FOV

- Black-Anodized, All-Aluminium Enclosure

- Gigabit Ethernet RJ45 Port (POE is no longer supported)

- Weidmuller Power Input Port

- USB C Imaging and Connectivity Port

- Internal IMU

- Hailo 8 AI Accelerator support with internal M.2 A+E Key Port.

## Software Capabilities (Limelight OS)​

- Plug-and-Play high-performance vision. No experience required.

- Self-hosted browser-based UI for vision pipeline configuration

- REST/HTTP, Websocket, NetworkTables, ModbusTCP, and ROS support

- USB connectivity with plug-and-play USB-Ethernet Driver support on Windows, Linux, MacOS, and Android

- Drag-and-Drop 20FPS MobileNetSSD object detector neural network support (CPU Inference)

- Drag-and-Drop 80FPS YoloV8 object detector neural network support (Requires Hailo-8)

- Configurable Fixed exposure, sensor gain, resolution, and framerate.

- Configure 10 Hot-swappable Vision Pipelines:

- Custom Python Pipelines with OpenCV 4.10, numpy, etc.

- 2D, 3D AprilTag Tracking and Robot Localization

- Full 3D Localization (Robot GPS) with MegaTag1

- Higher-Accuracy Full 3D Localization (Robot GPS) with External IMU Fusion with MegaTag2

- Internal IMU Fusion For higher-accuracy MegaTag2

- IMU Assist Modes to fuse internal IMU and External IMU or Camera-Based Yaw Estimate

- Up to 240FPS performance with detector Downscaling

- Full 3D Visualizer in web interface

- 120-240FPS Color Blob pipelines

- Neural Object Detection Pipelines

- Neural Image Classification Pipeliens

- Barcode Tracking Pipelines

- Lens Focusing Pipeline

- Viewfinder pipeline for low-latency streaming

- Built-in Charuco Intrinsics Calibration interface for high-accuracy vision pipelines.

- Intrinsics Calibration visualization

- Built-in low-latency MJPEG Streaming. Configurable stream orientation

Known Issues

- Hailo Accelerated Apriltag Framerates are too low when downscaling is enabled (To be addressed with a SW update)

- Temperature Readings from NetworkTables are not accurate while throttling is enabled (To be addressed with a SW update)

## 1. Mounting Limelight 4​

#### Thru-Hole Mounting​

- Use 1 1/4" #10-32 or #10-24 screws with nylock nuts

- Alternatively, use 38mm M4 bolts with nylock nuts

- Use plastic washers to preserve anodization

#### Threaded Mounting (Backside)​

- 2x M3 threaded mounting points

- Consider light application of threadlocker

## 2. Wiring Limelight 4​

#### Power​

- Run two 18-20AWG wires from your Limelight to a slot on your PDP, PDH, or Mini PDP

- Use a 5A or 10A breaker

- POE is no longer supported

- Note: Unlike previous models, LL4 can survive battery disconnect and regenerative braking events without requiring a dedicated VRM

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

- POE is no longer supported

#### USB Flashing​

- To enter flash mode, hold the configuration while plugging-in over USB C

- While flashing, it is safe to power Limelight 4 over USB.

#### USB-Ethernet Interface​

- Limelight 4 has USB-Ethernet funcitonality that allows for plug-and-play connectivity with Windows, Linux, and MacOS. You can use the web interface and all other features over USB.

- While using this interface, Limelight 4 will exceed the power rating of most USB ports. It is recommended to power Limelight 4 via the weidmuller port while using USB-Ethernet.

- Limelight 4 configuration UI on Windows (USB-Ethernet): http://172.28.0.1:5801

- Limelight 4 configuration UI on Linux (USB-Ethernet): http://172.29.0.1:5801

## 3. Accessing the Web Interface​

After connecting your Limelight 4 to your network:

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

- Download the latest USB drivers/RPIboot, Limelight OS image, and Balena Flash tool

- Hold the config button while connecting a USB-C cable from your laptop to your Limelight

- Run "rpiboot-CM4-CM5 - Mass Storage Gadget" from the Windows start menu

You should see the following if RPIBoot has successfully mounted your Limelight.

If you see anything else, remove the USB Cable, re-press the button, reinsert the usb cable, and restart the rpiboot utility.

- Run "Balena Etcher" as administrator

- Click "Flash From File" and select the latest .zip image

- Click "Select Target" and choose "mmcblk0 USB Device" in the "Drives" menu

- Click "Flash" and wait for completion

- Remove the USB cable after completion

## 5. Focusing Your Limelight 4​

- Power-on your robot.

- Connect to the web interface as described in section 3

- Click the "Ignore NT pipeline index" to enable pipeline switching, and switch to pipeline 9

- Set the pipeline type to "focus"

- Go to the configuration tab, and increase stream quality to maximum

- Make sure the camera is pointed at something with lots of features and contrast, such as an ARUCO board, a detailed scene, or a siemen's star

- Turn the lens to maximize the on-screen focus score

- Once focused, apply 3-8 dots of super glue or super glue gel around the lens

## 6. Network Configuration​

### Setting the Team Number (Required for FRC / Networktables)​

- Power up your robot and connect your laptop to your robot's network

- Open the Limelight Hardware Manager, scan for Limelights, and double click the entry that appears.

- Alternatively, navigate to http://limelight.local:5801

- Go to the "Settings" tab

- Enter your team number and press "Update Team Number"

### Setting a Unique Hostname (Only Required for FRC / Networktables systems with multiple Limelights)​

- If you are using multiple Limelights, each Limelight must have a unique hostname

- In the settings tab, configura a hostname and click the "set hostname" button.

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

- If you are using multiple Limelights, give each Limelight a unique static IP address. Gateways and netmasks should be the same across Limelights.

Q. Why do we recommend the use of a static IP address?A. It multiple seconds off Limelight’s boot time.
Second, teams have historically had issues with DHCP assignment and
mDNS responders on actual FRC fields and with event radio firmware.
We recommend setting static IP addresses on your robo-rio and driverstation as well.
The networking settings to use on all of these devices can be found near the bottom half of
this web page

## 7. Limelight 4 Thermal Management​

Limelight 4's thermal output can be reduced by setting the Throttle parameter to 100-200 while disabled, and to 0 while enabled.
Alternatively, you can switch to a viewfinder pipeline while disabled.

## 8. Hailo AI Accelerator Module Installation (Optional)​

If you have the optional Hailo AI accelerator module, follow these steps to install it:

- Attach the included thermal pad to the Hailo SOC (System on Chip)

- Use the included 1.5mm Allen wrench to remove the three 8mm M2 enclosure screws

- Set these screws aside (they have threadlocking material)

- Carefully open the enclosure (note: the camera cable will limit how far you can open it)

- Insert the Hailo module into the appropriate slot

- No screws are required to secure the Hailo module

- Reattach the enclosure using the original three 8mm M2 screws

- After installing the Hailo module, make sure to update to the latest version of LimelightOS.

 warning
The Hailo Accelerator Module is inoperable with USB power. It requires a stable 12V power source, like the main robot battery, for proper function.

## 8. Troubleshooting​

### Status Bar Indicators​

- Slow Cylon (Scanning): No targets detected by the current pipeline

- Fast Cylon (Scanning): Targets detected by the current pipeline

- Slow Alternating LED Blink: Hardware error (camera cable disconnected, sensor damage, etc.)

### If limelight.local:5801 doesn't work​

- Check if you have Bonjour installed (Windows: add/remove programs)

- Uninstall "bonjour print services" if you have two Bonjour items

- Install Bonjour from the Downloads page if missing

### Reset IP address​

- Hold the config button for 10 seconds after your Limelight has booted

- Networking configuration will reset to dynamic addressing on next boot

- Hardware Specifications
- Software Capabilities (Limelight OS)
- 1. Mounting Limelight 4
- 2. Wiring Limelight 4
- 3. Accessing the Web Interface
- 4. Updating LimelightOS
- 5. Focusing Your Limelight 4
- 6. Network Configuration- Setting the Team Number (Required for FRC / Networktables)
- Setting a Unique Hostname (Only Required for FRC / Networktables systems with multiple Limelights)
- Setting Static IP (Recommended, not required)

- 7. Limelight 4 Thermal Management
- 8. Hailo AI Accelerator Module Installation (Optional)
- 8. Troubleshooting- Status Bar Indicators
- If limelight.local:5801 doesn't work
- Reset IP address