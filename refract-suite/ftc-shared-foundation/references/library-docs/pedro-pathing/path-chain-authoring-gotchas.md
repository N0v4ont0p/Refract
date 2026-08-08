> AUTHORED BY REFRACT — not fetched from upstream. Written: 2026-08-07.
> Not a copy of Pedro's documentation. Checked directly before writing: none of the three items
> below appear as warnings anywhere in this corpus's bundled Pedro doc set (`path-building.md`,
> `followers.md`, `docs/pathing/reference/beziercurves.md`, `docs/pathing/reference/path-builder.md`,
> `docs/pathing/reference/optimization.md`, `docs/pathing/examples/auto.md`, `tuning.md`, and the
> rest of the 63-file set) — `optimization.md` recommends experimenting with heading-interpolation
> blends for speed, but nothing states the discontinuity risk below; `centripetalScaling` is
> documented as a value to tune, but nothing states what happens when it isn't. Each item was
> verified as a real, reproducible mechanism (numeric curvature/heading/saturation computation, not
> a visual read of a path export) before being written here as general, not team-specific, content.

# Path-chain authoring gotchas — three ways a path that "looks fine" isn't

Pedro's `PathBuilder` API is straightforward to use and its docs cover the happy path well. These
three failure modes share a property that makes them worth a dedicated page: each one produces a
path segment that looks completely reasonable in a visualizer or by eyeballing the coordinates, and
only shows itself as wrong once the robot actually runs it, or once the underlying numbers are
actually computed rather than glanced at.

## 1. Heading interpolation is not continuous across a chained `.addPath()` call by default

Each `.addPath(...).setLinearHeadingInterpolation(startRad, endRad)` (or its tangent/constant
variants) defines the heading target **for that segment only**. Nothing in the builder checks that
one segment's ending heading target matches the next segment's starting one — they're independent
declarations, and the builder will happily accept a chain where segment N ends its heading
interpolation at one angle and segment N+1 begins its own at a different one.

**The consequence:** the robot does not smoothly continue rotating between the two segments. It
snaps — a real, physical, near-instantaneous heading correction the instant the follower advances
past the segment boundary — even though each segment, read on its own, looks completely normal.
This is invisible reading either segment in isolation and only shows up by comparing the *ending*
heading target of one segment against the *starting* target of the next, across the whole chain.

**Check:** for every consecutive pair of segments in a chain, confirm the ending heading of segment
N equals the starting heading of segment N+1 (or that the transition is deliberately abrupt, if
that's genuinely intended — e.g. a fast direction reversal). Do this numerically across the whole
chain, not by skimming the coordinates.

## 2. A control point placed past its own segment's endpoint produces a hairpin, not a gentle bulge

A `BezierCurve`'s intermediate control points pull the curve toward them; that's the whole mechanism
that makes a Bezier curve useful. But a control point placed *beyond* the segment's actual endpoint
— past where the path is supposed to stop, rather than off to one side of a reasonable route between
start and end — doesn't produce a wide, gentle bulge the way a moderate off-line control point does.
It produces a sharp overshoot-and-double-back: the path travels past the intended region and turns
sharply to come back to the real endpoint, sometimes bottoming out at a turning radius of only a few
inches at the tightest point.

**Why it's easy to miss:** it's a natural mistake when dragging a point in a visual path editor (a
small pixel-space nudge can be a large real-world overshoot depending on zoom), and a hairpin that
only occupies a couple of inches of the overall path doesn't stand out when eyeballing the full
route — the overall shape still looks approximately right.

**Check:** compute the curve's actual curvature (or minimum turning radius) at a fine sample
resolution across each Bezier segment, not just at its labeled control points. A curvature spike
that doesn't correspond to an intentional tight turn is this failure mode.

## 3. Untuned `centripetalScaling` can silently saturate to full power — invisible on a straight path, real on the first curve

Pedro's own docs correctly explain what `centripetalScaling` is for (compensating drive output for
centripetal force while cornering) and that it needs tuning. What they don't state is the
consequence of *not* tuning it: the library's own centripetal-correction term is a function of
`centripetalScaling × mass × velocity² × curvature`, clamped to the drivetrain's maximum power. An
untuned value — including the library's own shipped default — can clamp to full sideways power well
before a curve's tightest point is reached, if the segment's tangential speed and curvature combine
to push the term past the clamp.

**Why it's invisible until the first curve:** the term is zero contribution on a perfectly straight
segment (zero curvature), so a robot can run an entirely straight-line autonomous with an untuned
`centripetalScaling` and see no symptom at all. The first `BezierCurve` — especially one with a
tight endpoint radius, which is exactly where curvature is highest — is where a saturated correction
term first has anything to saturate.

**Check:** before trusting any curved path segment, compute the centripetal-correction term across
the segment (using the robot's actual mass and the segment's actual tangential speed and curvature)
and confirm it stays within the drivetrain's power range at every sampled point, not just check that
`centripetalScaling` has *some* value.

## The pattern underneath all three

None of these are visible from a path visualizer's rendered shape, and none are visible from
reading the coordinates by eye. Each requires actually computing the relevant quantity — heading
continuity, curvature, the correction-term formula — across the whole chain, at a fine enough
sample resolution to catch a spike that a coarse or visual check would smooth past. Treat a path
chain as verified only once its numbers have actually been computed, not once it looks right.
