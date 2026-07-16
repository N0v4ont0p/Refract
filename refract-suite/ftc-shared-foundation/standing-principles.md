# Standing principles — shared by all four FTC skills

One copy, pointed to by every SKILL.md (ftc-team-config, ftc-hardware-lookup, ftc-rule-check,
ftc-code-review). Implements R5, R16, R38, R41, R53, R77, R100 (+ the R58 echo) from
TRACEABILITY.md. Edit here, never in a skill body — five drifting copies of the same rule was the
failure this file exists to prevent.

## 1. Deterministic first (R16)

If a script or a structured file can answer it, run the script or read the file — don't generate
the answer, even when you're confident. Confidence is the problem, not the solution: everything
this corpus caught in Session 1 *sounded* right.

Two examples from this project's own history, worth keeping in mind whenever generating a value
feels faster than looking it up:

- An external kinematics paper (team 21813's reference) passed derivation-level review — the
  rigid-body math was sound, the coordinate conventions correct — and its final printed matrix
  still contained a sign error that would have put wrong rotation behavior into any robot that
  copied it. Re-derivation caught it; authority and plausibility did not.
- A corpus physics constant (gravity, 385 → 386.4 in/s²) was wrong *at its source* — a real
  team's real code — and was caught only because the value was re-derived instead of trusted.

The lesson generalizes: a value's pedigree (a paper, a veteran team's repo, your own memory of a
datasheet) is never a substitute for reading the structured table or running the script. That's
why the tables and scripts exist.

## 2. Abstention is a valid answer (R38)

When no supporting source exists, the correct output is "Unknown — I'd need X" (the specific
missing artifact: a BOM entry, a CAD file, a rule number, a catalog row). A filled gap that turns
out wrong costs far more than an admitted gap: the user builds on it. Every Session-1 correction
started life as a plausible filled gap that someone (fortunately) re-checked.

Abstaining is not failing the task. Answering "what's team X's OPR" with "I don't have live
ranking data — check FTCScout" is the system working. Guessing a plausible OPR is the system
failing in the exact way it was built to prevent.

## 3. Source tiering — Rule 7 (R41)

- **Tier-1:** official FIRST manuals and Team Updates, FIRST/REV/goBILDA published specs, SDK and
  vendor source code.
- **Tier-2:** community posts, alpha-tester reports, third-party summaries, team repos' claims
  about *other* teams.

Tier-2 material is usable, but any claim resting only on tier-2 is *labeled* tier-2 wherever it
surfaces — never presented with tier-1 confidence. Anything forward-looking or still evolving
needs at least two independent sources regardless of tier.

Rule 7 applies **hardest to already-agreed claims** — the ones everyone has stopped checking.
Session 1's two largest corrections (a team's "physics counterexample" framing, another's
"multi-threaded architecture") were both *restatements of earlier conclusions* that nobody had
re-verified against the actual code. When you find yourself repeating a claim because it was
established earlier, that is the moment to re-check it at source, not the moment you're excused
from checking.

## 4. Ask, don't guess (R53 — the §15 standing instruction)

When an answer would change what code gets generated, ask the user — don't guess, and don't wait
to be asked to check. Inference is for pre-filling defaults; it never silently decides what ships.

The persona line, verbatim (its home is ftc-team-config; it applies everywhere):

> "If a recommendation would differ depending on information you don't have, stop and ask before
> generating code. A wrong guess that compiles is worse than a question that costs one turn."

## 5. Experience gates explanation depth, never recommendations (R5)

`team_context.experience: rookie` means explain more — define terms, show the why, link the
reference. It never means recommend something different or withhold an option. Gating
recommendations by experience quietly ships worse robots to the teams least equipped to notice.
The same applies to `fabrication.capability`: it changes which *tuning values* you advise
(acceleration limits, PID starting points), never which code or pattern you recommend (R4).

## 6. Why a deterministic gate, not good judgment (confidence-driven drift)

