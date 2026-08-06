> Source: https://docs.revrobotics.com/duo-build/structure/intro.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/structure/intro.md).

# Introduction to Structure

## Structure Basics&#x20;

The REV DUO Build System has two major structural components, [Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/) and [Channel](https://www.revrobotics.com/competition/ftc/structure/channel/). REV Extrusion is a rectangular structure rail with slots for [M3 hardware](https://www.revrobotics.com/ftc/hardware/fasteners/) on all four sides. The slots in the Extrusion allow for brackets and other items to be adjusted to any position along the rail. REV Channel is a larger structural member featuring a pattern for actuators, brackets, and other elements to be placed at set intervals. Channels have a combination of a **fixed pitch based system** (known as the **Extended Motion Pattern**) and an **extrusion system** for design flexibility.&#x20;

All REV DUO structural components are M3 hardware compatible. &#x20;

## Extrusion System Versus Pitch System&#x20;

The 15mm extrusion system allows for a more flexible, iterative process than fixed pitch systems. **Fixed pitch based systems** have a set pattern of holes to use for mounting; everything that is mounted is spaced on a multiple or a set fraction of the standard pitch. In contrast, the **15mm extrusion system** allows for flexible mounting positions along the slots. Simply slide any brackets that need to be mounted into the appropriate slot and adjust to the desired position.&#x20;

We believe that the easier it is to adjust your design, the easier it is to iterate and improve that design.&#x20;

See any of the pages linked below to learn more about how to use the extrusion system.

{% content-ref url="/pages/-M5yyrnGs22Qr2uV4kjT" %}
[15mm Extrusion](/duo-build/structure/intro/15mm-extrusion.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M5yyuZ3agN9qHxGWlv3" %}
[15mm x 30mm Extrusion](/duo-build/structure/intro/15mm-x-30mm-extrusion.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M5z-Ocn8ulgEuCgLUK1" %}
[M3 Hardware](/duo-build/structure/m3-hardware.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M5z1WhwVDz1sQhtFwZL" %}
[Tips and Tricks for Building](/duo-build/building/tips-and-tricks.md)
{% endcontent-ref %}

## Extended Motion Pattern&#x20;

While the 15mm Extrusion does not have a fixed pitch other components in the REV DUO Build System do. [Structural brackets](/duo-build/structure/brackets.md#bracket-basics) have M3 holes on an 8mm pitch. While [Motion Brackets](/duo-build/structure/brackets.md#key-terms) have the Motion Pattern, a circular M3 hole pattern on a 16mm diameter is used to mount to REV Robotics shaft accessories.&#x20;

[C Channel](/duo-build/structure/intro/15mm-x-45mm-c-channel.md), [U Channel](/duo-build/structure/intro/45mm-x-45mm-u-channel.md), and [Flat Plate](/duo-build/structure/intro/flat-plate.md) feature the Extended Motion Pattern, a modified circular M3 hole Motion Pattern on a 32mm diameter. This repeats down the length of channel to mount bearings, shafts, brackets, and more.

![](/files/1sIZoBmUGI3X39TSkeRF)

The Extended Motion Pattern starts with M3 holes on an 8mm pitch down the center of the Channel. Each of the holes on the center line pitch forms the "base" for an equilateral triangle with 8mm sides that extends outward towards the edges of the Channel. Every 16mm a center hole is opened up to become a 9mm bearing seat to attach shafts and bearings.&#x20;

{% content-ref url="/pages/-M5yyze9zZtCL\_QoAnGG" %}
[15mm x 45mm C Channel](/duo-build/structure/intro/15mm-x-45mm-c-channel.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M5yz1xgiI86UL9e4oe3" %}
[45mm x 45mm U Channel](/duo-build/structure/intro/45mm-x-45mm-u-channel.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M8pwSLCw6IgzJa89Wxp" %}
[Flat Plate](/duo-build/structure/intro/flat-plate.md)
{% endcontent-ref %}
