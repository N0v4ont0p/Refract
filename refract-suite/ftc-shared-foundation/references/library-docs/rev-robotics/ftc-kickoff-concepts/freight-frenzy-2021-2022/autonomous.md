> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/autonomous.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/autonomous.md).

# Programming Autonomous

## Basic Autonomous Strategy&#x20;

When we were planning for this years kickoff concept one thing we really wanted to address was the accessibility of autonomous scoring achievements. Certain barriers of entry to autonomous programming keep teams from scoring points during the autonomous period. What are these barriers? In our experience as FTC alumni and mentors, time and programming knowledge are the major reasons teams don't create autonomous programs. If a team feels like they don't have the time or skills, programming an autonomous can seem overwhelming. However, many autonomous scoring achievements, like navigation, are easily obtainable objectives that do not require a deep knowledge of programming.

After identifying this as a goal, analyzing the game, and laying out what a starter bot would look like; we decide to explore what a basic autonomous would be for the Freight Frenzy season. There are two major task we feel are achievable.

* Placing the Pre-Load Box on level 1 of the Alliance Shipping Hub
* Navigating to the Warehouse

As you may recall from the Game Breakdown, each robot must start with a pre-loaded box. For this season's randomization element, a robot determines what position the barcode is in and places the pre-loaded box on the corresponding level of the shipping hub. Using a vision component, like a webcam, to determine the position of the barcode is a more advanced programming concept. However, since placing freight on any level of the alliance shipping hub is worth 6 points (regardless of level), we think that placing the block on the 1st level of the shipping hub is an attainable task. This objective also comes with a 33% chance of getting the autonomous bonus.&#x20;

Once we decided on placing the pre-loaded box the next decision to make was where to navigate: the warehouse or the storage unit. We chose the warehouse for a few different reasons. Parking in or completely in the warehouse is worth more points that parking in or completely in the storage unit. The warehouse also has a larger surface area than the storage unit, which means that less tuning is needed to get completely in.&#x20;

We want to start with these two tasks for ease of access reasons. The important thing with programming is to work incrementally. Setting starting tasks allows us to focus on one section of the autonomous at a time, rather than get overwhelmed attempting to solve all the pieces. After tuning and working our autonomous to the point that we want, we can look at other tasks, like adding duck delivery to our lists of tasks.&#x20;

{% embed url="<https://www.youtube.com/watch?v=ktKpwMDMx2E&t=29s>" %}

## Autonomous Path

Once we identified what objectives we wanted to achieve in autonomous we created a a basic path. We decided to have the robot start on the red alliance side of the field near the carousel. From there we identified the following basic elements of the path:

1. Go to shipping hub and drop off the pre-loaded box
2. Head towards Warehouse and straighten out&#x20;
3. Drive into warehouse and park&#x20;

{% hint style="info" %}
This path design is for a red alliance autonomous. Adjustments will need to be made to create blue alliance autonomous.&#x20;
{% endhint %}

![](/files/-Mhti0QkX3gRgYC69QhR)

We know from our mockups for the basic starter kit robot that we want a differential drivetrain, single jointed arm, and roller intake. A differential drivetrain combined with limited the amount of space between the shipping hub and the field wall, makes turning in that space difficult. There is also a risk of the arm knocking into the shipping hub. Taking into consideration what the basic robot design was we knew we needed to make some adjustments to our path.

* Path 1&#x20;
  * Drive towards shipping hub&#x20;
  * Turn slightly&#x20;
* Path 2&#x20;
  * Lift arm to level 1 height
  * Get closer to shipping hub while arm is still lifted
  * Outtake pre-loaded box
* Path 3&#x20;
  * Reverse towards towards storage unit
  * Turn slight to angle towards warehouse&#x20;
* Path 4&#x20;
  * Drive into warehouse&#x20;
  * Park

![](/files/-Mhp2XMnhbt-_VxOgS5l)

## Programming Autonomous - Blocks

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-blocks/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

In the[ Hello Robot - Encoder Navigation](/duo-control/hello-robot-blocks/part-3/using-encoder.md), we covered how to use`RUN_TO_POSITION`  to create paths for the Class bot. We decided to use the same basic concepts to create the path for the Freight Frenzy autonomous. To start we created the code for the first path.&#x20;

![](/files/-MhyvJ6M-f6C9eRIJED1)

{% hint style="success" %}
Like with the Encoder Navigation guide, we created several constant variables to convert from encoder ticks per rotation of the HD Hex Motors (drivetrain motors) to ticks per millimeter traveled. We further converted this value to ticks per inch traveled. The`DRIVE_GEAR_REDUCTION` variable was created by following the same guidelines from the Total Gear Reduction formula; using our planned gear ratios for the motor gearboxes and for transmitting motion to the wheels.&#x20;

