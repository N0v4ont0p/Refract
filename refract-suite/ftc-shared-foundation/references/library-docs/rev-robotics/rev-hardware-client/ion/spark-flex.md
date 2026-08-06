> Source: https://docs.revrobotics.com/rev-hardware-client/ion/spark-flex.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/ion/spark-flex.md).

# SPARK Flex

{% hint style="danger" %}
Those using REV ION products on REVLib 2026 or newer must use [REV Hardware Client 2.](https://docs.revrobotics.com/rev-hardware-client-2)
{% endhint %}

## Connecting a SPARK Flex via USB

* Connect your SPARK Flex Motor Controller to your computer with a USB C cable.
* Open the REV Hardware Client application.
* The Client should automatically scan and connect to your SPARK Flex

<figure><img src="/files/H9qBRXY4gWQ53PHydMzt" alt=""><figcaption><p>SPARK Flex in the 1.6.1v of the REV Hardware Client</p></figcaption></figure>

{% hint style="info" %}
Additional SPARK Flex devices connected via CAN to the USB Host SPARK Flex are visible when using the latest firmware. For more information see the [SPARK Flex User's Manual.](https://docs.revrobotics.com/brushless/spark-flex/overview)
{% endhint %}

## Navigating the REV Hardware Client

The REV Hardware Client has four tabs to manage different features of the Client. The "Hardware Tab" is where supported hardware devices are managed. The "Utilities Tab" allows for viewing log files collected by the Control Hub or Driver Hub. The "Downloads Tab" allows for the downloading of supported device software for updating when offline. The "About Tab" has information on what devices are supported, updating the REV Hardware Client, and troubleshooting.

Individual devices, like the SPARK Flex, have additional tabs available when the device is selected. For a full overview of the default navigation features of the REV Hardware Client see the [User's Manual.](/rev-hardware-client/home/rev-hardware-client-overview.md) Below is more information on using the specific features for the SPARK Flex.

{% hint style="warning" %}
As of REV Hardware Client version 1.7.0, "Burn Flash" has been renamed to "Persist Perimeters"!
{% endhint %}

### Hardware Tab

The Hardware Tab is used to select devices connected via USB or the USB to CAN bridge for configuration, updates, and more.

<figure><img src="/files/S9lO051uGYi5J9zGNoTj" alt=""><figcaption><p>A SPARK Flex, PDH, and SPARK MAX showing in the 1.6.1 RHC</p></figcaption></figure>

Once a SPARK Flex is selected from the Hardware tab a number of device specific tabs will show.

### Basic Tab

The Basic Tab is used to set the most common parameters for the SPARK Flex.

<figure><img src="/files/HKA2DJJTeabc553xm3r9" alt=""><figcaption></figcaption></figure>

1. **Device Identify:** Blink the selected SPARK Flex's LED for identification.
2. **CAN ID:** This assigns a SPARK Flex a CAN ID for identification over the CAN BUS. Any configured SPARK Flex **must have** a CAN ID.
3. **Configurations:** This drop down allows you to select pre-existing configurations store on the Windows machine running the SPARK Flex Client or to pull the existing parameters stored on in RAM on the SPARK Flex. This is helpful when configuring multiple motor controllers to the same settings.
4. **Configured Parameters:** Change the motor type, sensor type, idle mode behavior, and more.

{% hint style="warning" %}
The ability to switch "Motor Type" to brushed on the SPARK Flex will be available with the SPARK Flex Dock (Coming Soon!)
{% endhint %}

### Advanced Tab

The Advanced Tab allows for changing all configurable parameters of the SPARK Flex without needing to set them in code.

<figure><img src="/files/7j4rT0ARfOwCBcTUKVDx" alt=""><figcaption><p>SPARK Flex "Advanced" Menu</p></figcaption></figure>

1. **Search Parameters:** Allows for easy look up of a specific parameter for editing.
2. **Parameter Table:** Select the arrow to show all configurable parameters within a specific group.&#x20;

{% hint style="info" %}
Remember to persist the parameters to memory before disconnecting the SPARK Flex
{% endhint %}

### Run Tab <a href="#run-tab" id="run-tab"></a>

The Run Tab allows for the SPARK Flex to operate over USB or a USB to CAN Bridge without the need for a full control system. This is helpful for testing mechanisms and tuning their control loops.

<figure><img src="/files/3Yc8IlU9iaNdM09MvjQt" alt=""><figcaption><p>SPARK Flex "Run" Menu</p></figcaption></figure>

1. **Run:** Choose setpoints to run a motor connected to a SPARK Flex using various modes, including position, velocity, and duty cycle.
2. **PIDF:** Update PIDF parameters on the fly to tune control loops on the SPARK Flex.
3. **View Graph:** Moves the Client over to the Telemetry Tab to show any added signals in graph form when running a SPARK Flex. This is helpful when tuning control loops.

### Update Tab <a href="#update-tab" id="update-tab"></a>

The Update tab shows what version of firmware is on the selected device, if that device is up to date, and update the firmware of the selected device.

<figure><img src="/files/bZIPGij6zciedNNvRSUb" alt=""><figcaption><p>SPARK Flex "Update" Tab</p></figcaption></figure>

1. **Download Latest Firmware:** Downloads latest firmware onto the local machine running the Client.
2. **Update Firmware:** Updates the selected device with the latest firmware.
3. **Out-of-date Firmware Warning:** Warning to alert the user there is new firmware available for any connected device.
