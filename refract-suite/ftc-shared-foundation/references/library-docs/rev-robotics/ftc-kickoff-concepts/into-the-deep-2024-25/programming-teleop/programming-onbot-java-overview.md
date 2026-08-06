> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-onbot-java-overview.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-onbot-java-overview.md).

# Programming - OnBot Java Overview

While most of our example program is the same between Blocks and OnBot Java there are a couple differences and some cool parts to the OnBot Java code we want to point out here!

## Using "enum" for variables

In the OnBot Java version of this code, we use something called "enum". This allows us to declare the variable name and have it treated as a unique value.

```java
    private enum RobotState {
        INIT,
        INTAKE,
        WALL_GRAB,
        WALL_UNHOOK,
        HOVER_HIGH,
        CLIP_HIGH,
        LOW_BASKET,
        MANUAL
    }
```

For example: the robot interprets the variable "MANUAL" as one of the states within our switch case in OnBot Java.&#x20;

With these variables defined we can now have all of our preset positions stored and easily updatable in our state machine:

```java
 // State machine logic
            switch (currentState) {
                case INIT:
                    targetArm = ARM_POSITION_INIT;
                    targetWrist = WRIST_POSITION_INIT;
                    telemetry.addData("State", "INIT");
                    break;
                case INTAKE:
                    targetArm = ARM_POSITION_INTAKE;
                    targetWrist = WRIST_POSITION_SAMPLE;
                    telemetry.addData("State", "INTAKE");
                    break;

                case WALL_GRAB:
                    targetArm = ARM_POSITION_WALL_GRAB;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "WALL_GRAB");
                    break;

                case WALL_UNHOOK:
                    targetArm = ARM_POSITION_WALL_UNHOOK;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "WALL_UNHOOK");
                    break;

                case HOVER_HIGH:
                    targetArm = ARM_POSITION_HOVER_HIGH;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "HOVER_HIGH");
                    break;
                    
                case CLIP_HIGH:
                    targetArm = ARM_POSITION_CLIP_HIGH;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "CLIP_HIGH");
                    break;
                case LOW_BASKET:
                    targetArm = ARM_POSITION_LOW_BASKET;
                    targetWrist = WRIST_POSITION_SAMPLE;
                    telemetry.addData("State", "LOW_BASKET");
                    break;
                case MANUAL:
                    telemetry.addData("State", "MANUAL");
                    break;
            }
```

Our robot will switch states depending on which button on the gamepad is pressed for the arm/wrist!

## Creating a Togglable Button&#x20;

Within our program there are a few buttons set up to work like a toggle. This means the button only needs to be pressed once rather than held for the code to run. In our Starter Bot code, we're taking advantage of this toggle to have one button be able to do multiple things. For example, our claw can switch between open and closed with just the right bumper.&#x20;

```java
            // Toggle claw position when right_bumper is pressed
            if (gamepad1.right_bumper && !lastBump) {
                clawOpen = !clawOpen;
                if (clawOpen) {
                    claw.setPosition(CLAW_OPEN_POSITION);
                } else {
                    claw.setPosition(CLAW_CLOSED_POSITION);
                }
            }
            lastBump = gamepad1.right_bumper;
```

In other programming languages, you might have an option such as "on button pressed", however that's not available to us here so we have to be a little clever to mimic this concept. Our claw is using two simple variables to make this possible.&#x20;

The variable `clawOpen` allows the servo to move between its two set positions. At the start of our program this is set to false, but will switch each time the right bumper is pressed.

Meanwhile the variable `lastBump` checks if the right bumper is currently being held down. If it is set to true, the button is held down so the claw will not move again until it is released, changing the value back to false, then pressed again.&#x20;

