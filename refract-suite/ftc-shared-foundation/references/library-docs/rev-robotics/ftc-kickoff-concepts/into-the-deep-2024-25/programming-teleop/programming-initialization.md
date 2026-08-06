> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-initialization.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-initialization.md).

# Programming - Initialization

Before the bulk of our program begins, we need to first establish our variables and tell our motors how we want them to run. This section of code will run once when the program is activated and before we hit "Play" on the Driver Hub.

<figure><img src="/files/vda3FI9n4EbRLECxJxJD" alt=""><figcaption><p>Initialization Code</p></figcaption></figure>

## Drivetrain Motor Settings

Since the motors on our drive train are a mirror of each other, one needs to be set to run in reverse. In this case we have the leftDrive motor set to run in reverse.&#x20;

By default, our drivetrain motors will not be using encoder data so we can set them to RUN\_WITHOUT\_ENCODER. Your team may choose to change this later when working on autonomous programming!

<figure><img src="/files/TmPavygFAHvuMmKC95JG" alt=""><figcaption></figcaption></figure>

## Establishing Variables

{% hint style="info" %}
[To learn more about "What is a Variable?" check out our Hello Robot tutorial!](/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks.md#what-is-a-variable)
{% endhint %}

<figure><img src="/files/22d9IGL6SfCyeweAYd1r" alt=""><figcaption><p>Variable states at program start</p></figcaption></figure>

There are two parts to our variable set up in this year's Starter Bot program. Often times we use variables in place of a number or equation, but in this case we will be using them to help our robot move between functions in our code and determine preset arm/wrist positions.&#x20;

Let's take a look at what all our variables do:&#x20;

<table><thead><tr><th width="217">Variable</th><th>Purpose</th></tr></thead><tbody><tr><td>MANUAL</td><td>Switches the arm and wrist to being manually controlled by the Dpad</td></tr><tr><td>INTAKE</td><td>Sets the arm and wrist to a preset position to intake game pieces</td></tr><tr><td>WALL_GRAB</td><td>Sets the arm and wrist to a preset position to pick up clipped specimens from human player</td></tr><tr><td>WALL_UNHOOK</td><td>Raises the arm from the wall (human player) position to remove clipped specimens</td></tr><tr><td>HOVER_HIGH</td><td>Sets the arm and wrist to a preset position to place specimens on the high rung</td></tr><tr><td>CLIP_HIGH</td><td>Moves the arm to clip specimens on the high rung</td></tr><tr><td>LOW_BASKET</td><td>Sets the arm/wrist to the needed high to score in the low basket</td></tr><tr><td>INIT</td><td>Resets the robot to its start up configuration</td></tr><tr><td>currentState</td><td>Switches the arm/wrist between the above preset positions and provides a readout for telemetry</td></tr><tr><td>clawOpen</td><td>Allows for the toggle control of the claw</td></tr><tr><td>lastBump</td><td>Allows for toggling the claw open or closed</td></tr><tr><td>lastHook</td><td>Allows for toggling between the two clip positions </td></tr><tr><td>lastGrab</td><td>Allows for toggling between the wall (human player) positions </td></tr></tbody></table>

### Variables: OnBot Java vs. Blocks

In the OnBot Java version of this code, we use something called "enum". This allows us to declare the variable name and have it treated as a unique value.

For example: the robot interprets the variable "MANUAL" as one of the states within our switch case in OnBot Java. We'll discuss more about the switch case down below!

However, "enum" is not available in Blocks meaning we have to be a little clever to mimic this process. We created strings using the "text" block to do a similar thing. This will have the robot understand MANUAL equals the word "manual", which allows it to move between cases. &#x20;

<div><figure><img src="/files/Q2rSWY1PHT19AF2z2stq" alt=""><figcaption><p>Variables in Blocks using strings</p></figcaption></figure> <figure><img src="/files/gkPy7j2FaEuz9tvA0urO" alt=""><figcaption><p>Variables in OnBot Java using enum</p></figcaption></figure></div>

### currentState Variable

You'll notice the variable currentState appears throughout our program repeatedly. But what does it do?&#x20;

This variable is what will allow our robot to switch between its various preset configurations based on what button is pressed on the gamepad. It's one variable that can be set to a number of different constant states. In comparison, our position variables will remain constant.

When we press one of the buttons on our gamepad it changes our currentState. In turn, this tells our arm and wrist on the robot to move to one of the predetermined positions seen below.

<figure><img src="/files/jYtvdgJdXlxz5xDa2kPA" alt=""><figcaption><p>Arm and Wrist Presets</p></figcaption></figure>

If we needed to update the position value for one of our presets, we can do so within this if/else statement and it will be reflected throughout the entire code without having the hunt down every instance it may be used.&#x20;
