> Source: https://pedropathing.com/docs/pathing/reference/path-builder · Fetched: 2026-07-12

# Pedro Pathing — Path Building API

> Source: https://pedropathing.com/docs/pathing/reference/path-builder · Fetched: 2026-07-12

## Path Builder

### What is PathBuilder?

The `PathBuilder` is a method for combining multiple paths into a single motion of independent or dependent interpolations and decelerations. It allows you to add paths, change how they interact with other paths in the chain, or their movement. This can be through local interpolation—interpolation over a specific path; global interpolation—interpolation over the entire pathchain; local deceleration—deceleration over a path; or global deceleration—deceleration over the path completion of the pathchain. The PathBuilder is able to be transformed into a PathChain with the `.build();` line. All headings are in **radians**—use `Math.toRadians(degrees)` if you’re starting with degrees.

### Usage

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

### Methods

- **addPath(path):** Add a path or curve to your chain.
- **setHeadingInterpolation(HeadingInterpolator):** Control the robot's heading while following paths. (See [Interpolation](/docs/pathing/reference/interpolation))
- **setBrakingStrength(double):** Control deceleration (See [Deceleration](/docs/pathing/reference/deceleration))
- **setTValueConstraint(double):** Control when each path is considered complete (See [Path Constraints](/docs/pathing/reference/constraints) for more on timing.)
- **build():** Convert PathBuilder -> PathChain

Curious how Pedro actually follows these paths? Dive into the [Drive Vector Algorithm](/docs/pathing/reference/drive-vector-algorithm) for the details.

---

> Source: https://pedropathing.com/docs/pathing/reference/beziercurves · Fetched: 2026-07-12

## Bezier Curves

Bézier curves are the main paths that Pedro Pathing follows. A consequence of the Weierstrass Approximation Theorem states that given any target precision, for any continuous curve on the interval $$[0,1],$$ there exists a Bézier curve that approximates this curve to the target precision.

It is typically undesirable to create any Bézier curves with 3 or more control points (excluding the start and end points), as Pedro may have difficulty following the curve in such cases. This may lead to unexpected behavior. Note that inputting the same control point more than once or putting several collinear points in the incorrect order (i.e. like the points (10, 10), (0, 0), (20, 20)) may cause degeneracies in a path. Degenerate paths cannot be followed well by Pedro Pathing.

#### Lazy Generation
BezierCurves can be generated lazily by passing in a `FuturePose` to the constructor, which can be defined with a lambda expression. These curves aren't initialized until the follower is called to follow the path, which can be useful to create paths at runtime based on camera-based readings or the robot's current pose. The advantage here is that these paths can still be defined in `init()` where the other paths are defined. Note that you cannot call methods like `length()` on the path until it is initialized at runtime.

For example, you could use the following segment to generate a `Path` in the `PathBuilder`: `.addPath(new BezierCurve(follower::getPose, new Pose(10, 10)))` which would make the robot travel from its current pose to the pose with coordinates at (10, 10).

#### Parameterization
By mathematical convention, Bézier curves aren't arc-length parameterized, a convention that Pedro follows for simplicity. This means that calling `getPose(0.5)` won't give you the `Pose` that is 50% along the path by distance. Bézier curves are instead parameterized using what we call a t-value, such that `t=0` gives the start of the path and `t=1` gives the end of the path.
Pedro Pathing offers a conversion between t-value and path completion, using the following `BezierCurve` methods: `getPathCompletion(double t)` which outputs a percentage of the distance the robot has traveled, along with `getT(double pathCompletion)` which gives the opposite conversion. The `Path` class also offers the `getDistanceTraveled(double t)` and `getDistanceRemaining(double t)` methods, which can be called without parameters to use the robot's `closestPointTValue.`
Pedro Pathing uses t-value for almost everything, but there a few notable exceptions: global `PathChain` heading interpolation uses path percentage completion instead for linear, custom, and piecewise interpolations, although the regular heading interpolation uses t-value. Furthermore, `ParametricCallbacks` actually use path percentage completion instead of t-value since this aligns more with our general intuition about where an action should be performed along a path.

---

> Source: https://pedropathing.com/docs/pathing/reference/coordinates · Fetched: 2026-07-12

## Coordinates

Pedro Pathing uses a right-hand coordinate system, which is nonstandard to the FTC SDK Standard.

<img
  className="inline-block dark:hidden"
  src="/docs/fieldcoordinates-light.png"
  alt="Pedro Pathing Decode FTC Coordinate System"
/>

<img
  className="hidden dark:inline-block"
  src="/docs/fieldcoordinates-dark.png"
  alt="Pedro Pathing Decode FTC Coordinate System"
/>

As shown, as a robot moves to the right in the image below, x increases. As a robot moves up on the field image, y increases.

