> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/turning-the-drivetrain-using-run_to_position.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/turning-the-drivetrain-using-run_to_position.md).

# Turning the Drivetrain Using RUN\_TO\_POSITION

Often times, like in the program created during [Part 2: Robot Control](/duo-control/hello-robot-blocks/part-2.md), we use the ![](/files/iyrTK3g728cFKdP6epwm) block to set the drivetrain motors to a set power or power based on a joystick's inputs. The combined power going to both motors help to determine the direction the robot moves or turns.&#x20;

However, in `RUN_TO_POSITION` mode the encoder counts are used instead of <img src="/files/-MVwRA9auYOOqnGmzAX7" alt="" data-size="original"> to dictate directionality of the motor.&#x20;

* [x] If a target position value is greater than the current position of the encoder, the motor moves forward.
* [x] If the target position value is less than the current position of the encoder, the motor moves backwards.

Since speed an directionality impacts how a robot turns, target position and velocity need to be edited to get the robot to turn. Consider the following code:&#x20;

<figure><img src="/files/isXK6xNxH5XWvAMhWwpQ" alt=""><figcaption><p>Example encoder code with turning</p></figcaption></figure>

The `rightTarget` has been changed to be a negative target position. Assuming that the encoder starts at zero due to `STOP_AND_RESET_ENCODER` this causes the robot to turn to the right.&#x20;

Notice the velocity is the same for both motors. If you try running this code, you can see that the robot pivots along its center of rotation.&#x20;

To get a wider turn, try changing the velocity so that the right motor is running at a lower velocity than the left motor. Adjust the velocity and target position as needed to get the turn you need.
