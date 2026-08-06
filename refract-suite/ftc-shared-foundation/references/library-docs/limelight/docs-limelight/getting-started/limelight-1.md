> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-1 · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Limelight 1 Quick-Start | Limelight Documentation

 Skip to main content

 On this page

# Limelight 1 Quick-Start

## Hardware Specifications​

- Footprint: 3.764in x 3.764in (95.67mm x 95.67mm)

- Thickness: 0.878in (22.30mm)

- #10 / M4 Thru-Hole Mounting

- Power Input: 4.1V-16V

- 10W maximum power consumption

- LED Illumination: 400 lumens, green illumination

- Sensor: OV5647 Color Rolling Shutter (320x240 @ 90FPS)

- Replaceable M12 Lens

- Black Impact-Resistant Polycarbonate Enclosure

- 10/100 Ethernet RJ45 Port

- RS-232 Serial (3.3V)

- USB-A Host Port (USB 2.0)

- Status Lights: Green (target detection), Yellow (network status)

- Google Coral USB Neural Network Accelerator Support

## Software Capabilities (Limelight OS)​

- Plug-and-Play high-performance vision. No experience required.

- Self-hosted browser-based UI for vision pipeline configuration

- REST/HTTP, Websocket, NetworkTables, ModbusTCP, and ROS support

- Configurable Fixed exposure, sensor gain, resolution, and framerate.

- Configure 10 Hot-swappable Vision Pipelines:

- Custom Python Pipelines with OpenCV 4.10, numpy, etc.

- 2D, 3D AprilTag Tracking and Robot Localization

- Full 3D Localization (Robot GPS) with MegaTag1

- Higher-Accuracy Full 3D Localization (Robot GPS) with External IMU Fusion with MegaTag2

- Full 3D Visualizer in web interface

- 90FPS Color Blob pipelines

- Neural Object Detection Pipelines

- Neural Image Classification Pipelines

- Barcode Tracking Pipelines

- Viewfinder pipeline for low-latency streaming

- Built-in low-latency MJPEG Streaming. Configurable stream orientation

## 1. Mounting Limelight 1​

#### Thru-Hole Mounting​

- Use 1 1/4" #10-32 or #10-24 screws with nylock nuts

- Alternatively, use 38mm M4 bolts with nylock nuts

- Use plastic washers to preserve the enclosure finish

## 2. Wiring Limelight 1​

#### Power​

- Run two 18-20AWG wires from your Limelight to a slot on your PDP/PDH

- Add a 5A breaker to the same slot

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

## 3. Accessing the Web Interface​

After connecting your Limelight 1 to your network:

- Power up your robot and connect your laptop to your robot's network

- Use one of these methods to access the web interface:

- Method 1: Open the Limelight Hardware Manager application, scan for Limelights, and double-click on your Limelight when it appears

- Method 2: Open a web browser and navigate to http://limelight.local:5801

- Method 3: Open a web browser and navigate to your Limelight's static IP address with port 5801 (if configured)

Once connected, you'll have access to:

- Settings tab - Configure team number, hostname, and other system settings

- Vision Pipeline tabs - Set up and tune your vision processing pipelines

- Camera & Crosshair tab - Adjust camera settings and crosshair parameters

All configuration is done through this web interface. Changes are saved automatically to your Limelight.

## 4. Updating LimelightOS​

 caution
Some versions of Limelight 1 are electrostatically sensitive around the micro-USB port. To prevent damaging the port, ground yourself to something metal before you connect to the micro-USB port. This will ensure your personal static charge has been discharged.

 caution
Backup your pipelines and scripts before upgrading - they will be erased during this process!

- Power off your Limelight

- Download the latest Limelight Hardware Manager and Limelight OS image

- Run a USB->MicroUSB cable from your laptop to your Limelight

- Turn on your Limelight

- Open Limelight Hardware Manager

- Navigate to the "Flash OS" tab

- Select the OS image file and wait for extraction to complete

- Click "Refresh Device List"

- Select your Limelight device from the list

- Click "Flash Device" and wait for completion

- Remove power from your Limelight after completion

 info
