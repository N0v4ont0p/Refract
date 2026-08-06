> Source: https://docs.revrobotics.com/duo-build/building/constraining-motion.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/building/constraining-motion.md).

# Constraining Motion

## Constraining Motion Basics&#x20;

Robots need movement to accomplish goals; arms must pivot, wheels must turn, etc. However, movement that isn’t directly related to those actions can affect the accuracy and precision of the robot mechanisms. This unintended motion must be properly restricted, or **constrained**.&#x20;

Long and thin structures can flex and deform, making it difficult to interact with objects and operate in a repeatable manner. Make use of brackets and additional [Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/) or [C Channel](https://www.revrobotics.com/competition/ftc/structure/channel/) to **strengthen** and constrain these structures.&#x20;

## **How to Constrain Motion**

Gears and sprockets must stay aligned or else they won’t work properly.

{% hint style="danger" %}
&#x20;If two sprockets are not perfectly aligned with each other, the chain between them will run off the sprockets.&#x20;
{% endhint %}

Keeping parts aligned on a shaft, and keeping the shaft itself from sliding out is critical for reliably working robot mechanisms. Use a combination of spacers and shaft collars to align and constrain these parts into place.

![](/files/-M7xgaxdf9RgjLOtNorx)

## **Constructing Joints**

Another crucial piece to proper motion constraint is joint construction. Places where structural components, like an Extrusion and Channel, meet need to be properly supported in order to avoid structural collapse during motion.&#x20;

### **Secure with 2 or More Brackets**&#x20;

In most cases joints should have at least two sides joined with brackets for strength and stability. This is especially true for plastic brackets. Commonly this involves taking two of the same kind of bracket and sandwiching the pieces of extrusion, but this can also be two different kinds of brackets such as a 90 Degree Bracket ([REV-41-1305](https://www.revrobotics.com/rev-41-1305/))([REV-41-1480](https://www.revrobotics.com/rev-41-1480/)) and an Inside Corner Bracket ([REV-41-1320](https://www.revrobotics.com/rev-41-1320/))([REV-41-1479](https://www.revrobotics.com/rev-41-1479/)) installed on the same corner.&#x20;

&#x20;

![](/files/-MlBteXzWZEYjnRtp-NG)

### Use Beveled Extrusions  &#x20;

When using brackets to connect extrusion, the joint will be much stronger if the end of the extrusion is beveled (cut at an angle) so that the end will sit flush with the face of the adjoining extrusion. &#x20;

![](/files/-MlBu-9QamQcRqfrMaZw)

Different bracket angles can be combined to make structures.  The joints in this example are all beveled to sit flush against the adjoining extrusion.&#x20;

![](/files/-MlBu9LE25g-rel_sN5R)

### Ways to Create 90 Degree Joints

There are three main ways to create extrusion joints that are at 90 degrees.  The most common is the 90° bracket which mates to pieces of extrusion at 90° in the same plane.  The second is an inside corner bracket is functionally equivalent to the 90° bracket.  The third type is called a lap joint bracket which allows two pieces of extrusion to “overlap.”

**90° Bracket**

![](/files/-MlBtYVQmzLIEl1laVmD)

**Inside Corner Bracket**

![](/files/-MlBtU6x7khT7umhDJt6)

**Lap Corner Bracket** ([REV-41-1321](https://www.revrobotics.com/rev-41-1321/))

![](/files/-MlBtQ2D5bz8zJjaDYG2)
