> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/pathing/trajectory/manipulating-trajectories.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

# Manipulating Trajectories

Once a trajectory has been generated, you can retrieve information from it using certain methods. These methods will be useful when writing code to follow these trajectories.

## Getting the Total Duration of the Trajectory

Because all trajectories have timestamps at each point, the amount of time it should take for a robot to traverse the entire trajectory is predetermined. The`getTotalTimeSeconds()`method can be used to determine the time it takes to traverse the trajectory.

```java
// Get the total time of the trajectory in seconds
double duration = trajectory.getTotalTimeSeconds();
```

## Sampling the Trajectory

The trajectory can be sampled at various timesteps to get the pose, velocity, and acceleration at that point. The `sample(double timeSeconds)` method can be used to sample the trajectory at any timestep. The parameter refers to the amount of time passed since 0 seconds \(the starting point of the trajectory\).

```java
// Sample the trajectory at 1.2 seconds. This represents where the robot
// should be after 1.2 seconds of traversal.
Trajectory.State point = trajectory.sample(1.2);
```

The sample has several pieces of information about the sample point:

* `t`: The time elapsed from the beginning of the trajectory up to the sample point.
* `velocity`: The velocity at the sample point.
* `acceleration`: The acceleration at the sample point.
* `pose`: The pose \(x, y, heading\) at the sample point.
* `curvature`: The curvature \(rate of change of heading with respect to distance along the trajectory\) at the sample point.

Note: The angular velocity at the sample point can be calculated by multiplying the velocity by the curvature.

