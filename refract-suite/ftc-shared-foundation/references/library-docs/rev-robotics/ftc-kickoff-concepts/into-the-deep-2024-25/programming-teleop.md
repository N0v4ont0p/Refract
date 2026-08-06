> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop.md).

# Programming TeleOp

## Getting Started!

This year's Starter Bot program offers a slightly more technical solution than previous years. If your team is new to FTC, or in need of a review, we strongly recommend checking out our updated [Hello Robot Programming Guide](/duo-control/hello-robot-blocks/welcome.md) before diving in!&#x20;

To begin, let's take a look at the configuration and actuators used in this year's design.&#x20;

## Configuration

Before getting started with programming we needed to create a [configuration file](/duo-control/hello-robot-blocks/configuration.md). Below is an overview of how the robot is configured for the TeleOp code to function as expected:

<table><thead><tr><th width="127">Port Type</th><th width="134">Port Number</th><th width="362">Device Type</th><th>Name</th></tr></thead><tbody><tr><td>Motor</td><td>0</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>arm</td></tr><tr><td>Motor</td><td>1</td><td>REV Robotics Core Hex Motor</td><td>wrist</td></tr><tr><td>Motor</td><td>2</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>leftDrive</td></tr><tr><td>Motor</td><td>3</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>rightDrive</td></tr><tr><td>Servo</td><td>4</td><td>Servo</td><td>claw</td></tr><tr><td>Servo</td><td>5</td><td>Continuous Servo</td><td>intake</td></tr></tbody></table>

## Configuration File Download

Right click the file below and select "save link as". To put this configuration file on your robot, drag this file into the "FIRST" folder of your Control Hub's file system.&#x20;

{% file src="/files/ECGKQvK5kbbta5zhRnO8" %}

