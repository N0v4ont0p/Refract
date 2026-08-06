> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/calculating-target-position.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/calculating-target-position.md).

# Calculating Target Position

Now that we have an estimate for our target position let's see if we can refine it to be more precise using similar methods to what we covered during the [Drivetrain Encoders section](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks.md).&#x20;

## What's Needed for the Conversion

### Ticks per Revolution

Recall, that ticks per revolution of the encoder shaft is different than the ticks per revolution of the shaft that is controlling a mechanism, such as what we determined on our [Drivetrain](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/converting-encoder-ticks-to-a-distance.md#whats-needed-for-the-conversion).

{% hint style="info" %}
For more information on the effect of motion transmission across a mechanism check out the [Compound Gearing](https://docs.revrobotics.com/duo-build/actuators/gears/gears-advanced#compound-gearing) section.&#x20;
{% endhint %}

The amount of ticks per revolution of the encoder shaft is dependent on the motor and encoder. Manufacturers of motors with built-in encoders will have information on the amount of ticks per revolution.

{% hint style="info" %}
Visit the manufacturers website for your motor or encoders for more information on encoder counts. For HD Hex Motors or Core Hex Motors visit the [Motor](https://docs.revrobotics.com/duo-build/actuators/motors) documentation.&#x20;
{% endhint %}

In the [Core Hex Motor specifications ](https://docs.revrobotics.com/duo-build/actuators/motors/core-hex-motor#product-specs)there are two different Encoder Counts per Revolution numbers:

* At the motor - 4 counts/revolution
* At the output - 288 counts/revolution

At the motor is the number of encoder counts on the shaft that encoder is on. This number is equivalent to the 28 counts per revolution we used for the HD Hex Motor. &#x20;

The 288 counts "at the output" accounts for the change in resolution after the motion is transmitted from the motor to the built in 72:1 gearbox.&#x20;

Lets use the **288 as ticks per revolution** so that we do not have to account for the gearbox in our total gear reduction variable.&#x20;

### Total Gear Reduction

Since we built the the gear reduction from the motor gearbox into the ticks per revolution the main focus of this section is calculating the gear reduction of the arm joint.&#x20;

The motor shaft drives a 45 tooth gear that transmits motion to a 125 tooth gear. The total gear ratio is 125T:45T. To calculate the gear reduction for this gear train, we can simply divide 125 by 45.&#x20;

$$
\frac{125}{45} = 2.777778
$$

### Quick Summary

To summarize, for the Class Bot V2 the following information is true:&#x20;

| Ticks per revolution | 288 ticks |
| -------------------- | --------- |
| Total gear reduction | 2.777778  |

## Adding Arm Encoders to the Program

### Establishing Initialization Variables

Now that we have this information lets create two constant variables:&#x20;

* `COUNTS_PER_MOTOR_REV`
* `GEAR_REDUCTION`

Add the variables `COUNTS_PER_MOTOR_REV` and `GEAR_REDUCTION` variables to the  initialization  section of the program.

<figure><img src="/files/x6JnpgBaRRfPbENuiSG7" alt=""><figcaption><p>Adding COUNTS_PER_MOTOR_REV and GEAR_REDUCTION</p></figcaption></figure>

Our `COUNTS_PER_MOTOR_REV` and `GEAR_REDUCTION` variables will be set to a value that will then be used to calculate our other two variables `COUNTS_PER_DEGREE` and `COUNTS_PER_GEAR_REV`. &#x20;

Let's go ahead and add these variables to our OpMode.

<figure><img src="/files/WymesmCvyaG5fHO2z0ji" alt=""><figcaption><p>Full list of initialization variables</p></figcaption></figure>

### Adding Calculations to the Variables

Once the variables are created and in place, use the <img src="/files/-MYRB7rWtI2jshN4W7LJ" alt="" data-size="original"> blocks to set the first variables to the respective [values](#quick-summary)

![](/files/-ManrpfRGL9WbH0S_hlT)

Now that these two variables have been defined, we can use them to calculate two other variables: the amount of encoder counts per rotation of the 125T driven gear and the number of counts per degree moved.

Calculating counts per revolution of the 125T gear (or `COUNTS_PER_GEAR_REV`) is the same formula we used for [`COUNTS_PER_WHEEL_REV` variable on our drivetrain](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/converting-encoder-ticks-to-a-distance.md#calculating-counts_per_wheel_rev), so to get this variable we can multiple `COUNTS_PER_MOTOR_REV` by `GEAR_REDUCTION`.

<figure><img src="/files/0lOcYTGpgklogbpjKI6W" alt=""><figcaption></figcaption></figure>

To calculate the number of `COUNTS_PER_DEGREE` divide the `COUNTS_PER_GEAR_REV` variable by 360.&#x20;

![](/files/-Mao6OjsQ1lyb5dBxPIQ)

All together our variables will look like below:

<figure><img src="/files/2O0BZHIwBiOPrNtgCPgt" alt=""><figcaption><p>All of the initialization variables calculated</p></figcaption></figure>

### Adjusting our If/Else Statement

We need to create one more non-constant variable that will act as our position. This will be called `armPosition`.&#x20;

To get to the 90 degree position, the arm needs to move roughly 45 degrees therefore set arm position equal to `COUNTS_PER_DEGREE` times 45.&#x20;

![](/files/-Maok2yFCAHOUh00l070)

Add this variable to the <img src="/files/-M_6pst95i16Ri14yZ4b" alt="" data-size="original"> section of the <img src="/files/-M_76Lu914wbfp2TPuaG" alt="" data-size="original"> statement, as this section dictates the 90 degree position. Add the <img src="/files/-MaotXo3dfKi8y9Cp7gE" alt="" data-size="original"> block to the <img src="/files/-MaosWQi5hUAA9ONxsD6" alt="" data-size="original"> block.&#x20;

<figure><img src="/files/io2wGmwAJLKr0BSkMTID" alt=""><figcaption><p>Adjusting the If/Else to include the armPosition</p></figcaption></figure>

Save your OpMode and give it a test!
