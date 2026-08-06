> Source: https://docs.revrobotics.com/duo-control/legacy/rev-hub-interface-software.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/legacy/rev-hub-interface-software.md).

# REV Hub Interface Software

The REV Hub Interface is a beta software allowing for a direct connection from a REV Expansion Hub and its peripherals to a Windows PC.&#x20;

This interface provides a method for teams to prototype with motors, servos, and sensors in a way that is faster and easier than setting up an entire robot control system. It is also a valuable troubleshooting tool that can help isolate the cause of an issue and determine if it is electrical or software related. The REV Hub Firmware can also be updated and recovered through this interface in addition to the Robot Controller Application.

#### [Download the Latest Hub Interface Software - Version 1.2.0](https://www.revrobotics.com/content/sw/REVHubInterface-1.2.0.exe)

{% hint style="warning" %}
The REV Hub Interface Software only works with the REV Expansion Hub and not the REV Control Hub
{% endhint %}

### System Requirements

* Operating System: Windows 7 or newer\*
* Processor: 64-bit
* RAM: Yes

{% hint style="info" %}
&#x20;The newest versions of Windows should automatically install the required USB drivers. Alternatively, you can download the latest drivers from the [FTDI VCP website](https://www.ftdichip.com/Drivers/VCP.htm).
{% endhint %}

### Installation Instructions

1. Download the Hub Interface software installer above.
2. Run the installer.
3. Run the REV Hub Interface Software from the Windows Start Menu or the desktop shortcut

### Connecting and Controlling an Expansion Hub

1. Connect your Expansion Hub to the computer with a USB A to USB Mini-B cable.
2. Run the REV Hub Interface Software.
3. The software will scan and connect to the Expansion Hub. The various peripheral tabs will populate with controls once connected.

{% hint style="warning" %}
Some peripherals, such as DC Motors and Servo Motors, require a battery to be connected to the Expansion Hub in order to operate through the REV Hub Interface.
{% endhint %}

### Alternative Installation Method

You may also download the following zip file if you would rather unzip the application in a directory of your choice. This method shouldn't require administrator privileges.&#x20;

[REV Hub Interface Software Zip File](https://www.revrobotics.com/content/sw/REVHubInterface-1.2.0.zip)

#### LATEST HUB INTERFACE SOFTWARE CHANGE LOG - VERSION 1.2.0

* Display encoder values on 'DC motors' tab.
* Added support for REV Color Sensor V3.
* Display proximity values along with RGBC for REV color sensors.
* Display REV Hub Interface version on the 'Firmware' tab.
* Changed behavior of 'INIT' and 'POLL' buttons on 'I2C'. User can no longer poll a device until it has been successfully initialized.
* Added ability to set LED pattern.
* Bug fix where 'POLL' had to be pressed twice to read values from the IMU.
* Bug fix where status LED would continue to flash blue the second time REV Hub Interface is connected.
* Allow user to press enter key to update motor/servo values.
* Fixed gyro labels on IMU tab and corrected units for linear acceleration.
