> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-color-sensors/detecting-color.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-color-sensors/detecting-color.md).

# Detecting Color

We've asked our robot to gather a lot of data with the color sensor. Now let's have it use that information to output an actual color name rather than just a value!

## Detecting Common Colors

Recall when we learned about using [`if/else` statements while working with the touch sensor.](/duo-control/hello-robot-blocks/part-1/programming-touch-sensors.md#touch-sensor-basics)&#x20;

Let's first set up the skeleton of our if/else statement for determining different colors:

<figure><img src="/files/R1fkzpa0m2KN5pkunBPK" alt=""><figcaption><p>Detecting color if/else statement</p></figcaption></figure>

Once we've added our ![](/files/DGRyM9dMNcubD7h2besn) block we'll click the gear to add the needed "else if" pieces to have enough for all our colors. To each we will add a ![](/files/VTRWOTpKdDW56tXxD4Jj) block from the Logic menu. Next we can add our ![](/files/9VJX5yIVq6Gwjvhlb5p3) variable and a ![](/files/GhPVwQxNLflhh2T8Q9FD) block to each side of this logic statement. We want for each if/else our robot to check if the read hue is LESS THAN a set number!

<figure><img src="/files/PyybSAsvOq8C9foAt7nk" alt=""><figcaption><p>Is the seen hue less than _?</p></figcaption></figure>

Last we can add our telemetry for our robot to read out information to the Driver Hub based on what it detects:

<figure><img src="/files/TNvrPU0XjczfudnpxTah" alt=""><figcaption><p>Added telemetry blocks</p></figcaption></figure>

Each check will be for a certain color that is within the specified range. "Key" can be changed to "Color" on the telemetry blocks. We can add the colors in first:

<figure><img src="/files/A8mhn0BkpjQrFIlQVvoz" alt=""><figcaption><p>If/else statement with colors added</p></figcaption></figure>

Next we will add our values for the hue ranges. For example, a color that's hue is between 90-149 should appear as green.

<figure><img src="/files/yvGlDLzeamSRyqipQt3E" alt=""><figcaption><p>Completed if/else statement</p></figcaption></figure>

The exact hue values may need to be adjusted slightly, but those used above are based on the default conversion of HSV to RGB when using hue to identify color.&#x20;

You'll notice that "red" is detected for values under 30 and above 350. This is intentional as red is the beginning and end of the RGB spectrum!

Let's snap our If/Else statement into our loop below the "Alpha" telemetry call.

<figure><img src="/files/lcBqhocbTptNoze5UvlJ" alt=""><figcaption><p>If/Else statement added to the full program.</p></figcaption></figure>

Save your OpMode and give it a try! You can adjust the values as you need to better reflect the colors available or changes due to lighting in the room.
