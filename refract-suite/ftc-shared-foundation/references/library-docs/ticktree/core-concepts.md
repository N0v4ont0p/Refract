> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/core-concepts.md · Fetched: 2026-07-16
> Note: fetched at HEAD (998011a), not the v0.1.0 release tag — TickTree is pre-alpha and actively changing; per G5's own staleness discipline, re-fetch and re-stamp before trusting this against a materially newer commit.

# Core concepts

The mental model behind TickTree. Read this once and the [node reference](node-reference.md) becomes
obvious.

## Tick and Status

You **build** a tree once (in `init()`), then **tick** it every loop. A tick flows from the root
down; each node does a little work and returns one of three statuses:

| Status | Meaning |
|---|---|
| `SUCCESS` | This node finished successfully. |
| `FAILURE` | This node failed / its condition doesn't hold. |
| `RUNNING` | Still working — tick me again next loop. |

`RUNNING` is what makes a tree stateful: an action that drives to a point returns `RUNNING` for
however many loops that takes, then `SUCCESS`. TickTree ticks **once per `loop()`**; it never blocks
or sleeps.

## Three kinds of node

- **Composites** combine multiple children: `sequence`, `reactiveSequence`, `selector`,
  `reactiveSelector`, `parallel`. They decide which child/children run and how their statuses
  combine.
- **Decorators** wrap exactly one child and modify it: `inverter`, `repeat`, `timeout`, `guard`, and
  friends.
- **Leaves** are the tips that touch the robot: an **`action`** (does work, can return `RUNNING`) or
  a **`condition`** (a pure yes/no test — only `SUCCESS`/`FAILURE`, never `RUNNING`).

## Memory vs reactive — the concept to get right

This is the single most error-prone idea in behavior trees, so TickTree makes it **explicit in the
node name** rather than a hidden flag. Every ordered composite comes in two flavors:

- **With memory** (`sequence`, `selector`) — remembers which child was `RUNNING` and **resumes
  there** next tick. It does **not** re-check the children it already passed.
- **Reactive** / memoryless (`reactiveSequence`, `reactiveSelector`) — **re-ticks from the first
  child every tick**, so earlier children are re-evaluated continuously.

Why it matters, concretely:

> You want the robot to score **only while it still holds a game piece**. You write
> `reactiveSequence(hasGamePiece, driveToGoal, score)`. Because it's *reactive*, `hasGamePiece` is
> checked **every tick**. The instant the piece is lost, that condition fails, `driveToGoal` (which
> was `RUNNING`) is **halted**, and the sequence bails — exactly what you want.
>
> If you'd used a plain `sequence` (memory), it would have committed to `driveToGoal` and never
> looked back at `hasGamePiece` until the drive finished. The robot would keep driving to score with
> nothing to score.

Rule of thumb: **put guard conditions in a `reactiveSequence`** (so they keep being checked), and
**use priority `reactiveSelector` when a higher-priority behavior must be able to interrupt a
lower-priority one** (see halt/preemption below). Use the memory variants for fixed step sequences
where re-checking a completed step would be wrong (e.g. "close the gripper, *then* lift" — you don't
want to re-open the gripper).

## Halt and preemption — why it matters

When a higher-priority branch takes over from a lower-priority one, the behavior that *was* running
must **stop cleanly** — its motors set to zero, its follower cancelled. TickTree calls this **halt**,
and it's a first-class part of every node's contract.

Two mechanisms *trigger* preemption:

- A **`reactiveSelector`**: the moment a higher-priority child becomes viable, the running
  lower-priority child is halted and the higher one takes over.
- A **`guard`** (or a condition in a `reactiveSequence`): when the condition flips false, the child
  it was gating is halted.

The motivating FTC cases:

- **Endgame buzzer** — a top-priority `guard(() -> matchTimer.inEndgame(), parkAndHang)` in a
  `reactiveSelector`. When the buzzer sounds, whatever the robot was doing is halted and it parks.
- **Driver override** — `guard(() -> !driverOverriding, autoScore)` above a `driverControl` fallback.
  Grab the sticks and auto-score is halted instantly; release and it resumes.

When you call `tree.halt()` (e.g. in `stop()`, or automatically via `OpModeTreeRunner` on exit),
the whole active branch is halted — so **actuators stop when the OpMode ends**, without you
remembering to zero every motor.

## The blackboard

The **blackboard** is the tree's shared, typed memory — how one node reads what another wrote,
without the nodes referencing each other. Keys are **typed handles** you declare once:

```java
// import static io.github.n0v4ont0p.ticktree.TickTree.*;
// import static io.github.n0v4ont0p.ticktree.Status.*;
// import io.github.n0v4ont0p.ticktree.*;

enum Element { LEFT, CENTER, RIGHT }
static final Key<Element> DETECTED = Key.of("detected", Element.class);

// an action writes it:
action("scan", bb -> { bb.set(DETECTED, vision.read()); return SUCCESS; });
// a guard reads it:
guard(bb -> bb.get(DETECTED) == Element.LEFT, scoreLeft);
```

Reads and writes are **compile-checked** by the key's type — there's no stringly-typed `Object` map
to mistype. `get` returns `null` if unset; `getRequired` throws a clear error naming the key if you
expected it to be present; `getOrDefault` supplies a fallback. See the
[node reference](node-reference.md#blackboard).

## Bridging to FTCLib / SolversLib commands

You can wrap an existing FTCLib or SolversLib `Command` as a leaf, so all the subsystem/command code
you've already written drops straight into a tree:

```java
action("intake", new SolversLibCommandAction(new IntakeCommand(intake)));
```

The command's `initialize/execute/isFinished/end` map onto the leaf's lifecycle: it runs until
`isFinished()`, then returns `SUCCESS`; if the tree preempts it, `end(true)` is called so the command
stops cleanly.

!!! danger "No subsystem mutual-exclusion — don't mix scheduling paradigms"
    The command shims **ignore `Command.getRequirements()`** and do **no** resource arbitration.
    FTCLib/SolversLib's `CommandScheduler` uses `getRequirements()` to guarantee two commands never
    drive the same subsystem at once — **TickTree does not replicate that.** If the same hardware is
    driven *both* through TickTree *and* through the `CommandScheduler` (or through two TickTree
    leaves active at the same time), nothing stops both from commanding it simultaneously.

    **Drive any given subsystem entirely through TickTree, or entirely through the CommandScheduler —
    never both.** Within TickTree, make competing behaviors mutually exclusive structurally by putting
    them under a `selector` / `reactiveSelector` so only one is ever active.
