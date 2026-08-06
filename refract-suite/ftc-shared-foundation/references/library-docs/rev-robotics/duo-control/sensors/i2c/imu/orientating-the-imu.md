> Source: https://docs.revrobotics.com/duo-control/sensors/i2c/imu/orientating-the-imu.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/i2c/imu/orientating-the-imu.md).

# Orientating the IMU

## Setting Orientation in Code:

### Blocks:

The IMU Blocks can be found under the Sensors dropdown menu:

<figure><img src="/files/RfVF692fDulIAViXt7kK" alt="" width="185"><figcaption><p>IMU listings on a Control Hub with a BNO055</p></figcaption></figure>

There are a few different ways to define the Hub's orientation. The easiest is by using the REV Robotics logo and USB ports to signify orientation:

<figure><img src="/files/FAurJtbnOHf3AAm6rlQ4" alt=""><figcaption><p>This Control Hub is flat with the logo up and USBs pointed towards the front of the robot.</p></figcaption></figure>

However, if the Hub is not flat you may also define its location using an orientation perimeter block:

<figure><img src="/files/Cqz0lkXwxv0g9QAcqKYb" alt=""><figcaption></figcaption></figure>

This method uses a perimeter object to specify the Hub's arbitrary orientation on the robot by describing the rotation that would need to be applied in order to rotate the Hub from its default to the actual orientation. A similar method using a Quaternion block is also available.

The default position assumes the logo is UP and USBs are FORWARD.&#x20;

### OnBot Java:

During the initialization process the following can be used to define the Hub's orientation:

```java
RevHubOrientationOnRobot.LogoFacingDirection logoDirection = RevHubOrientationOnRobot.LogoFacingDirection.UP;
RevHubOrientationOnRobot.UsbFacingDirection  usbDirection  = RevHubOrientationOnRobot.UsbFacingDirection.FORWARD;

RevHubOrientationOnRobot orientationOnRobot = new RevHubOrientationOnRobot(logoDirection, usbDirection);

imu.initialize(new IMU.Parameters(orientationOnRobot));
```

This method sets the orientation based on the position of the REV Robotics and USBs while the Hub is sitting flat orthogonally.&#x20;

It is also possible to define the orientation of a Hub in a nonorthogonal position by setting rotations along the X, Y, and Z axes. For more information on this process, please see the "SensorIMUNonOrthogonal" sample available in OnBot Java as part of the FTC SDK.

## Recommended Orientations

### Control Hubs with the Bosch BHI260AP IMU:&#x20;

For the most accurate readings from the Bosch BHI260AP IMU, it is recommended to have the Control Hub mounted flat on a horizontal plane.&#x20;

### Control and Expansion Hubs with the Bosch BNO055 IMU:

For the most accurate readings from the Bosch BNO055 IMU, it is recommend to have the Hub mounted flat on a horizontal OR vertical plane.&#x20;
