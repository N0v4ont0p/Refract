> Source: https://docs.revrobotics.com/duo-build/motion/intro.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/intro.md).

# Introduction to Motion

**Transmitting Motion** is the act of getting motion from one part of the robot to another using shafts, sprockets, gears, etc.&#x20;

**Transforming Motion** is the act of changing the turning force (torque) and speed. Torque and speed are inverse to each other, meaning when one increases the other decreases.&#x20;

![](/files/-M8M70BxFPkIW1BBwerA)

The core to transmitting motion in the REV DUO Build System is the 5mm hex (hexagonal, six sided) shape. This hex shape is incorporated into the other main motion components, such as: sprockets, gears, wheels, and shafts. [Shafts](https://www.revrobotics.com/ftc/motion/bearings-linear-slides-pillow-blocks/) are available in a number of different lengths up to 400mm, and can be cut to length if needed.&#x20;

The two primary systems used to transmit motion in the FTC Starter Kit V3.1 ([REV-45-3529](https://www.revrobotics.com/rev-45-3529/)) and [FIRST Global Kit](https://www.revrobotics.com/first-global/) are **sprockets** and **gears.**&#x20;

![](/files/-M8M7Nnyzrz2NVwY8qr6)

| [Sprockets and Chain](/duo-build/motion/sprockets-and-chain.md) |       [Gears](/duo-build/motion/gears.md)      |
| :-------------------------------------------------------------: | :--------------------------------------------: |
|        Better for transmitting motion over long distances       |   Can be used for changing rotation direction  |
|    Changing sprocket sizes requires changing the chain length   |                  More compact                  |
|         Chain is more forgiving in construction accuracy        | More flexibility in adjusting speed and torque |
|               Chain tension and wrap are important              |            Gear spacing is important           |

## Motion Component Features

Most REV DUO motion parts, mainly plastic sprockets and gears, all have a uniform thickness of 15mm. This helps to improve the iterative design experience. Changing from a gear reduction to a chain and sprocket, or going direct drive, will not require many frame or spacer changes.

![](/files/-M8pu2nOq_GBUp1NvSAL)

Product material selection is noted below. [Traction wheels](https://www.revrobotics.com/rev-for-ftc/motion/wheels-hubs-adapters/wheels/) and Grip Wheels ([REV-41-1267](https://www.revrobotics.com/rev-41-1267/)) are co-molded with a polyurethane tread for increased traction.

### Motion Components Materials

| Component   | Material                         |
| ----------- | -------------------------------- |
| Sprockets   | Acetal (Delrin/POM)              |
| Gears       | Acetal (Delrin/POM)              |
| Pulley      | Acetal (Delrin/POM)              |
| Wheel Body  | Nylon(PA66)                      |
| Wheel Tread | Thermoplastic polyurethane (TPU) |

REV DUO wheels, sprockets, and gears have a M3 bolt hole mounting pattern that is on an 8mm pitch as shown below. This makes it easy to directly mount to REV Robotics brackets, extrusion, and channel. The 8mm pitch is also compatible with many other building systems.

![](/files/-M8puR5vCAlKum6AwcSk)

Sometimes, it may be desirable to stack together multiples of the same gear or sprocket on a shaft. As a best practice, all components should have the **alignment notch** oriented the same direction on the shaft. The alignment notch can be found on the raised hub on either side of the gear or sprocket.

![](/files/-M8puTGPp9YhNFgvhZ0h)

In many cases the number of teeth on the gear or sprocket is not divisible by six, the number of sides on the hex shaft, and therefore the relative rotation between two of the same part will result in the teeth being out of alignment with each other. If the first sprocket was put on a shaft with the alignment notch facing upwards, there would be a valley at the top of the sprocket. If the second sprocket was added to the shaft, but rotated clockwise by 60 degrees (by the turn of one flat side), there would be most of a sprocket tooth at the top of that sprocket.&#x20;

![](/files/-M8pubv0wpi7aytPw2Rq)

{% hint style="warning" %}
It’s possible to build a working system without aligning stacked parts, but it’s not recommended.
{% endhint %}
