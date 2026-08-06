> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/features/hardware/motors.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.hardware.motors
---

# Motors

FTCLib offers fully-featured motor wrappers for the ease of the user. Behind the scenes, it utilizes the advanced features of FTCLib to produce a more powerful implementation of the DcMotor objects offered in the SDK. Similarly, FTCLib has a `Motor` and `MotorEx` object, each of which allow for the user to directly access the instance object from the hardware map in the case of wanting to work with it directly.

## Creating a Motor Object

Creating a motor is as simple as passing in the hardware map, the name of the device in the robot controller config, and an optional third parameter of a GoBILDA motor type. This is necessary because the goBILDA motors in the configuration don't specify the different max RPM \(rotations per minute\) and CPR \(counts per revolution\).

There is also an option of using a custom CPR and RPM value.

```java
Motor m_motor_1 = new Motor(hardwareMap, "motorOne");
Motor m_motor_2 = new Motor(hardwareMap, "motorTwo", GoBILDA.RPM_312);
Motor m_motor_3 = new Motor(hardwareMap, "motorThree", CPR, RPM);

// grab the internal DcMotor object
DcMotor motorOne = m_motor_1.motor;
```

### Using a RunMode

A RunMode is a method of running the motor when power is supplied. There are three modes: `VelocityControl`, `PositionControl`, and `RawPower`.

```java
// in Motor.java

/**
 * The RunMode of the motor.
 */
public enum RunMode {
    VelocityControl, PositionControl, RawPower
}
```

Raw power sets the motor power directly through a value of $$[-1, 1]$$ where the value represents the percentage of its maximum speed. This is also open loop control, which means there is no feedback control. This is the default mode of the motor.

```java
// set the run mode
m_motor.setRunMode(Motor.RunMode.RawPower);

// set the proportional output power of the motor
m_motor.set(0.37);    // 37% of maximum speed in current direction
```

