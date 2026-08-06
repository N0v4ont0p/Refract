> Source: https://docs.revrobotics.com/rev-hardware-client-2/rhc2/troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client-2/rhc2/troubleshooting.md).

# Troubleshooting

{% hint style="warning" %}
Please note that you cannot update the original Hardware Client to Hardware Client 2. You must install Hardware Client 2 separately, as they are completely different applications. While they can be installed simultaneously, it is not recommended to have both open at the same time.
{% endhint %}

## Device is not visible

&#x20;If you don't see all of the devices that you expect to see, follow these steps:

* Make sure that you are connected to the Internet, so that Windows can download the necessary drivers
* Disconnect the device from the computer and then reconnect it

### Mac Users and Recovery Mode

If you plan on using RHC2 on a macOS machine, please note that recovery mode devices will only show up on mac if the app is copied into /Applications.

### SPARK MAX Motor Controller

* Make sure that the SPARK MAX is not being used by another application, such as the REV SPARK MAX Client
* Unplug the SPARK MAX from the computer and plug it back in

## Firmware Compatibility

To use your device with RHC2, you must have 2026 firmware (v26.x.x). Devices with 2025 firmware or lower must be updated to 2026 via [recovery mode](https://docs.revrobotics.com/rev-hardware-client/ion/recovery-mode). SPARKs can be updated via CAN with RHC2 if the bridge device (the device connected to USB) is updated to firmware 2026.
