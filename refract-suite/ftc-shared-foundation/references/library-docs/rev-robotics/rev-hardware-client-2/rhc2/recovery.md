> Source: https://docs.revrobotics.com/rev-hardware-client-2/rhc2/recovery.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client-2/rhc2/recovery.md).

# Recovery Mode

Sometimes, when updating the firmware on an ION Control System Device, it is possible for the process to be interrupted or for the firmware to be corrupted by a bad download or other type of interruption in data transfer. In this state, the Status LED will be dark or dim and the device will fail to operate. There is a built-in recovery mode that can force your device to accept new firmware even if the controller seems to be bricked and the procedure is outlined below:

{% hint style="warning" %}
Performing this procedure will erase all data and settings on the device. You'll need to reconfigure your device after performing recovery mode.
{% endhint %}

### Materials Needed

* A small tool, like a straightened paper clip or a SIM card removal tool, to press the Mode Button&#x20;
* Data-capable USB-C to USB-A cable
* Computer with the [REV Hardware Client 2](/rev-hardware-client-2/rhc2/overview.md) installed and updated to the latest version

### Recovery Mode Steps

1. With the Device powered off, press and hold the Mode Button
2. While still holding the Mode Button, connect the Device to the computer using the USB-C cable - the Status LED will not illuminate - this is expected.
3. With the REV Hardware Client 2 running on the computer, wait a few seconds for the audible tone or icon for the device to be recognized, then release the Mode Button - no lights will be present on the device during this stage of the process. This is expected
4. Select the DFU Device Bootloader from the list of Connected Devices within the REV Hardware Client 2 window<br>

   <figure><img src="/files/sDSLl0IguFfdTXZ7JjZd" alt=""><figcaption><p>Example of a Device in Recovery Mode</p></figcaption></figure>
5. From the Device Type dropdown menu, choose the device name that matches the type of device you are attempting to recover. *\*\*Note: It is possible to install incorrect firmware on your device.*<br>

   <figure><img src="/files/XN5kK0BfOOZPry8ATKpw" alt=""><figcaption></figcaption></figure>
6. After the proper Device Type has been selected, the Current Firmware Version Dropdown menu will automatically select the most up-to-date firmware. If you wish to install a different version of firmware, please select it from this menu now. To use the REV Hardware Client 2, this firmware will still need to be version 26.x.x or newer.
7. Wait for the software update to complete
8. Power cycle your device (unplug and plug in USB-C) click on the device's icon, and then clear any sticky faults that may show

{% hint style="success" %}
Firmware Recovery Complete!&#x20;
{% endhint %}
