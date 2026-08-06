> Source: https://docs.revrobotics.com/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md).

# Advanced Sprockets and Chain

## Sprocket and Chain Physics&#x20;

Sprockets are one common way to transmit power and change the output torque or speed of a mechanical system. Understanding these basic concepts is required to make optimized design decisions. This section will briefly cover the definition of these concepts and then explain them in relationship to basic [sprocket and chain](https://www.revrobotics.com/ftc/motion/gears-sprockets-chain/) designs.

{% tabs %}
{% tab title="Speed" %}
***Speed*** is the measure of how fast an object is moving. The speed of an object is how far it will travel in a given amount of time. The SI unit for speed is meters per second but speed is also commonly expressed in feet per second.
{% endtab %}

{% tab title="Torque " %}
***Torque*** is roughly the measure of the turning force on an object like a sprocket or a wheel. Mathematically, torque is defined as the rate of change of the angular momentum of an object. A common example of torque is a wrench attached to a bolt produces a torque to tighten or loosen it. Torque is commonly expressed in N⋅m or in⋅lbs.

When torque is turning an object, like a sprocket, the sprocket will create a straight line (linear) force at the point where the teeth contact the chain. The magnitude of the torque created is the product of the rotational force applied and the length of the lever arm, which in the case of a sprocket, is half of the pitch diameter (the radius).

![](/files/-M9ZHmV80zbgk_SSkFEy)

{% endtab %}

{% tab title="Power" %}
***Power (P)*** is the rate of work over time. The concept of power includes both a physical change and a time period which the change occurs. This is distinct from the concept of work which only measures a physical change. It takes the same amount of work to carry a brick up a mountain whether you walk or run, but running takes more power because the work is done in a shorter amount of time. The SI unit for power is the watt(W) which is the same as one joule per second (J/s).

Often in competition robotics the total power is fixed by the motors and the batteries available. The maximum speed at which an arm can lift a certain load is dictated by the maximum system power.

![](/files/-M9ZHmV9OsxxeJtF-rKb)
{% endtab %}
{% endtabs %}

## Chain Drive&#x20;

By selecting sprockets with different sizes relative to the input sprocket varies the output speed and the output torque.  Total power is not effected through these changes.

Sprocket and chain is a very efficient way to transmit torque over long distances. Modest **reductions** can be accomplished using sprockets and chain, but gears typically provide a more space efficient solution for higher ratio reductions.&#x20;

### Sprocket Ratio&#x20;

When a larger sprocket drives a smaller one, for one rotation of the larger sprocket the smaller sprocket must complete more revolutions so the output will be faster than the input. If the situation is reversed and a smaller sprocket drives a larger output sprocket, then for one rotation of the input the output will complete less than one revolution resulting in a speed decrease from the input. The **ratio** of the sizes of the two sprockets is proportional to the speed and torque changes between them.

![](/files/-M9e6hv0hdA97FKNN2E1)

The **ratio** in size from the input (driving) sprocket to the output (driven) sprocket determines if the output is faster (less torque) or has more torque (slower). To calculate exactly how the sprocket size ratio effects the relationship from input to output use the ratio of the number of teeth between the two sprockets.

In the image below, the ratio of the number of teeth from the input sprocket to the output sprocket is 20T:15T which means the input needs to turn 1.3 rotations for the output to complete one rotation $$20T/15T =1.3$$. &#x20;

![](/files/-MlBeMBUjifHD3LVtn9z)

### Idlers&#x20;

Now lets add a 15 tooth **idler** sprocket into the example on the outside of the chain loop. An **idler** sprocket is any sprocket meshed with the chain which does not drive any shaft or do any work.  **Idlers** do not change the system reduction which remains 20T:15T.&#x20;

{% hint style="warning" %}
Regardless of the number or size of idler sprockets, only the input and output sprocket determine the reduction. &#x20;
{% endhint %}

![](/files/-MlCPp_UtOIbUOYtCdRP)

All sprockets on the same side of a chain have the same rotation. The driving and driven sprocket are inside the chain and are rotating counter clockwise while the idler sprocket is outside of the chain loop and is rotating clockwise.  This property is useful sometime when it is desirable to have two shafts powered from the same source, but with opposite rotations.  Common examples of this on robots are intakes and dual wheeled shooters.&#x20;

Idlers can be used to tension chain or increase the amount of chain wrap around a sprocket.  From the figure below, all power transmission sprockets should have chain wrapped approximately 180° around the circumference of the sprocket.  This amount of wrap is necessary so that there are sufficient teeth engaged with the chain to transmit the torque.  Too little wrap (<120°) and the chain will skip under heavy load, while excessive wrap (>200°) can decrease system efficiency. The sprocket outside of the chain is noted with a warning because it has a chain wrap of <90°.  If this sprocket is an idler, then it is unpowered and minimal chain wrap is acceptable, however if this sprocket will be driving a shaft which is doing work, this amount of wrap would be insufficient. &#x20;

![](/files/-MlBf0rOcHj4jUHrcQB5)

Sprocket and chain is an efficient way to transmit torque long distances in a robot. A common example of this is a sprocket and chain drivetrain. In this example the sprockets on the ends are linked to the drive wheels and the center sprocket would be driven by a motor (not shown). Because the driving and driven sprockets are all inside the chain, they all have the same rotation direction. The smaller sprockets on the outside of the chain loop are used to increase the amount of chain wrap on the center driving sprocket.

![](/files/-M9ZHmVEbTScXZQkgyNa)

### Compound Gearing

Some designs may require more reduction than is practical in a single stage. The ratio from the smallest sprocket available to the largest is 54:15, so if a greater reduction then 3.6x is required, multiple reduction stages can be used in the same mechanism which is called a compound gear reduction. There are multiple gear or sprocket pairs in a compound reduction with each pair linked by a shared axle. When using sprockets and chain in a multi stage reduction, it’s very common to use gears for the first stage and then use sprockets and chain for the last stage. The figure below is an example of a two-stage reduction using all gears, but one of the pairs could be replaced with sprockets and chain. The driving gear (input) of each pair is highlighted in orange.

![](/files/-M9ZHmVFLUMo9On7Vbus)

Reduction is calculated the same for gears and sprockets based on the ratio of the number of teeth. To calculate the total reduction of a compound reduction, identify the reduction of each stage and then multiply each reduction together.

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

For any gear system there are a limited number of gear and sprocket sizes available so in addition to being able to create greater reductions using compound reductions it is also possible to create a wider range of reduction values or the same reduction of a single stage, but with smaller diameter motion components.

{% hint style="info" %}
Each additional compound stage will result in a decrease in efficiency of the system.&#x20;
{% endhint %}

## Spacing and Center to Center Distances

When REV Robotics Sprockets are used in conjunction with the [slots](/duo-build/structure/intro/15mm-extrusion.md) on [Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/) or [Channel](https://www.revrobotics.com/competition/ftc/structure/channel/), the **center to center distance** between axles is completely adjustable. Slide and retighten the shaft mounting plates anywhere along the slots to adjust chain tension. This system allows any combination of compatible REV Robotics Sprocket to be used together, allowing for a high level of flexibility. When adjusting the reduction of a system, just a single sprocket can be replaced reducing the amount of reassembly time.

When using the pitch featured on the [Extended Motion Pattern](/duo-build/structure/intro.md#extended-motion-pattern) a similar level of flexibility can be achieved in sprocket spacing by using Tensioning Bushings ([REV-41-1702](https://www.revrobotics.com/rev-41-1702/)) with M3 Standoffs ([REV-41-1492](https://www.revrobotics.com/rev-41-1492/)).&#x20;

### Spacing&#x20;

In order for sprockets to work effectively, it’s important that the **center-to-center distance** is correctly adjusted. The sprocket and chain example with the red 'X;, in the image below, may work under very light loads, but they will certainly not work and will skip under any significant loading. The sprockets in this example are too close together so chain is loose enough that it can skip on the sprocket teeth. The sprockets, with the green check mark, are correctly spaced which will provide smooth reliable operation.

![](/files/-M9e6pADnUy4uJezA5i2)

**To correctly space REV Robotics Sprockets along slots, use the following procedure:**

1. Securely fix the axle of either the input or output sprocket. In the case of a gear train with multiple idlers or a compound reduction, consider which axle makes the most sense to fix such as the very first input gear or the very last gear.
2. Starting with the fixed axle, then identify all the driving and driven sprockets for any sprockets on that axle. One by one loosen these axles, slide them until the chain is tensioned and then retighten the axle mounts.
3. Continue the procedure from Step 2 for each fixed axle until all the chains are tight and all the axles have been retightened.

{% hint style="warning" %}
The process highlighted above works with the slots but the process with the Extended Motion Pattern may require center to center distance calculations.
{% endhint %}

### Center to Center Distance

It is possible to mathematically calculate the number of links needed between two sprockets or the correct center to center distances for two sprockets for a given chain length. These methods are appropriate for robot planning purposes, but assembling your robot using these measurement is typically impractical. The details of these calculations are included for completeness, but most modern CAD packages or numerous free online calculators can also generate the correct values.

#### Center to center distance in inches&#x20;

$$
\text{CDC} = \frac{P}{8}\left\[2L - (N+n) + \sqrt{(2L-(N+n))^2-\frac{8}{\pi^2}\times(N - n)^2} \right]
$$

#### Chain length in pitches&#x20;

$$
L = \frac{2C}{P} + \frac{N+n}{2} + \frac{P(\frac{N -n}{2\pi})^2}{C}
$$

**Where:**

* C= Center to Center Distance
* L= Chain Length in Pitches
* P= Pitch of Chain&#x20;
* N= Number of Teeth on Large Sprocket&#x20;
* n= Number of Teeth on Small Sprocket

#### Calculate center to center distance&#x20;

![](/files/-M9eBod8srE8BGJvT3Zz)

Calculate center to center distance using the '[center to center distance in inches'](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#center-to-center-distance-in-inches) formula and the chain drive example in the above image.&#x20;

**Where:**

* L = 48&#x20;
* P = 0.25
* N = 20&#x20;
* n = 15

$$
\text{CDC} = \frac{0.25}{8}\left\[2(48) - (20+15) + \sqrt{(2(48)-(20+15))^2-\frac{8}{\pi^2}\times(20 - 15)^2} \right]\newline= \frac{0.25}{8}\left\[ 96 - 35 +\sqrt{(96-35)^2 - \frac{8}{\pi^2} \times (5)^2} \right]\newline=\frac{0.25}{8} \left\[ 61 + \sqrt{(61)^2 - \frac{8}{\pi^2}\times25}\right]\newline = \frac{0.25}{8}\left\[ 61 + \sqrt{3721 - \frac{200}{\pi^2}}\right]\newline\frac{0.25}{8}\left\[61+\sqrt{3721-20.24642}\right]\newline = 0.03125\left\[61+60.833\right]\newline = 3.807
$$

After running calculations, the center to center distance for the example is **3.807 inches**

#### Calculate chain length

In most design cases the chain length is not known ahead of time, but the two sprockets in the reduction and an approximate center-to-center distance to fit the reduction is known. For this example, a 20:15 reduction is needed, and the whole solution must fit in a space of five inches or less.

In this example the whole solutions must fit into a five-inch space, so in addition to the center to center distance, the chain clearance radius for both sprockets must be accounted for. Use [Sprocket Measurement Details](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#sprocket-measurements) to look up the chain clearance diameter (A) for both the 15 tooth and 20 tooth sprocket and subtract the radius of each from the total given solution size to get the maximum center to center distance available.

![](/files/-M9ZHmVJ-5VEvhikU9Bh)

$$
\text{Maximum CDC} = \text{Total Solution Width} - \text{Clearance Radius 1}-\text{Clearance Radius 2}
$$

**Where:**

$$
\text{Total Solution Width} = 5  \text {inches}\newline\text{Clearance Radius 1},=15T\_{chain, clearance, diameter(A)} = 1.45,\text{inches}\newline\text{Clearance Radius 2} =20T\_{chain, clearance, diameter(A)} = 1.85,\text{inches}
$$

$$
\text{Maximum CDC Available} = 5 - \frac{1.45}{2} - \frac{1.85}{2}\newline\text{Maximum CDC Available} = 3.35 \text{inches}
$$

&#x20;Using the center to center distance of 3.371 inches as the maximum spacing for this reduction to fit into a five-inch space, solve the [chain length in pitches equation](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#chain-length-in-pitches).

**Where:**

* C= 3.35
* P= 0.25
* N= 20
* n= 15

$$
L =\left\[ \frac{2(3.35)}{0.25} \right]+\left\[ \frac{20+15}{2}\right] + \left\[\frac{0.25(\frac{20 -15}{2\pi})^2}{3.35}\right]\L = \left\[\frac{6.7}{0.25}\right] +\left\[\frac{35}{2}\right]+ \left\[\frac{0.25(\frac{5}{2\pi})^2}{3.35}\right]\L = 26.8 + 17.5 + \left\[\frac{0.25(0.796)^2}{3.35}\right]\newline L = 44.3 + \left\[\frac{0.25\times 0.634}{3.35} \right]\L = 44.3 + \frac{0.1585}{3.35}\ L = 44.347
$$

Since it is **not possible to have a fraction of a pitch length in the chain, the number obtained by solving the formula must be rounded to a whole even number**. In this example because the center to center distance used was the maximum allowed, the exact pitch length should be rounded down to 44 to meet the design requirements.

Now that the maximum even pitch lengths in the chain has been calculated, this value can be plugged back into [center to center distance formula ](/duo-build/motion/sprockets-and-chain/sprockets-and-chain-advanced.md#center-to-center-distance)to find the exact center to center distance using a 44 link chain:

**Where:**&#x20;

* L = 44&#x20;
* P = 0.25
* N = 20&#x20;
* n = 15&#x20;

$$
\text{CDC} = \frac{0.25}{8}\left\[2(44) - (20+15) + \sqrt{(2(44)-(20+15))^2-\frac{8}{\pi^2}\times(20 - 15)^2} \right]\\\text{CDC} = \frac{0.25}{8}\left\[88- 35 + \sqrt{(88-35)^2-\frac{8}{\pi^2}\times25} \right]\\\text{CDC} = \frac{0.25}{8}\left\[53 + \sqrt{(53)^2-\frac{200}{\pi^2}} \right]\\\\\text{CDC} = \frac{0.25}{8}\left\[53 + \sqrt{2809-20.24642} \right]\\\text{CDC} = 0.03125\left\[53 + 52.809\right]\\\text{CDC} = 3.307 \text{inches}
$$

For a 15T:20T reduction the longest chain which will fit in under 5-inches using a 44 link chain which gives a center-to-center distance is 3.307 inches and the total solution width of 4.957 inches.

### Sprocket Measurements

#### Plastic Sprockets

| ​                                                                                                   | Chain Clearance Diameter A    | Pitch Diameter B             |
| --------------------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------- |
| <p>15 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1339/">REV-41-1339</a>​</p> | <p>1.45 in</p><p>36.9 mm</p>  | <p>1.2 in</p><p>30.5 mm</p>  |
| <p>20 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1340/">REV-41-1340</a>​</p> | <p>1.85 in</p><p>46.9 mm</p>  | <p>1.6 in</p><p>40.6 mm</p>  |
| <p>26 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1342/">REV-41-1342</a>​</p> | <p>2.32 in</p><p>59.0 mm</p>  | <p>2.07 in</p><p>52.7 mm</p> |
| <p>40 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1343/">REV-41-1343</a>​</p> | <p>3.43 in</p><p>87.3 mm</p>  | <p>3.19 in</p><p>80.9 mm</p> |
| <p>54 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1341/">REV-41-1341</a>​</p> | <p>4.55 in</p><p>115.6 mm</p> | <p>4.3 in</p><p>109.2 mm</p> |

The **Motion Interface Pattern** is a circular M3 hole pattern on a 16mm diameter that interfaces with certain REV Brackets and the UltraPlanetary 5mm Hex Output ([REV-41-1615](https://www.revrobotics.com/rev-41-1615/)).

![](/files/JhLJaYCTjheW5lR6KFkr)

The 10 tooth #25 sprocket does not have a motion pattern due to size constraints. However, the 10 Tooth Sprocket shares features of the other Plastic Sprockets, like compatibility with #25 Chain. The table below provides the outer diameter and pitch diameter of the 10 Tooth Sprocket.&#x20;

|                                                                                                     | Chain Clearance Diameter A   | Pitch Diameter B             |
| --------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------- |
| <p>10 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1338/">REV-41-1338</a>​</p> | <p>0.95 in</p><p>24.1 mm</p> | <p>0.80 in</p><p>20.2 mm</p> |

#### Metal Sprockets&#x20;

|                                                                                                     | Chain Clearance Diameter A   | Pitch Diameter B             |
| --------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------- |
| <p>15 Tooth Sprocket</p><p><a href="https://www.revrobotics.com/rev-41-1717/">REV-41-1717</a></p>   | <p>1.45 in</p><p>36.9 mm</p> | <p>1.2 in</p><p>30.5 mm</p>  |
| <p>20 Tooth Sprocket</p><p><a href="https://www.revrobotics.com/rev-41-1720/">REV-41-1720</a></p>   | <p>1.85 in</p><p>46.9 mm</p> | <p>1.6 in</p><p>40.6 mm</p>  |
| <p>26 Tooth Sprocket</p><p>​<a href="https://www.revrobotics.com/rev-41-1342/">REV-41-1342</a>​</p> | <p>2.32 in</p><p>59.0 mm</p> | <p>2.07 in</p><p>52.7 mm</p> |
| <p>32 Tooth Sprocket</p><p><a href="https://www.revrobotics.com/rev-41-1722/">REV-41-1722</a></p>   | <p>2.80 in <br>87.3 mm</p>   | <p>2.55 in</p><p>64.8 mm</p> |
| <p>40 Tooth Sprocket</p><p><a href="https://www.revrobotics.com/rev-41-1723/">REV-41-1723</a></p>   | <p>3.43 in</p><p>87.3 mm</p> | <p>3.19 in</p><p>80.9 mm</p> |

![](/files/dJqkOy8Q9oTK5OqtM5hD)

{% hint style="info" %}
The 10 Tooth Metal #25 Sprocket ([REV-41-1716](https://www.revrobotics.com/rev-41-1716/)) while still being #25 Chain compatible differs from the other metal sprockets significantly. See the [drawing ](https://www.revrobotics.com/content/docs/REV-41-1716-DR.pdf)for relevant information for the 10 Tooth Metal #25 Sprocket.&#x20;
{% endhint %}
