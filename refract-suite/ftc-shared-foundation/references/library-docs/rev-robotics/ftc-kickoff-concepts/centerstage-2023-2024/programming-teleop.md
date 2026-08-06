> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/centerstage-2023-2024/programming-teleop.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/centerstage-2023-2024/programming-teleop.md).

# Programming Teleop

## Configuration

Before getting started with programming we needed to create a configuration file. Below is an overview of how the robot is configured for the teleop code to function as expected:

| Port Type | Port Number | Device Type                              | Name       |
| --------- | ----------- | ---------------------------------------- | ---------- |
| Motor     | 0           | REV Robotics Ultraplanetary HD Hex Motor | rightDrive |
| Motor     | 1           | REV Robotics Ultraplanetary HD Hex Motor | leftDrive  |
| Motor     | 2           | REV Robotics Core Hex Motor              | rightarm   |
| Motor     | 3           | REV Robotics Core Hex Motor              | leftarm    |
| Servo     | 0           | Servo                                    | wrist      |
| Servo     | 1           | Servo                                    | gripper    |

### Configuration file download

To put this configuration file on your robot, drag this file into the "FIRST" folder of your Control Hub's file system.

{% file src="/files/C15zneUgz8wpHAg9lzmT" %}

{% hint style="info" %}
For more in-depth information on the configuration process check out [Hello Robot - Configuration](/duo-control/hello-robot-blocks/configuration.md)!
{% endhint %}

## Wiring Diagram

<figure><img src="/files/lRCE4MQALFNdJ0Br5Gpm" alt=""><figcaption></figcaption></figure>

| Device Name | Device Type                                 | Port                 |
| ----------- | ------------------------------------------- | -------------------- |
| rightDrive  | UltraPlanetary Gearbox Kit and HD Hex Motor | Motor/Encoder Port 0 |
| leftDrive   | UltraPlanetary Gearbox Kit and HD Hex Motor | Motor/Encoder Port 1 |
| armright    | Core Hex Motor                              | Motor/Encoder Port 2 |
| armleft     | Core Hex Motor                              | Motor/Encoder Port 3 |
| wrist       | Smart Robot Servo                           | Servo Port 0         |
| gripper     | Smart Robot Servo                           | Servo Port 1         |

## Gamepad Setup

Items to consider when mapping out your gamepad:

