> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/lifts.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/lifts.md).

# Lifts

The varying heights of the Junctions create a challenge for placing cones that can be solved with a vertical movement from your robot. When designing these lifts, we decided to try three popular categories of Lifts used commonly in FTC: Linear Lifts, Single Jointed arms, and a Four Bar Linkages.&#x20;

## Requirements

* **Simple, Reliable, Compact** - we want something that fits within the 18"x18"x18" starting requirement, is easy to build and consistently scores at all levels&#x20;
* **Bear a Light Load** - The mechanism has to be able to handle the load of the intake and a single cone or Beacon.&#x20;

## Lift Prototypes

{% embed url="<https://youtu.be/SuGy5VHyT_w>" %}

### Elevator

We started exploring designs with our Linear Motion Kit. We made a few modifications to the two stage continuous lift to create the elevator below. While it is fairly easy to build and deploy, this lift is not capable of reaching the high junctions. However, you may be able to add on another stage to gain more height. Also, the Linear motion kit can be used for horizontal motion too, as seen in our Lift Prototypes video above.&#x20;

<figure><img src="/files/NDseNiAtkovNzjaMb0PP" alt=""><figcaption></figcaption></figure>

### Single Jointed Arms&#x20;

A Single Jointed Arm is one of the simplest solutions for a lift. We knew from past experience that this arm would struggle to reach the high junctions and fit within the 18"x18"x18" size restraint. It is important to pay attention to your geometry calculations when building a Single Jointed Arm so you can maximize your reach. This version of the arm was also a little heavier than we wanted, which may cause balance issues with a more narrow or smaller drivetrain.&#x20;

<figure><img src="/files/AborFxqjLCie2TGZ48zl" alt=""><figcaption></figcaption></figure>

### Four Bar Linkage

Four Bar Linkages are very similar to Single Jointed Arms because they both pivot around a single point. You will run into similar issues with what height they can reach so be sure to pay attention to your geometry calculations! However, Four Bar Linkages are unique because they maintain the orientation of the object they are lifting. This is very useful for POWERPLAY when lifting a standing cone. As the lift rises, the cone will remain parallel to the plane it started in, remaining upright.&#x20;

<figure><img src="/files/F0QFNWm87qooqgKPB7L4" alt=""><figcaption></figcaption></figure>

### Reverse Virtual Four Bar

A Reverse Virtual Four Bar Linkage is a two-stage lift where the second stage is actuated by a four bar arm. Because the lift folds back on itself, you can reach almost twice as high as a single jointed lift. The Virtual Four Bar is created by the chain and it helps keep the end of the lift traveling along one plane. This keeps whatever you are raising in an intake oriented correctly for the whole lift.&#x20;

The Kickoff Concepts team really liked this lift so we mounted our Compact Active Roller Intake to the end for our Starter Bot testing. It is mounted on a hinge so that the lift will keep the cones upright, but we will still have the needed compliance for lining up to intake cones.&#x20;

<figure><img src="/files/vri9BXrDTiEkYceiEnmy" alt=""><figcaption></figcaption></figure>
