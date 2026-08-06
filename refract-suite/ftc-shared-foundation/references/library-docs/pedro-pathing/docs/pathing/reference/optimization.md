> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/optimization.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Optimization
---

To optimize your robot, try these steps:

### Drive PID Adjustments
Increasing your Drive P value can often make your robot go faster, although after a certain threshold this likely won't help.

### Global Deceleration Mode
Toggle Global Deceleration mode in your PathChains with .setGlobalDeceleration(double brakingStrength). The lower the value you pass in, the later in your chain the robot will start decelerating. Optimize by seeing how low you can set this value without causing too much overshoot. This tends to help more on a PathChain-to-PathChain basis, instead of a single global value used everywhere.

### Optimal Pathing
Using the visualizer, try to optimize your robot's paths. Typically, shorter paths like lines tend to perform the best speed-wise. Beyond this, try experimenting with different heading interpolations. Make good use of features like piecewise heading interpolations, as for longer paths, a blend between linear and tangential can often be optimal.
