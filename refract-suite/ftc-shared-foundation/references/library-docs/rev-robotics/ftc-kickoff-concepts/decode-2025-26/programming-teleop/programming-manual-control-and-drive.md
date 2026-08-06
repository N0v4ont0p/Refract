> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-manual-control-and-drive.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-manual-control-and-drive.md).

# Programming - Manual Control and Drive

## Split Stick Arcade Drive

<figure><img src="/files/YOX9wTBqji2y3qMdrPb5" alt=""><figcaption><p>Split Stick Arcade Drive</p></figcaption></figure>

This year's Starter Bot is designed for split arcade drive. This means the left joystick controls the forward and back motion while the right joystick allows for rotation.

The approached to Split Stick Arcade Drive used in this year's Starter Bot is intended to be similar to those available as examples in the SDK from *FIRST* and our tutorial for standard [Arcade Drive](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/programming-arcade-drive)!&#x20;

{% hint style="info" %}
To learn more about the variables used and the equation for deciding motor power, check out [Hello Robot's walkthrough](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks#creating-x-and-y-variables)!
{% endhint %}

## Manual Feeder and Servo Control

<figure><img src="/files/3iOGYf7iN4TLSpShcAgZ" alt=""><figcaption><p>Manual Core Hex and Servo Controls</p></figcaption></figure>

Manual control is built into the program to allow flexibility in how team's approach launching balls or to aid in the event that a ball becomes stuck.

For visual clarity, the servo and Core Hex controls are separated into separate if/else statements.&#x20;

### Core Hex Feeder

<figure><img src="/files/FzOzZ4fxSzETqzsDW7ij" alt=""><figcaption><p>Manual control for the Core Hex feeder</p></figcaption></figure>

When cross/A is held on the gamepad, the Core Hex feeder will rotate at half power. This would feed balls to the flywheel. While holding triangle/Y, it will rotate at half power in the opposite direction. This would pull balls away from the flywheel back into the hopper.&#x20;

Be aware both the Core Hex and flywheel motor may need to be reversed to free a ball in the lower area of the launcher.&#x20;

### Servo Agitator

<figure><img src="/files/G0q13EJJ1W9TFwFrN6p8" alt=""><figcaption><p>Manual control for the servo agitator</p></figcaption></figure>

When dpad left or right is held on the gamepad, the agitator servo will continuously spin. This may help with adjusting balls already loaded in the hopper.
