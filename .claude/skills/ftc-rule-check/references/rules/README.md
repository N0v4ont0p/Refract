# Tagged Competition Manual corpora — one directory per season

Generated deterministically by `../../scripts/tag_manual.py` (no model in the extraction; §8,
operating rule 1). One subdirectory per season slug, matching `season-extensions/<slug>.yaml`:

```
python3 .claude/skills/ftc-rule-check/scripts/tag_manual.py --season biobuzz-2026-27
python3 .claude/skills/ftc-rule-check/scripts/tag_manual.py --season decode-2025-26
```

| season | manual | incorporates through | rules | sections | glossary |
|---|---|---|---|---|---|
| `biobuzz-2026-27` | BIOBUZZ Competition Manual V1 | Team Update 00 | 171 | 161 | 68 terms |
| `decode-2025-26` | DECODE Competition Manual | Team Update 32 | 212 | 156 | 76 terms |

Read through `../../scripts/rules.py` (`--season`, default `season-extensions/ACTIVE`), never by
opening a season directory by hand: **rule numbers are reused across seasons with different text**
(DECODE R101 = 18-inch cube; BIOBUZZ R101 = "It is your team's ROBOT", the cube is R102). Every
`rules.py` output names the season and manual it answered from. Each season's `STATS.md` has its run
stats and review flags; provenance of the staged inputs is in
`corpus-staging/manual-<slug>/SOURCES.md` (DECODE predates that file: `corpus-staging/manual/`).

## Files per season
- `rules.json` — rule chunks: `rule_id, series, short_title, text, asterisk_marked, section_path,
  table_pointers, manual, tier, effective_date`. A chunk ends at the next rule OR the next section
  heading, whichever comes first.
- `sections.json` — manual body text per numbered section (game overview, ARENA, scoring, point
  values…), tier `manual-body`: it describes the game; rules govern.
- `glossary.json` — the manual's Term/Definition table, verbatim.
- `cross_refs.json` — rule→rule citation edges `{from_rule, to_rule, cite_text, to_rule_found}`.
- `rule_index.json`, `section_map.json`, `dangling_citations.json` (non-empty = FLAG FOR HUMAN REVIEW).

## Conventions that CHANGE by season — read meta, don't assume
- **Rule series** come from the manual's own "X for Section N" legend. BIOBUZZ adds C (Section 15,
  `C301`) and declares L (Section 14) with zero numbered rules in V1. Part numbers that collide with a
  series letter (the Logitech `C270` webcam) are listed per season in `tag_manual.py`, with evidence.
- **`asterisk_marked`** — meaning is in `meta.asterisk_meaning`. DECODE: "relatively unchanged season
  to season". BIOBUZZ: **Evergreen** — subject constant, *details may change*. Never read it as
  "unchanged since last season".
- **Existence ≠ correctness of a cross-reference.** `dangling_citations.json` only catches IDs that
  don't exist. After a renumbering, a manual can cite an ID that exists but now means something else
  (BIOBUZZ V1: R601.A → R610 is wire colors, the fuse rule is R604; R903 → R203 should be R202). Those
  are recorded in the season yaml's `deliberation_checkpoint.manual_inconsistencies_found`.

## §8↔§9 table mechanism
Tables are not stored as rule prose. Each is extracted to
`ftc-hardware-lookup/references/manual-tables/<season>/table-<id>.json` and referenced from the citing
rule by a `[[TABLE:<id>]]` pointer. Table text is matched whitespace-insensitively (HTML cell text has
spaces around inline tags that page text doesn't; exact matching silently left BIOBUZZ Tables 12-1
motors, 12-2 servos, 12-8 wire sizing unlinked). Table IDs are season-scoped too: BIOBUZZ has no 12-10…12-12.

## QA per run (see STATS.md)
- Rule coverage cross-checked against an independent method — BIOBUZZ: 171 regex definitions ==
  171 rule-headline paragraphs in the HTML's own markup classes.
- DECODE regression: the season-parameterized tagger reproduced the prior committed DECODE corpus
  exactly before the heading-bound fix; the heading-bound fix then only truncated 33 over-long
  chunks (each a strict prefix of the old text, every cut at a real heading) and removed 31
  false edges that came from swallowed non-rule prose.
- §12.6 sample regression (DECODE): R601–R619, 14 edges.
