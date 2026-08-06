> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/drivetrain.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/drivetrain.md).

# Drivetrain

## General Drivetrain Options

Before diving into the specific obstacles in the Freight Frenzy game that may impact drivetrain design, lets first consider some of the game agnostic information on drivetrains.&#x20;

{% embed url="<https://www.youtube.com/watch?v=IjYp2vaRZLo&t=3s>" %}

### Robot Size Restrictions

Robot rules, outside of the weight limit, have mainly stayed the same. The main constraint is the 18" x 18" x 18" sizing requirement.

### Drivetrain Options

While there are many types of drivetrains teams can build, getting a drive train up and running as quickly as possible should be an overall goal. With this in mind there were two main drivetrains we considered utilizing for Freight Frenzy; Differential Drive or Mecanum Drive.

![](/files/-MHITU8RoRkSW0c5Hy-6)

#### Differential Drivetrain

Using a differential or tank drivetrain, like the [Channel Drivetrain](/duo-build/channel-drivetrain-build-guide.md), is a solid option for teams.

| Pros                            | Cons                                            |
| ------------------------------- | ----------------------------------------------- |
| More traction with the floor    | Can not strafe to align with game piece or goal |
| Stock out of FTC Starter Kit V3 |                                                 |

#### Mecanum Drivetrain

Using a [mecanum drivetrain](/duo-build/mecanum-drivetrain-kit-mecanum-drivetrain.md) gives teams some extra maneuverability on the field by allowing the chassis to move omni directional.

| Pros                                 | Cons                                         |
| ------------------------------------ | -------------------------------------------- |
| Move side to side for alignment      | May have trouble getting over the barrier    |
| Lower to the ground with 75mm Wheels | Requires two extra motors and mecanum wheels |

Either choice for a team will lead them to success this season. For our prototyping we went with the channel drivetrain to make modifications.

## Field Obstacles and Challenges

{% embed url="<https://www.youtube.com/watch?v=9C68qavGQVA>" %}

Many FTC teams recycle drivetrains from season to season, whether for cost or ease of design reason. The requirements surrounding the warehouse, such as the barriers and the warehouse procedures, shakes up the standard design expectations for drivetrains in FTC.&#x20;

There are two options for getting around the barriers: Going around or going over.&#x20;

#### Going Around&#x20;

Each barrier is roughly 13.7 inches from the playing field wall. To go around the barrier a drivetrain must be less than 13.7 inches wide. Creating a drivetrain that meets the size parameter creates constraints in the overall size of the robot. While this is a perfectly valid solution to the problem, we wanted to find a solution that could be made from a Starter Kit, and did not require structural components to be cut down.&#x20;

#### Going Over

The poles of the barriers are roughly 1.26" from the floor with a roughly 3.5" gap between each pole. If we compare these dimensions against the standard FTC kit drivetrains, the drivetrains do not have the clearance to get over the barrier. Using our C Channel we were able to create a solution to this clearance issues.&#x20;

![](/files/-MicMUh1962c97yDjtRJ)

Rather than seat the wheel shafts within the bearing holes on the Channel pattern, we used the extrusions slots and bearing pillow blocks to host the wheel shaft. By doing this we get approximately 2 inches of clearance, which gives us the clearance necessary to get over the barrier. &#x20;
