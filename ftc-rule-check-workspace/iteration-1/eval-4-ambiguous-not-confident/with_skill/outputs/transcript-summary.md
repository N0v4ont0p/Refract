# Transcript summary — eval-4 (silicone traction spray on mecanum wheels)

## Files read
- `.claude/skills/ftc-rule-check/SKILL.md` (in full, first)
- `references/standing-principles.md` (suite root) — abstention (§2), source tiering (§3), confidence-driven drift (§6)
- `.claude/skills/ftc-rule-check/references/rules/rules.json` (structure inspection + keyword search)
- Rule data via script (below); did not need the manual-tables pointer — no verdict turned on a legal-parts table value.

## Commands run (with key output)
1. `ls -R references scripts` — confirmed rule data layout (rules.json, cross_refs.json, rule_index.json, scripts/rules.py).
2. Python keyword scan of `rules.json` text for traction/tile/damage/liquid/spray/lubricant/silicone terms. Surfaced the on-point rules: **R201** (Do not damage the TILE floor), **R203** (safety/fair play), **R205** (Do not make a mess on the FIELD), **G412** (Don't damage the FIELD). Also noise: E510 (aerosols in approved areas — venue rule, not robot legality).
3. `python3 scripts/rules.py lookup R201 R203 R205 G412` — retrieved full text + one-hop cross-refs. Key findings:
   - **R205**: explicitly bans "liquid or gel materials," "tire sealant," and lubricants that contaminate the FIELD; lubricants allowed only to reduce friction *within* the ROBOT. Directly covers a sprayed-on wheel coating at the tile contact surface.
   - **G412**: defines FIELD damage to include "contaminating the FIELD with a liquid or fine solid as in R205"; penalty ladder VERBAL WARNING → DISABLED → YELLOW CARD. This is the in-match enforcement path.
   - **R201**: about physical traction-device surface features damaging tiles — related but not the direct hit for a coating.
   - Cross-ref traversal confirmed R205 ↔ G412 ↔ R201/G407 form the relevant cluster.
4. `python3 scripts/rules.py verify R201 R203 R205 G412 G407` — `all_valid: true`, `missing: []`, exit 0. All citations confirmed to exist before shipping.

## Verdict given
**Definite verdict: illegal / not allowed as described** — primary basis **R205** (contaminating the FIELD with a liquid/gel coating), enforced in-match via **G412**. Told the team clearly not to spray the wheels, plus practical notes (silicone is a lubricant → *reduces* grip on tile, and slicks shared tiles = fairness/safety problem) and legal alternatives (grippier wheel hardware within R201, weight/tuning, alcohol-clean wheels).

## Was it flagged ambiguous, and why
I gave a definite "no," but explicitly flagged the **narrow ambiguity band honestly** rather than overclaiming: the manual never names "silicone traction spray" by product, and whether a given surface treatment "contaminates" is ultimately an LRI/Head-Ref judgment. The genuine gray area — a hypothetical fully-cured, zero-residue coating — is not resolved by the manual, so that specific case is a "check with LRI / file an official Q&A" situation. But silicone traction spray is not that product (it stays wet/slick and transfers), so for the question as asked the honest answer is a confident "not allowed," not a coin-flip "ambiguous." This follows standing-principles §2/§6: I did not soften to a false "legal," and I did not manufacture false certainty at the true edge either. Staleness noted: base-manual rules, a newer Team Update could exist; confirm against current manual/Q&A.
