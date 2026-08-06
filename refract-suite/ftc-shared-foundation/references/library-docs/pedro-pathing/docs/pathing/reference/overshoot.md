> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/overshoot.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Mitigating Overshoot
---

Please read the Deceleration page before looking at this one.

If your robot is overshooting in your auto, there are a couple of things you can try:
- Lower BrakingStrength: try lowering your BrakingStrength. Subtracting by intervals of 0.25 typically works well.
- Toggle Global Deceleration mode: if your PathChain has two or more paths, this will help a lot.
