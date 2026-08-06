> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop.md).

# Programming TeleOp

## Getting Started! <a href="#getting-started" id="getting-started"></a>

This year's Starter Bot program aims to offer flexibility to teams in terms of complexity. This walkthrough will begin with the basic version for Blocks. A version with autonomous built in is also available!

If your team is new to FTC, or in need of a review, we strongly recommend checking out our updated [Hello Robot Programming Guide](https://docs.revrobotics.com/duo-control/hello-robot-blocks/welcome) before diving in!

To begin, let's take a look at the configuration and actuators used in this year's design.

## Configuration <a href="#configuration" id="configuration"></a>

Before getting started with programming we needed to create a [configuration file](https://docs.revrobotics.com/duo-control/hello-robot-blocks/configuration). Below is an overview of how the robot is configured for the TeleOp code to function as expected:

<table><thead><tr><th width="113.3333740234375">Port Type</th><th width="115.888916015625">Port Number</th><th>Device Type</th><th>Name</th></tr></thead><tbody><tr><td>Motor</td><td>0</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>rightDrive</td></tr><tr><td>Motor</td><td>1</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>leftDrive</td></tr><tr><td>Motor</td><td>2</td><td>REV Robotics Core Hex Motorr</td><td>coreHex</td></tr><tr><td>Motor</td><td>3</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>flywheel</td></tr><tr><td>Servo</td><td>0</td><td>Continuous Servo</td><td>servo</td></tr></tbody></table>

## Configuration File Download <a href="#configuration-file-download" id="configuration-file-download"></a>

Right click the file below and select "save link as". To put this configuration file on your robot, drag this file into the "FIRST" folder of your Control Hub's file system.

{% file src="/files/dmYtknVl3j00Z09aIIXg" %}

You will need to activate the configuration using the Driver Hub before proceeding. [Click here to learn more about the configuration process.](https://docs.revrobotics.com/duo-control/hello-robot-blocks/configuration#the-importance-of-configuration)

## Wiring Diagram

<figure><img src="/files/vTnt1IIflQKOp7lwE9Jh" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="122.3333740234375">Device Name</th><th>Device Type</th><th>Port</th></tr></thead><tbody><tr><td>rightDrive</td><td>UltraPlanetary Gearbox Kit and HD Hex Motor</td><td>Motor/Encoder Port 0</td></tr><tr><td>leftDrive</td><td>UltraPlanetary Gearbox Kit and HD Hex Motor</td><td>Motor/Encoder Port 1</td></tr><tr><td>coreHex</td><td>Core Hex Motor</td><td>Motor/Encoder Port 2</td></tr><tr><td>flywheel</td><td>UltraPlanetary Gearbox Kit and HD Hex Motor</td><td>Motor/Encoder Port 3</td></tr><tr><td>servo</td><td>Smart Robot Servo - set to CR mode</td><td>Servo Port 0</td></tr></tbody></table>

{% hint style="info" %}
The Smart Robot Servo can be changed to [continuous mode using the SRS Programmer!](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer)
{% endhint %}

## Gamepad Setup

The 2025-26 REV DUO FTC Starter Bot is designed to use a split arcade drive for the default. Check out our Upgrades page for the arcade drive version of the program.

In split arcade drive, the left joystick will control forward and reverse motion of the robot, and the right joystick will control turning. This is similar to how some RC cars are driven and video games are played.

{% hint style="info" %}
Not all gamepads have buttons labeled the same way. Check the manufacturer's documentation for accurate button mapping.
{% endhint %}

### 2025-26 REV DUO FTC Starter Bot Gamepad Layout:

<figure><img src="/files/YiqZsNVLemgZIQ0EPRDO" alt=""><figcaption></figcaption></figure>

| Gamepad Input        | Function                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| Right Joystick       | Turn left and right                                                                                       |
| Left Joystick        | Drive forward and reverse                                                                                 |
| Home/PS Button       | Cycle OpModes during Initialization  (Auto code only)                                                     |
| Right Bumper         | Activates flywheel, feeder Core Hex, and agitator servo to automatically fire at "bank shot" (near) range |
| Left Bumper          | Activates flywheel, feeder Core Hex, and agitator servo to automatically fire at "far shot" range         |
| Left Dpad/Right Dpad | Manually rotate agitator servo                                                                            |
| Y/Triangle           | Manually spins the Core Hex at half speed                                                                 |
| A/Cross              | Manually spins the Core Hex at half speed                                                                 |
| B/Circle             | Manually spins flywheel to "bank shot" (near) velocity                                                    |
| X/Square             | Manually spins flywheel to "max" velocity                                                                 |
| M1 (back button)     | Manually spins flywheel to "bank shot" (near) velocity                                                    |
| M2 (back button)     | Manually spins flywheel to "max" velocity                                                                 |
| Options              | Runs the flywheel motor in reverse                                                                        |

More information on programming gamepads for use with your robot can be found at [Hello Robot - Using Gamepads](https://docs.revrobotics.com/duo-control/hello-robot-blocks/using-a-gamepad).

{% hint style="warning" %}
The REV USB PS4 Compatible Gamepad (REV-31-2983) has two remappable M-buttons on the back side of the controller. For this program, we advise reprogramming them to be the Circle and Square buttons!

[Please see the guide here for how to remap](https://docs.revrobotics.com/rev-crossover-products/gamepad/remapping-guide).&#x20;
{% endhint %}

## Basic TeleOp Program Downloads

### Blocks:

[Check out *FIRST*'s guide on uploading a Blocks program!](https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.html#uploading-blocks)

{% file src="/files/PQ0RKb3XLYcmhLI41jeF" %}

### OnBot Java:&#x20;

{% file src="/files/ue7rq8rrPvadgqhTqQXP" %}

## TeleOp with Autonomous Program Downloads

### Blocks Auto:

{% hint style="success" %}
Please see the [Autonomous Program section of this guide](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-initialization.md) to learn how to switch between the program that will run!
{% endhint %}

[Check out *FIRST*'s guide on uploading a Blocks program!](https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.html#uploading-blocks)

{% file src="/files/YMpjg4B5UAdopdMbqczR" %}

### OnBot Java Auto:

{% file src="/files/k6SQV73mB1YnnrqIKVry" %}

Any updates to our example programs are documented in our changelog.

#### The following pages will dig deeper into unraveling the secrets behind this code. Grab your pickaxe and let's get started!

|                                                          Quick Links                                                          |
| :---------------------------------------------------------------------------------------------------------------------------: |
|     [Initialization and Variables](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-initialization.md)     |
|                 [Main Loop](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-main-loop.md)                 |
|          [Flywheel Control](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-flywheel-control.md)          |
|  [Manual Control and Drive](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-manual-control-and-drive.md)  |
| [Autonomous Initialization](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-initialization.md) |
|           [Autonomous Code](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-code.md)           |
|       [OnBot Java Overview](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-onbot-java-overview.md)       |

## Programming Walkthrough Video

{% embed url="<https://www.youtube.com/watch?t=170s&v=ogRBIn5wP74>" %}

### Programming Autonomous Video Walkthrough

{% embed url="<https://www.youtube.com/watch?v=Th4NfjHg0c8>" %}
