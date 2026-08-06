> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/expansion-hub-troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/expansion-hub-troubleshooting.md).

# Expansion Hub Troubleshooting

The following sections, "[Common Indicators and their Solution Steps](/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system.md#common-indicators-and-their-solution-steps)," provides common indicators of issues seen in the Expansion Hub. Think about what the potential indicators your Hub is currently exhibiting and consider the following questions:&#x20;

* Did you perform a firmware update before the Hub began to have issues?
* What is the behavior of the Status LED on the Expansion Hub?
* Is the Driver Station showing an error message 'Cant find the Expansion Hub Portal"?
* Did the Robot Controller app open when you plugged in the RC phone and gave power to the Hub?
* Are you experiencing issues with communication between a primary and secondary Hub?

{% hint style="info" %}
*If a path in this guide does not resolve the issue please contact REV Robotics Support at <support@revrobotics.com>*
{% endhint %}

### Common Indicators and their Solution Steps&#x20;

* The firmware update failed and the Hub is unresponsive&#x20;
  * Try a [Firmware Update](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware#expansion-hub)
* The LED on the Expansion Hub is not lighting up&#x20;
  * Try a [Firmware Update](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware#expansion-hub)&#x20;
  * [The LED is still not lighting up ](#usb-serial-converter-check)
* The Hub is not being recognized or communicating with the phones&#x20;
  * Try doing the [Hub Startup Procedure ](#hub-startup-procedures)
* There are [issues seeing a secondary Expansion Hub](#issues-seeing-a-secondary-expansion-hub)

{% hint style="info" %}
**Expansion Hubs purchased AFTER December 2021 no longer include an internal IMU**
{% endhint %}

### Issues Connecting Control Hub to an Expansion Hub

{% embed url="<https://youtu.be/f1ev2Ap9Ywo>" %}

The steps below utilize information provided in the [Adding an Expansion Hub ](/duo-control/menu/adding-more-motors/adding-an-expansion-hub.md)article. Use this article to help you navigate as you run through the troubleshooting flowchart. &#x20;

<figure><img src="/files/lOXo9oLW3Ok6bkhXcCLZ" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To update a Robot Controller check out the article on [Updating the Robot Controller Application](/duo-control/managing-the-control-system/updating-robot-controller-application.md).
{% endhint %}

If you are attempting to connect two Expansion Hubs together please confirm that the first Expansion Hub is connected to the Robot Controller. From there change the Expansion Hub address. For information on how to change the Expansion Hub address check out the [FTC Wiki Using a Second Expansion Hub](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Using-Two-Expansion-Hubs#checking-the-address-of-an-expansion-hub) article.&#x20;

### XT30 Pins are Compressed

The most common cause of a loose or wiggly XT30 port is compressed pins within the male XT30 connector on your Hub. Each pin of the male XT30 connector is made of 4 tines that should have a small amount of space between them. In the image below, the pin on the top has the correct amount of space and the bottom one is visibly compressed, however, an XT30 pin can still be too compressed even if there is visible space.

<figure><img src="/files/X7EGjtyOrWDolocY4ZAX" alt="detail shot of the XT30 connector&#x27;s tines. The top pin has tines that show the correct amount of space and the bottom pin shows a pin that&#x27;s pins are compressed"><figcaption></figcaption></figure>

To help repair compressed XT30 pins, we recommend using an X-ACTO Knife or similar very thin blade to slightly separate the tines. Please use extreme caution when doing this repair as expanding the tines too far can cause the XT30 connector to not fit.

<figure><img src="/files/gJU38k3EoRfawVlvxEQw" alt="close up of the Male XT30 port&#x27;s tines being separated with an x-acto knife"><figcaption></figcaption></figure>

After slightly separating the tines, the male and female XT30 connectors should have a more secure connection.

{% hint style="warning" %}
Again, please remember that this repair needs to be done carefully, as overextending the tines of the XT30 connector can cause them to become weakened and hold their shape less. Because of the nature of this kind of damage or wear to your Hub, compressed or overextended pins are not covered under warranty.
{% endhint %}

### **Firmware Update**

Use the[ REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client/) to [update the Expansion Hub](https://docs.revrobotics.com/rev-hardware-client/expansion-hub/updating-expansion-hub).

### USB Serial Converter Check&#x20;

1. Plug your Expansion Hub into a Windows PC
2. Open the Device Manager in Settings
3. Click the arrow next to Universal Serial Bus Controllers
4. Find USB Serial Converter under the menu
5. If this is not present there maybe a larger issue with your hub. Email <support@revrobotics.com> with details of the steps you have taken so far and any order numbers for the Expansion Hub (if you have them)

{% hint style="warning" %}
If you are using a Mac you can use System Information in Lion or later (or System Profiler in Snow Leopard and earlier versions of Mac OS) in Spotlight (press ⌘ and Space ). The program is in /Applications/Utilities and is the tool to see the connected USB devices and other hardware details.
{% endhint %}

### Expansion Hub Power Cycle

1. Unplug the USB from your RC phone
2. Power off the main robot switch (turn off 12V power from the Expansion Hub(s))
3. Wait a few seconds
4. Turn on the Main Robot Switch (supply 12V power to the Expansion Hub(s))
5. On your RC phone, press the square button and the swipe to close the FTC RC app
6. Plug your RC phone into the USB-- the FTC app should automatically open
   1. If the app doesn't automatically open, you do not have a good connection from the Expansion Hub to the Phone. Check your cables first, followed by the micro and mini USB connections.
   2. Consider using some form of strain relief (like the[ REV USB Retention Mount](http://www.revrobotics.com/rev-41-1214/) or one of the many 3d printable options available on places like Thingiverse) to keep the USB-mini port from being damaged.

{% hint style="info" %}
If the issues persist after applying the Retention Mount, try running through the [Firmware Update](/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system.md#firmware-update) procedure.
{% endhint %}

### Still Need Assistance?

Contact REV Support with details of the troubleshooting information you have collected such as the answers to the questions above and the outcome of your troubleshooting thus far. It will also help to send logs or other diagnostic data to REV Support.&#x20;

{% hint style="info" %}
Need help getting the Log Files to send to REV Support? See [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more information.
{% endhint %}
