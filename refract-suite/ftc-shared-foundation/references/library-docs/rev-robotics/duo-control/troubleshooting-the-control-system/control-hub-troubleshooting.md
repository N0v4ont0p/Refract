> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting.md).

# Control Hub Troubleshooting

The following questions consider common indicators of issues seen in the Control Hub. Think about the potential indicators your Hub is currently exhibiting and consider the following questions:&#x20;

| Is the Driver Station device unable to connect to to the Control Hub Wi-Fi?                              | [Yes](#driver-station-wont-connect)                         |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Is the Driver Station connected to the Wi-Fi but not showing a ping or any other signs of communication? | [Yes](#driver-station-wont-connect)                         |
| Has the Status LED been solid blue for longer than 30 seconds (after start up)?                          | [Yes](#status-led-is-solid-blue-for-longer-than-30-seconds) |

### Can't Connect the Control Hub to the REV Hardware Client

<figure><img src="/files/tejboVjPKR5hvz1xwtbx" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The Wi-Fi reset will down grade the Wi-Fi connection to 2.4GHz. If you have an android device with 5GHz you may want to switch the Wi-Fi Band in order to run on 5GHz. *Check out the* [*Updating Wi-Fi Settings* ](/duo-control/menu/control-hub-gs/updating-wifi-settings.md)*Section to learn more about making this switch.*
{% endhint %}

External factors, such as local Wi-Fi environment, play a part in the ability to establish or maintain a connection between a Control Hub and a computer. Like all aspects of of troubleshooting its important to isolate an issue by asking questions and discovering the answers! As you work on troubleshooting consider the following questions:&#x20;

* **What is your local Wi-Fi environment like?**&#x20;
  * Local Wi-Fi environment effects the consistency of a connection to the Control Hub. Use a [Wi-Fi analyzer](https://play.google.com/store/apps/details?id=com.farproc.wifi.analyzer\&hl=en) to check the local environment for channels that are cluttered with Wi-Fi networks. [Change the Control Hubs Wi-Fi channel ](/duo-control/managing-the-control-system/ch-wifi.md#rev-hardware-client)to a channel with the least amount of overlap with other networks.
* **Are you connected to another Wi-Fi network?**
  * The Control Hub produces a non internet Wi-Fi connection. Settings on the individual computer may cause the device to jump to a local, remembered network that produces an internet connection.
* **Are you in a school or a place of business?**
  * In addition to the amount of local networks in an environment its important to understand what those local networks are capable of. For instance, some school districts have security measures in place that block unauthorized Wi-Fi access points. Talk to your local Wi-Fi adminstrator to find out what you need to get the Control Hub as an approved network.

{% hint style="warning" %}
If the Control Hub SSID is not shown in the list of available Wi-Fi networks, try manually entering the Control Hub SSID to see if that allows you to connect.&#x20;
{% endhint %}

Contact REV Support with details of the troubleshooting information you have collected such as the answers to the questions above and the outcome of your troubleshooting thus far. It will also help to send logs or other diagnostic data to REV Support.&#x20;

{% hint style="info" %}
Need help getting the Log Files to send to REV Support? See [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more information.
{% endhint %}

### Driver Hub Won't Connect&#x20;

{% hint style="danger" %}
Information in this flowchart is for the initial bring up of connecting the Control Hub with a Driver Station. For issues with intermittent connection or periodic connection drops please check out the information below this flowchart.
{% endhint %}

<figure><img src="/files/JsWEt8SfGP1i8227aYLT" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The Wi-Fi reset will down grade the Wi-Fi connection to 2.4GHz. If you have an android device with 5GHz you may want to switch the Wi-Fi band in order to run on 5GHz. *Check out the* [*Updating Wi-Fi Settings* ](/duo-control/menu/control-hub-gs/updating-wifi-settings.md)*Section to learn more about making this switch.*
{% endhint %}

External factors, such as local Wi-Fi environment, play a part in the ability to establish or maintain a connection between a Control Hub and a Driver Station device. Like all aspects of of troubleshooting its important to isolate an issue by asking questions and discovering the answers! As you work on troubleshooting consider the following questions:&#x20;

* **Is your system operating on a 2.4 GHz band or 5GHz band?**
  * REV recommends, if you have a dual band Driver Station device, that you operate on the 5GHz Wi-Fi band. Check out the [Updating Wi-Fi Settings](/duo-control/menu/control-hub-gs/updating-wifi-settings.md) section to learn more about making this switch.
* **What is your local Wi-Fi environment like?**&#x20;
  * Local Wi-Fi environment effects the consistency of a connection to the Control Hub. Use a [Wi-Fi analyzer](https://play.google.com/store/apps/details?id=com.farproc.wifi.analyzer\&hl=en) to check the local environment for channels that are cluttered with Wi-Fi networks. [Change the Control Hubs Wi-Fi channel ](/duo-control/managing-the-control-system/ch-wifi.md#rev-hardware-client)to a channel with the least amount of overlap with other networks.&#x20;
* **Are you in a school or a place of business?**
  * In addition to the amount of local networks in an environment its important to understand what those local networks are capable of. For instance, some school districts have security measures in place that block unauthorized Wi-Fi access points. Talk to your local Wi-Fi administrator to find out what you need to get the Control Hub as an approved network.
* **Does the the Driver Station connect to the Control Hub until a mechanism is run?**&#x20;
  * Certain mechanisms draw enough power from the Control Hub to put a strain on the battery. If you notice a drop in displayed voltage when you start a code, or when a particular mechanism is run, this may be indicative of a brown out condition. Other indicators include:&#x20;
    * The Driver Station throwing errors about power to the system
    * The Driver Station making a disconnect sound
    * The voltage on the Driver Station showing 9 volts or lower when running code&#x20;
    * Motors running at lower speeds then what they have been set to run
  * To remedy this issue check out our instructions on [proper battery care.](https://www.revrobotics.com/rev-31-1302/)&#x20;

{% hint style="warning" %}
If the Control Hub SSID is not shown in the list of available Wi-Fi networks, try manually entering the Control Hub SSID on the Driver Station to see if that allows you to connect.&#x20;
{% endhint %}

If you are still experiencing connection issues, once you have gone through the flowchart and worked on addressing the potential root of connection issues describe in the list above, start looking for patterns in the behavior. How often does this behavior appear? Are there certain things that happen around the same time the disconnects happen? The following list provides some ideas on what sort of patterns you might see:

* The Control Hub connects fine when a team member takes it home but doesn't seem to like to connect at school.
* The Control Hub connects fine until you start driving the robot around.

{% hint style="info" %}
Just remember correlation does not equal causation of an event but is useful data to further troubleshooting
{% endhint %}

Contact REV Support with details of the troubleshooting information you have collected such as the answers to the questions above and the outcome of your troubleshooting thus far. It will also help to send logs or other diagnostic data to REV Support.&#x20;

{% hint style="info" %}
Need help getting the Log Files to send to REV Support? See [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more information.
{% endhint %}

### Status LED is Solid Blue for Longer than 30 Seconds&#x20;

{% hint style="info" %}
This section is for troubleshooting a Control Hub. If you have an Expansion Hub please refer to the [Expansion Hub Troubleshooting](/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system.md#expansion-hub-troubleshooting) guide for help solving Expansion Hub related issues.&#x20;
{% endhint %}

<figure><img src="/files/0BbNwCrfM7GQUooldUWv" alt=""><figcaption></figcaption></figure>

The status LED on the Control Hub is similar to a check engine light on a car. A solid blue status LED indicates the Robot Controller is not communicating to the I/O of the Control Hub, but not what the root cause is. Updating the Control Hub to the latest version of all the software is a first step to resolving this issue, listed below are two ways to update.

#### Using the REV Hardware Client

The [REV Hardware Client](/duo-control/managing-the-control-system/rev-hardware-client.md) is software designed to make managing REV devices easier for the user. This Client automatically detects connected device(s), downloads the latest software for those device(s), and allows for seamless updating of the device(s). Using the REV Hardware Client allows you to perform any required updates that may be needed to recover your Control Hub. The Hardware Client can also be used to [Send Diagnostic Data to REV](/duo-control/managing-the-control-system/downloading-log-file.md#rev-hardware-client).&#x20;

{% hint style="info" %}
If you do not have a Windows 10 or higher PC, see [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more options on getting your diagnostic data to REV, and [Updating Firmware](/duo-control/managing-the-control-system/updating-firmware.md), [Updating Operating System](/duo-control/managing-the-control-system/updating-operating-system.md), and [Updating Robot Controller Application](/duo-control/managing-the-control-system/updating-robot-controller-application.md) for steps to update the software.
{% endhint %}

#### Using Android Studio&#x20;

{% hint style="warning" %}
The Control Hub must run version 5.0 or higher of the Robot Controller Application. If using Android Studio, make sure you are using a 5.0 or higher project.
{% endhint %}

If you use Android Studio for coding you will need to update your Robot Controller application by creating a new Android Studio project with the most recent version of the Robot Controller APK. Information on this process can be found in [FTC Wiki Android Studio Tutorial](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Downloading-the-Android-Studio-Project-Folder).

### XT30 Pins are Compressed

The most common cause of a loose or wiggly XT30 port is compressed pins within the male XT30 connector on your Hub. Each pin of the male XT30 connector is made of 4 tines that should have a small amount of space between them. In the image below, the pin on the top has the correct amount of space and the bottom one is visibly compressed, however, an XT30 pin can still be too compressed even if there is visible space.

<figure><img src="/files/X7EGjtyOrWDolocY4ZAX" alt="detail shot of the XT30 connector&#x27;s tines. The top pin has tines that show the correct amount of space and the bottom pin shows a pin that&#x27;s pins are compressed"><figcaption></figcaption></figure>

To help repair compressed XT30 pins, we recommend using an X-ACTO Knife or similar very thin blade to slightly separate the tines. Please use extreme caution when doing this repair as expanding the tines too far can cause the XT30 connector to not fit.

<figure><img src="/files/gJU38k3EoRfawVlvxEQw" alt="close up of the Male XT30 port&#x27;s tines being separated with an x-acto knife"><figcaption></figcaption></figure>

After slightly separating the tines, the male and female XT30 connectors should have a more secure connection.

{% hint style="warning" %}
Again, please remember that this repair needs to be done carefully, as overextending the tines of the XT30 connector can cause them to become weakened and hold their shape less. Because of the nature of this kind of damage or wear to your Hub, compressed or overextended pins are not covered under warranty.
{% endhint %}

### Still Need Assistance?

Contact REV Support with details of the troubleshooting information you have collected such as the answers to the questions above and the outcome of your troubleshooting thus far. It will also help to send logs or other diagnostic data to REV Support.&#x20;

{% hint style="info" %}
Need help getting the Log Files to send to REV Support? See [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more information.
{% endhint %}
