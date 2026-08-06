> Source: https://docs.revrobotics.com/rev-hardware-client/ion/recovery-mode.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/ion/recovery-mode.md).

# Recovery Mode

{% hint style="danger" %}
Those using REV ION products on REVLib 2026 or newer must use [REV Hardware Client 2](https://docs.revrobotics.com/rev-hardware-client-2).
{% endhint %}

Sometimes, when updating the firmware on an ION Control System Device, it is possible for the process to be interrupted or for the firmware to be corrupted by a bad download or other type of interruption in data transfer. In this state, the Status LED will be dark or dim and the device will fail to operate. There is a built-in recovery mode that can force your device to accept new firmware even if the controller seems to be bricked and the procedure is outlined below:

{% hint style="warning" %}
Performing this procedure will erase all data and settings on the device. Be sure to burn your desired settings to flash after recovering the device
{% endhint %}

### Materials Needed

* A small tool, like a straightened paper clip or a SIM card removal tool, to press the Mode Button&#x20;
* Data-capable USB-C to USB-A cable
* A Windows computer with the [REV Hardware Client](/rev-hardware-client/gs/install.md)[ Installed](/rev-hardware-client/gs/install.md) and updated to the latest version

### Recovery Mode Steps

1. With the Device powered off, press and hold the Mode Button
2. While still holding the Mode Button, connect the Device to the computer using the USB-C cable - the Status LED will not illuminate - this is expected.
3. With the REV Hardware Client running on the computer, wait a few seconds for the audible tone or icon for the device to be recognized in recovery mode then release the Mode Button - no lights will be present on the device during this stage of the process, this is expected
4. Select the Device in Recovery Mode from the REV Hardware Client window<br>

   <figure><img src="/files/nqgssZHYhRYQMFx5k4lz" alt=""><figcaption><p>Example of a Device in Recovery Mode</p></figcaption></figure>
5. From the Choose a Device type dropdown, choose - the firmware that matches the device you are attempting to recover. *It is possible to install incorrect firmware on your device.*<br>

   <figure><img src="/files/fzfBlsDSP9rhKZaRCeqG" alt=""><figcaption></figcaption></figure>
6. Choose the latest version of Firmware from the dropdown and then click update<br>

   <figure><img src="/files/Lht7rvNyWRPnhsh1xUo2" alt=""><figcaption><p>Selecting the firmware on a SPARK MAX in recovery</p></figcaption></figure>
7. Wait for the software update to complete<br>

   <figure><img src="/files/DjAslEXChL2nH0ZQr4hA" alt=""><figcaption></figcaption></figure>
8. Power cycle your device (unplug and plug in USB-C) click on the device's icon, and then clear any sticky faults

{% hint style="success" %}
Firmware Recovery Complete!&#x20;
{% endhint %}
