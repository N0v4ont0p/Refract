> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/path-builder.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Path Builder
description: Using the PathBuilder
---

## What is PathBuilder?

The `PathBuilder` is a method for combining multiple paths into a single motion of independent or dependent interpolations and decelerations. It allows you to add paths, change how they interact with other paths in the chain, or their movement. This can be through local interpolation—interpolation over a specific path; global interpolation—interpolation over the entire pathchain; local deceleration—deceleration over a path; or global deceleration—deceleration over the path completion of the pathchain. The PathBuilder is able to be transformed into a PathChain with the `.build();` line. All headings are in **radians**—use `Math.toRadians(degrees)` if you’re starting with degrees.

## Usage

Let’s say you want your robot to go from a scoring position to a pickup, then back again, turning smoothly as it moves from one heading to another. Let's assume that all of our poses are defined:

```java
pathChain = follower.pathBuilder()
    .addPath(new BezierLine(scorePose, pickup1Pose))
    .setLinearHeadingInterpolation(scorePose.getHeading(), pickup1Pose.getHeading())
    .addPath(new BezierLine(pickup1Pose, scorePose))
    .setLinearHeadingInterpolation(pickup1Pose.getHeading(), scorePose.getHeading())
    .build();

follower.followPath(pathChain);
```

## Methods

- **addPath(path):** Add a path or curve to your chain.
- **setHeadingInterpolation(HeadingInterpolator):** Control the robot's heading while following paths. (See [Interpolation](/docs/pathing/reference/interpolation)) 
- **setBrakingStrength(double):** Control deceleration (See [Deceleration](/docs/pathing/reference/deceleration))
- **setTValueConstraint(double):** Control when each path is considered complete (See [Path Constraints](/docs/pathing/reference/constraints) for more on timing.)
- **build():** Convert PathBuilder -> PathChain

Curious how Pedro actually follows these paths? Dive into the [Drive Vector Algorithm](/docs/pathing/reference/drive-vector-algorithm) for the details.
