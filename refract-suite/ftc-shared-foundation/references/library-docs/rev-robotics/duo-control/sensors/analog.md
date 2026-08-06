> Source: https://docs.revrobotics.com/duo-control/sensors/analog.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/analog.md).

# Analog

## Analog Sensor Basics

Analog sensors can report an almost infinite number of states unlike digital sensors that report only two states. As the state of the sensor changes, the voltage reporting back to the robot changes as well. Think of a dimmer switch, the brightness of the lights in the room depends on where the slider or knob is positioned along the scale of potential positions. As the knob is adjusted the voltage level adjusts proportionally and the light continuously changes to the output from the knob. &#x20;

{% hint style="success" %}
Can you think of anything that acts like analog sensors around your household? Here are some we thought of: scale, thermometer, volume knob
{% endhint %}

Unlike the binary (low/high) status of digital sensors, analog sensors consider all numbers within a specific, given range. When using an analog sensor the actionable trigger will vary depending on the sensor. Consider a potentiometer attached to an arm, the output voltage (signal) will correspond to an angle of the arm. Knowing the angle of the arm then allows you to decide where to stop the arm along its travel path.&#x20;

{% hint style="info" %}
The Control Hub and Expansion Hub can read voltages ranging from 0V to 5V.&#x20;
{% endhint %}

REV Robotics offers analog sensor, known as a Potentiometer ([REV-31-1155](https://www.revrobotics.com/rev-31-1155/)). The Potentiometer can be used to sense or measure the angular position of a shaft.

## Wiring&#x20;

![](/files/-MFpy4npwGIxk0gowHcE)

Analog sensors connect to the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)), or Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)), via a JST PH 4-Pin Sensor Cable and the Analog Ports, shown in the image above. The color-coding of the analog ports in the image corresponds with each wire in the JST PH 4-Pin Sensor Cable. As a convention, the black wire is ground and the red wire is power. The blue (n) wire and white (n+1) wire are the communication (signal) channels along which the sensor sends feedback to the Hubs.

Each analog port on the Hub is capable of acting as two separate ports, thanks to the two channels of communication. This is why the ports are marked as 0-1 and 2-3. The image above shows which channel of communication corresponds with which port. The n+1 channel operates on odd-numbered ports 1-3 and the n channel operates on the even number ports 0-2.

Two analog sensors may be hosted on the same physical port using the Sensor Splitter Cable ([REV-31-1386](https://www.revrobotics.com/rev-31-1386/)). That being said, it is important to check the Pinout Diagram included in the datasheets for each individual sensor, as certain sensors, like the REV Potentiometer, use only one of the communication channels.

## Configuration

Before a sensor can be programmed it must be added to the Robot Configuration. The configuration file stores all configured devices in the Control Hub's "hardwareMap," which can be called to in the code to establish the line of communication between devices.&#x20;

The steps below show the basic configuration for analog devices. In the example, the Potentiometer will be configured as "Analog Input\`" on port 0.&#x20;

#### Step 1

While in the configuration select the **Analog Input Devices** option. This will open a screen that shows the four analog ports.

![](/files/-MFlh44cHXFDjx95r83N)

#### Step 2

In the drop-down menu for Port 0 select "Analog Input." After it is selected name the sensor. In this example, the Potentiometer is named "potentiometer," but any naming convention can be used.&#x20;

![](/files/-MFlj5YzRTH5KaHjq_ar)

#### Step 3&#x20;

When you have finished configuring the sensor hit **Done**. The app will return to the previous screen.

## Applications

How does the Potentiometer help a robot navigate the world around it? Potentiometers are most commonly used to measure the angle of an arm type joint. The angle measurement can be used to set or find a specific position along the arm joint.&#x20;

For more information on the REV Potentiometer's sensor specifications, coding examples, and more; click one of the links below to head to the sensor datasheets

|                                                                            |
| :------------------------------------------------------------------------: |
| [Potentiometer (REV-31-1155)](https://docs.revrobotics.com/potentiometer/) |
