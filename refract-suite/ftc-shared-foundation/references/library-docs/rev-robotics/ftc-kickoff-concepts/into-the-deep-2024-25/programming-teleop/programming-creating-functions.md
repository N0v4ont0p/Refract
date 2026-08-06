> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-creating-functions.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-creating-functions.md).

# Programming - Creating Functions

This year in our Starter Bot Blocks code we are using "functions" for the first time.&#x20;

<figure><img src="/files/I6CgU6IrxuDNmHc3tTPF" alt=""><figcaption><p>Blocks Functions</p></figcaption></figure>

## What is a Function?

Functions act similar to a variable in that we are using one thing to represent another. However, where a variable typically is used in place of something short, such as a number or equation, a function can take the place of several lines of code.&#x20;

This can be incredibly useful if there is a section of code we know will be repeated or to break apart our code into chunks for easy editing.

Below is a breakdown of our functions:

<table><thead><tr><th width="292">Function</th><th>Purpose</th></tr></thead><tbody><tr><td>GAMEPAD_INPUT_STATE</td><td>Contains the code related to the arm/wrist presets</td></tr><tr><td>GAMEPAD_INPUT_TOGGLE</td><td>Contains the code for the claw toggle</td></tr><tr><td>GAMEPAD_INPUT_MANUAL</td><td>Contains the code for manual control of the arm/wrist</td></tr><tr><td>GAMEPAD_INTAKE</td><td>Contains the code for running the servo on the intake</td></tr><tr><td>STATE_MACHINE</td><td>Contains all the preset positions for currentState</td></tr><tr><td>SPLIT_STICK_ARCADE_DRIVE</td><td>Contains the code for driving the robot</td></tr><tr><td>TELEMETRY</td><td>Contains the telemetry read out code</td></tr></tbody></table>

### How do Functions appear in Blocks?

When using functions, our Blocks program becomes divided into different sections containing separate series of code:

<figure><img src="/files/6bEkb9m2Yp6SjV4fSCCc" alt=""><figcaption><p>Starter Bot 2024-25 Example Code </p></figcaption></figure>

So let's say we wanted to change how quickly our robot's arm moves during [manual control](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-controlling-the-arm-and-wrist.md#manual-control) with the d-pad. With our functions organizing our code in chunks, it's easy to find the values we want to change:

<figure><img src="/files/UGxGBZC2396fiGxTmF19" alt=""><figcaption><p>Function for Manual Arm/Wrist control</p></figcaption></figure>

Without the use of functions our code would end up a little long and clunky:

<figure><img src="/files/dA4Wi6TBA5LihyUkLHIm" alt=""><figcaption><p>This is intended as an example only and not actual use!</p></figcaption></figure>

### Creating a new Function in Blocks

If we want to create a new function in our Blocks program, we start by pulling a ![](/files/OKnrIjSnKxnoysxNuwIj)block from the Functions menu:

<figure><img src="/files/SHPheleqNpi5PUITJS3z" alt=""><figcaption><p>Functions menu in Blocks</p></figcaption></figure>

Next we will replace "do something" with an appropriate name. Maybe in this case we are adding a new function for climbing:&#x20;

<figure><img src="/files/UaNenNTtMSZnBCzFjjL5" alt=""><figcaption><p>Example function for climbing</p></figcaption></figure>

Once our function is named it will appear in the "Functions" menu to be added to the main loop or wherever we need it within our code!

<figure><img src="/files/7DphB9gaZjSwdtPy6sY6" alt=""><figcaption><p>New function block</p></figcaption></figure>

<figure><img src="/files/obGmaeBqkeKQcdFpu0hf" alt=""><figcaption><p>New function added to our main code</p></figcaption></figure>

All that's left is to add whatever code we'd like to be within this function:

<figure><img src="/files/ubexbiSLcyQyjWU44EED" alt=""><figcaption><p>Example of a simple code within our function</p></figcaption></figure>

{% hint style="info" %}
The Starter Bot is able to climb the lower rung using the existing example program!
{% endhint %}

If the ![](/files/zvszCltRNHhLJVoUEfNz) block is deleted this will remove the function from the "Functions" menu.

## Additional Function Example

By default, the Starter Bot's program only references each function once during our loop. The following is intended to be an additional example for reusing functions throughout a program and as an additional educational resource!

{% hint style="info" %}
This program can be tested on the Starter Bot or another robot using the same configuration file! Create a new OpMode to begin. Ours is called `FunctionsDemo`.

If you are using the Starter Bot, make sure the arm is adjusted to not drag while the robot drives autonomously.&#x20;
{% endhint %}

Let's say we are working on an autonomous code where we want our robot to drive roughly in a square. Remember that autonomous means this code will move the robot on its own when play is pressed:

<figure><img src="/files/mq1EKr4dQ0z1VBJ35eXJ" alt=""><figcaption><p>Simple program for driving in a square</p></figcaption></figure>

Next, let's say we need the robot to do something between one of the turns, such as move its arm or open a servo's claw. There's a couple of ways we could approach this without functions:

<figure><img src="/files/6mi7gXua3QCxBLO1gocB" alt=""><figcaption><p>Full code with claw opening after driving two sides</p></figcaption></figure>

Already our code is getting a little long so let's move our side motion and turn into a function:

<figure><img src="/files/TsjLrQRcK00Ue5lWOY6P" alt=""><figcaption><p>Function containing the code for driving and turning</p></figcaption></figure>

Now our loop may look like this:

<figure><img src="/files/WJfkXPnwQMmnbynfOYrA" alt=""><figcaption><p>Using functions to drive in a square</p></figcaption></figure>

When we test our code we may notice our robot isn't exactly driving in a square shape. Thankfully with our function in place we only need to change the needed value in one place:

<figure><img src="/files/sYXe4SStfHyRWmGOR9eH" alt=""><figcaption><p>Code for controlling the robot's turn</p></figcaption></figure>

This change to the function will be reflected anywhere `DRIVE_AND_TURN` used.

Give it a try by changing the right motor's power or the timer to refine your square!
