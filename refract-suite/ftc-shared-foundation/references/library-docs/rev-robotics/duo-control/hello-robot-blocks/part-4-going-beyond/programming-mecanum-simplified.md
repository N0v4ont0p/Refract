> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-simplified.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-simplified.md).

# Programming Mecanum - Simplified

{% hint style="info" %}
This example is a simplified form of a mecanum drivetrain code intended to review the basics of mecanum movement and is not recommended for a FTC robot.&#x20;

Check out [Programming Mecanum - Refined](/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-refined.md)  for a competition ready example!
{% endhint %}

## Configuration <a href="#configuration" id="configuration"></a>

Before getting started with programming we needed to create a configuration file. Below is an overview of how the robot is configured for the TeleOp code to function as expected:

<table><thead><tr><th>Port Type</th><th width="160">Port Number</th><th>Device Type</th><th>Name</th></tr></thead><tbody><tr><td>Motor</td><td>0</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>frontLeft</td></tr><tr><td>Motor</td><td>1</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>frontRight</td></tr><tr><td>Motor</td><td>2</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>backLeft</td></tr><tr><td>Motor</td><td>3</td><td>REV Robotics Ultraplanetary HD Hex Motor</td><td>backRight</td></tr></tbody></table>

### Example Program:

{% file src="/files/BC2PThuijZvXKWzcdrSy" %}

## Gamepad Layout: <a href="#gamepad-layout" id="gamepad-layout"></a>

| Gamepad Input                              | Function                         |
| ------------------------------------------ | -------------------------------- |
| Left Joystick - Left/Right on X-Axis       | Strafe Left/Right                |
| Left Joystick - Forward/Backward on Y-Axis | Forward/Backward                 |
| Right Joystick - Left/Right on X-Axis      | Turn Counter-Clockwise/Clockwise |

## Programming Teleop - Blocks

### Initialization: <a href="#initialization" id="initialization"></a>

{% hint style="info" %}
Before diving into mecanum, double check the direction your motors and wheels are spinning. They may need to be reversed if you're experiencing jittering or inverted controls!

Adjust the ![](https://docs.revrobotics.com/~gitbook/image?url=https%3A%2F%2F268621232-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MHCAE012xNfg1h3SM9v%252Fuploads%252Fsd50OrsprUDav0TPnrSt%252Fimage.png%3Falt%3Dmedia%26token%3Dca1e5857-bb4c-48c3-a2e2-54044e9fc94b\&width=300\&dpr=4\&quality=100\&sign=d3125b20\&sv=1) block to change the set direction during initialization.
{% endhint %}

For this program, we'll set the motors to RUN\_WITHOUT\_ENCODER along with their direction

<figure><img src="/files/JVK37YhMCOXqHpbDQNSo" alt="" width="534"><figcaption><p>Setting up the motors</p></figcaption></figure>

### Moving Forward and Backwards: <a href="#moving-forward-and-back" id="moving-forward-and-back"></a>

For a mecanum drivetrain all 4 motors will be given a command to follow when the left joystick is moved along the Y-axis of the joystick. For moving forward and back all wheels must turn the same direction.&#x20;

[Recall that the Y-axis on the gamepad must be inverted.](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-motors/programming-a-motor-with-a-gamepad#adjusting-y-axis-direction)

<figure><img src="/files/7UUSWC2NxBtz07cgBBba" alt="" width="465"><figcaption><p>All four motors are set to move in the same direction</p></figcaption></figure>

### Strafing: <a href="#strafing" id="strafing"></a>

For this example, strafing is controlled by the left stick's X-axis allowing the robot to slide left and right. In order to achieve this movement, the motors move in diagonal pairs, so frontLeft and backRight will move the opposit direction of backLeft and frontRight, similar to the X shape the wheels make.&#x20;

<figure><img src="/files/O4DmApaUPf8mMrlUxc1a" alt="" width="470"><figcaption><p>Two motors will run in the opposite direction when strafing!</p></figcaption></figure>

### Turning: <a href="#turning" id="turning"></a>

Lastly, we have turning set by itself on the right joystick's X-axis. To turn our left and right pairs of wheels will spin in opposite directions.&#x20;

<figure><img src="/files/f7DwESxKppiY6Mq60xOX" alt="" width="457"><figcaption><p>When turning the front and back motors rotate in opposite directions.</p></figcaption></figure>

{% hint style="info" %}
This version of the mecanum program does not account for diagonal movements of the joystick. Check out [Programing Mecanum - Refined](/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-refined.md) to create a fully responsive mecanum drive!
{% endhint %}
