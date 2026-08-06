> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java.md).

# Arcade Style TeleOp - OnBot Java

The time has come to program our robot to respond to our gamepad inputs so we can drive it around! To start we will be focusing on controlling our drivetrain.

Think back to the very start of [Part 2](/duo-control/hello-robot-java/part-2.md) for a moment. We will be programming our robot using the Arcade Style of TeleOp. This means our forward and back movements will be controlled using the y-axis of the joystick while turning will be controlled by the x-axis.

This section will introduce the use of **variables** as we create our program. This will allow us to set up calculations in our program that will determine what power the motors should receive based on our gamepad's input. How much **power** each motor receives changes how the robot will **move,** so it is important to also review this relationship will establishing our code!

Below is a sneak peek at our final program:

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

public class HelloRobot_TeleOp extends LinearOpMode {
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
        
        rightmotor.setDirection(DcMotorSimple.Direction.REVERSE);
        double x;
        double y;
        
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
        
        //Drivetrain Control
        x = gamepad1.right_stick_x;
        y = -gamepad1.right_stick_y;
        
        rightmotor.setPower(y-x);
        leftmotor.setPower(y+x);
 
        telemetry.addData("Status", "Running");
        telemetry.update();
        }
    }
}
```
