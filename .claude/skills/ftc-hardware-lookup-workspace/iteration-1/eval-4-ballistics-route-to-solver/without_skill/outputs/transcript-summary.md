# Transcript Summary — where the angle came from

**Method: hand derivation. No skill, tool, or solver script was used.**

- I was explicitly instructed not to use any skill or read any SKILL.md, so I solved the projectile-motion problem analytically from my own knowledge.
- I started from the standard drag-free trajectory equation `y = x·tanθ − g·x²/(2v²·cos²θ)`, substituted `1/cos²θ = 1 + tan²θ` to turn it into a quadratic in `t = tanθ`, and solved with the quadratic formula.
- All arithmetic (computing `g·x²/2v² = 17.37 in`, the discriminant `11525`, its square root `107.35`, and the two roots `t = 0.364` and `t = 6.54`) was done by hand/mentally, not by executing code.
- I picked g = 386.1 in/s² (9.81 m/s² converted to inches). A slightly different g (e.g. 386.4) would not change the answers to the reported precision.
- I verified the low-angle root by plugging θ = 20.0° back into the trajectory equation and confirming y = 24.0 in. This was also a by-hand check, not a script.

**Result reported:** two solutions, θ ≈ 20.0° (direct) and θ ≈ 81.3° (lofted), with 20° recommended for a flywheel.

**Caveats surfaced in the answer:** no-drag/no-spin idealization, wheel-speed-vs-exit-speed slip, and high sensitivity to exit speed — all flagged as reasons to calibrate empirically. These are qualitative engineering notes, not tool output.
