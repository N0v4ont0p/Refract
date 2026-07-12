# Arm extension legality — how far can the robot expand past starting size?

**Verdict: legal to expand, but within hard limits — and horizontally you do NOT get any bigger than 18×18.**

```json
{"verdict": "legal (within stated limits)", "citations": ["R101", "R105", "G414", "G415"], "reasoning": "See below."}
```

## The short answer

Once the MATCH starts your robot is allowed to expand beyond its STARTING CONFIGURATION, but it stays boxed by a **fixed 18 in. × 18 in. horizontal footprint** and an **18 in. height limit** — with a single endgame exception that lets you go taller. (R105)

- **Horizontal (your arm reaching out sideways):** at *maximum mechanical extension* the whole robot must still fit inside a **fixed 18 in. × 18 in.** box (45.70 cm). That box is the same size as your starting footprint, so there is effectively **no net horizontal growth** past 18 in. — the arm can reach to the edge of that box, but the robot's overall length/width can never exceed 18 in. (R105.A, G414)
- **Vertical (arm lifting up):** you may expand up to **18 in. tall** at any time during the match. (R105.B)
- **Endgame vertical exception:** you may go up to **38 in. tall** (96.50 cm) **only when BOTH** are true: (A) it's the **final 20 seconds** of the match, **and** (B) the robot is **not in any LAUNCH ZONE**. (R105.C, G415)

## The detail that trips teams up (this is the one to get right for your arm)

**Horizontal expansion must be constrained MECHANICALLY, not by software.** R105 is explicit:

> "ROBOTS must be physically constrained to fit within these horizontal limits without the use of software… A ROBOT that can mechanically exceed the horizontal limit would be in violation even if the ROBOT has software limiting the position of the extension during the MATCH." (R105.A)

So for your arm: if the arm can *mechanically* reach out far enough to push the robot past 18 in. wide/long — even if your code stops it short — **it fails inspection.** You need a physical hard stop (mechanical limit) so the arm cannot exceed the 18 in. footprint even with software removed. During inspection you'll be asked to demonstrate maximum *mechanical* extension for horizontal; software limits are explicitly "not sufficient" there. (R105, I304)

**Vertical is more forgiving:** the 18 in. / 38 in. vertical limits *may* be enforced by software OR mechanically. (R105.B, R105.C)

**Two-sided extension:** a single mechanism that pokes out both sides is fine as long as the total horizontal dimension at max mechanical extension is ≤ 18 in. Two *independent* (not mechanically linked) mechanisms that can each extend opposite sides simultaneously past 18 in. total are **not** allowed. (R105)

**Flexible / floppy extensions count.** Surgical-tubing flappers, star intakes, anything springy that whips outside the box counts against the limit. Don't assume "it's soft so it doesn't count." (R105)

## Penalties if you blow the limit mid-match

Both the horizontal (G414) and vertical (G415) limits carry the same penalty scale:

- **MINOR FOUL** for an over-expansion, **escalating to MAJOR FOUL** if the over-expansion is used for strategic benefit (including if it impedes or enables a scoring action). (G414, G415)
- **Exception (horizontal, G414):** no penalty if the over-expansion is caused by *damage* and is *not* used for strategic benefit.

## Bottom line for your build

- Design the arm so that at its **hardest mechanical limit** the robot is still ≤ 18 in. in every horizontal direction — put a **physical stop** on it, don't rely on code. That's your real "how far past starting size" answer horizontally: **zero past 18 in.**, and 18 in. is already your starting footprint.
- The arm can lift to **18 in. tall** whenever you want; it can only reach **up to 38 in. tall in the last 20 seconds and outside every LAUNCH ZONE**. Height limits can be software-enforced.
- Be ready to show STARTING CONFIGURATION, max mechanical horizontal extension, and max vertical extension at inspection. (R105, R101, I304)

---

*Sources: R101 (STARTING CONFIGURATION is an 18 in. cube), R105 (expansion limits), G414 (horizontal expansion limits + penalty), G415 (vertical expansion limits, endgame exception + penalty). All four are base-manual text in the DECODE 2025–2026 Competition Manual incorporating Team Update 32; none of these four were altered by a Team Update in the local data. Note this snapshot was retrieved 2026-07-03 through TU32 — if FIRST has posted a newer Team Update, re-check before relying on it. All four citations verified to exist via `rules.py verify`.*