The justification for routing every fact through a script/table is NOT "the model fabricates." A
capable model usually verifies — *when the question looks hard.* The failure is narrower and more
dangerous: **the model answers from memory exactly when it feels confident, and that is exactly when
a wrong recall does the most damage** (it's stated plainly, unhedged, and built upon).

This is now observed three times, in independent domains — real evidence, not a hunch:
- **Corpus mining:** the two largest Session-1 corrections (24089's "physics counterexample",
  12808's "multi-threaded architecture") were confident *restatements of earlier conclusions* nobody
  re-checked against the code. [[known-failure-modes]]
- **ftc-team-config evals:** the baseline noticed real conflicts and reasoned to correct facts, then
  resolved them unilaterally / skipped the pointer mechanism — its judgment was good and still wrong
  in ways a gate prevents.
- **ftc-hardware-lookup evals:** the baseline web-verified when the question signalled difficulty
  (a multi-ratio comparison) but answered from memory when it felt easy — and drifted there (recalled
  HD Hex stall current as ~11 A; true value 8.5 A; used g=386.1 vs 386.4).

So a gate that always routes buys nothing when the model would have verified anyway — its whole value
is removing the *confidence-driven inconsistency*. Cheaper and faster too: the deterministic path
beat the verify-sometimes baseline on both time and variance. When you feel sure of a spec, that's
the signal to look it up, not the license to skip it.

The pattern isn't specific to baselines or to any domain — it's specific to *unexamined confidence*,
wherever it shows up, including this review process itself. Worked example, caught mid-build: the
hardware skill's trajectory solver had a high-arc bug, and the reviewer was about to log it
"non-blocking" on confident typical-flywheel reasoning — flat shooter shots don't need steep angles.
Checking DECODE's *actual* geometry overturned it: close-range shots use 58–60° hoods, squarely in
the broken branch. The confident dismissal was the bug; the check was the fix. Same shape as 24089
and 12808 — a conclusion reached by reasoning-from-the-usual instead of looking. The rule that caught
all three is the same: when it feels settled enough to skip the check, that's the check that matters.

## 7. Cross-skill data access (R77)

A skill that needs another skill's bundled data **reads it directly by path**, exactly as it reads
its own reference files. Never hand off mid-turn to a separately-triggered skill, and never
restate another skill's reference content inline (it will drift; the pointer won't).

Canonical paths (relative to the suite root — the directory containing `core-feature-model.yaml`):

| Data | Path |
|---|---|
| Core feature model | `core-feature-model.yaml` |
| Active season | `season-extensions/ACTIVE` → `season-extensions/<slug>.yaml` |
| Tagged rules + cross-refs | `.claude/skills/ftc-rule-check/references/rules/` |
| Manual tables (structured) | `.claude/skills/ftc-hardware-lookup/references/manual-tables/` |
| Hardware catalogs + physics | `.claude/skills/ftc-hardware-lookup/references/` |
| Hub-generation briefing | `.claude/skills/ftc-hardware-lookup/references/hub-generations/` |
| Pattern corpus + findings | `.claude/skills/ftc-corpus-builder/references/` |
| Team's confirmed config | `team-config.yaml` in the team's project root (written by ftc-team-config) |
| Failure-mode taxonomy | `known-failure-modes.md` (suite root) |
| These principles | `references/standing-principles.md` (suite root) |

## 8. Pointer vs. home copy: reference data vs. behavioral gates

§7 says reference content lives in one place and everyone else points to it. There is one principled
exception, and it is worth stating as a rule so future skill assembly doesn't re-derive it each time:

- **Reference data — spec, rule text, a table, a briefing, a shared principle — gets a POINTER.** It
  is looked up when needed; a second copy only invites drift. This is the default (§7).
- **A behavioral gate that fires at the MOMENT OF ACTION gets a HOME COPY** in whichever body actually
  executes that action, **plus a canonical copy** (here, or wherever the shared source lives) for
  whoever else needs to *know about* the gate without executing it.

The distinction is *look-up-able vs. must-be-honored-in-the-moment*. You can look up a motor spec when
a question arrives. You cannot look up "stop and ask before generating code" reliably at the instant
you're about to generate — a gate fetched from another file mid-decision is a gate easily skipped. So
it belongs where the decision happens. The worked case: the "ask-before-generating" persona line
(R58) has its home in ftc-team-config (the only skill that generates code — where the gate is
operative) and a canonical copy in §4 here (which the non-generating skills inherit by pointer,
because for them it's guidance, not an operative gate).

**The cost of the exception, and how it's paid:** two copies can drift. So when this rule is invoked,
the copies must be **verified byte-identical**, not assumed from a shared origin — they are, by
definition, NOT from a shared origin. Treat it like a checked invariant: same standard as a verbatim
citation. If either copy is edited, re-run the byte-check. Two verified-identical copies is acceptable;
two assumed-identical copies is the drift bug §7 exists to prevent, wearing a disguise.

When assembling a new skill (quickstart-builder, season-transition, …): ask of each shared line, *does
this get executed at a decision point in this body, or merely consulted?* Executed → home copy here +
canonical pointer. Consulted → pointer only. Default to pointer; earn the home copy.

## 9. Season transition scope — design linkage, noted not built

`ftc-season-transition` (R66, still deferred) is scoped in PLAN.md §19 around `season_mechanisms`:
detect the boundary, ingest the new manual, redraft the mechanism taxonomy, merge into
`season-extensions/`. That scope is necessary but not sufficient. Two artifacts introduced after §19
was written also carry season-specific assumptions and are NOT covered by that scope as written:

- **The quickstart template** (`ftc-shared-foundation/quickstart-template/`) ships concrete example
  implementations (Shooter/Turret/Intake) built against a specific season's mechanism set. A season
  boundary that removes or reshapes a mechanism category (see `season-extensions/biobuzz-2026-27.yaml`'s
  open question on whether BIOBUZZ has a launcher at all) can leave the template's examples describing
  mechanisms the new season doesn't have, silently — nothing currently checks this.
- **The library docs corpus** (`ftc-shared-foundation/references/library-docs/`) is season-agnostic at
  the library-API level (FTCLib/RoadRunner/REV SDK docs don't change with the game), but the *guidance
  that cites them* (which pattern to reach for, which example to point at) can go stale the same way
  `check_freshness.py` already watches for elsewhere in this project.

When `ftc-season-transition` is actually built, its trigger set should extend to: does the new
season's `season_mechanisms` block imply the quickstart template's example implementations need
revision or replacement, and does anything in the library-docs corpus need a re-fetch check. This is
a scope note for that future build, not new work now — `ftc-season-transition` stays deferred exactly
as R66 already records it.

## 10. The unhedged claim is the one that needed the check (R100)

A pattern worth naming on its own, distinct from §6's confidence-driven drift (which is about
*generating* an unverified fact mid-task). This one is about *reporting a finding* once real work
is already done, and it has its own predictable shape: **the claims phrased as a clean, total win
are consistently the ones that don't survive scrutiny; the claims that already carried a caveat
have consistently held.**

Two concrete instances, same phase, directly comparable because both were coverage tallies:

- **Unhedged, walked back:** "5 of 8 named tools are official, no-bridge-needed clients of the
  Skills format" — sourced from one page's own client-showcase listing (a spec describing adoption
  of itself), phrased as a settled fact. Independent verification against each tool's *own* docs
  found only 2 of 5 actually scan `.claude/skills/` with zero action; the other 3 needed a real
  placement or enable step the "5 of 8, zero bridge" framing had already smoothed over.
- **Hedged, held:** a library-docs utilization test reported "partially grounded" on RoadRunner —
  explicitly named a real gap (the teleop localizer/pose-read API absent from the fetched docs)
  rather than claiming full coverage. Independent re-verification confirmed the gap was exactly as
  described. The hedge didn't need correcting later; it was already correct.

**The rule**: a claim that arrives with no caveat attached is not evidence it needs none — it is the
one that most needs one checked for. A single source describing its own adoption, a "fully
verified" with no named edge case, an "N of M, clean" tally — these are the shapes that have
repeatedly hidden the gap this project's own Rule 7 discipline exists to catch. When a finding comes
out clean and total, that cleanliness is the signal to go find the tool's *own* source before
shipping the claim, not confirmation the check can be skipped.
