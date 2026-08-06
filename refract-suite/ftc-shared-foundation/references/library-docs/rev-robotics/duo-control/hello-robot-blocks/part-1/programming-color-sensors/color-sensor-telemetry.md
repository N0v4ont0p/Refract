> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-color-sensors/color-sensor-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-color-sensors/color-sensor-telemetry.md).

# Color Sensor Telemetry

We are going to add several telemetry blocks within our program, but let's start by having our robot tell us how much red, green, or blue it sees when looking at an object with our Color Sensor.&#x20;

For this we will be using the ![](/files/oOQxtT7EY4MZdoca44No) block from the Telemetry menu. We will need three in total, one for each color, which will be entered in the "key".&#x20;

The "precision" on the block will be changed to 3. Precision sets the number of decimal places!

<figure><img src="/files/TULKOmD1ZT4RMDupOIUy" alt=""><figcaption></figcaption></figure>

To "number" we will add the appropriate ![](/files/jJWHX7OwJNqxIwfubYpm) block from the "Color" menu:

<figure><img src="/files/ZmwHuI4o3TTNs8c0Y5ti" alt=""><figcaption></figcaption></figure>

### Adding Hue, Saturation, and Value Telemetry

To add telemetry for hue, saturation, and value we will repeat most of the previous process. However, for "number" we will snap in the matching variable block.&#x20;

<figure><img src="/files/bWHoCzGwWMNmhdEnJvZW" alt=""><figcaption></figcaption></figure>

### Quick Check!

Save your OpMode and give it a try! How do the values change depending on what color object the sensor is looking at?

{% hint style="info" %}
This feature requires the Color Sensor's LED to be switched on!
{% endhint %}

### Alpha Telemetry

While working on your code, you may have noticed something called "alpha". The alpha value of a surface tells how transparent or opaque it may be.&#x20;

Using a similar method as before, we can add a telemetry call for the alpha value to see on our Driver Hub.

<figure><img src="/files/DSr4dK6vsTIDZONjetlA" alt=""><figcaption></figcaption></figure>
