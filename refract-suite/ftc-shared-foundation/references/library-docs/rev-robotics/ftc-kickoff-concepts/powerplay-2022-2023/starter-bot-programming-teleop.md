> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/starter-bot-programming-teleop.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/starter-bot-programming-teleop.md).

# Starter Bot - Programming TeleOp

## Basic TeleOp Strategy

Our strategy for teleoperated mode was to make driving the robot as intuitive and precise as possible. Navigating carefully through the grid of Junctions is important for gameplay so we decided to use Split Arcade Drive this year.&#x20;

Since the Junctions are mounted on springs and can move or change height freely, we found the best method to control the Lift mechanism was to not use preset levels. This allows us to easily raise cones to any height needed.&#x20;

## Configuration and Wiring

Before getting started with programming we needed to create a configuration file. Below is an overview of how the robot is configured for the teleop code to function as expected:

| Port Type | Port Number | Device Type                | Name      |
| --------- | ----------- | -------------------------- | --------- |
| Motor     | 0           | REVRoboticsCoreHexMotor    | Lift (L)  |
| Motor     | 1           | REVRoboticsCoreHexMotor    | Lift (R)  |
| Motor     | 2           | REVRoboticsUltraplantary   | Drive (L) |
| Motor     | 3           | REVRoboticsUltraplantary   | Drive (R) |
| Servo     | 0           | Servo, Continuous Rotation | Intake    |
| I2C       | 0           | IMU                        | imu       |

{% hint style="info" %}
For more in depth information on the configuration process check out [Hello Robot - Configuration](/duo-control/hello-robot-blocks/configuration.md)!
{% endhint %}

### Wiring Diagram

<figure><img src="/files/eABIwLAaDYyz7uRXALWe" alt=""><figcaption></figcaption></figure>

| Device Name/Function | Device Type       | Port                 |
| -------------------- | ----------------- | -------------------- |
| Lift (L)             | Core Hex Motor    | Motor/Encoder Port 0 |
| Lift (R)             | Core Hex Motor    | Motor/Encoder Port 1 |
| Drive (L)            | HD Hex Motor      | Motor/Encoder Port 2 |
| Drive (R)            | Core Hex Motor    | Motor/Encoder Port 3 |
| Intake               | Smart Robot Servo | Servo Port 0         |

## Assigning Controls to a Gamepad/Controller

Items to consider when mapping out your gamepad:

* What kind of input does the mechanism need?&#x20;
  * **Joysticks and Triggers** input [floating point data](/duo-control/hello-robot-blocks/using-a-gamepad.md#float) to your code allowing you to adjust the speed of a motor based on the pressure applied to the trigger or position of the joystick.&#x20;
  * **Buttons, Bumpers, and D-Pad** provide [boolean data](/duo-control/hello-robot-blocks/using-a-gamepad.md#boolean) to your code and are ideal for triggering a action such as rotating a motor to a set position.&#x20;
* What drivetrain are you using and what driving style do you want to use?
  * We decided the POWERPLAY Starter Bot would be driven with Split Arcade Drive for advantages in precision while driving.
* Which input makes the most sense? Would pressing up on the d-pad be more intuitive for moving your arm up or down?
  * We chose to assign our D-Pad inputs to raising and lowering our lift and the right bumper to releasing Cones from the intake.&#x20;

POWERPLAY Starter Bot controller layout:

<figure><img src="/files/6iM8oium4SzJNOhux40I" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Not all controllers have buttons labeled the same way. Check the manufacturer's documentation for accurate button mapping.
{% endhint %}

| Input          | Function                         |
| -------------- | -------------------------------- |
| Right Joystick | Turn Left and Right              |
| Left Joystick  | Drive Forward and Reverse        |
| Right Bumper   | Reverse Intake (Let go of Cones) |
| D-Pad Up       | Raise Lift                       |
| D-Pad Down     | Lower Lift                       |

More information on programming gamepads for use with your robot can be found at[ Hello Robot - Using Gamepads](/duo-control/hello-robot-blocks/using-a-gamepad.md).

## Programming Teleop - Blocks

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-blocks/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

### Drive Code&#x20;

In [Hello Robot- Basics of Programming Drivetrains](/duo-control/hello-robot-blocks/part-2/programming-drivetrain-motors.md) we covered how to program arcade drive with one joystick. For this example, we will be programming arcade drive using two joysticks. This type of drive is called "split arcade". In split arcade drive, the left joystick will control forward and reverse motion of the robot, and the right joystick will control turning. This is similar to how some RC cars are driven and video games are played.&#x20;

We opted to use split arcade drive during the POWERPLAY season because it allows for forward and reverse movement without worrying about accidentally pushing the joystick in the X-Axis. The POWERPLAY field requires precise movements, and split arcade drive allows teams to have more control and precision.&#x20;

Similar to the traditional arcade style driving tutorial, we will use the Dual Motor block to assign power values to our motors.&#x20;

<figure><img src="/files/VfjkFa6YyHDMvrXrzEVy" alt=""><figcaption><p>POWERPLAY Starter Bot Drive Code (Blocks)</p></figcaption></figure>

{% hint style="info" %}
Remember to reverse one of the motors and negate the values on the Y-Axis of your joysticks.&#x20;
{% endhint %}

### Lift Code&#x20;

The control of our lift arm is done by running two Core Hex Motors ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) on a Reverse Virtual Four Bar Linkage. Unlike the joystick, the DPad on a gamepad inputs are Boolean data, `FALSE/TRUE`. In order to tell the arm to move when DPad Up or DPad Down are selected, an `if/else` statement needs to be used.

For all of our button inputs we used an `if/else` statement. In the image below you can see the code for pressing the DPad. When DPadUp is pressed, both Core Hex Motors set power to -1, which moves the lift upwards. When DPadDown is pressed, the Core Hex Motors change their power to 0.8, which moves the lift downwards.

{% hint style="info" %}
Remember that when it comes to coding your robot, the Y-Axis is -1 at its topmost point, and +1 at its bottommost point, unless you negate values.
{% endhint %}

<figure><img src="/files/93rvmAqorz9WFDPfhtuU" alt=""><figcaption><p>POWERPLAY Starter Bot Lift Code (Blocks)</p></figcaption></figure>

### Intake Code

The Starter Bot's compact active roller intake features one servo motor-driven roller paired with a free spinning roller. To make sure we keep a good grip on the Cone, the intake is always running inwards. This means we need to reverse the direction of the servo to release the Cone once the robot is in position to place it.&#x20;

For the intake, we chose to use the RightBumper to control the direction and speed of the motor spinning the mechanism. In order to tell the intake to increase power when RightBumper is pressed, an `if/else` statement needs to be used.

<figure><img src="/files/gKoiIqa27850HmPoOVUQ" alt=""><figcaption><p>POWERPLAY Starter Bot Intake Code (Blocks)</p></figcaption></figure>

As you can see, if you press the RightBumper, the intake sets its power to max. Otherwise, the intake power is set to 0.3.

### Complete Blocks Program

Below is the complete Blocks Program for the POWERPLAY Starter Bot.&#x20;

<figure><img src="/files/JUHNonp883EFLjExM2P4" alt=""><figcaption><p>POWERPLAY Starter Bot Complete Code (Blocks)</p></figcaption></figure>

[Click here to download the POWERPLAY Starter Bot Blocks code.](https://revrobotics.com/content/docs/POWERPLAY-Starter-Bot-Teleop.blk)