A robot facing towards the right side of the image is at a heading of 0 radians (0 degrees), facing up is $\frac{\pi}{2}$ radians (90 degrees), facing left is $\pi$ radians (180 degrees), and facing down is $\frac{3\pi}{2}$ radians (270 degrees).
Thus, counterclockwise rotation is positive rotation, similar to a unit circle.

To convert FTC Coordinates for the Decode game into Pedro's coordinates, first declare a Pose in FTC coordinates (inverted for decode). Let's say you have Pose2D (a class in the FTC SDK) `ftcPose2d` with your coordinates from a camera. You can use
`Pose ftcStandard = PoseConverter.pose2DToPose(ftcPose2d, InvertedFTCCoordinates.INSTANCE);` to convert this to Pedro's `Pose` class. Then, you need to convert to Pedro coordinates using
`ftcStandard.getAsCoordinateSystem(PedroCoordinates.INSTANCE);`

---

> Source: https://pedropathing.com/docs/pathing/reference/constraints · Fetched: 2026-07-12

## Constraints

Constraints are used to determine when a path is considered complete.

There are **five** criteria that all must be met for follower.isBusy() to become false.

#### Timeout
Sets how long, **in milliseconds,** the follower has to correct after stopping, and after this time delay is complete, this criteria to be considered complete.
Increasing it will give the robot more time to correct at the end of the path to improve its accuracy. Decreasing it will reduce the robot's wait time between following paths, but may cause the path following to be slightly more inaccurate.

To set: `path.setTimeoutConstraint(double set)`

#### TValue
Sets the path's parametric end criteria, or how much of the path the robot must follow before it is considered complete. `set` should be a double between 0.0 and 1.0.

To set: `path.setTValueConstraint(double set)`

#### Velocity
Sets the velocity that the robot must be below allowed for this criteria to be considered complete. This is in inches/second.

To set: `path.setVelocityConstraint(double set)`

#### Translational
Sets the maximum amount of translational error allowed for this criteria to be considered complete.
The error has to be under this value.

To set: `path.setTranslationalConstraint(double set)`

#### Heading
Sets the maximum amount of heading error allowed for this criteria to be considered complete.
The error has to be under this value.

To set: `path.setHeadingConstraint(double set)`

> **Tip:**
> If the robot gets stuck after reaching the end of the path and is unable to continue following the next one, the follower likely thinks that it is not done following the path.
> Try decreasing the T-Value and/or Timeout constraint for that path.

---

> Source: https://pedropathing.com/docs/pathing/reference/callbacks · Fetched: 2026-07-12

## Path Callbacks

#### Overview
In Pedro Pathing, you can define custom path callbacks to be run as the robot follows the path. This allows defining and running actions contained inside a `PathChain` object. These callbacks are reset if the chain is followed again.
Callbacks are automatically added to the **last defined path in the builder before the callback is created.** Note that when defining a callback, each Runnable can be defined using a lambda expression, and each method to add a callback can optionally take an additional `int` parameter for the maximum **number of times** the action should run (the default being 1).

#### Built-In Callbacks
Pedro Pathing has a couple built-in callback types:
1. Parametric
    - Executes after a certain percentage (calculated by distance traveled) of the path is exceeded
    - These are the most recommended callback to use
    - Can be added to a chain in the `PathBuilder` using `.addParametricCallback(double percent, Runnable action)` where `percent` is the percent completion of the previous path required to run `action`
2. Temporal
    - Executes a certain amount of time after the robot begins following the path.
    - These are not really recommended as they are inconsistent, given that Pedro's follower isn't based on time and the robot won't be guaranteed to be in the same spot between trials when the action is run.
    - Can be added to a chain in the `PathBuilder` using `.addTemporalCallback(double millis, Runnable action)` such that `action` executes after the `millis` amount has passed since the robot began following this path.
3. Pose
    - Executes after the robot passes the point on a path closest to a given `Pose`
    - The user inputs a `Pose` and the follower evaluates the closest point on the path to this pose. As the robot drives along the path, if it crosses this closest point, the action is run.
    - Can be added to a chain in the `PathBuilder` using `.addPoseCallback(Pose pose, Runnable action, double guess)` where `guess` is an initial guess for the parametric t-value of the closest point on the path to the specified pose. The more accurate this guess is the better the search will go, but a guess like 0.5 should suffice regardless.

#### Custom Callbacks
Callbacks can also be defined by creating a class that implements the `PathCallback` interface. The `isReady()` method should return a boolean value: true if the callback is ready to be run, and false otherwise. The `run()` method is the action to be run, while the optional `initialize()` method can be used to initialize the callback once the robot begins following the path it is attached to. Finally, the `getPathIndex()` returns the index of the `Path` in the `PathChain` that the callback should be attached to.
These callbacks can then be added using the `PathBuilder` method `.addPathCallback(PathCallback callback)`. As before, you can control the maximum number of times a callback is run when adding it to the `PathBuilder` by passing an integer after the callback.

