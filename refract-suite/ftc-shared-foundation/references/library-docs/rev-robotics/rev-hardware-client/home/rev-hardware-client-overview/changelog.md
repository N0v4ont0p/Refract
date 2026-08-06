> Source: https://docs.revrobotics.com/rev-hardware-client/home/rev-hardware-client-overview/changelog.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/home/rev-hardware-client-overview/changelog.md).

# Changelog

### Version 1.7.6 <a href="#version-173" id="version-173"></a>

* Add banner about RHC2

### Version 1.7.5 <a href="#version-173" id="version-173"></a>

* rerelease of 1.7.4 with correct binaries

### Version 1.7.4 <a href="#version-173" id="version-173"></a>

* Correct label for voltage ramp rate
* Fix overflow scrolling for some views that

### Version 1.7.3 <a href="#version-173" id="version-173"></a>

* Display warning on Servo Hub device page when Servo Hub is in rs-485 mode.

### Version 1.7.2

* Add dropdown for configuring port disabled behavior to Servo Hub hardware page

### Version  1.7.1

#### General improvements <a href="#general-improvements" id="general-improvements"></a>

* Fixes viewing and installing software when offline
* Improves the reliability of loading data from CAN devices
* Adds a "Forget REV USB Devices" button to the "Don't see your device?" page
  * This button will prompt for administrator privileges, tell Windows to forget REV USB devices, and restart the REV Hardware Client
  * You will have to disconnect and reconnect all REV USB devices for them to show up again
  * This may not affect all types of REV USB devices, such as Control Hubs and Driver Hubs.

#### SPARK improvements <a href="#spark-improvements" id="spark-improvements"></a>

* Fixes persisting parameters on SPARK motor controllers in follower mode

### Version 1.7.0

#### Breaking Changes

