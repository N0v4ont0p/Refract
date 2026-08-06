> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/centerstage-2023-2024/upgrades.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/centerstage-2023-2024/upgrades.md).

# Upgrades

## Mecanum Drive

Upgrading to a [Mecanum Drivetrain](https://www.revrobotics.com/rev-45-2470/) (REV-45-2470) allows for new kinds of movement giving the robot the ability to strafe side-to-side across the field.

{% hint style="info" %}
For Mecanum Drive each wheel has an individual motor!
{% endhint %}

<figure><img src="/files/KHWQPJUT0lth6h1OmAcF" alt=""><figcaption><p>REV's Mecanum Drivetrain Kit V2</p></figcaption></figure>

The FTC Starter Kit V3 can be [upgraded to the Mecanum Drivetrain V1 following this guide.](/duo-build/ftc-starter-kit-mecanum-drivetrain.md)&#x20;

### Upgrading from the FTC Starter Kit V3 to Mecanum Drivetrain V2:

The following additional parts are needed:

* [UltraPlanetary Gearbox Kit & HD Hex Motor](https://www.revrobotics.com/rev-41-1600/) - QTY 2&#x20;
* [Ultra 90 Degree Gearbox](https://www.revrobotics.com/rev-41-2080/) - QTY 4
* [75mm Mecanum Wheel Set](https://www.revrobotics.com/rev-45-1655/) - QTY 1 (set of 4)
* [M3 x 6mm HexCap Screws 50 Pack](https://www.revrobotics.com/M3-Hex-Cap-Screws/) - QTY 1

[Full build instructions can be found here!](/duo-build/mecanum-drivetrain-v2.md)

### Example Mecanum Drive Program

How a Mecanum Drivetrain is programmed largely depends on the driver's preference for how the controller is configured. If your team is new to Mecanum, we have a [demo code and breakdown available for Blocks. ](/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-refined.md)

{% hint style="info" %}
This example code uses a different configuration than the Starter Bot's provided code! Please make sure to update both your program and the configuration file through the Driver Station.
{% endhint %}

## Adding Independent Wrist Movement

Using the [provided program](/ftc-kickoff-concepts/centerstage-2023-2024/programming-teleop.md#programming-teleop-blocks) the wrist only moves when one of the preset arm/wrist buttons on the controller is pressed. Your team may decide to add independent wrist movement for more refined control.&#x20;

Below are a couple examples for adding wrist movement using the existing variables:&#x20;

{% hint style="warning" %}
These examples are meant to replace the use of presets in favor of manual control of the arm and wrist.
{% endhint %}

### Blocks:

Example 1:&#x20;

<figure><img src="/files/PRhw5DgGqWt9HohZ0akh" alt=""><figcaption></figcaption></figure>

This option functions similar to the gripper using the two preset positions. If "Up" on the Dpad is held down then the wrist will move and stay in the up position. When released, it will return down.&#x20;

Example 2:&#x20;

<figure><img src="/files/8z35Es6r9KHBToRL5dly" alt=""><figcaption></figcaption></figure>

This option breaks the movement apart to move up or down when the matching button is pressed once on the Dpad. The button does not need to be held for it to remain in the set position.&#x20;

### OnBot Java:&#x20;

Example 1:

```java
        //Indepedent Wrist 
         if (gamepad1.dpad_up) {
          wrist.setPosition(wristUpPosition);
        } else {
          wrist.setPosition(wristDownPosition);
        }
```

Example 2:

```java
        //Indepedent Wrist 
         if (gamepad1.dpad_up) {
          wrist.setPosition(wristUpPosition);
        } 
         if (gamepad1.dpad_down) {
          wrist.setPosition(wristDownPosition);
        }
```
