> AUTHORED BY REFRACT — not fetched from upstream. Written: 2026-08-09.
> Not a copy of Pedro's documentation. Every claim below was checked against the real
> `Follower.java`, `VectorCalculator.java`, `Mecanum.java`, `FollowerConstants.java`, and
> `BezierCurve.java` source at `Pedro-Pathing/PedroPathing@main`, fetched fresh for this file — not
> recalled, and not taken on trust from a report describing them. Line numbers are not cited because
> they drift; the structural claims (branch conditions, call order, what each branch does and does
> not compute) were re-derived directly from the fetched source and are stable across refactors that
> don't change the actual behavior. Two facts below were found independently while verifying this
> file's claims and are not restated from any external report: the `useCentripetal` public toggle,
> and that `atParametricEnd()` is a separate geometric check from the timing-gated end sequence.

# `Follower.update()`'s three branches, and why parking a Pedro robot is not obvious

Pedro's bundled examples show `follower.update()` called once per loop with no further explanation.
Internally it is not one code path — it is three **mutually exclusive** branches, and which one runs
determines what corrections are active, which is directly relevant to a question every teleop needs
an answer to: how do you make the robot actually stop and hold still.

## The three branches

Each loop, in order, `update()` checks:

1. **`manualDrive`** (teleop driving) — runs `getCentripetalForceCorrection()`, the teleop heading
   vector, and the teleop drive vector (the values from `setTeleOpDrive`). **No translational
   position correction.** This is the branch active while a driver is actively commanding the stick.
2. **`holdingPosition`** (set by `holdPoint(...)`) — runs a translational correction and a heading
   correction, each optionally scaled down (`holdPointTranslationalScaling` /
   `holdPointHeadingScaling`), with the drive vector forced to zero. **No centripetal correction is
   computed in this branch at all** — it isn't in the call.
3. **`isBusy`** (mid-`followPath`) — runs the full corrective vector, heading vector, and drive
   vector from active path following. This is normal autonomous path-following.

These are checked in order and are exclusive: whichever condition is true first is the only one that
runs that loop. A robot cannot be simultaneously "driving teleop" and "holding a point" — entering
one clears the others' governing booleans (see `breakFollowing()`, below).

## The centripetal-at-standstill bug

`VectorCalculator.getCentripetalForceCorrection()` behaves differently depending on whether a path is
active:

- **Following a path:** curvature comes from the path's own geometry — a known, stable quantity.
- **Teleop (`manualDrive`, no active path):** curvature is derived from the robot's own recent motion
  — an average velocity and average acceleration vector, combined as
  `curvature = (avgAccel.y / avgVel.x) / (sqrt(1 + (avgVel.y/avgVel.x)²))³`. The result is then
  clamped to the drivetrain's power range and applied as a real corrective vector.

**The failure case:** a stationary or near-stationary robot has an `avgVel.x` that is sensor noise,
not zero. An *exact* zero produces `0/0 → NaN`, and there is a `Double.isNaN(curvature)` guard that
correctly returns a zero vector for that case. But real sensor noise is essentially never exact zero
— it is small and nonzero, and dividing by a small nonzero denominator does not produce `NaN`, it
produces a curvature estimate that can be enormous. That gets clamped to the drivetrain's **full
power range**, applied along the previous path's stale tangent direction, and the sign flips as noise
flips the sign of the estimated acceleration. The NaN guard does not catch this case — it was never
meant to; it exists for the true 0/0 singularity, not for "small and noisy."

**Consequence:** commanding `manualDrive` (the `setTeleOpDrive` path) with a zero input vector, as a
way to "park," does not park the robot. It can inject a real, full-power, sign-flipping sideways
kick, every loop, sourced entirely from motion noise.

**Two independent mitigations, both real and available now:**

1. **Don't park via `manualDrive` at all — use `holdPoint(pose)` instead.** Its branch has no
   centripetal term in the call whatsoever (see above), so this failure mode cannot occur there
   regardless of noise. It also has genuine position-hold correction, which a zero-vector
   `manualDrive` call does not.
2. **`follower.useCentripetal`** is a public field on `Follower`, defaulting to `true`, and it gates
   `getCentripetalForceCorrection()` directly (`if (!useCentripetal) return new Vector();`). Setting
   `follower.useCentripetal = false` disables the term everywhere — including in teleop — without
   touching drive, heading, or translational correction. This is a coarser tool than switching to
   `holdPoint` (it also removes centripetal correction from active path-following, which is usually
   wanted), but it is a real, one-line escape hatch if a team needs to isolate the symptom quickly.

