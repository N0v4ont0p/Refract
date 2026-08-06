> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/converting-encoder-ticks-to-a-distance.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/converting-encoder-ticks-to-a-distance.md).

# Converting Encoder Ticks to a Distance

In the previous section, the basic structure needed to use `RUN_TO_POSITION`was created. The placement of<img src="/files/-MYGq13GHps2CyeLWbZt" alt="" data-size="original">within the code, set the target position to 1000 ticks.&#x20;

But how far is a tick and how can we use them to help our robot navigate an area? We could attempt to estimate the distance the robot moves per tick or we can convert the amount of ticks per revolution of the encoder into a unit like millimeters or inches! For instance, if you work through the conversion process and find out that a drivetrain takes 700 ticks to move an inch, this can be used to find the total number of ticks need to move the robot 24 inches.

{% hint style="warning" %}
Reminder that the basis for this guide is the [Class Bot V2](https://docs.revrobotics.com/duo-build/ftc-starter-kit-class-bot). The REV DUO Build System is a metric system. Since part of the conversion process references the diameter of the wheels, this section will convert to ticks per mm.
{% endhint %}

## What's Needed for the Conversion&#x20;

This process will take a bit of math to achieve so let's break it down.

When using encoders built into motors, converting from ticks per revolution to ticks per unit of measure moved requires the following information:

* [x] Ticks per revolution of the encoder shaft
* [x] Total gear reduction on the motor
  * Including gearboxes and motion transmission components like gears, sprockets and chain, or belts and pulleys
* [x] Circumference of the driven wheels

### Ticks per Revolution

The amount of ticks per revolution of the encoder shaft is dependent on the motor and encoder. Manufacturers of motors with built-in encoders will have information on the amount of ticks per revolution.&#x20;

For HD Hex Motors the encoder counts 28 ticks per revolution of the motor shaft.&#x20;

{% hint style="info" %}
Visit the manufacturers website for your motor or encoders for more information on encoder counts. For HD Hex Motors or Core Hex Motors visit the [Motor](https://docs.revrobotics.com/duo-build/actuators/motors) documentation.&#x20;
{% endhint %}

### Total Gear Reduction

Since ticks per revolution of the encoder shaft is before any gear reduction calculating the total gear reduction is needed. This includes the gearbox and any addition reduction from motion transmission components. To find the total gear reduction use the [Compound Gearing formula](https://docs.revrobotics.com/duo-build/actuators/gears/gears-advanced#compound-gearing).&#x20;

For the Class Bot V2 there are two UltraPlanetary Cartridges, 4:1 and 5:1, and an additional gear reduction from the UltraPlanetary Output to the wheels, 72T:45T ratio.

{% hint style="info" %}
The UltraPlanetary Cartridges use the nominal gear ratio as a descriptor. The actual gear ratios can be found in the [UltraPlanetary Users Manual's Cartridge Details](https://docs.revrobotics.com/ultraplanetary/cartridge-details#actual-cartridge-gear-ratios).&#x20;
{% endhint %}

Using the compound gearing formula for the Class Bot V2 the total gear reduction is:

$$
\frac{3.61}{1} \* \frac{5.23}{1} \* \frac{72}{45} = 30.21
$$

{% hint style="info" %}
Unlike the spur gears used to transfer motion to the wheels, the UltraPlanetary Gearbox Cartridges are planetary gear systems. To make calculations easier the gear ratios for the Cartridges are already reduced.&#x20;
{% endhint %}

### Circumference of the Wheel

The Class Bot V2 uses the 90mm Traction Wheels. 90mm is the diameter of the wheel. To get the appropriate circumference use the following formula&#x20;

$$
circumference = diameter \* \pi
$$

You can calculate this by hand, but for the purpose of this guide, this can be calculated within the code.&#x20;

{% hint style="info" %}
Due to wear and manufacturing tolerances, the diameter of some wheels may be nominally different. For the most accurate results consider measuring your wheel to confirm that the diameter is accurate.&#x20;
{% endhint %}

### Quick Summary

To summarize, for the Class Bot V2 the following information is true:&#x20;

| Ticks per revolution       | 28 ticks        |
| -------------------------- | --------------- |
| Total gear reduction       | 30.21           |
| Circumference of the wheel | $$90mm \* \pi$$ |

## Translating the Conversion to Code

### Setting up Variables

Each of these pieces of information will be used to find the number of encoder ticks (or counts) per mm that the wheel moves. Rather than worry about calculating this information by hand, these values can be added to the code as constant variables. To do this create three variables:

* `COUNTS_PER_MOTOR_REV`
* `DRIVE_GEAR_REDUCTION`
* `WHEEL_CIRCUMFERENCE_MM`

{% hint style="info" %}
The common naming convention for constant variables is known as CONSTANT\_CASE, where the variable name is in all caps and words are separated by and underscore.&#x20;
{% endhint %}

We'll add the [variables](/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks.md) to the initialization section of the OpMode:&#x20;

<figure><img src="/files/1mt1e6tzKQxwvn9Y3ha9" alt=""><figcaption><p>Adding our new variables to initialization</p></figcaption></figure>

Once the variables are created and added to the OpMode, use the <img src="/files/-MYRB7rWtI2jshN4W7LJ" alt="" data-size="original"> blocks to set the variables to the respective values.&#x20;

For `WHEEL_CIRCUMFERENCE_MM`  a combination of the <img src="/files/-MYRS32ax0_5fhPWNou9" alt="" data-size="original"> , <img src="/files/-MYRB7rWtI2jshN4W7LJ" alt="" data-size="original"> , and<img src="/files/-MYRSB17mEeOLwbUp2y2" alt="" data-size="original"> blocks will be used to get the circumference of the wheel.&#x20;

![](/files/-MYRP6ZUXJNSFde2UzFX)

Now that these three variables have been defined, we can use them to calculate two other variables: the **amount of encoder counts per rotation of the wheel** and **the number of counts per mm that the wheel moves**.&#x20;

<figure><img src="/files/Bdr6agurev2XBK6UtSIQ" alt=""><figcaption></figcaption></figure>

### Calculating COUNTS\_PER\_WHEEL\_REV

To calculate counts per wheel revolution multiply `COUNTS_PER_MOTOR_REV` by `DRIVE_GEAR_REDUCTION` Use the following formula:

$$
y = a
\*b
$$

Where:&#x20;

* $$a$$ = `COUNTS_PER_MOTOR_REV`
* $$b$$ = `DRIVE_GEAR_REDUCTION`&#x20;
* $$y$$ = `COUNTS_PER_WHEEL_REV`

Again math blocks need to be used to define these variables. Lets start with the `COUNTS_PER_WHEEL_REV`  variable. Add a <img src="/files/-MYRS32ax0_5fhPWNou9" alt="" data-size="original"> to the <img src="/files/-MYRfuLihTonvd67Sk4b" alt="" data-size="original"> block. Add the <img src="/files/-MYeigphTtcNkGuZlxOg" alt="" data-size="original"> and <img src="/files/-MYeikxKcR2ab3l-siE2" alt="" data-size="original">blocks to either side of the <img src="/files/-MYRS32ax0_5fhPWNou9" alt="" data-size="original"> block.

<figure><img src="/files/1ehXrWi0shwDAmB72rzo" alt=""><figcaption></figcaption></figure>

### Calculating COUNTS\_PER\_MM

Once the `COUNTS_PER_WHEEL_REV` is calculated, it can be used to calculate the counts per mm that the wheel moves. To do this divide the `COUNTS_PER_WHEEL_REV` by the `WHEEL_CIRCUMFERENCE_MM`. Use the following formula.

$$
x = \frac{(a\*b)}{c} = \frac{y}{c}
$$

Where,

* $$a$$ = `COUNTS_PER_MOTOR_REV`
* $$b$$ = `DRIVE_GEAR_REDUCTION`
* $$c$$ = `WHEEL_CIRCUMFERENCE_MM`
* $$y$$ = `COUNTS_PER_WHEEL_REV`
* $$x$$ = `COUNTS_PER_MM`

{% hint style="warning" %}
`COUNTS_PER_WHEEL_REV`will be created as a separate variable from `COUNTS_PER_MM` as it is used in calculating a target velocity.&#x20;
{% endhint %}

Since `COUNTS_PER_WHEEL_REV`  has been calculated it can be used to calculate `COUNTS_PER_MM` add the <img src="/files/-MYepPimZMwCPPARot8P" alt="" data-size="original"> to the <img src="/files/-MYeqNUzRqrbAl-CypnS" alt="" data-size="original">. On the left side of the <img src="/files/-MYepPimZMwCPPARot8P" alt="" data-size="original"> add the <img src="/files/-MYey5fLzndMDfYs7HdW" alt="" data-size="original"> block. On the right side of the <img src="/files/-MYepPimZMwCPPARot8P" alt="" data-size="original"> add the <img src="/files/-MYf-5tkdwxOZ7wRXrM-" alt="" data-size="original"> .

![](/files/-MYf7Q7ov7Ll3ETClAK_)

### Final Variables

Once `COUNTS_PER_WHEEL_MM` is set, this completes the conversion process, and all constant variables are set.&#x20;

<figure><img src="/files/wr7BO6ngkvlQKWC3X9jl" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/VMwxix5JTvaDmg5jjhnf" alt=""><figcaption></figcaption></figure>

Make sure to save your OpMode here to prevent any progress being lost in the event of a disconnect!
