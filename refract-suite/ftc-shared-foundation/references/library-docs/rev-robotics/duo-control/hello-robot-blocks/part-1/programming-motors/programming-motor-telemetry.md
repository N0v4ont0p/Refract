> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-motors/programming-motor-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-motors/programming-motor-telemetry.md).

# Programming Motor Telemetry

## Motors and Telemetry&#x20;

Recall that **telemetry** is the process of collecting and transmitting data. There is a lot of useful information our motors could send back to us, but to start let's have it output the power based on the joystick's movement.&#x20;

Similar to what we did for our servo program, let's add a <img src="/files/-MWBJfpbTuatRMfbhnlO" alt="" data-size="original"> block from the telemetry menu to the end of our ![](/files/9JmuqmIVva0NqYySaYlc) loop:

<figure><img src="/files/HwtwcQGeNVPRmnoFkRkN" alt=""><figcaption></figcaption></figure>

From the DcMotor menu pullout the ![](/files/UMSLYwqOpGB3x4y2RGDw) block . Drag the block and attach it to the number **parameter** on the telemetry blocks.&#x20;

Change the key parameter to "Motor Power"&#x20;

<figure><img src="/files/rHmlxkGS4cNinlUHWJYB" alt=""><figcaption></figcaption></figure>

When the OpMode is run the telemetry block will display the current power based on the joysticks movement. Give it a try!

## Full Program

<figure><img src="/files/WWLlPIRYwJODeavAo1zD" alt=""><figcaption></figcaption></figure>
