> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/intake.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/intake.md).

# Intake

Since Freight Frenzy's possession and control rule limits robots to one piece of freight at a time, one of the keys for success is the intake mechanism. Intakes can take many forms, so we brainstormed some concepts and put them through the engineering design process to help us decide on an intake that met our gameplay requirements

## Requirements

* Touch it, own it - Be able to quickly intake and control freight&#x20;
* Adaptable - Be able to pick up all the different types of freight
* Pick up one - reduces the chances of picking up more than one freight&#x20;
* Release it - be able to outtake the element with ease

{% embed url="<https://www.youtube.com/watch?v=n86OHvEJvXM>" %}

## Scoop Intake

Once we identified our requirements for an intake, one of things to come to mind as a potential mechanism was some sort of gripper. We started with a Class Bot claw to do initial testing. However we had some issues with grabbing cargo and ducks.&#x20;

![](/files/-Mk3WBKB5nb7W7crPazI)

With the variance in size and shape of each of the different types of freight, we decided to take inspiration from claw machine claws. However, while claw machine claws are capable of picking up objects of different sizes and shapes, they aren't great at retaining objects. By playing with the idea of a claw machine we came up with the idea to create a scoop mechanism. The idea was to have a mechanism attached to a cage. The scooper extends out to direct freight into the cage and retain them in place while the robot moves to a shipping hub.&#x20;

![](/files/-MgrCcWQTd38xQnU5WCA)

For this design we powered the scoop using a Smart Robot Servo ([REV-41-1097](https://www.revrobotics.com/rev-41-1097/)). We wanted to use the servo programmer on the Smart Robot Servo to have an operating range of 180 degrees for the scoop mechanism. To do this we utilized an Aluminum Double Servo Arm ([REV-41-1820](https://www.revrobotics.com/rev-41-1820/)) and a Flat Beam to create a linkage.

After designing and building the mechanism, we put it to the test to determine if it met our requirements. The scoop was great at directing and intaking the cargo, but struggled to intake the boxes and ducks. There are a few fixes to this design that would get it to work more efficiently, such as replacing the servo with a motor to get more power on the scoop. While, this alternative may elevate the design to more successfully grab the other freight, lets explore some of other options.

## Roller Intakes

To evolve our intake into something that meets the requirements we set, we took a look at the prior FTC games that the cargo and boxes were used in, particularly the 2019 game Rover Ruckus. One of the most common and efficient intake types during those seasons were some sort of roller intake.&#x20;

We used an intake prototype from last years kickoff concepts, and iterated three total designs: one with traction wheels, one with a corrugated plastic flapper, and one with surgical tubing. We tested each roller intake to determine over all compliance and effectiveness. From this we found that the flapper was the the relatively level of compliance we needed.&#x20;

![](/files/-Mk3Lh4nhKXOmL_qtjSW)

We used a sheet of corrugated plastic that leverages behind each type of freight to intake and outtake them. The benefit of using corrugated plastic as the intake is the ability to adjust compliance. In our case we cut our corrugated plastic piece so that the side that interfaces most with freight is parallel to the ridges of the plastic. We then folded along the ridges of the plastic. This made the corrugated plastic more compliant, which increased the intakes speed and accuracy.

![](/files/-MjAc2vhNxEdjVIs0gMx)

We still wanted to evolve our designs and find a better more robust intake. So after this initial test we went back to the drawing board to further iterate.&#x20;

### Side Roller Intake&#x20;

{% embed url="<https://www.youtube.com/watch?v=ks-DTN97uJ0&t=185s>" %}

After trying out the Scoop Intake, we decided to explore roller intakes. One of the benefits of roller intakes over grip intakes, like the Scoop, are their ability to direct game elements. This time we took inspiration from car wash rollers. The side rollers on car washes not only clean the car, but help direct it along the track.&#x20;

Using this idea we created the "Side Roller Intake". The Side Intake utilizes two rollers, both made using a combination of REV Sprockets and Polycord. &#x20;

![](/files/-MhFwXFNtcxDXA7M0zFh)

During the testing process the Side Roller Intake, grabbed and released boxes quickly and efficiently. However, in order to grab cargo, the cargo had to be pushed up against a wall; otherwise the intake knocked cargo out of the way rather than intaking it.&#x20;

In the Ultimate Goal season we explored side rollers and had some concerns about how they packaged into the robot. Some of those same concerns came up with the intake.&#x20;

* Size - Side Roller was difficult to package within the limits of our drivetrain
* Weight - The weight of the Side Roller, when attached to an arm, caused instability

There were some other issues with this design including: lack of mounting space to attach the intake to an arm and the fact that the arm picks up more than one game element. To address these issues, move standoffs to decrease the size of the storage for the intake or add other structural components to mount off of.

#### Building the Sprocket Wheel Assembly&#x20;

![](/files/-Mk3Q4udCG034bn0wznp)

{% hint style="info" %}
Belt segments should be a bit longer than needed. It’s easier to cut down than replace the loop.
{% endhint %}

1. Add 20mm screws in the corners of the motion pattern on a 32 Tooth Metal sprocket
2. Create three polybelt loops using zipties. Place them on alternating screws.&#x20;
3. Add a 26 Tooth Plastic Sprocket to the assembly. Then create and add the three more polybelt loops, on the opposite screws to where the bottom loops were places.&#x20;
4. Add another 32 Tooth Metal Sprocket and nuts to the assembly&#x20;
5. Cut the zipties and pull the belts so each loop rests against the screw and is equal distance from the others.&#x20;
6. Tight screws until belts a significantly compressed and can not shift around at all.&#x20;

### Top Roller Intake

We decided to create a top roller intake as well. Choosing to do a top roller allowed us to gain the benefits of a roller intake while taking up less space than the side roller intake.&#x20;

![](/files/-Mk3IJUf5b-jXZQhRi5x)

The top roller intake we created uses our compliant wheels with a 5mm Hex Insert. We also created a spring loaded jaw using M3 Standoffs and surgical tubing. The compliance and strength of this mechanism meets all of our requirements. It is able to intake and outtake all three freight quickly and and reduces the chance of picking up more than once piece of freight.&#x20;
