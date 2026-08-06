> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting.md).

# Driver Hub Battery Troubleshooting

{% hint style="info" %}
It is generally recommended to separate the battery from the Driver Hub for long term storage, such as over the summer or a similar long break.
{% endhint %}

{% hint style="info" %}
In this troubleshooting guide we will use specific language to describe different ways of power cycling the Driver Hub.

**Turn Off/Power Off** - Long press (1-2 seconds) the power button so that a drop down menu appears, then tap "power off" on the screen

**Hard Reboot** - Hold power button for at least 10 seconds and do not touch anything on the screen. Once the green LED light turns off and the screen goes dark, release the power button, and the hard reboot is complete.
{% endhint %}

## Most Common Issues

### Battery Installation

To install the battery, place it with the REV Logo facing out and the -/+ located near the contacts for the device. Add on the rear door and screw in using the included M3 hardware.

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FUOOiQ4S2QcMWmVoSmeQ8%2Fuploads%2F2LIa6NMNoDuG2jTnjSdA%2FDriver_Hub_Battery_Placement_In_Hub_Working.png?alt=media&#x26;token=ad37c002-b2f1-49b5-80be-438b7ead1ad4" alt=""><figcaption><p>A battery that is properly installed</p></figcaption></figure>

### Battery Calibration&#x20;

We are aware of some Driver Hubs that were shipped from the factory without having their batteries properly calibrated. If you are experiencing power issues such as trouble charging or being unable to power on the device, try the following:

1. Plug Driver Hub into a charger without battery (Please use the charger that came with the Driver Hub to ensure a proper calibration)
2. Turn on Driver Hub and verify that the Driver Hub reports 100% battery charge. If the Driver Hub does not report 100% charge, you may be using a PD charger and not the one that came with the Driver Hub.
3. Install battery into Driver Hub while device is still on and charging
4. Charge for at least 8 hours and do not remove battery or charge cable
5. Remove Driver Hub from Charger
6. Hard Reboot&#x20;

### Battery Verification&#x20;

After completing a battery calibration, use these steps to verify that your battery is functioning as expected.

1. Place the battery in a Driver Hub and verify that the Driver Hub turns on.&#x20;
2. Shake the Driver Hub with the screen still on and verify that the battery does not lose physical contact with the Driver Hub's contacts. If power drops, please see [instructions for Unexpected Shutdown above](#most-common-issues).
3. Take note of the indicated battery charge level, charge the Driver Hub for 10 minutes, and verify that the battery charge level increased.&#x20;
4. If you have the time, perform a full charge/discharge cycle with the battery to verify that the battery behaves normally.

### Foam Tape Installation

1. Cut foam tape into small pieces, approximately 2 inches or less long. The foam tape recommended is approximately 1/4 inch or less wide and 1/16 inch or less thick
2. Foam tape will be applied inside the battery case, opposite battery contacts and below the ridge that the battery door sits within.
3. Stick foam strip in the middle, both side to side and top to bottom, of the vertical surface opposite the battery contact switch
4. Press foam strip down firmly to make sure it sticks.
5. Battery
   1. Insert battery by inserting top of battery towards foam, and gently squeezing battery towards foam with thumb until battery can easily drop into battery case.
   2. Continue to push the battery down until it is flush in the case.
6. Done

### Battery Lockout Recovery

The Driver Hub can enter a "safe" mode intended to protect the battery. This safe mode, also referred to as a battery lockout, keeps your battery and Hub safe by preventing the battery from overcharging and/or keeping the Driver Hub on continuously. This most often happens when the Driver Hub’s battery charge is too low or the device has not been charged for a long period of time.

Symptoms of this lockout mode include:

* The Driver Hub only turning on while plugged to the USB without the battery installed.&#x20;
* The Driver Hub appearing to not charge the battery after being connected for long periods of time.
* The Driver Hub not turning on with the battery installed and the USB connected.&#x20;
* The Driver Hub not turning on, but the red Status LED lighting up while on USB.&#x20;

To get the Driver Hub out of the Safe Mode, please follow these steps:&#x20;

1. With the battery installed, plug the Driver Hub into its original USB-A Wall Charger and the Orange USB-A  to USB-C Cable. The [Battery Status LED should blink red](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/led-blink-codes#battery-status-led) at this time, indicating that power is being received.
2. Let the battery charge for 5 minutes then unplug the Driver Hub. Wait just a moment then plug the Hub back in.&#x20;
3. Check to see if the Driver Hub is out of lockout by pressing the power button while the Driver Hub is charging.&#x20;
   * If the "Battery charging icon" (red or white) appears on the screen proceed to Step 4.&#x20;
   * If you do not see the battery charging icon, please repeat Step 2. Typically, it takes 4-5 cycles of short charging to recover a Driver Hub from this lockout state.&#x20;
4. Let charge while completely off for 8 hours to complete a [battery calibration](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting#battery-calibration)[.](#battery-calibration)

### Still Need Assistance?

Contact REV Support with details of the troubleshooting information you have collected such as the answers to the questions above and the outcome of your troubleshooting thus far. It will also help to send logs or other diagnostic data to REV Support.&#x20;

If you encounter any of these issues below, please email <support@revrobotics.com>

* Device freezes on boot, then restarts the boot process in a loop
* Device freezes on boot and never gets into the OS, even after a hard reboot
* Charging and Power issues persist after multiple [battery calibrations ](#battery-calibration)

{% hint style="info" %}
Need help getting the Log Files to send to REV Support? See [Downloading Log File](/duo-control/managing-the-control-system/downloading-log-file.md#downloading-without-a-connection) for more information.
{% endhint %}
