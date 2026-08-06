> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/using-a-gamepad.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/using-a-gamepad.md).

# Using a Gamepad

## Using Gamepads

While our robot is able to do a lot autonomously, more often than not we need to input commands using our connected gamepad. There is a large variety of gamepads that could be used with the Driver Hub. For this tutorial we will be focusing on a generic PS4 controller, such as the [Etpark Wired Controller ](https://www.revrobotics.com/rev-39-1865/)or a Logitech controller.

{% hint style="info" %}
To initialize the gamepad that will act as User 1 (gamepad1, in code) press the options button and the Cross/A button on the gamepad at the same time. To initialize User 2 ( gamepad2, in code) press the options button and the Circle/B button at the same time.
{% endhint %}

<figure><img src="/files/X6SZsvvaC3xi61YK4rbg" alt=""><figcaption></figcaption></figure>

All buttons on a gamepad can be programmed to a specific task or behavior. Let's take a look at the breakdown of each button, their associated block name, and the type of data they output:&#x20;

<figure><img src="/files/h83i53xg2g2YQADYA4eJ" alt=""><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="157" align="center">PS4 Controllers</th><th width="142" align="center">Default (Logitech Gamepad) </th><th width="257" align="center">Blocks</th><th align="center">Data Type</th></tr></thead><tbody><tr><td align="center">PS4 Controllers</td><td align="center">Generic USB Gamepad</td><td align="center">Blocks</td><td align="center">Data Type</td></tr><tr><td align="center">Cross</td><td align="center">a</td><td align="center"><img src="/files/-MefyGMd_cjtIMfaGFye" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Circle</td><td align="center">b</td><td align="center"><img src="/files/-MefyIl-Ll13ocSPLPBb" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Triangle</td><td align="center">y</td><td align="center"><img src="/files/-MefyLTC5XT0ZCUcL4qa" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Square</td><td align="center">x</td><td align="center"><img src="/files/-MefyNihIOjS-Ex05c3V" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Dpad Up </td><td align="center">Dpad Up</td><td align="center"><img src="/files/-MefyQc43fGBd8YPQ1KH" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Dpad Down</td><td align="center">Dpad Down</td><td align="center"><img src="/files/-MefyWzBxrbhm_nxZdwK" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Dpad Left</td><td align="center">Dpad Left</td><td align="center"><img src="/files/-MefyZrTvZ4--3FR-LtP" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Dpad Right</td><td align="center">Dpad Right</td><td align="center"><img src="/files/-MefycRzLKZCh8Nyihuf" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Left Bumper</td><td align="center">Left Bumper</td><td align="center"><img src="/files/-MefvsReeMM-BoSDwSo9" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Right Bumper</td><td align="center">Right Bumper</td><td align="center"><img src="/files/-MefyhTGT065OSFPQMsO" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Left Trigger</td><td align="center">Left Trigger</td><td align="center"><img src="/files/-Meg1ixhp5UYWLTIwpfA" alt="" data-size="original"> </td><td align="center">Float</td></tr><tr><td align="center">Right Trigger</td><td align="center">Right Trigger</td><td align="center"><img src="/files/-Meg1l3U6mcavar6qAT0" alt="" data-size="original"> </td><td align="center">Float</td></tr><tr><td align="center">PS</td><td align="center">Home</td><td align="center"><img src="/files/-Meg23NRA8GyJEd6wi5t" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Options</td><td align="center">Start/Options</td><td align="center"><img src="/files/-Meg25mUFbikYvJ0CP2o" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Share</td><td align="center">Back/Share</td><td align="center"><img src="/files/-Meg289jpsjclF39NFy6" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Left Stick Button</td><td align="center">Left Stick Button</td><td align="center"><img src="/files/-MefymdCUyynn8QoQhb5" alt="" data-size="original"></td><td align="center">Boolean</td></tr><tr><td align="center">Left Stick X Axis</td><td align="center">Left Stick X Axis</td><td align="center"><img src="/files/-Meg2Bkc5e_G0-UfhDL7" alt="" data-size="original"> </td><td align="center">Float</td></tr><tr><td align="center">Left Stick Y Axis</td><td align="center">Left Stick Y Axis</td><td align="center"><img src="/files/-Meg2EWU1Uo-OOYRTZdx" alt="" data-size="original"> </td><td align="center">Float</td></tr><tr><td align="center">Right Stick Button</td><td align="center">Right Stick Button</td><td align="center"> <img src="/files/-Mefypw4O9JtYoO9CQQj" alt="" data-size="original"> </td><td align="center">Boolean</td></tr><tr><td align="center">Right Stick X Axis</td><td align="center">Right Stick X Axis</td><td align="center"><img src="/files/-Meg2IxQy9Nnb5ojouxt" alt="" data-size="original"> </td><td align="center">Float</td></tr><tr><td align="center">Right Stick Y Axis</td><td align="center">Right Stick Y Axis</td><td align="center"><img src="/files/-Meg2Lw3rWVWYEzLC8sq" alt="" data-size="original"> </td><td align="center">Float</td></tr></tbody></table>

### Boolean vs Float Data Types

The gamepad outputs two types of data back to the Control Hub to be used within the program:

#### Boolean&#x20;

Boolean data has two possible values: **True and False**. These two values can also be represented by **On and Off** or **1 and 0**.&#x20;

The buttons, bumpers, and triggers on the gamepad provide boolean data to our robot! For example, a button that is not pressed will return a value of False (or 0) and a button that is pressed will return the value True (or 1).&#x20;

#### Float

Float data is a number that can include decimal places and positive or negative values.&#x20;

On the gamepad, the float data returned will be between 1 and -1 for the joystick's position on each axis. Some examples of possible values are 0.44, 0, -0.29, or -1.&#x20;
