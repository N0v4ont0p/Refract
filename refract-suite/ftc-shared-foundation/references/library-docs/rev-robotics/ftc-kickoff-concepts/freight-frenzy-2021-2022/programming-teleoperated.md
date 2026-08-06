> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/programming-teleoperated.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/programming-teleoperated.md).

# Starter Bot - Programming TeleOp

## Basic TeleOp Strategy

Our strategy for teleoperated mode was to make driving the robot as intuitive as possible. Having certain actions pre-programmed and assigned to buttons, like moving the arm into position to score on level 2 of the Shipping Hubs, will make the robot easier to control.&#x20;

We decided to have buttons assigned to all 3 levels of the Shipping Hubs while scoring from the front and levels 2 and 3 from the back of the robot. Another decision we made was to have the intake motor controlled by the triggers. We chose to control the intake this way so that we could drive and pick up Freight at the same time.&#x20;

## Configuration and Wiring

Before getting started with programming we needed to create a configuration file. Below is an overview of how the robot is configured for the teleop code to function as expected:

| Port Type | Port Number | Device Type              | Name        |
| --------- | ----------- | ------------------------ | ----------- |
| Motor     | 0           | REVRoboticsUltraplantary | LeftDrive   |
| Motor     | 1           | REVRoboticsUltraplantary | RightDrive  |
| Motor     | 2           | REVRoboticsCoreHexMotor  | Arm         |
| Motor     | 3           | REVRoboticsCoreHexMotor  | Intake      |
| Servo     | 0           | Servo                    | DuckSpinner |
| I2C       | 0           | IMU                      | imu         |

{% hint style="info" %}
For more in depth information on the configuration process check out [Hello Robot - Configuration](/duo-control/hello-robot-blocks/configuration.md)!
{% endhint %}

### Wiring Diagram

![](/files/jPBDKZ1FWmmBclYAMtq0)

| Device Name/Function | Device Type       | Port                 |
| -------------------- | ----------------- | -------------------- |
| LeftDrive            | HD Hex Motor      | Motor/Encoder Port 0 |
| RightDrive           | HD Hex Motor      | Motor/Encoder Port 1 |
| Arm                  | Core Hex Motor    | Motor/Encoder Port 2 |
| Intake               | Core Hex Motor    | Motor/Encoder Port 3 |
| DuckSpinner          | Smart Robot Servo | Servo Port 0         |

## Assigning Controls to a Gamepad/Controller

Items to consider when mapping out your gamepad:

