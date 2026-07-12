# DECODE Competition Manual — tagged rules corpus

Generated deterministically by `../../scripts/tag_manual.py` (no model in the
extraction; §8, operating rule 1). Regenerate with:

```
python3 .claude/skills/ftc-rule-check/scripts/tag_manual.py
```

## Provenance
- **Source:** DECODE Competition Manual, HTML edition — https://ftc-resources.firstinspires.org/ftc/game/cm-html
- **Version:** incorporates through **Team Update 32**
- **Retrieved:** 2026-07-03
- **Tier:** `rule` (manual body text). Q&A-sourced content, when ingested, is
  tagged `clarification` — it does not supersede rule text (§8 step 4).
- **effective_date:** `base-manual` (Team Update diffs get their own dates via the §18 live feed, not this static pass).

## Files
- `rules.json` — 212 rule chunks. Each: `rule_id, series, short_title, text,
  marked_carryover, section_path, table_pointers, manual, tier, effective_date`.
- `cross_refs.json` — 130 rule→rule citation edges `{from_rule, to_rule, cite_text, to_rule_found}`.
- `rule_index.json` — every rule ID, by series (the whole-manual index used to resolve citations).
- `dangling_citations.json` — citations whose target rule doesn't exist anywhere
  in the manual. **Currently empty** — every cross-reference resolves. A non-empty
  entry here is a FLAG FOR HUMAN REVIEW (possible stale cross-ref from a Team
  Update, or a manual typo), per F4.
- `section_map.json` — TOC-anchored heading positions used for `section_path`.
- `STATS.md` — run stats.

## Conventions captured
- **Rule series = A, E, G, I, R, T.** Each maps cleanly to one manual section
  (I→§3 Inspection, E→§5 Event, A→§6 Awards, G→§11 Game, R→§12 Robot,
  T→§13 Tournament) — this series↔section coherence is an internal correctness check.
- **`marked_carryover: true`** = the manual printed this rule's headline in bold
  green with a leading asterisk, which §1.6 ("This Document & Its Conventions")
  defines as *"relatively unchanged from season to season."* CONFIRMED from the
  manual's own legend, not inferred. 196 of 212 rules are carryover.

## §8↔§9 table mechanism
Tables embedded in rules are NOT stored as prose here. Each is extracted to a
structured file under `ftc-hardware-lookup/references/manual-tables/table-<id>.json`
and referenced from the citing rule chunk by a `[[TABLE:<id>]]` pointer (see a
rule's `table_pointers`). 38 tables, 38 pointers. A legality question that turns
on a table resolves the pointer into the deterministic §9 data — the spec never
comes from prose an LLM could mangle. (Inline part-number mentions in rule prose,
e.g. "REV Control Hub (REV-31-1595)", are rule text and correctly remain.)

## QA performed on this run
- §12.6 regression: reproduces the human-approved sample exactly (R601–R619, 14 edges).
- Coverage: every in-series rule ID appearing in the manual is indexed (0 missing, 0 spurious).
- Table-leak scan: 0 tables leaked into rule prose.
- Deterministic-vs-LLM edge diff on the §12.6 sample: exact agreement (a *fidelity*
  check, not Rule-7 corroboration — both read the same document; staleness is §18's job).
