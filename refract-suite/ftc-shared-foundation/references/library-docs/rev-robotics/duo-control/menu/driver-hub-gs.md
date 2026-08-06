> Source: https://docs.revrobotics.com/duo-control/menu/driver-hub-gs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/driver-hub-gs.md).

# Getting Started with Driver Hub

After receiving the Driver Hub it is advised to unbox the device, plug the Driver Hub in to charge over USB-C, and power on the Driver Hub. Below is the initial bring up process of the Driver Hub. &#x20;

### Required Materials

* Driver Hub ([REV-31-1596](https://www.revrobotics.com/rev-31-1596/))
* USB-A to USB-C Cable
* USB-A Wall Charger

{% embed url="<https://youtu.be/RPcZOzUOZHg>" %}

## Battery Installation

To install the battery place it with the REV Logo out and the -/+ located near the contacts for the device. Add on the rear door and screw in using the included M3 hardware.&#x20;

![](/files/-MeWhoP-8ghsKkUj-wlG)

{% hint style="success" %}
After setup, optimize your Driver Hub's battery life by following our [Battery Calibration](/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md#battery-calibration) instructions! This process will ensure your Driver Hub and battery are tuned correctly after setting up.\
\
Until then, we recommend allowing the battery to charge over USB-C or keeping the Driver Hub plugged into a power source during these next steps.
{% endhint %}

## Setting up the Driver Hub

When the Driver Hub is first powered up, or a factory reset is performed, an initial set up process is needed. Start by selecting next on the main screen to continue.

![](/files/-Ma4Kw2BqMS8pPcVdkH1)

Select a local Wi-Fi network that has access to the internet, enter in the password for that network if required, and select next.

![](/files/-Ma4PodMhgHwQZ3eK7pv)

Time zone and date of the device are set by the local Wi-Fi network. Confirm these settings are correct before proceeding by the Next button.

![](/files/-Ma4RSciGsmofJRRwXyN)

Initial set up is complete! Select Finish to operate the Driver Hub.

![](/files/-Ma4SIHuWsaCR0ZRYjkx)

### Initial Update

After setting up the Driver Hub, the Software Manager application will open. Select the Update All button to start the download and installation of software updates for the Driver Hub.

{% hint style="info" %}
The updates can take several minutes to complete. Make sure the Driver Hub is charged or plug in the Driver Hub during the updating process.

**Note:** Restricted networks, such as at a school or business, may prevent the Driver Hub from being able to update.
{% endhint %}

![](/files/-Ma5AKbvt2TL3KEjzCSb)

{% hint style="success" %}
Now the Driver Hub is [ready to connect to a Control Hub](/duo-control/menu/control-hub-gs/driver-station-pairing-to-control-hub.md)!\
\
Don't forget to optimize your Driver Hub's battery by following our [Battery Calibration](/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md#battery-calibration) instructions after you are done with your session today!
{% endhint %}

## Navigating the Driver Station Application

Once the Driver Hub is connected to a Control Hub, you will have access to the entire Driver Station Application interface. Like any application, understanding the major components that make up the Driver Station Application interface, will maximize your ability to utilize the application efficiently. Consider the following components:

<figure><img src="/files/GO7lM6qvWNehVcbaeTxo" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/B0P5PuyOSr27gOcHCn77" alt=""><figcaption></figcaption></figure>

| 1  | Initialize, start, and stop programs | Only available when a program has been selected.                                                                                                                                                                                         |
| -- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2  | Telemetry display                    | <p>Displays telemetry outputs. </p><p></p><p>Displays any system warnings and error codes</p>                                                                                                                                            |
| 3  | Active configuration                 | <p>Displays which configuration file is currently active. </p><p></p><p>If this section says <strong>\<no config file></strong> you will need to activate or <a href="/pages/-MJhSpWDdVL6coLFLgIi">create a configuration file</a>. </p> |
| 4  | Network information                  | Displays Control Hub SSID Name, signal strength, and ping time.                                                                                                                                                                          |
| 5  | Gamepad connections.                 | See [Connecting Gamepads](/duo-control/menu/driver-hub-gs.md#connecting-gamepads) for more information.                                                                                                                                  |
| 6  | Autonomous drop down menu            | Drop down menu that displays all autonomous programs saved on the Control Hub.                                                                                                                                                           |
| 7  | Teleop drop down menu                | Drop down menu that displays all teleop programs saved on the Control Hub.                                                                                                                                                               |
| 8  | System power display                 | Displays the amount of battery voltage powering the robot, when connected to a Control Hub.                                                                                                                                              |
| 9  | Settings drop down menu              | Access settings, configure the robot, restart the robot, check to see if your system meets competition inspection requirements and more.                                                                                                 |
| 10 | Practice Timer                       | A built in timer that can be used to to practice for different portions of a match.                                                                                                                                                      |

### Tips and Tricks&#x20;

<figure><img src="/files/AnQxodBGdjj08cUPbLMo" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/0G2r09dNnTpEDf2iYB5s" alt=""><figcaption></figcaption></figure>

If you tap on area 4, it will switch to displaying the link speed and signal strength. It will go back to showing the signal strength and ping time if you tap it again.

The smaller number in area 8 is the lowest voltage that the Driver Station has observed from the Robot Controller. If you tap area 8, the lowest voltage will be reset to the current voltage.

### Battery Best Practices

We suggest the following best practices to help optimize and preserve the health of your Driver Hub’s battery. It is not necessary to strictly follow these recommendations, however, consistently operating outside of these guidelines may lead to decreased performance.

* If you are not using your Driver Hub any time soon, it is best to turn it off to minimize the battery usage.&#x20;
* Avoid temperature extremes, both high and low, when charging, using, or storing Driver Hub batteries. Elevated temperatures can accelerate degradation of the battery and can lead to significant safety risks. Although your Driver Hub is expected to get warm while charging, you should remove the Driver Hub from the charger if it becomes uncomfortably hot. It is also recommended to not charge the Driver Hub when the battery is 32°F/0°C or lower in order to best persevere battery health.
* If you need a faster charge, using a PD 3.0 fast charger would decrease the charge time but is not recommended for continuous charging. To get the best battery health, We recommend charging your Driver Hub before the battery reaches 20% charge. It is also best to remove your Driver Hub from the charger within 24 hours of reaching 100%, this would be even more impactful if you are using a PD 3.0 fast charger.&#x20;
* Avoid use or storage of Driver Hubs in high-moisture environments, and avoid mechanical damage such as puncturing and impacts. Remove the battery from the Driver Hub for long term storage, such as over summer break. Store it in a dry temperature controlled environment around room temperature. To best preserve battery health, avoid storing the battery with low or no charge.

## Connecting Gamepads

The Driver Station Application allows for the connection of two gamepads. When working with the Driver Hub these gamepads can be plugged into any of the three USB 2.0 ports. Once the gamepads are plugged in, you will need to initialize them. For the following example we will use PS4 controllers, such as the Etpark Wired Controller for PS4 ([REV-39-1865](https://www.revrobotics.com/rev-39-1865/)).

<figure><img src="/files/MsgM2SEKH2GuAFgqLQRs" alt=""><figcaption></figcaption></figure>

To initialize the gamepad that will act as User 1 (gamepad1, in code) press the **options** button and the **`X`**&#x62;utton on the gamepad at the same time. To initialize User 2 ( gamepad2, in code) press the **options** button and the **`O`** button at the same time.&#x20;

{% hint style="info" %}
For the Logitech F310 Gaming Controller and Xbox 360 Controller for Windows, press **start** and **A** at the same time to initialize User 1 and **start** and **B** at the same time to initialize User 2.&#x20;
{% endhint %}
