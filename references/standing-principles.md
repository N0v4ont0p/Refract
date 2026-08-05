# Standing principles — shared by all four FTC skills

One copy, pointed to by every SKILL.md (ftc-team-config, ftc-hardware-lookup, ftc-rule-check,
ftc-code-review). Implements R5, R16, R38, R41, R53, R77, R100, R102, R107 (+ the R58 echo) from
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

## 11. A workaround needed to get a correct result IS the result (R102)

A pattern distinct from both §6 (confidence-driven drift, about generating an unverified fact) and
§10 (about how a finding gets *reported* once work is already done). This one is about what happens
*during* a test run, in the moment a workaround becomes necessary — and it has a precise, missable
failure shape: the workaround gets treated as a solved problem (the test still produced a correct
result, so the run counts as a pass) instead of as the finding it actually is.

**Concretely, from this project's own history (R101):** a Phase B regression test needed to pass
`config_lint.py` an explicit `--config` because the script's own default discovery grabbed the
wrong file. The agent running that test noticed, worked around it, got a correct result, and
reported the workaround in passing. That was the right *tactical* move — but the workaround itself
was never escalated as "this script has a real discovery bug," so it sat unfixed for a full extra
session and fired again on the very next test that happened to omit `--config`, before finally
being recognized and fixed.

