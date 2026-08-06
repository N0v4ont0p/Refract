> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/servo-hub-firmware-changelog.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/servo-hub-firmware-changelog.md).

# Servo Hub Firmware Changelog

### Version 26.1.3

* Fixes USB compatibility for Mac

### Version 26.1.2

* Fixes bug preventing updating downstream SPARK devices

### Version 26.1.1

* Improves performance of USB bridging

### Version 26.1.0

* Fixes bug preventing proper communication with downstream SPARKs
* Updates the bootloader. This update must be done via DFU.
* Switches the USB CAN bridging to use SLCan
  * Note: Devices that use SLCan are NOT compatible with REV Hardware Client when used over USB. Devices running v26.x.x+ can only be used via REVUI, or downstream of a REV CAN device running v25.x.x or lower with RHC.

### Version 25.0.2

* Fixes 'Servo Hub x reported temporary power loss' reported when a battery is charged above 13.5V

### Version 25.0.1

* Fixes bug causing some servo hub boards to read channel current more slowly
* Fixes case where Servo Hub doesn't report being in the primary lock state

### Version 25.0.0

* Improves robustness of overcurrent handling
* Tracking for whether any CAN message came from hardware CAN
* Recovery task to detect when the short-circuit is removed
* Turn off the Buck Regulator when PGood falls
* Set PGood Fault based on pin state

### Version 24.0.4

Initial Servo Hub Release

* Control servos via RS-485 or CAN
* Channels can be enabled/disabled individually
* Channels can be powered on/off individually
* Status LEDs show the current state of each channel
* Adds over-current protection per-channel
