> Source: https://docs.revrobotics.com/duo-control/sensors/i2c/imu.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/i2c/imu.md).

# IMU

## IMU Basics&#x20;

![](/files/-MACxSFVQFnWa9fkbKDx)

Each REV Robotics Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)), and Expansion Hubs ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) purchased before December 2021, has a built in IMU, or inertial measurement unit. The IMU combines measurements from multiple internal sensors to compute its current orientation. It can also provide the angular velocity (how fast the IMU is rotating along each axis).

{% hint style="info" %}
**Expansion Hubs shipped AFTER December 1st, 2021 no longer include an internal IMU**
{% endhint %}

The data used by the IMU to track the orientation includes the rotation along each axis, and the forces of acceleration along each axis. Using the acceleration forces allows the IMU to detect the direction of gravity, preventing drift in the pitch and roll readings. Only the heading will drift slowly, as small inaccuracies build up over time.

### Product Specifications&#x20;

* I2C Address: 0x28
* Port: 0&#x20;

### Identifying your Hub's internal IMU

Originally, Control Hubs and Expansion Hubs shipped with the Bosch BNO055 IMU. However, as of **September 2022**, the Control Hub's IMU was replaced with the Bosch BHI260AP IMU.

To see which IMU your Control Hub has, navigate to the Manage page within the Program & Manage menu, either from the Driver Hub, REV Hardware Client, or [web interface](https://docs.revrobotics.com/duo-control/hello-robot-java/where-to-program#web-browser).&#x20;

When you create a new configuration file, the correct IMU type should be automatically detected for I2C port 0, and added to the configuration.

## IMU Interfaces

Version 8.1 of the FTC Robot Controller app adds a new universal IMU interface for Blocks and Java programming, which supports both the BNO055 IMU and the BHI260AP IMU. The BNO055 IMU can also be used from the legacy `BNO055IMU` interface.

### The universal `IMU` interface

The universal `IMU` interface added in version 8.1 of the FTC Robot Controller app provides robot-centric orientation and angular velocity values. You can specify the exact orientation of the Control or Expansion Hub on your robot, and the interface will convert the raw values from the IMU into robot-centric values. This simplifies how you use the IMU's values, and prevents problems when the hub is not mounted with the REV Robotics logo facing upwards.

All values from the `IMU` interface are in the Robot Coordinate System, in which the origin is inside your robot, the Z axis points towards the ceiling, the Y axis points straight ahead through the front of your robot (whatever you define the front to be), and the X axis points out the right side of your robot. This coordinate system is right-handed, which means that if you point a typical right thumb in the same direction as the axis, rotation in the same direction that the fingers curl is considered positive.

The `IMU.getRobotYawPitchRollAngles()`method on the `IMU` interface provides the robot's orientation in a simplified format of yaw, pitch, and roll angles. Most teams should use this method to get the robot's orientation.

* **Yaw** (also known as heading) is the measure of rotation along the robot's Z axis, or the side-to-side lateral rotation of the robot.
* **Pitch** is the measure of rotation along the robot's X axis, or the front-to-back rotation of the robot.
* **Roll** is the measure along the robot's Y axis, or the side-to-side tilt of the robot.

### The legacy `BNO055IMU` interface

The `BNO055IMU` interface has several disadvantages compared to the universal `IMU` interface.

* It can only be used with Control Hubs and Expansion Hubs that contain the original BNO055 IMU.
* It only works reliably when the Hub is mounted flat, with the REV Robotics logo pointed upwards.
* The values it provides are relative to the Hub, not the Robot.
* You have to manually specify the axes order for the orientation angles (ZXY is recommended for typical use cases).

The coordinate system used for the `BNO055IMU` interface is defined like this:

* The X axis  runs from the bottom of the hub, near the servo ports, to the top of the hub, where the USB ports are.
* The Y axis runs from the sensor ports on the right to the motor ports on the left.&#x20;
* The Z axis points upwards through the REV Robotics logo.

{% hint style="info" %}
*To learn more on how to configure the IMU check out the*[ *I2C* ](/duo-control/sensors/i2c.md#configuring-i-2-c-sensors)*introduction page.*
{% endhint %}

## Protecting the IMU from ESD

During the 2023-24 FTC season, *FIRST* and REV Robotics received reports of teams experiencing an unexpected reset of their IMU after an electrostatic discharge (ESD) event.  A new version of the Control Hub's Operating System (1.1.4) has been released, which introduces an update to reduce the frequency of these resets on Control Hubs with a BHI260AP IMU.

Below are additional tips for reducing the effects of ESD or conflicts with the internal IMU that may prevent similarly:

1. **Prepare your robot with ESD Mitigation Techniques** - [*FIRST* has a guide on Managing Electrostatic Discharge](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html) with additional tips and tricks for you to try, including installing a [Resistive Grounding Strap (REV-31-1269)](https://www.revrobotics.com/rev-31-1269/) on your robot.
2. **Ask what measures your Event Hosts have taken to mitigate ESD at your event** - Contact your event’s host in advance to see if they plan to [treat the playing fields with Staticide.](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html#step-1-treating-the-tile-floor-with-anti-static-spray-event-hosts-only)
3. **Ensure all of your team’s code references the IMU correctly**&#x20;
4. **Check that your battery has a secure connection to your robot and is fully charged** - We have found that Unexpected IMU Resets have also occurred due to poor battery connection or low voltage.
5. **Have a plan to reset your IMU** – Teams who rely on the IMU can add human-triggered actions, like pressing a button to reinitialize the IMU, to their Driver-Controlled robot code. Teams may find it beneficial to align their robots with the playing field tile seams (to ensure alignment) prior to starting the reinitialization action.