**The rule**: needing to work around a tool, script, or convention to get the correct answer is not
neutral information that a test still passed despite it — it is itself a finding, with the same
standing as a wrong answer would have had. Escalate it the moment it happens ("this needed a
workaround, and here's why"), not after it recurs enough times to become obviously a pattern. The
tactical fix that gets the current test to a correct result, and the report that the fix was
*necessary*, are two different obligations — doing only the first is how a real defect survives an
otherwise-careful test run. This is the more important lesson of the two R101 surfaced, not the bug
itself.

**A closely related failure shape, recurring three times in one work session — worth naming
visibly here rather than left scattered across three files' commit history as isolated bug notes:**
a fix or addition that *reads* as correct is not the same claim as one that has actually been run
and checked against real output.

1. `config_lint.py`'s own fix (R101): the first attempt (scope the `rglob` search to `code_dir`)
   read as a reasonable, targeted correction — and was wrong for the common case (a config at the
   project root, a *sibling* of `code_dir`, not nested inside it). Caught only by running it against
   the real fixture and getting an unexpected "no config found," not by re-reading the diff.
2. A pattern file's duplicate YAML key (`32008.yaml`, Phase F1): the source text had both a
   `classification`/`basis` block and a `public_shippable` block under the same key, `provenance:`
   — every field was present in the file as written, but YAML's own key-collision rule silently let
   the second occurrence overwrite the first, dropping the classification entirely. Caught only by
   parsing the file and printing the actual resulting dict, not by reading the source text.
3. `extract_feature_vector.py`'s TickTree signature (Phase G2): adding a `SIGS` entry matched the
   exact shape of every existing signature in the file — but `main()` separately hardcodes which
   axes reach the output JSON, so the new signature was silently unreachable. Caught only by running
   the script against a real positive case and checking the actual JSON, not by confirming the
   `SIGS` dict looked right.

**The rule, stated once so it doesn't need re-deriving three more times**: all three of the above
would have shipped silently broken if the check had stopped at "the diff looks right." A change
that reads as correct on inspection has not yet been verified — only running it and checking the
real output verifies it. This is the concrete, current evidence for why every fix in this project
gets an actual re-run, not just a re-read, before being called done.

## 12. A verified claim has a shelf life, not just a confidence level (R107)

Distinct from §10's rule (R100 — an unhedged claim that was *wrong at the time it was made*). This
is a different failure mode, adjacent but not the same: a claim that was genuinely, correctly
verified against a real source at the time — cited accurately, read correctly, nothing rushed —
and is no longer true, because the external thing it described changed afterward. Both are real
risks to a claim about the outside world; they don't get to share one mitigation.

**Concrete instance — the first one caught, not a hypothetical**: Phase C's cross-tool
compatibility check found Cursor did not scan `.claude/skills/`, cited directly to Cursor's own
documentation at the time. That finding was correct when made — not an unhedged guess, not a
stretched inference. A later pass (building this project's own `docs/` tree) re-checked the same
question against Cursor's *current* documentation and found it now states "for compatibility,
Cursor also loads skills from Claude and Codex directories." The earlier finding didn't fail R100's
test — it had a real citation, correctly read. It just didn't stay true, because Cursor's own
product changed underneath it.

**The rule**: a claim about an external tool or platform's current behavior is a claim with an
expiration date, not a permanent fact once verified — carry a "verified as of" sense with it, not
just the citation. Re-checking that class of claim on some real cadence (tied to how fast the
specific platform actually moves, not a fixed calendar rule) is a different, additional discipline
from R100's "check the ones that sound too clean" — R100 catches a claim that was never solid; this
catches a claim that was solid and stopped being true. A claims inventory that only re-runs R100's
check will still go stale here, silently, exactly the way this one almost did.

## 13. A physical tuning constant can never be source-derived (R109)

**The canonical case, first, because it is the reason this category exists.** Pedro Pathing's
current quickstart ships a `Constants.java` containing `new FollowerConstants()` and *no numbers at
all*. Every physical constant a robot needs therefore comes from the library's own field
initializers — `mass = 10.65`, `forwardZeroPowerAcceleration = -34.62719`, `xVelocity = 81.34056`,
`forwardPodY = 1`, `strafePodX = -2.5` — and applies **silently** to any team that never calls the
corresponding builder method. Nothing appears in the team's code. Nothing looks unset. A reviewer
reading that repo sees a clean constants file and no evidence of a problem, while the robot follows
paths computed from a mass that is off by several kilograms and a strafe pod the software believes
is 2.5 inches from where it is.

Those are not invented numbers. They are real measurements — off somebody else's robot — carried to
five decimal places, which is exactly what makes them worse than a fabrication. A made-up value
looks made up. `-34.62719` looks like the output of a tuning run, because it *was* the output of a
tuning run, on a machine that is not this one.

And there is not one such set. Pedro ships **three**, all live, all different, for the same
physical fields:

| field | library (current) | Beginner-Quickstart | Quickstart-1.0.9 |
|---|---|---|---|
| `mass` | 10.65 | 10.65942 | 13 |
| `forwardZeroPowerAcceleration` | -34.62719 | -34.62719 | -41.278 |
| `lateralZeroPowerAcceleration` | -78.15554 | -78.15554 | -59.7819 |
| `xVelocity` / `xMovement` | 81.34056 | 81.34056 | 57.8741 |
| `yVelocity` / `yMovement` | 65.43028 | 65.43028 | 52.295 |

Three different masses, none of them any given robot's. A check written against one set silently
misses the other two — `10.65` and `10.65942` are far enough apart that no near-match tolerance
bridges them, so covering the library alone would have left the two quickstart sets wide open, and
covering the quickstarts alone would have left the *silent* case — the one with nothing in team
code to look at — entirely uncovered. `failure_mode_lint.py`'s `template_default_tuning_constant`
check carries all three, and RoadRunner's mirror-image case besides: RoadRunner's library ships no
such numbers, so its defaults live in the quickstart's `Params` class as named fields at inert
values (`inPerTick = 1`, `kS = 0`, `lateralInPerTick = inPerTick`) that a team is meant to overwrite
and routinely partly doesn't. All of these are external-project facts under §12's shelf-life rule —
re-verify them against each library's current source rather than trusting the tables indefinitely.

Everything below is the general rule this case instantiates.

Distinct from every hallucination-control category already in this file, and distinct in a way
that matters more than the others. §10 (R100) and §12 (R107) both govern *claims about the world
that could in principle be checked against a source*. This one governs values for which **no source
exists, anywhere, by nature** — not "not seeded yet", not "the catalog is incomplete", not
"a better retrieval pass would find it."

**The distinction from the unseeded-catalog-SKU case.** When `ftc-hardware-lookup` abstains on a
motor outside the seeded catalog, the correct value exists — on a vendor page, in a datasheet — and
the abstention is about *this system's* coverage. Seed the catalog and the gap closes. A robot's
mass, a drivetrain PIDF gain, an odometry pod offset, a ticks-per-inch scalar: these are properties
of one specific physical robot on one specific day. No documentation contains them. No amount of
retrieval, catalog seeding, or reasoning produces them. The only two honest states are:

1. **carried forward from a real measurement** on that robot — verbatim, never regenerated,
   never "adjusted to look more reasonable"; or
2. **loudly marked untuned**, carrying no number at all, with the real procedure that produces it.

**Why the middle ground is categorically worse here than anywhere else in this system.** Every
other failure this project guards against produces a *wrong answer*: a mis-cited rule number, a
motor spec that's off, an API call that doesn't exist. Those are read by a person, and most of them
fail loudly — code that calls a non-existent method does not compile. A fabricated tuning constant
produces *wrong robot behavior*. It compiles. It deploys. It passes every linter. The robot drives
— into a wall, or through a path it was supposed to stop short of, at whatever speed the fabricated
feedforward gain implies. Nothing in the software stack registers a fault, because nothing is
faulty by software's standards. The failure surface is a physical machine with people around it.

A device name, by contrast, is safe to infer-then-confirm: a wrong `hardwareMap` name throws on
init and the robot never moves. Loud, immediate, cheap. The two are graded differently in
`core-feature-model.yaml` for exactly this reason, and the difference is the failure mode, not the
confidence level.

**The enforcement is structural, not a preference.** "Never fabricate a tuning constant" as prose
is worth little — it's the kind of instruction that holds until a plausible number is one token
away and the alternative is an unsatisfying answer. So the schema makes a guess *unrepresentable*:
`tuning_constants.<field>.origin` is a closed set of exactly `{measured, untuned}`. There is no
`estimated`, no `default`, no `typical`, no `library_recommended`. A number cannot be written into
a config without asserting it was measured on that robot; `origin: untuned` with a non-null value
is a validation error; an unconfirmed `measured` value blocks `generation_allowed`. A model
inclined to emit a reasonable-sounding value has nowhere to put it — the failure happens at config
validation, in front of a person, instead of on a field.

**Restating the enforcement boundary, since the lead case is where it bites.** A library default
that a team never overrode cannot be caught by reading the team's config — there is nothing there to
read. It is caught deterministically at review time, by the lint check above, against a table of
real upstream values. The config schema closes the *authoring* path; the lint closes the *inherited*
path. Neither alone is sufficient, and the inherited path is the one that leaves no trace.

**Config-confirmed and robot-tuned are two separate milestones.** `tuning_status` models them
separately (`not_yet_tunable` / `untuned` / `tuned`) because collapsing them is what makes a fully
confirmed config read as a robot ready to run on real numbers. A team can legitimately have every
config field confirmed and zero real constants; that is a normal state on the way to a working
robot, not an error, and generation must serve it honestly — a correctly-structured scaffold with
every tuning-dependent field loudly marked and the real tuning procedure attached, never a
scaffold silently pre-filled with numbers that came from nowhere.
