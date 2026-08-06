> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/turning-the-drivetrain-using-run_to_position.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/turning-the-drivetrain-using-run_to_position.md).

# Turning the Drivetrain Using RUN\_TO\_POSITION

Often times, like in the program created during [Part 2: Robot Control](/duo-control/hello-robot-java/part-2.md), we use `setPower();` to set the drivetrain motors to a set power or power based on a joystick's inputs. The combined power going to both motors help to determine the direction the robot moves or turns.

However, in `RUN_TO_POSITION` mode the encoder counts are used instead to dictate directionality of the motor.

* [x] If a target position value is greater than the current position of the encoder, the motor moves forward.
* [x] If the target position value is less than the current position of the encoder, the motor moves backwards.

Since speed an directionality impacts how a robot turns, target position and velocity need to be edited to get the robot to turn. Consider the following code:

```java
int leftTarget = (int)(610 * COUNTS_PER_MM);
int rightTarget = (int)(-610 * COUNTS_PER_MM);
double TPS = (100/ 60) * COUNTS_PER_WHEEL_REV;
       
        
waitForStart();
        
        
leftmotor.setTargetPosition(leftTarget);
rightmotor.setTargetPosition(rightTarget);
        
leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        
leftmotor.setVelocity(TPS);
rightmotor.setVelocity(TPS);
```

The `rightTarget` has been changed to be a negative target position. Assuming that the encoder starts at zero due to `STOP_AND_RESET_ENCODER` this causes the robot to turn to the right.

Notice the velocity is the same for both motors. If you try running this code, you can see that the robot pivots along its center of rotation.

To get a wider turn, try changing the velocity so that the right motor is running at a lower velocity than the left motor. Adjust the velocity and target position as needed to get the turn you need.
