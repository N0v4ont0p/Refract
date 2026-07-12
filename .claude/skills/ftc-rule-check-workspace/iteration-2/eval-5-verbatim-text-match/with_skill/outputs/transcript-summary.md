# Transcript summary — team number display question

Followed `ftc-rule-check/SKILL.md` in order: read skill in full → step 0 currency check → step 1 retrieve (lookup + one hop) → step 2 structured verdict → step 3 verify.

## Commands run (with key output)

### Step 0 — currency check (SKILL step 0)
```
python3 scripts/check_freshness.py    # exit 1
```
Output (key fields):
```json
{"season":"decode-2025-26","stored_incorporates_through":"Team Update 32",
 "live_tu":null,"status":"UNVERIFIABLE","flag":true,
 "reason":"could not read a live Team Update number ... treat corpus as possibly stale and say so in the answer"}
```
→ Exit 1 / `UNVERIFIABLE`. Per SKILL step 0, gave the verdict from local corpus but flagged possible staleness in answer.md and pointed to the live manual.

### Locating the governing rules
```
grep ... rules.json          # surfaced ROBOT SIGN text
python3 (json scan)          # mapped text -> rule_id: R401, R402, R403, G411 (also G303)
```

### Step 1 — retrieve rule + one hop (SKILL step 1)
```
python3 .claude/skills/ftc-rule-check/scripts/rules.py lookup R401 R402 R403 G411
```
Returned `found: true` for all four. The one-hop cross-references off **R402** surfaced **R403** (cites) and **G303** (cited-by) — G303 is the inspection/match-start hook, found via the mandated one hop, not from memory.

### Step 3 — verify citations (SKILL step 3)
```
python3 .claude/skills/ftc-rule-check/scripts/rules.py verify R401 R402 R403 G411 G303 I305    # exit 0
```
Output: `"all_valid": true`, `"missing": []`. Every ID cited in answer.md exists. No hallucinated rule numbers shipped.

## Verbatim-text provenance confirmation

**Every `text` field in the answer.md structured verdict was copied verbatim from the `rules.py lookup` JSON output above — not typed from memory.** Specifically:

- **R403, R401, R402, G411** text: copied directly from the `lookup R401 R402 R403 G411` output's `text` fields.
- **G303** text: copied from the `cross_references_one_hop` block returned under R402 in the same lookup output (it was not queried standalone; it came from the mandated one-hop traversal).

Fidelity preserved including the special characters as stored (`≥`, the curly apostrophe in "ROBOT'S", the "Figure 12-54" typo in R402's stored text, and R403's trailing "12.5 Motors & Actuators" section-header bleed). These artifacts are present because the text was pasted from tool output, which is the check that it was not paraphrased or regenerated from recall.

## Verdict emitted
`illegal (to run WITHOUT a displayed team number) — displaying it is mandatory`, high confidence on rule content, with a currency caveat (freshness UNVERIFIABLE). All effective dates are `base-manual` (no Team Update changed these rules in the local corpus).
