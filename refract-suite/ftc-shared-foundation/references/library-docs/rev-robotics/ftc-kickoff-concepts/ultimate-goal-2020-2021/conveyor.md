> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/conveyor.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/conveyor.md).

# Conveyor

Once the rings are in the robot we need a way to store and then move them to the shooter to score points. One way to accomplish this is to create a conveyor belt system to move the game piece.

### Requirements

* No jamming - pieces are pretty compliant so worried they will be easier to jam up
* Able to move vertically a plus - geometry of the 18" cube leaves a bit of a space constraint.
* Power off of one motor or servo- need to limit the number of motors used here to save for other applications

{% embed url="<https://www.youtube.com/watch?v=aWmIiIyM9sc>" %}

## Round Belt - Top/Bottom Belting

One of the first thoughts for moving the game pieces was to use pulleys with round belt. This is a good option as it gives flexibility where the pulleys are located as the belting is cut to length and then barbs are put in. One of the first sketches had belting on the top and/or bottom of the ring to move it along.

![](/files/-MHNasB4zEq9Yo6g8yPX)

We chose to make a simple test rig with pulleys and round belt with using cardboard as a bottom floor for the prototype. The rings move pretty well through the system this way, however there was some slipping and concerns on the belting having enough compression in the middle over a longer run.

## Side Belting

The next idea was to build a side belting with the pulleys and round belt. This would move the whole disk over as the belting was moving. We wanted to go with a bit of a thicker belt so transitioned to using GT2 Timing Belts to transfer the rings. This solution worked fairly well in testing.

![](/files/-MHNbSrTsSQC2FJ16eW7)

### Final Design

The final design uses 3mm GT2 belts mounted to extrusion to press on either side of the ring to bring from one location to another. The mechanism functions well at any angle up to 90 degrees, and even a little past 90 if need be.

![](https://lh4.googleusercontent.com/9n-KF9qfWji-2zX02751P9LVGw1V3nOJ0RXkGi_D7uCSYgcNcP3JuFcKGnocx2WsNECNjrw7Py_NQMgDAIO47hmhmqvutyCw0OQN9F4ERzu4sETjDw8cg-Ec-IGhbQEUIt3oyR6f)

The mechanism is driven by a single HD Hex Motor with a 20:1 reduction. This mechanism could probably go faster with a smaller reduction but would need more testing. Driving this with a servo(s) is also possible. The servo is slower, but the speed of this mechanism is not critical assuming you are moving pieces while aligning for a shot.

![Bottom View showing the Chain Run to ](https://lh4.googleusercontent.com/BGcNyTitGgeCzVYGaYd5GuipG201Uc8picMPXqwGHQHPMPyllLsugoZHOdlSadLXyvvYcQH-9FqMBz1ZCr5tRy-AB6ECWV_LxbIv1-N5j3fnqWR0PlxOjMVhOi-k5PwD7Fb4x9ji)

Notice that the flange of the GT2 pulleys extends past the thickness of the belt. In addition to changing the compression of the belt against the ring, the flange also has a very low coefficient of friction on the game piece. We found it was important to ensure that the pulley flanges didn't touch the game piece.

![](https://lh3.googleusercontent.com/xLLDDtFEFatzeLP5ev2bMymthMOVaeS_hc0ZtV3_6WYhAUQa3uup5jrh339dIyF8D0cVI5aXJCXFZNDjXVD_tLa4aqje2niHASsUI1irgB9KuLp-wOUGLmOyMPUDzA28YGX6dDKQ)

In order to get rid of the flange but keep the belt retained on the pulley, we used 30mm traction wheels on either side of the pulley middle section. These traction wheels have a good coefficient of friction against the game piece, and do not protrude past the thickness of the belt as much as the pulley flanges do.

![](https://lh5.googleusercontent.com/8JIrEb9jTyDxT-7tRJej413-RSqFlCCaKx-St9yRqKSvRPnaI8NkOPIwnbTSb14owe4wx3UyzO9pQu-eYM0dgw0q83L_IE8Abk9S5TJe9dFtAP5GruKGn70cfqjtvcyLjlfwMGts)

### Design Considerations

**Friction**: Friction is very important for pulling the ring up the feeder. The friction of the GT2 belts works well, but the friction of the round polybelt with only a single belt is not as good. If using polybelt multiple belts are likely needed.

**Compression**: There is a balance between the amount of compression the ring is seeing as it passes by a pulley versus the amount of compression it sees as it is in the middle of the belt. The amount of normal force, and thus the amount of friction, that the belt can exert on the ring greatly decreases in the middle of the belt. The extrusion side of the C-Channel could be used to have infinite adjustability on the mechanism to find the distance that has the perfect amount of compression. Once this is determined, the hole pattern of the c channel can be used to fix everything in place

**Belt Length**: Another important consideration is the length of the belt. On a long belt, the amount of normal force that the belt can exert on the ring is greatly reduced in the middle compared to a shorter belt. For this reason, two shorter belts are used in series rather than a single longer belt.
