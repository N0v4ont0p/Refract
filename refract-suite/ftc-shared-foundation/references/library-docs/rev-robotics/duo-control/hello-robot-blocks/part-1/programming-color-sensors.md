> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-color-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-color-sensors.md).

# Programming Color Sensors

{% hint style="warning" %}
It is recommended to create a new OpMode while following this tutorial. Ours is named HelloRobot\_ColorSensor!

The color and light sensor menus are found under the "Sensors" dropdown as seen below:\
![](/files/PXsK1WTzadXnlRMKQSim)\
\
Additional blocks to set or call colors are within the "Color" menu under Utilities: \
![](/files/MtckDMTSffOvh3RrbD5Z)
{% endhint %}

## Color Sensor Basics:

While a touch sensor features a physical switch to gather information, a color sensor makes use of reflected light. By doing so it collects different data to determine how much light it is seeing, the distance to a surface, and of course what color is in front of it.&#x20;

### But what makes up a color?&#x20;

For our robot we're going to focus on a few key components: hue, saturation, and value. With these we can use something known as the HSV color model to have the robot translate what its seeing into a recognizable color.&#x20;

HSV is a form of a cylindrical RGB color model used to do things like create color pickers for digital painting programs, to edit photos, and for programming vision code.

Hue, saturation, and value all will play a part in helping our robot tell us what color it detects and allow us to make adjustments for something like a uniquely colored game piece!

### Detecting Light vs. Dark

Before we tackle colors, let's start with having our robot use the color sensor to tell us how much light is being reflected.&#x20;

To start, let's grab a ![](/files/stQsBRfRww9S5pROJQ3I) block to add to our loop. Our "key" should be set to "Light detected":

<figure><img src="/files/5D94E0fuYqG8yzD00mMt" alt=""><figcaption></figcaption></figure>

To the "number" place we will pull a ![](/files/dFs3yieMmH3NfjUiTNw6) block from the color sensor menu:

<figure><img src="/files/aZhw6Hnfhy1B19BphDWm" alt=""><figcaption></figcaption></figure>

### Quick Check!

Time to test your program to see what your color sensor detects! While testing think about the following questions:

* Is the number higher when less or more light is detected?&#x20;
* What happens when the color sensor looks at different color surfaces?
* Does the value change when turning the color sensor's LED light on or off?
* Does the value change if there is a shadow or if the lighting in the room changes?

<details>

<summary>What happened?</summary>

Likely, the numbers and differences you saw while testing are different than those we'd see ourselves. There are many factors that might change the color sensor's readings including the lighting in the room and surface material.&#x20;

However, one thing that is the same is that 1 should be the least amount of light, such as when your hand is covering the sensor, and 0 is the most amount of light being seen.

</details>

## Establishing Variables

Let's start by establishing a few variables in our program.

<figure><img src="/files/3tBWtRv0J2eGrlv5wu4g" alt=""><figcaption></figcaption></figure>

We'll be going over [what a variable](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks#what-is-a-variable) is in more detail during Part 2: Robot Control, but for this example we are using them to help our robot translate the data it records more clearly. Our variables will be called "color", "hue", "saturation", "value", and "normalizedColors".&#x20;

<figure><img src="/files/4wj7hKImieyckaOEIil0" alt=""><figcaption></figcaption></figure>

We've discussed how most of these are related to the HSV color model, but what about normalizedColors?&#x20;

Color Normalization is another technique within vision programming intended to help compensate for differences caused by lighting and shadows when looking at colors. This also affects shades of a color. For example, there are a ton of different shades of blue, such as cyan, navy, and aquamarine, but to our robot these will all be referenced as blue.

### Defining Variables

Now that we've named our variables, we need to set them to different values.

From our variable menu we need a ![](/files/2ovvqsqGIjixvNmlhz4l) block. From the dropdown menu, we can change it to "normalizedColors". Next we will snap it in place with a ![](/files/5px8fb8gWFaZYKs5I5Y9) block from the Color Sensor menu below our light detecting telemetry:

<figure><img src="/files/lMXN7IAQqtRlpk078fZ2" alt=""><figcaption></figcaption></figure>

Next, let's go ahead and add set blocks for all our variables:

<figure><img src="/files/CbqGfAnLoHNN7p4FWVWP" alt=""><figcaption></figcaption></figure>

To each we can connect their corresponding block from the Color menu under Utilities:

<figure><img src="/files/2Aot0p5lK2C8sqqdZqen" alt=""><figcaption><p>NormalizedColors is at the bottom of the list.</p></figcaption></figure>

Next we need to change our variable name from the default of "myColor".

<figure><img src="/files/xtWOEWZY6Zy4hgDXwYGJ" alt=""><figcaption></figcaption></figure>

Notice that "color" is matched with NormalizedColors using the matching variable while the rest have the variable set to "color".&#x20;

From here we can add our telemetry blocks to see what values the color sensor detects!
