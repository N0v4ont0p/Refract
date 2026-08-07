> AUTHORED BY REFRACT — not fetched from upstream. Written: 2026-08-06.
> This file is deliberately different from everything else in this directory: it is not a copy of
> Pedro's documentation, because the content below does not exist in Pedro's documentation, in
> REV's, or in goBILDA's. It was written after a real integration bug that no bundled doc could
> have prevented. Grounded in: Pedro's own localization-tuning.md (lines ~36, ~554-557) and
> path-building.md:80, both of which state Pedro's frame correctly; and the observation that
> neither they nor rev-robotics/ say anything about the frame a *different* consumer sees.
> Treat every claim about Pedro's own convention here as a pointer to those files, not a
> restatement to trust independently — re-read them if the details matter.

# Coordinate frames across consumers — the gap no single library's docs can close

Pedro documents its own frame, correctly and in two places: forward is +x, strafing left is +y
(`localization-tuning.md`), and heading 0 faces the +x direction with the standard CCW quadrant
progression (`path-building.md:80`). The Pinpoint section states the same thing concretely — push
the robot forward, x increases; push it left, y increases. None of that is ambiguous, and nothing
below contradicts it.

**The gap is that a robot can read its pose through more than one object, and each one answers in
its own frame.** Pedro's documentation is about Pedro. It is not wrong about anything here; it
simply has no reason to describe what some *other* class in your codebase returns.

## The concrete shape

`GoBildaPinpointDriver` is a device driver. It has its own pose, in its own frame, in whatever
units you configured on it. `Follower.getPose()` is Pedro's answer, in Pedro's frame, after
Pedro's localizer has interpreted that device. These are two different questions with two
different answers, and **nothing in either library flags a disagreement between them.**

A codebase ends up reading both when, for example:

- a pre-Pedro subsystem still reads the raw driver directly, and newer code reads the follower;
- a debug or tuning OpMode talks to the driver to check the hardware, while competition code
  talks to the follower;
- constants — goal positions, preset poses, mechanism offsets — were measured *before* the team
  adopted Pedro, in whatever convention the old code used, and were carried forward unchanged
  when the follower was introduced.

That last one is the quiet one. The constants are real measurements. They are correct numbers.
They are simply answers to a question nobody re-asked after the frame changed underneath them.

## Why it is silent

There is no error, no exception, and no telemetry flag. A position in the wrong frame is still a
valid position — it is just somewhere else. The robot drives confidently to the wrong place, or
aims confidently at the wrong target. The symptom presents as an aiming or pathing *tuning*
problem, which sends people to the PIDF coefficients, which are fine.

## What to actually do

1. **Decide, per stored coordinate, which frame it is stated in — and write it down.** Not in a
   comment: somewhere a tool can check. Refract models this as `reference_frames` plus a `frame:`
   tag on geometric constants in `core-feature-model.yaml`; `emit_tuning.py render` refuses to emit
   a coordinate across an undeclared frame conversion rather than guessing one.
2. **Prefer a single reader.** If Pedro's follower is the localization authority, route everything
   through `Follower.getPose()` and treat direct driver reads as debug-only, clearly marked.
3. **Re-derive carried-forward constants on adoption.** A constant measured before a localizer
   change is untrusted until re-checked, in the same way a tuning constant is untrusted after a
   mechanical change. Same rule, different axis.
4. **Check the units too.** The Pinpoint driver is commonly configured in millimetres while Pedro
   path coordinates are in inches. A frame mismatch and a unit mismatch look identical from the
   outside and often travel together.

## Scope of this file

This describes a *cross-consumer* risk, not a defect in Pedro, the Pinpoint driver, or their
documentation. Each is individually correct and internally consistent. The failure only exists in
codebases that read more than one of them, which is why it falls between every upstream doc set —
and why it is written here rather than reported upstream.
