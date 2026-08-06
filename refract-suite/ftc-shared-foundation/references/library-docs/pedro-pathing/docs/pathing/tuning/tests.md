> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/tests.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Tests
description: Validating your tuning
---

To validate your tuning, it is prudent to try running at least one of these tests.
They are runnable via the Tuning class and using the gamepad to the `Tests` folder.

## Line
Line Test is used to analyze the follower's capability of driving with all of the PIDFs active at once. 
This helps determine if any PIDF(s) need adjusting.
The follower will drive 48 inches forward (two tiles) and then back to the initial position. It will loop this action.

## Triangle
Triangle Test is used to ensure that the follower is capable of straight line interpolation.
This helps determine if any PIDF(s) need adjusting.
The follower will drive in a triangle path, looping infinitely.

## Circle
Circle Test is used to ensure that the follower is capable of curved path following.
This helps determine if any PIDF(s) or if the Centripetal Scaling needs adjusting.
The follower will drive in a circle path always facing the center, looping infinitely.

## Troubleshooting
If you encounter a problem while tuning, check out the [troubleshooting page](/docs/pathing/troubleshooting) and [FAQ](/docs/pathing/faq).