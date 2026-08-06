> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java/programming-arcade-drive.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java/programming-arcade-drive.md).

# Programming Arcade Drive

### Programming Arcade Drive

With our variables established and movement understood we just need to add our equations to each power!&#x20;

```java
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
        x = gamepad1.right_stick_x;
        y = -gamepad1.right_stick_y;
        
        rightmotor.setPower(y-x);
        leftmotor.setPower(y+x);
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
```
