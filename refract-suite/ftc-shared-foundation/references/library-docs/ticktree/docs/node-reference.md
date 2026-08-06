> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/node-reference.md · Fetched: 2026-08-06 · Ref: main @ 998011a20399
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

# Node reference

Every node type, with a fixed format: **what it is**, **semantics**, **halt behavior** (where
relevant), and a **minimal example**. All factories are static methods on `TickTree`. Examples below
assume both `import static io.github.n0v4ont0p.ticktree.TickTree.*;` (the factories) and
`import static io.github.n0v4ont0p.ticktree.Status.*;` (`SUCCESS`/`FAILURE`/`RUNNING`) — `Status` is a
sibling enum, not a member of `TickTree`, so both imports are needed.

Composites take children as varargs (`Node...`); a composite with zero children throws at
construction. Every node accepts an optional name where shown (leaves and `subtree`); composites and
decorators report a fixed type name for telemetry.

---

## Composites

Composites combine children. The **memory vs reactive** distinction is explained in
[core concepts](core-concepts.md#memory-vs-reactive-the-concept-to-get-right).

### `sequence(children…)` — AND, with memory

- **Semantics:** ticks children left-to-right, **resuming at the remembered `RUNNING` child**.
  Returns `FAILURE` on the first child that fails, `RUNNING` while a child runs, `SUCCESS` only when
  all children have succeeded. Earlier children are *not* re-checked once passed.
- **Halt:** halts the currently-running child.

```java
sequence(
    action("closeGripper", () -> { gripper.close(); return SUCCESS; }),
    action("lift",         () -> lift.atTop() ? SUCCESS : RUNNING)
)
```

### `reactiveSequence(children…)` — AND, reactive

- **Semantics:** same AND propagation, but **re-ticks from the first child every tick**, so earlier
  children (guards) are re-evaluated continuously.
- **Halt:** if a guard flips and a *different* child (or none) ends up running this tick, the
  previously-running child is **halted** first.

```java
reactiveSequence(
    condition("hasGamePiece", intake::hasPiece),   // re-checked every tick
    action("driveToGoal", driveAction),
    action("score",       scoreAction)
)
```

### `selector(children…)` — OR, with memory

- **Semantics:** ticks children left-to-right, resuming at the `RUNNING` child. Returns `SUCCESS` on
  the first child that succeeds, `RUNNING` while a child runs, `FAILURE` only if all children fail.
- **Halt:** halts the currently-running child.

### `reactiveSelector(children…)` — OR, reactive (priority arbitration)

- **Semantics:** re-ticks from the highest-priority child every tick. Returns `SUCCESS` on the first
  child that succeeds, `RUNNING` on the first that runs, `FAILURE` only if all fail. **This is the
  preemption node:** when a higher-priority child becomes viable, the running lower-priority child is
  halted and the higher one takes over.
- **Halt:** halts the previously-running child when priority shifts.

```java
reactiveSelector(
    guard(() -> matchTimer.inEndgame(), parkAndHang),   // preempts everything below
    guard(() -> !driverOverriding,      autoScore),
    action("driverControl", driverControlAction)        // fallback
)
```

### `parallel(successPolicy, failurePolicy, children…)` — run all at once

- **Semantics:** ticks **all** still-running children every tick (not short-circuit), and arbitrates
  on two independent thresholds, each `REQUIRE_ALL` or `REQUIRE_ONE` (`Parallel.Policy`):

    | successPolicy | failurePolicy | Behavior |
    |---|---|---|
    | `REQUIRE_ALL` | `REQUIRE_ONE` | Succeeds only if **all** succeed; fails as soon as **any** fails. |
    | `REQUIRE_ALL` | `REQUIRE_ALL` | Succeeds if all succeed; fails only if all fail; else `RUNNING`. |
    | `REQUIRE_ONE` | `REQUIRE_ONE` | First child to finish decides (a race). |
    | `REQUIRE_ONE` | `REQUIRE_ALL` | Succeeds as soon as **any** succeeds; fails only if all fail. |

    Once a child returns a terminal status it is **not ticked again** that activation (it is held at
    its result). If both thresholds are met on the same tick, **success wins**.
- **Halt:** on the terminal decision, every still-`RUNNING` child is halted before returning.
- **Convenience:** `parallelAll(children…)` = `REQUIRE_ALL`/`REQUIRE_ONE` ("all must succeed, abort
  on any failure"); `parallelRace(children…)` = `REQUIRE_ONE`/`REQUIRE_ONE` ("first to finish wins").

```java
// Raise the lift and spin up the shooter together; done when both succeed:
parallelAll(action("raiseLift", raise), action("spinUp", spin))
```

---

## Decorators

Each wraps exactly one child. Unless noted, a decorator's `halt` delegates to its child (a safe
no-op if the child isn't running).

### `inverter(child)`
Swaps the child's terminal status: `SUCCESS`↔`FAILURE`. `RUNNING` passes through unchanged.

### `forceSuccess(child)`
Maps the child's terminal status to `SUCCESS`; `RUNNING` passes through. ("Try it, but don't let it
fail the parent.")

### `forceFailure(child)`
Maps the child's terminal status to `FAILURE`; `RUNNING` passes through.

### `repeat(times, child)`
Runs the child `times` times; `RUNNING` while iterating; `SUCCESS` after that many successes; a child
`FAILURE` aborts to `FAILURE`. Re-runs the child fresh on each iteration (one child tick per decorator
tick — it can never busy-loop within a tick). `times` must be ≥ 1.

### `repeatForever(child)`
Re-runs the child indefinitely; a child `SUCCESS` just restarts it. Only a child `FAILURE` (or an
external halt) exits.

### `retry(times, child)`
Re-runs the child on `FAILURE`, up to `times` attempts; a `SUCCESS` short-circuits to `SUCCESS`;
exhausting all attempts returns `FAILURE`. `times` must be ≥ 1.

```java
retry(3, action("grabSample", grab))   // try up to 3 times
```

### `timeout(durationNanos, child)` — time-limited
- **Semantics:** passes the child's status through until `durationNanos` elapses from this
  activation; on the first tick where elapsed **exceeds** the duration, returns `FAILURE` — even if
  the child would have returned `RUNNING`.
- **Halt:** **halts the child** on expiry.
- Use the `seconds(...)` / `millis(...)` helpers for the duration. A second overload takes an explicit
  `TimeSource` for deterministic tests: `timeout(seconds(5), clock, child)`.

```java
timeout(seconds(3), action("driveToWall", drive))   // fail if it takes over 3 s
```

### `cooldown(durationNanos, child)`
After the child returns a terminal status, further ticks return `FAILURE` (without ticking the child)
until `durationNanos` has elapsed since that completion; then the child is runnable again. Explicit
`TimeSource` overload available.

### `rateLimit(hz, child)`
Ticks the child at most `hz` times per second; on throttled (skipped) ticks it returns **`RUNNING`**
(deliberately — a throttled tick means "no fresh result this cycle, ask again," which avoids
surfacing a stale terminal status a parent could act on twice). Explicit `TimeSource` overload
available. Intended for throttling an expensive `action`, not an instant `condition`.

### `delay(durationNanos, child)`
Returns `RUNNING` **without ticking the child at all** until `durationNanos` elapses from this
activation, then ticks the child normally. Explicit `TimeSource` overload available.

### `runOnce(child)`
Runs the child to completion **once over the decorator's lifetime**, caches that terminal status, and
returns it forever after without ticking the child again (even across re-activations).

### `guard(condition, child)` — the observer-abort
- **Semantics:** ticks the child only while `condition` holds; returns the child's status. If the
  condition is false — including flipping false while the child is `RUNNING` — returns `FAILURE`.
- **Halt:** **halts the child** when the condition no longer holds.
- The condition is either a `BooleanSupplier` (`() -> ...`) or a `Predicate<Blackboard>`
  (`bb -> ...`), distinguished automatically by arity.

```java
guard(() -> !driverOverriding, autoScore)             // BooleanSupplier
guard(bb -> bb.get(DETECTED) == Element.LEFT, scoreLeft)   // Predicate<Blackboard>
```

### `subtree(name, child)`
A thin naming wrapper: delegates tick/halt to the child but reports `name` in telemetry, so a
reusable strategy fragment shows up under its own label in the active-path line.

---

## Leaves

Leaves touch the robot. Each takes a `name` (for telemetry) plus a functional body. The overloads are
**disjoint by shape**, so the compiler always picks the right one:

### `action(name, body)`
A unit of work that may span ticks. Three body forms:

| Body type | Use | Example |
|---|---|---|
| `Supplier<Status>` (`() -> ...`) | ignores the blackboard | `action("score", () -> fired ? SUCCESS : RUNNING)` |
| `Function<Blackboard,Status>` (`bb -> ...`) | reads/writes the blackboard | `action("scan", bb -> { bb.set(DETECTED, read()); return SUCCESS; })` |
| `StatefulAction` (an object) | needs distinct start / running / halt phases | `action("drive", new DriveToPoint(...))` |

`StatefulAction` has `onStart(bb)` (once, when activated), `onRunning(bb)` (each tick, returns a
`Status`), and `onHalt(bb)` (**required** — stop your motors here when preempted).

### `run(name, body)`
Convenience for a fire-and-forget side effect: runs a `Runnable`, returns `SUCCESS`.

```java
run("resetEncoders", () -> drive.resetEncoders())
```

### `condition(name, test)`
A pure yes/no test — returns `SUCCESS` when true, `FAILURE` when false, **never `RUNNING`** (returning
`RUNNING` from a condition throws). `test` is a `BooleanSupplier` (`() -> ...`) or a
`Predicate<Blackboard>` (`bb -> ...`).

```java
condition("hasPiece", intake::hasPiece)
condition("nearGoal", bb -> bb.get(DISTANCE) < 12.0)
```

---

## Blackboard

Shared, typed state. Declare each key once as a `static final` constant.

```java
static final Key<Double> HEADING = Key.of("drive.heading", Double.class);
```

| Method | Behavior |
|---|---|
| `Key.of(name, Class<T>)` | Create a typed key. Keys are **identity-based** — the same slot means the same `Key` instance, so two keys with the same name but different types never collide. |
| `set(Key<T>, T value)` | Store a value. Rejects `null`, and (defense-in-depth) a value whose type doesn't match the key. Updating an existing key allocates nothing. |
| `get(Key<T>)` | The value, or **`null`** if unset. |
| `getRequired(Key<T>)` | The value, or throws `IllegalStateException` **naming the key** if unset. Use in a guard/condition that requires the key to be present. |
| `getOrDefault(Key<T>, T dflt)` | The value, or `dflt` if unset. |
| `has(Key<?>)` | Whether a value is stored. |

---

## FTC bridge (`ticktree-ftc`)

### `new FtcLibCommandAction(command)` / `new SolversLibCommandAction(command)`
Wrap an FTCLib / SolversLib `Command` as an `action` body (a `StatefulAction`).
`initialize → onStart`, `execute`/`isFinished → onRunning` (returns `SUCCESS` when finished, calling
`end(false)`), and preemption → `onHalt` → `end(true)`. The shim is **`RUNNING`/`SUCCESS` only** — a
Command has no failure signal, so express failure with a `timeout` or `guard`.

```java
action("intake", new SolversLibCommandAction(new IntakeCommand(intake)));
```

!!! danger "No subsystem mutual-exclusion"
    These shims ignore `Command.getRequirements()` and do **no** resource arbitration. Drive a given
    subsystem **entirely through TickTree or entirely through the `CommandScheduler`, never both**,
    and make competing TickTree behaviors mutually exclusive with a `selector`. See
    [core concepts](core-concepts.md#bridging-to-ftclib-solverslib-commands).

### `OpModeTreeRunner.runLinear(tree, keepRunning)`
For a `LinearOpMode`: ticks the tree until `keepRunning` (e.g. `this::opModeIsActive`) is false or the
thread is interrupted, and **halts the tree on any exit**. Throws `InterruptedException` (never
swallows it). For an iterative `OpMode`, just call `tree.tick()` in `loop()` and `tree.halt()` in
`stop()`.

### `Conditions.gamepad(name, gamepad, test)` / `Conditions.trigger(name, gamepad, axis, threshold)`
Build a `Condition` from **live** gamepad state, re-read every tick.

```java
Conditions.gamepad("intake", gamepad1, g -> g.a);
Conditions.trigger("boost", gamepad1, g -> g.right_trigger, 0.5);
```

### `TreeTelemetry.addActivePath(telemetry, caption, tree)`
Writes the tree's active-path line (e.g. `teleop ▸ autoScore ▸ alignToGoal [RUNNING]`) to SDK
`Telemetry` under `caption`. Does not call `update()` — batch that yourself.

---

## Introspection (core)

- `TreeVisitor.activePath(tree)` → the compact active-path `String` shown above.
- `TreeVisitor.snapshot(tree)` → a recursive `NodeSnapshot` (name, type, last status, active flag,
  children) for a custom overlay.
- Any node exposes `lastStatus()` and `isActive()`.

These allocate only when you call them — a tick with no visitor attached is allocation-free.
