> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/localization/offsets-tuner.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Offsets Tuner
---

### Prerequisites
This tuner is made to automatically find odometry offsets for [Two Wheel](https://pedropathing.com/docs/pathing/tuning/localization/two-wheel) and [Pinpoint](https://pedropathing.com/docs/pathing/tuning/localization/pinpoint) localizers.  
Currently, it only supports two deadwheels in the calculations.  
Before using this tuner, you **must** set both of your odometry offsets to both be 0.
The tuner is a part of the Tuning.java in 2.1.0 or later versions; however, it can be copied over to previous versions [here](https://github.com/Pedro-Pathing/Quickstart/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedroPathing/Tuning.java#L1222).
### Steps
* Set both localizer offsets (forwardPodY and strafePodX) to be 0.
* Place the robot in the corner of the field or corner of a tile facing a cardinal direction.
* Select and run the tuner (located Tuning -> Localization -> Offsets Tuner).
* Move the robot out of the corner and turn the robot 180 degrees.
* Move the robot back into the corner with the new rotated heading.
* Transfer the offsets provided from telemetry into your code as your forwardPodY and strafePodX offsets.
