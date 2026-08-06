> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/localization/pinpoint.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Pinpoint
description: A localizer that uses the goBILDA Pinpoint Odometry Computer
---

<Callout title="Prerequisites" type="info">
  Ensure that two odometry pods are connected: one that is parallel to the length
  of your chassis (forward) and another that is perpendicular to your chassis length (lateral). 
</Callout>

<Callout title="Common Mistakes" type="warning">
  * Make sure the pinpoint is plugged into an I2C port **other than port 0**. This is because the Control Hub's built in IMU uses port 0.
  * Make sure the pinpoint has the sticker side (with the ports) facing up.
  * Make sure the forward pod is plugged into the x port on the pinpoint and the strafe pod is plugged into the y port. 
</Callout>

## Setup

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

### Offsets

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

### Encoder Resolution

By default, the encoder resolution is set to `GoBildaPinpointDriver.GoBildaOdometryPods.goBILDA_4_BAR_POD`. If you are
using a custom odometry pod, go back to your localizerConstants variable and replace `.encoderResolution()` with
`.customEncoderResolution()` and input your encoder resolution.

### Encoder Directions

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

### Yaw Scalar

If you want to use a yaw scalar, you can set the yaw scalar by doing `yawScalar` in `PinpointConstants` and inputting
your yaw scalar.

NOTE: The yaw scalar overrides calibration done by GoBilda, and it is recommended that you don't edit this unless
there is a reason to change it.

## Testing the localizer

Once you have completed the tuning steps, you can test your localizer as
described
[on the localization page](/docs/pathing/tuning/localization#localization-test).

Congratulations on successfully tuning your localizer!

## Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).
