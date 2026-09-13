---
name: ftc-rule-check
description: 'Citation-grounded FTC rules compliance: delivers legal/illegal/ambiguous verdicts with verified rule citations for "is X legal" questions, inspection readiness, scoring and gameplay rules, robot-size/mechanism restrictions, and Team Update changes. Use whenever the user asks about legality, compliance, penalties, inspection, or whether a mechanism, part, material, or strategy is allowed — even when the question is mixed with hardware or strategy concerns — and whenever any part of an answer would rest on what the Competition Manual says. Never answer a rules question from memory; this skill grounds every verdict in the tagged manual with cross-reference traversal.'
---

# FTC Rule Check

"Is X legal" is not a retrieval question — it's a reasoning question about how rules interact, and
the wrong answer gets a robot disqualified at inspection. The manual is retrievable; the trap is
answering from a confident memory of a rule that a Team Update changed, or citing a rule number that
doesn't exist. Two hard rules:

1. **Rule text comes from `rules.py lookup`, never from memory.** The manual updates weekly in-season,
   and **rule numbers are reused every season with different text** (DECODE R101 was the 18-inch cube;
   in BIOBUZZ that's R102 and R101 is "It is your team's ROBOT"). Your recall is a snapshot of an
   unknown date *and* an unknown season.
2. **Every citation is verified to exist before the answer ships** (`rules.py verify`). A cited rule
   number is checkable — so check it. An unverified citation is worse than no citation: it looks
   authoritative and isn't.

Read `references/standing-principles.md` (suite root) first — its abstention, Rule-7 tiering, and
confidence-driven-drift sections are the spine here. Paths below are relative to the suite root.

## Files

| File | Role |
|---|---|
| `scripts/rules.py` | `lookup` (rule + one-hop cross-refs), `verify` (citation existence), `section` (manual body text by section number — scoring, field, point values), `term` (Glossary definition); all take `--season` |
| `references/rules/<season>/` | one tagged corpus per season (see its `README.md` / `STATS.md` for counts) |
| `.claude/skills/ftc-hardware-lookup/references/manual-tables/<season>/` | legal-parts tables — read by pointer when a verdict turns on one |

## The verdict flow

### 0a. Pin the season

Decide which season the question is about **before** retrieving anything. Default is
`season-extensions/ACTIVE`; if the user names a game ("in BIOBUZZ…", "last season's DECODE rule…")
or the question's terms belong to one game (POLLEN/NECTAR/HIVE/FLOWER = BIOBUZZ;
ARTIFACT/CLASSIFIER/GATE = DECODE) and that isn't ACTIVE, pass `--season <slug>` to every script
below and say which season you answered for. If the question could be about either and the answer
differs, ask. Every `rules.py` output echoes `season` and `manual` — check it matches before quoting.

### 0. Check corpus currency first

```bash
# NOTE: this one lives at the SUITE ROOT (shared, reused for season transitions), not in this
# skill's scripts/ — run it from the suite root (the dir with core-feature-model.yaml):
python3 scripts/check_freshness.py      # checks the ACTIVE season (or --season <slug>)
```

(This skill's own `rules.py` below is skill-local: `.claude/skills/ftc-rule-check/scripts/rules.py`.)

A correct citation against a *stale* manual is still a wrong answer — freshness is calibrated
abstention applied to currency, not just completeness. If this reports `STALE` or `UNVERIFIABLE`
(exit 1), say so in the answer: give the verdict from the local corpus but flag that it may not
reflect the newest Team Update, and point the user to the live manual. Don't silently answer as if
the snapshot is guaranteed current. `CURRENT` → proceed without caveat. `WRONG_SEASON` → the live
manual is a different game than this corpus: this corpus is a *prior season's*. Answer from it only
if the question is explicitly about that season, and say so; otherwise switch to the current
season's corpus (or, if it isn't ingested yet, abstain and point to the live manual).

### 1. Retrieve — rule + one hop

```bash
python3 scripts/rules.py lookup <ID> <ID> --season <slug>   # the rule(s) plus their cross-referenced neighbors
python3 scripts/rules.py section 10.5.5 --season <slug>      # non-rule manual text: scoring, field, point values
python3 scripts/rules.py term CONTROL --season <slug>        # an ALL-CAPS term's Glossary definition, verbatim
```

`lookup` returns each rule's text AND one hop of cross-references in both directions (rules it cites
and rules that cite it), with the neighbors' text. That one hop is not optional decoration — "is this
mechanism legal" usually hinges on a rule the size/expansion rule points to. Reason over the returned
text, not over what you remember the rule saying. If `lookup` reports a rule `found: false`, it
doesn't exist — don't answer as if it does.

ALL-CAPS words in rule text are defined terms, and definitions decide verdicts (BIOBUZZ's CONTROL
includes *herding* — pushing an element counts toward the 4-element limit). Pull them with `term`
rather than reading the word in its everyday sense. A leading `*` on a headline is season-defined in
`asterisk_meaning`: in BIOBUZZ it marks an **Evergreen** rule — the subject recurs yearly but its
*details may change* — so it is never evidence that last season's version still applies.

### 2. Reason, then emit a structured verdict

