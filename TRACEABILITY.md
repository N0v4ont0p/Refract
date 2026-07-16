# Requirements Traceability Matrix — PLAN.md → skill suite (Session 2 assembly)

LIVE document for the skill-assembly phase. Built BEFORE any SKILL.md drafting (Step 0), kept
current as each skill is drafted. Every atomic, checkable requirement in PLAN.md gets an ID; each
skill marks which IDs it implements and where. Final deliverable: the coverage table at the bottom,
with zero unexplained gaps and zero unexplained overlaps.

**Owner codes:** TC = ftc-team-config · HW = ftc-hardware-lookup · RC = ftc-rule-check ·
CR = ftc-code-review · CO = ftc-construct (added post-Session-2, §23) · ALL = all five
(cross-cutting, intentional) · DEF = deferred out of this pass (season-transition, MCP/hooks infra —
quickstart-builder is no longer fully deferred, see R61) · S1 = already implemented as a Session-1
artifact (the skill's job is to WIRE to it, not rebuild it).

**Status codes:** `asset-exists` (artifact on disk, needs wiring) · `greenfield` (nothing exists;
the SKILL.md/scripts built this pass must implement it) · `MISSING-ASSET` (requirement needs a data/
script artifact that does not exist — cannot be satisfied by SKILL.md prose alone) · `deferred`.

Excluded with reason: §1 (architecture rationale — records why non-goals were rejected; constrains
nothing a skill does), §14.1 interview content and §14.2 pipeline steps (executed in Session 1;
their standing residues ARE extracted below as R51-R52 and §12 items), §21 (process ordering).

---

## §2 Skill suite structure
| ID | Requirement (one clause each) | Owner | Status |
|---|---|---|---|
| R1 | Each SKILL.md body stays ≤ ~500 lines; overflow goes to `references/` | ALL | greenfield |
| R2 | The four skill descriptions are sharply differentiated so routing does not collide | ALL | **VERIFIED (cross-skill-routing.json): blind classifier over 20 queries — 19/20 exact, 1 acceptable-ambiguous (q17), 0 collisions, 0 under-triggers, 0 negative over-triggers. Both required tight pairs passed: q5/q6 split HW-specs vs RC-allowed cleanly; q17 "look at repo" resolved to a valid single owner (CR, safe handback to TC). No description changes needed.** |

## §3 Core feature model
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R3 | Elicited config values must come from the axes declared in `core-feature-model.yaml` (no invented axes/values) | TC | asset-exists (core YAML) |
| R4 | `fabrication.capability` affects TUNING VALUES only — never gates which code/pattern is recommended | TC, CR — overlap intentional: TC records the field, CR must not filter patterns by it | greenfield |
| R5 | `team_context.experience` affects EXPLANATION DEPTH only — never gates a recommendation | ALL — intentional: any recommending skill | greenfield |

## §4 Season extension
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R6 | Season-specific data is resolved through `season-extensions/ACTIVE` at runtime, never hardcoded in a skill | TC, RC, CR — intentional: TC (mechanism set), RC (rules_current_through), CR (season archetypes) | asset-exists |
| R7 | `constraints_on_core` entries are enforced (e.g. fixed_shooter_on_swerve requires drivetrain=swerve) | TC (at elicitation), CR (at review) — intentional: catch at entry AND at review | greenfield check logic |

## §5 Model & effort routing
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R8 | Team-config inference pass runs Haiku-first, escalates to Sonnet only if ambiguous | TC | greenfield |
| R9 | Rule-legality verdicts run in the main session, citation-forced (no subagent) | RC | greenfield |
| R10 | Hardware spec lookup = structured-data read / script — an LLM never generates a spec value | HW | asset-exists (tables) + **MISSING-ASSET** (catalogs, see R20) |
| R11 | Deterministic lint tier = script invocation (`failure_mode_lint.py`), not LLM re-derivation | CR | asset-exists (S1 linter) |
| R12 | LLM structural-smell pass = Sonnet subagent, adaptive effort (don't over-invest) | CR | greenfield wiring |
| R13 | Full pre-competition review = `full-review` Opus 4.8 xhigh subagent, read-only tools, own context | CR | asset-exists (agents/full-review.md) |
| R14 | Verification pass on generated claims: Haiku-first, escalate to Sonnet on mismatch | RC, CR — intentional: both emit claims needing CoVe | greenfield |
| R15 | Skills invoke subagents by their pinned definitions; never override the pinned model IDs | CR (main invoker), TC | asset-exists (4 agents pinned) |

## §6 Layer allocation
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R16 | If a script can answer it, a model never guesses it (deterministic-first, all domains) | ALL — intentional: the project's spine | greenfield instruction + existing scripts |
| R17 | PreToolUse hook blocks `git commit` referencing an unconfirmed config field | DEF (hooks infra) — TC owns the confirmed/unconfirmed state it keys on | deferred |
| R18 | Live-data MCP layer (TU feed, FTCScout, goBILDA scraper) | DEF (§18 infra) | deferred |

## §7 Knowledge ingestion (what each skill's references/ must hold)
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R19 | RC references = tagged Manual P1+P2 + TU history + Q&A archive (clarification-tier-tagged) + Inspection Checklist | RC | asset-exists (212 tagged rules, cross_refs, index) — TU/Q&A/checklist ingestion PARTIAL, flag at RC build |
| R20 | HW references = REV + goBILDA catalogs as structured tables (part no., dims, electrical, compat) | HW | APPROVED in-scope: build a Rule-7-verified catalog SEED (common competition parts, per-value source citations, abstain-if-not-in-table rule). **PHASE GATE (user): the seed gets its OWN review checkpoint — Rule-7-verified per value, signed off separately — before assembly closes; not folded into SKILL.md-looks-done** |
| R21 | CR must recognize the ecosystem libraries (SDK, Pedro, RoadRunner, FTCLib/SolversLib, Dashboard, EasyOpenCV, Limelight) e.g. for §12 import-gating and idiom checks | CR | partial (corpus SOURCES + §12 gate list) |

## §8 Rules reasoning
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R22 | A legality question retrieves the relevant rule chunk(s) AND one hop of cross-references before any verdict | RC | asset-exists (cross_refs.json) + greenfield behavior |
| R23 | Legality output is structured: `{verdict: legal\|illegal\|ambiguous, citations[], reasoning}` | RC | greenfield |
| R24 | Every cited rule number is programmatically verified to exist (against rule_index.json) before the answer ships | RC | asset-exists (index) + greenfield check |
| R25 | Q&A-sourced content is presented as clarification-tier, never rule-tier (Q&A does not supersede the text) | RC | greenfield |
| R26 | Low retrieval confidence or unresolved Q&A disagreement → verdict "ambiguous — worth filing a Q&A", never a confident guess | RC | greenfield |
| R27 | A rule citing an embedded table resolves it BY POINTER into the §9 structured table file; table content is never quoted/paraphrased from rule prose | RC, HW — **intentional overlap**: this IS the §8↔§9 boundary; RC owns resolution behavior, HW owns the table files | asset-exists (37 tables + INDEX; rules hold pointers) |

## §9 Hardware knowledge
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R28 | Hardware spec values come ONLY from structured tables — never from prose, never from model memory | HW | asset-exists (manual tables) / **MISSING-ASSET** (catalogs) |
| R29 | CAD is a link/reference field only, never ingested as text | HW | greenfield instruction |
| R30 | ALL numeric hardware arithmetic (gear ratio, torque, speed, kinematics) via deterministic script; the model reads the script's output, never generates the number | HW | trajectory_solver.py exists; **MISSING-ASSET**: `motor_math.py` |
| R31 | Manual tables stored as structured files keyed by manual table ID | HW | asset-exists (S1: 37 files + INDEX.json) |

## §10 Config-driven generation
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R32 | A RobotConfig is generated only from a CONFIRMED feature-model instance | TC | greenfield |
| R33 | `Drivetrain` is the only fixed interface; mechanism interfaces derive dynamically from the active `season_mechanisms` keys (no hardcoded mechanism list) | TC (config side), CR (reviews generated code against it), CO (generates against it) | greenfield, now **delivered**. **What each actually implements:** TC — *derives the interface SET* from the confirmed config's `season_mechanisms` keys and confirms it (the "which interfaces exist" decision); CR — *checks generated/existing code against that set* via config_lint (flags a mechanism class the config doesn't declare); CO — *generates the actual interface + implementation classes* from `ftc-shared-foundation/quickstart-template/` (§23), matching what the confirmed config selects. Superseded note: this row previously deferred full codegen to `ftc-quickstart-builder` (R61) — that authority now belongs to `ftc-construct` (CO) instead; see §23. |
| R34 | Code for undeclared features is never generated into the team's fork, or is flagged "not referenced by current config — confirm if stale" | CR | greenfield check |

## §11 Hallucination control stack
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R35 | No hardware/rule claim without a citation to a chunk/file actually read THIS turn | RC, HW — intentional: the two claim-emitting domains | greenfield |
| R36 | Chain-of-Verification pass on generated claims before finalizing | RC, CR — intentional (R14 is its routing) | greenfield |
| R37 | High-variance resampled answers treated as an abstention flag, where feasible (soft requirement) | RC | greenfield (best-effort) |
| R38 | No support found → abstain ("Unknown — need the BOM/CAD entry for X"), never a filled gap | ALL — intentional: valid expected output everywhere | greenfield |
| R39 | Every recommendation ties to the confirmed config feature(s) AND the source pattern/rule that triggered it | CR (primary), RC (via R23) | greenfield |
| R40 | A deterministic script mechanically rejects generated code referencing features the confirmed config doesn't declare | CR | **MISSING-ASSET**: constraint-check script |
| R41 | Rule 7: tier-1/tier-2 source labeling; tier-2-only claims labeled as such; forward-looking claims need ≥2 independent sources | ALL — intentional: standing project-wide | greenfield instruction (S1 precedent throughout corpus) |

## §12 Provenance-aware confidence

> **Reading confirmed (user, assembly phase):** CR's obligation for R42-R46 is FAITHFUL DISPLAY of
> the existing mining-time tags — no inflation, caveats preserved verbatim — NOT re-implementation
> of the mining-time gates. The gates (import check, provenance classification) are Session-1
> pipeline machinery. The only CR-side edge on R46: a NEW pattern candidate surfacing mid-review is
> ROUTED to the corpus process, never classified inline by the review skill.
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R42 | Pattern recommendations carry their provenance classification + confidence tag faithfully — never upgraded in presentation | CR | asset-exists (tags in corpus) + greenfield behavior |
| R43 | Repo-count is never presented as independent confirmation; diversity-of-reasoning is the stated basis | CR | greenfield |
| R44 | The system's own generated output is a single lineage — never cited as independent confirmation of its own recommendations | CR, TC — intentional: TC generates, CR reviews | greenfield |
| R45 | Single-source patterns remain usable but labeled `single-source` | CR | asset-exists (corpus tags) |
| R46 | §12 shared-library import gate before any "independently-derived" classification of orchestration candidates | S1 (corpus pipeline) + CR if classifying new patterns mid-review | asset-exists (PLAN §12 rule + S1 precedent) |

## §13 Elicitation methodology
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R47 | A question is asked only if its answer changes the applicable pattern/recommendation set (nonzero information gain) | TC | greenfield |
| R48 | Question order = empirical branching factor from patterns' `applicable_when` counts, as a soft ranking | TC | asset-exists (64 patterns to count over) + greenfield ordering |
| R49 | Inference BEFORE elicitation: deterministic parse of provided artifacts first; only the residual becomes questions | TC | asset-exists (extract_feature_vector.py) + greenfield flow |
| R50 | Mandatory-ask set regardless of inferability: drivetrain topology, season mechanism set, software stack | TC | greenfield |

## §14 residues (standing rules from Session-1 scope decisions)
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R51 | Any cited team code keeps attribution (public source, file+line refs, never bulk reproduction) | CR | asset-exists (corpus convention) + greenfield behavior |
| R52 | Generated/reviewed code respects SDK integrity — never modify or omit compiled libraries in `libs/` (competition-legality hard rule) | CR (check), TC (generation guard) — intentional | greenfield check |

## §15 Session-2 runtime behavior
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R53 | Standing instruction in EVERY relevant SKILL.md: when an answer would change what code gets generated, ask — don't guess, don't wait to be asked | ALL — intentional: PLAN says "every relevant SKILL.md" literally | greenfield |
| R54 | Inference pre-fills defaults only; it never silently decides what ships — unconfirmed config → question, confirmed → code | TC | greenfield |
| R55 | Config is stated back explicitly and confirmed BEFORE any hardware-specific code is written; no generation fires against an unconfirmed field | TC | greenfield |
| R56 | Once config is confirmed, skills actually write/edit files (not just describe changes) | TC | greenfield |
| R57 | Continuous re-elicitation: a mid-session mechanism mismatch re-opens that part of the config; never proceed from a stale snapshot | TC | greenfield |
| R58 | Persona instruction (verbatim §15.5): "If a recommendation would differ depending on information you don't have, stop and ask before generating code. A wrong guess that compiles is worse than a question that costs one turn." | TC (persona home), echoed ALL | greenfield |
| R59 | `hub_generation` is NOT asked while REV is the sole legal system (zero info gain); the gate keys off the ACTIVE season slug, not a hardcoded date | TC | asset-exists (hub-generations refs) + greenfield gate |
| R60 | When the hybrid window opens (ACTIVE ≥ 2027-28): hub_generation joins the mandatory-ask set, preceded by the briefing (both-legal-for-years; hybrid is a real option), never a silent default | TC, HW — intentional: TC asks, HW hosts the tier-tagged briefing reference | asset-exists (systemcore-motioncore.md). **Implementation rule (user): POINTER, not duplication — TC's body cites the HW reference by path and reads it fresh at ask-time; it never restates the facts inline** |

## §16 QuickStart repo — DEFERRED (whole section)
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R61 | QuickStart repo build (§16, all requirements) | CO (ftc-construct, §23) — no longer owned by a deferred `ftc-quickstart-builder` skill | **partially delivered**: the template itself (`ftc-shared-foundation/quickstart-template/`, derived from FTCLib-Quickstart with NOTICE.md attribution) and the interface-based Drivetrain/Shooter/Turret/Intake scaffolding exist and are read by ftc-construct. What §16 originally scoped as a standalone `ftc-quickstart-builder` skill instead landed inside `ftc-construct` — a design decision (§23), not a fresh deferral. The `.claude/skills/ftc-quickstart-builder/` stub directory (design-notes.md only) is superseded by this and can be retired. |

## §17 Anti-pattern detection
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R62 | The deterministic lint tier is authoritative — its findings are reported as findings, not suggestions | CR | asset-exists (6-check linter) |
| R63 | The LLM smell tier is heuristic — it always shows the flagged code as evidence and never asserts a verdict outright | CR | greenfield |

## §18 Live data — infra deferred, consumption rules live
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R64 | Team Updates consumed as effective-dated diffs; a rule answer reflects the newest applicable TU | RC (consumption; MCP feed itself DEF) | partial — static TU state tagged; live feed deferred. **↔ R79:** R64 is the CONSUMPTION side (reflect the newest TU I have); R79 is the DETECTION side (am I stale vs the live manual?). R79 flags when R64's corpus is behind; R64's deferred live MCP feed is exactly the parseable current-TU source that will let R79's STALE branch fire on real data (see R79 open item). |
| R65 | OPR/ranking figures only from FTCScout's API, never asserted from memory (until MCP exists: abstain + point to FTCScout) | DEF infra; abstention fallback owned by RC/CR via R38 | deferred with live fallback |

## §19 Season transition — DEFERRED (skill), protocol already exercised Phase 8
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R66 | Season Transition Protocol skill (§19 steps 1-6 as a triggered skill) | DEF (ftc-season-transition) | deferred — draft artifact exists (biobuzz YAML) |

## §20 Testing & evals (this phase's eval grounding)
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R67 | Evals grounded in the three-plus-one synthetic configs (real 19859 config; rookie/stock-goBILDA/no-turret; veteran/CNC/swerve/turret) | ALL (eval process) | greenfield — configs to be written as eval fixtures |
| R68 | EVAL: no hardware spec appears without a traceable catalog citation | HW | eval to build |
| R69 | EVAL: a recommended pattern violating the declared config makes the constraint check fire, observably | CR | eval to build |
| R70 | EVAL: every rule citation resolves to a real, current rule number | RC | eval to build |
| R71 | EVAL: the system abstains when needed information is deliberately withheld | ALL (test at least TC + HW) | eval to build |
| R72 | EVAL: a shared-ancestry-seeded pattern gets downgraded, not treated as independent confirmation | CR | eval to build |
| R73 | EVAL: confirm-before-generate blocks code generation when a mandatory field is ambiguous | TC | eval to build |
| R74 | EVAL: a rule change dated after the base manual is surfaced (testable with a static TU fixture despite R64 deferral) | RC | eval to build |

## §22 Risks (standing residues)
| ID | Requirement | Owner | Status |
|---|---|---|---|
| R75 | Hardware answers are the sharpest hallucination edge — HW's structured-data path gets the hardest verification of the four (break-it testing, not read-and-approve) | HW (+ this phase's process) | process commitment |
| R76 | Rule cross-reference edges trusted only after extraction QA (regex-vs-LLM diff on a sample) | RC | asset-exists (S1: QA done, 0 dangling) |

