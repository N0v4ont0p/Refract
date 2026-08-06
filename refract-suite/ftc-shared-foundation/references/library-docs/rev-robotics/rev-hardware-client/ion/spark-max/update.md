> Source: https://docs.revrobotics.com/rev-hardware-client/ion/spark-max/update.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/ion/spark-max/update.md).

# Updating a SPARK MAX

{% hint style="danger" %}
Those using REV ION products on REVLib 2026 or newer must use [REV Hardware Client 2](https://docs.revrobotics.com/rev-hardware-client-2).
{% endhint %}

## Updating a Single SPARK MAX

* Connect your SPARK MAX Motor Controller to your computer with a USB-C cable.
* Open the REV SPARK MAX Client application.
* The Client should automatically scan and connect to your SPARK MAX.&#x20;

Once the SPARK MAX is connected via USB-C select it within the **Connected Hardware.**&#x20;

<figure><img src="/files/Ktk3Wb937MGiRXTkDdV0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If the SPARK MAX connected via USB-C is running firmware version 1.5.0 or later allows the SPARK MAX to work as a USB to CAN Bridge. Other CAN connected SPARK MAXs running version 1.4.0 can be selected for firmware updates over CAN.
{% endhint %}

Within the Hardware Client, for the SPARK MAX, there are 5 tabs. The Hardware Client will open up on the **Basic** tab. To update firmware select the **Update** tab.&#x20;

<figure><img src="/files/haFUGSv31eBLVapPSFX7" alt=""><figcaption></figcaption></figure>

Under **SPARK MAX Firmware**, select download to download the latest version of the firmware.&#x20;

<figure><img src="/files/cYU05up8d1fgH12iEtUW" alt=""><figcaption></figcaption></figure>

Once the firmware has downloaded select update.

<figure><img src="/files/N5OqrfGzxn4EqS23SHBX" alt=""><figcaption></figcaption></figure>

The update process will flash the firmware image onto the SPARK MAX. The status bar will show the progress of the process.&#x20;

<figure><img src="/files/9cJfqi0DAwBqJgvp4J1S" alt=""><figcaption></figcaption></figure>

Once the firmware update is done your SPARK MAX will show a new status of **Up-to-Date.**

<figure><img src="/files/zZgdUDdaGlDV1hKCafZT" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If your SPARK MAX is running firmware older than 1.4.0, you may need to unplug and replug the USB-C cable into the SPARK MAX for it to reconnect to the Client.&#x20;
{% endhint %}

## Updating Multiple Devices with the USB-to-CAN Bridge

SPARK MAX Firmware Version 1.5.0 includes a USB-to-CAN Bridge feature that allows a single USB-connected SPARK MAX to act as a bridge to the entire CAN bus it is connected to. This allows for configuration and simultaneous updating of multiple SPARK MAX controllers without having to connect to each one individually. Using this feature requires the following:

* A USB-connected SPARK MAX that is updated to firmware version 1.5.0 or newer to act as the Bridge.
* Other SPARK MAXs connected on the CAN bus must be individually updated to firmware version 1.4.0 before they are able to receive mass-updates from the Bridging SPARK MAX.

Once these requirements are satisfied, navigate to the **Hardware** tab, select the **Update All** button.

<figure><img src="/files/eLGaQ9xUKpwIWrERQv4L" alt=""><figcaption></figcaption></figure>

Each device with the Out-of-Date warning will update with the latest version of the firmware.