Another change we made was to how`rightTarget` and `leftTarget` are calculated. To reduce the need to use`STOP_AND_RESET_ENCODER` mode before each path, we instead take the current position of the motor encoders and add the calculate ticks needed to go to target to the current position.&#x20;
{% endhint %}

Once we had a general idea of the first path down and tested, we knew we were going to have to repeat the following segment of code for each path that requires the robot to drive.&#x20;

![](/files/-MhyyzB0Ii0VPrr5INoD)

This is a rather large segment of code, while duplicating it would allow us to repeat it, we decided instead to move it into a function. Functions in programming, much like mathematical functions, are a set of instructions that are bundled together to reach a particular goal. Since we are using the same (or similar) set of instructions to create each drive path, we can reduce clutter by creating a function that allows us to repeat these actions over and over again.&#x20;

Lets start by creating a function called drive.&#x20;

![](/files/-MhzFuilFaEUcgyr9mwX)

Before creating our function we looked at what information in our instructions needs to be editable. Each path will have a different target distance and we may want to change the speed the robot is running. Knowing this we create three parameters:`power`, `leftInches`, and`rightInches`. By adding parameters we are requiring that each instance of the function must be given a value for power (or speed) and the number of inches we want each motor to move.&#x20;

![](/files/-MhzHSbEl9GkwP_UC3VD)

Now that we have the basics of our function we can add in the motor code.&#x20;

![](/files/-MiN80zWZKp8uYOjWzd2)

The parameter that we pass through the function act similar to variables. We used the `rightInches` and `leftInches` parameters to help us calculate the target position. We also use power to set speed.

With the function created we removed the motor code from our main op mode and reference the function instead. To confirm the function worked as expected we passed the parameter we knew lined up with the first path.

![](/files/-MiNNi-5qkgL8Jb7gjX4)

{% hint style="info" %}
The `leftInches` and `rightInches` parameters are set to different values. We did this so that the robot would move in a relatively straight line and then turn slightly. For more information on the part speed and direction play in how drivetrains move, check out our Robot Navigation guide.&#x20;
{% endhint %}

From here we can work to create our other paths. We know the next action we need to make is to lift the arm and hold that position. We know that `RUN_TO_POSITION` alone will not hold the arm for the amount duration needed to move forward and outtake the pre-loaded box. So we used the elapsed time function to do path 2.&#x20;

![](/files/-MiNaRujHGfKm96T_dfm)

We did some testing with the elapsed time solution. While it was able to score consistently, there are some flaws with this solution. Since path two is included in a loop the reference to our function, repeats itself; meaning that the drivetrain moves forward twice before the condition of the loop is met. In general, a flaw of using elapsed time, is that basing movement on time isn't a guarantee for consistency. That being said, in testing and refining our code to our robot we were able to score the pre-loaded box about 80% of the time. This met our basic standard for our autonomous.&#x20;

Once we had path two figured out, we were able to do some basic testing to create paths 3 and 4 using our function.&#x20;

![](/files/-MiNiKfhEO4tRLZSIOiM)

This basic code allowed us to achieve our basic autonomous strategy. Bare in mind that we generated the power, rightInches, leftInches, and elapsed time numbers doing basic testing with our Class Bot and then made some assumptions from the other mechanisms we made. You will need to make adjustments based on your own mechanisms and hardware components To fine tune this code for your robot, test the code and adjust the number accordingly for the best results. Good luck!

## Programming Autonomous - OnBot Java

{% hint style="info" %}
This section makes the assumption that you have learned some of the FTC programming basics by going through the [Hello Robot](/duo-control/hello-robot-java/welcome.md) guide. If you have not gone through this guide please walk through it before proceeding.&#x20;
{% endhint %}

In the [Hello Robot - Encoder Navigation](/duo-control/hello-robot-java/part-3/using-encoder.md), we covered how to use`RUN_TO_POSITION`  to create paths for the Class bot. We decided to use the same basic concepts to create the path for the Freight Frenzy autonomous. To start we created the code for the first path.&#x20;

