> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/pedro-v-roadrunner.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: PedroPathing vs Roadrunner
---

For FTC when it comes to path following, there are two main solutions, **Road Runner 1.0** and **Pedro Pathing**.
Although both are designed to achieve the same task, each has its own benefits and tradeoffs. The table provides an abbreviated list of features. For more information, read the *paragraphs* provided below.

## Table

| Aspect                  | Pedro Pathing                                                                                                                                                                                                                                                                                                                               | RoadRunner                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Following Strategy      | Uses three PID controllers: translational, heading, and drive, along with centripetal force correction.                                                                                                                                                                                                                                     | Generates and follows motion-profiled trajectories by using a combination of feedforward and feedback control.                                                                                                                                                             |
| Visualizer              | Has a no-code, web-based [path generator and visualizer](https://visualizer.pedropathing.com) that can export code for paths.                                                                                                                                                                                                               | Has a code-based [path visualizer](https://github.com/acmerobotics/meepmeep) that visualizes paths defined in code.                                                                                                                                                        |
| Tuning                  | Half automatic and half manual. Has six automatic tuning steps and four manual tuning steps, although the manual steps take slightly longer.                                                                                                                                                                                                | Mostly automatic. Has four automatic tuning steps and two manual tuning steps, although the manual steps take slightly longer. If using the SparkFun OTOS for localization there are four additional automatic tuning steps.                                               |
| Loop Time Optimizations | Automatically implements motor write caching with a configurable cache tolerance.                                                                                                                                                                                                                                                           | Automatically implements bulk reading.                                                                                                                                                                                                                                     |
| Good At                 | Correction for unexpected disturbances.                                                                                                                                                                                                                                                                                                     | Time-consistent trajectory following.                                                                                                                                                                                                                                      |
| Coordinate System       | Custom coordinate system. Provides a `PoseConverter` for converting to and from the official FIRST coordinate system.                                                                                                                                                                                                                       | Uses the official FIRST coordinate system.                                                                                                                                                                                                                                 |
| Command System          | [Ivy](/docs/ivy) is the official command library for Pedro Pathing. Since Ivy is a separate library, Pedro also remains compatible with other command bases like [NextFTC](https://nextftc.dev), [SolversLib](https://docs.seattlesolvers.com), and [Mercurial](https://docs.dairy.foundation/Samples/user_samples). | Has a built-in actions system. Also has an example on the docs for usage with FTCLib. [NextFTC](https://nextftc.dev) provides built-in integration with RoadRunner. Mercurial has [two sample repos](https://docs.dairy.foundation/Samples/user_samples) using RoadRunner. |
| Logging                 | Automatically logs many values to telemetry, but does not log to a file. Data such as current position can be logged by the user by using a third-party library such as [PsiKit](https://psilynx.github.io/PsiKit) for replay with [AdvantageScope](https://advantagescope.org).                                                            | Logs many values automatically to telemetry and to a file during every OpMode run. Uses a custom log format that is supported by [AdvantageScope](https://advantagescope.org).                                                                                             |
| Drivetrain Support      | Has built-in support for mecanum drivetrains. Users can provide a custom implementation of the `Drivetrain` interface to use another drivetrain, but does not support nonholonomic drivetrains such as tank.                                                                                                                                | Has built-in support for mecanum and tank drivetrains. Does not support any other drivetrains.                                                                                                                                                                             |

## In-depth Information
**Pros and Cons of Road Runner:**
Road Runner typically prioritizes time consistency above all else, using pre-planned motion profiling.
This allows the following of full trajectories with preset speed and acceleration constraints created by the user.
The Road Runner tuning pass is nearly automatic, making it more accessible for many users (although the actual 
tuning time doesn't necessarily vary too much from Pedro Pathing). 
Due to prioritizing time-consistency, Road Runner defaults to about 80% of the robot's maximum speed when path-following,
a major drawback. Furthermore, the motion model doesn't account for the reduced speed due to strafing which can often 
produce inaccurate motion. Road Runner has a built-in action system, but you cannot use any other action system in 
conjunction with Road Runner. If a user uses a certain external command-base in their TeleOp, they cannot use it in auto.

**Pros and Cons of Pedro Pathing:**
Pedro Pathing typically prioritizes speed and precision while following the path. The follower corrects the robot 
back to the target position when outside forces create inaccuracies in the robot's position or heading, while still 
following the path. Pedro Pathing also uses centripetal force correction, so it is able to follow curved paths better.
Similar to custom p2p and Pure Pursuit algorithms, Pedro Pathing typically moves the robot along the path much faster than Road Runner.
[Ivy](/docs/ivy) is the official command library for Pedro Pathing, providing a concise, flexible, and
powerful way to organize autonomous routines and manage teleop actions. Since Ivy is a separate dependency rather than
built into Pedro, users are also free to use other command bases like NextFTC, SolversLib, or Mercurial if they prefer.
A major advantage of Pedro Pathing is its path visualizer. The visualizer is web-based, doesn't require the user to write
any code, and even generates code for the user. The visualizer is also typically considered to be easier to use, since 
"eyeballing paths" can be done by arbitrarily dragging control points until a desired path is achieved. To assist in storage,
these paths can then be exported concisely into a single, re-uploadable file.

{/* Thanks to Davis for the table */}