* What kind of input does the mechanism need?&#x20;
  * **Joysticks and Triggers** input [floating point data](/duo-control/hello-robot-blocks/using-a-gamepad.md#float) to your code allowing you to adjust the speed of a motor based on the pressure applied to the trigger or position of the joystick.&#x20;
  * **Buttons, Bumpers, and D-Pad** provide [boolean data ](/duo-control/hello-robot-blocks/using-a-gamepad.md#boolean)to your code and are ideal for triggering a action such as rotating a motor to a set position.&#x20;
* What drivetrain are you using and what driving style do you want to use?
  * We decided the Freight Frenzy Starter Bot would be driven tank style.
* Which input makes the most sense? Would pressing up on the d-pad be more intuitive for moving your arm up or down?
  * We chose to assign our backwards scoring presets to the bumpers because we liked the idea of backwards controls being on the back of the controller.&#x20;

{% hint style="info" %}
Not all controllers have buttons labeled the same way. Check the manufacturer's documentation for accurate button mapping.
{% endhint %}

Freight Frenzy Starter Bot controller layout:

![Gamepad layout](/files/-MlBgefoXNPrzj4_KxKk)

| Input          | Function                       |
| -------------- | ------------------------------ |
| Right Joystick | Right Side Drive Motor         |
| Left Joystick  | Left Side Drive Motor          |
| Right Trigger  | Intake In                      |
| Left Trigger   | Intake Out                     |
| Right Bumper   | High Level (Back Scoring)      |
| Left Bumper    | Mid Level (Back Scoring)       |
| A / **✕**      | Intake Ground Position         |
| B / ◯          | High Level (Front Scoring)     |
| Y / △          | Mid Level (Front Scoring)      |
| X / ☐          | Low Level (Front Scoring)      |
| D-Pad Right    | Duck Spinner Counter Clockwise |
| D-Pad Left     | Duck Spinner Clockwise         |

More information on programming gamepads for use with your robot can be found at[ Hello Robot - Using Gamepads](/duo-control/hello-robot-blocks/using-a-gamepad.md).

## Programming Teleop - Blocks

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-blocks/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

### Drive Code&#x20;

In [Hello Robot- Basics of Programming Drivetrains](/duo-control/hello-robot-blocks/part-2/programming-drivetrain-motors.md) we covered how to program arcade drive with one joystick, for this example we will be programming tank drive using two joysticks. The right joystick input will control forward and reverse motion of the right side motor and the left joystick will control the left motor in the same way. Similar to the arcade style driving tutorial, we will use the Dual Motor block to assign power values to our motors. This time, the motor's power value will be based on the Y-axis input from each joystick, as shown below.

![Blocks tank drive code](/files/-MlBIoe6wsae5XIrIwPE)

{% hint style="info" %}
Remember to reverse one of the motors and set the correct direction for forward movement of your robot. In our code we needed to reverse both motors with the dual drive block.
{% endhint %}

### Freight Delivery Mechanism Control Code&#x20;

The control of our freight delivery arm is done by running the Core Hex Motor ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) to a specific position. We measured the number of encoder ticks needed to reach each of the five positions we had planned for our arm: low level, mid level, high level, high level from the back of the robot, and mid level from the back of the robot. For detailed instructions on how to measure encoder ticks on your robot and use the `RUN_TO_POSITION` block see [Hello Robot - Arm Control](/duo-control/hello-robot-blocks/part-2/arm-control-blocks.md).

For all of our button inputs we used an `if/else` statement. In the image below you can see the first two sections, one for setting the position of the arm to the ground and one for setting it to the height of level 1 on the Shipping Hub.&#x20;

![Blocks freight delivery arm code](/files/-MlBMQavLjNabhVd8bKb)

### Carousel and Intake Mechanisms Control Code

For the intake, we chose to use the triggers to control the speed of the motor spinning the mechanism. Since the triggers are easy to accidentally bump when holding the controller we decided we would only count the action as active if it was more than half way pressed. You can see this in the blocks intake mechanism code where the value of the right/left trigger is compared to 0.5.

![Blocks intake mechanism code](/files/-MlBflADVjXf1qAFWbeu)

The carousel mechanism is driven by a Smart Robot Servo ([REV-41-1079](https://www.revrobotics.com/rev-41-1097/)), therefore the programming is slightly different for continuous motion. First, we programmed the Smart Robot Servo with the SRS Programmer ([REV-31-1108](https://www.revrobotics.com/rev-31-1108/)) to be in continuous mode. You can reference the [SRS Programmer Basics](/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md) for a tutorial on how to switch modes on your Smart Robot Servo. Make sure you are using a `set position` servo motor control block. Use[ Hello Robot - Servo Basics](/duo-control/hello-robot-blocks/part-1/programming-servos.md) as an in-depth guide. We added this into the end of our long `if/else` statement as seen below.

![Blocks carousel mechanism code ](/files/-MlBTUygcHuBLjdK_V-H)

### Complete Blocks Program

Below is the complete Blocks Program for the Freight Frenzy Starter Bot.&#x20;

![Full blocks code for the Freight Frenzy Starter Bot](/files/-MlBg4aJLWV3SQP__uN0)

[Click here to download the Freight Frenzy Starter Bot Blocks code.](<https://www.revrobotics.com/content/sw/StarterBot/StarterKitRobotTank.blk&#xA;&#xA;>)

## Programming Teleoperated - OnBot Java

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-java/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

### Drive Code

In [Hello Robot- Basics of Programming Drivetrains](/duo-control/hello-robot-java/part-2/programming-drivetrain-motors.md) we covered how to program arcade drive with one joystick, for this example we will be programming tank drive using two joysticks. The right joystick input will control forward and reverse motion of the right side motor and the left joystick will control the left motor in the same way. The main difference this time is the motor's power value will be based on the Y-axis input from each joystick, as shown below.

```
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;


@TeleOp

public class StarterKitRobotTank extends LinearOpMode {
    private DcMotor LeftDrive;
    private DcMotor RightDrive;


    @Override
    public void runOpMode() {
        LeftDrive = hardwareMap.get(DcMotor.class, "LeftDrive");
        RightDrive = hardwareMap.get(DcMotor.class, "RightDrive");
 
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            //DRIVETRAIN CODE
            double leftAxis = -gamepad1.left_stick_y;
            double rightAxis = -gamepad1.right_stick_y;
            
            double leftPower = -leftAxis;
            double rightPower = rightAxis;
            
            LeftDrive.setPower(leftPower);
            RightDrive.setPower(rightPower);
            
            telemetry.update();
            }
        }
    }


```

{% hint style="info" %}
Be sure to reverse one of the motors and set the correct direction for forward movement of your robot. In our code we needed to reverse both motors with the dual drive block.
{% endhint %}

### Freight Delivery Mechanism Control Code

The control of our freight delivery arm is done by running the Core Hex Motor ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) to a specific position. We measured the number of encoder ticks needed to reach each of the five positions we had planned for our arm: low level, mid level, high level, high level from the back of the robot, and mid level from the back of the robot. For detailed instructions on how to measure encoder ticks on your robot and use the `ArmTarget =` statement see [Hello Robot - Arm Control](/duo-control/hello-robot-java/part-2/arm-control-onbot-java.md).

For all of our button inputs we used the `if/else` statement shown below:

```
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;


@TeleOp

public class StarterKitRobotTank extends LinearOpMode {
    private DcMotor ArmMotor;
    private DcMotor IntakeMotor;


    @Override
    public void runOpMode() {
        ArmMotor = hardwareMap.get(DcMotor.class, "Arm");
        ArmMotor.setTargetPosition(0);
        ArmMotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        ArmMotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        
        int ArmTarget = 0;

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            //MECHANISM CODE
            
            if (gamepad1.a) {
                ArmTarget = 0; //On the ground for starting and intaking
            }
            else if (gamepad1.x) {
                ArmTarget = 120; //Low level on the goal
            }
            else if (gamepad1.y) {
                ArmTarget = 260; //Mid level on the goal
            }
            else if (gamepad1.b) {
                ArmTarget = 410; //High level on the goal
            }
            else if (gamepad1.right_bumper) {
                ArmTarget = 1420; //High level on the goal scoring backwards
            }
            else if (gamepad1.left_bumper) {
                ArmTarget = 1570; //Mid level on the goal scoring backwards
            }
            
            //stuff for arm position control
            ArmMotor.setTargetPosition(ArmTarget);
            ArmMotor.setPower(1);
             
            telemetry.addData("Arm Position", ArmMotor.getCurrentPosition());
            telemetry.update();
            }
        }
    }


```

### Carousel and Intake Mechanisms Control Code

For the intake, we chose to use the triggers to control the speed of the motor spinning the mechanism. Since the triggers are easy to accidentally bump when holding the controller we decided we would only count the action as active if it was more than half way pressed. This is what the statement`gamepad1.right_trigger>0.5)?1:((gamepad1.left_trigger>0.5)?-1:0);` is used to achieve.&#x20;

```
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;


@TeleOp

public class StarterKitRobotTank extends LinearOpMode {
    private DcMotor IntakeMotor;


    @Override
    public void runOpMode() {
       IntakeMotor = hardwareMap.get(DcMotor.class, "Intake");
        
   
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            //MECHANISM CODE
            
            double IntakePower = (gamepad1.right_trigger>0.5)?1:((gamepad1.left_trigger>0.5)?-1:0);
            
            IntakeMotor.setPower(IntakePower);
                         
            telemetry.update();
            }
        }
    }


```

The carousel mechanism is driven by a Smart Robot Servo ([REV-41-1079](https://www.revrobotics.com/rev-41-1097/)), therefore the programming is slightly different for continuous motion.  First, we programmed the Smart Robot Servo with the SRS Programmer ([REV-31-1108](https://www.revrobotics.com/rev-31-1108/)) to be in continuous mode. You can reference the [SRS Programmer Basics](/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md) for a tutorial on how to switch modes on your Smart Robot Servo. Instead of using a `motor.setPower` statement we will be using  `motor.setPosition` to make the servo rotate. You can find more information on how to program servos on the [Hello Robot - Servo Basics](/duo-control/hello-robot-java/part-1/programming-servos.md) page.

```
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;


@TeleOp

public class StarterKitRobotTank extends LinearOpMode {
    private Servo DuckSpinner;


    @Override
    public void runOpMode() {
         DuckSpinner = hardwareMap.get(Servo.class, "DuckSpinner");


        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            //MECHANISM CODE
            
            double SpinnerPower = gamepad1.dpad_left?1:(gamepad1.dpad_right?0:0.5);
           
            DuckSpinner.setPosition(SpinnerPower);
             
       
            telemetry.update();
            }
        }
    }


```

### Complete OnBot Java Program

Below is the complete OnBot Java Program for the Freight Frenzy Starter Bot.&#x20;

```
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.hardware.Blinker;
import com.qualcomm.robotcore.hardware.Gyroscope;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.util.ElapsedTime;


@TeleOp

public class StarterKitRobotTank extends LinearOpMode {
    private Blinker Control_Hub;
    private Gyroscope imu;
    private DcMotor LeftDrive;
    private DcMotor RightDrive;
    private DcMotor ArmMotor;
    private DcMotor IntakeMotor;
    private Servo DuckSpinner;


    @Override
    public void runOpMode() {
        Control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        imu = hardwareMap.get(Gyroscope.class, "imu");
        LeftDrive = hardwareMap.get(DcMotor.class, "LeftDrive");
        RightDrive = hardwareMap.get(DcMotor.class, "RightDrive");
        ArmMotor = hardwareMap.get(DcMotor.class, "Arm");
        ArmMotor.setTargetPosition(0);
        ArmMotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        ArmMotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        
        IntakeMotor = hardwareMap.get(DcMotor.class, "Intake");
        
        DuckSpinner = hardwareMap.get(Servo.class, "DuckSpinner");
        
        int ArmTarget = 0;

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            //DRIVETRAIN CODE
            double leftAxis = -gamepad1.left_stick_y;
            double rightAxis = -gamepad1.right_stick_y;
            
            double leftPower = -leftAxis;
            double rightPower = rightAxis;
            
            LeftDrive.setPower(leftPower);
            RightDrive.setPower(rightPower);
            
            //MECHANISM CODE
            
            double IntakePower = (gamepad1.right_trigger>0.5)?1:((gamepad1.left_trigger>0.5)?-1:0);
            
            double SpinnerPower = gamepad1.dpad_left?1:(gamepad1.dpad_right?0:0.5);
            
            if (gamepad1.a) {
                ArmTarget = 0; //On the ground for starting and intaking
            }
            else if (gamepad1.x) {
                ArmTarget = 120; //Low level on the goal
            }
            else if (gamepad1.y) {
                ArmTarget = 260; //Mid level on the goal
            }
            else if (gamepad1.b) {
                ArmTarget = 410; //High level on the goal
            }
            else if (gamepad1.right_bumper) {
                ArmTarget = 1420; //High level on the goal scoring backwards
            }
            else if (gamepad1.left_bumper) {
                ArmTarget = 1570; //Mid level on the goal scoring backwards
            }
            
            //stuff for arm position control
            ArmMotor.setTargetPosition(ArmTarget);
            ArmMotor.setPower(1);
            
            IntakeMotor.setPower(IntakePower);
            
            DuckSpinner.setPosition(SpinnerPower);
             
            telemetry.addData("Arm Position", ArmMotor.getCurrentPosition());
            telemetry.update();
            }
        }
    }


```
