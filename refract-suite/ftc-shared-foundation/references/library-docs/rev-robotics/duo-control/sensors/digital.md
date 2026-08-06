> Source: https://docs.revrobotics.com/duo-control/sensors/digital.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/digital.md).

# Digital

## Digital Sensor Basics&#x20;

The information from digital sensors comes in two states, also known as binary states. The binary state of a digital sensor is either low or high. This is similar to a light switch being on or off.&#x20;

{% hint style="info" %}
Binary information, or states, can be thought of as an "either/or"; a light switch can either be in an 'on' state or an 'off' state. On/off, 0/1, low/high, and FALSE/TRUE are all different ways of presenting binary information. In programming FALSE/TRUE is used most often.
{% endhint %}

The main difference between a light switch and a digital sensor is that a digital sensor has a **default state.** The default state is typically its **inactive states**. Digital sensor datasheets typically will report the sensors **active behavior**, either **active-low** or **active-high**. With an active-high behavior, when the digital sensor is triggered (or activated) you can detect a change in code from a "logic" low state to a "logic" high state.&#x20;

{% hint style="info" %}
Logic Level represents the voltage difference between the signal and ground of the Control and Expansion Hub's sensor ports. Both Hubs and REV Sensors operate on a 3.3V logic level. This means the digital sensor needs an operating voltage of 3.3V for use with the Hub. If you are looking to use a 5V digital sensor you will need a Logic Level Converter. See [Using 5V Sensors](/duo-control/sensors/5v-sensors.md) for more information.
{% endhint %}

This change is from FALSE to TRUE and you can program your robot to act accordingly with this information. Check the datasheet for the sensor you are using to determine its **active behavior** is and how the behavior is reported in your code.

REV carries the following digital sensors:&#x20;

* Touch Sensor ([REV-31-1425](https://www.revrobotics.com/rev-31-1425/))&#x20;
* Magnetic Limit Switch ([REV-31-1462](https://www.revrobotics.com/rev-31-1462/))

## Wiring&#x20;

![](/files/-MFCZ3Dv8p1rIz65EqkF)

Digital sensors connect to the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)), or Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)), via a JST PH 4-Pin Sensor Cable and the Digital Ports, shown in the image above. The color-coding of the digital ports in the image corresponds with each wire in the JST PH 4-Pin Sensor Cable. Following convention, the black wire is ground and the red wire is power. The blue **(n)** and white **(n+1)** wires are the communication (signal) channels along which the sensor sends feedback to the Hubs.

Each digital port on the Hub is capable of acting as two separate ports, thanks to the two channels of communication. This is why the ports are marked as 0-1, 2-3, etc. The image above shows which channel of communication corresponds with which port. The n+1 channel operates on odd-numbered ports 1-7 and the n channel operates on the even number ports 0-6.

Two digital sensors may be hosted on the same physical port using the Sensor Splitter Cable. That being said, it is important to check the Pinout Diagram included in the datasheets for each individual sensor, as certain sensors, like the Touch sensor, use only one of the communication channels.

## Configuration

Before a sensor can be programmed it must be added to the Robot Configuration. The configuration file stores all configured devices in the Control Hub's "hardwareMap," which can be called to in the code to establish the line of communication between devices.&#x20;

The steps below show the basic configuration for digital devices. In the example, the Touch Sensor is configured as "REV Touch Sensor" on port 1.

#### Step 1

While in the configuration select the **Digital Devices** option. This will open a screen that shows the eight digital ports.

![](/files/-MFlko31-elGGRKsI4w6)

#### Step 2

In the drop-down menu for Port 1 select "REV Touch Sensor." After it is selected name the sensor. In this example, the Touch Sensor is named "touch," but any naming convention can be used.&#x20;

![](/files/-MFlphSSelWsHWIc6tbc)

#### Step 3&#x20;

When you have finished configuring the sensor hit **Done**. The app will return to the previous screen&#x20;

{% hint style="info" %}
For more information on configuring the Touch Sensor or Magnetic Limit Switch go to the sensor datasheets.&#x20;
{% endhint %}

## Applications

How do digital sensors help a robot navigate the world around it? The REV Touch Sensor and REV Magnetic Limit Switch are most commonly used as **limit switches**! Limit switches can help detect when a mechanism, like an arm and/or a lift, has reached its physical limits. Installing a limit switch can help keep robot mechanisms from overextending and breaking. They can also be used to zero out the position of motor encoders to further reduce mechanical failure.&#x20;

For more information on how to use the REV Digital Sensors as limit switches, sensor specifications, coding examples, and more; click one of the links below to head to the sensor datasheets

|                                                                                            |
| :----------------------------------------------------------------------------------------: |
|          [Touch Sensor (REV-31-1425) ](https://docs.revrobotics.com/touch-sensor/)         |
| [Magnetic Limit Switch (REV-31-1462)](https://docs.revrobotics.com/magnetic-limit-switch/) |
|      [Digital LED Indicator (REV-31-2010)](https://docs.revrobotics.com/rev-31-2010/)      |
