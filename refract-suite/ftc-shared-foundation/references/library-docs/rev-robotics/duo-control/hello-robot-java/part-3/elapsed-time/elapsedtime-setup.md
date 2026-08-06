> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-setup.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-setup.md).

# ElapsedTime Setup

## Programming with ElapsedTime

Start by creating a new OpMode called HelloRobot\_ElapsedTime using the BlankLinearOpMode sample similar to what we used in [Part 1. ](/duo-control/hello-robot-java/part-1/test-bed-onbot-java.md)

<figure><img src="/files/eP1IHMrxO6mFHBL16dej" alt="" width="444"><figcaption></figcaption></figure>

Selecting the features discussed above will allow you to start with the following code. Remember that if "Setup Code for Configured Hardware" is selected the OpMode will try to generate a hardwareMap based on the active configuration. This example uses the same Hello Robot config file we originally created!

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.Blinker;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.util.ElapsedTime;

@TeleOp

public class HelloRobot_ElapsedTime extends LinearOpMode {
    private Blinker control_Hub;
    private DcMotor arm;
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    private DcMotor test_motor;
    private Servo test_servo;
    private TouchSensor test_touch;

    @Override
    public void runOpMode() {
        control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        arm = hardwareMap.get(DcMotor.class, "arm");
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
}
```

## Setting up the Basics

To prepare to use ElapsedTime, a variable and an instance of `ElapsedTime` needs to be created. To do this the following line is needed:

```java
private ElapsedTime     runtime = new ElapsedTime();
```

In this case we are named our variable **runtime**.&#x20;

The above line performs two actions:

1. &#x20;A  ElapsedTime variable called runtime is created. Once it is created and defined as an ElapsedTime variable, it can hold the relevant time information and data.&#x20;
2. The other part of the line, `runtime = new ElapsedTime();`, creates an instance of the ElapsedTime timer object and assigns it to our new runtime variable.&#x20;

Add this line to the OpMode with the other private variables:

```java
public class HelloRobot_ElapsedTime extends LinearOpMode {
    private DcMotor leftMotor;
    private DcMotor rightMotor;
    private DcMotor arm;
    private Servo claw;
    private TouchSensor touch;
    private ElapsedTime     runtime = new ElapsedTime();
```

{% hint style="info" %}
In OnBot Java the **private** keyword is an access modifier that, in this situation, means this variable can only be used within the class it was defined. Our class for this project is our "public class HelloRobot\_ElapsedTime".
{% endhint %}

Next we can go ahead and add the basic movement for our motors. For this example, we will set both motors to a power of 1:

```java
@TeleOp

public class HelloRobot_ElapsedTime extends LinearOpMode {
    private Blinker control_Hub;
    private DcMotor arm;
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    private DcMotor test_motor;
    private Servo test_servo;
    private TouchSensor test_touch;
    private ElapsedTime     runtime = new ElapsedTime();

    @Override
    public void runOpMode() {
        control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        arm = hardwareMap.get(DcMotor.class, "arm");
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            leftmotor.setPower(1);
            rightmotor.setPower(1);
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
}
```

Lastly, we need to make sure our right motor's direction is reversed during initialization:&#x20;

```java

    @Override
    public void runOpMode() {
        control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        arm = hardwareMap.get(DcMotor.class, "arm");
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");

        rightmotor.setDirection(DcMotorSimple.Direction.REVERSE);
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
```
