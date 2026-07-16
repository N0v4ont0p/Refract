> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/migration.md · Fetched: 2026-07-16
> Note: fetched at HEAD (998011a), not the v0.1.0 release tag — TickTree is pre-alpha and actively changing; per G5's own staleness discipline, re-fetch and re-stamp before trusting this against a materially newer commit.

# Migrating from an if/else ladder or a hand-rolled FSM

This isn't a migration from a previous version of TickTree — there isn't one yet. It's for teams
coming from what most FTC code actually looks like today: a big `if/else` chain in `loop()`, or an
`enum`-based state machine.

## Why switch

- **An `if/else` ladder has no notion of "currently running."** Every branch re-evaluates from
  scratch each loop, so anything that spans multiple loops (driving to a point, spinning up a
  shooter) needs hand-managed flags to avoid re-triggering — and interrupt handling gets copy-pasted
  and inconsistent everywhere it's needed.
- **A hand-rolled FSM is the natural next step, and it works — until it doesn't scale.** Every new
  state can, in principle, need a transition to and from every other state. Adding "if the intake
  jams, back off and retry, but only if there's still time" touches several existing states. FSMs are
  also weak at *hierarchical preemption* — "abandon whatever sub-behavior is running and go score
  because the buzzer just sounded" doesn't map onto a flat set of states cleanly.

A behavior tree fixes both: composites give you priority and sequencing without new transition code,
and `reactiveSelector`/`guard` give you preemption as a structural feature instead of something you
reimplement per state.

## A worked example: enum FSM → tree

Here's a small, typical TeleOp state machine:

```java
enum State { DRIVER_CONTROL, ALIGNING, SCORING }
State state = State.DRIVER_CONTROL;

@Override public void loop() {
    switch (state) {
        case DRIVER_CONTROL:
            drive.arcade(gamepad1);
            if (gamepad1.b) state = State.ALIGNING;
            break;
        case ALIGNING:
            if (aligner.align()) state = State.SCORING;
            if (gamepad1.a) state = State.DRIVER_CONTROL;   // manual cancel, handled separately
            break;
        case SCORING:
            shooter.fire();
            state = State.DRIVER_CONTROL;                    // back to driver once fired
            break;
    }
}
```

Already you can see the seams: the "cancel" check is duplicated logic bolted onto one state, and
nothing stops the shooter mid-fire if the driver cancels during `SCORING`. The equivalent tree
(`import static io.github.n0v4ont0p.ticktree.TickTree.*;` and `...Status.*;`, as throughout):

```java
BehaviorTree tree = TickTree.tree("teleop").root(
    reactiveSelector(
        guard(() -> !gamepad1.a,                 // "cancel" is now ONE guard, checked everywhere below
            sequence(
                guard(() -> gamepad1.b, action("align", () -> aligner.align() ? SUCCESS : RUNNING)),
                action("score", () -> { shooter.fire(); return SUCCESS; })
            )),
        action("driverControl", () -> { drive.arcade(gamepad1); return RUNNING; })
    )
).build(blackboard);
```

The cancel condition is now expressed **once**, as a guard above the whole scoring sequence — and
because it's a `reactiveSelector`/`guard`, pressing A halts whatever was running (including
mid-align or mid-score) automatically, instead of needing a hand-written interrupt check in every
state.

Mapping, in general:

| FSM concept | Tree equivalent |
|---|---|
| A state that does one thing then auto-advances | An `action` returning `SUCCESS` |
| A state that takes multiple loops | An `action` returning `RUNNING` until done |
| An explicit `state = X` transition | Structural — the next composite child, or a `guard` |
| A global "cancel"/"abort" check duplicated per state | One `guard` wrapping the whole branch |
| "State X can be interrupted by condition Y" | A higher-priority sibling in a `reactiveSelector` |

## What you don't have to throw away

If you already have FTCLib or SolversLib subsystems and `Command`s, **you don't rewrite them.** Wrap
an existing `Command` as a leaf with `FtcLibCommandAction`/`SolversLibCommandAction` (see the
[node reference](node-reference.md#ftc-bridge-ticktree-ftc)) and it drops straight into a tree:

```java
action("intake", new SolversLibCommandAction(new IntakeCommand(intake)));
```

Road Runner and Pedro Pathing trajectories don't change either — see the
[path-follower recipe](cookbook.md#wrapping-a-path-follower-road-runner-pedro-pathing-as-a-leaf) in
the cookbook. TickTree only replaces the **arbitration logic** (the `if/else`/FSM), not your
subsystems, commands, or motion code.
