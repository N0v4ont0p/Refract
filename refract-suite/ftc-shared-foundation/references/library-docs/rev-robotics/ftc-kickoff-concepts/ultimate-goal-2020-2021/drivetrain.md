> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/drivetrain.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/drivetrain.md).

# Drivetrain

Drivetrains are one of the first mechanisms that teams typically build and start development on. There are few changes to the robot rules that are needed to consider when designing a drivetrain&#x20;

### Field Layout and Obstacles

Ultimate Goal provides a flat field with little in the way for a robot to maneuver through out the field of play. Rings are re-introduced into the field through a drop on the side of the goals by a human player. Rings will likely be rolling along the field and sitting flat when hitting a robot or another object like a field wall. While the rings themselves are compliant it doesn't seem like they are easily trapped inside of a drivetrain.&#x20;

### Robot Size Restrictions

Robot rules, outside of the weight limit, have mainly stayed the same. The main constraint is the 18" x 18" x 18" sizing requirement.

{% embed url="<https://www.youtube.com/watch?v=800w8TNgAYU>" %}

### Drivetrain Options

While there are many types of drivetrains teams can build, getting a drive train up and running as quickly as possible should be an overall goal. With this in mind there were two main drivetrains we considered utilizing for Ultimate Goal; Differential Drive or Mecanum Drive.

![](/files/-MHITU8RoRkSW0c5Hy-6)

#### Differential Drivetrain

Using a differential or tank drivetrain, like the [Channel Drivetrain](/duo-build/channel-drivetrain-build-guide.md), is a solid option for teams.

| Pros                               | Cons                                            |
| ---------------------------------- | ----------------------------------------------- |
| Can hold ground when getting rings | Can not strafe to align with game piece or goal |
| More traction with floor           |                                                 |
| Stock out of FTC Starter Kit V3    |                                                 |

#### Mecanum Drivetrain

Using a [mecanum drivetrain](/duo-build/mecanum-drivetrain-kit-mecanum-drivetrain.md) gives teams some extra maneuverability on the field by allowing the chassis to move omni directional.

| Pros                                 | Cons                                         |
| ------------------------------------ | -------------------------------------------- |
| Move side to side for alignment      | May have trouble getting rings against other |
| Lower to the ground with 75mm Wheels | Requires two extra motors and mecanum wheels |

Either choice for a team will lead them to success this season. For our prototyping of intakes we went with a Mecanum Drivetrain mainly so it would sit lower to the ground.
