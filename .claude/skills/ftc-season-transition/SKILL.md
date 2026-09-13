---
name: ftc-season-transition
description: 'Maintainer workflow that moves Refract from one FTC season to the next, or ingests a new Team Update into the current season: stages the official Competition Manual and Team Updates, re-tags the rules corpus per season, drafts the season extension from the manual with citations, audits season coupling, refreshes per-season evals, and gates the season-extensions/ACTIVE flip on a deterministic readiness check plus human sign-off. Use when a new FTC game is released ("the new game dropped", "kickoff", a new manual or season name), when a Team Update is published, when check_freshness reports STALE or WRONG_SEASON, or when asked to switch Refract to a new season. Not for answering rules questions (ftc-rule-check) or team robot config (ftc-team-config).'
---

# FTC Season Transition

PLAN.md §19 as a runnable procedure, written from the first real run (DECODE 2025-26 → BIOBUZZ
2026-27, kickoff 2026-09-12; full record in `SEASON-TRANSITION-BIOBUZZ.md` and TRACEABILITY §29).
The lesson of that run: a season change is **not** a one-file swap. Rule numbers, table IDs, field
geometry, AprilTag IDs, scoring-element physics, lint tokens, template examples and team configs are
all season data, and each one silently gives a well-formed wrong answer if left keyed to last season.

Read `references/standing-principles.md` §7 (canonical per-season paths) first. Nothing about the
new game comes from memory: your training predates it. Every value written into the suite is a
quote from a fetched official source or a script output, and research subagents' claims are
re-verified by script or text grep before they are written anywhere.

## Scripts

| Script | Role |
|---|---|
| `scripts/stage_manual.py --season <slug> --game <NAME>` | fetch manual HTML/PDF + every Team Update → `corpus-staging/manual-<slug>/` with `SOURCES.md` hashes; refuses a page that doesn't name the game |
| `.claude/skills/ftc-rule-check/scripts/tag_manual.py --season <slug> [--out-root DIR]` | deterministic rules/sections/glossary/tables per season (add the season to its `SEASONS` registry first) |
| `scripts/check_freshness.py --season <slug>` (suite root) | CURRENT / STALE / WRONG_SEASON / UNVERIFIABLE |
| `scripts/transition_check.py --season <slug>` | readiness gate for the ACTIVE flip; exit 0 = everything but sign-off is in place |

## Detect

`check_freshness.py` on the ACTIVE season. `WRONG_SEASON` → new game (FIRST reuses the manual URL).
`STALE` → new Team Update for the same game: skip to **Team Update loop**.

## New season

1. **Stage.** `stage_manual.py --season <game>-<yyyy>-<yy> --game <GAME>`. Slug years order seasons
   (the validator compares them).
2. **Register + tag.** Add the slug to `tag_manual.py`'s `SEASONS`: `in_dir`, `meta.game_name`,
   `incorporates_through`, `source_url`, `tu_index_url`, and `asterisk_meaning` **quoted from the
   new manual's conventions section** (it changed meaning between DECODE and BIOBUZZ). Dry-run with
   `--out-root` into the scratchpad, then read `STATS.md`:
   - rule count vs an independent method (BIOBUZZ: count the HTML's rule-headline paragraph classes)
   - `SERIES (legend)` matches the manual's "X for Section N" list
   - `TABLES not linked`, `TABLES cited, not extracted`, `LONGEST rule chunk` (a huge chunk = swallowed
     prose), dangling citations (a part number like `C270` colliding with a series letter goes in
     `non_rule_tokens` with its evidence)
   - re-run the previous season's tagging and diff against its committed corpus: the tagger must
     still reproduce it (or every change must be explained)
   Then write for real and mirror `rules/` + `manual-tables/` to `refract-suite/skills/…`.
3. **Draft the season extension** (`season-extensions/<slug>.yaml`, both copies) from the manual only:
   `game_name`, scoring elements, field facts, match timing, scoring/RP tables, `season_mechanisms`
   (same list shape as prior seasons; every key justified by a rule), `code_tokens` for every mechanism
   (`[]` = not lintable by name), `code_constraints` (rule, text, applies_to, optional `detect`/`unless`
   regex — verify each regex against a real positive and negative file, and verify API claims by
   compiling, not by reading release notes), `constraints_on_mechanisms`, `deliberation_checkpoint`
   (open questions, manual inconsistencies). `UNKNOWN` when the text doesn't say; `FIGURE-ONLY` when
   only a figure/CAD says. Official non-rule docs (field setup guide, SDK release notes) are labeled as
   such. Mark `_meta.status: DRAFT_FROM_MANUAL`, `not_active: true`.
4. **Research in parallel (read-only subagents), verify before writing:** game-content extract with
   citations; rule-by-rule R/I-series diff vs last season (servo counts, expansion, streaming, energy
   storage); online sources around the manual (Team Updates, field setup guide, SDK release, ecosystem
   StarterBots as tier 2); coupling audit of every file still keyed to last season (rules paths,
   template examples, physics constants, lint tokens, docs with last season's tag IDs/coordinates,
   pattern `season_scope`, eval fixtures).
5. **Season-scope the rest:** physics constants per element (`physics/<slug>/<element>.json`, only
   from measured or tier-1 mass/diameter — otherwise the solver abstains); tag last season's
   library docs with a SEASON SCOPE header (never edit upstream text); give new corpus patterns a
   `season_scope`; label template examples by season.
6. **Evals:** `evals/<slug>.json` per skill with script-verified ground truths (renumbered-rule traps,
   carried-forward limits, the new season's code-legality rules, figure-only abstentions, a
   prior-season question), plus at least one fixture stamped `_meta.season: <slug>`. Run the eval loop
   (with/without skill, graded) and fix what fails.
7. **Gate + sign-off.** `transition_check.py --season <slug>` must exit 0. Present the deliberation
   checkpoint (mechanism taxonomy, open questions, manual inconsistencies) to the human. Only after an
   explicit yes: set `_meta.status: live`, `not_active: false`, write the slug into **both**
   `season-extensions/ACTIVE` files, re-run the gate, all fixtures, and the eval regression. Existing
   team configs then report "re-elicit the season layer (core axes carry over)" — that's intended.

## Team Update loop

`stage_manual.py` again (it picks up every `tu-NN`), bump `incorporates_through` in `SEASONS`, dry-run
`tag_manual.py`, diff rules/tables against the committed corpus, and write each changed rule into the
season yaml's affected fields/constraints. Q&A answers (from the date the manual opens Q&A) are
`clarification` tier: record them against the rule, never as rule text.

## Never

- Flip ACTIVE without the gate passing and a human yes.
- Copy a value from last season's corpus, template, or patterns as the new season's fact.
- Resolve figure-only geometry from prose, or treat another official document's rule number as the
  manual's (BIOBUZZ Team Update 00 called R501 "R510").
- Promote tier-2/3 web material (vendor listings, community threads) into rules, tables, or physics.
