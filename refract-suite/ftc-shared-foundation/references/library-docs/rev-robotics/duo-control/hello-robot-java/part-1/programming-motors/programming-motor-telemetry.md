> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-motor-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-motor-telemetry.md).

# Programming Motor Telemetry

## Motors and Telemetry&#x20;

Recall that **telemetry** is the process of collecting and transmitting data. There is a lot of useful information our motors could send back to us, but to start let's have it output the power based on the joystick's movement.&#x20;

Similar to our servo program, let's add a new line of `telemetry.addData();`.

```java
while (opModeIsActive()) {
            test_motor.setPower(- this.gamepad1.left_stick_y);
            telemetry.addData();
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
```

This time we are going to set our string as "Motor Power" and after our comma will use test\_motor.getPower()

```java
while (opModeIsActive()) {
            test_motor.setPower(- this.gamepad1.left_stick_y);
            telemetry.addData("Motor Power", test_motor.getPower());
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
```

## Full Code:

```java
    @Override
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
            test_motor.setPower(-this.gamepad1.left_stick_y);
            telemetry.addData("Motor Power", test_motor.getPower());
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
```
