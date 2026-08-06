> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/drive-algorithm/pidfs/centripetal.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Centripetal
---

### Purpose

The centripetal force correction enables the robot to accurately follow curved paths.

### Setup

1. Set your robot's mass
Your robot's mass is used to compensate for centripetal force. To set the
mass, simply add `.mass` in `FollowerConstants`. Note that the mass **must
be in kilograms**.

```java title="Constants.java"
public static FollowerConstants followerConstants = new FollowerConstants()
        .mass(5);
```
2. Open Panels. If you haven't used Panels before, you can read the documentation on [Panels Configurables](https://panels.bylazar.com/docs/com.bylazar.configurables/).
3. On your Driver Hub or Driver Station, select the `Tuning` Opmode, navigate to `Manual` and then choose `CentripetalTuner`.
4. Ensure that the timer for autonomous OpModes is **disabled.** Otherwise, the OpMode will automatically stop after 30 seconds.
5. Run the run the `CentripetalTuner` autonomous OpMode.

<Callout title="Warning!" type="warning">
 - Immediately after running the `Centripetal Tuner` Opmode, the robot will move forward and left 20 inches in a curved path. Make sure you have enough space before running this opmode.
 - You can adjust the distance the robot drives back and forth through Panels. 
</Callout>

## Tuning Process
Follow this video to help you tune the centripetal scalar: 

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/728GLkqy9yY?si=YFZ0iWha6KqztOsH" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>

Observe the robot’s path:

- If the robot corrects towards the inside of the curve, decrease `centripetalScaling`.
- If the robot corrects towards the outside of the curve, increase `centripetalScaling`.
Adjust the value of `centripetalScaling` within the `Tuning`-> `Follower` -> `Constants` section in Panels.

### Update Tuned values Into Your Code
1. Once you are satisfied with your `centripetalScaling`, head over to the `Constants` file. 
2. Navigate to the line `.centripetalScaling(0.005)` under `followerConstants`. If you don't have this line, feel free to add it yourself. 
3. Update the parameters in `.centripetalScaling(0.005)` with the `centripetalScaling` value you tuned. 

## Troubleshooting
If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).
