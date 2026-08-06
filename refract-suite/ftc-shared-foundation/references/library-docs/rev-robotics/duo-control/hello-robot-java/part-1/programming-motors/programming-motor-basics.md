> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-motor-basics.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-motor-basics.md).

# Programming Motor Basics

## Spinning a Motor:&#x20;

Let's start by getting a motor spinning by adding the line `test_motor.setPower(1);` &#x20;

```java
        while (opModeIsActive()) {
            test_motor.setPower(1);
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
```

Select **Build Everything** to build the code.&#x20;

### Quick Check!

Try running this OpMode on the test bed and consider the following questions:

* How fast is the motor running?&#x20;
* What happens if you change the power from **1** to **5**? What about **100**?
* What happens if you change the power from **1** to **0.3**?

This is a good time to experiment with different values to see how our motor reacts. You might notice that setting our power to 5 or even 100 does not make the motor spin any fast than when set to 1. But setting our power to 0.3 significantly slows our motor's speed, right?

Now what happens if you change the power from **1** to **-1**?

## Setting Direction and Power:

From our perspective, a power level of 1 probably doesn't sound very strong. However, to our robot the power being set to 1 translates to the motor running at 100%. That would mean setting the power to 0.3 requests the motor to spin at 30% of power.&#x20;

When we set our power to a negative power, the motor is told to reverse direction while maintaining that power. So if we set our power to -1 then our motor will still run at  100%, but in the opposite direction than when set to 1.

{% hint style="info" %}
The direction a motor spins may be determined by the power OR may be designated during the initialization process.&#x20;
{% endhint %}