* The standard REV Hardware Client installer no longer bundles device software files that are under 5MB
  * If you need an installer that has device software bundled into it, download one of the offline installers linked at [https://docs.revrobotics.com/rev-hardware-client](/rev-hardware-client/home/rev-hardware-client-overview.md)
* Once a REV Hardware Client instance starts controlling a SPARK motor controller, no other REV Hardware Client instance connected to the same bus can control a SPARK motor controller until the first instance exits
* The "Follow SPARK Using Preset" feature has been removed, in favor of simpler follower mode parameters in SPARK firmware version 25 and later
* The "Burn Flash" button for SPARK motor controllers has been renamed to "Persist Parameters" to match the 2025 version of REVLib
* The SPARK parameter `kSensorType` is no longer automatically-updated when the `kMotorType` parameter is changed
  * This only impacts SPARK firmware versions prior to 25.0.0, as the `kSensorType` parameter has been removed from later versions
* The MAXSwerve Utility now requires SPARK firmware version 25.0.0 or later

#### General Improvements

* Fixes issue where the installer could cause the computer to reboot unexpectedly
* Improves the reliability of displaying and using devices on a high-traffic CAN bus
* Fixes a performance regression in the 2025 beta release that affected CAN communication
* Stops the Telemetry tab from breaking after a device that was providing data is removed
* Fixes issue where Android devices that have a type other than "device" or "recovery" would cause device scans to take a long time and not include any Android devices or Expansion Hubs
* Only allows one instance of the REV Hardware Client to be open at a time
* Fixes an issue where Pneumatic Hubs and Power Distribution Hubs would be disabled when a SPARK motor controller is commanded to run

#### Servo Hub

* Adds support for updating, configuring, and actuating servos on Servo Hub

#### SPARK Improvements

* Adds support for SPARK firmware version 25
* Improves UI for configuring closed-loop parameters (including MAXMotion parameters) on the Run and Telemetry tabs
* Fixes issue updating SPARKs over the CAN bus
* Improves organization of parameters on the Advanced Tab
* Improves organization of faults and warnings on the Basic Tab
  * Some faults were renamed or combined
  * The statuses of the soft and hard limits are now displayed above the faults and warnings
* Exposes individual faults on the Telemetry tab
* Improves organization of SPARK signals on the Telemetry tab
* Many under-the-hood improvements

### Version 1.6.5 / 1.6.6

Version 1.6.6 was released shortly after version 1.6.5 to fix a regression where the Telemetry graph would disappear if you switched away from the Telemetry tab while the graph was running

#### Breaking changes

* Windows 10 or later is now required

#### General improvements

* Listens for safety keys (space and enter) even when not focused
  * If the FRC Driver Station or another application with administrative privileges is focused, the REV Hardware Client will not see the keypress
* Improves the Telemetry feature
  * Fixes tooltips
  * Fixes various chart interactions
  * Improves the visibility of data when more than 4 signals are active or a signal is being hovered over
  * Fixes the background color of image exports
  * Fixes an unhandled exception when resizing the window with the Telemetry tab open on a scaled display
* Improves the reliability of displaying devices
* Fixes an issue where all devices would be cleared out after an unexpected error occurred
* Various small improvements to safety and the user experience

#### SPARK improvements

* Allows typing incomplete numbers into the setpoint text field
* Dramatically improves behavior of the setpoint slider
* Always disables the setpoint controls and displays a tooltip when the motor cannot be run
* Improves the reliability of updating SPARK MAXes with firmware older than version 1.5.0
* Displays the input voltage
* Renames the "Gate Driver Fault" to "Gate Driver Fault or 12V Missing"

#### Pneumatic Hub improvements

* Turns off all solenoids when a safety key (Space or Enter) is pressed

#### Expansion Hub improvements

* Fixes installing firmware onto directly-connected Expansion Hubs<br>

### Version 1.6.4

#### General improvements

* Fixes an error message appearing when the selected device is unplugged
* Improves the reliability of device scans and removals
  * Includes changes to prevent duplicate devices from being displayed
* Improves reliability of detecting new USB CAN devices
* Adds support for public Software Channels

#### SPARK improvements

* Fixes issue where devices could run unexpectedly under certain situations
* Fixes issue where the REV Hardware Client could fail to receive data from a directly-connected SPARK after updating it
* Fixes issue where the REV Hardware Client would require the CAN bus to be error-free even when you were updating via USB
* Disables the Run Motor button when the SPARK is under roboRIO control

### Version 1.6.3

#### Improvements

* Fixes issue where SPARK firmware update retries over CAN fail to succeed
* Fixes SPARK Flexes disappearing immediately after a firmware update over CAN
* Fixes issue where Recovery Mode devices and SPARKs connected directly via USB fail to update when there is more than one such device.

### Version 1.6.2

#### Improvements

* Prevents SPARK Flexes from being configured in Brushed mode when not connected to a SPARK Flex Dock or when their firmware version does not support the SPARK Flex Dock.
* Makes adjustments for SPARK motor controller firmware version 24.0.0
* Improves reported NEO Vortex position accuracy when used with a SPARK Flex running firmware version 24.0.0 or later

### Version 1.6.1

#### Bug fixes <a href="#bug-fixes" id="bug-fixes"></a>

* Fixes a crash on startup under certain circumstances

### Version 1.6.0

#### New features

* Adds support for the SPARK Flex motor controller

#### Improvements

* Reduces the amount of data that needs to be downloaded for updates to the REV Hardware Client
* Starts respecting the operating system proxy and certificate settings (improves compatibility with school and corporate networks)
* Improves the warning displayed when the current FTC Robot Controller app was built using Android Studio
  * This warning is now always shown as a pop-up that must be confirmed if you try to replace the app.

#### Bug fixes

* Fixes the bundled software not being copied correctly if the REV Hardware Client was being installed for the first time&#x20;
* Fixes various issues related to canceling software downloads
* Fixes loading certain SPARK MAX configurations
* Increases default increment on SPARK MAX/Flex PIDF screen
* Fixes FTC log viewer pan/zoom buttons not working until after pan/zoom with mouse
* Fixes issue where uploading log files for REV support would sometimes fail

### Version 1.5.3

#### New features

* Includes all software less than 1MB in size in the REV Hardware Client installer
* Adds alternative installers for offline use that bundle all available software, or all software that applies to just FTC or just FRC

#### Enhancements

* Makes it so that downloading software and checking for updates now apply to all users on a computer
* Improves performance when checking for updates with large software updates downloaded
* Improves SPARK MAX fault names

#### Bug fixes

* Fixes issue where SPARK MAX limit switch polarities would be displayed incorrectly
* Fixes issue where selecting a DFU device's type would not work
* Fixes issue where non-CAN devices would not disappear when unplugged
* Fixes issue where the recovery device type selection menu was not working
* Improves error message when checking for REV Hardware Client updates while offline

### Version 1.5.2

#### SPARK MAX Improvements

* Fixes safety issue when stopping a motor that was running in Position or Smart Motion mode
* Fixes issue where the motor direction applied via the Run tab would be incorrect for an inverted SPARK MAX, making it appear that the inverted mode was broken&#x20;
* Fixes error when changing SPARK MAX parameters on the Advanced tab under certain conditions&#x20;
* Fixes issue where a SPARK MAX connected via USB would not disappear after being unplugged after a firmware update

#### MAXSwerve Drive Utility Improvements

* Sorts MAXSwerve drive configurations by when they were last accessed&#x20;
* Adds button for each selected SPARK MAX that makes the device blink momentarily&#x20;
* Makes SPARK MAXes blink momentarily when they are assigned a role in a MAXSwerve drive&#x20;
* Makes the turning SPARK MAX blink momentarily when a MAXSwerve module's calibration tool is opened&#x20;
* Fixes issue where the list of CAN IDs selectable in the MAXSwerve Drive Utility wouldn't be updated after changing a SPARK MAX's CAN ID

**Improves the experience of updating to future REV Hardware Client versions**

* It is now safe to navigate away from the About tab while the update is downloading

### Version 1.5.1

* Adds new MAXSwerve Drive Utility to the top-level Utilities tab
  * Current version is a beta, additional features are planned
  * Displays position of each MAXSwerve module's wheel
  * Allows all modules to be easily calibrated in one place
  * Detects configuration issues with the SPARK MAXes being used for MAXSwerve
  * Supports exporting and importing MAXSwerve drive configurations, so that the utility can be used on multiple computers without having to re-select the options
* Fixes infinite spinner after restoring SPARK MAX factory defaults
* Increases the number of decimal places shown for the zero offset on the \`AbsoluteEncoder\` tab, making the result suitable for pasting into your robot program
* After the Absolute Encoder zero offset has been set, the icon that indicates that a parameter has been modified and needs to be burned to flash is now displayed

### Version 1.5.0

**General Improvements**

* Upgrades Chart.js to improve performance and appearance of the charts
* Makes minor UI improvements

**SPARK MAX Improvements**

* Adds support for duty cycle absolute encoders, including a new `AbsoluteEncoder` tab
* Adds MAXSwerve getting started and module calibration guides to the `AbsoluteEncoder` tab
* Adds support for configuring position PID wrapping
* Adds support for configuring hall sensor velocity calculation
* Updates SPARK MAX kFeedbackSensorPID0 to use a dropdown instead of numeric values for clearer selection of types of sensors
* Fixes issue where a SPARK MAX could not be configured to follow another SPARK MAX with an ID higher than 15
* Allows running SPARK MAXes connected via the CAN bus without having to also run the SPARK MAX connected directly via USB

**Pneumatic Hub Improvements**

* Exposes additional telemetry values from the Pneumatic Hub

**Control Hub and Expansion Hub Improvements**

* Fixes issue where updating Control/Expansion Hub firmware through a Control Hub more than once would fail

### Version 1.4.3

* Fixes reported solenoid current values from Pneumatic Hubs
* Adds detailed hardware fault reporting for Pneumatic Hubs and Power Distribution Hubs
* Fixes issue where entries in exported CSV files were in the incorrect order (newest to oldest)
* Prevents the "Report an Issue" form from being dismissed accidentally

### Version 1.4.2

* Fixes updating SPARK MAXes over the CAN bus
* Adds support for restoring Driver Hubs that get stuck on the REV logo
* Adds support for TensorFlow Lite models, sounds, and external libraries to the Control Hub backup feature
* Updates bundled version of ADB

### Version 1.4.1

* Fixed setting the CAN ID of a SPARK MAX

### Version 1.4.0

* Adds support for the Power Distribution Hub and the Pneumatic Hub
* Renames "Hub Firmware" to "Expansion/Control Hub Firmware"
* Renames "Fatal" log event type to "Assert" in the FTC Log Viewer
  * Hides Assert events by default
* Allows longer filenames in the FTC log file selector
* Fixes various bugs

### Version 1.3.0

**General Improvements**

* Adds FTC log viewer utility
  * Can load log files directly from supported devices, or from anywhere on the user's computer
  * Allows users to easily filter, search, and sort events parsed from log files
  * Graphs the occurrence of important robot issues, and their corresponding timestamps
  * Supports match, robot controller, driver station, Wi-Fi, and updater logs
* Shows release notes for client even when an update is not available
* Scales telemetry graph ranges automatically when using default ranges
* Fixes issue with devices showing up multiple times when changing CAN IDs
* Shows update progress for all devices that are updating simultaneously
* Updates users to the latest available client version when removing a software channel
* Other minor bug fixes

**Control Hub Improvements**

* Improves stability of the connection to a Control Hub
* Includes program and manage logs with Control Hub diagnostic data sent to REV

**SPARK MAX Improvements**

* Fixes issue with SPARK MAX analog telemetry
* Improves SPARK MAX parameter fields
* Fixes issue where a SPARK MAX in recovery mode could not be updated on some computers
* Adds interface to run multiple SPARK MAX devices
* Adds simplified support for configuring follower mode (currently limited to following another SPARK MAX)
* Shows a dropdown for the `Alternate Encoder -> kDataPortConfig` parameter

### Version 1.2.0

**General Improvements**

* Allow installing previous versions of software
* Show client updates are available more subtly&#x20;
* Reconnect to ADB if it resets&#x20;
* Show manufacturer names for generic android devices
* Fixes issues with Control Hub and Expansion Hub firmware falsely saying out of date
* Other minor bug fixes

**Control Hub Improvements**

* Shows warning when the Control Hub internal communication is not responding
* Shows warning when Control Hub webserver is not running
* Full screen mode for Program and Manage Tab
* Prompts to backup Control Hub data if backup on file is over a week old
* Confirmation now required to restore backed up files
* Fix issues with not all files being restored

**SPARK MAX Improvements**

* Fixed bug where Alternate Encoder telemetry data was displaying incorrectly
* Allow for complete Factory Reset of all parameters on SPARK MAX
* Disabled setting of parameters that have no effect in current configuration
* Fixed bug where the Client would turn white on selecting SPARK MAX

### Version 1.1.0

* Adds support for SPARK MAX and other CAN devices&#x20;
* Allows for updating SPARK MAX devices, installing APIs, running motors, and viewing data from the SPARK MAX and its motor.&#x20;
* Shows all recognized devices on a CAN bus, and the data that is sent on the bus

### Version 1.0.0

* Original Release
