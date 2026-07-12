# How far can your robot expand past its starting size? (Is your arm extension legal?)

**Season:** DECODE 2025-26 · Corpus incorporates through Team Update 32

> ⚠️ **Currency flag — read before relying on this.** The freshness check returned
> `UNVERIFIABLE` (exit 1): the local corpus is current through Team Update 32, but the script
> could not read a live Team Update number from the FIRST site to confirm nothing newer exists.
> The verdict below is grounded in the local tagged manual and every citation is verified to
> exist — but a Team Update after TU32 could have changed an expansion threshold. Confirm against
> the live manual before your event: https://ftc-resources.firstinspires.org/ftc/game/cm-html

---

## Verdict: **LEGAL — an extending arm is allowed, but only inside three hard limits**

```json
{
  "verdict": "legal (conditional on staying within the expansion envelope below)",
  "citations": [
    {"id": "R101", "text": "In the STARTING CONFIGURATION ( the physical configuration in which a ROBOT starts a MATCH ), the ROBOT must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. (45.70 cm) long, by 18 in. (45.70 cm) high volume. The only exception is that: A. pre-loaded SCORING ELEMENTS may extend outside the starting size constraint. If a ROBOT uses interchangeable MECHANISMS per I304 , teams should be prepared to show compliance with this rule and R105 in all configurations."},
    {"id": "R105", "text": "After the MATCH has started, ROBOTS may expand beyond the STARTING CONFIGURATION but are still subject to sizing constraints relative to the ROBOT, based on the initial STARTING CONFIGURATION. The sizing constraints are: A. After the start of the MATCH, ROBOTS may expand horizontally but must remain within a fixed 18 in. (45.70 cm) by 18 in. (45.70 cm) when fully expanded per G414 . ROBOTS must be physically constrained to fit within these horizontal limits without the use of software. B. After the start of the MATCH, ROBOTS may expand vertically up to 18 in. (45.70 cm). ROBOTS may be physically constrained or software limited to fit within this vertical limit. C. Within the limitations per G415 , ROBOTS may expand vertically up to 38 in. (96.50 cm). ROBOTS may be physically constrained or software limited to fit within this vertical limit. Figure 12-1: Horizontal Expansion Limit Figure 12-2: Vertical Expansion Limit Examples Any extension beyond the maximum expansion limit during ROBOT operation is considered a violation of this rule. This includes flexible extensions (e.g., surgical tubing flappers, star intakes) that cause the ROBOT to exceed the expansion limit. Teams should be prepared to show compliance with this rule and demonstrate their ROBOT expansions during the inspection process. During inspection, each team will be asked to show the ROBOT’S STARTING CONFIGURATIONS and additionally its configurations at maximum mechanical (horizontal) extensions and mechanical/software (vertical) extensions. Software limits are not sufficient to demonstrate maximum extensions for horizontal expansion. ROBOTS must show their maximum mechanical extensions during the inspection process. A ROBOT that can mechanically exceed the horizontal limit would be in violation even if the ROBOT has software limiting the position of the extension during the MATCH. A ROBOT with a single mechanism that can extend out of both sides of a ROBOT would be allowed as long as the overall horizontal dimension at maximum mechanical extension does not exceed 18 in. A ROBOT with multiple mechanisms that are not mechanically linked that can extend out of both sides of a ROBOT simultaneously would NOT be allowed if the overall horizontal dimension at maximum mechanical extension exceeds the 18 in. limit. At maximum extension, a ROBOT in compliance will not exceed the maximum allowable vertical extension of 38 in. (96.50 cm) in one direction while maintaining the horizontal expansion requirements of 18 in. (45.70 cm) length and width perpendicular to the vertical height. Teams are responsible for maintaining compliance with expansion limits and subject to penalties listed in G414 and G415 for any violations during the MATCH. 12.2 ROBOT Safety & Damage Prevention"},
    {"id": "G414", "text": "ROBOTS must comply with the horizontal expansion limits outlined in R105 . A during the MATCH. Exceptions: A. If the over-expansion is due to damage and not used for strategic benefit. Violation: MINOR FOUL. MAJOR FOUL if the over-expansion is used for strategic benefit, including if it impedes or enables a scoring action. ROBOTS are allowed to have moving parts that extend outside its STARTING CONFIGURATION, but these extensions must stay within the expansion limit as described in R105 ."},
    {"id": "G415", "text": "ROBOTS must comply with the vertical expansion limits outlined in R105 . ROBOTS may only expand above 18 in. (45.70 cm) up to 38 in. (96.50 cm) if both of the following conditions are true: A. during the final 20 seconds of the MATCH, and B. when not in any LAUNCH ZONES. Violation: MINOR FOUL. MAJOR FOUL if the over-expansion is used for strategic benefit, including if it impedes or enables a scoring action. ROBOTS are allowed to have moving parts that extend outside its STARTING CONFIGURATION, but these extensions must stay within the expansion limit as described in R105 ."}
  ]
}
```

