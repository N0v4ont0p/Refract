> Source: https://docs.revrobotics.com/duo-build/motion/gears/gears-advanced.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/gears/gears-advanced.md).

# Advanced Gears

## Gear Physics&#x20;

Gears are one common way to transmit power and change the output torque or speed of a mechanical system. Understanding these basic concepts is required to make optimized design decisions which consider the trade-off between torque and speed for a system with a given power.&#x20;

{% tabs %}
{% tab title="Speed" %}
***Speed*** is the measure of how fast an object is moving. The **speed** of an object is how far it will travel in a given amount of time. For rotating parts like gears and wheels, **speed** is expressed in how many revolutions are made in a given amount of time. Under ideal conditions, the rotation of a wheel is converted into linear **speed** and can be calculated by multiplying the diameter of the wheel by the rotations for a given time. The SI unit for **speed** is meters per second (m/s), but **speed** is also commonly expressed in feet per second (ft/s).
{% endtab %}

{% tab title="Torque" %}
***Torque*** is roughly the measure of the turning force on an object like a gear or a wheel. Mathematically, **torque** is defined as the rate of change of the angular momentum of an object. This can also be stated as a force that acts normal (at 90 degrees) to a radial lever arm which causes the object to rotate. A common example of torque is the use of a wrench in order to tighten or loosen a bolt. In that example, using a longer wrench can produce more **torque** on the bolt than using a shorter wrench. **Torque** is commonly expressed in N⋅m or in⋅lbs.

When **torque** is turning an object like a spur gear, the gear will create a straight line (linear) force at the point where the teeth contact the other gear. The magnitude of the **torque** created is the product of the rotational force applied and the length of the lever arm ,which in the case of a gear, is half of the pitch diameter (the radius).

![](/files/-M9UzF3F-Eol6F880wQ6)

{% endtab %}

{% tab title="Power" %}
***Power (P)*** is the rate of work over time. The concept of **power** includes both a physical change and a time period in which the change occurs. This is different from the concept of work which only measures a physical change. The difference in these two concepts is that it takes the same amount of work to carry a brick up a mountain whether you walk or run, but running takes more **power** because the work is done in a shorter amount of time. The SI unit for **power** is the Watt (W) which is equivalent to one joule per second (J/s).

In competitive robotics, the total amount of available power is determined by the motors and batteries allowed to be used. The maximum speed at which an arm can lift a certain load is dictated by the maximum system **power**.

![](/files/-M9UzF3Gdxl1mD4Ln3l_)

{% endtab %}
{% endtabs %}

## Gear Train

Meshing two or more gears together is known as a **gear train**. Selecting the gears in the gear train as larger or smaller relative to the input gear can either increase the output speed or increase the output torque, but the total power is not affected.

### Gear Ratio&#x20;

When a larger gear drives a smaller one, for one rotation of the larger gear the small gear must complete more revolutions - so the output will be faster than the input. If the situation is reversed, and aa smaller gear drives a larger output gear, then for one rotation of the input the output will complete less than one revolution – so the output will be slower than the input. The **ratio** of the sizes of the two gears is proportional to the speed and torque changes between them.

![](/files/-M9UzF3HmI-qLC_QjeRt)

The **ratio** in size from the input (driving) gear to the output (driven) gear determines if the output is faster (less torque) or has more torque (slower). To calculate exactly how the **gear ratio** effects the relationship from input to output, find the ratio for the number of teeth between the two gears. In the image below, the ratio of the number of teeth from the input gear to the output gear is 72T:15T which means the input needs to turn 4.8 rotations for the output to complete one rotation.

![](/files/-M9UzF3IUfdh1DwB4qkU)

### Idlers&#x20;

What happens when a 45 tooth **idler** gear is inserted into the gear example? An **idler gear** is any intermediate (between input and output) gear which does not drive any output (work) shaft. Idler gears are used to transmit torque over longer distances than would be practical by using just a single pair of gears. Idler gears are also used to reverse the direction of the rotation of the final gear.

Regardless of the number or size of idler gears in the chain, only the first and last gear determine the reduction. Since idler gears do not change the gear **reduction**, the reduction in the example remains 72:15, but the direction of the output stage is now reversed from the previous example.

![](/files/-M9UzF3JyWpCpxFLipZ5)

Idler gears are a good way to transmit power across distances in your robot. A common example of this is an all gear drivetrain. In this example the gears on the end are linked to the drive wheels and one of the center gears would be driven by a motor (not shown). The orange arrows indicate the relative rotation of each of the gears showing that the two wheels are mechanically linked and will always rotate in the same direction.&#x20;

![](/files/-M9UzF3KsHGFxB45-orY)

Because idler gears reverse the direction of rotation, it is important to pay attention to the number of gears in the drivetrain. In the picture below there is an even number of gears, and because of this the wheels will always spin in the opposite direction.&#x20;

