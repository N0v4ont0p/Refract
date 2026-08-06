> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/upgrades.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/upgrades.md).

# Upgrades

## Dual Gamepads <a href="#mecanum-drive" id="mecanum-drive"></a>

There are many ways to split robot control across two gamepads. We recommend testing different combinations with your team to decide what feels the most comfortable to you!&#x20;

This version of the program is intended to be just one example for using two gamepads. Arm and wrist control has been moved to a second gamepad while the main gamepad handles driving and the servos on the intake and claw.

{% file src="/files/ZT4GuvOSv5UgIli1PNEg" %}

The associated gamepad for a button input can be changed at any time by clicking on the block's dropdown:

<figure><img src="/files/amK5fU02z1lK9v4xvspG" alt=""><figcaption><p>Switching arm control to gamepad 2</p></figcaption></figure>

## Arcade Drive

{% file src="/files/YoHM4vnwCwfRL7fMrtuY" %}

In this example code, we changed our drive function to only be on the left stick!

<figure><img src="/files/lg62ReJ3jvbHoOjQrAWz" alt=""><figcaption><p>Arcade Drive Code</p></figcaption></figure>

[You can learn about arcade style of driving in Hello Robot!](/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks.md)

When changing a function name this will automatically change throughout the entire code to reflect the new name.

## Mecanum Drive <a href="#mecanum-drive" id="mecanum-drive"></a>

{% embed url="<https://www.youtube.com/watch?v=1UgyhhbQ40g>" %}

