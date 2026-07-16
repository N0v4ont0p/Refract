> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/testing-your-tree.md · Fetched: 2026-07-16
> Note: fetched at HEAD (998011a), not the v0.1.0 release tag — TickTree is pre-alpha and actively changing; per G5's own staleness discipline, re-fetch and re-stamp before trusting this against a materially newer commit.

# Testing your tree

This is TickTree's quiet superpower: because `ticktree-core` has **zero Android/FTC-SDK
dependency**, you can unit-test your entire match strategy **on your laptop** — no robot, no
emulator, no Driver Station. You build the same tree you'd run on the robot, tick it in a loop, and
assert what it decides. None of the other FTC libraries can do this, because their decision logic is
tangled up with hardware.

!!! info "Setup"
    Put your strategy in terms of `ticktree-core` (build the tree from `TickTree.*` factories with
    your leaf bodies as lambdas), and add JUnit 5 to your test source set
    (`testImplementation 'org.junit.jupiter:junit-jupiter:5.10.2'`). The examples below use plain
    JUnit 5 assertions so they work with nothing else added.

## You don't need special fixtures — control the leaf bodies

To test a tree, you don't replace nodes; you make the **leaf bodies return values you control**. A
leaf is just `action("name", () -> someStatus)` — so back it with a mutable holder your test writes:

```java
import static io.github.n0v4ont0p.ticktree.TickTree.*;
import io.github.n0v4ont0p.ticktree.*;
import static io.github.n0v4ont0p.ticktree.Status.*;
import static org.junit.jupiter.api.Assertions.*;

@Test
void driverOverridePreemptsAutoScore() {
    boolean[] driverPressingA = {false};
    Status[] scoreResult = {RUNNING};

    Blackboard bb = new Blackboard();
    BehaviorTree tree = TickTree.tree("teleop").root(
        reactiveSelector(
            guard(() -> driverPressingA[0], action("driverControl", () -> RUNNING)),
            action("score", () -> scoreResult[0])
        )
    ).build(bb);

    assertEquals(RUNNING, tree.tick());                     // scoring
    driverPressingA[0] = true;
    assertEquals(RUNNING, tree.tick());                     // driver took over (higher priority)
    assertEquals("teleop ▸ driverControl [RUNNING]", TreeVisitor.activePath(tree));
}
```

That's the whole technique for most tests. You do **not** need — and should not depend on —
`ticktree-core`'s own internal test fixtures (`ScriptedLeaf`, `MutableLeaf`, `FakeClock`); those are
the engine's private test code, not published API. When you need a reusable helper, it's tiny —
write your own (below).

## The one lesson that will confuse you first: scripted vs. mutable

The first time you write a fake that returns "SUCCESS, then FAILURE on the next tick," you may see it
**reset unexpectedly**. That is *correct* behavior, and understanding why saves you an hour.

TickTree re-enters a node on the tick after it returns a terminal status (that's how a node runs
"fresh" the next time it's reached). So a fake that advances an internal script only makes sense for a
node that **stays `RUNNING`** across those ticks (one activation) — for example, modeling a single
multi-tick action:

```java
// A one-activation action: RUNNING, RUNNING, then SUCCESS. Fine — it never re-enters mid-script.
Status[] script = { RUNNING, RUNNING, SUCCESS };
int[] i = {0};
Node driveToPoint = action("drive", () -> script[Math.min(i[0]++, script.length - 1)]);
```

But a **guard or condition** returns a terminal status *every* tick, so it re-enters every tick — an
internal script would reset to the start each time and never advance. Model anything that changes
**across activations** (a sensor that flips, a match timer) with **external mutable state** the test
controls, not an internal script:

```java
// A guard whose value changes independently of activation → external holder, not a script.
boolean[] hasPiece = {true};
Node guarded = guard(() -> hasPiece[0], driveToGoal);
// ... tick a few times ...
hasPiece[0] = false;   // now the guard fails and halts driveToGoal on the next tick
```

Rule of thumb: **scripted sequence → a single multi-tick action; external mutable holder → a
condition/guard that flips.** (This exact distinction bit the library's own development more than
once — it's real, and it's the engine working as designed, not a bug to route around.)

## Time-based decorators: use a FakeClock, never sleep

`timeout`, `cooldown`, `delay`, and `rateLimit` read time through a `TimeSource`. Every one of those
factories has an overload that takes an explicit `TimeSource`, so your test injects a fake clock and
**advances it by hand** — tests stay instant and deterministic, and you never call `Thread.sleep`.

The fake clock is six lines — copy it into your test sources:

```java
final class FakeClock implements TimeSource {
    private long nanos;
    @Override public long nowNanos() { return nanos; }
    void advance(long deltaNanos) { nanos += deltaNanos; }
}
```

Testing a `Timeout`-wrapped action:

```java
@Test
void driveTimesOutAfterTwoSeconds() {
    FakeClock clock = new FakeClock();
    Blackboard bb = new Blackboard();
    // A drive that never finishes on its own:
    BehaviorTree tree = TickTree.tree("t").root(
        timeout(seconds(2), clock, action("drive", () -> RUNNING))
    ).build(bb);

    assertEquals(RUNNING, tree.tick());     // t = 0
    clock.advance(seconds(1));
    assertEquals(RUNNING, tree.tick());     // t = 1 s, still within timeout
    clock.advance(seconds(2));
    assertEquals(FAILURE, tree.tick());     // t = 3 s > 2 s → times out (and the drive is halted)
}
```

## Asserting across a sequence of ticks

The pattern for any stateful tree: build once, then tick and assert step by step, mutating your
controllable holders between ticks to simulate the world changing.

```java
@Test
void autonomousScoresTheDetectedSide() {
    Blackboard bb = new Blackboard();
    Key<String> element = Key.of("element", String.class);
    int[] scoreLeftTicks = {0};

    BehaviorTree auto = TickTree.tree("auto").root(
        sequence(
            action("scan", b -> { b.set(element, "LEFT"); return SUCCESS; }),
            selector(
                guard(b -> "LEFT".equals(b.get(element)),
                    action("scoreLeft", () -> ++scoreLeftTicks[0] >= 2 ? SUCCESS : RUNNING)),
                action("scoreRight", () -> SUCCESS)
            )
        )
    ).build(bb);

    assertEquals(RUNNING, auto.tick());   // scanned LEFT, scoring left (tick 1 of 2)
    assertEquals(SUCCESS, auto.tick());   // scoring left finished
    assertEquals("LEFT", bb.get(element)); // the scan wrote the blackboard
    assertEquals(2, scoreLeftTicks[0]);   // scoreRight never ran
}
```

Run it like any JUnit test — green means your strategy behaves, and you found out on your laptop
instead of on the field.
