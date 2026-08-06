> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3.md).

# Part 3: Autonomous and Encoders

We've tackled the basics. We have a robot able to drive around. What could be next?&#x20;

Right now our robot is largely dependent on inputs from us as the driver from the gamepad. We've helped it learn to sense a little bit using the touch sensor, but there is still more we can do.&#x20;

During **Part 3** we will be learning how to help our robot navigate the world around it autonomously in different ways. To start we will look at how to use a timer for the robot to keep track of how long it should do something. From there, we will move on to using the built in encoders of the HD Hex and Core Hex Motors.&#x20;

Encoders are a form of sensor that help collect data for the motor. Some encoders count the number of completed rotations. Others are able to track the exact position of a motor, similar to a servo. The use of encoders brings the need for more math and complex programming, however it will allow your robot to navigate more efficiently.&#x20;

## Quick Links

<table><thead><tr><th width="244" align="center">ElapsedTime</th><th align="center">Drivetrain Encoders</th><th align="center">Arm Encoders</th></tr></thead><tbody><tr><td align="center"><a href="/pages/W66ZuOL280TVc3BuYtWE">Overview</a></td><td align="center"><a href="/pages/NMo7JvEVdoyq8XWQD4kx">Overview</a></td><td align="center"><a href="/pages/K5nzmvxYP2dzDqJu91dd">Overview</a></td></tr><tr><td align="center"><a href="/pages/yoxozeH047aPESGq693r">ElapsedTime Setup</a></td><td align="center"><a href="/pages/aA4Dx57gVbUopTtY4FuI">Converting Encoder Ticks to a Distance</a></td><td align="center"><a href="/pages/Tt5IYygdgXjh5qiQtYbU">Estimating the Position of the Arm</a></td></tr><tr><td align="center"><a href="/pages/w5MNS7jNIstU2bja2gTh">ElapsedTime Logic</a></td><td align="center"><a href="/pages/30A1bNIlpweNMRE2bgq5">Moving to a Target Distance</a></td><td align="center"><a href="/pages/S2MPGtMFPBnUhZYQAZT4">Calculating Target Position</a></td></tr><tr><td align="center"><a href="/pages/WP8PFJQVNwErmQ66IVT5">ElapsedTime - Multiple Movements</a></td><td align="center"><a href="/pages/1JnWh4Cx8iMGx2Wb10E3">Setting Velocity</a></td><td align="center"><a href="/pages/yw6WY7onOKIoJUdSBbNL">Using Limits to Control Range of Motion</a></td></tr><tr><td align="center"></td><td align="center"><a href="/pages/R2WwK7FEyaxZvdMsjv0m">Turning the Drivetrain Using RUN_TO_POSITION</a></td><td align="center"></td></tr></tbody></table>
