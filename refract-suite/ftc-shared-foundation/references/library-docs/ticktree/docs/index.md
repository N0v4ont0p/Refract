> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/index.md · Fetched: 2026-08-06 · Ref: main @ 998011a20399
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

# TickTree

**A behavior-tree decision-making engine for FIRST Tech Challenge (FTC) robotics, in Java.**

TickTree answers a question FTC's existing tooling leaves to ad-hoc student code:

> *Given the current state of the match, the robot, and the field — which behavior should the
> robot run right now, and how does it get preempted the instant that stops being true?*

You express your robot's strategy as a **tree** you build once and **tick** every loop. The tree
continuously picks the right behavior and — critically — stops the old one cleanly when priorities
change (the driver grabs control, the endgame buzzer sounds, a sensor flips).

!!! warning "Pre-alpha"
    The engine and FTC bridge are implemented and tested off-robot, but 1.0 has not shipped and the
    API may still change between 0.x releases.

## Why not just an `if/else` or a state machine?

A wall of `if/else` in `loop()` has no notion of "currently running," priority, or clean
preemption — every branch re-runs from scratch each loop, and anything that takes more than one
loop (drive to a point, spin up a shooter) turns into a tangle of hand-managed flags. Hand-rolled
state machines work but scale badly: every new state can need transitions to and from every other
state. Behavior trees are the well-established fix — reactive arbitration among many behaviors with
clean, composable preemption.

## It's orthogonal to what you already use

TickTree is a **decision layer**. It doesn't move the robot or run subsystems — it decides *what
to do* and delegates the *how* to the libraries you already have:

- **vs. Road Runner / Pedro Pathing** — those are *motion* libraries: they build and follow
  trajectories. They have no concept of *whether* a path should be running, of priority between
  behaviors, or of being preempted by an unrelated condition. A TickTree action can command a Road
  Runner / Pedro follower and return `RUNNING` until it arrives, while a TickTree guard decides
  whether that path should still be running at all. They compose; they don't overlap.

- **vs. FTCLib / SolversLib** — those give you subsystems, commands, and a scheduler: *how to
  structure and run a unit of behavior*. Command groups are scripted composition ("do A then B"),
  not reactive arbitration. TickTree sits **above** commands and **bridges to** them — you wrap an
  existing `Command` as a leaf (see the [node reference](node-reference.md)) and keep everything
  you've already written.

One line: Road Runner/Pedro = *how to move*; FTCLib/SolversLib = *how to run a unit of behavior*;
**TickTree = which unit to run right now, and how it gets preempted.**

## Next

- **[Getting started](getting-started.md)** — install and get a tree ticking in ~10 minutes.
- **[Core concepts](core-concepts.md)** — the mental model (tick, composites, memory vs reactive,
  halt/preemption).
- **[Node reference](node-reference.md)** — every node type with examples.
