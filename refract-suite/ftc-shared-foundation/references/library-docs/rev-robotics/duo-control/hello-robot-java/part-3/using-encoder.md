> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/using-encoder.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/using-encoder.md).

# Encoder Basics

## What is an Encoder? <a href="#what-is-an-encoder" id="what-is-an-encoder"></a>

Encoders are a form of sensor built into some motors that help provide feedback to our robot. There are different kinds of encoders, but we're going to be focus on what's called a quadrature encoder for this tutorial. These encoders are able to count the number of revolutions of the motor also sometimes called "ticks".

While quadrature encoders aren't able to tell exact positions, they can still be used to help the motor move to a specified point. We'll go over how to do so later in this tutorial, but this works by specifying first an origin point in our code then a point the motor should move away.

<details>

<summary>Quadrature vs. Absolute Encoders</summary>

You may see the term absolute encoder when referring to something like REV's [Through Bore Encoder](https://www.revrobotics.com/rev-11-1271/). Absolute encoders have a set origin allowing exact movements of the motor in comparison.

Here's a hint for how to remember the difference:

* **Quadrature Encoders** are like a stopwatch continuously adding up time!
* **Absolute Encoders** are more like a clock telling an exact time!

</details>

## Exploring Motor Modes <a href="#exploring-motor-modes" id="exploring-motor-modes"></a>

Let's take a closer look at the different modes we can set our encoder to with our motor. The mode is often established during the initialization process of our code, meaning the motors are ready to go throughout our program, but it is possible to change this for specific use cases as it executes.

Which mode we need to use largely depends on the intended function of the motor and any attached mechanism. For example, we may not need our encoders active on the drivetrain motors when they're being controlled by a joystick's input. On the other hand, we may have a flywheel design that requires a specific speed our encoders can help us achieve.

### Using STOP\_AND\_RESET\_ENCODER <a href="#using-stop_and_reset_encoder" id="using-stop_and_reset_encoder"></a>

When using encoders, it is strongly recommended to first use STOP\_AND\_RESET\_ENCODER during initialization. This will allow you to know what position the motor is starting in, however you will want to plan for a repeatable start up configuration each time!

A motor can be switched to "STOP\_AND\_RESET\_ENCODER" while a code is executing as well. This is often set up using a button on the gamepad to allow the driver to reset the encoder in the event of a motor misbehaving, such as after the robot's been caught on an obstacle.

Below is a snippet of code that demonstrates how to reset the encoder in OnBot Java. You can skip the first line if you already have retrieved the motor object from hardwareMap:

```java
DcMotorEx motor = hardwareMap.get(DcMotorEx.class, "Motor");
motor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
```

### Using RUN\_WITHOUT\_ENCODER <a href="#using-run_without_encoder" id="using-run_without_encoder"></a>

Use this mode when you don’t want the Control Hub to attempt to use the encoders to maintain a constant speed. You can still access the encoder values, but your actual motor speed will vary more based on external factors such as battery life and friction. In this mode, you provide a power level in the -1 to 1 range, where -1 is full speed backwards, 0 is stopped, and 1 is full speed forwards. Reducing the power reduces both torque and speed.

The RUN\_WITHOUT\_ENCODER motor mode is very straightforward, you simply set a power throughout the program using the "Power" block or, such as for a drivetrain, to be set by the joysticks.

The power level is set in Java by calling `setPower()` on a DcMotor or DcMotorEx object, as shown in this snippet. You can skip the first line if you already have retrieved the motor object from hardwareMap.

```java
DcMotorEx motor = hardwareMap.get(DcMotorEx.class, "Motor");
motor.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
// This will run the motor forward at half-power
double motorPower = 0.5;
motor.setPower(motorPower);
```

### Using RUN\_USING\_ENCODER <a href="#using-run_using_encoder" id="using-run_using_encoder"></a>

In this mode, the Control Hub will use the encoder to take an active role in managing the motor’s speed. Rather than directly applying a percentage of the available power, RUN\_USING\_ENCODER mode targets a specific velocity (speed). This allows the motor to account for friction, battery voltage, and other factors. You can still provide a power level in RUN\_USING\_ENCODER mode, but this is not recommended, as it will limit your target speed significantly.

Setting a velocity from RUN\_WITHOUT\_ENCODER mode will automatically switch the motor to RUN\_USING\_ENCODER mode. You should pick a velocity that the motor will be capable of reaching even with a full load and a low battery.

The velocity is set in Java by calling `setVelocity()` on a DcMotorEx object, as is shown in this snippet. You can skip the first line if you have already retrieved the motor object as a DcMotorEx from hardwareMap.

```java
DcMotorEx motor = hardwareMap.get(DcMotorEx.class, "Motor");
motor.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
// This will turn the motor at 200 ticks per second
double motorVelocity = 200;
motor.setVelocity(motorVelocity);
```

### Using RUN\_TO\_POSITION <a href="#using-run_to_position" id="using-run_to_position"></a>

In this mode, the Control Hub will target a specific position, rather than a specific velocity. You can still choose to set a velocity, but it is only used as the maximum velocity. The motor will continue to hold its position even after it has reached its target.

If the motor is unable to reach the determined position the motor will continue to run attempting to reach or maintain that position, which can lead to the motor stalling and overheating.

To use RUN\_TO\_POSITION mode, you need to do the following things in this order:

1. Set a target position (measured in ticks)
2. Switch to RUN\_TO\_POSITION mode
3. Set the maximum velocity (if not determined by a gamepad input)

Remember it is recommended to always reset the encoder during initialization, however you will need to make sure your robot has been reset physically to the initialization position. For example, an arm may need to be brought back to the start up configuration like for the beginning of a FTC match.

The motor will continue to hold its position even after it has reached its target, unless you set the velocity or power to zero, or switch to a different motor mode.

```java
package org.firstinspires.ftc.teamcode;
// import lines were omitted. OnBotJava will add them automatically.

@TeleOp
public class JavaRunToPositionExample extends LinearOpMode {
    DcMotorEx motor;
    
    @Override
    public void runOpMode() {
        motor = hardwareMap.get(DcMotorEx.class, "Motor");
        
        // Reset the encoder during initialization
        motor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
 
        waitForStart();
        
        // Set the motor's target position to 300 ticks
        motor.setTargetPosition(300);
        
        // Switch to RUN_TO_POSITION mode
        motor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        
        // Start the motor moving by setting the max velocity to 200 ticks per second
        motor.setVelocity(200);
 
        // While the Op Mode is running, show the motor's status via telemetry
        while (opModeIsActive()) {
            telemetry.addData("velocity", motor.getVelocity());
            telemetry.addData("position", motor.getCurrentPosition());
            telemetry.addData("is at target", !motor.isBusy());
            telemetry.update();
        }
    }
}
```
