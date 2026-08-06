> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/interpolation.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Interpolation
---

Pedro Pathing supports many types of interpolation when following paths and/or pathchains.

## Single Path Interpolation
### Linear Heading Interpolation
This will cause the robot to turn from `startHeading` to `endHeading` while it is following the path. 
	
The `endTime` parameter is a double between 0.0 and 1.0, and it specifies when the robot should finish turning to endHeading. Setting `endTime` to somewhere around 0.8 should work 
well for most paths. Setting endTime too low will cause the robot to turn too quickly and create too many oscillations, while setting it too high may lower the robot's end heading accuracy. 

To set: `setLinearHeadingInterpolation(double startHeading, double endHeading, double endTime)`
	
### Constant Heading Interpolation
Causes the robot to maintain a constant heading while following the path. If the robot starts a path with a different heading compared
to that set in the path, it will turn to that heading before starting the path.

To set: `setConstantHeadingInterpolation(double setHeading)` 

### Tangent Heading Interpolation 
Causes the robot to adjust the heading tangential to the path, or adjust the heading to the slope of the
curve.

To set: `setTangentHeadingInterpolation()` 
	
**Warning:** All heading values must be in **radians!** To convert degrees to radians, use `Math.toRadians(degrees)`. 


### Facing Point Interpolation
As the name suggests, this will cause the robot to face a specific point while following the path.

```java
PATH.setHeadingInterpolation(
    HeadingInterpolator.facingPoint()
)
```
### Piecewise Interpolation
Like a piecewise function, this will allow you to set different types of interpolation for different segments.
These are defined by tvalue, where 0 is the start and 1 is the end.

An example of this is shown below on a single path.

```java
PATH.setHeadingInterpolation(
    HeadingInterpolator.piecewise(
                new HeadingInterpolator.PiecewiseNode(
                        0,
                        .3,
                        HeadingInterpolator.linear(0, Math.toRadians(180))
                ),
                new HeadingInterpolator.PiecewiseNode(
                        .3,
                        .6,
                        HeadingInterpolator.facingPoint(72, 72)
                ),
                new HeadingInterpolator.PiecewiseNode(
                        .6,
                        .7,
                        HeadingInterpolator.reversedLinear(
                                Math.toRadians(180), 0
                        )
                ),
                new HeadingInterpolator.PiecewiseNode(
                        .7,
                        1,
                        HeadingInterpolator.tangent
                )
        );
                ```
### Custom Interpolation
If users wish, they can create their own interpolation by implementing the `HeadingInterpolator` interface and the interpolate method.

### Reverse
On any Heading Interpolator, you can call `.reversed()` to reverse the direction of the interpolation.  
For Linear, it would take the longer route around, for tangent it would drive backwards along the tangent, and for facingPoint it would face directly away from the point.

## PathChain Interpolation
To interpolate over all of the paths in a pathchain as if they were one connected path, users can use `.setGlobalHeadingInterpolation(HeadingInterpolator)` on the pathchain object.  
Thus, you can use all of the above options globally on PathChains, as they all implement the HeadingInterpolator interface.
