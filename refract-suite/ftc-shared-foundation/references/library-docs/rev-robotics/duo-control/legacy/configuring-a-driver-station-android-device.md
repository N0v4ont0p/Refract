> Source: https://docs.revrobotics.com/duo-control/legacy/configuring-a-driver-station-android-device.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/legacy/configuring-a-driver-station-android-device.md).

# Configuring Your Android Devices

When using Android Phones as your Robot Controller and Driver Station devices, there are several steps you need to take in order to get the phones up and running. This section will go through the process of installing a Driver Station and Robot Controller application onto a phone using the REV Hardware Client, as well as the process for renaming your Wi-Fi direct network. &#x20;

{% hint style="info" %}
For information on how to pair a configured Android phone with a Control Hub please see our [Driver Station Pairing to Control Hub ](/duo-control/menu/control-hub-gs/driver-station-pairing-to-control-hub.md)article in the Getting Started with Control Hub section.&#x20;
{% endhint %}

## **Installing the Driver Station Application**

### **Android Developer Options**

In order to install the Driver Station Application onto and Android phone, the phone's developer settings and USB debugging options need to be turned on.&#x20;

The developer options on Android Devices are hidden within the phone as a default. Different phone manufactures have different ways of accessing the developer options. However, once the developer options are available in the phone's settings, the steps for activating USB debugging and development settings are similar.&#x20;

{% hint style="danger" %}
Before moving forward it is advised to look up where the developer options on your Android Device are located. For Motorola users, the [Motorola Support Page ](https://motorola-global-portal.custhelp.com/app/answers/detail/a_id/160067/~/developer-options)has information on how to unlock the developer options.
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
The following steps will go through how to install the Driver Station Application via the REV Hardware Client. It is possible to install the application via the app store or via the [FTC GitHub repository](https://github.com/FIRST-Tech-Challenge/FtcRobotController) as well.
{% endhint %}

{% embed url="<https://youtu.be/wpE50vjXvdM>" %}

Connect the Android Device to a PC with the [REV Hardware Client](https://www.revrobotics.com/software/#REVHardwareClient) installed.

Startup the REV Hardware Client. Once the Android Device is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Android Device.&#x20;

![](/files/-MGnQndSMGYRPbtPXYaW)

After selecting the Connected Hardware the Update tab will pop up.  Under **Driver Station App** select Download.

![](/files/-MGnTeLef0pI_QyCR3qO)

Once the Driver Station App has downloaded, select Install.&#x20;

![](/files/-MGnX5ZLpzALgiEYbFM3)

When the application installation has completed the status for the Driver Station App will change to "Up-to-Date."

![](/files/-MGnXY2dmMqPZ43PKYai)

## Renaming Your Smartphone&#x20;

Part of the process for configuring your Android Device is changing the Wi-Fi Direct network. The intent of this process is to give your Robot Controller and Driver Station phones an identifiable and unique network name. This is a general best practice when working with networks, but is also a requirement for FIRST programs.&#x20;

{% hint style="info" %}
FIRST has specific naming convention requirements for Robot Controllers and Driver Stations. Please check your programs game manual for more information on what you need to name your devices.&#x20;
{% endhint %}

{% hint style="danger" %}
Before moving forward it is advised to look up where the Wi-Fi direct options on your Android Device are located. This guide goes over where to make this change on the Moto E5.
{% endhint %}

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Locate settings in the application list for your Android Device. Select the settings application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | <img src="/files/-M_bY3PyW5Q2VPqxFZS5" alt="" data-size="original"> |
| <p>In the settings application, look for the <strong>Wi-Fi</strong> or <strong>Network & Internet settings</strong> and select it. </p><p></p><p><strong>Note:</strong> the naming convention for the network settings will vary depending on device model and manufacturer </p>                                                                                                                                                                                                                                                                                                 | <img src="/files/-M_bYyZrXhuodC-C6V0C" alt="" data-size="original"> |
| <p>In the network settings on Moto E5, scroll to the bottom and look for <strong>Wi-Fi preferences</strong>. Select Wi-Fi preferences. </p><p></p><p><strong>Note:</strong> on other phone models Wi-Fi Direct settings will likley be found in a different place. Please look up the Wi-Fi direct information for your phone model.</p>                                                                                                                                                                                                                                         | <img src="/files/-M_bbbiarvZnKIINIs4t" alt="" data-size="original"> |
| In **Wi-Fi preferences** select **Advanced**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <img src="/files/-M_bi2EQFNTgtk3bfrDL" alt="" data-size="original"> |
| Select **Wi-Fi Direct**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <img src="/files/-M_fGcnysExaHIP8DisE" alt="" data-size="original"> |
| In the **Wi-Fi Direct** settings select the three vertical dots in the upper right hand corner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | <img src="/files/-M_fHfYcTOLZI_qpJ71A" alt="" data-size="original"> |
| Select **Configure device**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | <img src="/files/-M_fIqhj3vlDGgSjqy_I" alt="" data-size="original"> |
| <p>Change the name of your device to something unique and identifiable. For this example the device has been renamed to REVDemo\_DS. It is also good to check the <strong>Wi-Fi Direct Inactivity timeout</strong> and confirm it is set to <strong>Never disconnect</strong>. Hit 'save' to confirm your changes. </p><p></p><p>Note: If you are competing in robotics competitions you may need to follow a Wi-Fi Direct naming convention set by the competition rules. Check any relative documentation to confirm that you are following the correct naming convention.</p> | <img src="/files/-M_fKjCsjXXCanEhEKHl" alt="" data-size="original"> |
