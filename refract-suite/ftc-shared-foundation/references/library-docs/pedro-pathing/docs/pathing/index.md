> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/index.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Introduction
description: What is Pedro Pathing?
---

Pedro Pathing is a **path follower** initially developed by [FTC
team 10158](https://ftcscout.org/teams/10158?season=2023) to revolutionize
autonomous navigation in robotics. Pedro Pathing uses Bézier curves, PIDF
control, centripetal force correction, and more to provide smooth, fast, and
accurate path following.

Using Pedro Pathing for your autonomous routines allows for:

- **Faster path execution:** Pedro Pathing uses four vectors to calculate
optimal wheel powers.
- **Correction for disturbances:** Since localization allows Pedro Pathing
to know your robot's position, it can correct for disturbances and get back
on the path.
- **Creating paths on-the-fly:** Since Pedro Pathing uses PID control, it
can instantly go to any position.

No matter how good your team is, Pedro Pathing can give you the tools
necessary to create high-quality, fast, consistent autos.

## Prerequisites

To use Pedro Pathing, you must:

- **Have an omnidirectional drive**, such as mecanum, x-drive, or swerve.
This is most drives except for tank.
- **Have some form of localization**. This can be dead wheels, the goBILDA
Pinpoint,
the SparkFun OTOS, or more. If you don't want to buy anything, you can use
your drive motor encoders.
- **Be using Android Studio**. Pedro Pathing does not work with OnBot Java
or Blocks. If you are not using Android Studio, you should give it a try!

## Tuning

For Pedro Pathing to work properly with your robot, it must be tuned first.
This process is designed to be very approachable and should take at most a
few days.

Pedro Pathing also requires localization, or knowing where your robot is on
the field. There are many forms of localization for you to choose from.