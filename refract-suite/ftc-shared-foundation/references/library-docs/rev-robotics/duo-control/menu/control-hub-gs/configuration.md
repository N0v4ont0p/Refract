> Source: https://docs.revrobotics.com/duo-control/menu/control-hub-gs/configuration.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/control-hub-gs/configuration.md).

# Next Steps

Being able to connect to the Robot Controller Console, connect a Driver Station to a Control Hub, and the basics of wiring different actuators and sensors is just the start!&#x20;

This section focuses on the next steps for using the REV Control System, including getting started with programming and best practices for managing the Control Hub and Slim Batteries.&#x20;

## Getting Started with Programming &#x20;

Now that the Control Hub is setup, it is ready to start programming to control a robot.

Hello Robot, available for [Blocks](/duo-control/hello-robot-blocks/welcome.md) and [OnBot Java](/duo-control/hello-robot-java/welcome.md), will walk you through the basics of getting started moving motors, using sensors, and programming a basic drivetrain!

#### Before you program:

In order for the Control Hub to properly communicate with hardware components, you must perform a two part process known as hardware mapping. One of the most important, and commonly forgotten steps, when getting started programming is the creation of the configuration file, which is the first part of the hardware mapping process.&#x20;

A properly created configuration file, defines each hardware component with a unique name and a port type and number. After attaching hardware components to the Hub, use the Driver Station application to create a configuration, before beginning to program.&#x20;

![](/files/-M_w9VuqOatKGRtqwaGG)

{% hint style="info" %}
For more information on the important of hardware mapping and how to configure your robot please see the [Hello Robot - Configuration](/duo-control/hello-robot-blocks/configuration.md) page.&#x20;
{% endhint %}

## Adding a Expansion Hub&#x20;

Depending on the application more motor, sensor, or servo ports maybe needed. If your robot needs more motors adding an Expansion Hub might be necessary. Adding an Expansion Hub adds the same amount of hardware ports as one Control Hub (an additional four motor ports, six servo ports, and all the sensor ports) to the system.&#x20;

{% hint style="info" %}
For more information on how to add a secondary Expansion Hub please visit our [Adding an Expansion Hub ](/duo-control/menu/adding-more-motors/adding-an-expansion-hub.md)page.&#x20;
{% endhint %}

## Managing the Control Hub&#x20;

The Control Hub and Expansion Hub are field upgradable devices. When new software is released with new features, bug fixes, and season specific changes users can update the device themselves. Checking for software updates at the start of September and then about every 6-8 weeks is recommended.&#x20;

To check for software updates you can use the [REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client/).

{% hint style="info" %}
Information on updating various pieces of software for the Control Hub, Expansion Hub, and Driver Hub can be found in the Updating and Managing section on the left hand list.&#x20;
{% endhint %}

## Slim Battery Best Practices

To maintain and care for your battery, reference the general best practices on the 12V Slim Battery ([REV-31-1302](https://www.revrobotics.com/rev-31-1302/)) product page or the information below. This includes how to properly store, charge, and care for your battery on the long term.

All rechargeable batteries have a finite lifespan. Factors that affect lifespan include the number of discharge/charge cycles and the average loading of the battery. The following best practices can help maximize the lifespan of your battery:

* Charge rate
  * Minimum: 1.5A
  * Maximum: 3.0A
  * Recommended: 1.8A or 2.0A
* Do not overcharge
  * Disconnect the battery from the charger once it indicates a full charge.
  * Typical charge time does not exceed 2 hours.
  * Do not charge a battery that hasn't been discharged significantly.
    * For example, running the robot under minimal load for a few minutes will not significantly discharge the battery.
* Minimum no-load voltage: 9.0V
  * Discharging the battery past 9.0V can reduce the lifespan of the battery and can permanently damage the cells.
  * Periodic dips below 9.0V when under load is expected and OK.
    * For example, don't forget to unplug your battery after you are finished running the robot and don't run your robot until it completely stops responding!
* Temperature
  * Let the battery cool before and after charging.
  * The battery may feel warm after heavy loading or after charging. This is normal.
