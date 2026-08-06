> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/carousel.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/carousel.md).

# Carousel Mechanism

As we stated in the Game Breakdown, delivering ducks during the end game is a potential of 54 points. At 6 points per duck this is an equivalent action to scoring in the third level of the Shipping Hub. The Carousel itself is pretty similar to the Control Panel from the 2020 FIRST Robotics Competition game, Infinite Recharge, and is a good starting point for inspiration for a mechanism.

## Requirements

* Reliable - consistently interfaces with the rim of the carousel to do a full delivery
* Balance of power - can rotate the carousel quickly without tossing the duck off
* Simple - achieves the task without needing to be overly complex

## Grip Wheel Mechanism&#x20;

{% embed url="<https://www.youtube.com/watch?v=SrJ5mrpJKfA>" %}

We focused on creating one carousel mechanism, the grip wheel mechanism. The reason we focused so intently on this particular mechanism was that we wanted a mechanism that was easy to build. Powering a grip wheel with a servo we were able to produce the necessary traction to transmit motion to the carousel.

![](/files/-Mk3X1F9V-tXSgD6oGPl)

This mechanism met our needs and requirements for rotating the carousel. However, it does take the mechanism about six second to fully rotate the carousel, bringing our total points per second to about one. You may want to get a low speed motor, like the Core Hex Motor, to provide a bit more speed to the mechanism than the servo. Obviously be cautious of the speed, as we have mentioned in the previous sections.&#x20;
