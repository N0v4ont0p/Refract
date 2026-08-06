> Source: https://docs.revrobotics.com/duo-control/sensors/intro-to-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/intro-to-sensors.md).

# Introduction to Sensors

## **Sensor Basics**&#x20;

When starting out many of the robot actions can be accomplished by turning on a motor for a specific amount of time. Eventually, these time-based actions may not be accurate or repeatable enough. As battery power drains while the robot is running and mechanisms wearing in through use can all affect time-based actions. Fortunately, there is a way to give feedback to the robot about how it is operating by using sensors; devices that are used to collect information about the robot and the environment around it.&#x20;

Sensors provide information that allows you to program the robot to use this information to perform specific actions. This allows the robot to perform at its best and in a repeatable manner. A few scenarios that can benefit from a sensors information are listed below.

### **Scenarios where a sensor is needed:**

* The robot needs to autonomously move to a specific location and stop there.
* The robot needs to move forward at a green signal and stop moving at a red signal.
* The robot has an arm that needs to be prevented from rotating too far or it may damage other parts of the robot.
* The robot needs to stop 1 meter away from an opaque wall.
* The robot needs to be able to tell how many game objects it is currently holding inside its hopper.

## Different Sensor Types and Uses

![Control Hub ports](/files/w3fvbo7UNj26uS06E4zE)

In the REV Robotics Control System sensors are classified as **basic**, **intermediate**, or **advanced**. This division among sensors is based on programming complexity. **Basic sensors** can typically be coded using a if/else statement. **Intermediate sensors,** like the Color Sensor or Encoders, require a higher level understanding of programming. **Advanced sensors** require an advanced knowledge of programming. Visions sensors and using the Inertial Measurement Unit (IMU) are considered advanced.&#x20;

### Basic

In the REV Robotics Control System, both [**Analog** ](/duo-control/sensors/analog.md)and [**Digital** ](/duo-control/sensors/digital.md)sensors are considered basic sensors.

Digital sensors provide **binary** information: information that can take one of two possible values or states. These states are represented in programming languages as: **TRUE/FALSE** or **1/0**. Electrically, these states are usually represented as two voltages: a **High** voltage and a **Low** voltage. For REV Hubs, High is 3.0V and Low is 0V.&#x20;

A touch sensor is a common digital sensor. It has two states: pressed and not-pressed.

Analog sensors provide a range of information with an almost infinite set of values, instead of just two. These values are usually represented in programming languages as decimal numbers. Electrically, these values are represented as voltage. REV Hubs can measure voltages on the analog ports between 0V and 5.0V.&#x20;

Depending on the sensor, the reported voltage can represent anything that can't be represented by two digital states. A potentiometer is a common analog sensor that reports the angle of an attached shaft as voltages.

{% hint style="info" %}
*Some sensors in the REV Control System are capable of running up to 5V. To learn more about sensor voltage visit the pages of the individual sensors!*
{% endhint %}

The table below gives the basic usage scenarios for analog and digital sensors

| Digital                                                                                             | Analog                                                                                                                                         |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Gives feedback as either on or off. This type of sensor is ideal for setting limits of a mechanism. | Gives feedback as a proportional voltage range. This type of sensor is ideal for knowing exactly where a mechanism is, like a dial on a radio. |

#### Digital Sensors&#x20;

* Touch Sensor: A sensor with a button. The button press can be used to trigger actions like stopping motors.
* Magnetic Limit Switch: A sensor that detects magnetic fields. When there is sufficient field strength of either magnetic pole detected the sensor is triggers and a limit of movement can be established.&#x20;

#### Analog Sensors

* Potentiometer: A sensor that senses the angular position of a shaft.

### Intermediate&#x20;

[**I2C**](/duo-control/sensors/i2c.md) sensors are considered intermediate because they give feedback through two-way communication with a robot controller. These types of sensors allow for more complex data to communicate to the robot, such as color values of an object.&#x20;

* Color Sensor: A sensor capable of sensing colors and proximity of objects.&#x20;
* 2m Distance Sensor: A sensor typically used to detect the distance from the sensor to other opaque objects.&#x20;

All REV Robotics motors contain a built-in intermediate-level sensor called an Encoder. An [**Encoder**](/duo-control/sensors/encoders.md), in the context of robotics, is a type of digital sensor that converts rotary motion into digital signal. These type of sensors require “decoding” to get this information into a usable form. The Control Hub and Expansion Hub have built in decoding through the “Encoder Ports” under the motor ports.

### Advanced

Advanced sensors, in the REV Control System, are considered advanced as they rely on complex coding and information from other sensors in order to work effectively. Both the IMU and vision sensors require higher level code in order to decipher information being received from the sensor.&#x20;

| Vision                                                                                                                                                               | IMU                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gives feedback as images to the robot controller. These types of sensors require the use of image processing software, like VuForia, to use to their full potential. | The IMU incorporates three sensors: a 3-axis accelerometer, a 3-axis gyroscope, and a 3-axis geomagnetic sensor. This sensor can be used to determine orientation and location of the robot. |