You will need to activate the configuration using the Driver Hub before proceeding. [Click here to learn more about the configuration process. ](/duo-control/hello-robot-blocks/configuration.md#the-importance-of-configuration)

## Wiring Diagram

<figure><img src="/files/lYxxNCTijYZyb9bNsOMx" alt=""><figcaption><p>Wiring diagram for the 2024-25 Starter Bot</p></figcaption></figure>

<table><thead><tr><th width="147">Device Name</th><th width="382">Device Type</th><th>Port</th></tr></thead><tbody><tr><td>arm</td><td>UltraPlanetary Gearbox Kit and HD Hex Motor</td><td>Motor/Encoder Port 0</td></tr><tr><td>wrist</td><td>Core Hex Motor</td><td>Motor/Encoder Port 1</td></tr><tr><td>leftDrive</td><td>UltraPlanetary Gearbox Kit and HD Hex Motor</td><td>Motor/Encoder Port 2</td></tr><tr><td>rightDrive</td><td>UltraPlanetary Gearbox Kit and HD Hex Motor</td><td>Motor/Encoder Port 3</td></tr><tr><td>claw</td><td>Smart Robot Servo</td><td>Servo Port 4</td></tr><tr><td>intake</td><td>Smart Robot Servo - set to continuous mode</td><td>Servo Port 5</td></tr></tbody></table>

{% hint style="info" %}
The Smart Robot Servo can be changed to [continuous mode using the SRS Programmer!](/rev-crossover-products/servo/srs-programmer.md)
{% endhint %}

## Gamepad Setup

The 2024-25 REV DUO FTC Starter Bot is designed to use a split arcade drive for the default. Check out our [Upgrades](/ftc-kickoff-concepts/into-the-deep-2024-25/upgrades.md) page for the arcade drive version of the program.

In split arcade drive, the left joystick will control forward and reverse motion of the robot, and the right joystick will control turning. This is similar to how some RC cars are driven and video games are played.

{% hint style="info" %}
Not all gamepads have buttons labeled the same way. Check the manufacturer's documentation for accurate button mapping.
{% endhint %}

### 2024-25 REV DUO FTC Starter Bot Gamepad Layout:

<figure><img src="/files/mR8l1wvvRRtyNOTFiIVt" alt=""><figcaption></figcaption></figure>

| Gamepad Input  | Function                                                                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Right Joystick | Turn left and right                                                                                                                                   |
| Left Joystick  | Drive forward and reverse                                                                                                                             |
| A/Cross        | <p>Intake Preset Position</p><ul><li>Arm down, wrist out</li></ul>                                                                                    |
| B/Circle       | <p>Wall Grab and Unhook Preset Position</p><ul><li>Arm up to grab, wrist in - first click</li><li>Arm up to unhook, wrist in - second click</li></ul> |
| Y/Triangle     | <p></p><p>Hover High and Clip High Preset Position</p><ul><li>Arm up to low basket height, wrist in</li><li>Arm lower to clip, wrist in</li></ul>     |
| X/Square       | <p></p><p>Low Basket Preset Position</p><ul><li>Arm up to low basket height, wrist out</li></ul>                                                      |
| D-pad Up       | Arm Up                                                                                                                                                |
| D-pad Down     | Arm Down                                                                                                                                              |
| D-pad Left     | Wrist Out                                                                                                                                             |
| D-pad Right    | Wrist In                                                                                                                                              |
| Left Bumper    | Reset arm/wrist to Initialization Position                                                                                                            |
| Right Bumper   | Claw toggle to open or close                                                                                                                          |
| Left Trigger   | Reverse intake flaps                                                                                                                                  |
| Right Trigger  | Run intake flaps                                                                                                                                      |

More information on programming gamepads for use with your robot can be found at [Hello Robot - Using Gamepads](/duo-control/hello-robot-blocks/using-a-gamepad.md).

{% hint style="warning" %}
The REV USB PS4 Compatible Gamepad (REV-31-2983) has two remappable M-buttons on the back side of the controller. By default, these are mapped to circle and cross.

[Please see the product page for directions on remapping these buttons. ](https://www.revrobotics.com/rev-31-2983/)
{% endhint %}

## TeleOp Program Downloads

#### Blocks (v1.0.2):

[Check out *FIRST*'s guide on uploading a Blocks program!](https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.html#uploading-blocks)

{% file src="/files/xdZHNI3RFnVYI8HnGeJt" %}

#### Java (v1.0.1):

{% file src="/files/Q3GHcrK93gumK4Mwl9SL" %}

{% hint style="info" %}
A version of the Blocks program without the arm and wrist motors moving to an initialization position is now available on start up on our [Tips & Tricks page. ](/ftc-kickoff-concepts/into-the-deep-2024-25/build-tips-and-tricks.md#starter-bot-programming-teleop-without-initialization)
{% endhint %}

Any updates to our example programs are documented in our [changelog. ](/ftc-kickoff-concepts/into-the-deep-2024-25/starter-bot-changelog-2024-25.md)

#### The following pages will be a deep dive into the Blocks code, grab your snorkel and let's get started!

|                                                                                    Quick Links                                                                                   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                           [Initialization and Variables](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-initialization.md)                           |
|                              [Creating Functions](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-creating-functions.md)                              |
| [Controlling the Arm and Wrist - Preset Positions](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-controlling-the-arm-and-wrist.md#preset-movements) |
|   [Controlling the Arm and Wrist - Manual Movement](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-controlling-the-arm-and-wrist.md#manual-control)  |
|                          [Intake ](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-intake-and-claw-toggle.md#intake-control)                          |
|                      [Claw Toggle](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-intake-and-claw-toggle.md#claw-toggle-control)                     |
|                   [Split Arcade Drive](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-driving-and-telemetry.md#split-arcade-drive)                   |
|                            [Telemetry](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-driving-and-telemetry.md#telemetry)                            |

## Video Walkthrough&#x20;

{% embed url="<https://www.youtube.com/watch?t=4s&v=LxAXkyWiyjE>" %}
Starter Bot Programming Walkthrough
{% endembed %}