Upgrading to a [Mecanum Drivetrain](https://www.revrobotics.com/rev-45-2470/) (REV-45-2470) allows for new kinds of movement giving the robot the ability to strafe side-to-side across the field.

For Mecanum Drive each wheel has an individual motor!

<figure><img src="/files/JpqDg448Gc3ddfLspGzR" alt=""><figcaption><p>REV's Mecanum Drivetrain Kit V2</p></figcaption></figure>

The FTC Starter Kit V3.1 can be [upgraded to the Mecanum Drivetrain V1 following this guide.](/duo-build/ftc-starter-kit-mecanum-drivetrain.md)

#### Upgrading from the FTC Starter Kit V3.1 to Mecanum Drivetrain V2: <a href="#upgrading-from-the-ftc-starter-kit-v3-to-mecanum-drivetrain-v2" id="upgrading-from-the-ftc-starter-kit-v3-to-mecanum-drivetrain-v2"></a>

The following additional parts are needed:

* [UltraPlanetary Gearbox Kit & HD Hex Motor](https://www.revrobotics.com/rev-41-1600/) - QTY 2
* [Ultra 90 Degree Gearbox](https://www.revrobotics.com/rev-41-2080/) - QTY 4
* [75mm Mecanum Wheel Set](https://www.revrobotics.com/rev-45-1655/) - QTY 1 (set of 4)
* [M3 x 6mm HexCap Screws 50 Pack](https://www.revrobotics.com/M3-Hex-Cap-Screws/) - QTY 1
* [Expansion Hub](https://www.revrobotics.com/rev-31-1153/) (QTY 1) OR [SPARKmini Motor Controller](https://www.revrobotics.com/rev-31-1230/) (QTY 2)

[Full build instructions can be found here!](/duo-build/mecanum-drivetrain-v2.md)

### Example Mecanum Drive Program <a href="#example-mecanum-drive-program" id="example-mecanum-drive-program"></a>

How a Mecanum Drivetrain is programmed largely depends on the driver's preference for how the controller is configured.&#x20;

In our provided example, the left joystick controls forward/back and strafe then the right joystick controls turning. This code is based on the sample provided by *FIRST* in Blocks (BasicOmniOpMode).

#### Mecanum Demo Blocks Code:

{% file src="/files/7xlHnEceoo0iNuC0AEcs" %}

#### Mecanum Configuration File:

{% file src="/files/WpkBRHsoPYrc668zUwTU" %}

#### Mecanum Configuration - Control Hub and Expansion Hub

<table><thead><tr><th width="118">Port Type</th><th width="133">Hub</th><th width="136">Port Number</th><th width="249">Device Type</th><th>Name</th></tr></thead><tbody><tr><td>Motor</td><td>Control Hub</td><td>0</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>frontLeft</td></tr><tr><td>Motor</td><td>Control Hub</td><td>1</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>backLeft</td></tr><tr><td>Motor</td><td>Control Hub</td><td>2</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>frontRight</td></tr><tr><td>Motor</td><td>Control Hub</td><td>3</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>backRight</td></tr><tr><td>Servo</td><td>Control Hub</td><td>4</td><td>Servo</td><td>claw</td></tr><tr><td>Servo</td><td>Control Hub</td><td>5</td><td>Continuous Servo</td><td>intake</td></tr><tr><td>Motor</td><td>Expansion Hub</td><td>0</td><td>REV Robotics Core Hex Motor</td><td>wrist</td></tr><tr><td>Motor</td><td>Expansion Hub</td><td>1</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>arm</td></tr></tbody></table>

### Mecanum Code Breakdown

{% hint style="info" %}
Before diving into mecanum,  double check the direction your motors and wheels are turning. They may need to be reversed if you're experiencing jittering or inverted controls!

Add a ![](/files/ZbMybuCQQtDPpltXXlxt) block to change the set direction during initialization.
{% endhint %}

<figure><img src="/files/442IkAQfp4vMYj0xIAqX" alt=""><figcaption><p>Motors are set to RUN_WITHOUT_ENCODER are the beginning of the code</p></figcaption></figure>

At the very beginning of our program the drivetrain motors are set to RUN\_WITHOUT\_ENCODER.&#x20;

<figure><img src="/files/ynaMFVXTPnPw4dUxMo3Y" alt=""><figcaption><p>Our mecanum drive function</p></figcaption></figure>

We need to create some new variables in order to use mecanum. Let's break those down first:

| Variable        | Purpose                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| FB              | Moving forward and backwards                                                                         |
| Strafe          | Strafing side to side                                                                                |
| Turn            | Turning left and right                                                                               |
| leftFrontPower  | Sets the front left motor power                                                                      |
| rightFrontPower | Sets the front right motor power                                                                     |
| leftBackPower   | Sets the back left motor power                                                                       |
| rightBackPower  | Sets the back right motor power                                                                      |
| max             | This is used to check that our values do not exceed the expected range - similar to the "clip" block |

At the beginning of the MECANUM\_DRIVE function, our variables for each movement direction are being set to the value generated by the movement of the matching joystick axis.&#x20;

<figure><img src="/files/lAcLMBX5Q9UrhqtLuF7S" alt=""><figcaption><p>Forward/back is on left Y, strafe on left X, and turning on right X</p></figcaption></figure>

Since we now have four motors in play, our equation for setting the appropriate power to each motor  gets a little more complicated.&#x20;

Our robot first needs to determine the combined movement of the left stick then calculate with the right stick's value. This allows for movement when the left joystick is at an angle, such as strafing along a diagonal!

<figure><img src="/files/BJCYhZ0LPnZjWifbJvyi" alt=""><figcaption><p>Calculating motor power</p></figcaption></figure>

Next, similar to our original drivetrain code, there's a chance a value may fall outside the range of the motor's power  (-1 to 1). Therefore, we want our robot to check and bring those values back into range so we don't miss any inputs.&#x20;

<figure><img src="/files/tc3wcK7ciMP7XokHJuft" alt=""><figcaption><p>Making sure our power range is between -1 to 1</p></figcaption></figure>

For our last step, our robot sets the power of each pair of motors based on all our calculations!

<figure><img src="/files/38ng1bYeg7uRMVl9fdfA" alt=""><figcaption><p>Setting motor power</p></figcaption></figure>

## Tips, Tricks, & Upgrades Video Walkthrough

{% embed url="<https://www.youtube.com/watch?feature=youtu.be&v=hIvENLdEs3Y>" %}