---

## Standing rule — eval benchmark records are append-only (all future iterations)

A `benchmark.json`/`benchmark.md` reflects what happened in THAT run. Corrections apply going forward
(next iteration, or a note in the live record like TRACEABILITY.md), never by retroactively editing a
frozen benchmark — same reason a merged corpus entry isn't silently rewritten. A stale note inside a
past benchmark is history, not a bug to patch.

## Standing finding from the ftc-team-config eval (carries forward to all remaining skills)

The iteration-1 baseline was NOT weak, and that is the finding. It **noticed real problems and
still resolved them unilaterally** (eval-3: surfaced the swerve/mecanum conflict, then chose a
resolution on the user's behalf; eval-2: noticed the config contradiction, then flipped it to
confirmed itself), and it **reasoned its way to correct facts while skipping the pointer mechanism
entirely** (eval-4: right SystemCore timeline via web search, no tier labels, no single source of
truth). The precise justification for these skills is therefore NOT "the model gets things wrong
without them" — it is that **verification by construction and decisions-left-with-the-user cannot
be supplied by good judgment exercised turn by turn**. A deterministic check fires every time
regardless of model diligence; a gate forbids choosing for the user even when the choice looks
obvious. Cite THIS, not the raw benchmark delta, when a skill body needs to justify a hard gate —
and design the remaining skills' evals to test for unilateral-resolution and
mechanism-skipped-but-answer-right failure modes, which raw correctness scoring misses.

