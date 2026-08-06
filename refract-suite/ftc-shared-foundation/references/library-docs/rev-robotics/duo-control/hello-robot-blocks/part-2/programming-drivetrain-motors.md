> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/programming-drivetrain-motors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/programming-drivetrain-motors.md).

# Programming Drivetrain Motors

In [Part 1](/duo-control/hello-robot-blocks/part-1.md) we learned how to control a single motor by giving it power or input from a joystick. For controlling a drivetrain, we need to be able to control two motors simultaneously to help the robot move. While we could try adding each motor individually, Blocks has a **dual** motor block available already for just this purpose.

To access the **dual** block you will need to select the actuators dropdown menu:

<figure><img src="/files/ydg2LAjzk2HZ126z71SL" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Not seeing DcMotor under the actuators menu? Make sure your[ configuration](/duo-control/hello-robot-blocks/configuration.md) has been properly set up and activated before getting started!
{% endhint %}

## Programming Drivetrain Motors

Any code from Part 1 should be moved to the side of the workspace or deleted before continuing this section. Alternatively, you may choose to create a new program.

***

Add the <img src="/files/-MVNpboWEAOhTj8EGLe4" alt="" data-size="original"> block to op mode while loop.&#x20;

<figure><img src="/files/bvEtco8DnEHZNkEogsXp" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
When there are multiple of the same type of variable (such as multiple DcMotors) the variable specific blocks will choose a default variable based on alphabetical order. For this example, OpMode DcMotor blocks will default to the **arm** variable.&#x20;
{% endhint %}

Use the variable drop down menu on the block to change from arm to rightmotor.

<figure><img src="/files/5aaRLJNV5YrDNN9ddEa6" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/qyTkvc6iAgC3Bsy22SXm" alt=""><figcaption></figcaption></figure>

### Quick Check!

Before running your code for the first time, pause and think about the following:

* What do you expect your robot to do once the program is activated?&#x20;

Now save your OpMode using the button in the upper lefthand corner and give your program a go!

<details>

<summary>Did the robot move as you expected? </summary>

You may have expected your robot to move in a straight line forwards or backwards. Instead, your robot likely spun in a circle.&#x20;

When motors run at different speeds they spin along their center pivot point. But the motors are both set to a power of 1 here so what else could be the cause?

</details>

{% hint style="danger" %}
Always keep the Driver Hub within reach in the case of the event that a robot does not perform as expected. When in doubt, disable your robot to keep you and it safe.&#x20;
{% endhint %}

## Mirroring Motors

DC Motors are capable of spinning in two different directions depending on the current flow provided. When a positive power value is applied the motors will spin in a clockwise direction. The opposite will happen when using a negative power value, meaning the motors will spin in a counter clockwise direction.

But how does that help with our current spinning robot? Let's take a closer look at our physical robot to find out:

<figure><img src="/files/BAN9rLe7q7Z9Cm0CvVig" alt=""><figcaption><p>Top down view of the Class Bot V2</p></figcaption></figure>

Notice how the motors on your robot are currently mirrored from each other as part of the drivetrain.  Now think about how we learned that when giving the motors a positive value they should turn clockwise. This is still how, however while they may both be rotating clockwise, the direction they know to be as clockwise is opposite.

![Motors running the same direction, but facing opposite ways!](/files/-MVrsHYT6qr4y1KLl-RD)

Try activating your robot's code again, but this time watching which direction the wheels turn. You may consider supporting the robot's frame so the wheels are suspended to make this easier to see.

## Reversing a Motor:

There are a couple ways we could adjust our program to help our robot not to be a spinning top. For example, we could make sure the power is set to a negative value whenever one of our motors is called. Or we could simple reverse our motor's direction during initialization.&#x20;

***

Add <img src="/files/-MVOBZ-rzSPjT4Aje-Ub" alt="" data-size="original"> to your program, under the <img src="/files/-MVRzzz2RWu0i_oNzqo3" alt="" data-size="original"> comment block. If you recall, blocks placed in this section will run AFTER the intilizal button is pressed on the Driver Hub, but BEFORE the play button is clicked.

<figure><img src="/files/GsvKO1Xr04lsR8SuqsGm" alt=""><figcaption></figcaption></figure>

Now with the <img src="/files/-MVOBZ-rzSPjT4Aje-Ub" alt="" data-size="line"> block added the direction for the rightmotor will always be reversed for this program. Our power values do not need to be changed.

Go ahead and give it a try!
