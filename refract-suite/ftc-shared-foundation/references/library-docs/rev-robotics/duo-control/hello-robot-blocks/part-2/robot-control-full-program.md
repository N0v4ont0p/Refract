> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/robot-control-full-program.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/robot-control-full-program.md).

# Robot Control Full Program

It's time to bring everything together so to have a fully mobile robot! Returning to our HelloRobot\_TeleOp program we can add our arm control to our loop below the drivetrain code.

## Full Program

<figure><img src="/files/HuWx6YKnJsPAN8dFJKzL" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Right Stick vs. Left?

Which joystick is used for driving the robot is largely based on driver preference.&#x20;

For Hello Robot, we will be referencing using the right stick due to the arm control using the Dpad. This can be changed at any time by selecting your preferred option from the dropdown menu on the ![](/files/ArjxXrEikUGggQ92tfi4) blocks!
{% endhint %}

## Downloads

{% hint style="info" %}
These premade programs do not include control of the Class Bot V2's "claw" servo. To learn about programming a servo visit [Programming Servos](/duo-control/hello-robot-blocks/part-1/programming-servos.md).
{% endhint %}

#### Class Bot V2 / Hello Robot Configuration File:

{% file src="/files/0I0l46NcUfJw0kdGxeKM" %}

**Note:** This configuration file includes the test\_motor from Part 1 and no color sensor.

#### Class Bot V2 / Hello Robot Full TeleOp:

{% file src="/files/yfDDcjJyCFDgVneyznsF" %}

#### Class Bot V2 / Hello Robot Arm Control no Limit Switch:

{% file src="/files/mY2tKw8ILgO89JfLMEbg" %}

#### Class Bot V2 / Hello Robot Arm Control with Limit Switch:

{% file src="/files/vhiDVr6ecnvUweX8fAaN" %}
