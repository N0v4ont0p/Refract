> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/constants.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Constants
description: The Constants file
---

You may have noticed that there is a `Constants` file in the `pedroPathing`
package. This is where you configure all your constants for Pedro. It
contains four types of constants:

1. **Follower constants** consist of values from the
automatic, PID, and centripetal tuners.
2. **Drivetrain constants** contain constants specific to your drivetrain
type. For example, mecanum drivetrain constants contain the motor names.
3. **Localizer constants** contain constants specific to your localizer. For
example, OTOS constants include the hardware map name of the OTOS and the
offset.
4. **Path constraints** determine under what conditions a path may end.

There is also a `createFollower` method that constructs the follower. You
will call this method in your OpModes.

Below is a starting `Constants` file. The different tuning pages will guide
you through modifying it to suit your robot.

```java title="Constants.java"
public class Constants {
    public static FollowerConstants followerConstants = new FollowerConstants();

    public static PathConstraints pathConstraints = new PathConstraints(0.99, 100, 1, 1);

    public static Follower createFollower(HardwareMap hardwareMap) {
        return new FollowerBuilder(followerConstants, hardwareMap)
                .pathConstraints(pathConstraints)
                .build();
    }
}
```