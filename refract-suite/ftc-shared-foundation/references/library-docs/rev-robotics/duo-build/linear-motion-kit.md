> Source: https://docs.revrobotics.com/duo-build/linear-motion-kit.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/linear-motion-kit.md).

# Linear Motion Kit

## Introduction to Linear Motion

The REV Robotics 15mm Linear Motion kit is designed for use with the [REV Robotics 15mm Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/). The Linear Motion Kit v2 ([REV-45-1507](https://www.revrobotics.com/rev-45-1507/)) contains many of the hardware pieces needed to build a single stage lift. Items necessary for powering the linear motion system are sold separately, as part of a linear motion bundle, or in the FIRST Global Kit. Requirements are highly dependent on implementation so tools and actuators are excluded from the bundle. This guide is designed to build a three stage lift in two possible configurations ([Cascading](/duo-build/linear-motion-kit/three-stage-cascading-lift.md) or [Continuous](/duo-build/linear-motion-kit/three-stage-continuous-lift.md)). Additional materials are needed to complete the build are detailed in the Tools and Materials below.&#x20;

![](/files/0hMV6zh3kcmUjBS7XMuF)

### Tools and Materials

To complete the full assembly in this guide a few tools and additional materials are needed. Some quantities are depended on the type of lift being built.&#x20;

For this guide you will need:

* A 5.5mm nut driver ([REV-41-1119](https://www.revrobotics.com/rev-41-1119/))
* 2mm Allen Key ([REV-62-1868](https://www.revrobotics.com/rev-62-1868/))
* REV Robotics 15mm Extrusion
  * In this example, 420mm lengths are used ([REV-41-1432](https://www.revrobotics.com/rev-41-1432/)). Different lengths of REV Robotics 15mm Extrusion will work depending on application.
* REV Linear Motion Kit v2 – QTY 2
* Hardware not included in the REV Linear Motion Kit v2
  * Small Pulley Bearings ([REV-41-1368](https://www.revrobotics.com/rev-41-1368/)) – Max QTY 5
  * M3 x 12mm or longer hex cap bolts ([REV-41-1360](https://www.revrobotics.com/rev-41-1360/)) – Max QTY 13
  * M3 Nyloc Nuts ([REV-41-1361](https://www.revrobotics.com/rev-41-1361/)) – Max QTY 13
  * UHMWPE Cord ([REV-41-1162](https://www.revrobotics.com/rev-41-1162/)) – QTY 1 (actual length is dependent on length of extrusion)
* Core Hex Motor ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) or HD Hex Motor ([REV-41-1291](https://www.revrobotics.com/REV-41-1291/)) – QTY 1 (this example uses the Core Hex Motor)
* Surgical Tubing ([REV-41-1163](https://www.revrobotics.com/rev-41-1163/))

## Assembly Instructions

These instructions explain how to build **one half of a single stage lift**. Each linear motion kit contains enough hardware to create a full single stage lift. Repeat this process four times to create all of the segments needed for the four-stage lift.

| Images                           | **Steps**                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](/files/-M8r06tzjJU_Xta8o_TI) | <p><strong>Step 1</strong></p><p>Insert <strong>2</strong> M3 x 8mm bolts into the holes on the side of the slider plate with just the alignment groove, not the slider. Do not fully tighten these bolts, just start the lock nuts enough so they won’t fall off, but leave the bolts loose. Make <strong>2</strong> of these assemblies.</p><p>Note: use nylock nuts for this application</p>                                                                                        |
| ![](/files/-M8r06u-HhAjLQyNgP9L) | <p><strong>Step 2</strong></p><p>Insert <strong>2</strong> M3 x 8mm low profile socket head bolts into the double-sided slider. Be sure that you insert the bolts from the correct side because the double-side slider is not completely symmetrical. The bolt head is placed on the side with the circular countersunk cutouts, and the nuts fit into the hex countersunk cutouts. Make <strong>2</strong> of these assemblies.</p><p>Note: use regular nuts for this application</p> |
| ![](/files/-M8r06u0-7UIwpuLQcFf) | <p><strong>Step 3</strong></p><p>When assembling the double-sided slider, only tighten the nut so that it is flush with the bottom of the slider when the bolt head is all the way down. There should be clearance between the top of the nut and the slider as shown.</p>                                                                                                                                                                                                             |
| ![](/files/-M8r06u1tKLne6yakuDP) | <p><strong>Step 4</strong></p><p>Insert the double-sided slider into the extrusion channel with the nuts in the channel. You may have to slightly loosen or tighten the nut so that it will align with the channel.</p><p>One the slider is fully inserted into the channel, tighten the bolt until snug. <strong>Do not overtighten the bolts as it may cause the slider to deform and bind with the extrusion.</strong></p>                                                          |
| ![](/files/-M8r06u26U9wkbtDShwk) | <p><strong>Step 5</strong></p><p>Take the slider plate assembly from Step 1 and slide it into the extrusion channel adjacent to the double-sided slider.</p><p>Once the slider assembly from Step 1 is fully inserted into the channel, tighten just enough so that the slider plate assembly does not freely slide in the channel, but is still loose enough that you can move the slider with minimal force.</p>                                                                     |

![Basic Assembly](/files/-M8r06u3ncjJcVzIUyiT)

The above steps 1-5 will result in the Basic Assembly for a 15mm linear motion elevator using the REV Robotics Linear Motion Kit and Extrusion. **Repeat the steps 1-5** above four times building the four-stage lift in this guide. A minimum of two assemblies are needed for a single stage lift. Adding additional Basic Assemblies will add more stages to the lift system.

![Basic Slide Assembly ](/files/-M8r06u4f6rAtM4EgoJZ)

Take two of the basic assemblies created in Steps 1-5 and slide them together.

With the hex cap bolts still slightly loose from step 5, gently slide the extrusion in and out allowing the slider plates to shift into optimal alignment. The slide should only take a minimal effort to move.

Carefully tighten the hex cap bolts without shifting the joining plates and re-check the slide for any binding. Repeat as necessary.

To finish assembly for the three stage lift, add two additional basic assemblies to the Basic Slide Assembly shown in Figure 3. One basic assembly is added to each side of the Basic Slide Assembly.

{% hint style="danger" %}
Don’t overtighten the bolts as it may cause deformation of the slider plate and binding.
{% endhint %}

![](/files/-M8r06u5C0Xbdm-BdAPX)

Once all four basic assemblies are slid together, attach an endcap onto one of the ends of the extrusion pieces with a M3 x 8mm or larger bolt. Make sure it is the same end for all four sections of the lift. The ends of the extrusion need to be tapped\* for M3. These will help keep the lift from overextending as well as hold the pulleys that are used to drive the lift up and down. Which type of elevator you are making will determine which pieces of extrusion on the lift require an endcap, and which can be left uncovered.

{% hint style="warning" %}
Tapping will make the attachment easier but is not necessary. Using a M3 x 16mm bolt and nut driver, carefully thread into the end of the extrusion. Finish threading with the nut wrench for addition leverage on the bolt.
{% endhint %}

## Driving Linear Motion

Linear motion stages can be driven many different ways, but our recommendation is to use a string wound around a pulley and segments of surgical tubing to operate as a powered return. The string and pulley arrangement is used in one of two ways: **Cascading** **or Continuous lifts**. In the [Cascading lift assembly](/duo-build/linear-motion-kit/three-stage-cascading-lift.md), all the stages move up simultaneously, each one by an equal amount. In the [Continuous string assembly](/duo-build/linear-motion-kit/three-stage-continuous-lift.md) only one stage moves at a time and the position of each stage relative to each other is not controlled, only the position of the final stage relative to the start position is controlled. This distinction is not relevant in most applications; however, it is a feature that can be used to great effect and is worth keep in mind during design and prototyping. The guide **assumes** you are attaching the lift to a robot. For creating this guide REV used a test stand to secure the lift and motor. This stand is shown in the steps for the Cascading and Continuous lift.

To drive the linear motion system, we recommend using a combination of these products:

* Small Pulley Bearings (REV-41-1368)
* M3 x 12mm or longer hex cap bolts (REV-41-1360)
* M3 Nyloc Nuts (REV-41-1361)
* M3 Plain Nuts (REV-41-1126)
* UHMWPE Cord (REV-41-1162)
* Core Hex Motor (REV-41-1300) or HD Hex Motor (REV-41-1301)
* Surgical Tubing

{% hint style="info" %}
*Check out the* [*Continuous* ](/duo-build/linear-motion-kit/three-stage-continuous-lift.md)*or* [*Cascading* ](/duo-build/linear-motion-kit/three-stage-cascading-lift.md)*lift guides to learn more on how to build a three stage lift.*
{% endhint %}
