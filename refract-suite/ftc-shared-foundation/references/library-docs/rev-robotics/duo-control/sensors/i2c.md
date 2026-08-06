> Source: https://docs.revrobotics.com/duo-control/sensors/i2c.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/i2c.md).

# I2C

## I2C Sensor Basics&#x20;

I2C is a common electronic communication standard that allows a **host** (the Hub) to communicate with multiple **devices** on the same I2C bus.&#x20;

Each I2C port on a Hub is its own **I2C bus**. Every I2C device has a unique address, a number that is normally fixed by the manufacturer. All of the devices on an individual I2C bus must have a unique address so that the host can communicate with one device at a time. If two devices have the same address, such as when using two of the same kind of sensors, they must be used on different I2C buses otherwise the communication channels conflict.&#x20;

{% hint style="info" %}
While I2C is technically a digital communication protocol, it is more advanced than the simple on/off style of basic digital sensors. I2C sensors require software drivers for the information from a follower (sensor) to be interpreted by the leader (Hub).
{% endhint %}

There are three I2C sensors within the REV system: the Inertial Measurement Unit (IMU), Color Sensor ([REV-31-1557](https://www.revrobotics.com/rev-31-1557/)), and 2m Distance Sensor ([REV-31-1505](https://www.revrobotics.com/rev-31-1505/)).&#x20;

There is an IMU built into the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)), which is connected to I2C bus 0. Expansion Hubs shipped BEFORE 12/01/2021 also feature a built in IMU.

### Logic Level and 3rd Party I2C Sensors

Logic Level represents the voltage difference between the signal and ground of the Control and Expansion Hub's sensor ports. Both Hubs and REV Sensors operate on a 3.3V logic level.&#x20;

Therefore, to use a digital sensor it needs an operating voltage of 3.3V for use with the Hub. If you are looking to use a 5V I2C sensor you will need a Logic Level Converter.&#x20;

See [Using 5V Sensors](/duo-control/sensors/5v-sensors.md) for more information or check out our [sensor compatibility chart](/duo-control/sensors/5v-sensors/sensor-compatibility-chart.md).&#x20;

## Wiring

![](/files/-MFq-WJhA4JId_hdXUnn)

I2C sensors connect to the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)), or Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)), via a JST PH 4-Pin Sensor Cable and the I2C buses, shown in the image above. The color-coding of the I2C buses in the image corresponds with each wire in the JST PH 4-Pin Sensor Cable. As a convention, the black wire is ground and the red wire is power. The blue (SCLn) wire and white (SDAn) wire are the communication signals for each I2C bus on the Hubs.

Sensor feedback to the Hub works differently for the I2C sensor than it does for Analog or Digital sensors. With the Analog and Digital Sensors, only one communication channel needs to be used by an individual sensor. In contrast, an I2C sensor sends different kinds of information over the SDA (white) and SCL (blue) wires. Since the I2C is transferring more complex data to the Hub then Analog or Digital sensors, there has to be a component of harmonization, or consistency, as the data moves from the sensor to the Hub. The **SCL (Serial Clock)** channel provides consistency by acting as a clock line and time-stamping the data provided by the **SDA (Serial Data)** channel.

While it is possible to host more than one I2C sensor on the same bus, there are a couple of factors to take into account. The Hub keeps track of the information from different sensors by considering the sensor's address in relation to the data being sent. When two sensors have the same address, like the REV Color Sensor V3 and the 2m Distance Sensor, they cannot be hosted on the same bus. Check the sensor datasheets for all I2C sensors to determine what sensors can and cannot be hosted on the same bus.

Currently, REV Robotics does not produce a cable or breakout board to connect two sensors to one I2C port on the Hub. A custom cable will need to be made in order to wire more than one I2C to the Hub.

{% hint style="info" %}
The internal IMU is hosted on I2C bus 0. See the configuration section below to learn more about configuring a secondary sensor on bus 0.
{% endhint %}

## Configuration

Before a sensor can be programmed it must be added to the Robot Configuration. The configuration file stores all configured devices in the Control Hub's "hardwareMap," which can be called to in the code to establish the line of communication between devices.&#x20;

In order to function, all FTC legal I2C devices have drivers installed into the SDK. With regards to configuration, this means that the device has to be set to the drop-down menu item that corresponds with its drivers. Visit the datasheet for the sensor you are trying to configure to see how to configure it.&#x20;

The steps below shows a basic configuration for I2C devices. The I2C Bus 0 hosts the internal[ IMU](/duo-control/sensors/i2c/imu.md) sensor within the Hubs. In this example, the Color Sensor V3 is being added to Bus 0 as well.&#x20;

#### Step 1

While in the configuration select the **I2C Bus 0** option. This will open a screen that shows the IMU. Press the Add button to add the Color Sensor to this bus.

<div><figure><img src="/files/E49zuYGFi9dNjGK5vgKd" alt=""><figcaption></figcaption></figure> <figure><img src="/files/YVjr6FhoHMZ2tzy90Tc4" alt=""><figcaption></figcaption></figure></div>

#### Step 2

&#x20;Select "REV Color Sensor V3" from the dropdown menu and name the device.

<div><figure><img src="/files/TnjrSa4GsN6cOCJSJNrX" alt=""><figcaption></figcaption></figure> <figure><img src="/files/ysQzD0civFpIyZQO7ju8" alt=""><figcaption></figcaption></figure></div>

#### Step 3&#x20;

When you have finished configuring the sensor hit **Done**. The app will return to the previous screen.

## Applications

How do I2C sensors help a robot navigate the world around it? The answer to this question is a bit more diverse than it is for Analog or Digital sensors.&#x20;

#### Color Sensors:

All three Color Sensors (V1-V3) sense color within a 2cm distance from the sensor. When mounted on the robot this can help in autonomous period tasks where robots have to decide between several different colored objects.&#x20;

#### 2m Distance Sensors:

While the Color Sensors have some proximity sensing capabilities, the 2m Distance Sensor is able to detect proximity with higher accuracy and reliability. When combined with odometry, the 2m Distance Sensor can help the robot navigate obstacles on the field during autonomous!

#### IMU:

The IMU has a built-in accelerometer, gyroscope, and magnetometer. There are a multitude of applications for the IMU within autonomous op modes:

* Use the Gyroscope to drive in the straight lines and turn during autonomous
* Use the Accelerometer in conjunction with the gyroscope to avoid drift and give an approximation of position/travel&#x20;
* Use the IMU with motor encoders to track and determine robot placement on a field&#x20;

For more information on the I2C sensor specifications, coding examples, and more; click one of the links below to head to the sensor datasheets

|                                                                                                                           |
| :-----------------------------------------------------------------------------------------------------------------------: |
|         [Color Sensor V3 (REV-31-1557)](https://docs.revrobotics.com/rev-crossover-products/sensors/color-sensor)         |
| [Color Sensor V2 (REV-31-1537)](https://docs.revrobotics.com/rev-crossover-products/sensors/color-sensor/discontinued/v2) |
| [Color Sensor V1 (REV-31-1154)](https://docs.revrobotics.com/rev-crossover-products/sensors/color-sensor/discontinued/v1) |
|            [2m Distance (REV-31-1505)](https://docs.revrobotics.com/rev-crossover-products/sensors/2m-distance)           |
