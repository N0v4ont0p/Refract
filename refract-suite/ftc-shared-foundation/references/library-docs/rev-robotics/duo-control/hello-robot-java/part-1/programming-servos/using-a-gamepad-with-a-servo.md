> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/using-a-gamepad-with-a-servo.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/using-a-gamepad-with-a-servo.md).

# Using a Gamepad with a Servo

## Programming a Servo with a Gamepad

Having our robot able to rotate the servo automatically can be incredibly useful, especially when writing an autonomous program, but what if I want to control the positions with my gamepad?&#x20;

Let's take a look at how we can add input commands to our code!

For this example the known state will stay at position 0, so that after initialization the servo will be a the -135 degree position of the servo range. The following list shows what buttons correspond with which servo position:

{% hint style="info" %}
If you are using a PS4 Controller, selecting the appropriate button from the dropdown in Blocks may be easier to follow when looking back at your code. The buttons are also interchangeable when programming in Blocks. (ex: Y  in code = Triangle pressed on controller)
{% endhint %}

| **Button** | Degree Position | Code Position |
| ---------- | --------------- | ------------- |
| Y/Triangle | -135            | 0             |
| X/Square   | 0               | 0.5           |
| B/Circle   | 0               | 0.5           |
| A/Cross    | 135             | 1             |

## Introducing If/Else Statements

One of the most common logic statements used in programming is an **if/else** statement, also known as an **if/then** statement. In its most simple format we will be asking our robot to check **IF** something is happening and if the answer is yes, or true in our robot's mind, **THEN** it will **DO**  what has been asked.&#x20;

### Quick Check!

During this section we are going to be asking "If the Y button is pressed on our controller then move our servo to position 0."&#x20;

```java
if (gamepad1.y){
    test_servo.setPosition(0);
}
```

If our servo will move to position 0 when the previous statement is TRUE, what do expect to happen when the answer is FALSE (or the Y button is not pressed)?

<details>

<summary>What will happen when the answer is FALSE?</summary>

At the moment, we have not asked our robot to do anything specific when our statement is false. This means for now our servo will not move or change while our Y button is not pressed.&#x20;

</details>

## If/Else If Statements:

An `if/else if` statement takes in multiple different conditional statements. If the first conditional statement is found to be false then the second conditional state is analyzed.&#x20;

```java
if (gamepad1.y){
    test_servo.setPosition(0);
    
} else if () {
  
}
```

### Quick Check!

Let's add to our existing logic statement the ability to move our servo to position 1 when A is pressed on our controller. Give it a try first before revealing the answer below!

How would our full logic statement be read once our new blocks are added?

<details>

<summary>Reveal the answer!</summary>

Programming our servo to move to position 1 when A is pressed will look very similar to our existing code:

<pre class="language-java"><code class="lang-java"><strong>if (gamepad1.y){
</strong>    test_servo.setPosition(0);
    
} else if (gamepad1.a) {
    test_servo.setPosition(1);
}
</code></pre>

Now our statement reads: "If the Y button is pressed then move the servo to position 0, else if the A button is pressed then move the servo to position 1."

</details>

{% hint style="success" %}
If you have not already, test the code we have written thus far! The previous `test_servo.setPosition(1);`should be removed if it has not already.

* What happens when both buttons are pressed at the same time?
  {% endhint %}

## Adding Logic Operators:

We've previously added our ability to move to position 0 and 1, but what about 0.5?&#x20;

You may have noticed in our gamepad chart at the beginning of this section that we are going to have two buttons able to move our servo to position 0.5. This is so we can practice using a **logical operator.**&#x20;

In OnBot Java, `||` means "or" allowing the robot to check if one of two buttons things are true. In this case, it will check if the x OR b button are pressed on the gamepad.&#x20;

<pre class="language-java"><code class="lang-java"><strong>if (gamepad1.y){
</strong>    //move to position 0
    test_servo.setPosition(0);
    
} else if (gamepad1.x || gamepad1.b) {
    //move to position 0.5
    test_servo.setPosition(0.5);

} else if (gamepad1.a) {
    //move to position 1 
    test_servo.setPosition(1);
    
}
</code></pre>

{% hint style="success" %}
Click to Build Everything and give your program a try!
{% endhint %}

There are three different paths in this **if/else if** statement. If the first conditional statement is true (the Y button is pressed) the servo moves to code position 0 and the other conditional statements are ignored.&#x20;

If the first condition is false (the Y button is not pressed) the second condition is analyzed. This means the order we add our pathways DOES matter. If  X and A are pressed at the same time, the robot will will try to prioritize the X button first.&#x20;

## Full Program:

```java
public void runOpMode() {
        control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");
        
        test_servo.setPosition(0);

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            if (gamepad1.y){
                //move to position 0
                test_servo.setPosition(0);
    
            } else if (gamepad1.x || gamepad1.b) {
                //move to position 0.5
                test_servo.setPosition(0.5);

            } else if (gamepad1.a) {
                //move to position 1
                test_servo.setPosition(1);
                        }
                        
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
}
```
