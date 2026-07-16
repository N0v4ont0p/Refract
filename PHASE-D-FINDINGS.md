# Phase D findings — final hardening, Part 1

Per ROADMAP.md's D1: a real final inspection across all 5 skills before the website. Not a
formality — one real bug was caught and fixed along the way (R101).

---

## Rule-7 staleness re-check — exercised for real, not just confirmed to exist

`GITHUB_TOKEN=$(gh auth token) python3 corpus-input-scan.py --libraries`, live:

| Library | Result |
|---|---|
| FTCLib | CURRENT |
| RoadRunner | CURRENT |
| EasyOpenCV | CURRENT |
| FTC Dashboard | CURRENT |
| Pedro Pathing | CURRENT |
| **FTC SDK** | **STALE** — docs fetched 2026-07-12, real release `v11.2` published 2026-07-15 |

REV Robotics, Limelight, and goBILDA build guides remain outside this check (vendor docs/PDFs,
no GitHub release feed — unchanged from Phase C, not a gap in this pass).

**FTC SDK STALE, characterized, not just flagged**: fetched `v11.2`'s real release notes. It's an
offseason release whose stated breaking change is a minimum-toolchain bump (Android Studio Narwhal
3 Feature Drop or later). Checked whether this contradicts anything currently stored —
`dev-environment-setup.md` and `sdk-overview.md`/`opmode-basics.md` mention Android Studio
generically but never claimed a specific version, so this is an omission being closed, not a
correction of something wrong. Added a clearly-sourced addendum to
`refract-suite/ftc-shared-foundation/references/library-docs/ftc-sdk/dev-environment-setup.md`
citing the actual GitHub release (Tier-1), not blended into the original fetched content or the
original "Fetched:" date (that page wasn't re-scraped, only this one fact was checked against its
own source).

---

## Fresh eval battery — 6 real scenarios, all 5 skills touched

Six agents, each reading the *current* SKILL.md fresh (not relying on any memory of an earlier
version) and running the skill's actual scripts for real:

| Skill | Scenario | Result |
|---|---|---|
| ftc-team-config | Rookie mecanum/goBILDA-strafer elicitation, full ask/infer/confirm/handoff cycle | Regression-free — mandatory-ask set, time-gating, question ranking all matched SKILL.md exactly; declined to write code, described handoff only |
| ftc-hardware-lookup | Seeded-SKU spec+ratio math, then a deliberately unseeded SKU | Regression-free — real numbers on the seeded part, clean abstain (exit 3, real reason, known-SKU pointer) on the unseeded one |
| ftc-rule-check | New scenario: expansion-hub separate-battery legality | Regression-free — full 5-part flow ran for real (freshness UNVERIFIABLE, correctly carried into the verdict; R601/R602/R605 lookup+verify; verdict illegal, citations byte-quotable) |
| ftc-construct | RoadRunner re-test (autonomous + teleop, real trajectory-building + localizer gap) | Regression-free — trajectory calls grounded to exact doc lines; localizer/pose-read still absent from the docs, correctly stubbed with a TODO, not fabricated; matches the Phase B finding and standing-principles §10's own citation of it |
| ftc-construct | goBILDA re-test (viper-slide soft limit) | Regression-free — guide re-confirmed to still lack the net-travel figure; generation abstained immediately (no repeated searching), fail-safe placeholder + TODO shipped, not a fabricated number |
| ftc-code-review | **New** legality-flavored existing-code scenario (turret expansion-limit question — deliberately different from Phase C's flywheel/R207 case) | **§5 generalizes correctly** — real freshness check (UNVERIFIABLE, carried forward), real rule IDs found by grep (G414/R105/R101), real lookup+verify, verdict `ambiguous` (correctly — code alone can't establish physical constraint compliance). Ordinary §§1-4 review ran alongside it unmodified and surfaced real findings. **Also surfaced R101 (below)** — a real config-discovery bug, not previously known. |

---

## R101 — a real bug, caught live, fixed at root cause

The CR legality re-test above ran `config_lint.py` without `--config` and got a **silent
false-negative**: the script's old discovery logic (`Path(".").rglob("team-config.yaml")`,
unscoped from the working directory) picked up `32008teamcode/team-config.yaml` — an unrelated
file — instead of the fixture's own config, and reported `clean: true` when a real finding existed.

Root cause, not the symptom: the search went the wrong direction. `team-config.yaml` conventionally
lives at the project root, a *sibling* of the code directory being reviewed, not nested inside it —
searching downward from an arbitrary CWD was never reliable, in this repo or any real one with more
than one stray config file lying around (test fixtures, reference material).

**Fixed**: `find_config()` now walks *up* from `code_dir` through its ancestors, stopping at the
first (closest) match — deterministic by construction, bounded at the git repo root. Re-verified
against the exact failing scenario: now correctly finds the fixture's own config, correctly reports
`clean: false` with the real finding, exit 1. Self-test extended to cover both the sibling-discovery
case and the original "must not pick up an unrelated config" case. Fixed identically in both the
source and plugin copies (`.claude/skills/ftc-code-review/scripts/config_lint.py` and its plugin
mirror), confirmed byte-identical. Full record: TRACEABILITY.md R101.

---

## R100 self-scan — this project's docs, checked against its own new rule

Grepped ROADMAP.md, TRACEABILITY.md, and all 5 skills' SKILL.md files across several passes for
unhedged, total-sounding phrasing ("fully verified", "always", "100%", "guarantees", "catch all",
"without exception", etc.). Every hit was read in context and judged individually — most were
either negated ("don't imply the snapshot is guaranteed current"), precisely bounded ("6/6 evals" —
a specific, real count, not an unbounded claim), or describing a baseline/comparison condition, not
Refract's own behavior.

**One genuine finding**: `ftc-code-review`'s TRACEABILITY.md sign-off row said "linters catch all
needles regardless of repo size" before the qualifying "3 [test needles]" appeared later in the same
sentence — accurate once read in full, but the first mention could mislead a skimmer into reading it
as an unbounded coverage claim ("catches every possible bug") rather than the actual, defensible,
narrower claim (a deterministic pattern-match always fires on its own pattern, regardless of scale —
verified independently: neither `config_lint.py` nor `failure_mode_lint.py` makes any LLM/API call,
confirmed by reading both scripts directly). Tightened at first mention to scope it explicitly, not
rewritten wholesale — the substance was correct, only the first-read clarity needed fixing.

No other claim required correction. This is itself evidence for R100's own thesis: the claims found
here were already either hedged or precisely bounded; the one exception was a wording-clarity gap
around an otherwise-true claim, not a claim that had actually been fabricated or gone unverified.

---

## Corpus depth expansion — checked, nothing to expand this pass

`corpus-input-scan.py --team-repos` (real, authenticated GitHub search): **0 new candidates** beyond
the 9 already-mined teams. No padding attempted — an honest "nothing found" is the correct outcome
here, not a reason to lower the bar or manufacture an addition.
