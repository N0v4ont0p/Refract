> Source: https://pedropathing.com/docs/pathing/tuning/localization · Fetched: 2026-07-12

# Pedro Pathing — Localization & Localizer Tuning

> Source: https://pedropathing.com/docs/pathing/tuning/localization · Fetched: 2026-07-12

## Localization

There are many localizers for you to choose from. If you don't have any, you
can use your drive motor encoders.

All localizers except for the OTOS localizer
use a pose exponential method of localization, a way of turning movements
from the robot's coordinate frame to the global coordinate frame.

### Localizers

**Select your localizer below and follow the instructions to tune it. Once
your localizer is tuned, come back to this page.**

- [**Drive Encoder Localizer**](https://pedropathing.com/docs/pathing/tuning/localization/drive-encoder) — A localizer that uses the drive motor encoders.
- [**Two Wheel Localizer**](https://pedropathing.com/docs/pathing/tuning/localization/two-wheel) — A localizer that uses two odometry wheels.
- [**Three Wheel Localizer**](https://pedropathing.com/docs/pathing/tuning/localization/three-wheel) — A localizer that uses three odometry wheels.
- [**Three Wheel + IMU Localizer**](https://pedropathing.com/docs/pathing/tuning/localization/three-wheel-imu) — A localizer that uses three odometry wheels and an IMU.
- [**Pinpoint Localizer**](https://pedropathing.com/docs/pathing/tuning/localization/pinpoint) — A localizer that uses the goBILDA Pinpoint Odometry Computer.
- [**OTOS Localizer**](https://pedropathing.com/docs/pathing/tuning/localization/otos) — A localizer that uses the SparkFun Optical Tracking Odometry Sensor.

### Localization Test

After completing the tuning steps described in your localizer, you can test the accuracy of it.

1. Run the `Tuning` OpMode, then navigate under to `Localization Test`
2. On your computer, connect to your robot's Wi-Fi, and navigate to Panels or the FTC Dashboard. Panels is accessible at the ip address `192.168.43.1:8001` when connected to robot wifi.
3. You should see the robot's position on the field.
4. Observe the movements, make sure moving forward increases `x` and strafing left increases `y`.

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/two-wheel · Fetched: 2026-07-12

## Two Wheel

> **Prerequisites:**
> Ensure that two odometry pods are connected: one that is parallel to the length
> of your chassis and another that is perpendicular to your chassis length. These should be plugged
> into ports that have motors on them preferably. Due to technical limitations on REV hubs, encoder ports
> 0 and 3 are the fastest and are recommended for both pods

### Setup

In `Constants.java`, add an instance of `TwoWheelConstants`. Make sure to replace the hardware map names
with the actual names of the motor port they are plugged into. You must also set the
IMU orientation to match the orientation of your Control Hub.

```java title="Constants.java"
public static TwoWheelConstants localizerConstants = new TwoWheelConstants()
        .forwardEncoder_HardwareMapName("leftFront")
        .strafeEncoder_HardwareMapName("rightRear")
        .IMU_HardwareMapName("imu")
        .IMU_Orientation(
            new RevHubOrientationOnRobot(
                RevHubOrientationOnRobot.LogoFacingDirection.UP,
                RevHubOrientationOnRobot.UsbFacingDirection.LEFT
            )
        );
```

Then, add `.twoWheelLocalizer` to `createFollower`:

```java title="Constants.java"
return new FollowerBuilder(followerConstants, hardwareMap)
    .twoWheelLocalizer(localizerConstants)
    /* other builder steps */
    .build();
```

#### Offsets

Offsets can be found **manually** or **automatically**:

- **Automatic**: Use the [offsets tuner](/docs/pathing/tuning/localization/offsets-tuner)
- **Manual**: Use the diagram below (offsets are in inches)

Set your odometry pod offsets to define where they are relative to your robot's center of rotation.

<img
  className="inline-block dark:hidden"
  src="/docs/odometry-light.png"
  alt="Odometry Pod Offset Diagram"
/>

<img
  className="hidden dark:inline-block"
  src="/docs/odometry-dark.png"
  alt="Odometry Pod Offset Diagram"
/>

Once you have found your offsets, add them to your localizer constants by
using `.forwardPodY()` and `.strafePodX()`.

### Tuning

#### Encoder Directions

We will now determine the encoder directions. First, select and run
localization test under the localization folder in the tuning OpMode. Then,
move the robot forward. The x coordinate should increase. Next, move the
robot left. The y coordinate should increase. If either of those does not
happen, you must reverse the respective encoder. To reverse an encoder, add

To reverse an encoder, add one of the following to `TwoWheelConstants`:

```java title="Constants.java"
.forwardEncoderDirection(Encoder.REVERSE)

// and/or:

.strafeEncoderDirection(Encoder.REVERSE)
```

#### Forward Tuner

We will now adjust multipliers that convert encoder ticks into real-world
measurements: inches. This ensures your localizer's readings are accurate.

> **Tip:**
> It is recommended that you run these tests multiple times and average the results,
> as it can result in more accurate localization.

In the tuning OpMode, under localization, select and start the forward tuner.
Then, push the robot **forward 48 inches** (exactly 2 field tiles). This
distance is configurable if needed. Once you push the robot forward, two
numbers will be displayed on telemetry:

- The distance the robot thinks it has traveled
- The multiplier; this is the number you want.

Add the multiplier to your `TwoWheelConstants` by adding the following.

```java title="Constants.java"
.forwardTicksToInches(multiplier)
```

#### Lateral Tuner

The lateral tuner is very similar to the forward tuner, except it is
sideways. In the tuning OpMode, under localization, select and start the
lateral tuner. Push the robot **left 48 inches** (exactly 2 field tiles). As
with the forward tuner, this distance is configurable.

Lastly, add the multiplier to `TwoWheelConstants` by adding the following line.

```java title="Constants.java"
.strafeTicksToInches(multiplier)
```

### Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/three-wheel · Fetched: 2026-07-12

## Three Wheel

> **Prerequisites:**
> Ensure that three odometry pods are connected: two that are parallel to the length
> of your chassis and another that is perpendicular to your chassis length. These should be plugged
> into ports that have motors on them preferably. Due to technical limitations on REV hubs, encoder ports
> 0 and 3 are the fastest and are recommended for the two parallel pods.

### Setup

In `Constants.java`, add an instance of `ThreeWheelConstants`. Make sure to replace the hardware map names
with the actual names of the motor port they are plugged into.

```java title="Constants.java"
public static ThreeWheelConstants localizerConstants = new ThreeWheelConstants()
            .forwardTicksToInches(.001989436789)
            .strafeTicksToInches(.001989436789)
            .turnTicksToInches(.001989436789)
            .leftPodY(1)
            .rightPodY(-1)
            .strafePodX(-2.5)
            .leftEncoder_HardwareMapName("leftFront")
            .rightEncoder_HardwareMapName("rightRear")
            .strafeEncoder_HardwareMapName("rightFront")
            .leftEncoderDirection(Encoder.FORWARD)
            .rightEncoderDirection(Encoder.FORWARD)
            .strafeEncoderDirection(Encoder.FORWARD);
```

Then, add `.threeWheelLocalizer` to `createFollower`:

```java title="Constants.java"
return new FollowerBuilder(followerConstants, hardwareMap)
    .threeWheelLocalizer(localizerConstants)
    /* other builder steps */
    .build();
```

#### Offsets

You must also set your odometry pod offsets, which are
relative to your robot's center of rotation. You can use the diagram below
to find them. **Offsets are in inches.**

<img
  className="inline-block dark:hidden"
  src="/docs/odometry-light.png"
  alt="Odometry Pod Offset Diagram"
/>

<img
  className="hidden dark:inline-block"
  src="/docs/odometry-dark.png"
  alt="Odometry Pod Offset Diagram"
/>

Once you have found your offsets, add them to your localizer constants by
using `.leftPodY()`, `.rightPodY()` and `.strafePodX()`.

### Encoder Directions

We will now determine the encoder directions. First, select and run
localization test under the localization folder in the tuning OpMode. Then,
move the robot forward. The x coordinate should increase. Next, move the
robot left. The y coordinate should increase. If these do not happen, the
respective encoders must be the inverse of what they currently are (NOTE:
both parallel pods must be inversed if the x coordinate decreases).
To reverse an encoder, add

To reverse an encoder, add one of the following to `ThreeWheelConstants`:

```java title="Constants.java"
.leftEncoderDirection(Encoder.REVERSE)
.rightEncoderDirection(Encoder.FORWARD)

// and/or:

.strafeEncoderDirection(Encoder.REVERSE)
```

> **Important:**
> If when you push the robot forward both x and y change, it is likely that either your offsets have the wrong sign,
> or that the hardwareMap is incorrect (ie. forward encoder is actually your strafe encoder and vise versa)

### Forward Tuner

We will now adjust multipliers that convert encoder ticks into real-world
measurements: inches. This ensures your localizer's readings are accurate.

> **Tip:**
> It is recommended that you run these tests multiple times and average the results,
> as it can result in more accurate localization.

In the tuning OpMode, under localization, select and start the forward tuner.
Then, push the robot **forward 48 inches** (exactly 2 field tiles). This
distance is configurable if needed. Once you push the robot forward, two
numbers will be displayed on telemetry:

- The distance the robot thinks it has traveled
- The multiplier; this is the number you want.

Add the multiplier to your `ThreeWheelConstants` by adding the following.

```java title="Constants.java"
.forwardTicksToInches(multiplier)
```

### Lateral Tuner

The lateral tuner is very similar to the forward tuner, except it is
sideways. In the tuning OpMode, under localization, select and start the
lateral tuner. Push the robot **left 48 inches** (exactly 2 field tiles). As
with the forward tuner, this distance is configurable.

Lastly, add the multiplier to `ThreeWheelConstants` by adding the following line.

```java title="Constants.java"
.strafeTicksToInches(multiplier)
```

### Turn Tuner

The turn tuner is similar to both the forward tuner and lateral tuner, except it is
rotational. Place the robot so it aligns to a fixed reference point (e.g., edge of a field tile).
In the tuning OpMode, under localization, select and start the
turn tuner. Rotate the robot **counterclockwise one full rotation**. As
with the previous tuners, this amount is configurable.

Lastly, add the multiplier to `ThreeWheelConstants` by adding the following line.

```java title="Constants.java"
.turnTicksToInches(multiplier)
```

### Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/three-wheel-imu · Fetched: 2026-07-12

## Three Wheel + IMU

> **Prerequisites:**
> Ensure that three odometry pods are connected: two that are parallel to the length
> of your chassis and another that is perpendicular to your chassis length. These should be plugged
> into ports that have motors on them preferably. Due to technical limitations on REV hubs, encoder ports
> 0 and 3 are the fastest and are recommended for the two parallel pods.

### Setup

In `Constants.java`, add an instance of `ThreeWheelIMUConstants`. Make sure to replace the hardware map names
with the actual names of the motor port they are plugged into. You must also set the IMU orientation to match the orientation of your Control Hub.

```java title="Constants.java"
public static ThreeWheelIMUConstants localizerConstants = new ThreeWheelIMUConstants()
            .forwardTicksToInches(.001989436789)
            .strafeTicksToInches(.001989436789)
            .turnTicksToInches(.001989436789)
            .leftPodY(1)
            .rightPodY(-1)
            .strafePodX(-2.5)
            .leftEncoder_HardwareMapName("leftFront")
            .rightEncoder_HardwareMapName("rightRear")
            .strafeEncoder_HardwareMapName("rightFront")
            .leftEncoderDirection(Encoder.FORWARD)
            .rightEncoderDirection(Encoder.FORWARD)
            .strafeEncoderDirection(Encoder.FORWARD)
            .IMU_HardwareMapName("imu")
            .IMU_Orientation(new RevHubOrientationOnRobot(RevHubOrientationOnRobot.LogoFacingDirection.UP, RevHubOrientationOnRobot.UsbFacingDirection.LEFT));
```

Then, add `.threeWheelIMULocalizer` to `createFollower`:

```java title="Constants.java"
return new FollowerBuilder(followerConstants, hardwareMap)
    .threeWheelIMULocalizer(localizerConstants)
    /* other builder steps */
    .build();
```

#### Offsets

You must also set your odometry pod offsets, which is where they are
relative to your robot's center of rotation. You can use the diagram below
to find them. **Offsets are in inches.**

<img
  className="inline-block dark:hidden"
  src="/docs/odometry-light.png"
  alt="Odometry Pod Offset Diagram"
/>

<img
  className="hidden dark:inline-block"
  src="/docs/odometry-dark.png"
  alt="Odometry Pod Offset Diagram"
/>

Once you have found your offsets, add them to your localizer constants by
using `.leftPodY()`, `.rightPodY()` and `.strafePodX()`.

### Encoder Directions

We will now determine the encoder directions. First, select and run
localization test under the localization folder in the tuning OpMode. Then,
move the robot forward. The x coordinate should increase. Next, move the
robot left. The y coordinate should increase. If either of those does not
happen, you must reverse the respective encoder. To reverse an encoder, add

To reverse an encoder, add one of the following to `ThreeWheelIMUConstants`:

```java title="Constants.java"
.leftEncoderDirection(Encoder.REVERSE)
.rightEncoderDirection(Encoder.FORWARD)

// and/or:

.strafeEncoderDirection(Encoder.REVERSE)
```

> **Important:**
> If when you push the robot forward both x and y change, it is likely that either your offsets have the wrong sign,
> or that the hardwareMap is incorrect (ie. forward encoder is actually your strafe encoder and vise versa)

### Forward Tuner

We will now adjust multipliers that convert encoder ticks into real-world
measurements: inches. This ensures your localizer's readings are accurate.

In the tuning OpMode, under localization, select and start the forward tuner.
Then, push the robot **forward 48 inches** (exactly 2 field tiles). This
distance is configurable if needed. Once you push the robot forward, two
numbers will be displayed on telemetry:

- The distance the robot thinks it has traveled
- The multiplier; this is the number you want.

Add the multiplier to your `ThreeWheelIMUConstants` by adding the following.

```java title="Constants.java"
.forwardTicksToInches(multiplier)
```

> **Tip:**
> It is recommended that you run these tests multiple times and average the results,
> as it can result in more accurate localization.

### Lateral Tuner

The lateral tuner is very similar to the forward tuner, except it is
sideways. In the tuning OpMode, under localization, select and start the
lateral tuner. Push the robot **left 48 inches** (exactly 2 field tiles). As
with the forward tuner, this distance is configurable.

Lastly, add the multiplier to `ThreeWheelIMUConstants` by adding the following line.

```java title="Constants.java"
.strafeTicksToInches(multiplier)
```

### Turn Tuner

The turn tuner is similar to both the forward tuner and lateral tuner, except it is
rotational. Place the robot so it aligns to a fixed reference point (e.g., edge of a field tile).
In the tuning OpMode, under localization, select and start the
turn tuner. Rotate the robot **counterclockwise one full rotation**. As
with the previous tuners, this amount is configurable.

Lastly, add the multiplier to `ThreeWheelIMUConstants` by adding the following line.

```java title="Constants.java"
.turnTicksToInches(multiplier)
```

### Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

> **Note on ESD:**
> If you robot seems to:
>
> 1. Turn or face a different direction when starting a path
> 2. Turn to a incorrect angle or miss with large, unfixable errors
>
> Your robot's IMU might be affected by ESD (electrostatic discharge). Consider grounding
> the robot with a [grounding strap](https://www.revrobotics.com/rev-31-1269/) and/or
> [reading this guide from FIRST to understand ESD](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html)
>
> If after the above you cannot fix the issue, [switch to the non-IMU ThreeWheel Localizer](/docs/pathing/tuning/localization/three-wheel), as
> it will be significantly more accurate than an interfered IMU.

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/pinpoint · Fetched: 2026-07-12

## Pinpoint

> **Prerequisites:**
> Ensure that two odometry pods are connected: one that is parallel to the length
> of your chassis (forward) and another that is perpendicular to your chassis length (lateral).

> **Common Mistakes:**
> * Make sure the pinpoint is plugged into an I2C port **other than port 0**. This is because the Control Hub's built in IMU uses port 0.
> * Make sure the pinpoint has the sticker side (with the ports) facing up.
> * Make sure the forward pod is plugged into the x port on the pinpoint and the strafe pod is plugged into the y port.

### Setup

In `Constants.java`, add an instance of `PinpointConstants`. Make sure to replace the pinpoint hardware map name
with the actual name.

```java title="Constants.java"
public static PinpointConstants localizerConstants = new PinpointConstants()
            .forwardPodY(-5)
            .strafePodX(0.5)
            .distanceUnit(DistanceUnit.INCH)
            .hardwareMapName("pinpoint")
            .encoderResolution(GoBildaPinpointDriver.GoBildaOdometryPods.goBILDA_4_BAR_POD)
            .forwardEncoderDirection(GoBildaPinpointDriver.EncoderDirection.FORWARD)
            .strafeEncoderDirection(GoBildaPinpointDriver.EncoderDirection.FORWARD);
```

Then, add `.pinpointLocalizer` to `createFollower`:

```java title="Constants.java"
return new FollowerBuilder(followerConstants, hardwareMap)
    .pinpointLocalizer(localizerConstants)
    /* other builder steps */
    .build();
```

#### Offsets

Offsets can be found **manually** or **automatically**:

- **Automatic**: Use the [offsets tuner](/docs/pathing/tuning/localization/offsets-tuner)
- **Manual**: Use the diagram below (offsets are in inches)

Set your odometry pod offsets to define where they are relative to your robot's center of rotation.

<img
  className="inline-block dark:hidden"
  src="/docs/odometry-light.png"
  alt="Odometry Pod Offset Diagram"
/>

<img
  className="hidden dark:inline-block"
  src="/docs/odometry-dark.png"
  alt="Odometry Pod Offset Diagram"
/>

Once you have found your offsets, add them to your localizer constants by
using `.forwardPodY()` and `.strafePodX()`.

#### Encoder Resolution

By default, the encoder resolution is set to `GoBildaPinpointDriver.GoBildaOdometryPods.goBILDA_4_BAR_POD`. If you are
using a custom odometry pod, go back to your localizerConstants variable and replace `.encoderResolution()` with
`.customEncoderResolution()` and input your encoder resolution.

#### Encoder Directions

We will now determine the encoder directions. First, select and run
localization test under the localization folder in the tuning OpMode. Then,
move the robot forward. The x coordinate should increase. Next, move the
robot left. The y coordinate should increase. If either of those does not
happen, you must reverse the respective encoder. To reverse an encoder, add

To reverse an encoder, add one of the following to `PinpointConstants`:

```java title="Constants.java"
.forwardEncoderDirection(Encoder.REVERSE)

// and/or:

.strafeEncoderDirection(Encoder.REVERSE)
```

#### Yaw Scalar

If you want to use a yaw scalar, you can set the yaw scalar by doing `yawScalar` in `PinpointConstants` and inputting
your yaw scalar.

NOTE: The yaw scalar overrides calibration done by GoBilda, and it is recommended that you don't edit this unless
there is a reason to change it.

### Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/otos · Fetched: 2026-07-12

## OTOS

> **Prerequisites:**
> Ensure that the OTOS is properly mounted and connected, and the yellow kapton
> tape has been pulled off the sensor. The OTOS
> should be connected to a REV Hub through an I2C cable (not to port 0 because
> the IMU is there).

### Setup

In `Constants.java`, add an instance of `OTOSConstants`. Make sure to
replace the hardware map name with the actual name.

```java title="Constants.java"
public static OTOSConstants localizerConstants = new OTOSConstants()
            .hardwareMapName("otos")
            .linearUnit(DistanceUnit.INCH)
            .angleUnit(AngleUnit.RADIANS);
```

Then, add `.OTOSLocalizer` to `createFollower`:

```java title="Constants.java"
return new FollowerBuilder(followerConstants, hardwareMap)
    .OTOSLocalizer(localizerConstants)
    /* other builder steps */
    .build();
```

### Offsets

You must specify the sensor's position relative to the center of the robot.
Measure the X and Y coordinates, and then change the value of `.offset()`.
If you would like to change the units used, you can change `.linearUnit()`
and/or `.angleUnit()`. The defaults are inches and radians, respectively.

> **Important:**
> The y axis is the left/right axis, and the x axis is the forward/backward
> axis.
>
> Left is positive y and forward is positive x.
>
> Facing forward is `PI/2` radians or `90` degrees, and clockwise rotation
> is negative.

> **Tip:**
> It is recommended that you run the following tests multiple times and
> average the results, as it results in more accurate localization.

### Linear Scalar

We will now adjust multipliers that convert encoder ticks into real-world
measurements: inches. This ensures your localizer's readings are accurate.

Since the OTOS has only one linear scalar, you can run either the forward or
lateral tuner, as they should result in very similar values.

#### Option 1: Forward Tuner

In the tuning OpMode, under localization, select and start the forward tuner.
Then, push the robot **forward 48 inches** (exactly 2 field tiles). This
distance is configurable if needed. Once you push the robot forward, two
numbers will be displayed on telemetry:

- The distance the robot thinks it has traveled
- The linear scalar; this is the number you want.

Add the linear scalar to your `OTOSConstants` by doing the following.

```java title="Constants.java"
.linearScalar(multiplier)
```

#### Option 2: Lateral Tuner

In the tuning OpMode, under localization, select and start the lateral tuner.
Then, push the robot **left 48 inches** (exactly 2 field tiles). This
distance is configurable if needed. Once you push the robot forward, two
numbers will be displayed on telemetry:

- The distance the robot thinks it has traveled
- The linear scalar; this is the number you want.

Add the linear scalar to your `OTOSConstants` (or modify the value in the quickstart)
by doing the following.

```java title="Constants.java"
.linearScalar(multiplier)
```

### Turn Tuner

The turn tuner is similar to both the forward tuner and lateral tuner, except it is
rotational. Place the robot so it aligns to a fixed reference point
(e.g., edge of a field tile).
In the tuning OpMode, under localization, select and start the turn tuner.
Rotate the robot **counterclockwise one full rotation**.

Add the angular scalar to your `OTOSConstants` by doing the following.

```java title="Constants.java"
.angularScalar(multiplier)
```

### Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/drive-encoder · Fetched: 2026-07-12

## Drive Encoder

> **Prerequisites:**
> Ensure that you have all four drive motors encoders connected to their
> respective ports on
> a REV hub.

### Setup

In `Constants.java`, add an instance of `DriveEncoderConstants`. Make sure to
replace the motor names and directions with the correct ones.

```java title="Constants.java"
public static DriveEncoderConstants localizerConstants = new DriveEncoderConstants()
            .rightFrontMotorName("rf")
            .rightRearMotorName("rr")
            .leftRearMotorName("lr")
            .leftFrontMotorName("lf")
            .leftFrontEncoderDirection(Encoder.FORWARD)
            .leftRearEncoderDirection(Encoder.FORWARD)
            .rightFrontEncoderDirection(Encoder.FORWARD)
            .rightRearEncoderDirection(Encoder.FORWARD);
```

Then, add `.driveEncoderLocalizer` to `createFollower`:

```java title="Constants.java"
return new FollowerBuilder(followerConstants, hardwareMap)
    .driveEncoderLocalizer(localizerConstants)
    /* other builder steps */
    .build();
```

### Robot Dimensions

Measure your robot's wheelbase in inches.

- Length: the distance between the front and back wheels
- Width: the distance between the left and right wheels

In your `DriveEncoderConstants`, use `.robotWidth()` and `.robotLength()` to
set the values you just measured.

### Forward Tuner

We will now adjust multipliers that convert encoder ticks into real-world
measurements: inches. This ensures your localizer's readings are accurate.

> **Tip:**
> It is recommended that you run these tests multiple times and average the
> results,
> as it can result in more accurate localization.

In the tuning OpMode, under localization, select and start the forward tuner.
Then, push the robot **forward 48 inches** (exactly 2 field tiles). This
distance is configurable if needed. Once you push the robot forward, two
numbers will be displayed on telemetry:

- The distance the robot thinks it has traveled
- The multiplier; this is the number you want.

Add the multiplier to your `DriveEncoderConstants` by adding the following.

```java title="Constants.java"
.forwardTicksToInches(multiplier)
```

### Lateral Tuner

The lateral tuner is very similar to the forward tuner, except it is
sideways. In the tuning OpMode, under localization, select and start the
lateral tuner. Push the robot **left 48 inches** (exactly 2 field tiles). As
with the forward tuner, this distance is configurable.

Lastly, add the multiplier to `DriveEncoderConstants` by adding the following line.

```java title="Constants.java"
.strafeTicksToInches(multiplier)
```

### Turn Tuner

The turn tuner is again, similar to both the forward tuner and lateral tuner, except it is
rotational. Place the robot so it aligns to a fixed reference point (eg. edge of a field tile).
In the tuning OpMode, under localization, select and start the
turn tuner. Rotate the robot **counterclockwise one full rotation**. As
with the previous tuners, this amount is configurable.

Lastly, add the multiplier to `DriveEncoderConstants` by adding the following line.

```java title="Constants.java"
.turnTicksToInches(multiplier)
```

### Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/localization/offsets-tuner · Fetched: 2026-07-12

## Offsets Tuner

#### Prerequisites
This tuner is made to automatically find odometry offsets for [Two Wheel](https://pedropathing.com/docs/pathing/tuning/localization/two-wheel) and [Pinpoint](https://pedropathing.com/docs/pathing/tuning/localization/pinpoint) localizers.
Currently, it only supports two deadwheels in the calculations.
Before using this tuner, you **must** set both of your odometry offsets to both be 0.
The tuner is a part of the Tuning.java in 2.1.0 or later versions; however, it can be copied over to previous versions [here](https://github.com/Pedro-Pathing/Quickstart/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedroPathing/Tuning.java#L1222).
#### Steps
* Set both localizer offsets (forwardPodY and strafePodX) to be 0.
* Place the robot in the corner of the field or corner of a tile facing a cardinal direction.
* Select and run the tuner (located Tuning -> Localization -> Offsets Tuner).
* Move the robot out of the corner and turn the robot 180 degrees.
* Move the robot back into the corner with the new rotated heading.
* Transfer the offsets provided from telemetry into your code as your forwardPodY and strafePodX offsets.

