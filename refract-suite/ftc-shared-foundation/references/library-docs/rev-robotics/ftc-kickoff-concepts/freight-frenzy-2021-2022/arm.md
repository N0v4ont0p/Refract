> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/arm.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/arm.md).

# Freight Delivery Mechanisms

Once we decided on a way to intake and outtake components, we needed to decide how to place freight on the various levels of the shipping hub. That line of thought brought us to our next game challenge question: what kind of mechanism do we need to score on each of the three levels. From there we brainstormed requirements and came up with a few different Freight Placement Mechanisms.&#x20;

## Requirements

* Bare a Light Load - The mechanism has to be able to handle the load of an intake and a piece of freight.&#x20;
* Mounting Point - has a mounting point for an intake&#x20;
* Score All Three Levels - The mechanism has to be able to score on any of the three alliance shipping hub levels with ease
* Simple, repeatable, reliable - we want something that is easy to build and consistently scores the required levels&#x20;

{% embed url="<https://www.youtube.com/watch?v=3gQJs75M3Uo>" %}

## Conveyor

In our kickoff concepts for the 2021 FTC game Ultimate Goal, we explored conveyor mechanisms to move the major game element  between an intake and a shooter.  This year, we wanted to explore how a conveyor mechanism could be used to intake, transfer, and outtake freight.&#x20;

![](/files/-Mk3La2vVOvprgeULwhr)

We created a simple conveyor mechanism using carboard and Timing Belts and Pulleys. We then attached it to a drivetrain. Right away we realized that the conveyor would not act as intake. In order to mitigate this we could attach a top roller intake to the mechanism and power it from the same motor that powers the conveyor. However, we noticed some other issues with this design that did not meet our requirements.&#x20;

* The conveyor is set to shipping hub level 3 and can not move to level 1 or 2
* Does not consistently score at any level
* Struggles to work with boxes

With the faults in mind we decided to scrap this idea, rather than develop it further.&#x20;

## Elevator

After scrapping the conveyor idea, we wanted to explore using our Linear Motion Kit to create an elevator. We made a few modifications to at two stage continuous lift to create the elevator below.&#x20;

![](/files/-MiYAbfFJdI5J1W-tYCX)

{% hint style="info" %}
The graphic above showcases the lift on a drivetrain to show one of the ways it could (or would) be mounted.&#x20;
{% endhint %}

We focused on some small changes to the lift to enhance performance, such as adding more Double Sided Sliders to the assembly to increase stability. However, the main change we made we spooled the string for the life. By sandwiching the string between the two sides of a GT2 Pulley, we were able to ensure that the string would stay secured while powering the mechanism.

![](/files/-MjVnlZAaK0mlEGGTJ11)

To set the string in the pulley, pull the string through the wholes of the pulley so that one end of the string is sandwiched between the two pulleys. Ties of the other of the string and secure the assembly with bolts.

While the optimizations to the elevator worked in our favor as far as performance of the elevator, the elevator still did not meet our outlined requirements. Elevator mechanisms take time to make sure they are working smoothly that we didn't have as much time to optimize during the weekend.

## Single Jointed Arms&#x20;

{% embed url="<https://www.youtube.com/watch?v=tPapwToqGGA>" %}

As soon as we began brainstorming for Freight Frenzy, we realized that our Class Bot would be a good model for a pick and place game. The main reason for this realization is the fact that the Class Bot features a single jointed arm.&#x20;

![](/files/-MjV-3LIqXHJhYtrAGDT)

What makes a single jointed arm desirable as a mechanism this season? Lets consider a similar season to answer this question. Rover Ruckus required teams to intake components like the cargo and boxes (known in that season as silver and gold minerals), and place them inside a lander to score. The main difference between Rover Ruckus and Freight Frenzy is the height of lander versus the height of the alliance shipping hub. To score in the lander the robot needed to be able to extend to a height of \~29.5 inches from the game field floor, whereas level 3 of the alliance shipping hub is 16.25 inches from the game field floor.&#x20;

In Rover Ruckus to reach the required height for scoring many teams created several stage linear motion mechanisms, linear motion mechanism attached to an arm, or multijointed arms. With Freight Frenzy the scoring height requirement is much shorter than that of Rover Ruckus. All three levels of the shipping hub are within the 18 by 18 by 18 inch frame requirement for the robot. Meaning that a robot with a single jointed arm within the frame requirement can easily score on each level of the alliance shipping hub.&#x20;

Ultimately a single jointed arm with an intake mounted to it, is one of the simplest solutions to Freight Frenzy. We knew from experience that the class bot arm along would struggle to bare the load of an intake like the roller intakes we discussed previously. To solve this we decided to explore some sturdier options.&#x20;

![](/files/-MiWwLw5zFy6KAGcYDHr)

Above is one of our first drafts of a single jointed arm. C Channel provides an elevated torsional strength over extrusion, allowing the arm to withstand larger loads. The Channel also gives us more options for mounting an intake.&#x20;

However, this version of the arm was  heavier than we wanted, which may cause balance issues with the robot. This is easily solved with some counter balancing, but we wanted to see if we could create a more optimized version.&#x20;

## Four Bar Linkage

One of the issues with a single jointed arm is the positioning of the intake on the arm relative to the goal or playing field. This is something to consider with any pick and place type game like Freight Frenzy as the orientation of the intake matters for placement. Four Bar Linkages are one way to have the orientation of the intake stay constant through out the movement of the of the arm.

![](/files/-MjGcGh0RucVPMsBWycN)

This specific implementation of a four bar linkage allows for the arm to be very light. The L Beams on the end of the linkage provide a number of mounting locations for an intake or claw. The linkage itsefl is connected to mounting points on the L Beams with Ball Joint Rod Ends with the stand offs connected back to the channel uprights in a similar manner.&#x20;
