> Source: https://docs.revrobotics.com/duo-build/motion/linear-motion.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/linear-motion.md).

# Linear Motion

## Linear Motion Basics&#x20;

The REV DUO 15mm Linear Motion kit is designed for use with the slots on [REV DUO Structural Components](/duo-build/structure/intro.md). The Linear Motion Kit v2 ([REV-45-1507](https://www.revrobotics.com/rev-45-1507/)) contains all the necessary hardware to build a single stage lift if a team already has an FTC Starter Kit. Items necessary for powering the linear motion system are sold separately or as part of a linear motion bundle. That being said, requirements are highly dependent on implementation so tools and actuators are excluded from the bundle. This guide is designed to build a three stage lift in two possible configurations (Cascading or Continuous). Additional materials are needed to finish the build and detailed in the Tools and Materials.&#x20;

Linear motion can typically be defined as "straight line" or one-dimensional motion. Mechanisms like elevators and lifts are common examples of one-dimensional motion in robotics. The REV DUO Build System supports linear motion through the REV DUO Linear Motion Kit.&#x20;

![](/files/0hMV6zh3kcmUjBS7XMuF)

### Product Specifications&#x20;

The REV DUO Linear Motion Kit is designed for use with slots in REV DUO structural products. The Linear Motion Kit v2 ([REV-45-1507](https://www.revrobotics.com/rev-45-1507/)) contains all the necessary hardware to build a single stage lift if a team already has an FTC Starter Kit. &#x20;

{% hint style="warning" %}
The requirements for linear motion mechanisms are highly dependent on implementation. Other necessary parts for your mechanism may be sold separately.
{% endhint %}

## Driving Linear Motion

Linear motion stages can be driven many different ways, but our recommendation is to use a string wound around a pulley and segments of surgical tubing to operate as a powered return. The string and pulley arrangement is used in one of two ways: **Cascading** **or Continuous lifts**. In the [Cascading lift assembly](/duo-build/linear-motion-kit/three-stage-cascading-lift.md), all the stages move up simultaneously, each one by an equal amount. In the [Continuous string assembly](/duo-build/linear-motion-kit/three-stage-continuous-lift.md) only one stage moves at a time and the position of each stage relative to each other is not controlled, only the position of the final stage relative to the start position is controlled. This distinction is not relevant in most applications; however, it is a feature that can be used to great effect and is worth keep in mind during design and prototyping.&#x20;

{% hint style="danger" %}
Linear motion is driven by actuators, which means that the rotational motion of the actuators is transformed into linear motion. To ensure the integrity and consistency of the linear motion, motion constraint methods need to be employed.&#x20;
{% endhint %}
