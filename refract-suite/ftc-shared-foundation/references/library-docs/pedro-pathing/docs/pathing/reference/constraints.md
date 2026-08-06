> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/constraints.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Constraints
---

import { Callout } from 'fumadocs-ui/components/callout'

Constraints are used to determine when a path is considered complete. 

There are **five** criteria that all must be met for follower.isBusy() to become false.

### Timeout
Sets how long, **in milliseconds,** the follower has to correct after stopping, and after this time delay is complete, this criteria to be considered complete.
Increasing it will give the robot more time to correct at the end of the path to improve its accuracy. Decreasing it will reduce the robot's wait time between following paths, but may cause the path following to be slightly more inaccurate. 

To set: `path.setTimeoutConstraint(double set)` 
	
### TValue
Sets the path's parametric end criteria, or how much of the path the robot must follow before it is considered complete. `set` should be a double between 0.0 and 1.0.

To set: `path.setTValueConstraint(double set)`

### Velocity
Sets the velocity that the robot must be below allowed for this criteria to be considered complete. This is in inches/second. 

To set: `path.setVelocityConstraint(double set)`

### Translational
Sets the maximum amount of translational error allowed for this criteria to be considered complete.
The error has to be under this value.

To set: `path.setTranslationalConstraint(double set)`

### Heading
Sets the maximum amount of heading error allowed for this criteria to be considered complete.
The error has to be under this value.

To set: `path.setHeadingConstraint(double set)`

<Callout title="Tip" type="info">
	If the robot gets stuck after reaching the end of the path and is unable to continue following the next one, the follower likely thinks that it is not done following the path. 
	Try decreasing the T-Value and/or Timeout constraint for that path. 
</Callout>