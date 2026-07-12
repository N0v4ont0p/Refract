# Transcript summary — 30 AWG drive-motor-lead legality (with skill)

## Question
"We want to run 30 AWG wire for our drive motor power leads to save weight. Is that within spec?"

## Files read
- `.claude/skills/ftc-rule-check/SKILL.md` — read in full first (per instructions).
- `references/standing-principles.md` (suite root) — abstention, source tiering, deterministic-first, confidence-driven-drift.
- `.claude/skills/ftc-rule-check/references/rules/rules.json` — searched for the wire-sizing rule.
- **`.claude/skills/ftc-hardware-lookup/references/manual-tables/table-12-8.json`** — the table file that holds the actual wire-gauge requirement (read by pointer, per the §8→§9 table-resolution rule in SKILL.md).

## Commands run (key output)
- `find` for `rules.py`, `references/rules`, `standing-principles.md` — located skill scripts/data.
- Python scan of `rules.json` for `awg` / `gauge` / `wire` — surfaced R607, R611, R615, R616, R712 as wire-related.
- `python3 scripts/rules.py lookup R607` → general "appropriately gauged/rated" principle, no specific gauge (0 cross-refs).
- `python3 scripts/rules.py lookup R615` → **the wire-sizing rule**: "All circuits shall be wired with appropriately sized insulated copper wire … Table 12-8: Wire sizing requirements [[TABLE:12-8]]." Also contains the parallel-strands prohibition. `effective_date: base-manual`, 0 cross-refs returned.
- `python3 scripts/rules.py verify R615 R607` → `all_valid: true`, `missing: []`. Both citations exist.

## Where the wire-gauge requirement value came from
From **Table 12-8 (Wire sizing requirements)**, file `table-12-8.json`, DECODE Competition Manual (2025-2026) — NOT from the rule prose or from memory. R615 holds only a `[[TABLE:12-8]]` pointer; the numeric minimums live in the hardware skill's structured table, read directly by path per SKILL.md ("resolve the pointer, don't paraphrase") and standing-principles §1/§7.

Relevant values pulled from the table:
- "Motor Power (unless otherwise listed)" → **minimum 18 AWG** (grouped with 12V Main Battery Power and 11–20 A fuse circuits, which share the 18 AWG cell).
- "Motor Power — TETRIX MAX 12V DC Motors, REV Core Hex (REV-14-1300)" → minimum 22 AWG (grouped with PWM/Servo, LEDs, ≤10 A fuse circuits).
- SIGNAL LEVEL circuits → minimum 28 AWG.

Table cells are vertically merged (some rows in the JSON have only one element = the application, sharing the wire-size value from the grouped row). Interpreted accordingly: 18 AWG group, 22 AWG group, 28 AWG signal row.

## Reasoning → verdict
Higher AWG number = thinner wire. 30 AWG is thinner than the 18 AWG minimum for a standard drive motor, thinner than the 22 AWG special-case (Core Hex/TETRIX), and thinner even than the 28 AWG signal-level floor. No category in Table 12-8 admits 30 AWG for motor power. R615 also bars faking a larger conductor by paralleling thin wires.

**Verdict: illegal.** Fix: use 18 AWG or thicker for drive motor power leads (22 AWG only if specifically REV Core Hex / TETRIX MAX). Noted the COTS-attached-lead exemption in R615.

## Staleness note
All cited rules are `effective_date: base-manual` in local data; no live Team Update feed available in this session, so flagged that a newer TU could exist.
