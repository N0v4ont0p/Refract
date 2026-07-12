# Launch angle for 400 in/s, 120 in out, 24 in up

I ran your numbers through the deterministic trajectory solver (I don't hand-calculate or recall ballistics numbers — they come from the solver, which reads its physics constants from a structured file). Here's what it returned.

## Answer: aim about 21° above horizontal

**Inputs:** distance = 120 in, target height = +24 in above the launch point, launch speed = 400 in/s.

| Solution | No-drag angle | Drag-aware angle |
|---|---|---|
| **Low arc (use this)** | 20.0° | **21.2°** |
| High arc | 81.3° | (unreliable — see below) |

**Act on the drag-aware low-arc angle: ~21.2°.** That's the one that accounts for the artifact actually slowing down in the air, so it's the number to point the hood at. The 20.0° no-drag figure is the idealized version — real drag makes you aim about a degree higher to still hit 24 in of rise at 120 in out.

## Why two arcs, and why the low one

For any reachable target there are two launch angles that both pass through (120 in, +24 in): a **low, flat arc** (~21°) and a **high, lobbed arc** (~81°+). The low arc is almost always what you want for a flywheel shooter — flatter trajectory, shorter flight time, less sensitive to small speed errors, and a more forgiving entry into the goal. I'd go with ~21°.

(The solver's drag-aware *high*-arc result came back as 106°, which is past vertical and physically not what you'd shoot — that's the numerical shooting-method wandering off on the steep branch, not a real firing solution. The low arc is clean and is the one to trust here. If you specifically wanted a lobbed shot, we'd want to re-solve that branch more carefully.)

## The constants behind this

- **Gravity:** 386.4 in/s² — source: `references/physics/decode-artifact-ballistics.json` (this value was corrected at the source from a team's shipped 385.0; 386.4 = 32.2 ft/s² × 12).
- **Drag model:** the solver models the DECODE artifact as a hollow 5 in ball (Cd = 0.3, effective area × 0.7), which is why the drag-aware angle differs from the ideal one. Those are the source team's (24089) modeling choices, carried as-is and not independently verified — so treat the drag-aware angle as a strong starting point to dial in on the field, not a to-the-tenth-of-a-degree guarantee.

## Practical notes

- **400 in/s is your assumption, not a measured value.** The angle is sensitive to launch speed, so if the real exit velocity off the flywheel is different, the angle shifts. Worth chronographing / measuring your actual artifact speed and re-running if you can.
- **Tune from ~21°.** Set the hood there, then adjust empirically — real-world spin, artifact-to-artifact variation, and flywheel speed sag under load all move the true number a little.
- One honest caveat the solver carries: having a correct solver proves the physics is tractable; it is **not** evidence that a physics-based auto-aim is the right competitive approach. Plenty of strong teams just use a tuned lookup table of (distance → angle/RPM). The math above is a great way to seed that table.

Want me to re-run it for a different distance/height, or generate a distance-vs-angle table you could drop into a shooter lookup?
