> Source: https://docs.revrobotics.com/duo-control/menu/configuring-devices.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/configuring-devices.md).

# Configuring Devices

The configuration file is a readable file created by the user through the Driver Station Application. When creating a configuration file users are required to assign each device to a port, select the type of device it is from options provided by the SDK, and give it a **unique** name.

It's important to name each device something recognizable and distinguishable!

Once a configuration file is saved or activated the robot will restart. This restart is so the SDK can read the file, determine what devices are present, and add the devices to the hardwareMap class.

{% hint style="info" %}
Learn more about configuration by checking out our Hello Robot tutorial for [Blocks ](https://docs.revrobotics.com/duo-control/hello-robot-blocks/configuration)or [OnBot Java](https://docs.revrobotics.com/duo-control/hello-robot-java/configuration).
{% endhint %}

## Configuring Common Hardware Devices

### Accessing the Configuration Utility

* Select the menu in the stop right corner of the Driver Station app. Then select Configure Robot.

<figure><img src="/files/XI1zzxERVOPMtnWVQWVP" alt=""><figcaption></figcaption></figure>

* In the Available configurations page, select New.

<figure><img src="/files/y4I17pe7EPxA7X8ZtgIx" alt=""><figcaption></figcaption></figure>

* In the USB Devices in configuration page select the Control Hub Portal.

**Note:** If you have an Expansion Hub connected via USB it will appear as an Expansion Hub Portal.

<figure><img src="/files/StCZLcMxJktvaceUsA8R" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Pressing "**Scan**" on an existing configuration may result in the already named devices being erased. A new configuration file is needed when adding a camera or Expansion Hub.
{% endhint %}

* Within the Hub Portal select the device you want to configure. In this use case, select the Control Hub.

**Note:** if you have an Expansion Hub connected to a Control Hub via RS485, the Expansion Hub will also appear as a configurable device in the portal.

<figure><img src="/files/IA53r8SNRNOkxSSHNELH" alt=""><figcaption></figcaption></figure>

* This will bring you to the page shown in the image. From here you can configure motors, servos and sensors that you are using. Follow through the rest of the guide to figure out how to configure devices that will be used in the Test Bed section.

**Note:** The way that Digital and Analog devices are configured versus how I2C devices are configure differ significantly. This is because each physical I2C port is a different bus that can host multiple different sensors. For more information on the different types of sensors check out the [sensors](https://docs.revrobotics.com/duo-control/sensors/intro-to-sensors) section.

<figure><img src="/files/OdDLzsNyrML0oGHLtqTD" alt=""><figcaption></figcaption></figure>

### Configuring Actuators and Sensors

{% hint style="success" %}
Curious what sensors or devices are natively compatible with the Robot Controller App on the Control Hub? Check our [compatibility chart here](/duo-control/sensors/5v-sensors/sensor-compatibility-chart.md)!
{% endhint %}

This walkthrough provides an example of configuring each device type. This process will vary slightly depending on the part in use and decided name.

{% tabs %}
{% tab title="Motor" %}

#### **Configuring a Motor**

Select Motors.

<figure><img src="/files/S83UO0x1nvIoSJZr5aZo" alt=""><figcaption></figcaption></figure>

The Motor page will allow you to configure all four motor ports on the Hub. For this example, a REV Robotics Core Hex Motor is being configured to Port 0. Select the port and then the motor from the dropdown.&#x20;

<figure><img src="/files/IWZ4Z20Wc3pn9v8ZwvgR" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/xU22IzDkc7MvLB3yNbG2" alt=""><figcaption></figcaption></figure>

Name the motor then select done.

**Note:** When naming hardware in the configuration file the REV Control System is Case Sensitive.

<figure><img src="/files/uxypZUkglsXS556nZtwr" alt=""><figcaption></figcaption></figure>

Select **done** once all motors are added.
{% endtab %}

{% tab title="Servo" %}

#### **Configuring a Servo**

Select Servos.

<figure><img src="/files/dqVV17PFPGRPdxzfzxUs" alt=""><figcaption></figcaption></figure>

The Servo page will allow you to configure all six servo ports on the Hub. For this example, a servo is being added to Port 0.&#x20;

**Note:** REV Smart Robot Servos can be configured as a Servo or a Continuous Rotation Servo. The type of device a servo is configured as should correspond with the mode the sensor is in. For more information visit [our page on using the SRS Programmer to switch modes](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer).

<figure><img src="/files/QXvAoBg1OHM1IQmb2vzd" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/swAFX2puvbe7uILhGabp" alt=""><figcaption></figcaption></figure>

Name the servo and select **done.**

**Note:** When naming hardware in the configuration file the REV Control System is Case Sensitive.

<figure><img src="/files/CoLD0CsW2Lh5NzuTJX6p" alt=""><figcaption></figcaption></figure>

Select done once all servos are added.
{% endtab %}

{% tab title="Digital Device" %}

#### **Configuring a Digital Device**

Select **Digital Devices.**

<figure><img src="/files/V1VHGxfhQdi6Y4OupMcW" alt=""><figcaption></figcaption></figure>

The Digital Devices page will allow you to configure all eight digital ports on the Hub. For this example, a touch sensor is being configured to Port 1.

**Note:** Touch Sensors must always be configured on odd number ports.

**Note:** REV Touch Sensors can be configured as a REV Touch Sensor or a Digital Device. In the FTC SDK the type of device it is configured as changes the classes and methods that can be used.<br>

<figure><img src="/files/wXuimPb9pOl8ErJBLGhs" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/AjoyKqs0BIlm3yoC2oRB" alt=""><figcaption></figcaption></figure>

Name the sensor and select done.

**Note:** When naming hardware in the configuration file the REV Control System is Case Sensitive.

<figure><img src="/files/GPnxCpwZhBGO2eXJcamU" alt=""><figcaption></figcaption></figure>

Select done once all sensors are added.
{% endtab %}

{% tab title="I2C" %}

#### **Configuring an I2C Device**

Select I2C Bus 0.

<figure><img src="/files/0J3ewPBk3ylFJ8OSmTaq" alt=""><figcaption></figcaption></figure>

Select Add.

**Note:** Each I2C Bus can host more than one I2C sensor as long as the I2C addresses do not conflict. Bus 0 will always host the internal IMU. For more information on I2C sensors visit the [I2C section](https://docs.revrobotics.com/duo-control/sensors/i2c).

<figure><img src="/files/utAL5ZsZpyddzaGUnTuk" alt=""><figcaption></figcaption></figure>

On Port 1, which was created in the previous step, open the drop down menu and select the desired sensor. In this example, a REV Color Sensor V3 is being added.

**Note:** If you are using Color Sensors V1 or V2 select REV Color/Range Sensor. For more information on configuring with the REV Color Sensors visit the [Color Sensor Datasheets](https://docs.revrobotics.com/color-sensor/).

<figure><img src="/files/2KQ7m2CZCIfkHwkPRf9c" alt=""><figcaption></figcaption></figure>

Name the sensor and select done.

**Note:** When naming hardware in the configuration file, the REV Control System is Case Sensitive.

<figure><img src="/files/gWneSJc725YBFXZ6m5JL" alt=""><figcaption></figcaption></figure>

Select done once all sensors have been added.
{% endtab %}
{% endtabs %}

### Configuring RS485 Devices

#### Expansion Hub

{% hint style="info" %}
Configurations are unique to each Expansion Hub. A new configuration file must be created if the Expansion Hub is changed with a different one.
{% endhint %}

1. After creating a new configuration file, select the Control Hub Portal in the USB Devices menu.

<figure><img src="/files/fbk7kXgzqAWvb47ZaXBA" alt=""><figcaption></figcaption></figure>

2. An Expansion Hub connected via RS485 will appear here as a separate portal.

<figure><img src="/files/RByEoU9A6GADnqh95Bn2" alt=""><figcaption></figcaption></figure>

3. Once in the Expansion Hub's portal, devices can be configured the same as the Control Hub using the [directions above](#configuring-actuators-and-sensors). At the top of the menu, it will show if you are within the Expansion Hub or Control Hub's options.

<figure><img src="/files/4F0E9qa1J5PgkdiA1FPm" alt=""><figcaption></figcaption></figure>

Select Done once all devices are added.

#### Servo Hub

1. After creating a new configuration file, select the Control Hub Portal in the USB Devices menu.

<figure><img src="/files/ezLn3yrPpMi2plcOWlkh" alt=""><figcaption></figcaption></figure>

2. Select the Servo Hub you wish to configure. It will show the set ID number.

<figure><img src="/files/EhEyJUAQlp3S6UJMddqB" alt=""><figcaption></figcaption></figure>

3. Select **Servos.**&#x20;

<figure><img src="/files/EL0E4CDk12GLCTFX7wXa" alt=""><figcaption></figcaption></figure>

4. Servos will be configured the same as for a Control or Expansion Hub from here.

<figure><img src="/files/iqE18Fnkc4SFhy3fvaGI" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/rWpZrDDude0SJ9ZW2fSr" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/CW2BJSomVmM8Is9iRH8Y" alt=""><figcaption></figcaption></figure>

Select Done once all servos are added.

## Saving the Configuration File <a href="#saving-the-configuration-file" id="saving-the-configuration-file"></a>

* Hit Done twice until you reach the USB Devices in configuration page. On the USB Devices in configuration page hit Save.

<figure><img src="/files/pHPqy6UA1anupcgqXn9o" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/fvIykrA5LhbSbDw3z7wS" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/Kd0fjWtliTFy1Irb12VJ" alt=""><figcaption></figcaption></figure>

Name the configuration  then select Ok.

<figure><img src="/files/8b7QZfSAPYls6LvZWjiJ" alt=""><figcaption></figcaption></figure>

Press back to activate the saved configuration. Your Robot Controller will restart once you activate a new configuration.

The active configuration appears in the upper right on the configuration screen and on the main Driver Station screen.

<figure><img src="/files/w6Xf2NxGwlrQX3AseiGH" alt=""><figcaption></figcaption></figure>
