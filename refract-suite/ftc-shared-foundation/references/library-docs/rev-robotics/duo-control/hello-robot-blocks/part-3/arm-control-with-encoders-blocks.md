> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks.md).

# Arm Control with Encoders - Blocks

{% hint style="info" %}
This section is written with the Class Bot V2 in mind, but can be followed with appropriate adjustments, such as mechanism angles, on other robot designs!
{% endhint %}

We've covered using encoders for a drivetrain, but what about for a different mechanism, such as an arm? Unlike the drivetrain, the arm does not follow a linear path. This means rather than converting to a linear distance it makes more sense to convert the encoder ticks into an angle measured in degrees!&#x20;

In the image below two potential positions are showcased for the Class Bot arm. One of the positions (blue) is the position where the arm meets the limit of the touch sensor. Due to the limit, this position will be our default starting position.&#x20;

From the Class Bot build guide, it is known that the Extrusion supporting the battery sits a 45 degree angle. Since the arm is roughly parallel to these extrusion when it is in the starting position, we can estimate that the default angle of the arm is roughly 45 degrees.&#x20;

<figure><img src="/files/WSXYUcUfmT9MnwgUlOYq" alt=""><figcaption></figcaption></figure>

The goal of this tutorial is to determine the amount of encoder ticks it will take to move the arm from its starting position to a position around 90 degrees. &#x20;

There are a few different ways this can be accomplished. For example, an estimation can be done by moving the arm to the desired position and recording the telemetry feedback from the Driver Station. Alternatively, we can do the math calculations to find the amount of encoder ticks that occur per degree moved.&#x20;

Follow through this tutorial to walk through both options and determine which is the best for your team!
