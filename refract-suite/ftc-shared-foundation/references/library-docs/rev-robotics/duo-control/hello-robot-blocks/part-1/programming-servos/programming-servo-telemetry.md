> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-servos/programming-servo-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-servos/programming-servo-telemetry.md).

# Programming Servo Telemetry

## What is Telemetry?&#x20;

**Telemetry** is the process of collecting and transmitting data.  In robotics ,telemetry is used to output internal data from the actuators and sensors to the Driver Hub. It is a way for the robot to communicate back to you the programmer what the robot thinks its doing or seeing. This information can then be used to improve your code, make adjustments to a mechanism, or to strategize when driving around the field if competing.&#x20;

Telemetry blocks in Blocks can be found under the Utilities dropdown menu:

<figure><img src="/files/JlojzsXv6eFtf3PcVuaf" alt=""><figcaption></figcaption></figure>

## Using Telemetry with Servos

The most useful telemetry from the servo is the position of the servo along its 270° range.&#x20;

From the telemetry menu, select the <img src="/files/-MWBCD-8cdq6zfjWEnDn" alt="" data-size="original"> block. &#x20;

Drag the <img src="/files/-MWBCD-8cdq6zfjWEnDn" alt="" data-size="original"> block and place it beneath the **if/else if** block set. In this scenario, we want our telemetry to be constantly providing output rather than waiting for a designated check.&#x20;

From the Servo menu pullout the block <img src="/files/-MWBETk3wvRYKbvYxj0p" alt="" data-size="original"> Drag the Block and attach it to the number parameter on the telemetry blocks.&#x20;

{% hint style="info" %}
For the ![](/files/PTwGEbw2pITqERy44NaX)block "key" is a text box we are able to change to help define what the value is being read out to the Driver Hub's screen. Think of it like an answer key or one used on a map to identify symbols.

Only certain blocks can be added to the second parameter based on what is being requested. In this case the parameter number means the data must be a numeric value.
{% endhint %}

Change the key parameter to "Servo Position"&#x20;

<figure><img src="/files/irSo2lIquVkTeIEsz8KW" alt=""><figcaption></figcaption></figure>

Give your program a go!

<figure><img src="/files/Dxtmytem0q2tRItL3M83" alt=""><figcaption></figcaption></figure>
