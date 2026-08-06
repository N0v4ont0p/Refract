> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-intake-and-claw-toggle.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-intake-and-claw-toggle.md).

# Programming - Intake and Claw Toggle

## Intake Control

<figure><img src="/files/703MgOCUKdKlN9hXARgw" alt=""><figcaption></figcaption></figure>

When one of the triggers on the gamepad is pressed, it activates our GAMEPAD\_INTAKE function. This simple if/then statement just checks which trigger is being pressed so our servo knows which way to rotate.&#x20;

Because our servo is set to [continuous mode](/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md#continuous-rotation) in our configuration, we have the ability to tell our servo to set a power instead of moving by position increments!&#x20;

<figure><img src="/files/HZBvO2oTGSIlwv2XIV3o" alt=""><figcaption></figcaption></figure>

## Claw Toggle Control

<figure><img src="/files/G0mpFGIslzIRMIttJ2Ec" alt=""><figcaption></figcaption></figure>

When the right bumper is pressed on the gamepad, the claw on the robot either opens or closed. This prevents the driver from having to hold down the button to maintain control of a picked up specimen!&#x20;

Because togglable control is not natively available in the FTC SDK, we have to make use of a couple of variables to help the robot check the state of the claw's servo and the right bumper.&#x20;

<figure><img src="/files/6Ffm90LYtVL6c2KOpCim" alt=""><figcaption></figcaption></figure>

Similar to what's used in our arm control's presets, lastBump checks if the right bumper is being held down and won't accept another input until its been released.&#x20;

<figure><img src="/files/iVdB9CimSv23MV3DXBo8" alt=""><figcaption></figcaption></figure>

Meanwhile, clawOpen allows the servo to shift between the two set positions based on where it has last moved to. You can adjust these values based on your specific robot to have the claw open more or less.
