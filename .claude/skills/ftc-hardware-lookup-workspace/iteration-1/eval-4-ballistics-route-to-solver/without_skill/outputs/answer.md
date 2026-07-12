# Flywheel Launch Angle

Short answer: there are **two** launch angles that hit your target — about **20°** (a fast, flat, direct shot) and about **81°** (a high, lofted arc). For a flywheel shooter you almost always want the **~20°** solution.

## The setup

- Launch speed: v = 400 in/s
- Horizontal distance to target: x = 120 in
- Target height above the launch point: y = 24 in
- Gravity: g = 386.1 in/s² (that's 9.81 m/s² expressed in inches)
- Assumption: no air drag, and the exit speed is exactly 400 in/s at the launch point.

## The math

The projectile trajectory, written in terms of the launch angle θ:

    y = x·tanθ − (g·x²) / (2·v²·cos²θ)

Using the identity 1/cos²θ = 1 + tan²θ and letting t = tanθ, this becomes a quadratic in t:

    (g·x² / 2v²)·t² − x·t + [y + g·x²/(2v²)] = 0

Plugging in numbers:

    g·x² / (2·v²) = 386.1 · 14400 / (2 · 160000) = 17.37 in

So:

    17.37·t² − 120·t + 41.37 = 0

Solving:

    discriminant = 120² − 4·17.37·41.37 = 14400 − 2875 = 11525
    √ = 107.35
    t = (120 ± 107.35) / (2·17.37) = (120 ± 107.35) / 34.75

    t = 0.364  →  θ ≈ 20.0°   (direct/flat shot)
    t = 6.54   →  θ ≈ 81.3°   (lofted arc)

## Quick check (θ = 20.0°)

    y = 120·tan20° − 17.37/cos²20°
      = 120·0.3640 − 17.37/0.8830
      = 43.68 − 19.68
      = 24.0 in  ✓

## Which one to use

- **~20°** — flatter, faster time of flight, less sensitive to small timing/height errors near the peak. This is the practical FTC choice for a flywheel.
- **~81°** — a near-vertical lob that just barely reaches out to 120 in; very sensitive to speed variation. Only useful if you need to clear an obstacle.

## Reality-check notes

- This ignores air drag and spin (Magnus) effects. A real artifact will fall a bit short of the no-drag prediction, so expect to aim **slightly higher** than 20° and tune on the field.
- 400 in/s ≈ 33.3 ft/s. If that number is a nominal wheel-surface speed, the artifact's actual exit speed is lower due to slip — measure real range at a known angle and back out your effective v.
- Small changes in exit speed move the landing point a lot at these distances, so plan to calibrate empirically once the mechanism is built.
