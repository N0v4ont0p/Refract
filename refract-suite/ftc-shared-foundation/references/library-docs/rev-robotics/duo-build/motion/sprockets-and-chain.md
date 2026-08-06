> Source: https://docs.revrobotics.com/duo-build/motion/sprockets-and-chain.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/sprockets-and-chain.md).

# Sprockets and Chain

## Sprocket Basics&#x20;

Sprockets are rotating parts that have teeth and can be used with a chain and another sprocket to transmit torque. Sprockets and chain can be used to change the speed, torque or direction of a motor. For sprockets and chain to be compatible with each other, they must have the same thickness and pitch.&#x20;

{% hint style="info" %}
Sprocket and chain is a very efficient way to transmit torque over long distances.
{% endhint %}

Sprockets consist of a disk with straight teeth projecting radially. Sprockets will only work correctly with chain and other sprockets if they are on parallel shafts and the teeth are in the same plane. A chain consists of a continuous set of links that ride on the sprockets to transmit motion. The REV 15mm Build System is designed around #25 Roller Chain ([REV-41-1365](https://www.revrobotics.com/rev-41-1365/)) using compatible [#25 Sprockets](https://www.revrobotics.com/ftc/motion/gears-sprockets-chain/).&#x20;

### Anatomy of a Sprocket

The most common and important features of a sprocket are called out in the figure below.

![](/files/-M9ZHmV-HhrFRbhJbDCK)

{% tabs %}
{% tab title="Number of Teeth" %}
***Number of Teeth*** is the total count of the **number of teeth** (projections) around the whole circumference of a sprocket. For sprockets with very few teeth this number is easily physically counted, but for high tooth counts this may not be isn’t very practical.
{% endtab %}

{% tab title="Pitch Diameter" %}
***Pitch Diameter (PD)*** is an imaginary circle which is traced by the center of the chain pins when the sprocket rotates while meshed with a chain. The ratio of the **pitch diameter** between sprockets can be used to calculate the gear ratio, but more commonly and much more simply the ratio of the **number of teeth** is used for this calculation.
{% endtab %}

{% tab title="Pitch" %}
***Pitch*** represents the amount of **pitch diameter** in inches per tooth. Sprockets with a larger **pitch** will have bigger teeth. Common pitches are 0.25”, known as #25, and 0.375” (#35). The REV Robotics building system uses #25 chain.
{% endtab %}

{% tab title="Outside Diameter" %}
***Outside Diameter (OD)*** will always be larger than the **pitch diameter** but smaller than the **chain clearance diameter**. The **outside diameter** does not account for the additional diameter added by the chain, so it should not be used to check for assembly interference.
{% endtab %}

{% tab title="Chain Clearance Diameter" %}
***Chain Clearance Diameter*** is the outside diameter of a sprocket with chain wrapped around it. The **chain clearance diameter** will always be larger than the **pitch diameter** and the **outside diameter**. The **chain clearance diameter** should be used when checking for interference when placing sprockets very close to other structures.
{% endtab %}
{% endtabs %}

### Anatomy of Chain

Roller chain is used to connect two sprockets together and transfer torque. Roller chain is made up of a series of inner and outer links connected together which forms a flexible strand.

![](/files/-M9ZHmV0-Ztn6yJAhmzn)

{% tabs %}
{% tab title="Outside Links" %}
***Outside Links*** consist of two outside plates which are connected by two ***pins*** that are pressed into each plate. The ***pins*** in the outside link go through the inside of the hollow ***bushings*** when the inner and outer links are assembled. The ***pins*** can freely rotate on the inside of the ***bushings***.
{% endtab %}

{% tab title="Inside Links" %}
***Inside Link*** consist of two inside plates that are connected by two hollow ***bushings*** which are pressed into each plate. The teeth of the sprocket contact the surface of the ***bushings*** when the chain is wrapped around a sprocket.
{% endtab %}

{% tab title="Pitch" %}
***Pitch*** is the distance between the centers of two adjacent ***pins***. Common pitches are 0.25”, known as #25, and 0.375” (#35). The REV 15mm Building System uses #25 chain.
{% endtab %}
{% endtabs %}

### Product Specifications&#x20;

