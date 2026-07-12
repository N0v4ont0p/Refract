# Transcript summary — eval-4 ballistics (with skill)

## Where the answer came from
The launch angle came from the **solver**, not a hand derivation. I did no ballistics arithmetic myself; the numbers are verbatim solver output.

## Files read
1. `.claude/skills/ftc-hardware-lookup/SKILL.md` — read in full first. Section 4 ("Physics / ballistics") routes launch-angle questions to `scripts/trajectory_solver.py`, which reads constants from the physics JSON; gravity is 386.4 in/s² (corrected, stored in the file, not hardcoded). Directs to report the drag-aware angle if the user acts on it, and to carry the "not-fielded" caveat.
2. `.claude/skills/ftc-hardware-lookup/references/physics/decode-artifact-ballistics.json` — confirmed gravity 386.4 in/s² (corrected from a team's shipped 385.0), plus drag model (hollow 5 in ball, Cd 0.3, effective area ×0.7). Confirms constants are structured data, not recalled.
3. `.claude/skills/ftc-hardware-lookup/scripts/trajectory_solver.py` — verified it reads G from the JSON, provides a correct closed-form no-drag solver plus a drag-aware shooting method, and abstains (exit 3) if distance/speed missing.

## Commands run and key output
Working dir: `.claude/skills/ftc-hardware-lookup`

**1. Low arc (default):**
```
python3 scripts/trajectory_solver.py -d 120 -t 24 -v 400
```
Output (key fields):
- `no_drag_angle_deg: 20.01`
- `drag_aware_angle_deg: 21.18`
- `reachable: true`
- `gravity_in_s2: 386.4`, source `references/physics/decode-artifact-ballistics.json (corrected 385->386.4)`

**2. High arc:**
```
python3 scripts/trajectory_solver.py -d 120 -t 24 -v 400 --high-arc
```
Output (key fields):
- `no_drag_angle_deg: 81.3`
- `drag_aware_angle_deg: 106.3`  ← past vertical; drag shooting-method artifact on the steep branch, flagged as unreliable in the answer.

## Answer delivered
Primary: **~21.2° (drag-aware, low arc)** to act on; 20.0° is the no-drag idealization. Reported both arcs, recommended the low/flat arc for a flywheel shooter, flagged the 106° high-arc drag result as a numerical artifact, cited gravity 386.4 in/s² with its source, noted 400 in/s is a user assumption the angle is sensitive to, advised tuning empirically from ~21°, and carried the solver's "correct solver ≠ evidence teams field physics-based power" caveat.
