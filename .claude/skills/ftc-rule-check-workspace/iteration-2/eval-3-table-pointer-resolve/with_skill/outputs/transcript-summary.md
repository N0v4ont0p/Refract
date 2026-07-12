# Transcript summary — 30 AWG drive-motor power leads

## Skill flow followed (ftc-rule-check/SKILL.md)

### Step 0 — Corpus currency check
```
python3 scripts/check_freshness.py
```
Output (exit 1):
```json
{"season": "decode-2025-26", "stored_incorporates_through": "Team Update 32",
 "stored_tu": 32, "live_tu": null, "status": "UNVERIFIABLE", "flag": true,
 "reason": "could not read a live Team Update number (no marker on page); treat corpus as possibly stale and say so in the answer"}
```
→ Flagged in answer; verdict given from local corpus with a staleness caveat.

### Locate the governing rule
```
grep / python3 scan of references/rules/rules.json for AWG|wire|gauge + table_pointers
```
Found **R615 "Use appropriately sized wire"**, `table_pointers: ["12-8"]`, effective_date `base-manual`.

### Step 1 — Retrieve (rule + one hop)
```
python3 .claude/skills/ftc-rule-check/scripts/rules.py lookup R615
```
Returned R615 text verbatim (requires wire per Table 12-8; parallel-wire workaround explicitly banned; COTS/manufacturer leads exempt). `cross_references_one_hop: []`.

### Tables — resolve the pointer (§8→§9)
Read the table file directly (not paraphrased):
```
.claude/skills/ftc-hardware-lookup/references/manual-tables/table-12-8.json
```
Key rows (minimum = thinnest/largest-AWG allowed):
- Motor Power (unless otherwise listed) → **18 AWG**
- Motor Power — TETRIX MAX 12V DC / REV Core Hex REV-14-1300 → **22 AWG**
- SIGNAL LEVEL circuits → **28 AWG**

Merged-cell reading: the "Minimum Wire Size" value sits on the first row of each merged group, so "Motor Power (unless otherwise listed)" and "11–20A fuse protected circuit" both fall under the 18 AWG value; the 22 AWG group covers TETRIX/REV Core Hex, PWM/Servo, LEDs, and ≤10A circuits.

### Step 3 — Verify citation
```
python3 .claude/skills/ftc-rule-check/scripts/rules.py verify R615   # exit 0
```
```json
{"exists": {"R615": true}, "missing": [], "all_valid": true}
```

## Result
30 AWG < 18 AWG minimum for standard motor power (and < 22 AWG even for the exempt small-motor category, and < 28 AWG signal minimum). **Verdict: ILLEGAL.** R615 also forbids paralleling thin wires to fake a larger cross-section.