The REV DUO Build System includes both [Metal](https://www.revrobotics.com/rev-41-1723/) and [Plastic](https://www.revrobotics.com/DUO-Plastic-25-Sprockets/) Sprockets. The table below covers some of the basic specifications for the different types of Sprockets.&#x20;

|               | Plastic             | Metal                              |
| ------------- | ------------------- | ---------------------------------- |
| **Material**  | Acetal (Delrin/POM) | 6061 Aluminum                      |
| **Thickness** | 15mm                | 3mm (15mm with Locking Motion Hub) |

REV DUO sprockets are a #25 pitch. Plastic Sprockets are designed to fit a 5mm hex shaft which eliminates the need for special hubs and setscrews. Most Metal Sprockets use a Locking Motion Hub ([REV-41-1719](https://www.revrobotics.com/rev-41-1719/)) in order to connect to a [Hex Shaft](https://www.revrobotics.com/ftc/motion/bearings-linear-slides-pillow-blocks/). The REV DUO Metal Sprockets are at less risk for wear than the Plastic Sprockets.&#x20;

All REV DUO Plastic Sprockets have a M3 bolt hole mounting pattern that is on an 8mm pitch. This makes it easy to directly mount REV DUO [Brackets](https://www.revrobotics.com/ftc/structure/) and [Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/) to sprockets. The 8mm pitch is also compatible with many other building systems.

![](/files/-M9ZHmVKmo_Y6Z92vjWX)

## Using Sprockets and Chain as a Powertrain&#x20;

Transforming the **torque** and **speed** of the motion is accomplished by changing the size of the sprockets.

{% hint style="info" %}
*Physics concepts, like speed and power, have a lot of applications in the REV 15mm Build System. To learn more about them, check out how they apply to sprockets and chains* [*here*](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#sprocket-and-chain-physics)*.*
{% endhint %}

![](/files/-M9clZlqHK2PVLoeGZQm)

A **sprocket size ratio** is the relationship between the number of teeth of two sprockets (input and output). In the image below, the input sprocket is a 15 tooth sprocket and the output is a 20 tooth. The sprocket size ratio for the example is 20T:15T. The ratio in size from the **input** (driving) sprocket to the **output** (driven) sprocket determines if the output is **faster** (less torque) or has more **torque** (slower).&#x20;

{% hint style="info" %}
To learn more about ratio calculations for sprockets check out the [ratio ](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#sprocket-ratio)section.
{% endhint %}

![](/files/-M9_NHsIrzJ2NEXEKk12)

{% hint style="warning" %}
The 15 tooth sprocket outside of the chain loop is known as an **idler**. Idlers do not affect the sprocket size ratio and thus are not part of the calculation. To learn more about idlers check out [Idler ](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#idlers)section on the Advanced Sprockets and Chain page.&#x20;
{% endhint %}

Within a chain loop, motion follows the direction set by the input sprocket. In the example, both sprockets inside the chain loop move counter clockwise. Idlers, which sit outside of the chain loop, are pushed in the opposing direction. So, the 15 tooth idler sprocket is moving clockwise.&#x20;

## How to Use REV DUO Sprockets and Chain?

Like with other motion components, REV DUO Sprockets drive motion with the 5mm Hex Shaft. However, in order to use a Hex Shaft with the Metal Sprockets, a Locking Motion Hub will also need to be used. To learn more about using Hex Shafts and proper motion support and constraint visit the pages linked below:

{% content-ref url="/pages/-M7hM1-IHRWKjRZe9h-K" %}
[Hex Shaft and Spacers](/duo-build/motion/intro/shaft.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M5z1\_4ic51Y1mIBVwMw" %}
[Supporting Motion](/duo-build/building/supporting-motion.md)
{% endcontent-ref %}

{% content-ref url="/pages/-M5z5Jp9K1d1yRq0YfrF" %}
[Constraining Motion](/duo-build/building/constraining-motion.md)
{% endcontent-ref %}

### Chain Tension&#x20;

In order for sprockets to work effectively, it’s important that the **center-to-center distance** is correctly adjusted. The sprocket and chain example with the red 'X', in the image below, may work under very light loads, but they will certainly not work and will skip under any significant loading. The sprockets in this example are too close together so chain is loose enough that it can skip on the sprocket teeth. The sprockets, with the green check mark, are correctly spaced which will provide smooth reliable operation.

{% hint style="info" %}
*To learn more about calculating center-to-center distance for sprockets visit the* [*Advance Sprockets and Chain Page*](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#center-to-center-distance)*.* &#x20;

To ensure proper chain tension it is recommended to create a properly sized chain loop. To learn more about manipulating chain to size check out the [Chain Tool ](/duo-build/motion/sprockets-and-chain/chain-tool.md#manipulating-chain)page.
{% endhint %}

![](/files/-M9_Nhn3b_qUQLsJsZei)

The first step to getting ideal chain tension is to manipulate, or cut the chain to the correct size. Using the center-to-center distance calculation is one of the most accurate ways to find the chain size needed. Once sizing is approximated, use the Chain Tool ([REV-41-1442](https://www.revrobotics.com/rev-41-1442/)) or Master Link ([REV-41-1366](https://www.revrobotics.com/rev-41-1366/)) to break and reform the chain.&#x20;

{% hint style="info" %}
*To learn more about using the Chain Tool and Master Link, check out the* [*Chain Tool* ](/duo-build/motion/sprockets-and-chain/chain-tool.md)*section*
{% endhint %}

When using the slots on REV DUO structural elements its is very easy to adjust and tension the chain if the sizing is off. When using the [Extended Motion Pattern](/duo-build/structure/intro.md#extended-motion-pattern) in conjunction with a chain drive, use Tensioning Bushings ([REV-41-1702](https://www.revrobotics.com/rev-41-1702/)) and Standoffs ([REV-41-1492](https://www.revrobotics.com/rev-41-1492/)).&#x20;

{% hint style="info" %}
*For an example on how to use the Tensioning Bushings check out the* [*Drivetrain* ](/duo-build/channel-drivetrain-build-guide/drive-rail-assembly.md)*guide.*&#x20;
{% endhint %}

### Sprocket Alignment Mark

Sometimes in a design it may be desirable to stack together multiple of the same sprocket on a shaft. In the cases where the number of teeth on the sprocket is not divisible by six, because of how they are oriented when put onto the hex shaft, the teeth may not be aligned between the two sprockets. To ensure all of the sprockets are clocked the same way, use the alignment shaft notch to put all the gears on the shaft with the same orientation.

![](/files/-M9ZHmVL4qyzm0fHZxfY)
