> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/using-limits-to-control-range-of-motion.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/using-limits-to-control-range-of-motion.md).

# Using Limits to Control Range of Motion

In [Part 2: Robot Control](/duo-control/hello-robot-blocks/part-2/arm-control-blocks/adding-a-limit-switch.md) the idea of creating a limit switch was introduced using a physical sensor, like a touch sensor. We can make use of our motor's built-in encoder to do something similar. While a physical sensor would be described as a hard limit, using the built-in encoder is called a soft limit.

To set the soft limits we will build off the program created in the last sections (HelloRobot\_ArmEncoder)!

<figure><img src="/files/pGA1n9QpVCEEZuyZrNnV" alt=""><figcaption><p>HelloRobot_ArmEncoder program</p></figcaption></figure>

### Creating minPosition and maxPosition

To start, we need to create our upper and lower limits. Create two new variables one called `minPosition` and one called `maxPosition` to be added to initialization.

<figure><img src="/files/Sm0OymMFvK9TpIg0oXKt" alt=""><figcaption><p>maxPosition and minPosition added for our limits</p></figcaption></figure>

For now we want the `minPosition` set as our starting position and the `maxPosition` set to our 90 degree position. Set `minPosition` equal to <img src="/files/-MYRB7rWtI2jshN4W7LJ" alt="" data-size="original"> and set `maxPosition` equal to <img src="/files/-MbDKWl-0JA7163odOxB" alt="" data-size="original"> .  The ![](/files/jRTezTnH16sB4KOuPH1T) block previously used for [`armPosition`](/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/calculating-target-position.md#adjusting-our-if-else-statement) can be moved to our `maxPosition`.

<figure><img src="/files/DaKQH2Ekov40Fe9ANoiI" alt=""><figcaption></figcaption></figure>

### Adjusting our If/Else Statement

To start, our If/Else Statement will be changed back to a simplified format like we had at the beginning of[ estimating the position of the arm](/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/estimating-the-position-of-the-arm.md).

![If/Else Statement for arm movement](/files/-MbDOTQhQBREe4ZXSqoI)

To set the limit we need to edit our `if/else` statement to include our limits:

* If up on the Dpad is pressed and the position of the arm is less than the `maxPosition`, then the arm will move to the `maxPosition`.&#x20;
* If down on the Dpad is pressed and the position of the arm is greater than the `minPosition` then the arm will move towards the `minPosition`.&#x20;

<figure><img src="/files/MoIw4WqQMA10YoGJdGaL" alt=""><figcaption><p>Use the "logic" dropdown to fill out the statement's check</p></figcaption></figure>

## Overriding Limits

One of the benefits of having a soft limit is being able to exceed that limit.

Remember that the encoders zero tick position is determined by the position of the arm when the Control Hub powers on! So if we aren't careful to reset the arm before powering on our robot this will effect the arm's range of motion. For instance, if we have to reset the Control Hub while the arm is in the 90 degree position, the 90 degree position will become equal to 0 encoder ticks.

As a back up, we can create an override for the range of motion. There are a few different ways an override can be created, but in our case we are going to use the "A" button and touch sensor to help reset our range.&#x20;

### Adding a Gamepad Override

Start by editing the <img src="/files/-M_6poiXjN6Ho7PTyWm3" alt="" data-size="original"> to add another <img src="/files/-MWAnBZGxGoi9TO3k6FC" alt="" data-size="original"> condition. Use the <img src="/files/-MbIJAD2Ou3ksEcYY6ya" alt="" data-size="original"> block as the condition. Add a <img src="/files/-MaAmcRjToPMPrh6OqtT" alt="" data-size="original"> block to the do portion of the <img src="/files/-M_6poiXjN6Ho7PTyWm3" alt="" data-size="original"> block and set the power to -0.5.

<figure><img src="/files/DVgYXequrbI4ep6UcDwk" alt=""><figcaption><p>Adding gamepad "A" override</p></figcaption></figure>

Now that we have this change in place, when the "A" button is pressed the arm will move toward the starting position.&#x20;

### Adding a Touch Sensor Limit

Next, when the arm reaches and presses the touch sensor we want to `STOP_AND_RESET_ENCODER` .

We can create an additional <img src="/files/-MWAm39BsREHDm26Al4M" alt="" data-size="original"> statement that focuses on performing this stop and reset when the touch sensor is pressed. Check out [Programming Touch Sensors](/duo-control/hello-robot-blocks/part-1/programming-touch-sensors.md) from Part 1: Tackling the Basics for review if needed!

<figure><img src="/files/4b1XAV4iAF6PNTXSbUok" alt=""><figcaption><p>Touch sensor limit switch added as a separate If/Else statement</p></figcaption></figure>

Save your OpMode and try testing it!
