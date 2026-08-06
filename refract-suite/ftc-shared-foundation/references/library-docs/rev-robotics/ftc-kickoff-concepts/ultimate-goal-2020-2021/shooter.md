> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/shooter.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/shooter.md).

# Flywheel Launcher

One of the strategic goals laid out was to score in the high goal from the starting location. Designing a flywheel launcher was the direction we chose to prototype.

### Requirements

* No jamming - pieces are pretty compliant so worried they will be easier to jam up
* Score from starting location - need to reach the goal from the starting location to match strategy
* Shoot consistently - be able to hit the same spot repeatedly to make alignment easier

## Shooter Design

Many FRC teams in 2013 fired frisbees into similar goals, and this design was common among them. Teams like [254](https://www.team254.com/first/2013/), [2791](https://www.youtube.com/watch?v=MmC1i6gHi-Y), and [399](https://www.youtube.com/watch?v=w1nhkMPqsDk) used this shooter with success.

Other mechanisms could also inspire shooting methods. [Clay Pigeon Shooters](https://www.youtube.com/watch?v=2jBhJ25Zq_M) could also be effective, as would shooters with a [rounded wall](https://www.youtube.com/watch?v=VrhiPnBz-iI) instead of a straight wall.

We chose the linear shooter because it was the simplest to construct and package in the time required.

There are three types of launchers we wanted to test with the rings: single fly wheel, double flywheel, and a single flywheel with accelerator wheel.

### First Prototype

The first prototype used an UltraPlanetary Gearbox on an HD Hex Motor that was mounted to extrusion. Compression plays a role in the speed the rings exit the launcher however this stayed constant as the gear ratios were swapped out. Testing for the mechanism is in the video below.

{% embed url="<https://www.youtube.com/watch?v=eHVtErHj9lg>" %}

### Final Design

The goal of this mechanism was to have a powerful launcher that could consistently make a full-court toss into the high goal. We deemed that it was necessary to launch the ring as close to laser-like as possible to make aiming and programming easier. This necessitated beefing up the framework, adding ball bearings, and having the UltraPlanetary Gearbox running as a direct drive onto the HD Hex Motor.

{% embed url="<https://www.youtube.com/watch?v=jtsXcoepRL8&lc=Ugyztkrd4jbwNctyAxp4AaABAg>" %}

An important concept to understand when designing a launcher is that the game piece will generally fly better the longer the amount of time that it is being accelerated. For this reason, this mechanism uses two motors, both on 1:1 ratios. Each motor directly drives one grip wheel. The first wheel accelerates the ring to a certain speed, and the second motor accelerates the ring from that speed to a very fast final speed. To add weight to the flywheel 86 Tooth Metal Gears were inset to the wheel allowing it to keep inertia when it was in contact with a ring.

The ring rolls against the 15x30mm extrusion as it is being accelerated by the wheel. The compression of the ring against the grip wheels can be adjusted by sliding the 15x30mm extrusion along the bottom extrusion rails. An adjustable amount of compression is an important factor when designing prototypes. This mechanism was designed robustly because any amount of compliance in the system will likely result in inconsistencies in the shot.

#### 1:1 Ratio on the Motors&#x20;

![](/files/-MHSJDJEHMYfule56P_t)

Getting the 1:1 ratio on the motors is simple! The following table is a list of all REV products needed to get the 1:1 ratio for one motor.

| Part Number                                             | Description                                         | Qty |
| ------------------------------------------------------- | --------------------------------------------------- | --- |
| [REV-41-1607](https://www.revrobotics.com/rev-41-1607/) | UltraPlanetary 550 Motor Plate                      | 1   |
| [REV-41-1604](https://www.revrobotics.com/rev-41-1604/) | UltraPlanetary Female 5mm Hex Output Cartridge      | 1   |
| [REV-41-1608](https://www.revrobotics.com/rev-41-1608/) | UltraPlanetary 550 Motor Pinion Gear                | 1   |
| [REV-41-1609](https://www.revrobotics.com/rev-41-1609/) | UltraPlanetary Hardware Pack (M3 x 10mm)            | 6   |
| [REV-41-1609](https://www.revrobotics.com/rev-41-1609/) | UltraPlanetary Hardware Pack (M3 x 8mm Button Head) | 2   |

{% hint style="warning" %}
The 550 Motor Pinion Gear comes pre-pressed onto the HD Hex Motors that come with UltraPlanetary Gearbox and HD Hex Motor Kit.&#x20;

If you have an HD Hex Motor that is not from an UltraPlanetary Kit you will have to remove the pinion pre-pressed on the motor and then press the 550 Motor Pinion onto the motor.&#x20;
{% endhint %}
