> SEASON SCOPE (added by Refract, 2026-09-13): only the header note's remark that the AprilTag/Motif
> examples are "DECODE-relevant" is season-specific (DECODE motif tags 21/22/23); the troubleshooting
> list itself is generic. The BIOBUZZ game has no MOTIF. It does not describe BIOBUZZ (2026-27). For
> BIOBUZZ facts read `ftc-shared-foundation/season-extensions/biobuzz-2026-27.yaml`. BIOBUZZ AprilTags
> (IDs 30-45) are clusters of 4 on the underside of the tipping HIVE's CELLs and, per the FTC SDK
> v12.0 README, move and are not suitable for absolute field localization.

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