```java
@Autonomous
public class FreightFenzy_REDAuton1 extends LinearOpMode {

  private DcMotor RightDrive;
  private DcMotor LeftDrive;
  private DcMotor Arm;
  private DcMotor Intake;
  
  //Convert from the counts per revolution of the encoder to counts per inch
  static final double HD_COUNTS_PER_REV = 28;
  static final double DRIVE_GEAR_REDUCTION = 20.15293;
  static final double WHEEL_CIRCUMFERENCE_MM = 90 * Math.PI;
  static final double DRIVE_COUNTS_PER_MM = (HD_COUNTS_PER_REV * DRIVE_GEAR_REDUCTION) / WHEEL_CIRCUMFERENCE_MM;
  static final double DRIVE_COUNTS_PER_IN = DRIVE_COUNTS_PER_MM * 25.4;
    
  @Override
  public void runOpMode() {

    RightDrive = hardwareMap.get(DcMotor.class, "RightDrive");
    LeftDrive = hardwareMap.get(DcMotor.class, "LeftDrive");
    Arm = hardwareMap.get(DcMotor.class, "Arm");
    Intake = hardwareMap.get(DcMotor.class, "Intake");

   // reverse left drive motor direciton
    LeftDrive.setDirection(DcMotorSimple.Direction.REVERSE);
    
    waitForStart();
    if (opModeIsActive()) {
      // Create target positions
      rightTarget = RightDrive.getCurrentPosition() + (int)(30 * DRIVE_COUNTS_PER_IN);
      leftTarget = LeftDrive.getCurrentPosition() + (int)(15 * DRIVE_COUNTS_PER_IN);
      
      // set target position
      LeftDrive.setTargetPosition(leftTarget);
      RightDrive.setTargetPosition(rightTarget);
      
      //switch to run to position mode
      LeftDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      RightDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      
      //run to position at the desiginated power
      LeftDrive.setPower(0.7);
      RightDrive.setPower(0.7);
      
      // wait until both motors are no longer busy running to position
      while (opModeIsActive() && (LeftDrive.isBusy() || RightDrive.isBusy())) {
      }
      
      // set motor power back to 0 
      LeftDrive.setPower(0);
      RightDrive.setPower(0);
        }
     }
 }
```

{% hint style="success" %}
Like with the Encoder Navigation guide, we created several constant variables to convert from encoder ticks per rotation of the HD Hex Motors (drivetrain motors) to ticks per millimeter traveled. We further converted this value to ticks per inch traveled. The`DRIVE_GEAR_REDUCTION` variable was created by following the same guidelines from the Total Gear Reduction formula; using our planned gear ratios for the motor gearboxes and for transmitting motion to the wheels.&#x20;

Another change we made was to how`rightTarget` and `leftTarget` are calculated. To reduce the need to use`STOP_AND_RESET_ENCODER` mode before each path,; we instead take the current position of the motor encoders and add the calculate ticks needed to go to target to the current position.&#x20;
{% endhint %}

Once we had a general idea of the first path down and tested, we knew we were going to have to repeat the following segment of code for each path that requires the robot to drive.&#x20;

```java
if (opModeIsActive()) {
      // Create target positions
      rightTarget = RightDrive.getCurrentPosition() + (int)(30 * DRIVE_COUNTS_PER_IN);
      leftTarget = LeftDrive.getCurrentPosition() + (int)(15 * DRIVE_COUNTS_PER_IN);
      
      // set target position
      LeftDrive.setTargetPosition(leftTarget);
      RightDrive.setTargetPosition(rightTarget);
      
      //switch to run to position mode
      LeftDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      RightDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      
      //run to position at the desiginated power
      LeftDrive.setPower(0.7);
      RightDrive.setPower(0.7);
      
      // wait until both motors are no longer busy running to position
      while (opModeIsActive() && (LeftDrive.isBusy() || RightDrive.isBusy())) {
      }
      
      // set motor power back to 0 
      LeftDrive.setPower(0);
      RightDrive.setPower(0);
  }
  
```

This is a rather large segment of code, while duplicating it would allow us to repeat it, we decided instead to move it into a function. Functions in programming, much like mathematical functions, are a set of instructions that are bundled together to reach a particular goal. Since we are using the same (or similar) set of instructions to create each drive path, we can reduce clutter by creating a function that allows us to repeat these actions over and over again.&#x20;

Lets start by creating a function called drive.&#x20;

```java
//drive function
private void drive() {

  }
```

Before creating our function we looked at what information in our instructions needs to be editable. Each path will have a different target distance and we may want to change the speed the robot is running. Knowing this we create three parameters:`power`, `leftInches`, and`rightInches`. By adding parameters we are requiring that each instance of the function must be given a value for power (or speed) and the number of inches we want each motor to move.&#x20;

```java
// drive function intakes 3 parameters
private void drive(double power, double leftInches, double rightInches) {

  }
```

