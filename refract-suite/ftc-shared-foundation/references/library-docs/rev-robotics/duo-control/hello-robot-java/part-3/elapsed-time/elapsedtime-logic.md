> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-logic.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-logic.md).

# ElapsedTime Logic

## Setting a Time Limit

For now our goal will be to have the motors move forward for 3 seconds. To accomplish this we need to edit our main **While Loop** so that it triggers when the OpMode is active AND the ElapsedTime timer is less than or equal to 3 seconds.

Let's take a look first at how our timer appears in OnBot Java when checking for less than or equal to 3 seconds:

```java
runtime.seconds() <= 3.0
```

<details>

<summary>Click to Review OnBot Java Operators</summary>

In OnBot Java we can use the following operators when assigning a check for a variable's value:

* Equal to: `==`
* Less than: `<`
* Greater than: `>`
* Less than or equal to: `<=`
* Greater than or equal to: `>=`

</details>

## Modifying Our While Loop

When using our default template, our program will continue running until we press stop on the Driver Hub. However, in this situation we want our program to end when our timer is up. This means we need to modify our **while loop** to add a second condition!

Alongside our check for `opModeIsActive()` we will add our check for if runtime is under 3 seconds:

```java
       waitForStart();
       while (opModeIsActive() && (runtime.seconds() <= 3.0)) {

        }
```

{% hint style="info" %}
`&&` is a logical operator in Java. This symbol is the Java equivalent of "and."&#x20;

Think back to in [Part 1](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/using-a-gamepad-with-a-servo#adding-logic-operators) we learned that `||` means OR in OnBot Java!
{% endhint %}

Now the **While Loop** will now activate when both conditions of the *AND* block are true.

### Quick Check!

Let's give our OpMode a try and test the following scenarios:

* What happens when hitting play quickly after the initialization button is pressed?
* What happens when hitting play 2 seconds after the initialization button is pressed?
* What happens when hitting play 10 seconds after the initialization button is pressed?

<details>

<summary>What happens while testing?</summary>

You may notice the robot moves different distances depending on how long the wait is between INITIALIZATION and PLAYING the program. But why is that?

Remember our timer starts counting when created. Currently, our program creates our timer during initialization meaning it's counting up before Play is ever pressed. If we wait too long our robot may not do anything at all when clicking Play!

</details>

## Resetting the Timer

Not being able to pause between initialization and pressing Play is probably not ideal in most situations. It certainly makes tracking how far the robot will travel more challenging, the opposite of what we'd like ElapsedTime to help us do.

To keep this from happening the timer should be reset once the OpMode is active. Let's add the line `runtime.reset();` between the `waitForStart();` command and the **while loop**.

```java
       waitForStart();
       runtime.reset();
       
       // run until the end of the match (driver presses STOP)
       while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
```

Since this is before our loop our robot will complete it once when Play is pressed. Then will complete the check for our While Loop.

Test your program again with this change!

```java
        rightmotor.setDirection(DcMotorSimple.Direction.REVERSE);
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        runtime.reset();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
            leftmotor.setPower(1);
            rightmotor.setPower(1);
            telemetry.addData("Status", "Running");
            telemetry.update();
```

{% hint style="success" %}
Now let's explore what happens when we change our time limit to different amounts. You can adjust your time limit by changing the 3 seconds within `(runtime.seconds() <= 3.0)` to different numbers.

Consider marking different goals on the floor with tape to practice determining how much time the robot needs to reach it.
{% endhint %}

## Adding Telemetry

In previous parts, we've looked at adding telemetry as a way for the robot to communicate with us. In this situation, it would be helpful for the robot to be able to tell us how much time it has counted so we can make adjustments to our program!

For our **key** let's call it "Number of Seconds in Phase 1" for now. This will be useful for distinguishing where in our program our robot is during the next section.

```java
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
            leftmotor.setPower(1);
            rightmotor.setPower(1);
            telemetry.addData("Status", "Running");
            telemetry.addData("Number of Seconds in Phase 1", runtime.seconds());
            telemetry.update();
```
