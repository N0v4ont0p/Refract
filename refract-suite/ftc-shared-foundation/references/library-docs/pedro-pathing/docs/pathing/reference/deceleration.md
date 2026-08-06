> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/deceleration.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Deceleration
---

### Default Deceleration
This is the default deceleration method that is used if no other method is specified. This deceleration method only decelerates on the last path of a PathChain or on the last. It uses two parameters to control the deceleration behavior:

#### BrakingStrength
This controls how strong the braking is. A higher value means stronger braking, while a lower value means gentler braking. The higher the value, the more abrupt the stop will be. The lower the value, the smoother the stop will be. However, a very low value may cause the robot to overshoot the target position.
This value is a double stored in the PathConstraint class/object and can be set in a PathChain or a Path.
To set in a PathChain after a path is added: `.setBrakingStrength(double set)`
To set in a Path: `PATH.setBrakingStrength(double set)`

<Callout title="Note" type="info">
  - BrakingStrength was formerly known as **Zero Power Acceleration Multiplier (ZPAM)** in earlier versions of Pedro Pathing
  - A BrakingStrength of 1 corresponds to a ZPAM of 4.
</Callout>

### Global Deceleration
This allows deceleration based on a entire PathChain and not only the last path of the chain. This is especially useful if the last path in the chain is short. Note that this mode is recommended for use globally, even when path chains are only one path, because it is more optimized than the default mode. Settings like BrakingStrength still take effect here as normal.

To set in a PathChain: `.setGlobalDeceleration(double BrakingStrength)` or `.setGlobalDeceleration()`

#### BrakingStart
This controls when the braking starts. The higher the value, the earlier the braking starts. The lower the value, the later the braking starts. A very high value may cause the robot to stop too early, while a very low value may cause the robot to stop too late.

BrakingStart is recommended to be used primarily for optimization, not for mitigating overshoot.

To set in a PathChain (only used with Global Deceleration): `.setBrakingStart(double set)`

### No Deceleration
This disables deceleration for the entire path chain, allowing full speed at the end of the path chain. Though, this may cause overshoot and inaccuracy at the end of the path chain.

To set in a PathChain: `.setNoDeceleration()`
