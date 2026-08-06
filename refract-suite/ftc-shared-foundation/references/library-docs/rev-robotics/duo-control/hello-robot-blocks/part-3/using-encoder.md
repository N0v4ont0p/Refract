> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/using-encoder.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/using-encoder.md).

# Encoder Basics

{% hint style="info" %}
The HD Hex Motor and Core Hex Motor from REV Robotics include a built-in encoder. You may need to check your motor's documentation if following this tutorial with a different vendor's motor.&#x20;
{% endhint %}

## What is an Encoder?

Encoders are a form of sensor built into some motors that help provide feedback to our robot. There are different kinds of encoders, but we're going to be focus on what's called a quadrature encoder for this tutorial. These encoders are able to count the number of revolutions of the motor also sometimes called "ticks".&#x20;

While quadrature encoders aren't able to tell exact positions, they can still be used to help the motor move to a specified point. We'll go over how to do so later in this tutorial, but this works by specifying first an origin point in our code then a point the motor should move away.&#x20;

<details>

<summary>Quadrature vs. Absolute Encoders</summary>

You may see the term absolute encoder when referring to something like REV's [Through Bore Encoder](https://www.revrobotics.com/rev-11-1271/). Absolute encoders have a set origin allowing exact movements of the motor in comparison.&#x20;

Here's a hint for how to remember the difference:&#x20;

* **Quadrature Encoders** are like a stopwatch continuously adding up time!
* **Absolute Encoders** are more like a clock telling an exact time!

</details>

Different motors have different numbers of ticks per rotation of the output shaft based on the gear ratio of the motor. When the Control Hub is turned on, all of its encoder ports are at 0 ticks. As a motor moves forward, its encoder value increases. As a motor moves backwards, its encoder value decreases.&#x20;

## Exploring Motor Modes

<figure><img src="/files/bXQ1RjJLuLwirS2Ct06W" alt=""><figcaption></figcaption></figure>

Let's take a closer look at the different modes we can set our encoder to with our motor. The mode is often established during the initialization process of our code, meaning the motors are ready to go throughout our program, but it is possible to change this for specific use cases as it executes.&#x20;

Which mode we need to use largely depends on the intended function of the motor and any attached mechanism. For example, we may not need our encoders active on the drivetrain motors when they're being controlled by a joystick's input. On the other hand, we may have a flywheel design that requires a specific speed our encoders can help us achieve.&#x20;

### Using STOP\_AND\_RESET\_ENCODER&#x20;

When using encoders, it is strongly recommended to first use STOP\_AND\_RESET\_ENCODER during initialization. This will allow you to know what position the motor is starting in, however you will want to plan for a repeatable start up configuration each time!

A motor can be switched to "STOP\_AND\_RESET\_ENCODER" while a code is executing as well. This is often set up using a button on the gamepad to allow the driver to reset the encoder in the event of a motor misbehaving, such as after the robot's been caught on an obstacle.

### Using RUN\_WITHOUT\_ENCODER

Use this mode when you don’t want the Control Hub to attempt to use the encoders to maintain a constant speed. You can still access the encoder values, but your actual motor speed will vary more based on external factors such as battery life and friction. In this mode, you provide a power level in the -1 to 1 range, where -1 is full speed backwards, 0 is stopped, and 1 is full speed forwards. Reducing the power reduces both torque and speed.&#x20;

The RUN\_WITHOUT\_ENCODER motor mode is very straightforward, you simply set a power throughout the program using the "Power" block or, such as for a drivetrain, to be set by the joysticks.

<figure><img src="/files/yXsu5J4N7KoCwYyfp1kv" alt=""><figcaption></figcaption></figure>

### Using RUN\_USING\_ENCODER

In this mode, the Control Hub will use the encoder to take an active role in managing the motor’s speed. Rather than directly applying a percentage of the available power, RUN\_USING\_ENCODER mode targets a specific velocity (speed). This allows the motor to account for friction, battery voltage, and other factors. You can still provide a power level in RUN\_USING\_ENCODER mode, but this is not recommended, as it will limit your target speed significantly.&#x20;

Setting a velocity from RUN\_WITHOUT\_ENCODER mode will automatically switch the motor to RUN\_USING\_ENCODER mode. You should pick a velocity that the motor will be capable of reaching even with a full load and a low battery.

<figure><img src="/files/ijjxjwLiamslP3zwTdrj" alt=""><figcaption></figcaption></figure>

### Using RUN\_TO\_POSITION

In this mode, the Control Hub will target a specific position, rather than a specific velocity. You can still choose to set a velocity, but it is only used as the maximum velocity. The motor will continue to hold its position even after it has reached its target.&#x20;

{% hint style="danger" %}
If the motor is unable to reach the determined position the motor will continue to run attempting to reach or maintain that position, which can lead to the motor stalling and overheating.&#x20;
{% endhint %}

To use RUN\_TO\_POSITION mode, you need to do the following things in this order:

1. Set a target position (measured in ticks)
2. Switch to RUN\_TO\_POSITION mode
3. Set the maximum velocity (if not determined by a gamepad input)

Remember it is recommended to always reset the encoder during initialization, however you will need to make sure your robot has been reset physically to the initialization position. For example, an arm may need to be brought back to the start up configuration like for the beginning of a FTC match.&#x20;

The motor will continue to hold its position even after it has reached its target, unless you set the velocity or power to zero, or switch to a different motor mode.

<figure><img src="/files/pul6c8pAdTYBgzIOuwT1" alt=""><figcaption></figcaption></figure>
