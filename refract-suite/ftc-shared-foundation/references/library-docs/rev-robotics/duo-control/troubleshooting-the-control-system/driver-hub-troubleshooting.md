> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting.md).

# Driver Hub Troubleshooting

{% hint style="info" %}
In this troubleshooting guide we will use specific language to describe different ways of power cycling the Driver Hub.

**Turn Off/Power Off** - Long press (1-2 seconds) the power button so that a drop down menu appears, then tap "power off" on the screen

**Hard Reboot** - Hold power button for at least 10 seconds and do not touch anything on the screen. Once the green LED light turns off and the screen goes dark, release the power button, and the hard reboot is complete.
{% endhint %}

## Most Common Issues

{% tabs %}
{% tab title="Updating the OS" %}

### Updating the Driver Hub Operating System

When Updating your Driver Hub to the newest operating system, version 1.2.0, please be sure to follow these steps:

* Install the update on a fully charged Driver Hub. If the update fails, please plug in your hub and try again after fully charging.
* Don't touch the screen when a loading bar is displayed on the Driver Hub during the update process. If you touch the screen you will be directed to a menu after installation completes. Do not touch the screen and hard reboot your Driver Hub.
* Once you have updated your hub, please verify that your device is showing the current version 1.2.0, in the REV Hardware Client.&#x20;
  {% endtab %}

{% tab title="Unexpected Shut Down" %}

### Driver Hub Intermittent Battery Power Loss

Some Driver Hubs have a slight amount of extra space inside the battery bay that may cause a loss of power or intermittent battery charging. We have two quick fix options we are suggesting as solutions. The first is to use a small piece of folded paper or a few layers of tape to provide a more secure connection between the contacts. The second is a piece of foam tape we can ship to teams which will accomplish the same goal. Suggested installation steps are highlighted below:

### **Option 1: Tape Quick Fix**

![Tape (painters tape or masking tape) is placed on the thin edge above the battery on the side opposite the contacts](/files/0zLiTx1eW8qZw2YiX2eF)

![Any tape or paper  needs to sit inside the battery bay door edge](/files/Aqt1xxv2TbSEAeeGR9U7)

### **Option 2: Foam Tape**

![1. Cut foam tape into small pieces, approximately 2 inches or less long. The foam tape recommended is approximately 1/4 inch or less wide and 1/16 inch or less thick](/files/AvbQlKLu6Ps24M7XBTQR) ![2. Foam tape will be applied inside the battery case, opposite battery contacts and below the ridge that the battery door sits within.  ](/files/fTLyQgWXwl34fgEMVPsV)

![3. Stick foam strip in the middle, both side to side and top to bottom, of the vertical surface opposite the battery contact switch.](/files/YmuY6MOl4hWNncSkg0Gy) ![4. Press foam strip down firmly to make sure it sticks.](/files/WW0HrYVLMkWhSkv9J4Pf)

![5.1 Insert battery by inserting top of battery towards foam, and gently squeezing battery towards foam with thumb until battery can easily drop into battery case.](/files/CIxNKFNXkrR3wCiUUN2M) ![5.2 Continue to push the battery down until it is flush in the case.](/files/EJvID5CVVKy4Fkquh69z) ![6. Done](/files/4ZIIFK2dJtV5eVuKBey7)
{% endtab %}

{% tab title="Charging/Power" %}

### Common Charging/Power Issue Symptoms

The symptoms listed below can have a number of causes.

* Driver Hub only turns on when plugged into a charger
* Battery is discharging rapidly
* Battery reports low-battery at levels significantly above 0% and shuts off
* Device will not boot due to low battery even when Driver Hub is charged
* Driver Hub is on charger but will not turn on
* Device stopped charging and will not continue to charge&#x20;

#### To properly troubleshoot, please start with the steps below