All four citations verified to exist in the corpus (`rules.py verify` → `all_valid: true`).

---

## The plain-English answer

You start inside an **18 × 18 × 18 in cube** (R101). Once the MATCH starts you are allowed to
expand past that starting shape (R105), but "how far" splits into two very different axes:

### 1. Horizontal — you do NOT get any extra footprint
- Your robot can extend/move parts out, but the **overall horizontal dimension must stay within a
  fixed 18 in × 18 in** at full extension (R105.A). That's the *same* 18 in as your starting
  width/length — horizontally you can rearrange, not grow.
- This limit must be **enforced mechanically, not by software.** A robot that *can* mechanically
  reach past 18 in is illegal even if code stops it during the match (R105, G414). At inspection
  you'll be asked to show the max *mechanical* horizontal extension.
- One arm poking out one side is fine as long as the total width ≤ 18 in. Two independent
  (non-mechanically-linked) mechanisms extending out both sides at once are **not** allowed if the
  combined horizontal dimension exceeds 18 in (R105).

### 2. Vertical — this is where you actually get to grow
- **Most of the match: up to 18 in tall** (R105.B). Note: this vertical limit *may* be software-limited (unlike horizontal).
- **Only during the final 20 seconds of the MATCH, and only when NOT in any LAUNCH ZONE:** you may
  go up to **38 in tall** (R105.C, G415). Both conditions must be true simultaneously.

### So, for your arm specifically
- **Legal** if, at maximum *mechanical* reach, the whole robot stays within 18 in × 18 in
  horizontally, and the arm's height stays ≤ 18 in during normal play (≤ 38 in only in the last
  20 s and outside launch zones).
- If the arm is designed to reach *further out sideways* than 18 in total width, it is **illegal** —
  a software cap will not save it (horizontal must be physically constrained).
- Flexible/whippy extensions (surgical tubing, star intakes, etc.) count — if they flick past the
  envelope, that's a violation (R105).

### Penalties if you bust the envelope in a match
Both G414 (horizontal) and G415 (vertical): **MINOR FOUL**, escalating to **MAJOR FOUL** if the
over-expansion gives strategic benefit (e.g., it impedes an opponent or enables/blocks a scoring
action). Exception: horizontal over-expansion caused by *damage* and not used for strategic
benefit is not penalized (G414).

## Design/inspection checklist for the arm
1. Build a hard mechanical stop so the arm physically cannot push total width past 18 in — don't rely on code.
2. Verify the arm's tallest position is ≤ 18 in for general play; reserve the 18–38 in range strictly for endgame (last 20 s) and keep it retracted in launch zones.
3. Be ready at inspection to demonstrate: starting config, max mechanical horizontal extension, and max vertical extension (R105 / I304).

## Cross-references traversed
- R101 (starting cube) → cites **R105** (the expansion rule) and I304 (interchangeable mechanisms / inspection); cited-by G304 (field setup must stay in starting config).
- R105 → cited-by/cites **G414** (horizontal penalty rule) and **G415** (vertical penalty rule); cited-by R101.
- G414 ↔ R105, G415 ↔ R105 (each defines the foul tiers for its axis).