Now that we have the basics of our function we can add in the motor code.&#x20;

```java
private void drive(double power, double leftInches, double rightInches) {
    int rightTarget;
    int leftTarget;

    if (opModeIsActive()) {
     // Create target positions
      rightTarget = RightDrive.getCurrentPosition() + (int)(rightInches * DRIVE_COUNTS_PER_IN);
      leftTarget = LeftDrive.getCurrentPosition() + (int)(leftInches * DRIVE_COUNTS_PER_IN);
      
      // set target position
      LeftDrive.setTargetPosition(leftTarget);
      RightDrive.setTargetPosition(rightTarget);
      
      //switch to run to position mode
      LeftDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      RightDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      
      //run to position at the desiginated power
      LeftDrive.setPower(power);
      RightDrive.setPower(power);
      
      // wait until both motors are no longer busy running to position
      while (opModeIsActive() && (LeftDrive.isBusy() || RightDrive.isBusy())) {
      }
      
      // set motor power back to 0
      LeftDrive.setPower(0);
      RightDrive.setPower(0);
    }
  }
```

The parameter that we pass through the function act similar to variables. We used the `rightInches` and `leftInches`parameters to help us calculate the target position. We also use `power` to set speed.

With the function created we can remove the motor code from our main op mode and reference the function instead. To confirm the function worked as expected we passed the parameter we knew lined up with the first segment.

```java
  @Override
  public void runOpMode() {

    RightDrive = hardwareMap.get(DcMotor.class, "RightDrive");
    LeftDrive = hardwareMap.get(DcMotor.class, "LeftDrive");
    Arm = hardwareMap.get(DcMotor.class, "Arm");
    Intake = hardwareMap.get(DcMotor.class, "Intake");
   
   // reverse left drive motor direciton
    LeftDrive.setDirection(DcMotorSimple.Direction.REVERSE);
    
    waitForStart();
    if (opModeIsActive()) {
    
      // segment 1 
      drive(0.7, 30, 15);
    }
}
```

{% hint style="info" %}
The `leftInches` and `rightInches` parameters are set to different values. We did this so that the robot would move in a relatively straight line and then turn slightly. For more information on the part speed and direction play in how drivetrains move, check out our Robot Navigation guide.&#x20;
{% endhint %}

From here we can work to create our other paths. We know the next action we need to make is to lift the arm and hold that position. We know that `RUN_TO_POSITION` alone will not hold the arm for the amount duration needed to move forward and outtake the pre-loaded box. So we used the elapsed time function to do segment 2.&#x20;

```java
 static final double HD_COUNTS_PER_REV = 28;
 static final double DRIVE_GEAR_REDUCTION = 20.15293;
 static final double WHEEL_CIRCUMFERENCE_MM = 90 * Math.PI;
 static final double DRIVE_COUNTS_PER_MM = (HD_COUNTS_PER_REV * DRIVE_GEAR_REDUCTION) / WHEEL_CIRCUMFERENCE_MM;
 static final double DRIVE_COUNTS_PER_IN = DRIVE_COUNTS_PER_MM * 25.4;
 
 //Create elapsed time variable and an instance of elapsed time
 private ElapsedTime     runtime = new ElapsedTime();
```

```java
waitForStart();
    if (opModeIsActive()) {
      
      //segment 1
      drive(0.7, 30, 15);
      
      runtime.reset(); // reset elapsed time timer
      
      //segment 2 - lift arm, drive to shipping hub, outtake freight
      while (opModeIsActive() && runtime.seconds() <= 7) {
        
        //lift arm and hold
        Arm.setTargetPosition(120);
        Arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        Arm.setPower(0.3);
        
        //drive forward for 1 second
        while (runtime.seconds() > 2 && runtime.seconds() <= 3) {
          drive(0.4, 4, 4);
        }
        
        //run intake
        while (runtime.seconds() > 4 && runtime.seconds() <= 7) {
          Intake.setPower(-0.6);
        }
      
      // turn off arm and intake
      Arm.setPower(0);
      Intake.setPower(0);
    
      }
```

We did some testing with the elapsed time solution. While it was able to score consistently, there are some flaws with this solution. Since path two is included in a loop the reference to our function, repeats itself; meaning that the drivetrain moves forward twice before the condition of the loop is met. In general, a flaw of using elapsed time, is that basing movement on time isn't a guarantee for consistency. That being said, in testing and refining our code to our robot we were able to score the pre-loaded box about 80% of the time. This met our basic standard for our autonomous.&#x20;

