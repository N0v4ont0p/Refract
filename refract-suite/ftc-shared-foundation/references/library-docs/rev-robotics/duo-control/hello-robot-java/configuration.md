> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/configuration.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/configuration.md).

# Setting up a Configuration

Before we can truly dive into programming our robot, we need to help our robot's brain, the Control Hub, to know what is connected to it. Through the configuration process we can tell the Control Hub which port sensors, motors, servos, and any other connected devices can be found.&#x20;

This is one of the most important steps to always complete BEFORE you can start programming!

## The Importance of Configuration

While every REV Control Hub is the same, the robots being controlled by the Control Hub are not. Each Control Hub has the same number of motor ports, servo ports, digital ports, and the like, but how you may utilize these ports varies from system to system. For instance, a Color Sensor V3 may be plugged in to I2C Bus 1 on one person's Hub, but another might use the same bus to host a 2m Distance Sensor.&#x20;

While the Control Hub may know there is a device attached to a port, it doesn't instinctively know which information needs to be transferred back for use in an [OpMode](/duo-control/hello-robot-blocks/where-to-program/what-is-an-opmode.md). To help our robot out we need to complete a process called hardware mapping. This is a two step process that includes creating our configuration file using the Driver Hub and calling the hardware map within our OpMode.&#x20;

When using Blocks, this second step is handled for the user by the tool. However, in OnBot Java it is up to us as the programmer to create our variables and assign an external hardware unit.&#x20;

<figure><img src="/files/mMj9ilS4mBlePSAN7hvZ" alt=""><figcaption><p>Example of the hardwareMap in OnBot Java</p></figcaption></figure>

<details>

<summary>Click to Learn More about the Configuration File</summary>

The configuration file is a readable file created by the user through the Driver Station Application. When creating a configuration file users are required to assign each device to a port, select the type of device it is from options provided by the SDK, and give it a **unique** name.&#x20;

It's important to name each device something recognizable and distinguishable!&#x20;

Once a configuration file is saved or activated the robot will restart. This restart is so the SDK can read the file, determine what devices are present, and add the devices to the hardwareMap class.

</details>

## Configuring Common Hardware Devices

### Accessing the Configuration Utility

* Select the menu in the stop right corner of the Driver Station app. Then select Configure Robot.

<figure><img src="/files/JgZakWbzNUkC6aXOrtyE" alt="" width="563"><figcaption></figcaption></figure>

* In the Available configurations page, select New.&#x20;

<figure><img src="/files/KJXSuPkBS9YEaQJ5NQ7z" alt="" width="563"><figcaption></figcaption></figure>

* In the USB Devices in configuration page select the Control Hub Portal.&#x20;

  **Note:** If you have an Expansion Hub connected it will appear as an Expansion Hub Portal.&#x20;

<figure><img src="/files/LFctZmVJJkjlAXfB2E27" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="danger" %}
Pressing "**Scan**" on an existing configuration may result in the already named devices being erased. A new configuration file is needed when adding a camera or Expansion Hub.
{% endhint %}

* Within the Hub Portal select the device you want to configure. In this use case, select the Control Hub.<br>

  &#x20;**Note:** if you have an Expansion Hub connected to a Control Hub, the Expansion Hub will also appear as a configurable device in the portal.

<figure><img src="/files/DSHvIQ7CJreEEgisMDj3" alt="" width="563"><figcaption></figcaption></figure>

* This will bring you to the page shown in the image. From here you can configure motors, servos and sensors that you are using. Follow through the rest of the guide to figure out how to configure devices that will be used in the Test Bed section.&#x20;

  **Note:** The way that Digital and Analog devices are configured versus how I2C devices are configure differ significantly. This is because each physical I2C port is a different bus that can host multiple different sensors. For more information on the different types of sensors check out the [sensors](/duo-control/sensors/intro-to-sensors.md) section.&#x20;

<figure><img src="/files/WE40zA7EVP1FjRZqd74V" alt="" width="563"><figcaption></figcaption></figure>

### Configuring Hardware&#x20;

The following section will show how to configure components that will be used in the Test Bed. The hardware type and names have been chosen in consideration for the Hello World lesson plan. Users should heed notes within the steps to consider when creating configuration files for other instances.&#x20;

{% tabs %}
{% tab title="Motor" %}

#### Configuring a Motor

* Select Motors.

<figure><img src="/files/XwRDuSGAOq0xrzvp5usT" alt=""><figcaption></figcaption></figure>

* The Motor page will allow you to configure all four motor ports on the Hub. On Port 0 open the drop down menu and select REV Robotics Core Hex Motor.&#x20;

  **Note:** In your configuration file you should configure the motor ports to the type of motor you are using.&#x20;