![](/files/-M9UzF3LBmXg8vVT1eVi)

### Compound Gearing&#x20;

Some designs may require more **reduction** than is practical in a single stage.  The ratio from the smallest gear available to the largest in the REV 15mm Build System is 125:15, so if a greater reduction then 8.3 is required, multiple reduction stages can be used in the same mechanism, this is called a **compound gear reduction**.  There are multiple gear pairs in a compound reduction with each pair of gears linked by a shared axle. Below is an example of a two-stage reduction. The driving gear (input) of each pair is highlighted in orange.&#x20;

{% hint style="info" %}
**Reduction** is the concept lowering input speed to reduce overall output speed.&#x20;
{% endhint %}

![](/files/nUBrYyxkm5B2X5qawfwv)

To calculate the total reduction of a compound reduction, identify the reduction of each stage and then multiply each reduction together. &#x20;

$$
\text{CR}=\text{R}\_1×\text{R}\_2 ×\text{…} ×\text{R}\_n
$$

**Where:**

* CR is the total Compound Reduction&#x20;
* Rn is the total reduction of each stage

Using the image above as an example the compound reduction is 12:1.

$$
\text{CR}=\text{R}\_1×   \text{R}\_2 =\frac{60}{30}× \frac{90}{15}=2 ×6=12
$$

For any gear system there are a limited number of gear sizes available, so in addition to being able to create greater reductions using compound reductions it is also possible to create a wider range of reduction values, or the same reduction of a single stage, but with smaller diameter gears.

## Spacing and Center to Center Distance&#x20;

