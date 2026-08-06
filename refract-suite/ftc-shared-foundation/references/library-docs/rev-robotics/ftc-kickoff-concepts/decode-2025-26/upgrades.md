> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/upgrades.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/upgrades.md).

# Upgrades

## Arcade Drive

{% file src="/files/rHd5jhylS3pwNbE8FdIZ" %}

In this example code, we changed our drive function to only be on the left stick!

<figure><img src="/files/sboqpnuupRcVRvEetdIE" alt=""><figcaption><p>Modified drivetrain function for Arcade Drive</p></figcaption></figure>

For clarity, the name of the function has been changed to arcadeDrive. In Blocks, this will automatically update it throughout our code once saved.

[You can learn about arcade style of driving in Hello Robot!](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks)

## Dual Gamepads

{% file src="/files/FGe7g5mr4Iu4mZCTb3jE" %}

There are many ways to split robot control across two gamepads. We recommend testing different combinations with your team to decide what feels the most comfortable to you!

Our example here splits driving onto gamepad1 and all launcher controls to gamepad2. If you decide to split up controls differently, all that needs to be done is the preferred gamepad needs to be chosen from the dropdown menu.&#x20;

<figure><img src="/files/m1sKp3mBNyTbTI7biaLD" alt=""><figcaption><p>Example of updating the gamepad for the feeder</p></figcaption></figure>

Gamepad controls are found in the manualCoreHexAndServoControl, setFlywheelVelocity, and splitStickArcadeDrive functions. Below is how the launcher controls look once changed for this example.&#x20;

<figure><img src="/files/wFmzNwB2InIP5rtW1YL4" alt=""><figcaption><p>Manual servo and Core Hex controls on gamepad2</p></figcaption></figure>

<figure><img src="/files/QSwgwVdteDXTUwJAINRw" alt=""><figcaption><p>Flywheel controls set to gamepad2 - manual and auto</p></figcaption></figure>

Remember to make sure the check for the servo is updated to reflect the correct gamepad as well!

<figure><img src="/files/sDgy4KvievHyM5qPt39q" alt=""><figcaption><p>Servo check updated for gamepad2</p></figcaption></figure>

## Mecanum Drive

{% embed url="<https://www.youtube.com/watch?v=duOYZcVqYTA>" %}

Upgrading to a [Mecanum Drivetrain](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/upgrades#upgrading-from-the-ftc-starter-kit-v3-to-mecanum-drivetrain-v2) (REV-45-2470) allows for new kinds of movement, giving the robot the ability to strafe side-to-side across the field.

For Mecanum Drive each wheel has an individual motor!

<figure><img src="/files/XKFz6wojY4dXxM2TiLSe" alt=""><figcaption><p>REV's Mecanum Drivetrain Kit V2</p></figcaption></figure>

#### Upgrading from the FTC Starter Kit V3.1 to Mecanum Drivetrain V2:

The following additional parts are needed:

* [15mm Plastic Inside Corner Bracket](https://www.revrobotics.com/15mm-corner-brackets/)  - QTY 2
* [UltraPlanetary Gearbox Kit & HD Hex Motor](https://www.revrobotics.com/rev-41-1600/) - QTY 2
* [Ultra 90 Degree Gearbox](https://www.revrobotics.com/rev-41-2080/) - QTY 4
* [75mm Mecanum Wheel Set ](https://www.revrobotics.com/rev-45-1655/)- QTY 1 (set of 4)
* [M3 x 6mm HexCap Screws 50 Pack](https://www.revrobotics.com/M3-Hex-Cap-Screws/) - QTY 1
* [Expansion Hub](https://www.revrobotics.com/rev-31-1153/) (QTY 1) OR [SPARKmini Motor Controller](https://www.revrobotics.com/rev-31-1230/) (QTY 2)
  * If using the SPARKmini Motor Controllers a [XT30 Power Distribution Block](https://www.revrobotics.com/rev-31-1293/) (QTY 1) is recommended

[Full build instructions can be found here!](https://docs.revrobotics.com/duo-build/mecanum-drivetrain-v2)

{% hint style="warning" %}
To upgrade this year's starter bot to mecanum, you'll need to replace the two [15mm Plastic 90 Degree Brackets](https://www.revrobotics.com/15mm-Plastic-Brackets/) with two [15mm Plastic Inside Corner Brackets](https://www.revrobotics.com/15mm-corner-brackets/). These brackets secure the rear vertical extrusion to the rear C-channel of the drivetrain. Pre-loading the corner brackets with [T-Slot Screws](https://www.revrobotics.com/rev-41-1907-pk25/?searchid=4691574\&search_query=T-Slot+Screws) would be recommended.
{% endhint %}

### Example Mecanum Drive Program

How a Mecanum Drivetrain is programmed largely depends on the driver's preference for how the gamepad is configured.

In our provided example, the left joystick controls forward/back and strafe then the right joystick controls turning. This code is based on the sample provided by *FIRST* in Blocks (BasicOmniOpMode).

### Mecanum Demo Blocks Code:

{% file src="/files/gmjsruL5SekADauUTBaD" %}

### Mecanum Configuration  - Control Hub and Expansion Hub

When adding an Expansion Hub, you will need to create a new configuration file.&#x20;

<table><thead><tr><th width="119.33331298828125">Port Type</th><th>Hub</th><th width="91.77764892578125">Port </th><th width="214.1109619140625">Device Type</th><th>Name</th></tr></thead><tbody><tr><td>Motor</td><td>Expansion</td><td>0</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>frontLeft</td></tr><tr><td>Motor</td><td>Expansion</td><td>1</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>backLeft</td></tr><tr><td>Motor</td><td>Expansion</td><td>2</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>frontRight</td></tr><tr><td>Motor</td><td>Expansion</td><td>3</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>backRight</td></tr><tr><td>Motor</td><td>Control</td><td>2</td><td>REV Robotics Core Hex Motor</td><td>coreHex</td></tr><tr><td>Motor</td><td>Control</td><td>3</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>flywheel</td></tr><tr><td>Servo</td><td>Control</td><td>0</td><td>Continuous Servo</td><td>servo</td></tr></tbody></table>

{% hint style="info" %}
[A full tutorial on programming mecanum is available here!](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-refined) Your team may need to do some testing to account for any changes in configuration or building of your mecanum drivetrain.
{% endhint %}
