> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arm-control-blocks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arm-control-blocks.md).

# Arm Control - Blocks

Now that our robot is able to drive around let's get our arm up and moving!

## Introduction to Arm Control&#x20;

![](/files/-Mbh_RZjnHpZbvvDsZ8H)

Controlling an arm requires a different thought process than the one you used to control the drivetrain. While the drivetrain uses the rotation motion of the motors to drive along a linear distance, an arm rotates along a central point, or joint.&#x20;

Unlike our drivetrain, our arm has physical limitations for how far it can rotate. We don't want our robot to damage itself so we'll be making use of our touch sensor to act as a limit switch.

## Basics of Programming an Arm

For this section, we will start by creating a new program called HelloRobot\_ArmControl. We will be able to add this to our drivetrain OpMode later, but for now keeping it separate will help us to focus just on the arm.

To control our arm we will be using the Dpad on our gamepad. While our joystick provides a range of possible values or float data, our Dpad will only be read as 1 or 0. To us these numbers translate to true, the button has been pressed, or false, the button has not been pressed.&#x20;

<details>

<summary>Click to Review Boolean vs. Float Data Types!</summary>

#### Boolean  (Dpad, a/b/y/x buttons, bumpers)

Boolean data has two possible values: **True and False**. These two values can also be represented by **On and Off** or **1 and 0**.&#x20;

The buttons, bumpers, and triggers on the gamepad provide boolean data to our robot! For example, a button that is not pressed will return a value of False (or 0) and a button that is pressed will return the value True (or 1).&#x20;

#### Float (Joysticks and triggers)

Float data is a number that can include decimal places and positive or negative values.&#x20;

On the gamepad, the float data returned will be between 1 and -1 for the joystick's position on each axis. Some examples of possible values are 0.44, 0, -0.29, or -1.&#x20;

</details>

***

Let's start by adding an <img src="/files/-MWBUDlUpVQmk7Y7zght" alt="" data-size="original"> block to our active loop. Use the settings dropdown to change the block to an <img src="/files/-M_76Lu914wbfp2TPuaG" alt="" data-size="original"> block.&#x20;

![](/files/-M_7-FqCBac6olINNE2x)

<figure><img src="/files/i80nqlq7HM5jn3hIgcNp" alt=""><figcaption></figcaption></figure>

Now the skeleton of our if/else if statement is ready. We can add the  <img src="/files/-M_6pst95i16Ri14yZ4b" alt="" data-size="original"> and <img src="/files/-M_6pxul-r5EMNjjKUza" alt="" data-size="original"> blocks next.&#x20;

![](/files/-M_7SXNq7poj15LVdIbC)

With this in place our robot will be checking if the Dpad Up or Dpad Down button are pressed before proceeding with the appropriate action. But what do we want our arm to do?

### Adding Motion

For now, our easiest path is to have our arm move up with DpadUp and down with DpadDown. You may decide later to change which buttons are being used, but the logic found here should be similar.

Let's add a ![](/files/YmO08cURdjailiuwbxa9) block to each "do" section of our statement. While testing our movement we will want to reduce the power to a more manageable range. For now, we will set our up to 0.2 and down to -0.2.&#x20;

![](/files/-M_7kP-c-lQmc4VuTWk4)

### Quick Check!

Save your OpMode and give it a go! Consider the following as test your program:

* What happens if you press up on the Dpad?
* What happens if you press down on the Dpad?
* What happens when neither button is actively pressed?

Did the robot move as you expected?

<details>

<summary>What happened while testing your program?</summary>

Likely, you noticed even when no button is pressed the motor continues to try to move the last direction inputted. This is more obvious when pressing the DpadUp button, but if you listen closely you'll be able to hear the motor trying to move downward once DpadDown is pressed as well.

Stalled movement such as this is not healthy for our motors nor is it the easiest to control. We'll want to fix this before we continue testing!

</details>

### Establishing an "Else"

The current <img src="/files/-M_76Lu914wbfp2TPuaG" alt="" data-size="original"> statement tells the robot when the motor should move and in what direction, but nothing tells the motor to stop, thus the arm is continuing to run without limits. Ideally, we want our arm to move ONLY when a button is pressed.&#x20;

To fix this we can edit the <img src="/files/-M_76Lu914wbfp2TPuaG" alt="" data-size="original">block to have an extra ![](/files/bh6Wvay4FCiwDnD9WbEV) at the end of the statement.

![](/files/-M_LuuheylqocGOY0N_J)

Then add a <img src="/files/-MaAmcRjToPMPrh6OqtT" alt="" data-size="original"> block to our new "else" section.

![](/files/-M_M-uNIIp95KM1rQbde)

With this change in place, save your program and give it another test!
