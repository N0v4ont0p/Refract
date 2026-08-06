> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/beziercurves.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Bezier Curves
---

Bézier curves are the main paths that Pedro Pathing follows. A consequence of the Weierstrass Approximation Theorem states that given any target precision, for any continuous curve on the interval $$[0,1],$$ there exists a Bézier curve that approximates this curve to the target precision.

It is typically undesirable to create any Bézier curves with 3 or more control points (excluding the start and end points), as Pedro may have difficulty following the curve in such cases. This may lead to unexpected behavior. Note that inputting the same control point more than once or putting several collinear points in the incorrect order (i.e. like the points (10, 10), (0, 0), (20, 20)) may cause degeneracies in a path. Degenerate paths cannot be followed well by Pedro Pathing.

### Lazy Generation
BezierCurves can be generated lazily by passing in a `FuturePose` to the constructor, which can be defined with a lambda expression. These curves aren't initialized until the follower is called to follow the path, which can be useful to create paths at runtime based on camera-based readings or the robot's current pose. The advantage here is that these paths can still be defined in `init()` where the other paths are defined. Note that you cannot call methods like `length()` on the path until it is initialized at runtime.

For example, you could use the following segment to generate a `Path` in the `PathBuilder`: `.addPath(new BezierCurve(follower::getPose, new Pose(10, 10)))` which would make the robot travel from its current pose to the pose with coordinates at (10, 10).

### Parameterization
By mathematical convention, Bézier curves aren't arc-length parameterized, a convention that Pedro follows for simplicity. This means that calling `getPose(0.5)` won't give you the `Pose` that is 50% along the path by distance. Bézier curves are instead parameterized using what we call a t-value, such that `t=0` gives the start of the path and `t=1` gives the end of the path.
Pedro Pathing offers a conversion between t-value and path completion, using the following `BezierCurve` methods: `getPathCompletion(double t)` which outputs a percentage of the distance the robot has traveled, along with `getT(double pathCompletion)` which gives the opposite conversion. The `Path` class also offers the `getDistanceTraveled(double t)` and `getDistanceRemaining(double t)` methods, which can be called without parameters to use the robot's `closestPointTValue.`
Pedro Pathing uses t-value for almost everything, but there a few notable exceptions: global `PathChain` heading interpolation uses path percentage completion instead for linear, custom, and piecewise interpolations, although the regular heading interpolation uses t-value. Furthermore, `ParametricCallbacks` actually use path percentage completion instead of t-value since this aligns more with our general intuition about where an action should be performed along a path.