A shortcut to defining a new `PathCallback` in the builder is the use of the following `PathBuilder` method: `.addPathCallback(CallbackCondition isReady, Runnable action)` where two lambda expressions can be passed in such that `action` is run when `isReady` returns true. The `CallbackCondition` interface is functionally the same as a `BooleanSupplier`.

#### Pausing and Resuming Paths
A powerful tool that can be used in conjunction with callbacks is the `pausePathFollowing()` method. This method makes the robot stop moving in th middle of a path, which is useful for performing arm actions. After completing an action, you can call `resumePathFollowing()` for the robot to continue following the path. Note that the `breakFollowing()` method doesn't work in the same way since it resets you to the first `Path` in the PathChain and resets all the `PathCallback` objects associated with the PathChain.

---

> Source: https://pedropathing.com/docs/pathing/reference/pathcomplete · Fetched: 2026-07-12

## Detecting Path Completion

This page serves as a guide for determining when the robot has finished following a `Path` or `PathChain` object and is ready to follow the next one.

In general, the ideal way to determine this is through checking `!follower.isBusy()` which would return true when the path is complete and false otherwise. The method `follower.isBusy()` becomes false after the robot is done correcting at the end of the path.
If you don't want to wait until the follower is done correcting, you can instead use `follower.atParametricEnd()` along with a heading check (i.e., `follower.getHeadingError() < follower.getCurrentPath().getHeadingConstraint()`) to detect that the path is complete.

Sometimes, calls to `!follower.isBusy()` may stay false even when the path appears to be complete. This generally occurs when either the heading or translational end constraints aren't met, preventing the `Follower` instance from thinking the path is complete. This issue typically happens almost every time the autonomous is run, so it becomes easily apparent when this will be a problem. The problem occurs when the `secondaryTranslationalPIDF` or `secondaryHeadingPIDF` aren't powerful enough to correct the robot to the endpoint exactly, but they can't be made stronger without impacting path-following performance.
In such cases, there are two solutions: you can either lower the bar for the `PathConstraints`, which can be done easily in the `PathBuilder`, or use `follower.getVelocity.getMagnitude() < follower.getCurrentPath().getVelocityConstraint()` along with a check to the distance of the robot's current pose to the last point in the path. A similar constraint can be put on heading when necessary, for example, `follower.getAngularVelocity() < 0.055` with a more lenient check on the heading error.

A good autonomous can sometimes even have failsafes on whether the follower thinks the path is completed, for example, tracking the amount of time the robot moves for a set of preloads and having the follower automatically assume the path is completed a given amount of time after the robot begins the path. This can be done with either a basic timer or a `TemporalCallback`.

---

> Source: https://pedropathing.com/docs/pathing/reference/interpolation · Fetched: 2026-07-12

## Interpolation

Pedro Pathing supports many types of interpolation when following paths and/or pathchains.

### Single Path Interpolation
#### Linear Heading Interpolation
This will cause the robot to turn from `startHeading` to `endHeading` while it is following the path.

The `endTime` parameter is a double between 0.0 and 1.0, and it specifies when the robot should finish turning to endHeading. Setting `endTime` to somewhere around 0.8 should work
well for most paths. Setting endTime too low will cause the robot to turn too quickly and create too many oscillations, while setting it too high may lower the robot's end heading accuracy.

To set: `setLinearHeadingInterpolation(double startHeading, double endHeading, double endTime)`

#### Constant Heading Interpolation
Causes the robot to maintain a constant heading while following the path. If the robot starts a path with a different heading compared
to that set in the path, it will turn to that heading before starting the path.

To set: `setConstantHeadingInterpolation(double setHeading)`

#### Tangent Heading Interpolation
Causes the robot to adjust the heading tangential to the path, or adjust the heading to the slope of the
curve.

To set: `setTangentHeadingInterpolation()`

**Warning:** All heading values must be in **radians!** To convert degrees to radians, use `Math.toRadians(degrees)`.

#### Facing Point Interpolation
As the name suggests, this will cause the robot to face a specific point while following the path.

```java
PATH.setHeadingInterpolation(
    HeadingInterpolator.facingPoint()
)
```
#### Piecewise Interpolation
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
#### Custom Interpolation
If users wish, they can create their own interpolation by implementing the `HeadingInterpolator` interface and the interpolate method.

#### Reverse
On any Heading Interpolator, you can call `.reversed()` to reverse the direction of the interpolation.
For Linear, it would take the longer route around, for tangent it would drive backwards along the tangent, and for facingPoint it would face directly away from the point.

### PathChain Interpolation
To interpolate over all of the paths in a pathchain as if they were one connected path, users can use `.setGlobalHeadingInterpolation(HeadingInterpolator)` on the pathchain object.
Thus, you can use all of the above options globally on PathChains, as they all implement the HeadingInterpolator interface.