## Post-check additions (assembly phase — IDs now run R1-R78)

| ID | Requirement | Owner | Status |
|---|---|---|---|
| R77 | **General cross-skill data mechanism:** a skill needing another skill's bundled data reads it DIRECTLY BY PATH, exactly as it reads its own reference files — never a mid-turn hand-off to a separately-triggered skill. (The §8↔§9 fix, generalized to every boundary: TC reading HW's hub-generation briefing, CR reading the corpus patterns and TC's confirmed config, RC resolving table pointers into HW files.) | ALL | greenfield — canonical path list lives in standing-principles.md |
| R78 | **Known gap, explicitly deferred (alongside R61):** a rookie team's from-scratch "what should our first robot look like" design question is owned by NONE of the four skills. Correctly out of scope this pass — the design-advice layer belongs with the quickstart-builder/strategy work. Recorded now so it is discovered by plan, not by surprise. | DEF | deferred |
| R79 | **Manual-freshness / corpus-currency check (calibrated abstention for currency, not just completeness).** A general-purpose repo-root script, parameterized by the `season-extensions/ACTIVE` slug, fetches the season's public manual page, compares to the stored tagged version (`incorporates_through`), and flags STALE/UNVERIFIABLE rather than answering silently against possibly-stale data. ftc-rule-check runs it BEFORE any verdict. Built season-parameterized so pointing at BIOBUZZ later is a one-line change — but does NOT fetch/ingest BIOBUZZ now. Reusable later for season-transition + hardware-catalog currency. **↔ R64:** R79 is the DETECTION side of R64's consumption promise — it flags when the RC corpus is behind the live manual; R64's deferred live-feed MCP is the parseable current-TU source R79 needs to distinguish real STALE from UNVERIFIABLE. | shared (`scripts/check_freshness.py`); RC consumes; TC/season-transition + HW reuse later | **implemented; STALE-detection discipline validated against real drift (Phase C2) — narrower open item remains, see below** |