```java
            // Toggle claw position when right_bumper is pressed
            if (gamepad1.right_bumper && !lastBump) {
            //checks if right bumper is pressed AND has been released since last pressed
                clawOpen = !clawOpen;
            //switches the state of clawOpen, this is defined originally during initilization
                if (clawOpen) { 
                //if clawOpen = clawOpen  then open claw, else clawOpen = not clawOpen then close claw
                    claw.setPosition(CLAW_OPEN_POSITION);
                } else {
                    claw.setPosition(CLAW_CLOSED_POSITION);
                }
            }
            lastBump = gamepad1.right_bumper;
            //when right bumper is pressed this will set lastBump to true
```

Along with the claw, our robot is using a togglable button for retrieving specimens and hooking them on the high rung!

## Full Code

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.robot.Robot;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.robot.RobotState;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.CRServo;
import com.qualcomm.robotcore.util.Range;

@com.qualcomm.robotcore.eventloop.opmode.TeleOp(name="StarterBot_V1_Java", group="Linear Opmode")
public class StarterBot2025TeleOpJava extends LinearOpMode {

    // Declare OpMode members.
    private DcMotor leftDrive = null;
    private DcMotor rightDrive = null;
    private DcMotor arm = null;
    private DcMotor wrist = null;
    private Servo claw = null;
    private CRServo intake = null;


    // Arm and Wrist target positions for each state
    private static final int ARM_POSITION_INIT = 300;
    private static final int ARM_POSITION_INTAKE = 450;
    private static final int ARM_POSITION_WALL_GRAB = 1100;
    private static final int ARM_POSITION_WALL_UNHOOK = 1700;
    private static final int ARM_POSITION_HOVER_HIGH = 2600;
    private static final int ARM_POSITION_CLIP_HIGH = 2100;
    private static final int ARM_POSITION_LOW_BASKET = 2500;

    
    private static final int WRIST_POSITION_INIT = 0;
    private static final int WRIST_POSITION_SAMPLE = 270;
    private static final int WRIST_POSITION_SPEC = 10;


    
    // Claw positions
    private static final double CLAW_OPEN_POSITION = 0.55;
    private static final double CLAW_CLOSED_POSITION = 0.7;

    // Enum for state machine
    private enum RobotState {
        INIT,
        INTAKE,
        WALL_GRAB,
        WALL_UNHOOK,
        HOVER_HIGH,
        CLIP_HIGH,
        LOW_BASKET,
        MANUAL
    }

    // Initial state
    private RobotState currentState = RobotState.INIT;

    // Claw toggle state
    private boolean clawOpen = true;
    private boolean lastBump = false;
    private boolean lastHook = false;
    private boolean lastGrab = false;
    
    //target position
    private int targetArm = 0;
    private int targetWrist = 0;

    @Override
    public void runOpMode() {
        // Initialize the hardware variables.
        leftDrive  = hardwareMap.get(DcMotor.class, "leftDrive");
        rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");
        arm = hardwareMap.get(DcMotor.class, "arm");
        wrist = hardwareMap.get(DcMotor.class, "wrist");
        claw = hardwareMap.get(Servo.class, "claw");
        intake = hardwareMap.get(CRServo.class, "intake");

        // Stop and reset encoders
        leftDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        arm.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        wrist.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);

        // Set motors to use encoders
        leftDrive.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
        rightDrive.setMode(DcMotor.RunMode.RUN_WITHOUT_ENCODER);
        
