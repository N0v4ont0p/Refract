> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks.md).

# Arcade Style TeleOp - Blocks

The time has come to program our robot to respond to our gamepad inputs so we can drive it around! To start we will be focusing on controlling our drivetrain.&#x20;

Think back to the very start of [Part 2](/duo-control/hello-robot-blocks/part-2.md) for a moment. We will be programming our robot using the Arcade Style of TeleOp. This means our forward and back movements will be controlled using the y-axis of the joystick while turning will be controlled by the x-axis.

This section will introduce the use of **variables** as we create our program. This will allow us to set up calculations in our program that will determine what power the motors should receive based on our gamepad's input. How much **power** each motor receives changes how the robot will **move,** so it is important to also review this relationship will establishing our code!

Below is a sneak peek at our final program:

<figure><img src="/files/oiVStvKYLLCLpGkjeqvT" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Right Stick vs. Left?

Which joystick is used for driving the robot is largely based on driver preference.&#x20;

For Hello Robot, we will be referencing using the right stick due to the arm control using the Dpad. This can be changed at any time by selecting your preferred option from the dropdown menu on the ![](/files/ArjxXrEikUGggQ92tfi4) blocks!
{% endhint %}

## Quick Links

<table data-header-hidden><thead><tr><th width="261"></th><th width="232"></th><th></th></tr></thead><tbody><tr><td><a href="/pages/NzlN7ZFDdnoDNYbVM4rX">Establishing Variables in Blocks</a></td><td><a href="/pages/kKi79oYBTnQ6Vyaaa1s7">Motor Power vs. Robot Movement</a></td><td><a href="/pages/WnmqrzEiHPk4J5GMMITC">Programming Arcade Drive</a></td></tr></tbody></table>
