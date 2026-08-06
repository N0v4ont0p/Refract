> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2.md).

# Part 2: Robot Control

Thus far we've tackled a lot of the basics to get parts of our robot moving in response to our gamepad or sensors. So what comes next?&#x20;

In Part 2 of Hello Robot we're going to look at working with a full, functional robot. By the end of this section your robot will be able controlled with the gamepad!

{% hint style="info" %}
Before continuing it is recommended to complete, at minimum, a drivetrain. There are a few different options depending on the kit being used. We recommend looking at the [C-Channel Drivetrain](https://docs.revrobotics.com/duo-build/channel-drivetrain-build-guide), such as what is used with our [Starter Bot program](https://docs.revrobotics.com/ftc-kickoff-concepts), or the Class Bot V2!&#x20;

For this guide the Class Bot V2 is used. [Check out the build guide for full building instructions](https://docs.revrobotics.com/duo-build/ftc-starter-kit-class-bot) for the Class Bot V2!
{% endhint %}

## Create a Basic Robot&#x20;

The graphic below highlights the major hardware components of the Class Bot V2. These components are important to understand for the configuration process.&#x20;

<figure><img src="/files/mhP8eTklWMmpInXlbqci" alt=""><figcaption></figcaption></figure>

The [Hello Robot - Configuration ](/duo-control/hello-robot-blocks/configuration.md)section focused on configuring the components in the Test Bed.&#x20;

In order to continue forward with the Robot Control programming sections, additional motors must be added. It is your choice what variable names you would like to assign to your robot, but for reference this guide will use the following names for each hardware component.&#x20;

| Hardware Component | Hardware Type                            | Name        |
| ------------------ | ---------------------------------------- | ----------- |
| Right Drive Motor  | REV Robotics UltraPlanetary HD Hex Motor | rightmotor  |
| Left Drive Motor   | REV Robotics UltraPlanetary HD Hex Motor | leftmotor   |
| Arm Motor          | REV Robotics Core Hex Motor              | arm         |
| Touch Sensor       | REV Touch Sensor                         | test\_touch |

## Drivetrain Basics&#x20;

Before continuing it is important to understand the mechanical behavior of different drivetrains. The two most common drivetrain categories types are Differential and Omnidirectional. &#x20;

<figure><img src="/files/79mWIJXGP6BCnAztDpEb" alt=""><figcaption></figcaption></figure>

**Differential Drivetrains** are the standard starting drivetrain. They are able to move in forward/reverse, as well as rotate either direction around a central point. There are different styles of directional drivetrains depending on the type of wheels, number of motors, and wheel positions. These include 4WD, 6WD, West Coast, and C-Channel drivetrains.

By comparison, **omnidirectional drivetrains** can move in any direction with each wheel typically being controlled separately. This allows for advanced forms of navigation, such as strafing, but requires a more complex program. Omnidirectional drivetrains include the use of omni wheels in Y or X configurations, mecanum wheel drivetrains, swerve drive, and other forms of holonomic drives.&#x20;

{% hint style="info" %}
The Class Bot V2 uses a directional drivetrain, which will be the drivetrain of focus for this tutorial!
{% endhint %}

## Teleoperated Control Types

While driving our robot with teleop control, we will be giving the robot inputs from our gamepad connected to our Driver Hub. Its job is to translate those inputs to the robot to perform the specified actions. How your robot drives and what joystick does what can be largely dependent on what you or your team's driver is comfortable using. Let's take a look at two of the more common methods of control: Tank Drive and Arcade Drive.

### Tank Drive

For tank drive, each side of the differential drivetrain is mapped to its own joystick so both will be used. Changing the position of each joystick allows the drivetrain to steer and change its heading. Sample code exists in the Robot Controller Application to control a differential drivetrain in this way.

### Arcade Drive

For arcade drive, each side of the differential drivetrain is controlled by a single joystick. Changing position of the joystick changes the power applied to each side of the drivetrain allowing for a given command.&#x20;

Arcade drives typically have left/right movement of the joystick set to spin the robot about its axis with forward/back moving the robot forward and reverse.&#x20;

{% hint style="info" %}
Arcade Drive may also be configured as a Split Arcade Drive where one joystick turns the robot while the other controls forward/back. An example of a Split Arcade Drive robot can be found as part of our [2023-24 Starter Bot.](https://docs.revrobotics.com/ftc-kickoff-concepts/centerstage-2023-2024/programming-teleop#split-arcade-drive)&#x20;
{% endhint %}
