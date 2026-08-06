> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/intake.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/intake.md).

# Intake

POWERPLAY's rules limit robots to possessing a maximum of one corresponding Alliance Cone or one corresponding Alliance Beacon at a time, so, a major component of your points per second strategy should be the intake.  Intakes come in many different forms, so we brainstormed some concepts and put them through the first stages of the engineering design process to help us decide if they met our gameplay requirements.

## Requirements

* **Touch it, Own It** - Be able to quickly intake and control elements
* **Pick Up One Only** - reduce the chances of picking up more than one element by using the exterior rather than interior as a grip point
* **Adaptability** - ability to pick up a cone against a wall on a cone stack as well as in the open from a substation or on the field
* **Release It** - be able to release the element with ease whether by mechanical movement or by automation

## First Round of Prototyping&#x20;

{% embed url="<https://youtu.be/n1MbgEBi1jk>" %}

### **Simple Gripper**

We started with a simple gripper that has one pivot joint. The simple gripper has two stationary compliant wheels on the moving arm that grip the cone. This design is actuated by a servo and its low profile allows for cones to be picked up close to the wall.&#x20;

<figure><img src="/files/ldBSSl8MGrHeu0Lgw0MT" alt=""><figcaption></figcaption></figure>

### **Passive Intake**

We also wanted to explore passive options for an intake. This passive intake works with free-spinning rollers at the end of two arms that are mounted with surgical tubing. The flexibility of the surgical tubing allows the arms to stretch around the cones as the rollers lock them in. Because this intake is passive and grabs a cone from the side, a bit of assistance from the field wall to keep the cone in place while grabbing is necessary. This may be an issue with intaking cones that are in the middle of the field.

<figure><img src="/files/zb5ttU3AF3E03DovA4xn" alt=""><figcaption></figcaption></figure>

### **Active Roller Intake**

The active roller intake uses two sets of wheels powered by servo motors that roll the cones into a held position.  The space needed to mount the servos and gear them correctly for the intake wheels causes this intake to be a bit bulkier than the others. Depending on what structural material you use, the frame can also be heavier which will need to be taken into consideration when building a lift.&#x20;

<figure><img src="/files/6QcrHw8IIlU6FeE28kwx" alt=""><figcaption></figcaption></figure>

## Second Round of Prototyping&#x20;

{% embed url="<https://youtu.be/UglIW28PXGc>" %}

### Compact Active Roller Intake

For our final intake design we took inspiration from the Active Roller Intake to create a version that could get closer to the wall and pick up cones from the cone stacks. This compact active roller intake features one servo motor driven roller paired with a free spinning roller. This provides the same amount of control as the two roller intake with about half the footprint. Because of the smaller size, this intake is also easier for your lift to move.&#x20;

<figure><img src="/files/U2DzIM9ZghvaVaUeit4k" alt=""><figcaption></figcaption></figure>

### Bonus: Cone Flipper

A bonus mechanism we prototyped was a cone righting device. With cones getting dropped or knocked over, it might be a useful tool to have on your robot if your intake can only pick up an upright cone. Our idea was to mount compliant wheels on a rotating roller that is hinged to allow the cone to rotate into position.

<figure><img src="/files/pXwi7iwouEsyqBKfvczc" alt=""><figcaption></figcaption></figure>