Position control has the motor run to a desired position based on the input speed and the distance between current motor position and target position \(in counts\). This utilizes a P controller whose coefficient can be changed using `setPositionCoefficient(double)`. This is a tuned value. For tuning, we currently recommend using [FTC Dashboard](https://acmerobotics.github.io/ftc-dashboard/basics).

```java
// set the run mode
m_motor.setRunMode(Motor.RunMode.PositionControl);

// set and get the position coefficient
m_motor.setPositionCoefficient(0.05);
double kP = m_motor.getPositionCoefficient();

// set the target position
m_motor.setTargetPosition(1200);      // an integer representing
                                      // desired tick count

m_motor.set(0);

// set the tolerance
m_motor.setPositionTolerance(13.6);   // allowed maximum error

// perform the control loop
while (!m_motor.atTargetPosition()) {
  m_motor.set(0.75);
}
m_motor.stopMotor(); // stop the motor

/* ALTERNATIVE TARGET DISTANCE */

// configure a distance per pulse,
// which is the distance traveled in a single tick
// dpp = distance traveled in one rotation / CPR
m_motor.setDistancePerPulse(0.015);

// set the target
m_motor.setTargetDistance(18.0);

// this must be called in a control loop
m_motor.set(0.5); // mode must be PositionControl
```

Velocity control has the motor run using velocity in ticks per second with both a feedback and feedforward controller rather than simply setting the speed to a percentage of the maximum output speed. This can lead to smoother control for your motors, and is highly recommended for autonomous programs.

```java
// set the run mode
m_motor.setRunMode(Motor.RunMode.VelocityControl);

// set and get the coefficients
m_motor.setVeloCoefficients(0.05, 0.01, 0.31);
double[] coeffs = m_motor.getVeloCoefficients();
double kP = coeffs[0];
double kI = coeffs[1];
double kD = coeffs[2];

// set and get the feedforward coefficients
m_motor.setFeedforwardCoefficients(0.92, 0.47);
double[] ffCoeffs = m_motor.getFeedforwardCoefficients();
double kS = ffCoeffs[0];
double kV = ffCoeffs[1];

m_motor.setFeedforwardCoefficients(0.92, 0.47, 0.3);
ffCoeffs = m_motor.getFeedforwardCoefficients();
kA = ffCoeffs[2];

// set the output of the motor
// this must be called in a control loop
m_motor.set(-0.54);
```

### Setting Behaviors

FTCLib, like the SDK, has wrapper methods for setting the ZeroPowerBehavior and the direction of the motors. ZeroPowerBehavior is often used for mechanisms other than the drivetrain; for example, like how you would use the BRAKE behavior for a lift.

```java
// set the inversion factor
m_motor.setInverted(true);

// get the inversion factor
boolean isInverted = m_motor.getInverted();

// set the zero power behavior to BRAKE
m_motor.setZeroPowerBehavior(Motor.ZeroPowerBehavior.BRAKE);
```

### The Built-In Encoder

A lot of motors have built-in encoders. FTCLib offers a nested class `Motor.Encoder` that utilizes advanced mechanics and corrects for [velocity overflow](https://github.com/FIRST-Tech-Challenge/SkyStone/issues/241). One of the other great things is that resetting the encoder does not require stopping the motor. It calculates an offset and subtracts that from the current position. This offset is set to the current position of the encoder each time the `reset()` method is called. The Motor object also has methods that manipulate the encoder so that you don't have to grab the internal encoder instance from the object.

You can also use the built-in encoder as an encoder itself when using an external encoder.

```java
// reset the encoder
m_motor.resetEncoder();

// the current position of the motor
int pos = m_motor.getCurrentPosition();

// get the current velocity
double velocity = m_motor.getVelocity(); // only for MotorEx
double corrected = m_motor.getCorrectedVelocity();

// grab the encoder instance
Motor.Encoder encoder = m_motor.encoder;

// get number of revolutions
double revolutions = encoder.getRevolutions();

// set the distance per pulse to 18 mm / tick
encoder.setDistancePerPulse(18.0);
m_motor.setDistancePerPulse(18.0); // also an option

// get the distance traveled
double distance = encoder.getDistance();
distance = m_motor.getDistance(); // also an option

/** USEFUL FEATURES **/

// you can set the encoder of the motor to a different motor's
// encoder
m_motor.encoder = other_motor.encoder;

// sometimes the encoder needs to be reset completely
// through hardware
m_motor.stopAndResetEncoder();
```

## The MotorEx Object

`MotorEx` is an implementation of the Motor class with better integrated velocity control. Unlike the Motor object, it uses the corrected velocity by default instead of the raw velocity returned by the SDK's encoder estimates. It also uses the `DcMotorEx` object instead of the `DcMotor`. Calling `getVelocity()` will return the velocity.

You can also set the velocity directly using `setVelocity()`. You can pass the angular rate and the angle unit \(optional\). Passing just the angular rate will set the velocity in ticks per second. Passing an angle unit will set the velocity to units per second, depending on the unit that is passed into the method.

### Bulk Reading

A bulk read reads all of the sensor data \(except I2C\) on a lynx module to save cycle times. Bulk reads were introduced in SDK version 5.4. Since FTCLib uses wrappers, we can treat them the same way as other sensors.

Here's a sample implementation of auto-caching.

```java
// obtain a list of hubs
List<LynxModule> hubs = hardwareMap.getAll(LynxModule.class);

MotorEx m1 = new MotorEx(hardwareMap, "one");
MotorEx m2 = new MotorEx(hardwareMap, "two");

for (LynxModule hub : hubs) {
     hub.setBulkCachingMode(LynxModule.BulkCachingMode.AUTO);
}

// control loop
int cycles = 0;
while (cycles++ < 500) {
    double v1 = m1.getVelocity();
    double v2 = m2.getVelocity();

    /* implementation */
}
```

You can also take a look at [this sample](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptMotorBulkRead.java) in the SDK.

## CRServo

Th [CRServo](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/hardware/motors/CRServo.java) class is just a motor object intended to be used for a continuous rotation servo. Its general purpose is to be used in FTCLib classes that require a `Motor` input. It works just like a regular motor, without any of the encoder stuff.

## MotorGroup

A motor group object takes several motors and runs them in parallel like a single motor. Motor groups have one leader
and a set of followers. For any group, there _must_ be a leader, but the number of followers can be zero. This makes
creating different drive profiles simpler. The constructor for a `MotorGroup` is as follows:

```java
MotorGroup myMotors = new MotorGroup(leader, follower1, follower2, ...);
```

The number of followers is variable. The other methods of the `MotorGroup` are the same as the ones found in `Motor`. You can very simply treat a `MotorGroup` object
like a single `Motor` object. The [flywheel sample](https://github.com/FTCLib/FTCLib/blob/v2.1.1/examples/src/main/java/com/example/ftclibexamples/FlywheelSample.java)
in the examples folder shows a few other methods you can utilize with the `MotorGroup`.
