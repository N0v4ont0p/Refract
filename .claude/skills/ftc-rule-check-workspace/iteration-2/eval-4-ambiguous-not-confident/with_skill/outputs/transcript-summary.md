# Transcript Summary — ftc-rule-check (with skill)

**User question:** "Is it legal to spray our mecanum wheels with silicone traction spray for extra grip on the tiles? Does the manual allow that?"

## Process (followed SKILL.md verdict flow)

### Step 0 — Corpus currency check (required first)
```bash
python3 scripts/check_freshness.py    # EXIT 1
```
Key output:
```json
{"season": "decode-2025-26", "stored_incorporates_through": "Team Update 32",
 "stored_tu": 32, "live_tu": null, "status": "UNVERIFIABLE", "flag": true,
 "reason": "could not read a live Team Update number (no marker on page); treat corpus as possibly stale and say so in the answer"}
```
Result: `UNVERIFIABLE` → staleness caveat included in the answer (verdict from local snapshot, flag that a newer TU could exist, point to live manual/Q&A).

### Step 1 — Retrieve (rule + one-hop cross-refs)
Located rules.py at `.claude/skills/ftc-rule-check/scripts/rules.py`. Grepped `rules.json` for traction/material/contamination terms, surfacing candidate rules R201, R203, R205 (plus E510, G412).

```bash
python3 .claude/skills/ftc-rule-check/scripts/rules.py lookup R205 R201 R203
```
Key findings:
- **R205** ("Do not make a mess on the FIELD") — directly on point. Prohibits materials that if released would contaminate the FIELD / require clean-up; lubricants allowed only "within the ROBOT"; lists "liquid or gel materials" and "tire sealant" as violating examples.
- **R201** ("Do not damage the TILE floor") — traction devices must not damage tile; context for grip-on-tile intent.
- **R203** ("Design ROBOTS for safety and fair play") — hazardous materials list; not the primary hook.
- One-hop cross-reference surfaced **G412** ("Don't damage the FIELD"), which explicitly defines FIELD damage to include "contaminating the FIELD with a liquid or fine solid as in R205" → verbal warning / DISABLED / yellow card. This one-hop neighbor was the decisive corroborator.

### Step 2 — Reasoning → structured verdict
Verdict: **illegal**. Silicone traction spray applied to the tile-contacting wheel tread is designed to sit where it transfers onto the shared field = contamination under R205; R205's lubricant allowance is limited to "within the ROBOT" and does not cover an external tread coating; G412 makes it callable as FIELD damage in-match. One honest gap noted: the product is not named by the manual, so a Q&A gives definitive certainty. Verdict rendered with verbatim rule text copied from the `lookup` output.

### Step 3 — Verify citations (non-negotiable)
```bash
python3 .claude/skills/ftc-rule-check/scripts/rules.py verify R205 R201 R203 G412
```
Output:
```json
{"exists": {"R205": true, "R201": true, "R203": true, "G412": true},
 "missing": [], "all_valid": true}
```
All citations verified (exit 0). Answer shipped.

## Files written
- `answer.md` — verdict-tier answer with verbatim R205/G412/R201 text, freshness caveat, Q&A pointer, and legal grip alternatives.
- `transcript-summary.md` — this file.
