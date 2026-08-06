> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/pathcomplete.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Detecting Path Completion
---

This page serves as a guide for determining when the robot has finished following a `Path` or `PathChain` object and is ready to follow the next one.

In general, the ideal way to determine this is through checking `!follower.isBusy()` which would return true when the path is complete and false otherwise. The method `follower.isBusy()` becomes false after the robot is done correcting at the end of the path.
If you don't want to wait until the follower is done correcting, you can instead use `follower.atParametricEnd()` along with a heading check (i.e., `follower.getHeadingError() < follower.getCurrentPath().getHeadingConstraint()`) to detect that the path is complete.

Sometimes, calls to `!follower.isBusy()` may stay false even when the path appears to be complete. This generally occurs when either the heading or translational end constraints aren't met, preventing the `Follower` instance from thinking the path is complete. This issue typically happens almost every time the autonomous is run, so it becomes easily apparent when this will be a problem. The problem occurs when the `secondaryTranslationalPIDF` or `secondaryHeadingPIDF` aren't powerful enough to correct the robot to the endpoint exactly, but they can't be made stronger without impacting path-following performance.
In such cases, there are two solutions: you can either lower the bar for the `PathConstraints`, which can be done easily in the `PathBuilder`, or use `follower.getVelocity.getMagnitude() < follower.getCurrentPath().getVelocityConstraint()` along with a check to the distance of the robot's current pose to the last point in the path. A similar constraint can be put on heading when necessary, for example, `follower.getAngularVelocity() < 0.055` with a more lenient check on the heading error.

A good autonomous can sometimes even have failsafes on whether the follower thinks the path is completed, for example, tracking the amount of time the robot moves for a set of preloads and having the follower automatically assume the path is completed a given amount of time after the robot begins the path. This can be done with either a basic timer or a `TemporalCallback`.