> **R79 open item, updated (Phase C2 — no longer "synthetic only"):** the claim that this script's
> STALE-detection shape had *never* caught real drift is no longer accurate. `corpus-input-scan.py`
> reuses the exact stored-vs-live comparison this script pioneered — applied to library-release
> freshness instead of rules freshness — and its first live run caught a REAL, unprompted STALE
> case: `ftc-sdk`'s docs were fetched 2026-07-12, a real release (`v11.2`) published 2026-07-15,
> three days later. Not a synthetic override, not staged for a test — the discipline this script
> established is now proven against real-world drift, not just its own `--self-test`/`--live-tu`
> harness.
>
> **What's still precisely open, and shouldn't be conflated with the above:** `check_freshness.py`'s
> own STALE branch — on rules/manual-page data specifically, the R79 scope as originally written —
> has still never fired on a real, non-override call. Every live (no `--live-tu` override) call
> against the actual manual page has returned UNVERIFIABLE (no parseable "Team Update N" marker),
> both in this pass and previously. So: the underlying mechanism is now proven real, via its sibling
> reuse; this script's own literal branch, on its own original data source, is still waiting on
> either a real Team Update dropping or the deferred §18 live-feed MCP layer providing a parseable
> current-TU source. Narrower than before, but still genuinely open — not closed by the ftc-sdk catch.
| R80 | **Verbatim rule text in verdict output.** Each citation in the structured verdict carries the actual stored rule text (the corpus `text` field, from `rules.py lookup`) alongside its ID — never regenerated or paraphrased. Makes every verdict self-verifying without a separate lookup. | RC | rules.py already returns `text`; SKILL.md schema + instruction change |

## §23 — ftc-construct: grounded code generation (post-Session-2 addition, IDs now run R1-R93)

A fifth skill, added after the original four were signed off. Reason it's separate rather than
folded into ftc-team-config: repo-check + template scaffolding + multi-domain-grounded generation
is materially bigger scope than config confirmation warrants bundling together, and giving codegen
its own skill lets it carry a dedicated grounding discipline (library docs, corpus patterns,
hardware catalog) instead of being a paragraph at the end of ftc-team-config's body. This also
required a real edit to ftc-team-config itself (R89 below) — not just an addition.

