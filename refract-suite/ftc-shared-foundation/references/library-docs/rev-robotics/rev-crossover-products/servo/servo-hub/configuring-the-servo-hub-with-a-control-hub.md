> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/configuring-the-servo-hub-with-a-control-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/configuring-the-servo-hub-with-a-control-hub.md).

# Configuring the Servo Hub with a Control Hub

{% hint style="success" %}
You must be running Robot Controller App and Driver Station App version 10.0 to use a Servo Hub.
{% endhint %}

## Setting Servo Hub IDs <a href="#accessing-the-configuration-utility" id="accessing-the-configuration-utility"></a>

{% hint style="info" %}
Servo Hub IDs should be set while the Servo Hub is disconnected from a Control Hub OR before powering the robot on. Servo Hubs previously connected to a robot may need to be power cycled before changing IDs.
{% endhint %}

By default, the Servo Hub's ID should be set to 3. This can be changed by connecting the Servo Hub directly to the REV Hardware Client using a USB-C cable. The Servo Hub will appear in the Hardware List as shown below:

<figure><img src="/files/09Ji7ZuQgZuJV8QNf9Mu" alt=""><figcaption></figcaption></figure>

The "CAN ID" is the individual ID for the Servo Hub.

{% hint style="warning" %}
Each Servo Hub and Expansion Hub must have a unique ID before being able to complete the configuration process.&#x20;
{% endhint %}

<figure><img src="/files/K4uFZJP9TMSKm8zgaXmn" alt=""><figcaption></figcaption></figure>

The CAN ID can be set between 1-10 for FTC. After choosing the ID, click "Set CAN ID".

{% hint style="info" %}
Expansion Hubs default to ID 1 or 2.
{% endhint %}

<figure><img src="/files/mE0MAEjtfLYJSEJMB9Jp" alt=""><figcaption></figcaption></figure>

The new Servo Hub ID is not set!

## Accessing the Configuration Utility <a href="#accessing-the-configuration-utility" id="accessing-the-configuration-utility"></a>

1. Select the menu in the stop right corner of the Driver Station app. Then select Configure Robot.

<figure><img src="/files/18yQnR2D9weMGlJ8ZiCr" alt=""><figcaption></figcaption></figure>

2. In the Available configurations page, select New.

<figure><img src="/files/uF8Qp82FyZvkyppNjn7y" alt=""><figcaption></figcaption></figure>

3. In the USB Devices in configuration page select the Control Hub Portal. **Note:** If you have an Expansion Hub connected via USB it will appear as an Expansion Hub Portal.

<figure><img src="/files/MHlTpThdeRMPDEtCxYiR" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Pressing "**Scan**" on an existing configuration may result in the already named devices being erased. A new configuration file is needed when adding a camera or Expansion Hub over USB.
{% endhint %}

4. All connected Servo or Expansion Hubs using RS485 will appear within the menu of the portal. If you are using multiple Servo Hubs, they can be identified by their ID number.

**Menu while using a single Servo Hub:**&#x20;

<figure><img src="/files/BfS2XXh1qac8AVGVYiDg" alt=""><figcaption></figcaption></figure>

**Menu while using multiple Servo Hubs:**

<figure><img src="/files/65anvNe2Ll00C3up4EJw" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This menu will appear the same if the Servo Hub is connected to another Servo Hub or an Expansion Hub connected using RS485.&#x20;
{% endhint %}

## Configuring Servos

1. Select the Servo Hub where you are adding servos

<figure><img src="/files/4a8fPiqSfqvK6bB1FHFx" alt=""><figcaption></figcaption></figure>

2. Select the "Servos" option

<figure><img src="/files/IcrhxOWDTUMPrHIAYuZg" alt=""><figcaption></figcaption></figure>

3. This will open a configuration menu similar to what is used for motors and sensors!

<figure><img src="/files/hBHfwmxBOopcAr2T3ZkU" alt=""><figcaption></figcaption></figure>

4. Select your desired option from the dropdown menu

<figure><img src="/files/sZfRvYCf5k0VsIeQ42ZS" alt=""><figcaption></figcaption></figure>

5. Assign the device an appropriate name

<figure><img src="/files/lTNWWd4Vf01CIDG362DF" alt=""><figcaption></figcaption></figure>

6. Click "Done" once all names are entered to return to the main Servo Hub menu

<figure><img src="/files/ILzOQI2YBYwdR4giEb1v" alt=""><figcaption></figcaption></figure>

7. Click "Done" again on to return to the list of all connected Hubs
