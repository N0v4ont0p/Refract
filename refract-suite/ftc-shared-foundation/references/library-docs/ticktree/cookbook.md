> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/cookbook.md · Fetched: 2026-07-16
> Note: fetched at HEAD (998011a), not the v0.1.0 release tag — TickTree is pre-alpha and actively changing; per G5's own staleness discipline, re-fetch and re-stamp before trusting this against a materially newer commit.

# Cookbook

Complete, copy-pasteable recipes for common problems. For full API coverage of every node, see the
[node reference](node-reference.md) — this page is "how do I actually accomplish X."

!!! info "Imports"
    Every snippet below assumes:
    ```java
    import static io.github.n0v4ont0p.ticktree.TickTree.*;
    import static io.github.n0v4ont0p.ticktree.Status.*;
    import io.github.n0v4ont0p.ticktree.*;   // Blackboard, Key, Node, StatefulAction, ...
    ```

## Priority arbitration with driver override

The flagship TeleOp pattern: auto-score while the driver isn't overriding, endgame park preempts
everything, otherwise hand control back to the driver.

```java
BehaviorTree tree = TickTree.tree("teleop").root(
    reactiveSelector(                                   // re-checked every loop; higher branch wins
        guard(() -> matchTimer.inEndgame(),             // highest priority: preempts everything below
            sequence(
                action("driveToPark", parkAction),
                action("engageHang",  hangAction)
            )),
        guard(() -> !gamepad1.a,                         // next: auto-score, unless the driver overrides
            reactiveSequence(
                condition("hasGamePiece", intake::hasPiece),   // re-checked — bail if the piece is lost
                action("alignToGoal", alignAction),
                action("score",       scoreAction)
            )),
        action("driverControl", () -> { drive.arcade(gamepad1); return RUNNING; })   // fallback
    )
).build(blackboard);
```

## Conditional autonomous branching on a detected element

Scan once, then branch on what was seen, with a timeout safety net so autonomous never stalls.

```java
enum Element { LEFT, CENTER, RIGHT }
static final Key<Element> DETECTED = Key.of("element", Element.class);

BehaviorTree auto = TickTree.tree("auto").root(
    sequence(
        action("scanElement", bb -> { bb.set(DETECTED, vision.scan()); return SUCCESS; }),
        selector(
            guard(bb -> bb.get(DETECTED) == Element.LEFT,   action("scoreLeft",   scoreLeftAction)),
            guard(bb -> bb.get(DETECTED) == Element.CENTER, action("scoreCenter", scoreCenterAction)),
            action("scoreRight", scoreRightAction)          // default: RIGHT or scan failed
        ),
        timeout(seconds(5), action("park", parkAction))
    )
).build(blackboard);
```

## Wrapping a path follower (Road Runner / Pedro Pathing) as a leaf

TickTree doesn't depend on either library — it just needs *something* that reports whether a
trajectory is still running. Wrap your follower behind a tiny interface and adapt it:

```java
// A stand-in for whichever follower you use — Road Runner's TrajectorySequenceRunner /
// Pedro's Follower both expose an equivalent "am I still driving?" signal. Adapt to yours.
interface TrajectoryFollower {
    boolean isBusy();
    void stop();
}

Node driveTrajectory(TrajectoryFollower follower) {
    return action("driveTrajectory", new StatefulAction() {
        @Override public void onStart(Blackboard bb) { /* follower.followTrajectory(traj) already started elsewhere, or start it here */ }
        @Override public Status onRunning(Blackboard bb) {
            return follower.isBusy() ? Status.RUNNING : Status.SUCCESS;
        }
        @Override public void onHalt(Blackboard bb) { follower.stop(); }   // preemption stops the robot
    });
}
```

Now `driveTrajectory(myFollower)` is a normal leaf — put it under a `guard` or a `reactiveSelector`
and it gets preempted (and the follower stopped) exactly like any other action. This is the concrete
shape of the orthogonality argument: Road Runner / Pedro answer *how to drive*; the leaf above lets
TickTree answer *whether it should still be driving*.

## Retry a flaky action, then fall back to a different strategy

```java
selector(
    retry(3, action("grabSample", grabAction)),      // up to 3 attempts
    action("grabFallback", grabFallbackAction)        // give up and try something else
)
```

## Timeout-guarded action with a fallback

```java
selector(
    timeout(seconds(3), action("driveToWall", driveAction)),   // fails if it takes > 3 s
    action("backOffAndRetryLater", backOffAction)                // fallback on timeout
)
```

## Sharing sensor state via the Blackboard (no direct coupling)

A `Condition` and an `Action` that never reference each other directly — both just read/write a
shared key.

```java
static final Key<Double> DISTANCE_TO_GOAL = Key.of("vision.distanceToGoal", Double.class);

Node updateDistance = action("readDistance", bb -> {
    bb.set(DISTANCE_TO_GOAL, vision.distanceToGoal());
    return Status.SUCCESS;
});

// Anything downstream just reads the key — no reference to updateDistance or `vision` at all.
Node driveIn = guard(bb -> bb.getOrDefault(DISTANCE_TO_GOAL, Double.MAX_VALUE) < 12.0,
    action("driveIn", driveInAction));

// Composed in a reactive sequence so the distance is refreshed every tick before the guard reads it:
reactiveSequence(updateDistance, driveIn);
```

`updateDistance` and `driveIn`'s guard never hold a reference to each other or to `vision` — they
only share the `DISTANCE_TO_GOAL` key, so either can be reused, reordered, or tested independently.

## Active-path telemetry on the Driver Station

Show what the tree is doing right now, live, every loop.

```java
@Override public void loop() {
    tree.tick();
    TreeTelemetry.addActivePath(telemetry, "Tree", tree);   // e.g. "teleop ▸ autoScore ▸ alignToGoal [RUNNING]"
    telemetry.update();
}
```

If you want the raw string yourself (for a custom overlay, logging, etc.), call
`TreeVisitor.activePath(tree)` directly, or `TreeVisitor.snapshot(tree)` for the full structured
tree (name/type/status/active per node).