```json
{"verdict": "legal | illegal | ambiguous",
 "citations": [{"id": "R101", "text": "<verbatim stored rule text from lookup>"}],
 "reasoning": "..."}
```

Each citation carries the actual stored rule text alongside its ID — copied **verbatim** from the
`text` field that `rules.py lookup` returned, never regenerated or paraphrased. This makes the
verdict self-verifying: the reader sees the rule the ruling rests on without a separate lookup, and
a paraphrase that drifted from the source is visible on its face. Tie the reasoning to that quoted
text. (Existence of every `id` is still checked in step 3 — the quote and the verify are two
independent guards, per the eval finding that a real-but-wrong rule number passes existence yet the
quoted text exposes the mismatch.)

### 3. Verify citations before shipping — non-negotiable

```bash
python3 scripts/rules.py verify <ID> <ID> --season <slug>   # exit 1 + a missing[] list if any ID is fake
```

If `verify` reports any missing ID, the answer is not ready — a hallucinated rule number is exactly
the failure this skill exists to prevent. Fix the citation or drop the claim; never ship an unverified
one. `verify` proves existence *in that season's manual* only: a prior season's number can exist
now with unrelated text (DECODE G416 → BIOBUZZ G416 is construction limits), which is why the
verbatim quote in step 2 is the second, independent guard. Official documents can carry stale
numbers too — BIOBUZZ Team Update 00 cites "R510 Only specific motors are allowed"; the V1 manual
numbers it R501. Cite what `lookup` returns, not what another document calls it.

### 4. When the honest answer is "ambiguous"

Low retrieval confidence, or a genuine unresolved disagreement, resolves to
`verdict: "ambiguous — worth filing a Q&A"`, not a confident guess. In this domain a confidently
wrong "legal" is worse than an admitted "unclear": the team builds the illegal mechanism. Abstention
is a correct verdict, not a failure (standing-principles §2).

**A rule whose actual boundary is drawn in a figure, not text, is ambiguous by construction if the
corpus only stores text.** Some legality questions turn on a zone polygon, a dimension diagram, or a
marked boundary that the manual defines visually — a scoring zone's exact extent (e.g. BIOBUZZ's
FLOWER scoring volume, defined by CAD Reference 10-4), which corner a zone sits in, a legal mounting
region, a size-check silhouette (BIOBUZZ R105's 24 in axis is shown only in Figures 12-1/12-2). The tagged manual corpus in this skill stores rule *text*; it does
not store or reason over figures. When a verdict would require reading a figure the corpus doesn't
carry, that is not a retrieval-confidence problem to push through with careful reading — inferring a
polygon's shape from the surrounding prose and presenting that inference as the verdict is exactly
the confident-wrong-guess this section already rules out, and the stakes are real: several of these
restrictions carry a MAJOR FOUL per violating element, not a minor deduction. State the verdict as
`ambiguous`, name specifically what the figure would need to show, and say so rather than resolve it
by prose alone.

## Q&A is clarification-tier, never rule-tier

The manual states the official Q&A doesn't supersede the rule text. So Q&A-sourced content is
presented as *clarification* ("the Q&A suggests…"), never as the rule itself, and never outweighs the
manual text. If the Q&A shows real unresolved disagreement, that's a signal for the "ambiguous" verdict
above, not a tiebreaker you get to pick.

## Tables: resolve the pointer, don't paraphrase

Many rules (legal motors, batteries, wire gauge) hinge on a manual table. Those tables live as
structured data in the hardware skill's `manual-tables/`, keyed by table ID — the rule chunk holds a
pointer, not the table contents. When a verdict turns on a table, read the table file by path and
resolve the spec from there; never paraphrase legal-parts data from the rule prose or from memory.
Summarize a table by its row classes, not by one row: BIOBUZZ Table 12-2 gives standard servos ≤ 8 W /
≤ 4 A but linear servos ≤ 1 A with power N/A, and a one-line "servos must be ≤ 8 W and ≤ 4 A" makes an
illegal linear servo look legal. Likewise, don't write "X is the only rule about Y" unless you actually
looked up the section it would live in — say "the rule that governs this is X".
That's the §8→§9 boundary, and it exists because a mangled spec in a legality verdict is the same
hazard as a mangled spec anywhere.

## Team Updates and staleness

Each rule carries an `effective_date`. A season's manual collects dozens of Team Updates (DECODE had
32, several changing thresholds and scoring rules) — so a verdict must reflect the newest applicable update, and a rule whose
`effective_date` is a Team Update (not `base-manual`) is surfaced as such: "changed by a Team Update,
effective <date>." When the live-update feed (deferred MCP layer) isn't present, and a question turns
on whether something changed after the base manual, say what the local data shows and flag that a
newer TU could exist — don't imply the snapshot is guaranteed current.

## Rule 7 and explanation depth

Rule-tier (manual) outranks clarification-tier (Q&A); anything from a community reading is tier-2 and
labeled so (standing-principles §3). `experience: rookie` means explain the *why* of a ruling and
point to the rule to read — never a softer or different verdict (§5).

## Not this skill

Hardware specs and the table *values* (ftc-hardware-lookup — though this skill reads those tables by
pointer), robot config and code generation (ftc-team-config), code review (ftc-code-review). A
hardware or strategy question wearing a legality coat still answers here; a pure spec question doesn't.