When [REV Robotics Gears](https://www.revrobotics.com/duo/motion/gears-chain-belts/) are used in conjunction with the [slots](/duo-build/structure/intro/15mm-extrusion.md) on [Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/) or [Channel](https://www.revrobotics.com/competition/ftc/structure/channel/), the **center to center distance** between axles is completely adjustable. Slide and re-tighten the shaft mounting plates anywhere along the slots to mesh gears together. This system allows any combination of compatible REV Robotics Gears to be used together, allowing for a high level of flexibility. When adjusting the reduction of a system, just a single gear can be replaced, reducing the amount of reassembly time.

{% hint style="danger" %}
Any combination of gear sizes can be used together. However, REV Plastic Gears and Metal Gears should NOT be used in conjunction with each other.&#x20;
{% endhint %}

When using the pitch featured on the [Extended Motion Pattern](/duo-build/structure/intro.md#extended-motion-pattern) there will not be the same level of flexibility for gear spacing. Flexibility can be maintained by using a combination of the slots and the pattern, which allows more gear options. If just the pattern is being used then center to center distance calculations will be more prevalent.&#x20;

### Spacing&#x20;

In order for gears to work effectively, and not become damaged, it’s important that the **center-to-center distance** is correctly adjusted. The gears in DETAIL A ,of the figure below, may work under very light load, but they will certainly not work and will skip under any significant loading. The gears in that example are too far apart and so the teeth of each gear barely contact each other. The gears in DETAIL B are correctly spaced and will provide smooth and reliable operation.

![](/files/-M9UzF3Ocby0zcpWrm2E)

**To correctly space REV Robotics Gears along slots, use the following procedure:**

1. Securely fix the axle of either the input or output gear. In the case of a gear train with multiple idlers or a compound reduction, consider which axle makes the most sense to fix, such as the very first input gear or the very last gear.
2. Starting with the fixed axle, identify all the driving and driven gears for any gears on that axle. One by one, loosen these axles and slide them until the teeth of both gears are fully engaged and parallel. Re-tighten the axle mounts.
3. Continue the procedure from Step 2 for each fixed axle until all the gears are tightly meshed and all the axles have been re-tightened.

{% hint style="warning" %}
When using a gear train in conjunction with the Extended Motion Pattern, only certain combinations of gears will work.&#x20;
{% endhint %}

### Center to Center Distance

{% hint style="info" %}
*To learn more about pitch diameter return to the top level* [*Gear page*](/duo-build/motion/gears.md#gear-basics)*.*
{% endhint %}

The gear spacing adjustment procedure above is sufficient in cases where the slot system is being used. To mathematically calculate the correct center to center distance use the [Gear Measurements](/duo-build/motion/gears.md#gear-measurements) section to determine the pitch diameter (PD) of both gears.

$$
\text{CCD} = \frac{\text{PD}\_1}{2}+ \frac{\text{PD}\_2}{2}
$$

**Where:**

* CCD is the Center to Center Distance&#x20;
* PD1 is the pitch diameter for gear one&#x20;
* PD2 is the pitch diameter for gear two&#x20;

Using the example in the figure with the 60 tooth and 72 tooth gears, the correct center to center distance calculation for a 72T:60T gear ratio is 49.5 mm.

$$
72!:!60 \~\text{CCD} = \frac{45mm}{2} +\frac{54mm}{2}= 49.5mm
$$

### Gear Measurements

#### Plastic Gear Measurements

|                                                                                                | Outside Diameter A            | Pitch Diameter B               |
| ---------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------ |
| <p>15 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1331/">REV-41-1331</a></p>  | <p>0.5 in</p><p>12.7 mm</p>   | <p>0.44 in </p><p>11.25 mm</p> |
| <p>30 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1332/">REV-41-1332</a></p>  | <p>0.95 in </p><p>24.0 mm</p> | <p>0.89 in</p><p>22.5 mm</p>   |
| <p>45 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1335/">REV-41-1334</a></p>  | <p>1.39 in</p><p>35.3 mm</p>  | <p>1.33 in</p><p>33.75 mm</p>  |
| <p>60 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1335/">REV-41-1335</a></p>  | <p>1.83 in</p><p>46.5 mm</p>  | <p>1.77 in</p><p>45.0 mm</p>   |
| <p>72 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1336/">REV-41-1336</a></p>  | <p>2.19 in</p><p>55.5 mm</p>  | <p>2.13 in</p><p>54 mm</p>     |
| <p>90 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1337/">REV-41-1337</a></p>  | <p>2.72 in</p><p>69.0 mm</p>  | <p>2.66 in </p><p>67.5 mm</p>  |
| <p>125 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1333/">REV-41-1333</a></p> | <p>3.75 in </p><p>93.5 mm</p> | <p>3.69 in </p><p>93.75 mm</p> |

The **Motion Interface Pattern** is a circular M3 hole pattern on a 16mm diameter that interfaces with certain REV Brackets and the UltraPlanetary 5mm Hex Output ([REV-41-1615](https://www.revrobotics.com/rev-41-1615/)).

![](/files/lJXIqpQZdt3s1cMw0Cq7)

The 15 tooth and 30 tooth plastic gears do not have a motion pattern due to size constraints. However, they share the same 0.75 module as the other acetal gears. The table below provides the outer diameter and pitch diameter of these gears.&#x20;

|                                                                                               | Outside Diameter A            | Pitch Diameter B             |
| --------------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------- |
| <p>15 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1331/">REV-41-1331</a></p> | <p>0.5 in</p><p>12.7 mm</p>   | <p>0.35 in</p><p>9 mm</p>    |
| <p>30 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1332/">REV-41-1332</a></p> | <p>0.95 in </p><p>24.0 mm</p> | <p>0.89 in</p><p>22.5 mm</p> |

#### &#x20;Metal Gear Measurements

|                                                                                               | Outside Diameter A            | Pitch Diameter B             |
| --------------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------- |
| <p>42 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1664/">REV-41-1664</a></p> | <p>1.39 in</p><p>35.2 mm</p>  | <p>1.32 in</p><p>33.6 mm</p> |
| <p>56 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1663/">REV-41-1663</a></p> | <p>1.83 in </p><p>46.4 mm</p> | <p>1.73 in</p><p>44.0 mm</p> |
| <p>70 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1662/">REV-41-1662</a></p> | <p>2.27 in</p><p>57.6 mm</p>  | <p>2.20 in</p><p>56.0 mm</p> |
| <p>86 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1661/">REV-41-1661</a></p> | <p>2.77 in</p><p>70.3 mm</p>  | <p>2.71 in</p><p>68.8 mm</p> |

The **Motion Interface Pattern** is a circular M3 hole pattern on a 16mm diameter that interfaces with certain REV Brackets and the UltraPlanetary 5mm Hex Output ([REV-41-1604](https://www.revrobotics.com/rev-41-1604/)).

![](/files/tY3chYLUH8NRqM1MqrlB)

The 12 Tooth and 28  Tooth Metal Gears do not have a motion pattern due to size constraints. They are also made from sintered steel rather than aluminum. However, they share the same 0.8 module as the other metal gears. The table below provides the outer diameter and pitch diameter of these gears.&#x20;

|                                                                                               | Outside Diameter A           | Pitch Diameter B            |
| --------------------------------------------------------------------------------------------- | ---------------------------- | --------------------------- |
| <p>12 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1666/">REV-41-1666</a></p> | <p>0.44 in</p><p>11.2 mm</p> | <p>0.38 in</p><p>9.6 mm</p> |
| <p>28 Tooth Gear</p><p><a href="https://www.revrobotics.com/rev-41-1665/">REV-41-1665</a></p> | <p>0.95 in</p><p>24.0 mm</p> | <p>0.88 in</p><p>35.2 m</p> |

{% hint style="info" %}
The 12 Tooth Pinion Gear ([REV-41-1660](https://www.revrobotics.com/rev-41-1660/)) while sharing the 0.8 module differs from the other metal gears significantly. See the [drawing](https://www.revrobotics.com/content/docs/REV-41-1660-DR.pdf) for relevant information for the 12 Tooth Pinion Gear.
{% endhint %}
