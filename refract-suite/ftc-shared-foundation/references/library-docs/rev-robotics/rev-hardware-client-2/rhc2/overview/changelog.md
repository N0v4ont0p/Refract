> Source: https://docs.revrobotics.com/rev-hardware-client-2/rhc2/overview/changelog.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client-2/rhc2/overview/changelog.md).

# Changelog

{% hint style="warning" %}
For the most up-to-date changelog, please reference the [About Tab](/rev-hardware-client-2/rhc2/navigation.md#about-tab) within the REV Hardware Client 2
{% endhint %}

### Version 1.0.7

* Adds support for configuring new MAXSpline Encoder parameters
* Fixes start/stop button moving when running a SPARK

### Version 1.0.6

* Fixes motors not stopping immediately when running multiple motors simultaneously
* Fixes a bug causing devices to appear as remaining in bootloader mode after updating

### Version 1.0.5

* Adds button to install DFU drivers on Windows
* Adds warning when trying to run a motor without 12V
* Adds ability to reset SPARK slider to zero by double-clicking on slider handle
* Fixes splash screen not appearing in the foreground
* Fixes taskbar icon not appearing immediately on Windows
* Fixes SPARK slider setpoint resetting to zero after interacting with the minimum and maximum setpoint input boxes
* Fixes detecting MAXSpline Encoders in bootloader mode
* Fixes device drawer not defaulting to update page for devices in bootloader mode
* Fixes firmware version select taking a long time to load for devices in bootloader mode

### Version 1.0.4

* Adds warning about SPARK devices with an unconfigured CAN ID
* Adds button to clear telemetry signals
* Adds dialog to move the application into the Applications folder on macOS for improved experience:
  * Fixes devices in recovery mode not appearing on macOS
  * Fixes application not updating after clicking the Update button on macOS
* Adds AdvantageScope logo
* Fixes AdvantageScope sometimes not loading layout correctly on startup or when loaded from a file
* Fixes AdvantageScope not resuming when computer wakes from sleep
* Fixes regression preventing telemetry to resume when reconnecting a device

### Version 1.0.3

* Adds warning when trying to run a motor with the roboRIO present on the bus
* Adds error toast for when a SPARK parameter value is rejected
* Adds help dialog when loading devices takes a long time, especially for brand new SPARK MAXes on unsupported factory firmware
* Adds privacy policy
* Improves CAN utilization when running multiple devices on telemetry page
* Prevents multiple instances of the app from running at once
* Fixes bug causing SPARKs in brushed mode to get set to brushless upon connection
* Fixes issue with parameters not refreshing when switching devices on telemetry run tab
* Fixes spike in CAN utilization when opening a SPARK device by switching to lazy loading parameters
* Fixes issue with SPARK run slider sometimes continuing to drag with mouse after releasing
* Fixes device list sometimes not updating when unplugging USB
* Disables highlighting across general areas of the application
* Updates troubleshooting steps on about page

### Version 1.0.2

* Adds ability to start and stop multiple selected motors simultaneously
* Fixes high CAN utilization when switching between many SPARK device tabs
* Fixes an issue causing some SPARKs to continue spinning when disabling multiple at once
* Fixes an issue causing SPARK devices to resume spinning after leaving the bus and returning

### Version 1.0.1

* Fixes crash when opening on macOS
* Fixes detection of devices on Linux
* Fixes app icon

### Version 1.0.0

Initial stable release of REV Hardware Client 2
