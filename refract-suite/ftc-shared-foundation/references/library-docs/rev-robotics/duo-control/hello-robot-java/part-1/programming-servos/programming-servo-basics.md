> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/programming-servo-basics.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/programming-servo-basics.md).

# Programming Servo Basics

### Programming Position Movements

Add the line `test_servo.setPosition(1);` to the OpMode while loop.&#x20;

```java
        while (opModeIsActive()) {
            test_servo.setPosition(1);
            telemetry.addData("Status", "Running");
            telemetry.update();
            
        }
```

Select **Build Everything** ![](/files/N1m2DXs9PLBwZmh9uQhJ) to build the code.&#x20;

### Quick Check!

Let's give our program a try. Take a moment to observe what happens.&#x20;

When running our program for the first time, we should have seen our servo move itself to position 1 and maintain that position. But what happens if we run it again? Does the servo move?

<details>

<summary>Running our program a second time</summary>

Likely, on a second run our servo did not move since it is already at the correct position. Now check what happens if you first manually rotate the servo while the robot is disabled. Once the code is activated again by pressing play we should see it move again!

**Note:** Servos are designed to maintain their position so long as the robot's program is enabled. Trying to forcibly move the servo while ON may damage it and is not recommended.

</details>

{% hint style="info" %}
If your servo did not move as expected, double check your wiring and port are correct compared to your configuration.
{% endhint %}

### Resetting Back to Zero

The intent of the`test_servo.setPosition();`is to set the position of the servo. If the servo is already in the set position when a code is run, it will not change positions. Lets try adding the line `test_servo.setPosition(0).`

In this case, we do not want our servo to reset to 0 every time our code repeats. Because of this where do you think we would add this line?

Recall when we discussed the different sections of our OpMode during [Programming Essentials](/duo-control/hello-robot-java/part-1/programming-essentials.md). Since we only want our servo to reset ONCE we will request it do so during the initialization process when the code is first activated, but before play is pressed.&#x20;

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
            test_servo.setPosition(1);
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
}
```

{% hint style="success" %}
Try running this op mode on the test bed and consider the following question:

* What is different from the previous run?
  {% endhint %}

In many applications starting the servo in a **known state**, like at position zero, is beneficial to the operation of a mechanism. Setting the servo to the known state in the initialization ensures it is in the correct position when the OpMode runs.&#x20;

Take a moment to think about where setting the servo to a known state during initialization may be helpful before moving to the next section!
