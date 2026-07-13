> Source: https://rr.brott.dev/docs/v1-0/new-features/, https://rr.brott.dev/docs/v1-0/modules/, https://rr.brott.dev/docs/v1-0/guides/path-following/ · Fetched: 2026-07-12

# Road Runner — Core Concepts (v1.0.x)

**LEGACY REFERENCE.** RoadRunner 1.0.x. Not the primary recommended
path-following library in this project anymore.

## What changed in 1.0 (vs 0.5.x)

RoadRunner 1.0 is a ground-up redesign of the quickstart and API, aimed at
better calibration results in less time and incorporating community-learned
best practices — including first-class support for dead wheel odometry. The
underlying math is the same as 0.5.x, but the API and quickstart changed
enough that 1.0.x is **not backwards compatible** with 0.5.x.

Key changes:

- **Path continuity is no longer an exception.** In 0.5.x, violating path
  continuity threw an error. In 1.0.x, builders instead produce a *sequence*
  of paths/trajectories, auto-splitting where continuity would otherwise be
  violated.
- **Asymmetric motion profiles.** `ProfileAccelerationConstraint` now takes
  separate min/max acceleration values, so acceleration and deceleration
  limits can differ.
- **Trajectory cancellation.** `Trajectory#cancel()` brings the robot to a
  smooth stop on the path while still respecting motion constraints, instead
  of an abrupt halt.
- **Ramsete replaces tank PIDVA.** A unit-adjusted Ramsete controller is now
  the default trajectory-following strategy (aligned with WPILib), and
  reportedly performs better than the old default with less tuning.

## Module layout

RoadRunner is split into small modules, on the principle that "the fewer
dependencies a module has, the more places and situations it can be used":

- **`core`** — the foundational math/planning module. No FTC SDK
  dependency, so it can run on non-Android systems too.
- **`actions`** — builds on `core`; adds the `Action` execution model used
  for autonomous routines (see `trajectories.md`).
- **`ftc`** — the FTC-specific integration layer. Depends on `actions`,
  `core`, the FTC SDK, and FTC Dashboard.
- **`dashboard` (core)** — telemetry/visualization, usable independently by
  other modules. RoadRunner core and FTC Dashboard don't depend on each
  other.
- **MeepMeep** — the trajectory visualizer/simulator; depends on `actions`
  and `core` only, so it can preview paths without a full FTC project.
- **road-runner-quickstart** — the batteries-included FTC template, pulling
  in the full stack.

## Path following (how the controller tracks a trajectory)

RoadRunner offers two conceptually different ways to track a path:

- **Trajectory-based (time-scheduled) following** — the traditional
  approach: a stopwatch drives progress along a time-parameterized
  trajectory. Simple termination criterion, but the feedback controller has
  to keep acceleration headroom in reserve and the robot can't get ahead of
  its schedule even if it's tracking well.
- **Path-following without a time schedule** — instead of a clock, the
  controller finds the closest point on the path to the robot's current
  position and drives toward that. Described as "similar to pure pursuit,"
  except there's no lookahead distance — it aims for higher-accuracy path
  tracking rather than just pushing toward a goal point.

### `HolonomicController`

The core feedback controller for holonomic (mecanum) drives:

```kotlin
fun compute(
    targetPose: Pose2dDual<Time>,
    actualPose: Pose2d,
    actualVelActual: PoseVelocity2d,
): PoseVelocity2dDual<Time>
```

**Getting the target pose off the path:**

1. `project(path, actualPose, displacementGuess)` — finds the path
   displacement closest to the robot's current pose.
2. `path.get(displacement, 3)` — gets the target pose at that displacement,
   including up to 2nd-order derivatives.
3. Reparametrize from arclength-based derivatives to time-based derivatives:
   ```kotlin
   fun <NewParam> reparam(oldParam: DualNum<NewParam>) =
       Pose2dDual(position.reparam(oldParam), heading.reparam(oldParam))
   ```
4. Evaluate a `DisplacementProfile` at that displacement to get a
   `DualNum<Time>`.

**Feedback command** (position + velocity error, combined with independent
axial/lateral/heading gains):

```kotlin
val error = targetPose.value().minusExp(actualPose)

val feedbackCommand = PoseVelocity2d(
    Vector2d(
        axialPosGain * error.position.x,
        lateralPosGain * error.position.y,
    ),
    headingGain * error.heading.log(),
) +
PoseVelocity2d(
    Vector2d(
        axialVelGain * velErrorActual.linearVel.x,
        lateralVelGain * velErrorActual.linearVel.y,
    ),
    headingVelGain * velErrorActual.angVel,
)
```

The controller then picks the maximum path displacement velocity that still
satisfies each motor's voltage constraint, assuming `kA` (acceleration
feedforward) is zero for this part of the computation.
