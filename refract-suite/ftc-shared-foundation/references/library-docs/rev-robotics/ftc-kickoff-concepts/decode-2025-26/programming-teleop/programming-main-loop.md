> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-main-loop.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-main-loop.md).

# Programming - Main Loop

<figure><img src="/files/e6nR28lDZ1sIRoOcIvyL" alt=""><figcaption><p>Main loop for the TeleOp code</p></figcaption></figure>

The main "whileLoop" of our program this year is fairly short containing our functions and temeletry for the flywheel.

## What is a Function? <a href="#what-is-a-function" id="what-is-a-function"></a>

You can think of functions (also known as methods) as a set of pre-written instructions represented by one line of code. When the function is called, the robot knows to run that set of instructions.

As an example, in our program we've created a function called splitStickArcadeDrive. Any time the robot receives an input for that function, in this case from the joysticks, it knows to go through the process of running the drivetrain despite those code lines not being listed individually in the mainLoop.

<figure><img src="/files/XGP8HiIEgrzHFoVx75Xd" alt=""><figcaption><p>splitStickArcadeDrive function being called in the mainLoop</p></figcaption></figure>

Our full splitStickArcadeDrive function, and those code steps, can be found elsewhere within our program organized and self-contained with all the relevant pieces together. This code is what's run when the function is called.

<figure><img src="/files/haQfqiRHEgdFNjvNCIsy" alt=""><figcaption><p>splitStickArcadeDrive function</p></figcaption></figure>

**In short:**&#x20;

Functions take the place of several lines of code and appear as a single line when called. This can be incredibly useful if there is a section of code we know will be repeated or to break apart our code into chunks for easy editing and viewing.

Below is a breakdown of our functions

<table><thead><tr><th width="272.8887939453125">Function</th><th>Purpose</th></tr></thead><tbody><tr><td>splitStickArcadeDrive</td><td>Contains the code for driving the robot</td></tr><tr><td>setFlywheelVelocity</td><td>Contains both the auto and manual control for the flywheel</td></tr><tr><td>manualCoreHexAndServoControl</td><td>Contains manual control for the feeder Core Hex and servo</td></tr></tbody></table>

{% hint style="info" %}
Interested in learning more about functions? [Check our Hello Robot!](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/exploring-functions)
{% endhint %}

## Telemetry

The telemetry of the main loop reports the flywheel's velocity and how that equals to power. This can be used as a reference when troubleshooting the flywheel or determining if a new velocity target should be set.&#x20;

<figure><img src="/files/axqv5qRyCaQJBeuJdaz2" alt=""><figcaption><p>Telemetry for the flywheel's velocity and power</p></figcaption></figure>
