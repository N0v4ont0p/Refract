> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/drivetrain.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/drivetrain.md).

# Drivetrain

## General Drivetrain Considerations

### Field Obstacles and Challenges&#x20;

The grid of Junctions on the POWERPLAY field is the largest field obstacle for this season. Ground, Low, Medium, and High Junctions spaced in a 2ft grid can limit the amount of space your robot has to navigate the field. There are floor obstacles as well- the Ground Junctions. The Ground Junctions are 0.56in tall with a recessed portion that drivetrains can get stuck on if they do not have the necessary clearance. However, once a Cone has been scored on a Ground Junction, you can no longer drive over the Junction.&#x20;

### Robot Size Restrictions

Robot rules have mainly stayed the same for this years game. The main constraint is the starting 18" x 18" x 18" sizing requirement.

{% embed url="<https://youtu.be/uPkc0w7TgB4>" %}

## Drivetrain Options

While there are many types of drivetrains teams can build, getting a drivetrain up and running as quickly as possible to begin testing should be a priority. This year the two main drivetrains we considered were Differential Drive and Mecanum Drive.

### Differential Drivetrain

<figure><img src="/files/GXZR5p7MyMtcKwurIcGk" alt=""><figcaption></figcaption></figure>

Using a differential or tank drivetrain, like our [Channel Drivetrain](/duo-build/channel-drivetrain-build-guide.md) is a solid option for teams.&#x20;

| Pros                              | Cons                                                    |
| --------------------------------- | ------------------------------------------------------- |
| More traction with the floor      | Cannot strafe to easily align with game pieces or goals |
| Stock with the FTC Starter Kit V3 |                                                         |

### Mecanum Drivetrain

<figure><img src="/files/1s2MLz9AqxM8V7UcSs8V" alt=""><figcaption></figcaption></figure>

Using a [Mecanum Drivetrain](/duo-build/mecanum-drivetrain-v2.md) gives teams some extra maneuverability on the field by allowing the chassis to move omni directionally.

| Pros                                                                     | Cons                                                  |
| ------------------------------------------------------------------------ | ----------------------------------------------------- |
| Easily move side to side for alignment                                   | May have some trouble traversing the ground junctions |
| Lower to the ground with 75mm Wheels allowing for a more stable platform | Requires two extra motors and mecanum wheels          |

### Other Options

In addition to changing the wheels, you can vary other parts of your drivetrain to change how effective it is for navigating the POWERPLAY field.&#x20;

One way to do this is to change the size of your frame. If you shrink down your drivetrain, you will have more space to drive around the grid than if you built your robot to the full 18in X 18in dimensions. However, if you do this pay attention to the geometry of your other mechanisms as that will change too.&#x20;

Also consider raising your drivetrain with pillow blocks if you need more clearance to get over obstacles. This is similar to what we did with the [Freight Frenzy Starter Bot](/ftc-kickoff-concepts/freight-frenzy-2021-2022/starter-bot-freight-frenzy.md).

## Starter Bot Drivetrain Update

Using either differential, mecanum, or another drivetrain for a robot will lead a team to success this season. For our prototyping and the final Starter Bot we used the channel drivetrain. In the video below we installed an optional mecanum upgrade to our Starter Bot to highlight it's maneuverability on this years field.

{% embed url="<https://youtu.be/_ugi4OpWkuU>" %}