<figure><img src="/files/KwYsFDmqOTXxMom4ewOf" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/BrFQQT4b4QUoKTyLHdC7" alt=""><figcaption></figcaption></figure>

* Name the motor test\_motor. Select done.&#x20;

  **Note:** remember when naming hardware in the configuration file that the REV Control System is Case Sensitive.&#x20;

<figure><img src="/files/Y7ZN5o0jhACovSFTPCEo" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Servo" %}

#### Configuring a Servo

* Select Servos.

<figure><img src="/files/Z0oRxDJO1bqI9MSIGc0o" alt=""><figcaption></figcaption></figure>

* The Servo page will allow you to configure all six servo ports on the Hub. On Port 0 open the drop down menu and select Servo.

  **Note:** REV Servos can be configured as a Servo or a Continuous Rotation Servo. The type of device a servo is configured as should correspond with the mode the sensor is in. For more information on Sensor modes visit the [Sensor section](https://docs.revrobotics.com/15mm/actuators/servos).&#x20;

<figure><img src="/files/9SN9i3BDkIHzdfcmYx2U" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/CuzqSFYB7PbgAkfspwkh" alt=""><figcaption></figcaption></figure>

* Name the servo test\_servo. Select **done.**&#x20;

  **Note:** remember when naming hardware in the configuration file that the REV Control System is Case Sensitive.&#x20;

<figure><img src="/files/CPjYg19t3B98zJKBfAcw" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Digital Device" %}

#### Configuring a Digital Device

* Select **Digital Devices.**&#x20;

<figure><img src="/files/zZUjBm5aPFS9U8WvGF6U" alt=""><figcaption></figcaption></figure>

* The Digital Devices page will allow you to configure all eight digital ports on the Hub. On **Port 1** open the drop down menu and select Digital Device .

  **Note:** Touch Sensors must always be configured on odd number ports. <br>

  **Note:** Touch Sensors can be configured as a REV Touch Sensor or a Digital Device. In the FTC SDK the type of device it is configured as changes the classes and methods that can be used.&#x20;

<figure><img src="/files/yoNW7125pp2tYfZUkbDD" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/zDjrPdRMKfLBY6WZ6zxn" alt=""><figcaption></figcaption></figure>

* Name the motor test\_touch. Select don&#x65;**.**&#x20;

  **Note:** remember when naming hardware in the configuration file that the REV Control System is Case Sensitive.&#x20;

<figure><img src="/files/LBufOrKV58xPKXigiRl8" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="I2C Device" %}

#### Configuring an I2C Device

* Select I2C Bus 0.

<figure><img src="/files/IhyQVDAv8cYjqVtA1Tds" alt=""><figcaption></figcaption></figure>

* Select Add.&#x20;

  **Note:** Each I2C Bus can host more than one I2C sensor as long as the I2C addresses do not conflict. Bus 0 will always host the internal IMU. For more information on I2C sensors visit the [I2C section](/duo-control/sensors/i2c.md).&#x20;

<figure><img src="/files/rewll8x32rxcrHJ905r0" alt=""><figcaption></figcaption></figure>

* On Port 1, which was created in the previous step,  open the drop down menu and select REV Color Sensor V3.&#x20;

  **Note:** If you are using Color Sensors V1 or V2 select REV Color/Range Sensor. For more information on configuring with the REV Color Sensors visit the [Color Sensor Datasheets](https://docs.revrobotics.com/color-sensor/).&#x20;

<figure><img src="/files/rAUC263pd8LbDeai1xNT" alt=""><figcaption></figcaption></figure>

* Name the motor test\_color. Select **done.**&#x20;

  **Note:** remember when naming hardware in the configuration file, that the REV Control System is Case Sensitive.&#x20;

<figure><img src="/files/ZI8hc0C7ej9RsAJJ8Djv" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Saving the Configuration File

* Hit Done twice until you reach the USB Devices in configuration page. On the USB Devices in configuration page hit Save.

<figure><img src="/files/GSPqnDXLfmCJRW6Jckk3" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/8SG12pv60GgdPO9SF1pL" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/ejihqwDsgXWvqB8Zg3Ev" alt=""><figcaption></figcaption></figure>

* Name the configuration **helloRobotTest** and then select Ok.

  **Note:** The FTC SDK does not force you to abide by a naming convention for but it is common to name configurations in lowerCamelCase.&#x20;

<figure><img src="/files/lPWFyyAtEfdWIa9NdY3E" alt=""><figcaption></figcaption></figure>

* Press back to activate the saved configuration. Your Robot Controller will restart once you activate a new configuration.&#x20;

<figure><img src="/files/tjG6PzRYdubkC9qW5AYR" alt=""><figcaption></figcaption></figure>