        // Set motor direction
        leftDrive.setDirection(DcMotor.Direction.REVERSE);
        rightDrive.setDirection(DcMotor.Direction.FORWARD);
        //Set zero power behavior
        wrist.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        arm.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        leftDrive.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.FLOAT);
        rightDrive.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.FLOAT);

        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // Run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {

            // State machine logic
            switch (currentState) {
                case INIT:
                    targetArm = ARM_POSITION_INIT;
                    targetWrist = WRIST_POSITION_INIT;
                    telemetry.addData("State", "INIT");
                    break;
                case INTAKE:
                    targetArm = ARM_POSITION_INTAKE;
                    targetWrist = WRIST_POSITION_SAMPLE;
                    telemetry.addData("State", "INTAKE");
                    break;

                case WALL_GRAB:
                    targetArm = ARM_POSITION_WALL_GRAB;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "WALL_GRAB");
                    break;

                case WALL_UNHOOK:
                    targetArm = ARM_POSITION_WALL_UNHOOK;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "WALL_UNHOOK");
                    break;

                case HOVER_HIGH:
                    targetArm = ARM_POSITION_HOVER_HIGH;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "HOVER_HIGH");
                    break;
                    
                case CLIP_HIGH:
                    targetArm = ARM_POSITION_CLIP_HIGH;
                    targetWrist = WRIST_POSITION_SPEC;
                    telemetry.addData("State", "CLIP_HIGH");
                    break;
                case LOW_BASKET:
                    targetArm = ARM_POSITION_LOW_BASKET;
                    targetWrist = WRIST_POSITION_SAMPLE;
                    telemetry.addData("State", "LOW_BASKET");
                    break;
                case MANUAL:
                    telemetry.addData("State", "MANUAL");
                    break;
            }
            

            // Handle state transitions based on gamepad input
            if (gamepad1.a) {
                currentState = RobotState.INTAKE;
            } else if (gamepad1.b && !lastGrab) {
                if(currentState == RobotState.WALL_GRAB){
                    currentState = RobotState.WALL_UNHOOK;
                }else{
                    currentState = RobotState.WALL_GRAB;
                }
            } else if (gamepad1.y && !lastHook) {
                if(currentState == RobotState.HOVER_HIGH){
                    currentState = RobotState.CLIP_HIGH;
                }else{
                    currentState = RobotState.HOVER_HIGH;
                }
            } else if (gamepad1.x) { 
                currentState = RobotState.LOW_BASKET;           
            } else if (gamepad1.left_bumper) {
                currentState = RobotState.INIT;
            } else if (gamepad1.dpad_up){ //manual control
                currentState = RobotState.MANUAL;
                targetArm += 10;
            } else if (gamepad1.dpad_down){
                currentState = RobotState.MANUAL;
                targetArm -= 10;
            } else if (gamepad1.dpad_left){
                currentState = RobotState.MANUAL;
                targetWrist += 1;
            } else if (gamepad1.dpad_right){
                currentState = RobotState.MANUAL;
                targetWrist -= 1;
            }
            
            lastGrab = gamepad1.b;
            lastHook = gamepad1.y;

            // Toggle claw position when right_bumper is pressed
            if (gamepad1.right_bumper && !lastBump) {
                clawOpen = !clawOpen;
                if (clawOpen) {
                    claw.setPosition(CLAW_OPEN_POSITION);
                } else {
                    claw.setPosition(CLAW_CLOSED_POSITION);
                }
            }
            lastBump = gamepad1.right_bumper;

            // Control intake servo with triggers
            if (gamepad1.right_trigger>0.1) {
                intake.setPower(1.0);
            } else if (gamepad1.left_trigger>0.1) {
                intake.setPower(-1.0);
            } else {
                intake.setPower(0);
            }
            
            //DRIVE Split Arcade
            double drive = -gamepad1.left_stick_y;
            double turn  =  -gamepad1.right_stick_x;
            double leftPower    = Range.clip(drive + turn, -1.0, 1.0) ;
            double rightPower   = Range.clip(drive - turn, -1.0, 1.0) ;
    
            leftDrive.setPower(leftPower);
            rightDrive.setPower(rightPower);
            
            arm.setTargetPosition(targetArm);
            arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
            wrist.setTargetPosition(targetWrist);
            wrist.setMode(DcMotor.RunMode.RUN_TO_POSITION);
            arm.setPower(1);
            wrist.setPower(1);

            // Send telemetry data to the driver station
            telemetry.addData("Claw Position", clawOpen ? "Open" : "Closed");
            telemetry.addData("Arm Position", arm.getCurrentPosition());
            telemetry.addData("Arm Power", arm.getPower());
            telemetry.addData("Wrist Position", wrist.getCurrentPosition());
            telemetry.addData("Wrist Power", wrist.getPower());
            telemetry.update();
        }
    }
}
```
