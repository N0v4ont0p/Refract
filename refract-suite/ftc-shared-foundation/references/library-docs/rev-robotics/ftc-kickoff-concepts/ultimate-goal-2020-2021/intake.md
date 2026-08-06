> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/intake.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/intake.md).

# Intake

Manipulating the ring game piece during play is a key for success in this year's challenge. Intakes can take many forms but we would want to try a few concepts and see how the meet some of our requirements.

### Requirements

* Touch it, own it - Be able to quickly touch the rings and have control of them
* Pick up multiple - Be able to handle multiple of the rings coming in at a time
* Ability to hand-off to a conveyor/shooter

Two concepts to try as 15 minute prototypes are a pinch intake and a roller intake.&#x20;

{% embed url="<https://www.youtube.com/watch?v=RGW7R9zM6oo>" %}

## Pinch Intake

Basic idea is to have a servo with a pivot to pick up the rings. Ability to lift up the intake and put it down on top of other rings in position to carry up to 3 is another requirement.

![Concept Sketch for Pinch Intake](/files/-MHNAr9Jcj2gROff0Z7N)

We took the intake that we made last season for SKYSTONE and tried it out with the rings. Surprisingly it didn't need much adjustment to pick up the rings. Holding multiple rings was possible however the grip on the pinch decreased with the more rings used. If using a pinch intake teams may want to consider picking up from the inside diameter of the ring and finding some ways to hold onto a compliant piece like the ring.

With the difficulty of picking up multiple rings for carrying we chose to look at another option for intakes as well.

## Roller/wheel Intake

Another way is to have a roller or wheeled intake. With the size of the game piece relative to the size of the robot and the number of game pieces a robot could hold, we chose to go with a horizontal roller intake and to iterate on this concept.

![Concept Sketch for Roller Intake](/files/-MHNAr9Kq-lIZNDW0lZ6)

The real quick test of this concept was stacking 90mm Traction wheels across a simple 15mm Extrusion frame. We direct drove the wheel roller with a Core Hex Motor as a proof of concept. This worked well as the traction wheels had enough grip to pick up the ring game pieces. Picking off of a stack of pieces could be challenging and something needed in future iterations.

This is the design we chose to iterate off of to find a better solution. Next steps were to mount this to a drivetrain to see how it performed.

## Pasta Roller Intake

When we started the process of developing the intake we were thinking of styles used in the 2017 FIRST Robotics Competition game STEAMWORKS as inpsiration. In that game a gear, which was a flat game piece like the ring, was picked up individually and delivered to another location on the field. Curious to see if a "Pasta Roller" intake would work we started tinkering on a drivetrain to see what we could come up with.

{% embed url="<https://www.youtube.com/watch?v=WIMA0Spyy28&t=1s>" %}

### Final Design

![](https://lh5.googleusercontent.com/b2NcBeCa8BEis1EZXg3_K24eXHAlmDof6lb7YCoIUL2HiGN8qshmLj0ecWVxkAPUiOTTdqRMWwRK_ZhZoZLzOpEuvfRN5og9IPx8HcZE70ycskq4qVRf-Xs0jcqwVRnXddznciZg)

Utilizes one large roller to pull the ring in, one small roller to knock the front edge of the ring up, and one small roller to redirect the ring into the robot. This utilizes an open front of the robot to move the ring into a location where a conveyor or indexing system could live.

The large front roller is connected to an arm that is free to rotate, which introduces some compliance into the system. Since the rings have some compliance to them we could hard connect this to a specific location. Furthermore, a ridgid mounted intake didn't allow for the "kicking" of the ring up the back to rollers and into the drivetrain. Another option is to keep the "drop down" behavior and have the intake pushed further forward. This would allow for the outer large roller to store inside the start configuration and deploy once the match begins to give extra space. This option also could allow for more wheels and wider roller for better ability to pick up rings.

### Design Considerations

The HD Hex Motor is running an UltraPlanetary with a 5:1 ratio. This is four times faster than the 20:1 ratio that the drive motors have. It is important for the intake speed to be faster than the driving surface speed so that the intake is able to pick up rings while the drivetrain is moving towards or away from the game piece.

Pieces of corrugated plastic were used as an easy way to direct rings from the wide front intake to the narrower rear rollers. The ring needs some way to be centered on the indexing mechanism, and corrugated plastic is an easy and effective way to create such a mechanism and comes in the FTC Starter Kit V3.

#### Other options

Rollers on the sides (i.e. parallel to the ground, on either side of the ring) could also be used, but it is more difficult to package:

* The rollers have to fit within the 18” footprint limit but still reach out enough to grab the wheels
* Adding compliance to the system is more difficult to achieve with side rollers, unless the rollers have some sort of compliant finger.

![](https://lh6.googleusercontent.com/uww24laI2WDazJDuxjFw3kFucL-rFZm1e_bNVKxYOx6De1DxJMXcjY3nS8-rB9m9m2DEAkFXURHVUKI2dNSnxPFJ6q1_OH4F3maIUGrMWbHSZ80dOSSqTGVcZiqW1XA3TQKUGOku)

* Power the side rollers is also a packaging/power issue as with the current design all rollers are powered off of the same motor.
