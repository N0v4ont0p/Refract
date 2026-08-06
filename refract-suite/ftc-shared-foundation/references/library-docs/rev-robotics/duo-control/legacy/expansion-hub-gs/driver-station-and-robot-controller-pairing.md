> Source: https://docs.revrobotics.com/duo-control/legacy/expansion-hub-gs/driver-station-and-robot-controller-pairing.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/legacy/expansion-hub-gs/driver-station-and-robot-controller-pairing.md).

# Driver Station and Robot Controller Pairing

When you first receive your Expansion Hub, you will have to install the Driver Station and Robot Controller Applications and pair (link) your Driver Station (Android Device) to your Robot Controller. The following sections of the page will walk through how to install the applications and how to connect the Driver Station to the Robot Controller's Network.&#x20;

## **Install Applications**&#x20;

### **Android Developer Options**

In order to install the Driver Station Application or Robot Controller Application onto and Android phone, the phone's developer settings and USB debugging options need to be turned on.&#x20;

The developer options on Android Devices are hidden within the phone as a default. Different phone manufactures will have different ways of accessing the developer options. However, once the developer options are available in the phone's settings, the steps for activating USB debugging and development settings are similar.&#x20;

{% hint style="danger" %}
Before moving forward it is advised to look up where the developer options on your Android Device are located. For Motorolla users, the Motorolla Support Page has information on how to unlock the developer options.
{% endhint %}

|                                                                                                                      |                                                                     |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Open the Android Devices settings                                                                                    | <img src="/files/-MGnOO0_68a5pk5k8QLx" alt="" data-size="original"> |
| Scroll to the bottom of the settings, where the unlocked developer options are available. Open the developer options | <img src="/files/-MGnOyKijL413uuk7knF" alt="" data-size="original"> |
| At the top of the developer options page is an on/off switch. Turn the developer options on.                         | <img src="/files/-MGnPDBGGK5c7fDjSZ-5" alt="" data-size="original"> |
| The device will open a confirmation message. Select 'OK.'                                                            | <img src="/files/-MGnPPXxOtGHr_j_mX0M" alt="" data-size="original"> |
| Scroll through the developer options until you find the Debugging section. Turn USB Debugging on.                    | <img src="/files/-MGnPd1do5isMW8cmfRW" alt="" data-size="original"> |
| Another confirmation message will appear, click 'OK.'                                                                | <img src="/files/-MGnPvVMgVSi6cRbmCQv" alt="" data-size="original"> |

USB debugging is now on! You can move on to the steps for installing the application.

### Driver Station Application&#x20;

{% hint style="info" %}
The following steps will go through how to install the Driver Station Application via the REV Hardware Client. It is possible to install the application via the FTC GitHub repository as well.
{% endhint %}

Connect the Android Device to a PC with the REV Hardware Client installed.

Startup the REV Hardware Client. Once the Android Device is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Android Device.&#x20;

![](/files/-MGnQndSMGYRPbtPXYaW)

After selecting the Connected Hardware the Update tab will pop up.  Under **Driver Station App** select Download.

![](/files/-MGnTeLef0pI_QyCR3qO)

Once the Driver Station App has downloaded, select Install.&#x20;

![](/files/-MGnX5ZLpzALgiEYbFM3)

When the application installation has completed the status for the Robot Controller App will change to "Up-to-Date."

![](/files/-MGnXY2dmMqPZ43PKYai)

### Robot Controller Application&#x20;

{% hint style="info" %}
The following steps will go through how to install the Robot Controller Application via the REV Hardware Client. It is possible to install the application via the [FTC GitHub repository](https://github.com/FIRST-Tech-Challenge/FtcRobotController) as well.
{% endhint %}

Connect the Android Device to a PC with the REV Hardware Client installed.

Startup the REV Hardware Client. Once the Android Device is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Android Device.&#x20;

![](/files/-MGnQndSMGYRPbtPXYaW)

After selecting the Connected Hardware the Update tab will pop up.  Under **Robot Controller App** select Download.

![](/files/-MGnZAiOc7Sd_clC9WP_)

Once the Robot Controller App has downloaded, select Install.&#x20;

![](/files/-MGn_xwJz3sYGpauvwwP)

When the application installation has completed the status for the Robot Controller App will change to "Up-to-Date."

![](/files/-MGnYy9ImkUOExlPbtDX)

## Driver Station and Robot Controller Pairing&#x20;

{% hint style="warning" %}
You should update your Driver Station(DS) and Robot Controller(RC) phones to the latest app version in order to use the Expansion Hub controller. The minimum compatible version is 3.1 released on May 10th, 2017
{% endhint %}

Please ensure that the Driver Station and Robot Controller phones are properly configured and paired. Refer to the latest pairing and troubleshooting instructions provided by in the [FTC Control System Wiki](https://github.com/ftctechnh/ftc_app/wiki).
