> Source: https://docs.revrobotics.com/duo-build/motion/timing-belts-and-pulleys.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/timing-belts-and-pulleys.md).

# Timing Belts and Pulleys

## Timing Belt and Pulley Basics&#x20;

The Timing Belt and Pulley system is a pulley-based motion transmission system. Timing Belts and Pulleys transmit motion similarly to sprockets and chains. Both the Belt and the Pulley have teeth that interlock and engage with each other to drive motion. &#x20;

Timing Belts and Pulleys are lighter, more compact, and more efficient at transferring motion than chains and sprockets. Belts do not stretch over time as much as chain, making re-tensioning less of an issue. In general, a timing belt and pulley system should last a full season, if properly installed. Follow through the rest of this section to learn more about the proper installation and tensioning of the [REV GT2 3mm Pitch Pulley and Belt system](https://www.revrobotics.com/duo/motion/gears-chain-belts/).&#x20;

### Product Specs:&#x20;

The REV GT2 3mm Pitch Pulleys and the GT2 3mm Pitch Belt come in various sizes to fit your needs.

|               |              |
| ------------- | ------------ |
| **Pitch**     | GT2 3mm      |
| **Material**  | Acetal (POM) |
| **Thickness** | Varies       |

All pulleys, except the 12 Tooth  ([REV-41-1668](https://www.revrobotics.com/rev-41-1668/)), come with two ends and an inset to adjust the width of the pulley as needed to drive multiple belts.&#x20;

![](/files/-M9KTgm-_wjrY9N9AmWr)

## Belt Installation&#x20;

All of the GT2 3mm Pitch Pulleys, with the exception of the 12 Tooth Pulley, have flanges to keep the belt on track. This is because the belts tend to thrust to the side when in motion. It is recommended that at least one pulley in the system have flanges to keep the belt from slipping. In situations where the center distance between shafts is more than 8 times the diameter of the smaller pulley or when the drive is operating on vertical shafts, both pulleys should have flanges on both sides.&#x20;

When choosing what structural aspect to use to support a pulley system, it is important that the support be rigid or capable of withstanding torsion. Any significant flex or give in the supporting structure can cause the center-to-center distance between the pulleys to change. Repercussions of a change in the center distance are slack in the belt and the belt jumping teeth.&#x20;

During the installation process, ensure that supporting shafts are parallel and that pulleys are aligned.&#x20;

Belts require relatively little maintenance if installed correctly, but it's always advised to run the center distance calculation to account for the installation and removal of belts.&#x20;

{% hint style="danger" %}
As a general rule avoid subjecting belts to sharp bends or rough handling.&#x20;
{% endhint %}

## Belt Tension

The Timing Belt should be snug when installed to ensure a longer life and less wear on the mechanism. A taut belt is not going to have the same lifespan as a snug belt, and a loose belt may jump teeth in situations where torque is high.&#x20;

When working with the REV GT2 3mm Pitch Pulleys and Belts there will be some difference in pitch between the [Extended Motion Pattern](/duo-build/structure/intro.md#extended-motion-pattern), featured on the [Channels](https://www.revrobotics.com/competition/ftc/structure/channel/), and the pitch of the Timing Belts. Because of the mismatched pitches, there may be limitations to getting the perfect center-to-center distance. One solution to accommodate this issue is to use a combination of M3 Standoffs ([REV-41-1492](https://www.revrobotics.com/rev-41-1492/)) and Tensioning Bushings ([REV-41-1702](https://www.revrobotics.com/rev-41-1702/)) to help tension the belt appropriately.&#x20;

{% hint style="danger" %}
Do not force the belt over the flange of the pulley!
{% endhint %}

## Calculating Belt Size

Determining the size of  belt you need is dependent on a several factors of your mechanism. Below is the formula you will need for a 1:1 belt and pulley configuration. Here are the values you will need to find and how they work in your calculations.&#x20;

{% hint style="info" %}
The below formulas assume 1:1 ratio, different reductions will change these numbers. We recommend using a Chain/Belt C-C Distance Calculator such as the [AMB Robotics Calculator](https://ambcalc.com/chain_belt?=) to find the numbers for your application

\
Special thanks to Ari Meles-Braverman for creating and maintaining the AMB Robotics Calculator!
{% endhint %}

#### RT25 Belt

* 0.0393 - This is the conversion of Centimeters to Inches so the formula can calculate tooth count in 1/4in increments.
* C2C - Center to center distance, the DUO System is on a 8mm Pitch so this value should be in mm for accurate calculations.&#x20;
* 8 - This is the number of teeth in one inch of RT25 Belt multiplied by 2 for the top and bottom run of the belt.&#x20;
* P - This is the number of teeth in one pulley, this is to account for the teeth the belt loops around on both ends of your mechanism. Since the belt loops around half of one pulley and half of the other we can just count it as 1 whole instead of two half.&#x20;
* BL = This is is your exact amount of teeth your belt will need for you mechanism, however since DUO is on a 8mm pitch and RT25 is in 1/4in pitch you will need to round your answer up to the next reasonable belt size and use tensioners for the additional length.&#x20;

$$
(0.0393\*C2C)\*8+P=BL
$$

#### GT2 3mm Belt

* C2C - Center to center distance, the DUO System is on a 8mm Pitch so this value should be in mm for accurate calculations.&#x20;
* 2/3 - This is the number of teeth in one millimeter of GT2 Belt multiplied by 2 for the top and bottom run of the belt.&#x20;
* P - This is the number of teeth in one pulley, this is to account for the teeth the belt loops around on both ends of your mechanism. Since the belt loops around half of one pulley and half of the other we can just count it as 1 whole instead of two half.&#x20;
* BL = This is is your exact amount of teeth your belt will need for you mechanism, however since DUO build system is on a 8mm pitch and GT2 is in 3mm pitch you will need to round your answer up to the next reasonable belt size and use tensioners for the excess length.&#x20;

$$
(C2C\*2/3)+P=BL
$$

## Calculating Center to Center Distance

Sometimes you will have the belt and pulleys you want to use, but not the ideal center to center distance. Use the below formula to find that ideal distance for your mechanism.&#x20;

#### RT25 Belt

* T - This is the number of teeth in the belt.
* P - This is the number of teeth in one pulley, this is to account for the teeth the belt loops around on both ends of your mechanism. Since the belt loops around half of one pulley and half of the other we can just count it as 1 whole instead of two half.
* 3.175 - This is a conversion of half a tooth pitch to millimeters. In a RT25 belt, there is a tooth every 6.35 mm and there is a belt on top and below the pulley, so the number is divided in half to be 3.175 mm so that two teeth are added per 3.175 mm spacing.
* C2C - This is your exact center to center distance. You may need to use a smaller C2C to stay on pitch with the DUO build system, if so remember to use tensioners for the excess length.&#x20;

$$
(T - P) \* 3.175 = C2C
$$

#### GT2 3mm Belt

* T - This is the number of teeth in the belt.
* P - This is the number of teeth in one pulley, this is to account for the teeth the belt loops around on both ends of your mechanism. Since the belt loops around half of one pulley and half of the other we can just count it as 1 whole instead of two half.
* 1.5 - This is a conversion of half a tooth pitch to millimeters. In a GT2 3mm belt, there is a tooth every 3 mm and there is a belt on top and below the pulley, so the number is divided in half to be 1.5 mm so that two teeth are added per 1.5 mm spacing.
* C2C - This is your exact center to center distance. You may need to use a smaller C2C to stay on pitch with the DUO build system, if so remember to use tensioners for the excess length.&#x20;

$$
(T - P) \* 1.5 = C2C
$$
