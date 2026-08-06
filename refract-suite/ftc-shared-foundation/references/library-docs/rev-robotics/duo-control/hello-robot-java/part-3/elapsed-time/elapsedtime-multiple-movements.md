> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-multiple-movements.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/elapsed-time/elapsedtime-multiple-movements.md).

# ElapsedTime - Multiple Movements

Right now our robot should move forward 3 seconds then stop. What if we wanted our robot to do something else after those 3 seconds? How do we request our program to continue?

To save some time we can copy and paste our entire loop and timer reset below our existing code to make adjustments to!

```java
runtime.reset();
while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
    leftmotor.setPower(1);
    rightmotor.setPower(1);
    telemetry.addData("Number of Seconds in Phase 1", runtime.seconds());
    telemetry.update();
        }

runtime.reset();
while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
    leftmotor.setPower(1);
    rightmotor.setPower(1);
    telemetry.addData("Number of Seconds in Phase 1", runtime.seconds());
    telemetry.update();
        }
```

Notice our second loop also has a call for telemetry data, however the name is the same! Let's edit it to be "Number of Seconds in Phase 2". Keep the names in mind if you duplicate additional loops.

{% hint style="warning" %}
When copying and pasting code within OnBot Java be sure to double check you still have the correct number of brackets! You may see a line highlighted in red in the case of a bracket missing or if there are too many: ![](/files/DAVK5uXyUGKjMrhD6iNH)
{% endhint %}

## Quick Check! <a href="#quick-check" id="quick-check"></a>

Give your program a test to see what happens. Think about the following while testing:

* How long does the robot move?
* Could you tell when the robot switched between Phase 1 and 2?
* What happens if we change the power in the second loop?

## Reversing Movement

Having multiple loops with different amounts of time can give us a lot of power to help our robot navigate an area. For now let's have our robot complete it's first movement forward for 3 seconds, then reverse back to the start.

This simply requires changing our power in the second loop to -1 !

```java
runtime.reset();
while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
    leftmotor.setPower(1);
    rightmotor.setPower(1);
    telemetry.addData("Number of Seconds in Phase 1", runtime.seconds());
    telemetry.update();
        }

runtime.reset();
while (opModeIsActive() && (runtime.seconds() <= 3.0)) {
    leftmotor.setPower(-1);
    rightmotor.setPower(-1);
    telemetry.addData("Number of Seconds in Phase 2", runtime.seconds());
    telemetry.update();
        }
```
