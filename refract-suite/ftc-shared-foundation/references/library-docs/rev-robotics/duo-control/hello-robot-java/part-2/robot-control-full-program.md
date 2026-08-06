> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/robot-control-full-program.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/robot-control-full-program.md).

# Robot Control Full Program

It's time to bring everything together so to have a fully mobile robot! Returning to our HelloRobot\_TeleOp program we can add our arm control to our loop below the drivetrain code.

## Full Program

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
        
        //Arm Control with Limit Switch
        if(test_touch.isPressed()){
              if(gamepad1.dpad_up){
                    arm.setPower(0.2);         
                         }
              else{
                    arm.setPower(0);
                         }  
               }
        else {
              if(gamepad1.dpad_up){
                    arm.setPower(0.2);         
                 }
              else if (gamepad1.dpad_down){
                    arm.setPower(-0.2); 
                 }   
              else { 
                    arm.setPower(0); 
                 } 
               } 
        telemetry.addData("Status", "Running");
        telemetry.update();
        }
    }
}
```

{% hint style="info" %}
**Right Stick vs. Left?**

Which joystick is used for driving the robot is largely based on driver preference.

For Hello Robot, we will be referencing using the right stick due to the arm control using the Dpad. This can be changed at any time by changing from right to left in your `x = gamepad1.right_stick_x;` lines.
{% endhint %}

## Downloads

{% hint style="info" %}
These premade programs do not include control of the Class Bot V2's "claw" servo. To learn about programming a servo visit [Programming Servos.](/duo-control/hello-robot-java/part-1/programming-servos.md)
{% endhint %}

**Class Bot V2 / Hello Robot Configuration File:**

{% file src="/files/h3jZwCldfVAdiwdgGG1E" %}

**Class Bot V2 /  Hello Robot Full TeleOp:**

{% file src="/files/Mtbmk3Q1neuV68mVDvGT" %}

**Class Bot V2 / Hello Robot Arm Control no Limit Switch:**

{% file src="/files/l1Q7SQD8XajNW9X9qnuS" %}

**Class Bot V2 / Hello Robot Arm with Limit Switch:**

{% file src="/files/3wDXu8I6CBAZXZ2IAQwc" %}
