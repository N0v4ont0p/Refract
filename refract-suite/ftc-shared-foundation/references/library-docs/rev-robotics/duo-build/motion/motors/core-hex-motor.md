> Source: https://docs.revrobotics.com/duo-build/motion/motors/core-hex-motor.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/motors/core-hex-motor.md).

# Core Hex Motor

## Core Hex Motor Basics&#x20;

The Core Hex Motor ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) is a motor that features a 90 degree orientation and a female output shaft for maximum flexibility and ease of use. Insert any of the REV standard [5mm Hex Shafts](https://www.revrobotics.com/ftc/motion/bearings-linear-slides-pillow-blocks/) into or through the Core Hex Motor to create custom length motor output shafts. The Core Hex Motor has a built in magnetic quadrature encoder which is compatible with 5V or 3.3V logic level devices including the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)). &#x20;

![](/files/-M8Mau1m3YkY8a8rLOaT)

### Pinout

The Core Hex Motor uses a 2-pin JST-VH Connector for motor power and a 4-pin JST-PH for sensor feedback from the built-in encoder. For more information on using the cables and connectors included with the Core Hex Motor, see the [REV Control System - Cable and Connectors documentation](https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors). The image below has the pinout for the motor power and the encoder.

![](/files/-M_MCcUszaBq8eeo9Rmp)

### Product Specs

* Output Shaft: 5mm Female Hex
* Weight: 7 oz
* Voltage: 12V DC
* Free Speed: 125 RPM
* Stall Torque: 3.2 N-m
* Stall Current: 4.4 A
* Gear Ratio: 72:1
* Encoder Counts per Revolution
  * At the motor - 4 counts/revolution
  * At the output - 288 counts/revolution

## When to Use?

The general recommendation is to use the Core Hex motor for lighter duty arms and intakes.&#x20;

{% hint style="info" %}
*Visit the* [*Choosing and Actuator*](/duo-build/motion/actuators.md) *page to learn more about how the determine what type of actuator is correct for your mechanism.*
{% endhint %}

## How to Use?

{% hint style="info" %}
*To learn more about the built in encoders and wiring for the core hex motor visit the Control System Guide.*
{% endhint %}

### How to Mount the Core Hex Motor&#x20;

The Core Hex Motor has two faces for mounting on two sides of the motor. The combination of the Motion Pattern is clocked to different angles on each face giving twelve different motor angles. The images below exhibit a basic mounting structure for two of the twelve positions that are available.&#x20;

{% hint style="warning" %}
The images show a very basic mounting system. It is always advised to properly support elements of your robot with more 2 or more plastic brackets&#x20;
{% endhint %}

![](/files/-M8w-OcpkhH60EeMi9iI)

![](/files/-M8w-aUS2DZGHedGYMuR)
