> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system/operating-system-changelog.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system/operating-system-changelog.md).

# Control Hub Operating System Changelog

{% hint style="warning" %}
When updating from OS 1.1.1 or earlier to OS 1.1.2 or later, the Control Hub will switch to the 5 GHz band, regardless of the previous Wi-Fi band setting. Some devices do not support 5 GHz Wi-Fi, and will not be able to connect to the Control Hub wirelessly while it is using the 5 GHz Wi-Fi band. To switch to the 2.4 GHz band without needing a computer, see the [Changing Wi-Fi Band section](/duo-control/managing-the-control-system/ch-wifi.md#changing-wi-fi-band).
{% endhint %}

### Version 1.1.6 - Latest Version

* Important security updates for the Control Hub Wi-Fi driver

<p align="center"><a href="https://github.com/REVrobotics/REV-Software-Binaries/releases/download/chos-1.1.6/controlHubOS-1.1.6.zip" class="button primary" data-icon="download">Download Control Hub OS Version 1.1.6</a></p>

### Version 1.1.4

* Reduces the frequency of an issue that could cause the BHI260AP IMU to reset after an ESD event

<p align="center"><a href="https://github.com/REVrobotics/REV-Software-Binaries/releases/download/chos-1.1.4/ControlHubOS-1.1.4.zip" class="button primary" data-icon="download">Download Content Hub OS Version 1.1.4</a></p>

### Version 1.1.3

* Adds support for new alternative built-in BHI260AP IMU on Control Hub
* Improves reliability of the Wi-Fi access point monitoring feature

<p align="center"><a href="https://github.com/REVrobotics/REV-Software-Binaries/releases/download/chos-1.1.3/ControlHubOS-1.1.3.zip" class="button primary" data-icon="download">Download Control Hub OS Version 1.1.3</a></p>

### **Version 1.1.2**

* Adds support for Auto Channel Selection, where the Control Hub will pick the least busy Wi-Fi channel on the selected Wi-Fi band when it starts up &#x20;
* Migrates all users to Auto Channel Selection on the 5 GHz band by default.
  * If you find that you are unable to connect to the Control Hub after updating, you should perform a Wi-Fi Factory Reset by holding down the Control Hub's button as it boots, until you see a colorful light sequence. That will reset the Wi-Fi settings and switch to the 2.4 GHz Wi-Fi band.
* Allows switching the Wi-Fi band between 2.4 GHz and 5 GHz by holding down the Control Hub's button when the hub has been booted for at least 20 seconds
  * If version 5.5 or later of the Robot Controller app is installed, the Control Hub's light will blink magenta when the band is switched to 5 GHz, or yellow when the band is switched to 2.4 GHz.
* Continuously monitors the Wi-Fi access point status, and will attempt to restart it if it goes down for any reason
* Continuously monitors the Robot Controller app, and restarts it if it crashes or hangs (requires version 6.1 or later of the Robot Controller app)
* Allows the Robot Controller app to access the current Wi-Fi band and channel
* Always backs up the FTC Robot Controller app data before it is uninstalled, in order to preserve Wi-Fi settings
* Improves Wi-Fi reliability
* Prevents issue that could cause device to boot into recovery mode
* Enables use of mouse button in recovery mode

<p align="center"><a href="https://github.com/REVrobotics/REV-Software-Binaries/releases/download/ch-os-1.1.2/ControlHubOS-1.1.2.zip" class="button primary" data-icon="download">nload Control Hub OS Version 1.1.2</a></p>

### **Version 1.1.1**

* Fixed bug where Wi-Fi access point would sometimes fail to start after an Operating System update
* Stopped the FtcAccessPointService UI auto-starting on boot
* Allowed Wi-Fi beacon rate to be changed by the FTC Robot Controller app

### **Version 1.1.0**

* Improved reliability of making changes to Wi-Fi access point settings
* Updated to latest Realtek Wi-Fi driver
* Increased Wi-Fi beacon rate to 6mbps, which reduces congestion when many Control Hubs are being used in an area
* Enabled 802.11w, which prevents Wi-Fi deauthentication attacks when the Control Hub is used with a client device that also supports 802.11w
* Added WifiLog.txt file for debugging and disconnection analysis
* Improved reliability of FtcAccessPointService UI (accessed through an HDMI monitor)
* Added 5 GHz channels to FtcAccessPointService UI
* Ensured app data is not lost when installing a Robot Controller with a different signature via the Manage webpage
* Fixed issue where Wi-Fi SSID would sometimes be AndroidAP

### **Source Files for Control Hub OS:**

* [Linux Kernel Source](https://github.com/REVrobotics/kernel-controlhub-android)
* [U-Boot Source](https://github.com/REVrobotics/uboot-controlhub-android)
