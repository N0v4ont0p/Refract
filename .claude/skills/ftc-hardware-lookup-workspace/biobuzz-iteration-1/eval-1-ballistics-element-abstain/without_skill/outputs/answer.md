**Short answer: set your launch angle to about 21 to 24 degrees above horizontal (flat shot), or about 70 to 80 degrees (lob). The exact number depends on the pollen's mass, size and drag coefficient, and you didn't give me those. I wouldn't trust any one number until you test it.**

I don't have reliable details on the BIOBUZZ game or its "pollen" game piece. So I left the drag values open instead of pretending to know them.

**Setup:** launch speed 400 in/s (10.16 m/s), 120 in to the target horizontally, target 24 in above the launch point, g = 386.1 in/s², air density 1.2 kg/m³, and drag that grows with the square of speed. I stepped the flight forward in small time steps and searched for the angles that hit the target. As a check, the no-drag case matches the textbook formula (20.0 degrees).

| Case (assumed pollen) | Flat shot | Lob |
|---|---|---|
| No drag | 20.0°, still rising (+14 in/s) | 81.3°, falling (-371 in/s) |
| Dense 3 in ball, 70 g, Cd 0.47 | 20.5°, barely rising | 80.0°, falling |
| 5 in foam ball, 60 g, Cd 0.5 | 21.4°, just starting to fall (-6 in/s) | 76.6°, falling |
| 5 in wiffle ball, 30 g, Cd 0.6 | 24.1°, falling (-32 in/s) | 69.7°, falling |

What this means:
- **Drag adds about 0.5 to 4 degrees to the flat shot** and takes about 1 to 12 degrees off the lob. A lighter, bigger piece moves the angles more.
- **The flat shot hits at or near the top of its arc.** If the goal needs the piece to drop in from above (a basket or funnel), that shot is marginal. You'd need more distance, less speed or the lob.
- **The lob is very sensitive.** At 400 in/s it takes roughly 1.5 s in the air and changes a lot with drag. It's only worth using if the goal can only be scored from above.
- **"Hood angle" is not always the launch angle.** Many hoods are measured from vertical, and the piece often leaves a few degrees off the hood surface. Measure how the actual launch angle relates to your hood setting.
- **The real launch speed is probably below 400 in/s**, because of slip and wheel squish. Treat the speed as a tuning value: fire at 120 in, measure where it lands, and adjust the speed or angle in your lookup table.

Script: /private/tmp/claude-501/-Users-georgehu-Desktop-FTC-Training-AI/95cb109b-9a3f-4bed-97ed-a0ec2881d9b9/scratchpad/evalruns/traj.py. Change the mass, diameter and Cd in the last loop and rerun.

**Questions I'd ask you, and how each answer changes the result:**
1. **What are the pollen's mass, diameter and shape (solid, foam or hollow with holes)?** I'd put those into the script. If you don't know Cd, I'd use 0.47 for a smooth sphere and about 0.6 for a hollow ball with holes, then give you one final angle.
2. **Is 400 in/s the measured launch speed or a number worked out from wheel RPM?** If it's worked out, I'd tell you to measure it (for example, slow-motion video against a ruler). A 10% slower launch moves the flat shot by several degrees.
3. **Does the goal need the piece to come in from above, and how big is the opening?** If it needs a downward entry, I'd recommend the lob or a different distance. Knowing the opening size, I'd give the range of angles that still score.
4. **Is 24 in measured to the goal's center or its rim, and from the point where the piece leaves the launcher?** If it's the rim, I'd aim a few inches higher so the piece clears it.
5. **Is your hood angle measured from horizontal or vertical, and what are its limits?** I'd convert the numbers above to your hood setting and check the angle is within reach. If about 21° isn't reachable, I'd switch to the lob or adjust speed.
6. **Do you shoot from different distances?** If so, I'd build an angle table (every 12 in) instead of one number, with speed as the extra tuning value.