Once we had path two figured out, we were able to do some basic testing to create segments 3 and 4 using our function.&#x20;

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.util.ElapsedTime;

@Autonomous(name = "FreightFenzy_REDAuton1 (Java)")
public class FreightFenzy_REDAuton1 extends LinearOpMode {

  private DcMotor RightDrive;
  private DcMotor LeftDrive;
  private DcMotor Arm;
  private DcMotor Intake;
  
  //Convert from the counts per revolution of the encoder to counts per inch
  static final double HD_COUNTS_PER_REV = 28;
  static final double DRIVE_GEAR_REDUCTION = 20.15293;
  static final double WHEEL_CIRCUMFERENCE_MM = 90 * Math.PI;
  static final double DRIVE_COUNTS_PER_MM = (HD_COUNTS_PER_REV * DRIVE_GEAR_REDUCTION) / WHEEL_CIRCUMFERENCE_MM;
  static final double DRIVE_COUNTS_PER_IN = DRIVE_COUNTS_PER_MM * 25.4;
  
  //Create elapsed time variable and an instance of elapsed time
  private ElapsedTime     runtime = new ElapsedTime();
  
  // Drive function with 3 parameters
  private void drive(double power, double leftInches, double rightInches) {
    int rightTarget;
    int leftTarget;

    if (opModeIsActive()) {
     // Create target positions
      rightTarget = RightDrive.getCurrentPosition() + (int)(rightInches * DRIVE_COUNTS_PER_IN);
      leftTarget = LeftDrive.getCurrentPosition() + (int)(leftInches * DRIVE_COUNTS_PER_IN);
      
      // set target position
      LeftDrive.setTargetPosition(leftTarget);
      RightDrive.setTargetPosition(rightTarget);
      
      //switch to run to position mode
      LeftDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      RightDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      
      //run to position at the desiginated power
      LeftDrive.setPower(power);
      RightDrive.setPower(power);
      
      // wait until both motors are no longer busy running to position
      while (opModeIsActive() && (LeftDrive.isBusy() || RightDrive.isBusy())) {
      }
      
      // set motor power back to 0
      LeftDrive.setPower(0);
      RightDrive.setPower(0);
    }
  }


  @Override
  public void runOpMode() {

    RightDrive = hardwareMap.get(DcMotor.class, "RightDrive");
    LeftDrive = hardwareMap.get(DcMotor.class, "LeftDrive");
    Arm = hardwareMap.get(DcMotor.class, "Arm");
    Intake = hardwareMap.get(DcMotor.class, "Intake");

 
    LeftDrive.setDirection(DcMotorSimple.Direction.REVERSE);
    
    waitForStart();
    if (opModeIsActive()) {
      
       //segment 1
      drive(0.7, 30, 15);
      
      runtime.reset(); // reset elapsed time timer
      
      //segment 2 - lift arm, drive to shipping hub, outtake freight
      while (opModeIsActive() && runtime.seconds() <= 7) {
        
        //lift arm and hold
        Arm.setTargetPosition(120);
        Arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        Arm.setPower(0.3);
        
        //drive forward for 1 second
        while (runtime.seconds() > 2 && runtime.seconds() <= 3) {
          drive(0.4, 4, 4);
        }
        
        //run intake
        while (runtime.seconds() > 4 && runtime.seconds() <= 7) {
          Intake.setPower(-0.6);
        }
      
      // turn off arm and intake
      Arm.setPower(0);
      Intake.setPower(0);
      
      //segment 3 - reverse to get better angle 
      drive(0.7, -15, -30);
      
      //segment 4 - drive into warehouse
      drive(1, 90, 90);
    }
  }
}
```

This basic code allowed us to achieve our basic autonomous strategy. Bare in mind that we generated the power, rightInches, leftInches, and elapsed time numbers doing basic testing with our Class Bot and then made some assumptions from the other mechanisms we made. You will need to make adjustments based on your own mechanisms and hardware components. To fine tune this code for your robot, test the code and adjust the number accordingly for the best results.&#x20;

## Autonomous Wrap Up

The above walkthrough should give you the basic information to get started with programming your own autonomous. We recommend testing and tuning your code to make sure everything works consistently. Once you have a functioning code, explore different ways you can add on this code to elevate it. The starting position for the path puts you in a great place to deliver the duck, which can easily be reworked into your path. Also it is worth considering what your alliance partner may do in a match to better optimize the code.

{% hint style="info" %}
If you are new to FTC programming check out our [Hello Robot programming guide](/duo-control/hello-robot-blocks/welcome.md) to learn the basics of programming within the FTC SDK.&#x20;
{% endhint %}
