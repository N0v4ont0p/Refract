**Verdict: ILLEGAL.** Your software limit doesn't count. The arm can physically reach 32 in., and the height limit is 29 in., so it fails as built. (Season: BIOBUZZ 2026-27, Competition Manual V1 including Team Update 00. The freshness check came back CURRENT: live TU 0 matches the stored TU 0.)

```json
{
  "verdict": "illegal",
  "citations": [
    {"id": "R105", "text": "A. After the start of the MATCH, ROBOTS may expand beyond the STARTING CONFIGURATION but at all times must remain within a 18 in. (45.70 cm) by 24 in. (61.0 cm) by 29 in. (73.65 cm) tall sizing volume when fully expanded per G416, B. ROBOTS must be physically constrained to fit within these limits without the use of software, and C. ROBOTS may not be designed to deliberately detach COMPONENTS. ... ROBOTS must show their maximum mechanical extensions during the inspection process. A ROBOT that can mechanically exceed the sizing limit would be in violation even if the ROBOT has software limiting the position of the extension during the MATCH. (Figure 12-3)"},
    {"id": "G416", "text": "ROBOTS may not violate the limits outlined in R105 during the MATCH. ROBOTS may not: A. expand such that they exceed the expansion limits noted in R105.A or R105.B, or B. deliberately detach parts per R105.C. Violation: VERBAL WARNING. MAJOR FOUL per instance, if STRATEGIC."}
  ],
  "reasoning": "R105.A sets the height limit at 29 in. above the field surface. R105.B says the robot must stay inside that limit without relying on software. R105 also names your exact case: a robot that can mechanically exceed the limit is in violation even if software limits the extension during the match. Your arm reaches 32 in. mechanically, so it breaks R105.B, and inspectors will have you show maximum mechanical extension. The 28 in. software cap doesn't matter. In a match, going over the limit is a G416 violation (VERBAL WARNING, or a MAJOR FOUL per instance if STRATEGIC)."
}
```

Both citations were checked with `rules.py verify` (all_valid: true). The quotes are copied exactly from `rules.py lookup`, with "..." marking cut text.

**How to fix it:** add a physical limit so the arm can't go above 29 in. from the field surface. That could be a hard stop, a shorter slide or limited travel, or a mechanical block on the pivot. Your 28 in. software limit can stay as a second layer. Measure with all wheels on the tiles, because that's how inspectors measure. Give yourself some margin under 29 in. for slop and flex in the mechanism.

**Also check:** the 18 x 24 in. footprint of the same volume applies at full extension too. If the arm reaches outward as well as up, check its horizontal reach at maximum mechanical extension. Your robot must also still fit the 18 in. cube (R102) at the start of the match.