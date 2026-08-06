> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-controlling-the-arm-and-wrist.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-controlling-the-arm-and-wrist.md).

# Programming - Controlling the Arm and Wrist

## Setting up the Arm and Wrist Motors:

<figure><img src="/files/qtmyrimc1J0v1c6Ea0rY" alt=""><figcaption><p>Setting the mode and target position for the motors</p></figcaption></figure>

As part of our main loop, our arm and wrist motors are set to RUN\_TO\_POSITION mode with their TargetPosition set to the appropriate variable. Additionally, our arm and wrist motors are set to full power whenever they are moving.&#x20;

Because our targetArm and targetWrist values change throughout our code, we include this as part of our loop rather than initialization. &#x20;

## Preset Movements

The GAMEPAD\_INPUT\_STATE function contains all our code for controlling the arm and wrist. Let's break it down by what each button does in our If/Else statement!

<figure><img src="/files/VQDRQxhUu1Ij4L0prW0k" alt=""><figcaption></figcaption></figure>

### Pressing A/Cross

<figure><img src="/files/sFfbWqJuE4QehfUJ9IeX" alt=""><figcaption></figcaption></figure>

When the A/Cross button on the gamepad is pressed our currentState switches to INTAKE meaning our robot's arm will move down and wrist will unfold to be ready to pick up samples.&#x20;

### Pressing B/Circle

<figure><img src="/files/2r2g1b4Ro0w63huuv3Wx" alt=""><figcaption></figcaption></figure>

This section of code allows for a togglable state between two positions of our arm/wrist when B/Circle are pressed. Because we want this to be togglable and not require the button to be held, we want to have our robot check the state of the B/Circle button each loop.&#x20;

<figure><img src="/files/7PuzzQYj3UjIzIftm763" alt=""><figcaption></figcaption></figure>

The lastGrab variable will change between true or false based on the state of the button. If the driver holds down the B/Circle button its state will not update again until it is first released.&#x20;

If B/Circle is pressed AND is not currently held then the robot will run a second if/then statement to determine which of the Wall positions the arm/wrist should move to.

<figure><img src="/files/SFOdCzIPZF3RiHVzZrRW" alt=""><figcaption></figcaption></figure>

With this statement the robot knows that if the arm is already at our WALL\_GRAB preset it should move to unhook. The opposite is also true where if the arm/wrist is in the WALL\_UNHOOK preset it will go back to grab.&#x20;

### Pressing Y/Triangle

This section functions similarly to B/Circle providing a togglable control for clipping a specimen!

<figure><img src="/files/Nu88jA7PTGEWwBxZBnHu" alt=""><figcaption></figcaption></figure>

In this case lastHook allows the robot to determine if the Y/Triangle button is being held before the robot moves between the two positions.&#x20;

<figure><img src="/files/Ul0YlGvXlSCKrxQAYVmI" alt=""><figcaption></figcaption></figure>

### Pressing X/Square

<figure><img src="/files/7l2uZMQzoFBimbi10S8U" alt=""><figcaption></figcaption></figure>

When the X/Square button on the gamepad is pressed our currentState switches to LOW\_BASKET meaning our robot's arm will move up and wrist will unfold to be ready to deposit samples in the low basket.

### Pressing Left Bumper

<figure><img src="/files/cNFtQ7leQEVv41yc6itA" alt=""><figcaption></figcaption></figure>

It's always good to have a way to reset our robot if needed! By pressing left bumper, currentState will be set to INIT moving our robot back to its initilization configuration, like what might be used at the start of a match.&#x20;

## Manual Control

Beyond our preset movements, we want our robot to have refined control for the arm and wrist as we navigate the field.

<figure><img src="/files/D01NdEgVuApN5rJG2nwZ" alt=""><figcaption></figcaption></figure>

Whenever we press a button on the d-pad our currentState will switch to MANUAL allowing the arm or wrist to move in increments until the button is released.&#x20;

Because we have our motors set to "RUN\_TO\_POSITION" mode we can't just turn the power on for manual control. Instead we have the robot changing the position in the appropriate direction in chunks. Depending our your driver's preference, you may choose to adjust these values for quicker or more refined control!&#x20;

{% hint style="info" %}
By default, these position values are different in the OnBot Java and Blocks version of the provided code. This is due to a difference in how quickly OnBot Java loops through a program compared to Blocks.
{% endhint %}