1. Check the orientation of the battery - see [Battery Installation](#battery-installation)&#x20;
2. Ensure you are using the charger that came with the Driver Hub - the charger must specifically be a non-PD charger for these troubleshooting steps, and using the charger that was shipped with the Driver Hub is the simplest way to confirm that.
3. Unplugging and replugging in the charger from the Driver Hub may resolve some symptoms
4. Ensure your Driver Hub is [fully updated](/duo-control/managing-the-control-system/updating-the-driver-hub.md)
5. Perform a [Battery Recalibration](/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md#battery-calibration)
6. Complete the procedure to restore the [Driver Hub from "lockout"](/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md#battery-lockout-recovery)
7. If possible, swap the battery with a known good battery to see if the issue follows the battery or follows the Driver Hub unit
   {% endtab %}

{% tab title="Known Software Issues" %}
The following are known issues that we are working to resolve via a future software update:

### Waking Wi-Fi from a Sleep State

There is a known issue with the Wi-Fi driver not restarting correctly when the Driver Hub is woken from a "sleep" state. The current resolution is to perform a hard reboot on the device when the Driver Hub is having issues connecting to a Wi-Fi network.

You can make sure this issue doesn't happen before a match by leaving the screen on, and the Driver Station app open. This will prevent the Driver Hub from going to sleep.

### Unlock Times are Inconsistent&#x20;

Unlock can take anywhere from 2-10 seconds to occur, this is normal behavior.&#x20;

### Device Froze or Crashed while in Sleep Mode

Perform a hard reboot to wake up the device. This includes some cases where status LED B is solid green, indicating that the device is on, but the screen will not wake.&#x20;

### Inconsistent Battery Drain

Inconsistent battery draining while in a "sleep" state is a known issue. Devices may also shut off while in a "sleep" state due to this. Future software updates are in the works to resolve this.
{% endtab %}
{% endtabs %}

## Additional Troubleshooting

### Driver Hub Shows as a "Control Hub in Recovery Mode"

<figure><img src="/files/yUkAVwUXDKnE8kEjQf62" alt=""><figcaption><p>Driver Hub Appearing as "Control Hub in Recovery Mode"</p></figcaption></figure>

Occasionally, the Driver Hub may show as a "Control Hub in Recovery Mode" after **fully** powering on and connected via USB to the REV Hardware Client. &#x20;

To fix this issue you will need to perform a [factory reset on the Hub](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/pages/EOcma2BhlfeDqYqIj2NG#performing-a-factory-reset-to-the-driver-hub.).

### "App Not Installed" Error

{% hint style="warning" %}
Please ensure your Driver Hub and Robot Controller App are fully updated before proceeding.&#x20;
{% endhint %}

The following error in the Driver Station App can occur when the date/time is incorrect on the Driver Hub:

On the homepage the FTC Driver Station app can report an "app not installed" error after updating the OS and the app. This can also cause the Driver Hub to not allow you to open the FTC Driver Station app. To fix this do the following:

1. Remove the Driver Station app icon on the home page by clicking and dragging to the X icon
2. Drag the new icon from the app drawer on the home screen. The app drawer is accessed by swiping up on the home screen of the device.

### Android Permissions Lock Out

If the FTC Driver Station app is locked out due to android permissions, a factory reset of the Driver Hub should resolve this issue. Please power on the device, then follow the steps below to perform a factory reset:

1. Tap the "Setting" icon
2. Tap the "System" icon
3. Tap "reset options"
4. Tap "erase all data" (factory reset)

### Battery Installation

To install the battery, place it with the REV Logo facing out and the -/+ located near the contacts for the device. Add on the rear door and screw in using the included M3 hardware.

![A battery that is properly installed](/files/hIY7tGIHizMdsmcElRiP)

### Digitizer Lines

Due to variances in the manufacturing process related to screen digitizer installation, some Driver Hubs have minor visible digitizer lines on the screens when the device is powered off. These lines are more prevalent in some units than others, but the presence or absence of digitizer lines does not impact the performance of the touch screen or unit in any way. Please contact us at <mark style="color:blue;"><support@revrobotics.com></mark> if you have any concerns about your specific unit.

### Connecting to Control Hub

{% hint style="danger" %}
Information in this flowchart is for the initial bring up of connecting the Control Hub with a Driver Hub. For issues with intermittent connection or periodic connection drops please check out the information below this flowchart.
{% endhint %}

<figure><img src="/files/FFKR2vUb8PrJX6euuIoT" alt=""><figcaption></figcaption></figure>

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
* **Does the the Driver Hub connect to the Control Hub until a mechanism is run?**&#x20;
  * Certain mechanisms draw enough power from the Control Hub to put a strain on the battery. If you notice a drop in displayed voltage when you start a code, or when a particular mechanism is run, this may be indicative of a brown out condition. Other indicators include:&#x20;
    * The Driver Hub throwing errors about power to the system
    * The Driver Hub making a disconnect sound
    * The voltage on the Driver Hub showing 9 volts or lower when running code&#x20;
    * Motors running at lower speeds then what they have been set to run
  * To remedy this issue check out our instructions on [proper battery care.](https://www.revrobotics.com/rev-31-1302/)&#x20;

{% hint style="warning" %}
If the Control Hub SSID is not shown in the list of available Wi-Fi networks, try manually entering the Control Hub SSID on the Driver Hub to see if that allows you to connect.

If no networks are shown at all, you should reboot the Driver Hub. See [Most Common Issues](#most-common-issues) section.
{% endhint %}

If you are still experiencing connection issues, once you have gone through the flowchart and worked on addressing the potential root of connection issues describe in the list above, start looking for patterns in the behavior. How often does this behavior appear? Are there certain things that happen around the same time the disconnects happen? The following list provides some ideas on what sort of patterns you might see:

* The Driver Hub connects to Wi-Fi and the Control Hub when a team member takes it home but doesn't connect consistently at school.
* The Driver Hub connects to the Control Hub until you start driving the robot around.

{% hint style="success" %}
Correlation does not equal causation of an event but is useful to take note of for further troubleshooting
{% endhint %}

### Performing a Factory Reset to the Driver Hub.&#x20;

1. Power on the Driver Hub and find the Settings application.<br>

   <figure><img src="/files/P8GN7foxLbGw61puD0yf" alt=""><figcaption><p>Driver Hub Home Screen</p></figcaption></figure>
2. Click Settings and scroll down to System, then tap System.
3. Once you are in System, find "Reset Options".
4. Press "Erase all data (factory reset)". Keep in mind this will erase all applications, files, images, and anything else you have stored on your Driver Hub.

### Still Need Assistance?

Contact REV Support with details of the troubleshooting information you have collected such as the answers to the questions above and the outcome of your troubleshooting thus far. It will also help to send logs or other diagnostic data to REV Support.&#x20;

If you encounter any of these issues below, please email <support@revrobotics.com>

* Device freezes on boot, then restarts the boot process in a loop
* Device freezes on boot and never gets into the OS, even after a hard reboot
* Charging and Power issues persist after multiple [battery calibrations ](/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md#battery-calibration)

{% hint style="info" %}
Need help getting the Log Files to send to REV Support? See [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more information.
{% endhint %}

### Wi-Fi immediately turning off on the Driver Hub

If you are having trouble getting the Wi-Fi to stay on or turn on, it is likely that your Driver Hub is experiencing a failure of the built-in Wi-Fi chip. This most often presents as the Driver Hub’s Wi-Fi no longer functioning and also not staying turned “on” under the device’s settings.

Since this failure is caused by physical damage to the Wi-Fi Chip, we highly suggest using the [Driver Hub Repair Service (REV-31-1596-RFB)](https://www.revrobotics.com/rev-31-1596-rfb/) to purchase a repair for your Driver Hub. If you are still within the warranty period, or have any questions about the Repair Service, please email our support team at <support@revrobotics.com>.&#x20;
