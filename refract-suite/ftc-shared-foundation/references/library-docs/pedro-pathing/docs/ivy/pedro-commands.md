> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/pedro-commands.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Pedro Commands
---

Ivy includes built-in commands for controlling your robot's movement using
[Pedro Pathing](https://pedropathing.com). To use them, add the following
static import:

```java
import static com.pedropathing.ivy.pedro.PedroCommands.*;
```

All Pedro commands take a `Follower` as their first argument. Usually your Follower
is one created from your `Constants` file's `createFollower()` method.

## Follow

Makes the robot follow a `PathChain`. The command finishes when the follower
is no longer busy (i.e. the path is complete).

```java
Command goToBasket = follow(follower, basketPath);
```

You can optionally specify whether the robot should hold its position at the
end of the path, and a maximum power between 0 and 1:

```java
Command goToBasket = follow(follower, pickupCloseSpikemark, true);          // hold at end
Command goToBasket = follow(follower, pickupCloseSpikemark, 0.5);           // cap max power at half
Command goToBasket = follow(follower, pickupCloseSpikemark, true, 0.5);     // both
```

If you don't pass `holdEnd`, it defaults to your follower's
`automaticHoldEnd` setting. If you don't pass `maxPower`, it defaults to
the follower's current max power.

## Hold

Makes the robot hold a position. The command finishes when the robot is
within tolerance of the target (based on translational and heading error).

To hold the robot's current position:

```java
Command stayHere = hold(follower);
```

To hold a specific pose:

```java
Command holdAtBasket = hold(follower, new Pose(50, 30, Math.toRadians(90)));
```

You can also pass custom `PathConstraints` to control how tight the
completion tolerance is:

```java
Command preciseHold = hold(follower, targetPose, new PathConstraints(
    0.995,  // tValueConstraint
    100     // timeoutConstraint (ms)
));
```

## Turn To

Makes the robot turn in place to a specified heading (in radians). The
command finishes when the follower is no longer busy.

```java
Command faceForward = turnTo(follower, Math.toRadians(0));
Command faceLeft = turnTo(follower, Math.toRadians(90));
```

As with `hold`, you can pass custom `PathConstraints`:

```java
Command preciseTurn = turnTo(follower, Math.toRadians(180), customConstraints);
```

## Composing Pedro Commands

Since Pedro commands are regular Ivy commands, you can compose them with
everything else. For example:

```java
Command auto = sequential(
    follow(follower, shootPreloads),
    Shooter.shoot(), // the shoot method here would be a command
    instant(() -> claw.open()),
    parallel(
        follow(follower, pickupCloseSpikemark),
        instant(() -> intake.activate())
    )
/* ... */
);
```
