> Source: https://pedropathing.com/docs/pathing/troubleshooting · Fetched: 2026-07-17
> Completeness-audit addition: Pedro Pathing's real docs have ~30 pages under /docs/pathing;
> this was one of ~15 missing before this pass. Remaining known gaps (dashboard, constants,
> pedro-v-roadrunner comparison, most of reference/* — interpolation, deceleration, constraints,
> coordinates, pathcomplete, beziercurves, predictive, callbacks, speed-control, optimization,
> overshoot — custom/* extension points, and examples/apriltags + examples/apriltagpatternauto)
> are logged, not silently dropped — the AprilTag/Motif examples specifically are DECODE-relevant
> and worth a follow-up fetch.

# Pedro Pathing — Troubleshooting

Common issues during setup and tuning, per Pedro's own troubleshooting page (expandable sections
on the live page; consolidated here):

- **Localization problems** generally.
- **Heading tuner causes 180° turns / oscillation.**
- **Drift during turning-drive tuning.**
- **Excessive jitter** in robot movement.
- **Robot doesn't stop during a velocity test.**
- **Movement direction is wrong** during tuning.
- **No movement at all** during translational or heading tuning.
- **Constants aren't visible in the dashboard/panels.**
- **Directional errors or encoder inaccuracies.**

For anything not resolved by the above: the project's Discord has dedicated `#general` and tuning
channels — this is the maintained, current support channel per Pedro's own docs, not a stale
pointer.

See also: the tuning-validation-tests pages and the Pedro-vs-RoadRunner comparison page (both
currently unfetched gaps, noted above) for related context.