* What kind of input does the mechanism need?&#x20;
  * **Joysticks and Triggers** input [floating point data](/duo-control/hello-robot-blocks/using-a-gamepad.md#float) to your code allowing you to adjust the speed of a motor based on the pressure applied to the trigger or position of the joystick.&#x20;
  * **Buttons, Bumpers, and D-Pad** provide [boolean data](/duo-control/hello-robot-blocks/using-a-gamepad.md#boolean) to your code and are ideal for triggering an action such as rotating a motor to a set position.&#x20;
* What drivetrain are you using and what driving style do you want to use?
  * We decided our robot for CENTERSTAGE would be driven with Split Arcade Drive for advantages in precision while driving.
* Which input makes the most sense?&#x20;
  * There are multiple buttons in play for this year's Starter Bot. Both bumpers control the gripper's ability to pick up Pixels. The wrist servo is bound to the "A/Cross" and "B/Circle" buttons for rotating between the intake and home position. Lastly, this year's arm is controlled by the triggers.&#x20;

{% hint style="info" %}
Not all gamepads have buttons labeled the same way. Check the manufacturer's documentation for accurate button mapping.
{% endhint %}

### 2023-24 REV DUO FTC Starter Bot Gamepad Layout:

<figure><img src="/files/koGmHwHKU2yrS8TX6uFF" alt=""><figcaption><p>2023-24 Starter Bot Gamepad Control Bindings</p></figcaption></figure>

| Gamepad Input            | Function                                                                          |
| ------------------------ | --------------------------------------------------------------------------------- |
| Right Joystick           | Turn Left and Right                                                               |
| Left Joystick            | Drive Forward and Reverse                                                         |
| Right and/or Left Bumper | Gripper Close                                                                     |
| A/Cross                  | <p>Arm & Wrist Move to Home Position </p><ul><li>Arm Down, Wrist Up</li></ul>     |
| B/Circle                 | <p>Arm & Wrist Move to Intake Position </p><ul><li>Arm Down, Wrist Down</li></ul> |
| Y/Triangle               | <p>Arm & Wrist Move to Scoring Position </p><ul><li>Arm Back, Wrist Up </li></ul> |
| Option                   | Zero Encoder for Arm                                                              |
| Left Trigger             | Lower Arm                                                                         |
| Right Trigger            | Raise Arm                                                                         |

More information on programming gamepads for use with your robot can be found at[ Hello Robot - Using Gamepads](/duo-control/hello-robot-blocks/using-a-gamepad.md).

## Programming Teleop - Blocks

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-blocks/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

In [Hello Robot- Basics of Programming Drivetrains](/duo-control/hello-robot-blocks/part-2/programming-drivetrain-motors.md) we covered how to program arcade drive with one joystick. For this example, we will be programming arcade drive using two joysticks. This type of drive is called "split arcade". In split arcade drive, the left joystick will control forward and reverse motion of the robot, and the right joystick will control turning. This is similar to how some RC cars are driven and video games are played.&#x20;

{% file src="/files/HJVbnxUvpqBY0jFz5biU" %}
Copy of the full Blocks code!
{% endfile %}

Let's break down the Blocks Code for CENTERSTAGE!

### Establishing Variables:

This year's Starter Bot makes use of a lot of variables.

| Variable              | Purpose                                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| homearmposition       | Tells the arm where it should sit when set to "home position"                                              |
| armIntakePosition     | Tells the arm where it should sit to intake pixels                                                         |
| armScorePosition      | Tells the arm where it should be for scoring                                                               |
| manualMode            | Used for checks of if the arm is being manually controlled with the triggers or using the preset positions |
| armShutdownThreshold  | Used in the watchdog check for if the motors are running and when to shutdown                              |
| wristUpPosition       | Sets the value for when the wrist is in the up position                                                    |
| wristDownPosition     | Sets the value for when the wrist is in the down position                                                  |
| gripperClosedPosition | Sets the default gripper position                                                                          |
| gripperOpenPosition   | Sets the position for where the gripper should move to when the bumpers are pressed                        |
| running               | Used in the watchdog check for if the motors are in "run\_to\_position" mode                               |

<figure><img src="/files/TNjXUZzgcEUz9efWJBac" alt=""><figcaption><p>Variables for the 2023-24 Starter Bot</p></figcaption></figure>

{% hint style="warning" %}
[You will need to program your servos with the SRS Programmer](/rev-crossover-products/servo/srs-programmer.md) in your kit for accurate gripper and wrist movement!
{% endhint %}

### Setting Up Encoders:

{% hint style="info" %}
This code runs AFTER the initialization is activated, but BEFORE the play button is clicked.&#x20;
{% endhint %}

This section allows the encoder on the arm Core Hex Motors to be reset to zero on start up and establishes their default behavior. Additionally, this sets two of the motors to run in reverse, one on the drivetrain and one of the arm motors.&#x20;

<figure><img src="/files/XOVyXTsk687U2mANBCdV" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This code will run ONCE after the play button is activated.&#x20;
{% endhint %}

This section acts as an additional check for resetting the arm's power and position as well as setting the Core Hex Motors to "RUN\_TO\_POSITION" mode as default when the play button is clicked. &#x20;

<figure><img src="/files/d49OKSZ1vWMkaXJq8du9" alt=""><figcaption></figcaption></figure>

### Split Arcade Drive:

{% hint style="info" %}
The following sections all run REPEATEDLY in the "while loop" once the play button is activated.&#x20;
{% endhint %}

Let's begin with programming our Split Arcade Drive. This code will take input from the right and left joysticks to determine the robot's movement. The left joystick controls forward and back, while the right stick controls left and right turning movement.&#x20;

<figure><img src="/files/f6EJ9O7cQ9DF7we2ROs9" alt=""><figcaption><p>Arcade Split Drive Code</p></figcaption></figure>

### Manual Arm Movement:

The triggers on the controller determine the direction of the arm's rotation. The arm's power is determined by how far down both triggers are pressed. Additionally, the if/then statement switches the arm between manual drive and being ready to run the preset positions. &#x20;

<figure><img src="/files/8Zu6eDv5P2QAA4YVYPqx" alt=""><figcaption></figcaption></figure>

### Arm and Wrist Preset Positions:

There are three preset positions for the arm and wrist on the Starter Bot- intake, home, and scoring.&#x20;

| Controller Button | Position                                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| A/Cross           | Arm moves to the down position, Wrist moves up                                                            |
| B/Circle          | Arm moves to the down position, Wrist moves down                                                          |
| Y/Triangle        | Arm moves up to behind the robot, Wrist moves to up - the arm should adjust to its final scoring position |

<figure><img src="/files/WXle0NlZNxwi7bd9PBsj" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/huQonhJIhs9Bnj4P15Ua" alt=""><figcaption></figcaption></figure>

### Re-zero Encoder:

{% hint style="info" %}
When you re-zero the encoder the arm and wrist should be in the HOME position.&#x20;
{% endhint %}

<figure><img src="/files/JG0ULZCKdz7O3WSB3r2D" alt=""><figcaption></figcaption></figure>

### Watchdog to Shutdown Motor in Home Position:

This check prevents the Core Hex Motors from continuing to run while in home position to prevent potential overheating.&#x20;

<figure><img src="/files/I86Bh15nycYZDLrDXQwK" alt=""><figcaption></figcaption></figure>

Let's take a closer look at all the parts of this if/then statement:&#x20;

<figure><img src="/files/RQ0rFgbQ733cKjmT7hBi" alt=""><figcaption></figcaption></figure>

This if/then statement will only run if all the following are met:&#x20;

* The arm is not currently moving in manual mode from the triggers being pressed
* The motors are actively on
* The left Core Hex Motor's current and target position are less than or equal to the threshold (currently set to five)&#x20;
  * Home position's value is set to 0 while Intake is set to 10

### Gripper Controls:

When either or both of the bumpers on the controller are held down the gripper will open fully. When released it will return to the closed position to secure the fingers around the pixel.&#x20;

<figure><img src="/files/YRWczhn3ydT7EJoPXZ0w" alt=""><figcaption></figcaption></figure>

## Programming Teleop - OnBot Java

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-java/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

In [Hello Robot- Basics of Programming Drivetrains](/duo-control/hello-robot-java/part-2/programming-drivetrain-motors.md)[ ](https://docs.revrobotics.com/duo-control/programming/hello-robot-autonomous-robot/robot-nav-onbot-java#basics-of-programming-drivetrains)we covered how to program arcade drive with one joystick. For this example, we will be programming arcade drive using two joysticks. This type of drive is called "split arcade". In split arcade drive, the left joystick will control forward and reverse motion of the robot, and the right joystick will control turning. This is similar to how some RC cars are driven and video games are played.&#x20;

### Full Robot Code

To use this code with your Starter Bot, copy and paste it into a new OnBot Java OP Mode!

```java
/* Copyright (c) 2017 FIRST. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted (subject to the limitations in the disclaimer below) provided that
 * the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this list
 * of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice, this
 * list of conditions and the following disclaimer in the documentation and/or
 * other materials provided with the distribution.
 *
 * Neither the name of FIRST nor the names of its contributors may be used to endorse or
 * promote products derived from this software without specific prior written permission.
 *
 * NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS
 * LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.util.ElapsedTime;
import com.qualcomm.robotcore.util.Range;

@TeleOp(name="Starter Bot 2024", group="Iterative Opmode")

public class StarterBot2024Teleop extends OpMode
{
    // Declare OpMode members.
    private ElapsedTime runtime = new ElapsedTime();
    private DcMotor leftDrive = null;
    private DcMotor rightDrive = null;
    private DcMotor armLeft = null;
    private DcMotor armRight = null;
    private Servo gripper = null;
    private Servo wrist = null;
    
    private boolean manualMode = false;
    private double armSetpoint = 0.0;
    
    private final double armManualDeadband = 0.03;
    
    private final double gripperClosedPosition = 1.0;
    private final double gripperOpenPosition = 0.5;
    private final double wristUpPosition = 1.0;
    private final double wristDownPosition = 0.0;
    
    private final int armHomePosition = 0;
    private final int armIntakePosition = 10;
    private final int armScorePosition = 600;
    private final int armShutdownThreshold = 5;

    /*
     * Code to run ONCE when the driver hits INIT
     */
    @Override
    public void init() {
        telemetry.addData("Status", "Initialized");

        leftDrive  = hardwareMap.get(DcMotor.class, "leftDrive");
        rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");
        armLeft  = hardwareMap.get(DcMotor.class, "armLeft");
        armRight = hardwareMap.get(DcMotor.class, "armRight");
        gripper = hardwareMap.get(Servo.class, "gripper");
        wrist = hardwareMap.get(Servo.class, "wrist");

        leftDrive.setDirection(DcMotor.Direction.FORWARD);
        rightDrive.setDirection(DcMotor.Direction.REVERSE);
        leftDrive.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.FLOAT);
        rightDrive.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.FLOAT);
        
        armLeft.setDirection(DcMotor.Direction.FORWARD);
        armRight.setDirection(DcMotor.Direction.REVERSE);
        armLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        armRight.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        armLeft.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        armRight.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        armLeft.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
        armRight.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
        armLeft.setPower(0.0);
        armRight.setPower(0.0);

        telemetry.addData("Status", "Initialized");
    }

    /*
     * Code to run REPEATEDLY after the driver hits INIT, but before they hit PLAY
     */
    @Override
    public void init_loop() {
    }

    /*
     * Code to run ONCE when the driver hits PLAY
     */
    @Override
    public void start() {
        runtime.reset();
        
        armLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        armRight.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        armLeft.setTargetPosition(armHomePosition);
        armRight.setTargetPosition(armHomePosition);
        armLeft.setPower(1.0);
        armRight.setPower(1.0);
        armLeft.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        armRight.setMode(DcMotor.RunMode.RUN_TO_POSITION);
    }

    /*
     * Code to run REPEATEDLY after the driver hits PLAY but before they hit STOP
     */
    @Override
    public void loop() {
        double leftPower;
        double rightPower;
        double manualArmPower;
        
        //DRIVE
        double drive = -gamepad1.left_stick_y;
        double turn  =  gamepad1.right_stick_x;
        leftPower    = Range.clip(drive + turn, -1.0, 1.0) ;
        rightPower   = Range.clip(drive - turn, -1.0, 1.0) ;

        leftDrive.setPower(leftPower);
        rightDrive.setPower(rightPower);
        
        //ARM & WRIST
        manualArmPower = gamepad1.right_trigger - gamepad1.left_trigger;
        if (Math.abs(manualArmPower) > armManualDeadband) {
            if (!manualMode) {
                armLeft.setPower(0.0);
                armRight.setPower(0.0);
                armLeft.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
                armRight.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
                manualMode = true;
            }
            armLeft.setPower(manualArmPower);
            armRight.setPower(manualArmPower);
        }
        else {
            if (manualMode) {
                armLeft.setTargetPosition(armLeft.getCurrentPosition());
                armRight.setTargetPosition(armRight.getCurrentPosition());
                armLeft.setPower(1.0);
                armRight.setPower(1.0);
                armLeft.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                armRight.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                manualMode = false;
            }
            
            //preset buttons
            if (gamepad1.a) {
                armLeft.setTargetPosition(armHomePosition);
                armRight.setTargetPosition(armHomePosition);
                armLeft.setPower(1.0);
                armRight.setPower(1.0);
                armLeft.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                armRight.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                wrist.setPosition(wristUpPosition);
            }
            else if (gamepad1.b) {
                armLeft.setTargetPosition(armIntakePosition);
                armRight.setTargetPosition(armIntakePosition);
                armLeft.setPower(1.0);
                armRight.setPower(1.0);
                armLeft.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                armRight.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                wrist.setPosition(wristDownPosition);
            }
            else if (gamepad1.y) {
                armLeft.setTargetPosition(armScorePosition);
                armRight.setTargetPosition(armScorePosition);
                armLeft.setPower(1.0);
                armRight.setPower(1.0);
                armLeft.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                armRight.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                wrist.setPosition(wristUpPosition);
            }
        }
        
        //Re-zero encoder button
        if (gamepad1.start) {
            armLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
            armRight.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
            armLeft.setPower(0.0);
            armRight.setPower(0.0);
            manualMode = false;
        }
        
        //Watchdog to shut down motor once the arm reaches the home position
        if (!manualMode &&
        armLeft.getMode() == DcMotor.RunMode.RUN_TO_POSITION &&
        armLeft.getTargetPosition() <= armShutdownThreshold &&
        armLeft.getCurrentPosition() <= armShutdownThreshold
        ) {
            armLeft.setPower(0.0);
            armRight.setPower(0.0);
            armLeft.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
            armRight.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
        }
        
        //GRIPPER
        if (gamepad1.left_bumper || gamepad1.right_bumper) {
            gripper.setPosition(gripperOpenPosition);
        }
        else {
            gripper.setPosition(gripperClosedPosition);
        }

        telemetry.addData("Status", "Run Time: " + runtime.toString());
        telemetry.addData("Gamepad", "drive (%.2f), turn (%.2f)", drive, turn);
        telemetry.addData("Motors", "left (%.2f), right (%.2f)", leftPower, rightPower);
        telemetry.addData("Manual Power", manualArmPower);
        telemetry.addData("Arm Pos:",
            "left = " + 
            ((Integer)armLeft.getCurrentPosition()).toString() + 
            ", right = " +
            ((Integer)armRight.getCurrentPosition()).toString());
        telemetry.addData("Arm Pos:",
            "left = " + 
            ((Integer)armLeft.getTargetPosition()).toString() + 
            ", right = " +
            ((Integer)armRight.getTargetPosition()).toString());
    }

    /*
     * Code to run ONCE after the driver hits STOP
     */
    @Override
    public void stop() {
    }

} 
```
