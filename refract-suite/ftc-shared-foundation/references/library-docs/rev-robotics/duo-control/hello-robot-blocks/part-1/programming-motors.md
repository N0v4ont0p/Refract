> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-motors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-motors.md).

# Programming Motors

{% hint style="warning" %}
Modify your OpMode to add the motor related code. For now your completed servo code can be dragged to the side of your work space. You may alternatively choose to create a second program.
{% endhint %}

### What is a Motor?

Just like servos, a motor is a form of actuator. You may picture a dozen different things when you think of a motor, from those used to spin the wheels of a car to the large turbines that allow a plane to fly. For our robots, we will be focusing on DC motors. These are a type of electrical motor that use direct current, or DC, to rotate and produce the mechanical force needed to move an attached mechanism.

{% hint style="info" %}
For this tutorial, either a Core Hex Motor or HD Hex Motor may be used as long as they have been properly configured on the Driver Hub.
{% endhint %}

Most standard motors are able to continuously rotate in either direction with an adjustable speed or power. Some motors may also include a built in encoder, which allows them to move to a specified position, similar to a servo, or to collect data like the number of completed rotations!

To access the motor snippets in Blocks we need to look under the **Actuators** dropdown menu:

<figure><img src="/files/17Oz99Qfxw8L79bKKQnc" alt=""><figcaption></figcaption></figure>

You may notice there are several options for blocks under the **DcMotor** menu. For Hello Robot we will be using those found in the **DcMotor** menu itself and under **Dual.**

<figure><img src="/files/AmUXr3VM47JNtakt8POl" alt=""><figcaption></figcaption></figure>

As the name suggests, the blocks found under **Dual** are intended for the use of two motors. We will learn more about them in [Part 2](/duo-control/hello-robot-blocks/part-2.md)!

{% hint style="info" %}
If you do not see the DcMotor menu under Actuators double check your [configuration ](/duo-control/hello-robot-blocks/configuration.md)includes a motor and is currently active on the Driver Hub!
{% endhint %}

## Let's get Programming!

In the next few sections, we will be learning to program our motor to first move automatically in different directions then in response to our gamepad inputs. In our final section we will take a look at using telemetry with our motor's built in encoder.

***

| [Programming Motor Basics](/duo-control/hello-robot-blocks/part-1/programming-motors/programming-motors-basics.md) | [Programming a Motor with a Gamepad](/duo-control/hello-robot-blocks/part-1/programming-motors/programming-a-motor-with-a-gamepad.md) | [Programming Motor Telemetry](/duo-control/hello-robot-blocks/part-1/programming-motors/programming-motor-telemetry.md) |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |

Below is a sneak peek of our final full code:

<figure><img src="/files/WWLlPIRYwJODeavAo1zD" alt=""><figcaption></figcaption></figure>
