> Source: https://docs.revrobotics.com/rev-hardware-client/crossover/servo-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/crossover/servo-hub.md).

# Servo Hub

<figure><img src="/files/cypT2G2tBl3ud3rMocKk" alt="" width="375"><figcaption></figcaption></figure>

## Connecting a Servo Hub via USB

* Connect your Servo Hub to your computer with a USB C cable.
* Open the REV Hardware Client application.
* The Client should automatically scan and connect to your Servo Hub

## Navigating the REV Hardware Client

The REV Hardware Client has four tabs to manage different features of the Client. The "Hardware Tab" is where supported hardware devices are managed. The "Utilities Tab" allows for viewing log files collected by the Control Hub or Driver Hub. The "Downloads Tab" allows for the downloading of supported device software for updating when offline. The "About Tab" has information on what devices are supported, updating the REV Hardware Client, and troubleshooting.

Individual devices, like the Servo Hub, have additional tabs available when the device is selected. For a full overview of the default navigation features of the REV Hardware Client see the [User's Manual.](/rev-hardware-client/home/rev-hardware-client-overview.md) Below is more information on using the specific features for the Servo Hub.

### Basic Tab

<figure><img src="/files/wg3sDmxiMVwAh50wcVCz" alt=""><figcaption></figcaption></figure>

1. **CAN ID:** This assigns the Servo Hub a CAN ID for identification over the CAN BUS. Any configured Servo Hub **must have** a CAN ID. This is also the **Hub Address** used with the Control Hub and Expansion Hub.&#x20;
2. **Servo Limits:** Here you can set the angular limits for each servo port. Any changes to these parameters are automatically saved to the Servo Hub.&#x20;
3. **Disabled Behavior:** This drop down allows you to select the behavior of the Servo Hub when it is disabled through code.&#x20;

### Servo Tab

<figure><img src="/files/IcoxPjbCHs30iCs7Iu2L" alt=""><figcaption></figcaption></figure>

1. **Servo Controls:** These controls allow you to run and test servos connected to the Servo Hub through the REV Hardware Client. This is useful for testing your servo's application.&#x20;

### Update Tab <a href="#update-tab" id="update-tab"></a>

The Update tab shows what version of firmware is on the selected device, if that device is up to date, and update the firmware of the selected device.

<figure><img src="/files/v6FHLGpAxRhkefZIokh5" alt=""><figcaption></figcaption></figure>

1. **Download Latest Firmware:** Downloads latest firmware onto the local machine running the Client.
2. **Update Firmware:** Updates the selected device with the latest firmware.
3. **Out-of-date Firmware Warning:** Warning to alert the user there is new firmware available for any connected device.
