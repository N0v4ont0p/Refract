> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-the-driver-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-the-driver-hub.md).

# Updating the Driver Hub

The Driver Hub has two pieces of software that are field upgradable, the Driver Hub Operating System and the Driver Station Application. Both pieces of software are updatable either through the [REV Hardware Client](/duo-control/managing-the-control-system/updating-the-driver-hub.md#rev-hardware-client) or directly on the [Driver Hub with the Software Manager](/duo-control/managing-the-control-system/updating-the-driver-hub.md#driver-hub-software-manager).&#x20;

## Driver Hub Software Manager

The Driver Hub has a Software Manager Application pre-installed for updating the Driver Hub. Open the application by pressing on the Software Manager icon. Select the Update All button to update all the software that requires updating.

{% hint style="info" %}
Make sure the Driver Hub is connected to a Wi-Fi network with access to the internet to download and install the latest software.
{% endhint %}

![](/files/-Ma5AKbvt2TL3KEjzCSb)

{% hint style="info" %}
The updates can take several minutes to complete. Make sure the Driver Hub is charged or plug in the Driver Hub during the updating process.
{% endhint %}

## REV Hardware Client

Start the REV Hardware Client and connect the Driver Hub to the PC using the USB-A to USB-C cable. Once the Driver Hub is connected, it will show up on the front page of the UI under the **Hardware Tab**. Select the Driver Hub.

![](/files/-M_gj7qK7cQ1TcSHAoGF)

After selecting the Connected Hardware, the Update tab will pop up. Any software that needs updating will have an Out-of-Date notification. Pressing the Update button allows the REV Hardware Client to download the software update and install on the Driver Hub.

![](/files/-M_gjBM1BbFGx9zN_ubo)

{% hint style="success" %}
Once all the Out-of-Date notifications are cleared, the Driver Hub is fully up to date.
{% endhint %}
