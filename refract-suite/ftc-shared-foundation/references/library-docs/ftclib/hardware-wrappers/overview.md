> Source: https://raw.githubusercontent.com/FTCLib/FTCLib-Docs/v2.1.0/features/hardware/README.md · Fetched: 2026-07-12
> Note: docs.ftclib.org (GitBook) returned HTTP 403 to automated fetch tools; content below is pulled from the FTCLib-Docs GitHub source at tag v2.1.0 (the same version live at https://docs.ftclib.org/ftclib/features/hardware), which is the exact markdown GitBook renders for that page.

# Hardware

Each hardware device in FTCLib is based on the `HardwareDevice` interface. This comes with two methods inherited by every device:

* `disable()`: disables the device
* `getDeviceType()`: returns a String characterization of the device

FTCLib offers _a lot_ of hardware devices that can be implemented or customized into your program. The best advice we can give to users is to take a look at the [hardware package](https://github.com/FTCLib/FTCLib/tree/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware) in the FTCLib repository. Here is the list of devices we currently have available (not including motors):

## Gyro Extensions

The `GyroEx` class is an extended gyro that allows users to add more configurable methods and possible control to their gyro. An example would be creating a `ModernRoboticsGyro` class. The abstract class has the following methods:

* `init()`: initializes the gyro and sets the current direction to the 0 heading
* `getHeading()`: returns the heading of the robot compared to the last reset
* `getAbsoluteHeading()`: returns the absolute heading relative to the initial direction
* `getAngles()`: returns the x, y, and z orientation of the gyro. This is functionally the same as yaw, pitch, and roll.
* `getRotation2d()`: transforms the heading into a `Rotation2d` object
* `reset()`: applies an offset so that `getHeading()` returns the 0 position

A useful implementation of this is the [RevIMU](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/RevIMU.java) class for the built-in imu on your REV hub.

## Sensors

There are a few sensors that are offered in FTCLib:

* [SensorColor](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/SensorColor.java)
* [SensorDistance](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/SensorDistance.java) & [SensorDistanceEx](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/SensorDistanceEx.java)
* [SensorRevTOFDistance](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/SensorRevTOFDistance.java)

The `SensorColor` class is just an extension for the `ColorSensor` class that is in the SDK.

`SensorDistance` and `SensorDistanceEx` are interfaces for creating custom distance sensors if desired. An implementation of the `SensorDistanceEx` interface is `SensorRevTOFDistance` which utilizes the time-of-flight mechanic to track distance.

## Servos

The [ServoEx](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/ServoEx.java) interface allows for more methods and actions than the normal servo class in the SDK. You can change the position of the servo relative to the last position or set it to an absolute position. You can either specify a position within the range of the servo's motion or have it rotate a certain number of specified angle units.

An example implementation of this can be found in the [SimpleServo](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/SimpleServo.java) class. You can create a simple servo like this:

```java
ServoEx servo = new SimpleServo(
    hardwareMap, "servo_name", MIN_ANGLE, MAX_ANGLE
);

// the above is functionally equivalent to
servo = new SimpleServo(
    hardwareMap, "servo_name", MIN_ANGLE, MAX_ANGLE,
    AngleUnit.DEGREES
);

// if you want to set the range in radians in the constructor
// you can use the following
servo = new SimpleServo(
    hardwareMap, "servo_name", MIN_ANGLE, MAX_ANGLE,
    AngleUnit.RADIANS
);
```

`MIN_ANGLE` and `MAX_ANGLE` are the minimum and maximum angle positions in degrees you would like to set the servo. This functionally serves as the servo's effective range. If you want to change the effective range at any point, you can do the following:

```java
// change the effective range to a min and max in DEGREES
servo.setRange(MIN_ANGLE, MAX_ANGLE);

// change the range to a min and max in RADIANS
servo.setRange(MIN_ANGLE, MAX_ANGLE, AngleUnit.RADIANS);

// return the effective range
double degreeRange = servo.getAngleRange();

// return the effective range in RADIANS
degreeRange = servo.getAngleRange(AngleUnit.RADIANS);
```

You can invert the servo's direction as well:

```java
// invert the servo
servo.setInverted(true);

// get if the servo is inverted (true if inverted, false if not)
boolean isInverted = servo.getInverted();
```

To turn to positions and angles, utilize the following methods:

* `rotateByAngle`: turns the servo a number of angle units relative to the current angle
* `turnToAngle`: sets the absolute angle of the servo
* `rotateBy`: turns the servo a relative positional distance from the current position
* `setPosition`: set the absolute position of the servo (from 0 to 1)
