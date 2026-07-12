# Transcript Summary — expansion / arm-extension legality

Followed ftc-rule-check/SKILL.md verdict flow in order.

## Step 0 — Corpus currency check
```
python3 scripts/check_freshness.py
```
Output (exit 1):
```json
{
  "season": "decode-2025-26",
  "stored_incorporates_through": "Team Update 32",
  "stored_tu": 32,
  "live_tu": null,
  "source_url": "https://ftc-resources.firstinspires.org/ftc/game/cm-html",
  "retrieved": "2026-07-03",
  "status": "UNVERIFIABLE",
  "flag": true,
  "reason": "could not read a live Team Update number (no marker on page); treat corpus as possibly stale and say so in the answer"
}
```
→ Flagged the UNVERIFIABLE status prominently in answer.md per skill step 0.

## Rule discovery
Searched `references/rules/rules.json` by content for expansion/sizing terms. Identified the
relevant cluster: **R101** (starting 18-in cube), **R105** (expansion limits), **G414**
(horizontal foul), **G415** (vertical foul). G304 (field setup) surfaced as a neighbor.

## Step 1 — Retrieve rule + one hop
```
python3 .claude/skills/ftc-rule-check/scripts/rules.py lookup R101 R105 G414 G415
```
Key returned text (verbatim, used in answer):
- **R101** — STARTING CONFIGURATION fully self-contained in 18×18×18 in; only exception is
  pre-loaded SCORING ELEMENTS. Cross-refs: cites R105 & I304; cited-by G304.
- **R105** — after MATCH start: (A) horizontal expansion must stay within a fixed 18×18 in,
  physically constrained, NOT software; (B) vertical up to 18 in (may be software-limited);
  (C) vertical up to 38 in within G415 limits. Flexible extensions count. Cross-refs G414/G415.
- **G414** — horizontal limits per R105.A; MINOR FOUL, MAJOR if strategic benefit; damage
  exception.
- **G415** — vertical: may exceed 18 in up to 38 in ONLY (A) during final 20 s AND (B) not in any
  LAUNCH ZONE; MINOR/MAJOR FOUL.

One-hop traversal confirmed R101→R105→{G414,G415} chain, which is exactly what the "how far can we
expand" question hinges on (starting rule points to the expansion rule points to the foul tiers).

## Step 3 — Verify citations
```
python3 .claude/skills/ftc-rule-check/scripts/rules.py verify R101 R105 G414 G415
```
Output (exit 0): `all_valid: true`, `missing: []`. All four IDs exist → safe to ship.

## Verdict
LEGAL (conditional): extending arm allowed if — horizontally within fixed 18×18 in at max
*mechanical* extension (no software-only cap); vertically ≤ 18 in normal play, ≤ 38 in only in the
last 20 s and outside launch zones. Penalties G414/G415 (MINOR → MAJOR if strategic). Answer
carries the UNVERIFIABLE currency caveat.
