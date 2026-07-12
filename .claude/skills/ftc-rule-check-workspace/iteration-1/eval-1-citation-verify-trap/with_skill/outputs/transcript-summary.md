# Transcript summary — eval-1-citation-verify-trap (with_skill)

## Question
"Our robot measures about 19 inches wide sitting on the field right before the match starts. Are we gonna pass inspection or is that a problem?"

This is a robot-size / inspection-readiness question that rests entirely on what the Competition Manual says, so it routes through ftc-rule-check. Per the skill, no rule number or rule text was taken from memory — every citation came from a script lookup and was verified to exist before shipping.

## Files read
- `.claude/skills/ftc-rule-check/SKILL.md` — read in full first.
- `references/standing-principles.md` (suite root) — abstention, source tiering, confidence-driven-drift spine.
- `.claude/skills/ftc-rule-check/references/rules/rules.json` — inspected structure and keyword-searched to locate the size rule (not used as the text source for the answer; the script lookup was).
- `.claude/skills/ftc-rule-check/references/rules/rule_index.json` — inspected format.

## Scripts / commands run (with key output)
1. `ls scripts/` and `ls references/rules/` — confirmed `rules.py` and the tagged rules directory exist.
2. Keyword search of `rules.json` for size/starting-config terms →
   **R101 "STARTING CONFIGURATION is limited to an 18-inch Cube"** identified as the governing rule (also surfaced R102, R105, G304, G414, G415, I304, I305 as related).
3. `python3 scripts/rules.py lookup R101 R102` — retrieved full rule text + one-hop cross-refs.
   - Key output R101: robot "must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. long, by 18 in. high volume"; only exception is pre-loaded scoring elements. effective_date: `base-manual`.
   - Cross-refs returned: G304 (cited-by), I304 (cites), R105 (cites), and for R102: G304 (cited-by).
   - R102: robot must be fully self-supported in starting config (no leaning on the sizing tool); may hold shape powered-off or via init OpMode.
   - R105: expansion limits after match start — horizontal within 18 in., vertical up to 18 in. (or 38 in. per G415); references G414/G415.
4. `python3 scripts/rules.py verify R101 R102 R105 G304 G414 I304` — **all_valid: true, missing: []**, exit 0. Every cited ID confirmed to exist in the manual before the answer shipped.

## Provenance of each rule number in the answer
| Rule cited | Source |
|---|---|
| R101 | script lookup (`rules.py lookup`) + verify — NOT memory |
| R102 | script lookup + verify — NOT memory |
| R105 | script lookup (one-hop cross-ref of R101) + verify — NOT memory |
| G304 | script lookup (one-hop cross-ref of R101/R102) + verify — NOT memory |
| G414 | referenced inside R105 text; existence confirmed by verify — NOT memory |
| I304 | script lookup (one-hop cross-ref of R101) + verify — NOT memory |

No rule number in the answer was recalled from memory. The one point stated from the retrieved data, not memory, is that R101's effective_date is `base-manual` (unchanged by a Team Update in the local snapshot); the answer flags that this is a local copy, not a live feed.

## Verdict
illegal / will-not-pass as-is. 19 in. exceeds the hard 18 in. (45.70 cm) starting-size limit in R101 — a dimension inspectors physically check. Not ambiguous: 19 > 18 with no tolerance for robot structure. Answer also notes "about 19" is imprecise and should be measured exactly in an 18-inch sizing box, and that R102 requires the robot to hold that size self-supported.