`holdPoint` is the better fix for the parking case specifically, since it adds real correction rather
than just removing a broken one.

## Park semantics — what each call actually gives you

| Call | Translational correction | Centripetal term | Motor zero-power behavior |
|---|---|---|---|
| `startTeleopDrive(true)` + zero drive vector | none (`manualDrive` branch has no translational correction) | yes, and broken per above | `BRAKE` (verified: `Follower.startTeleopDrive(boolean)` → `Mecanum.startTeleopDrive(boolean)` → `setMotorsToBrake()`) |
| `holdPoint(pose)` | yes, real correction (optionally scaled) | none | `FLOAT` (verified: `holdPoint` calls `breakFollowing()` first, which calls `setPower(0)` on every motor then `setMotorsToFloat()` — but `holdingPosition` then commands real, nonzero correction power every subsequent loop, so "FLOAT" describes the zero-power *behavior mode*, not that the robot is coasting with no correction) |

Neither call gives brake-mode motors *and* active position correction simultaneously — that's not a
gap in the API, it's what the two calls are each built for. `holdPoint` is the right answer for
"stop and hold a position": active correction fighting real drift beats a passive brake resisting
none. It's also what Pedro's own `followPath(..., holdEnd = true)` enters automatically at the end of
a path (see below) — the library's own default for "stay here" is `holdPoint`, not a bare brake.

**`holdPoint()` re-snapshots its target on every call.** Each call re-runs `breakFollowing()` and
re-captures the target pose fresh. Calling it once when entering a hold state is correct; calling it
every loop while already holding re-anchors the target to wherever the robot currently is each time,
which drags the hold point along behind any drift rather than correcting back to the original spot.

## `followPath(..., holdEnd)` really does hand off to `holdPoint` — verified

A plausible-sounding wrong belief: that `followPath(chain, power, true)` just means "PIDF keeps
nudging toward the end forever." **It does not.** The real sequence, confirmed directly in
`Follower.update()`'s path-end handling:

1. Once the path's parametric end is reached, the follower starts a timeout clock and continues
   running full path-following PIDF (the `isBusy` branch) every loop.
2. Each loop it checks three constraints — velocity below `pathEndVelocityConstraint`, translational
   error below `pathEndTranslationalConstraint`, heading error below `pathEndHeadingConstraint` — or
   the timeout constraint elapsing.
3. Once those constraints are satisfied (or the timeout fires): if `holdEnd` was `true`, it calls
   `holdPoint(...)` on the path's last control point and the chain's final heading goal. If `holdEnd`
   was `false`, it calls `breakFollowing()` instead — no hold, motors simply stop.

So `holdEnd = true` genuinely transitions the follower from "actively following" into the same
`holdingPosition` branch a manual `holdPoint()` call would enter — not an indefinite PIDF chase.

## `atParametricEnd()` can be true while `isBusy` is still true

`atParametricEnd()` is a separate, purely geometric query — it answers "has the closest point on the
path reached parametric t=1", independent of the timing/tolerance sequence described above. It can
return `true` well before the velocity/translational/heading constraints in that sequence are
satisfied, and while `isBusy` is still `true` and full path PIDF is still actively running. **A state
machine that keys its next-state transition on `atParametricEnd()` alone, rather than on `isBusy`
going `false` (or an explicit hold/break having actually happened), enters its next state while the
robot is still under active path-following correction** — which is a different condition than
"the robot has stopped," and can look identical to the stillness question the next state actually
needs answered.

## Small facts worth having on hand

- **`BezierCurve(FuturePose... controlPoints)`** is a varargs constructor. A Bezier curve's degree is
  `(control point count) − 1` by definition — 3 poses is a quadratic curve, 4 is a cubic.
- **`stuckVelocity` defaults to `1.0`** (in/s) in `FollowerConstants` — the library's own built-in
  reference point for "is the robot actually still moving," used internally to detect a stalled path
  follow. Worth knowing as a reference scale when picking a "stopped" threshold elsewhere, though it
  governs a different internal mechanism (stall detection, not the end-of-path hold sequence above).
- **Angular/heading rate is radians/sec**, consistent with Pedro's heading convention being radians
  throughout its public API (`Math.toRadians(...)` in every heading-interpolation call the bundled
  examples show; `path-building.md` states the same convention for static headings). A control term
  scaled assuming degrees/sec will be off by a factor of ~57.3.
