> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time.md).

# ElapsedTime - OnBot Java

## Introduction to ElapsedTime <a href="#introduction-to-elapsedtime" id="introduction-to-elapsedtime"></a>

When using our gamepad, we can actively communicate with our robot while our program runs. Our robot waits for our input and acts accordingly until a different command is issued. However, this may not always be the case, such as during the autonomous period of a FTC competition.

Our robot is smart enough to navigate some on its own, however we need to help it along to know what to look for. Eventually, you could work up to your robot being able to navigate using a camera and machine learning or its IMU to sense direction, but for now let's start with one of the built in features of the SDK: **ElapsedTime**

***

What do you think of when you think of a timer? A stopwatch? Your phone? Maybe the timer on a microwave or oven? Timers commonly consist of two main categories: **count up** and **count down**. You can think about the differences of these two by a comparison like keeping track of how fast a runner did a 100m dash vs. needing to know how much longer our food should cook.

**ElapsedTime** is a count up timer. Registering the amount of time elapsed from the start of a set event, like the starting of a stopwatch. In this situation, it is the amount of time passed from when the timer is created or reset within the code.

{% hint style="info" %}
For more information on the ElapsedTime object outside this tutorial check out the [FTC Java Docs](https://ftctechnh.github.io/ftc_app/doc/javadoc/index.html)!
{% endhint %}

### Quick Links

| [ElapsedTime Setup](/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-setup.md) | [ElapsedTime Logic](/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-logic.md) | [ElapsedTime - Multiple Movements](/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-multiple-movements.md) |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |

### Full Code Example

This program uses the same configuration file created at the start of Hello Robot. Some hardware may not be used during this section.

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

        rightmotor.setDirection(DcMotorSimple.Direction.REVERSE);
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        runtime.reset();
        while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
            leftmotor.setPower(1);
            rightmotor.setPower(1);
            telemetry.addData("Number of Seconds in Phase 1", runtime.seconds());
            telemetry.update();
        }

        runtime.reset();
        while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
            leftmotor.setPower(-1);
            rightmotor.setPower(-1);
            telemetry.addData("Number of Seconds in Phase 2", runtime.seconds());
            telemetry.update();
        }
    }
 }
```
