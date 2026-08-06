> Source: https://docs.revrobotics.com/duo-build/motion/intro/shaft.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/intro/shaft.md).

# Hex Shaft and Spacers

## 5mm Hex Shaft

The REV DUO Build System is built around a [5mm hex shaft](https://www.revrobotics.com/ftc/motion/bearings-linear-slides-pillow-blocks/). Using a hex shaft to transmit torque in the system removes the need for set screws, which can loosen over time and can damage shafts so that they become unusable. REV Robotics Hex Shafts are precision ground 5mm stainless steel and fit [snugly](/duo-build/building/tips-and-tricks.md#snug-not-stuck) in all other REV hex drive components.

![](/files/ZBdbA6M7fKJYT1bd63b5)

### Product Specs&#x20;

* Material: Stainless steel (SUS303)
* OD: 5mm hex
* Length: Four Lengths, can be cut if needed&#x20;

| Length | Product Code                                            |
| ------ | ------------------------------------------------------- |
| 75mm   | [REV-41-1347](https://www.revrobotics.com/rev-41-1347/) |
| 90mm   | [REV-41-1348](https://www.revrobotics.com/rev-41-1348/) |
| 135mm  | [REV-41-1349](https://www.revrobotics.com/rev-41-1349/) |
| 400mm  | [REV-41-1362](https://www.revrobotics.com/rev-41-1362/) |

### When to Use?

Use the 5mm Hex Shaft in areas where you have moving parts or need to transmit torque.&#x20;

For high load applications it is recommended to use the REV precision shaft, stack multiple gears or sprockets in parallel, or use the High Strength Hex Hub Adapter ([REV-41-1147](https://www.revrobotics.com/rev-41-1147/)) to increase strength.

{% hint style="info" %}
*If you are looking to switch to Hex Shafts from another shaft system check out the* [*Compatibility*](/duo-build/building/compatibility.md) *page.*&#x20;
{% endhint %}

### How to Use?

{% hint style="info" %}
*For more information on how to properly use the 5mm hex shaft see the* [*Supporting Motion*](/duo-build/building/supporting-motion.md) *page*&#x20;
{% endhint %}

## Shaft Collars

![](/files/nVfvL7hSjum6g8a6KzTw)

A shaft collar is a hollow cylinder with one or more set screws which tighten towards its center and an inner dimension (ID) that is just slightly larger than the shaft it is being used on. Most standard 6mm ID shaft collars can be used on the REV Robotics 5mm hex shaft, but the REV Robotics Shaft Collar ([REV-41-1327](https://www.revrobotics.com/rev-41-1327/))  is customized with a M3 thread so a standard hex cap bolt can be used instead of the supplied set screw.

### When to Use?

Shaft collars are used to prevent lateral (sideways/sliding) movement of a shaft, or an item on the shaft. Since shaft collars are used to prevent lateral shaft movement they are often used in place of shaft spacers.

### How to Use?

![](/files/wozb9nlt4B4R8OSaWxas)

To use the shaft collar, slide it onto the hex shaft and rotate it until a flat side is facing the setscrew. Adjust the collar to the desired location and use a 1.5mm Allen Wrench ([REV-62-1867](https://www.revrobotics.com/rev-62-1867/)) to tighten the included set screw snuggly against the shaft.&#x20;

{% hint style="warning" %}
A small amount of a thread locker product, like Loctite Blue, can be used if desired.&#x20;
{% endhint %}

![](/files/-M7yIIu-w_Q8VU-h9mTZ)

The REV Robotics shaft collar has a 6mm inside diameter and is customized with a M3 thread so a standard hex cap bolt can be used instead of the supplied set screw.

## Spacers&#x20;

![](/files/-M8HZobqWk7JIkgR1rc4)

[Spacers](https://www.revrobotics.com/competition/ftc/hardware-tools/accessories/) for the 15mm building system have a 5mm hex center, are made of Delrin, and come in 3 lengths. Spacers are used between parts on a shaft to take up the extra space and prevent the parts from sliding on the shaft. If more than a few spacers are needed, it is typically better to use a shaft collar.

### When to Use?

Spacers and shaft collars are used for the same purpose: to [constrain](/duo-build/building/constraining-motion.md) components on a shaft. This keeps shafts from falling out and also keeps motion components, such as gears and sprockets, aligned.&#x20;

* **For larger sections of exposed shaft**, shaft collars are preferred because installing multiple spacers is less efficient and is more difficult to manage during robot building and maintenance.&#x20;
* **For shorter shaft lengths**, spacers are generally more efficient.

![](/files/RDah9qTUq69OnWVqzjKm)

## Adapters

### **High Strength Hex Hub**

![](/files/-MlCDePpzH1df8QJTTUx)

These aluminum hubs can be mounted to any of the REV robotics hex driven motion products to increase their maximum torque. When the hex hub adapter is used on a REV product, the raised part of the hub should face away from the gear. There will be a small gap between the back of the hub and the body of the gear because of the built in spacer on the gear. Insert a shaft into both parts and then using M3x20mm and nylocs, evenly tighten the hub against the gear to ensure good alignment.&#x20;

![](/files/-MlCDhV8KeYfLn0ZruIS)

In addition to the increasing the maximum torque of REV products, the High Strength Hex Hub can be used to convert almost any of the Tetrix and AndyMark gears with the 4-hole mounting pattern to accept a 5mm hex drive shaft. Hex hub adapters allow teams to use the parts they already have with the reliability and convenience of a hex drive shaft.&#x20;

{% hint style="info" %}
*For more information on how to use the High Strength Hex Hub with products from other companies see the* [*Compatibility* ](/duo-build/building/compatibility.md)*page.*&#x20;
{% endhint %}

### Locking Motion Hub&#x20;

The Locking Motion Hub ([REV-41-1719](https://www.revrobotics.com/rev-41-1719/)) places a motion pattern on any 5mm hex shaft. Use this to connect metal sprockets to 5mm hex shaft or add strength to any REV product with the Motion Pattern. The Locking Motion Hub has a shaft collar component built-in and does not need an additional shaft collar to constrain the Hex Shaft.&#x20;