| ID | Requirement | Owner | Status |
|---|---|---|---|
| R81 | `ftc-construct` exists as a skill separate from `ftc-team-config`, owning repo-check + template scaffolding + multi-domain-grounded generation | CO | **delivered** — `skills/ftc-construct/SKILL.md` (both source and plugin copies) |
| R82 | Reads a confirmed config from `ftc-team-config` by reference (`team-config.yaml` + `validate_config.py`'s `generation_allowed`) — never re-elicits one. If unconfirmed, hands back to `ftc-team-config` rather than proceeding on a guess. | CO | **delivered** — SKILL.md §0; verified live by the boundary test below |
| R83 | Scaffolds from an interface-based quickstart template (`Drivetrain` fixed + `Shooter`/`Turret`/`Intake` derived from `season_mechanisms`), derived from FTCLib-Quickstart with full license/attribution (`quickstart-template/NOTICE.md`) | CO | **delivered** — `ftc-shared-foundation/quickstart-template/` (15 files); license verified (FIRST BSD-3-Clause-style SDK license, distinct from FTCLib's own MIT — both stated correctly in NOTICE.md) |
| R84 | Grounds generated API usage in a fetched library-docs corpus (not memory) | CO | **delivered** — `ftc-shared-foundation/references/library-docs/{pedro-pathing,ftclib,roadrunner,rev-robotics,limelight,gobilda-build-guides,ftc-sdk,easyopencv,ftc-dashboard}/`, 56 files, each header-tagged with source URL + fetch date (2026-07-12) |
| R85 | Cites corpus patterns (`patterns/*.yaml`) with `confidence`/`provenance.classification` displayed exactly as stored, never inflated — same discipline as CR's R43/R46 | CO | greenfield instruction (SKILL.md §3); no new corpus data needed, reuses existing patterns |
| R86 | Hardware/tuning values used in generated code are read from `ftc-hardware-lookup`'s catalog/scripts, never generated | CO | greenfield instruction (SKILL.md §3), reuses existing HW assets |
| R87 | Structural generation rules (interfaces derived not enumerated / no code for undeclared features / never touch `libs/`) | CO (moved from TC — see R89) | **delivered**, carried over verbatim from ftc-team-config's former §6 |
| R88 | **Mandatory post-generation verification, no exceptions:** `config_lint.py` + `failure_mode_lint.py` re-run against generated code, plus an `ftc-rule-check` citation-grounded legality re-check, before anything is declared done. Combined result reported ("code written and verified..."), not just "code written." | CO | **delivered** — SKILL.md §5; reuses CR's and RC's existing scripts/flow by path, no new scripts needed |
| R89 | **Real edit to an already-signed-off skill:** ftc-team-config's former §6 ("actually write the code") is replaced with a hand-off to `ftc-construct` once `generation_allowed` is true. Both the source and plugin copies updated identically. | TC | **delivered** — `.claude/skills/ftc-team-config/SKILL.md` §6 + plugin mirror, verified byte-consistent apart from the established path-substitution pattern |
| R90 | **Season-transition scope note (design linkage, not new work):** `standing-principles.md` §9 records that a future `ftc-season-transition` build should also check whether the quickstart template's example implementations and the library-docs corpus need revision at a season boundary — not just `season_mechanisms`. | DEF (ftc-season-transition, unchanged deferral status) | **delivered as a note only** — `references/standing-principles.md` §9 (+ plugin mirror); ftc-season-transition itself stays deferred exactly as R66 already records |
| R91 | **`validate_config.py` fails gracefully on a missing config file, for every caller, not just ftc-construct.** Originally patched around in ftc-construct's SKILL.md §0 (a manual existence check before invoking the script); the user correctly rejected that as a workaround and required the fix at the script level. A missing file now returns a clean `{valid: true, generation_allowed: false, config_found: false, unconfirmed_mandatory: [...]}` instead of an unhandled traceback — `config_found` is new, every other field's shape is unchanged. `ftc-construct`'s §0 simplified back down to a single unconditional script call once the fix landed. | TC (script owner) | **delivered, tested** — both copies fixed identically (verified same diff as the pre-existing `find_suite_root` path-resolution difference, nothing else); 3 direct runs confirm no regression: missing file (clean, exit 0), the rookie fixture's real unconfirmed field (unchanged output + `config_found: true`), the invalid-constraint fixture's two errors (unchanged output) |

**Routing note (mirrors the existing TC/CR tight pair, R2):** `ftc-construct`'s description
("write a teleop", "add an intake subsystem") deliberately overlaps `ftc-team-config`'s own
codegen-adjacent phrasing ("add an intake", "write auto-aim"). This is accepted, not a defect —
the existing cross-skill-routing eval already established that overlapping trigger phrasing between
two skills is fine as long as whichever one fires first correctly hands off/back to the other
(q17's TC/CR pair). Here it's symmetric: TC-first correctly asks-then-hands-off (§0 above), and
CO-first correctly checks-then-hands-back (R82). See the boundary-test result below for the live
check of the CO-first path specifically.

**Boundary test — RUN, PASSED (`cross-skill-routing.json`, `result_5_skill_rerun`).** Re-ran the
existing blind-classifier eval with `ftc-construct` added as a 5th skill and 3 new queries (q21-q23).
`"write me a teleop OpMode for our shooter"` (the user's own Step-5 test phrase) and `"generate the
ShooterOpMode.java for us"` both routed cleanly to `ftc-construct`, no hedging. The deliberate TC/CO
overlap query (`"add an intake subsystem"`) resolved as `AMBIGUOUS:ftc-team-config|ftc-construct`,
exactly the accepted pattern q17 already established for TC/CR. Separately, the actual handback
mechanism was exercised live, not just described: `validate_config.py` run against the
`rookie-mecanum-stock.yaml` eval fixture (an unconfirmed `software_stack.pathing` field) returned
`generation_allowed: false` — the exact signal `ftc-construct`'s §0 checks before generating.
Two pre-existing, unrelated description-softness findings surfaced incidentally in the re-run (q6
HW/RC ambiguity, q14 CR over-triggering on a networking query) — recorded in the fixture, explicitly
out of scope for §23, not silently dropped.

## Standing finding from the ftc-construct eval (carries forward alongside §20's finding)

Two results from `evals/generation-quality-eval.md` are direct, validated evidence of this skill's
core design claims — not incidental eval color — and are named here at the same standing as the
confidence-driven-drift finding (§20) and the orchestration-nonblocking recurrence (corpus notes,
16093/18742), because they're the same shape of thing: a claim this project makes about itself,
caught being actually true (or actually false) by a real run, not asserted from confidence in the
design.

| ID | Requirement | Owner | Status |
|---|---|---|---|
| R92 | **Config-aware scaffolding, not template-blind.** ftc-construct's core design claim (§22 R83) is that it *adapts* the quickstart template to the confirmed config rather than copying it. Eval-2 forced a real test of this: the template's shipped `RollerIntake` example is written against FTCLib's command framework, but the eval fixture's `software_stack.opmode_style` is `raw_linear_opmode` — a config the template has no example for. A template-blind implementation would have copied the FTCLib-shaped example anyway and shipped code that doesn't match the team's actual software stack. Instead, the run detected the mismatch (via `extract_feature_vector.py`'s own style-detection logic — the same deterministic signal ftc-team-config's inference step already relies on) and rewrote `RollerIntake` plus a new `IntakeTeleOp` against the raw FTC SDK, grounded in `ftc-sdk/opmode-basics.md`. **This wasn't the scenario the eval was designed to force** — eval-2's stated purpose was checking "no code for undeclared mechanisms"; the opmode-style adaptation was a side discovery on the way to that check, which is exactly why it counts as real evidence rather than a confirmed hypothesis: nobody engineered the fixture to specifically exercise this path. | CO | **VERIFIED** — `.claude/skills/ftc-construct-workspace/eval-2-no-undeclared-mechanisms/outputs/mechanisms/intake/RollerIntake.java` + `opmodes/IntakeTeleOp.java`, independently re-read (not taken on the eval transcript's self-report alone) |
| R93 | **Grounded generation fails fast at the point of shipping code, rather than fabricating a plausible number.** ftc-construct's hardware-grounding claim (§22 R86) is that tuning values are read from the catalog, never generated. Eval-3 deliberately requested code against an UNSEEDED motor SKU (`5203-2402-0001`) specifically to force the choice between abstaining and guessing at the exact moment of writing a file, not just at the moment of answering a question (the discipline ftc-hardware-lookup already has, tested here at the harder point — inside generated code a human will compile and flash, not inside a chat answer). Result: `motor_math.py spec/ticks/external` all correctly abstained (exit 3); the generated `FlywheelShooter.java` sets the would-be tuning constants to `Double.NaN` with a fail-fast `init()` guard and a doc comment quoting the script's actual abstain reason plus the concrete unblocking step (seed the datasheet, re-run the script, wire in the result). **Direct, same-scenario contrast**: the baseline run for the identical "write me a teleop OpMode for our shooter" premise (reused from the TC re-eval, not a separately staged strawman) picked a placeholder shooter velocity of `1500 ticks/sec` with zero catalog lookup and reported it to the user as if considered. Same request, same missing-data situation, opposite outcome — this is the confidence-driven-drift pattern (§20) recurring at the code-generation layer specifically: the moment a number is needed to keep writing code is exactly the moment an ungrounded system reaches for a plausible-sounding one instead of stopping. | CO | **VERIFIED** — `.claude/skills/ftc-construct-workspace/eval-3-hardware-grounded/outputs/FlywheelShooter.java` (independently `grep`-checked for `NaN`/`TODO`/`abstain` markers, not taken on self-report), contrasted against the baseline transcript in `evals/post-construct-split-reeval.md` |

**Process finding from running these evals, elevated for the same reason as R92/R93 — not swept
past.** A baseline test run (the one contrasted in R93) had live file-write access and used it to
write a real file into `32008teamcode/`, a different team's mined reference code sitting in this
repo. Caught and cleaned up manually in the moment, but the safeguard at that point was
gitignore-plus-cleanup — real, but not structural: nothing would have stopped a *future* run from
doing the same thing. Fixed properly afterward: a project-level `PreToolUse` hook
(`.claude/settings.json`, git-tracked) now blocks any `Write`/`Edit`/`MultiEdit`/`NotebookEdit`
targeting `corpus-sources/` or `32008teamcode/` outright, for every agent, verified live (a real
`Write` attempt into `32008teamcode/` was rejected by the actual permission system before touching
disk, not just pipe-tested). Full writeup in `ftc-team-config/evals/post-construct-split-reeval.md`.

## §24 — Phase B: library-docs utilization audit + six fixes (IDs now run R1-R99)

A verification pass over the 57-file library-docs corpus (§23's own deliverable), not new
construction: does every fetched file actually have a reachable path from a skill's real
instructions, not just a sibling directory? Full findings + fix-by-fix re-verification in
`ftc-construct/evals/library-docs-utilization-audit.md`. Six fixes landed, each re-tested with a
real scenario, not assumed fixed from the text diff alone.

| ID | Requirement | Owner | Status |
|---|---|---|---|
| R94 | **CO's post-generation rule-check brought to genuine parity with RC's real 5-part flow** — `check_freshness.py` as an actual first step (not skipped), plus an explicit reason-to-verdict instruction between `rules.py lookup` and `rules.py verify`, matching RC's own structure instead of approximating it with retrieval-plus-citation-existence alone. | CO | **VERIFIED** — forced-stale re-test (`check_freshness.py --live-tu 40` against the stored TU-32 corpus) confirmed the final report now explicitly caveats the rule-check verdict as resting on a stale snapshot; previously this check never ran and nothing would have surfaced it. |
| R95 | **EasyOpenCV and FTC Dashboard wiring made structural, not incidental** — CO's SKILL.md §3 grounding bullets now explicitly cover the `sensing.vision` axis (not just `software_stack`) and template-inherited domains requiring a fresh read when extended beyond baseline. | CO | **VERIFIED** — re-test: fresh agent quoted the exact new FLOW-section instruction (not the files-read table) for both EasyOpenCV and FTC Dashboard before generating; previously both returned "NONE FOUND" and worked only via model initiative. |
| R96 | **RoadRunner tested for the first time**, not assumed verified by analogy to Pedro Pathing's result. | CO (test coverage, no skill change) | **TESTED — partially grounded, new corpus gap found.** New fixture `veteran-roadrunner-confirmed.yaml` built and validated (`generation_allowed: true`). 7 of 11 cited API calls traced to real quoted lines in `trajectories.md`/`tuning.md`; the teleop localizer/pose-read API is genuinely absent from the fetched docs and was correctly stubbed (`UnsupportedOperationException` + TODO) rather than fabricated — same shape of gap as goBILDA's (R97), flagged for the same Phase F candidate list. |
| R97 | **goBILDA build-guides gap marked permanent** — a known, structural corpus-completeness gap (source material lacks the derived specs generation needs), not a wiring defect; correct abstention is the designed behavior, not a shortfall to keep searching for. Flagged as a Phase F candidate: team 19859's own measured specs are the real fix, not more fetching. | CO (documentation), flagged DEF (Phase F) | **DELIVERED** — CO's SKILL.md §3 now states this inline; the audit file carries the same note as a load-bearing record, not an incidental observation. |
| R98 | **REV's two orphaned files explicitly annotated** (`onbot-java-programming.md`: intentionally unreachable, template is Gradle-based; `troubleshooting.md`: no current owner, correctly excluded) so a future utilization audit doesn't re-discover these as mysteries. | — (documentation only) | **DELIVERED** — audit matrix entries updated with the explicit one-line notes. |
| R99 | **CR gets a narrow, explicit handoff to RC's real flow for legality-flavored questions about existing code** — same sequential-boundary pattern as the existing RC/HW table-pointer (R27): CR invokes `check_freshness.py` + `rules.py lookup` + `rules.py verify` directly and reasons to the same `{verdict, citations, reasoning}` shape, rather than reviewing structurally or guessing. Not new legality logic inside CR, not a third skill. Resolves §23's Step-4 open question (the combined generate→verify chain was previously reachable only for newly generated code). | CR | **VERIFIED** — real scenario against the existing `evals/fixtures/sample-robot/` code (mixed structural-review + legality request: "is this flywheel shooter legal?"). Freshness check ran for real (returned `UNVERIFIABLE` this time — a live network fetch with no parseable TU marker — and that flag was carried into the reasoning, not dropped); `rules.py lookup`/`verify` ran against real candidate IDs (R207, R801) surfaced by grepping the actual corpus, not guessed; verdict `legal`, citation independently re-checked byte-for-byte against `rules.json` (matches verbatim). The ordinary structural pass ran alongside it unmodified — caught a real R34 config-mismatch (`TurretAimer.java` vs. `turret: none`), routed back to ftc-team-config per CR's existing boundary, not resolved inline. |

**Post-fix state, per the audit's own tally: 0 files with an unaddressed wiring gap.** Every one of
the 57 files now has either verified real usage, directory-level wiring not yet exercised (a testing
gap, not a routing one), or an explicit, load-bearing annotation stating why it's excluded/thin/
structurally gapped. Nothing is silently orphaned.

## §25 — Phase C close-out: a standing suspicion rule earned by a real correction (IDs now run R1-R100)

Full findings in `PHASE-C1-C2-FINDINGS.md`. One requirement, elevated to standing-principles rather
than left as a phase-local note, because the pattern it names is general, not specific to Phase C.

| ID | Requirement | Owner | Status |
|---|---|---|---|
| R100 | **The unhedged claim is the one that needed the check.** Phase C1's first-pass Skills-format claim ("5 of 8 named tools, zero bridge") was sourced from one page's own client-showcase listing and phrased as a clean, total win — it did not survive independent per-tool verification (only 2 of 5 checked tools actually scan `.claude/skills/` with zero action). Contrasted against the same phase's RoadRunner utilization test, which reported "partially grounded" — a hedged claim, naming a real gap up front — and held up exactly as stated under independent re-verification. Elevated to a standing suspicion rule: a claim with no caveat attached is the one that most needs one checked for, same standing as §6's confidence-driven-drift finding. | ALL (review discipline, not one skill) | **DELIVERED** — `references/standing-principles.md` §10 (+ byte-verified plugin mirror), citing both instances by name. |

## §26 — Phase D: final hardening (IDs now run R1-R102)

Full findings in `PHASE-D-FINDINGS.md` (staleness re-check, fresh eval battery across
all 5 skills, R100 self-scan, corpus-depth check). One fix landed, caught live by the fresh eval
battery, not gone looking for — recorded here per this project's own discipline.

| ID | Requirement | Owner | Status |
|---|---|---|---|
| R101 | **`config_lint.py`'s config-discovery bug, caught live by a Phase D regression test, fixed at root cause.** Running the script from the repo root with no explicit `--config`, against a fixture whose real config lives at `evals/fixtures/sample-robot/team-config.yaml`, the old discovery logic (`Path(".").rglob("team-config.yaml")`, unscoped from the CWD) matched `32008teamcode/team-config.yaml` instead — an unrelated file — and silently returned a false-negative `clean: true`. Root cause: the logic searched in the wrong direction. `team-config.yaml` conventionally lives at the project root, a SIBLING of the code directory being reviewed, not nested inside it; searching downward from an arbitrary CWD was never going to reliably find it. Fixed: `find_config()` now walks UP from `code_dir` through its ancestors, stopping at the first (closest) match — deterministic by construction, bounded at the git repo root. | CR | **FIXED, RE-VERIFIED** — re-run against the exact failing scenario now correctly finds the fixture's own config and reports `clean: false` with the real finding (exit 1), not the prior silent `clean: true`. Self-test extended to cover both the sibling-discovery case and the "must not pick up an unrelated config" case. Fixed identically in both the source and plugin copies, byte-identical confirmed. |

> **R101 impact check, sharpened (per user instruction) — "no past result was affected" is true, but
> for two different, non-equivalent reasons; lumping them together would hide the actual gap:**
>
> - **`ftc-construct`'s immunity is structural, but incidental.** CO's SKILL.md hardcodes
>   `--config <team-config.yaml>` in its documented invocation (R88) — not as a deliberate guard
>   against this specific discovery bug, which wasn't known to exist when that instruction was
>   written, but as a side effect of CO always knowing which config it's generating against. The
>   buggy discovery path was simply never reached. This is the kind of safety margin this project
>   has otherwise tried to build everywhere: correct by construction, not dependent on anyone
>   noticing anything.
> - **`ftc-code-review`'s two exposures (Phase B's R99 test, and the Phase D test that finally
>   triggered this fix) were real hits, not near-misses.** Both times the buggy path actually fired
>   and actually returned the wrong config. Both times the final reported result was only correct
>   because the agent running the test happened to notice the wrong filename in the script's own
>   JSON output and re-ran with an explicit override. That is a human/agent-in-the-loop catch — the
>   exact thing a deterministic, "authoritative-tier" script (§17) exists to make unnecessary. **"No
>   results were affected" here means "no result went unnoticed," not "the script was correct" —
>   those are different claims, and only the weaker one happened to hold, twice, by attentiveness
>   rather than design.**
>
> This distinction is *why* R101 alone wasn't a sufficient response — see R102 in
> `standing-principles.md` §11 for the actual gap it exposes: the Phase B workaround should have
> been escalated as a possible defect the moment it happened, not left to recur before being
> recognized as one.

| R102 | **A workaround needed to get a correct result during testing is itself a finding — escalate it the moment it happens, not after it recurs.** Directly derived from R101's own history: Phase B's regression test needed an explicit `--config` to route around `config_lint.py`'s discovery bug, got a correct result, and reported the workaround in passing — but never escalated it as a possible script defect. It sat unfixed for a full extra session and fired again on the next test that omitted `--config`, before finally being recognized and fixed. The tactical fix that gets a test to a correct result and the report that the fix was *necessary* are two different obligations; doing only the first is how a real defect survives an otherwise-careful test run. | ALL (review discipline, not one skill) | **DELIVERED** — `references/standing-principles.md` §11 (+ byte-verified plugin mirror). |

## Cross-cutting implementation decision (user, assembly phase)

R5, R16, R38, R41, R53 — the five ALL-owner requirements — are implemented as **ONE shared file,
`references/standing-principles.md` at repo root**, pointed to by all four skill bodies, NOT as five
independently-maintained copies audited for consistency after the fact. Same fix already applied to
the feature model, applied to the same class of drift risk. R58's cross-skill echo also lives there
(the verbatim persona line's HOME stays in ftc-team-config; standing-principles carries the echo for
the other three). Each SKILL.md body carries only its pointer plus any skill-SPECIFIC sharpening.

**R58 — why this ONE requirement is inline (in TC) rather than pointer-only, stated for the record.**
R58 is not a reference fact to look up; it is a *behavioral gate that fires at the moment of action*
("stop and ask BEFORE generating code"). A gate is more reliably honored when it sits at the decision
point than when it must be fetched from another file mid-decision — and **ftc-team-config is the
skill whose decision unlocks generation** (flipping `generation_allowed` to true is the moment this
gate fires), so the line stays operative *there specifically* even after §23's split. **Post-§23
correction:** the physical act of generating code moved to `ftc-construct` — TC no longer writes
files itself — but the ask-vs-proceed decision R58 governs is still TC's: it is the choice of
whether the config is settled enough to hand off, not the act of writing a file. `ftc-construct`
carries its own, distinct gate (R82: hand back if `generation_allowed` is false) rather than a copy
of R58 itself, since R82 fires on a different question (is the input trustworthy) than R58 (should
I stop and ask more). Hence exactly TWO verbatim instances of R58 by design: the **home copy in the
TC body** (where that specific gate is operative) and the **canonical copy in standing-principles.md
§4** (which the other skills inherit by pointer, since for them it is guidance, not an operative
gate). This is a real, narrow exception to pure-pointer, not an oversight. The two copies are
**verified byte-identical** (sha `71d8d15009ac`, same standard as R80's citation byte-match) — so
the 2-copy design carries no drift risk. Re-run the byte-check if either is edited.

## Coverage table (LIVE — updated as each skill is drafted)

Per-skill implementation columns get filled in as bodies are written: requirement ID → file + section/line.
Final check before phase close: (a) zero requirements with no owner that aren't explicitly `deferred`;
(b) every multi-owner requirement has its overlap rationale in the table above.

| Skill | Status | Implements (IDs) | Where |
|---|---|---|---|
| ftc-team-config | **SIGNED OFF** (iter-1 12/12 with-skill; iter-2 eval-2 re-run confirmed SCRIPT-level constraint catch after the requires-annotation patch) — original scope, generation-inclusive. **§23 update, RE-EVALED (not left stale):** §6 body changed from "generate the code" to "hand off to ftc-construct"; a trimmed re-eval against the skill's actual current scope (confirm/validate/signal/handoff, not generation — that's ftc-construct's job now) ran 3 with-skill scenarios + 1 baseline contrast, **7/7 assertions PASS**, full report at `evals/post-construct-split-reeval.md`. The original 12/12 result stands for what it always covered (inference, validation, empirical questioning, hub-generation gate) but no longer speaks to post-generation_allowed behavior on its own — the re-eval is what closes that specific gap. | R3-R8, R15-R16, R32-R33, R38, R41, R44, R47-R50, R52-R60, R67, R71, R73, R89 | SKILL.md: R3/R7 → §"Validate" + scripts/validate_config.py (tested: fires on invalid-constraint fixture); R8/R15 → §"Infer" (Haiku-first, pinned agents); R32/R55/R73 → §"Confirm back" + validate_config.py `generation_allowed` (tested: blocks rookie fixture's unconfirmed pathing); R33/R34-TC-side/R52/R44 → §"Hand off to ftc-construct" (renamed from "Generation rules", R89); R47/R48 → §"Ask only what's left" + scripts/question_order.py (tested: opmode_style=15 top); R49 → §"Infer before asking"; R50 → mandatory-set para; R54 → "pre-fill, not a decision"; R56 → §"Hand off to ftc-construct" lead para; R57 → §"Keep the config live"; R58 → verbatim quote in §"Confirm back" (unchanged, byte-verified post-edit); R59/R60 → hub-generation gate para (pointer to HW file, read fresh); R6 → ACTIVE resolution throughout; R5/R16/R38/R41/R53 → standing-principles pointer (top); R67 → evals/fixtures/ (3 configs) + evals/post-construct-split-reeval.md (§23 re-eval, same 3 fixtures reused); R71/R73 → **eval PASSED iteration-1** (12/12 with-skill vs 4/12 baseline: confirm-gate blocked generation in evals 1-3; R60 pointer verified live in eval 4); R89 → §"Hand off to ftc-construct" — **re-evaled, PASS** (scenario 3 of the §23 re-eval: fully-confirmed fixture correctly hands off to ftc-construct, generates zero code itself; baseline contrast confirms a no-skill agent generates directly with an invented tuning constant instead — the exact failure this closes). Known gap logged: validate_config.py does not machine-check mechanism-level `requires` annotations (turret→shooter) — caught by model diligence in eval 2; iteration candidate |
| ftc-construct | **SIGNED OFF (§23): boundary/routing-tested AND generation-quality eval-suited at the same bar as the original four.** 3/3 with-skill scenarios pass (independently re-verified via direct grep on generated files, not self-report alone), 1 baseline contrast confirms the failure mode this skill prevents is real. Full report: `evals/generation-quality-eval.md`. | R81-R93 | SKILL.md (both copies): R81 → whole-file existence; R82 → §0 "Precondition — confirmed config, or hand back" (re-verified: `config_found`/missing-file handling fixed at the script level, R91); R83 → §2 "Scaffold from the quickstart template" + `quickstart-template/` (15 files, NOTICE.md attribution verified; eval-1/eval-2 both confirm real adaptation, not blind copying — eval-2 caught an opmode_style mismatch and rewrote accordingly); R84 → §3 "Ground the implementation" + `references/library-docs/` (9 libraries, 56 files, source+fetch-date headers; eval-1 cites two specific FTCLib doc files actually read before writing); R85 → §3 pattern-citation para (eval-1: correctly abstained from citing any of 9 corpus patterns since none matched the confirmed config — abstention, not oversight); R86 → §3 hardware-value para (eval-3: unseeded SKU correctly triggers a fail-fast NaN + TODO, not an invented tuning constant — direct contrast with the baseline's fabricated "1500 ticks/sec"); R87 → §4 "Structural rules" (eval-2: independently grep-verified zero shooter/turret code for a config with both declared `none`); R88 → §5 "Mandatory verification" (all 3 evals show real config_lint.py/failure_mode_lint.py/rules.py invocations with pasted output, combined result reported, not just "code written"). |
| ftc-hardware-lookup | **SIGNED OFF (behavioral + catalog seed, 2026-07-08). Eval 12/12 with-skill vs 3/12 baseline (break-it R75)** | R1-R2, R5, R10, R16, R20, R27-R31, R35, R38, R41, R53, R60, R67-R68, R71, R75 | R20/R28/R31 → references/catalogs/{motors,servos,INDEX}.json (5 parts, each value _source-cited, tier-1); R30 → scripts/motor_math.py + trajectory_solver.py CLI (both ABSTAIN on missing data, tested); R10/R16/R53/R75 → SKILL.md route-to-data gate (eval-2 fabrication trap held: abstained on unseeded ratios, 0 fabricated numbers); R35/R68 → per-value _source; R38/R71 → abstention verified live; R60 → hub-generation briefing hosted here, read by TC; R67 → 4 break-it evals. EVAL-SURFACED CORRECTION: INDEX gap-list wrongly listed 43.7:1 (nonexistent) — fixed. SOLVER high-arc branch: was going to log non-blocking, but the DECODE-geometry check overturned that (close-range shots ARE steep, 58-60 deg hoods) → FIXED (robust full-range scan replaces the monotonic-bisection bug; high-arc drag now 78.4 deg not 106 deg garbage, steep close shots handled, unreachable abstains). Body/scripts done; catalog seed VALUES signed off (per-value Rule-7, CATALOG-SEED-REVIEW.md, 2026) |
| ftc-rule-check | **SIGNED OFF (iter-2 with R79+R80; with-skill 6/6 evals 100%, baseline 15%). R79 freshness step-0 (byte-verified STALE/UNVERIFIABLE, STALE-branch open item logged), R80 verbatim citation text (byte-match confirmed)** | R1-R2, R5-R6, R9, R14, R16, R19, R22-R27, R35-R38, R41, R53, R64, R67, R70, R74, R76 | R22 → scripts/rules.py lookup (one-hop cross-refs; eval-2 traversed R105→G414/G415); R24/R70 → rules.py verify (existence, exit 1 on fake ID); R35 → retrieve-not-recall (eval-1 caught baseline's real-but-wrong R104-for-R101); R23/R26 → SKILL.md verdict-shape + ambiguous-over-confident; R25 → Q&A clarification-tier; R27 → eval-3 resolved [[TABLE:12-8]] into HW manual-tables (RC/HW boundary); R64/R74 → effective_date surfacing + staleness flag (all data base-manual); R5/R16/R38/R41/R53 → standing-principles pointer. NOTE: eval-4 premise self-corrected (manual DOES address via R205), non-discriminating, kept as regression guard |
| ftc-code-review | **SIGNED OFF (2026, on 3 findings, precision check per R100 — Phase D: "guaranteed" here is a structural claim about deterministic pattern-matching, not an empirical one about bug coverage; re-scoped below to name exactly what was tested rather than read as unbounded: (1) a deterministic script that matches a specific pattern will always fire on that pattern regardless of repo size — proven at both scales for the 3 specific test needles this fixture buried, not "catches every possible bug"; (2) favorable cost profile — O(1) script call vs ~70k tokens for the equivalent baseline result; (3) crossover point where determinism beats reading is honestly UNRESOLVED and not worth manufacturing a fixture to force). Small-fixture floor +0.25; large-fixture no catch-rate gap at 2343 lines, same 3 needles** | R1-R2, R4-R7, R11-R16, R21, R33-R34, R36, R39-R46, R51-R53, R62-R63, R67, R69, R72 | R11/R62 → failure_mode_lint.py (god_opmode+mutable_static fired, reported authoritative); R40/R34/R69 → scripts/config_lint.py (turret-vs-config:none flagged; self-test); R42-R46/R72 → eval-2 grounded no-inflation in stored §12 shared-ancestry tags, routed candidate to corpus (not minted inline); R63 → eval-4 evidence-not-verdict; R5 → rookie depth; R13 → full-review agent (not invoked on trivial fixture, correctly); R4/R52/R51 → body. FIXTURE LIMITATION logged: 3 files under-stress the determinism advantage; +0.25 is a floor. LARGE-FIXTURE FOLLOW-UP (2343 lines / 23 files, 3 buried needles): both thorough baselines READ ALL 23 FILES and caught all 3 needles → NO catch-rate gap even at this scale. Honest reframe (not a delta): at 2343 lines a careful model still reads exhaustively; the determinism value is GUARANTEED-catch-at-O(1)-cost (one script call vs ~70k tokens of exhaustive reading), and a catch-RATE gap needs a scale where reading-everything fails (10k+ lines or a genuinely rushed/human reviewer) — threshold is higher than 2343 lines. Linters verified to catch all 3 deterministically regardless. |
| references/standing-principles.md (shared) | **written** | R5 (§5), R16 (§1, with 21813 + gravity examples), R38 (§2), R41 (§3, with 24089/12808 re-check lesson), R53+R58 echo (§4), R77 (§6 + canonical path table), R90 (§9, added §23), R100 (§10, added §25, unhedged-claim suspicion rule), R102 (§11, added §26, workaround-is-a-finding rule) | references/standing-principles.md §1-§11 |
| (deferred pass) | — | R17-R18, R65-R66 | explicitly deferred, listed so Session 2+ inherits a list, not silence. **R61 removed from this row (§23): no longer purely deferred** — see its own row above. |
