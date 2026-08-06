> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-driving-and-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-driving-and-telemetry.md).

# Programming - Driving and Telemetry

## Split Arcade Drive

This year's Starter Bot is designed for split arcade drive. This means the left joystick controls the forward and back motion while the right joystick allows for rotation.

<figure><img src="/files/xFhEOgOKtkSaO50bzIlG" alt=""><figcaption><p>Split Arcade Drive</p></figcaption></figure>

By adding a "clip" block to our drive program, we determine the minimum and maximum number or equation can equal out to. This reduces the possibility of an error occurring in the scenario where the value equals something higher than 1 or lower than -1, the motor's max range, which may cause a missed input.&#x20;

## Telemetry&#x20;

Telemetry helps our robot to communicate to use what it thinks it is doing.

<figure><img src="/files/feldBxbidAg2mlBP8zVO" alt=""><figcaption></figcaption></figure>

As part of our telemetry function, we have our robot reading out the currentState variable letting us know if the arm/wrist are in manual mode or at one of our various preset positions.&#x20;

Claw Position shows us if the claw is currently open or closed. The "test" block can be found under the logic menu!

<figure><img src="/files/7rhXKoAWO2NuQZgrhw7Y" alt=""><figcaption></figcaption></figure>

Lastly, our robot provides the current position and power of the arm and wrist. This is helpful for if we need to change a preset or for adding new code using the encoders on the motors!

<figure><img src="/files/1E0D3kHjg0IsveFVbkxa" alt=""><figcaption></figcaption></figure>
