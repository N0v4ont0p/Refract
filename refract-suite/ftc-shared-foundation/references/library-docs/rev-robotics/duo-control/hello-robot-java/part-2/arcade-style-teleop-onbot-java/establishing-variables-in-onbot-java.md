> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java/establishing-variables-in-onbot-java.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java/establishing-variables-in-onbot-java.md).

# Establishing Variables in OnBot Java

## Creating X and Y Variables:

You may not expect it, but there is a little bit of math that needs to be done to get our robot moving smoothly. But before we dive too deeply into that let's start with the basics of movement we'll need.

To start, create two variables$$x$$and $$y$$. In OnBot Java to establish a variable with a numerical value we will use the object `double`. Our variables are established during our initialization process.

```java
public void runOpMode() {
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");

        rightmotor.setDirection(DcMotorSimple.Direction.REVERSE);
        double x;
        double y;
        
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        waitForStart();
```

&#x20;Then within our loop assign $$y$$  as `y = -gamepad1.right_stick_y;` and the $$x$$ as the `x = gamepad1.right_stick_x;.`

{% hint style="info" %}
Remember positive/negative values inputted by the gamepad's y-axis are inverse of the positive/negative values of the motor.&#x20;
{% endhint %}

```java
while (opModeIsActive()) {
        x = gamepad1.right_stick_x;
        y = -gamepad1.right_stick_y;
        
        rightmotor.setPower(1);
        leftmotor.setPower(1);
        }
```

Setting `x = gamepad1.right_stick_x;` and `y = -gamepad1.right_stick_y;` assigns values from the gamepad joystick to x and y. Depending on the orientation of the joystick, these valuables will receive some value between -1 and 1.&#x20;

For a quick reference let's take a look at what number each variable would be assigned at their far ends:

|                          Joystick Direction                         | $$x$$ | $$y$$ |
| :-----------------------------------------------------------------: | :---: | :---: |
| <img src="/files/-Mefhx7EWkkmadU6LW8V" alt="" data-size="original"> |   0   |   1   |
| <img src="/files/-MefhzwimOC2m68IoDSE" alt="" data-size="original"> |   0   |   -1  |
| <img src="/files/-Mefi1rcj_EIfo6ZRW2u" alt="" data-size="original"> |   -1  |   0   |
| <img src="/files/-Mefi4IQJxLAupAhBq8Y" alt="" data-size="original"> |   1   |   0   |

### What is a Variable?

Right now we have x and y assigned values based on our joystick's movement, but what does that mean? Why is that useful?

Maybe you have seen in a math class before something like this:

$$
a + 8 = 15
$$

In this case, **a** is our variable that has been assigned some value. For this example, we can determine that value is 7. But what does that mean in programming?&#x20;

Variables used in programming follow this same principle. We can define a variable within our code to hold a set value or a value that changes, such as we are doing here. Then whenever that variable is referenced the robot will read it as that assigned value!

So using our example above if I had:

$$
a + 10 = ?
$$

My robot would know my variable of **a** is equal to 7 and therefore calculate the answer as 17 for me!

### When or Why do we use Variables?

Consider for a moment, why should we use a variable when we could just use the number on its own?&#x20;

We'll be using variables in greater detail in later sections, but even for our drive code you will be able to see the use of variables helps keep our program clean and easier to follow.&#x20;

By using setting our *y* variable at the beginning of our code we can inverse it without needing to do so every time we may reference the joystick's y-axis. Within a longer program, having our variables defined at the start would allow us to quickly change a value without having to hunt down or double check that every possible instance in the code has been updated to reflect this change. Instead we are able to change it once and continue testing!