Only connect the micro-USB cable while imaging. Limelight enters a special flash mode while the microUSB cable is connected. You will not be able to access the web interface while Limelight is in flash mode.

Legacy Update Instructions (macOS & Linux) warning
Save your pipelines before updating LimelightOS. They will be deleted during the update.

- Download the Limelight OS image and Balena Flash tool from the Downloads Page

- Build the USB Boot driver yourself:

brew install libusb
brew install pkg-config
git clone --recurse-submodules --shallow-submodules --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot
make
sudo ./rpiboot
# As long as rpiboot is running, your camera will properly enumerate on macOS and Linux
# You need to run rpiboot every time you want to flash.

- Run a USB->MicroUSB cable from your laptop to your Limelight

- Turn on your Limelight

- Your Limelight is now in flash mode, and its LEDs will not blink

- Run "Balena Etcher"

- It may take up to 20 seconds for your machine to recognize the camera

- Select the latest .zip image in your downloads folder

- Select a "Compute Module" device in the "Drives" menu

- Click "Flash"

- Once flashing is complete, remove power from your Limelight

 info
Only connect the micro-USB cable while imaging. Limelight enters a special flash mode while the microUSB cable is connected. You will not be able to access the web interface while Limelight is in flash mode.

Legacy Update Instructions (Windows) warning
Save your pipelines before updating LimelightOS. They will be deleted during the update.

- Power off your Limelight

- Download the latest USB drivers, Limelight OS image, and Balena Flash tool

- Run a USB->MicroUSB cable from your laptop to your Limelight

- Turn on your Limelight

- Run "Balena Etcher" as administrator

- It may take up to 20 seconds for your machine to recognize the camera

- Select the latest .zip image in your downloads folder

- Select a "Compute Module" device in the "Drives" menu

- Click "Flash"

- Once flashing is complete, remove power from your Limelight

 info
Only connect the micro-USB cable while imaging. Limelight enters a special flash mode while the microUSB cable is connected. You will not be able to access the web interface while Limelight is in flash mode.

## 5. Network Configuration​

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

## 6. Controlling the LEDs​

Limelight 1 includes built-in green illumination LEDs. These LEDs can be controlled in several ways:

### Via Web Interface​

- Navigate to the Camera & Crosshair tab in the web interface

- Use the LED Mode dropdown to select:

- On - Always on

- Off - Always off

- Blink - Blink the LEDs

- Pipeline - LEDs turn on when a target is detected

### Via NetworkTables or API​

- Set the "ledMode" value:

- 0: Pipeline default

- 1: Force off

- 2: Force blink

- 3: Force on

## 7. Troubleshooting​

### Status Light Indicators​

- Green Light: Blinks slowly (no targets), blinks quickly (targets detected)

- Yellow Light: Blinks (no static IP), solid (static IP assigned)

### LED Diagnostic Patterns​

- Left/Right or Top/Bottom alternating blink: The internal camera cable has become unseated or the image sensor is damaged

- Fast Blink (all LEDs): The networking reset button has been held for at least 10 seconds

- Repeated Startup Sequence: The software is crashing, possibly due to hardware damage

### If limelight.local:5801 doesn't work​

- Check if you have Bonjour installed (Windows: add/remove programs)

- Uninstall "bonjour print services" if you have two Bonjour items

- Install Bonjour from the Downloads page if missing

### Reset IP address​

- Hold the config button for 10 seconds after your Limelight has booted

- Networking configuration will reset to dynamic addressing on next boot

- Hardware Specifications
- Software Capabilities (Limelight OS)
- 1. Mounting Limelight 1
- 2. Wiring Limelight 1
- 3. Accessing the Web Interface
- 4. Updating LimelightOS
- 5. Network Configuration- Setting the Team Number (Required for FRC / Networktables)
- Setting a Unique Hostname (Only Required for FRC / Networktables systems with multiple Limelights)
- Setting Static IP (Recommended, not required)

- 6. Controlling the LEDs- Via Web Interface
- Via NetworkTables or API

- 7. Troubleshooting- Status Light Indicators
- LED Diagnostic Patterns
- If limelight.local:5801 doesn't work
- Reset IP address