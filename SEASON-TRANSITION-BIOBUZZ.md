# Season transition: DECODE (2025-26) → BIOBUZZ (2026-27)

Kickoff 2026-09-12. Work started 2026-09-13, the day after release. This is PLAN.md §19 (Season Transition
Protocol) run for real for the first time, plus the plan for everything it showed still needs doing.

**Status (updated 2026-09-13, second pass):** all six §19 steps done. **`season-extensions/ACTIVE` =
`biobuzz-2026-27`** (sign-off given; `transition_check.py` passed before and after the flip). The
Q&A-dependent questions stay open until Q&A opens 2026-09-28. Quant strategy is a provisional draft in
`strategy/biobuzz-2026-27/`. Eval iteration-1 results: §7. Nothing is committed.

---

## 1. Sources ingested (all verified, nothing from memory)

| Source | Tier | Where |
|---|---|---|
| BIOBUZZ Competition Manual V1, HTML edition (rules, tables, sections, glossary extracted from it) | T1 official | `corpus-staging/manual-biobuzz-2026-27/cm.html` + `SOURCES.md` (sha256) |
| Same manual, PDF. Your `BIOBUZZ_Competition_Manual_V1.pdf` has **identical extracted text** to FIRST's PDF | T1 | `cm-pdf-layout.txt` |
| Team Update 00 (2026-09-12), the latest as of 2026-09-13 | T1 | `tu-00.pdf/.txt` |
| Event Field Setup Guide V1.0: HIVE tip calibration | T1 field doc (not a rule) | recorded in the season yaml |
| FTC SDK v12.0 release (2026-09-12): AprilTag Cluster breaking change; BIOBUZZ tags "not suitable for absolute Field Localization" | T1 SDK | `gh api` on the FtcRobotController README |
| AndyMark element listings, goBILDA/REV/AndyMark StarterBots, community threads | T2/T3, labeled | scratchpad report only, not promoted to the skills |

Not found or not yet published: POLLEN/NECTAR mass and hollow-vs-solid (T1), a BIOBUZZ section of
ftc-docs' field-coordinate page, the AprilTag-cluster docs page (stub until 2026-09-14), Team Update
01+, and Q&A (opens **2026-09-28 12:00 ET**).

## 2. What changed in the game, for design and code (all verified in the manual text)

- **Elements.** POLLEN is ~2.8 in yellow (40 per match). NECTAR is ~3.6 in, red/blue (8 each). Both are
  polyethylene. Mass is UNKNOWN.
- **Scoring (Table 10-2).** LEAVE 3. PARK in the LOADING ZONE 5+5. HIVE TIP 20 (AUTO or TELEOP).
  - The only legal way to TIP is **launching** into the upward CELL (§10.5.1).
  - Balls left in a CELL at the end: 2 each. An owned FLOWER: 2 per ball. Bottom-NECTAR bonus: 5.
    GARDEN: 1 per ball.
- **Ranking points (Table 10-3, non-premier events).** SWARM = 16 LEAVE+PARK points. POLLINATOR
  1/2 = 4/7 TIPS.
- **Match.** 30 s AUTO, 8 s transition with no powered motion (G403), 2:00 TELEOP. There is no period
  named ENDGAME; NECTAR→FLOWER unlocks in the last 60 s (G410).
- **Robot.**
  - Start inside an 18 in cube, fully stationary (R102).
  - Expand to at most 18×24×29 in, **physically** limited; software limits don't count (R105).
  - 8 motors + **8 servos** (R503; DECODE allowed 10). WATTOS Stingray is now a legal motor
    (Table 12-1). Gas shocks are allowed (R801).
  - At most 4 elements CONTROLLED, and herding counts as CONTROL (G407, Glossary).
- **Code-legality changes.**
  - **R704 names FTC Dashboard and FTControl Panels as prohibited streaming.**
  - SDK v12.0 removes `.id`/`.metadata`/`.center` from the base `AprilTagDetection` (compile-verified;
    `.ftcPose`/`.robotPose` still compile), so older tag-identity code breaks.
  - BIOBUZZ AprilTags are IDs 30–45 on the CELL undersides, facing down, and they move when the
    HIVE tips.
- **HIVE tip calibration (setup guide, not a rule).**
  - With 3 NECTAR in the CELL: the 3rd POLLEN tossed in tips it.
  - Empty CELL: the 8th POLLEN tips it.
  - Fields vary.

All of this, with citations, is in `season-extensions/biobuzz-2026-27.yaml`.

## 3. Bugs and gaps found. Status: FIXED (verified) or OPEN

"Runtime-breaking" means it would give a BIOBUZZ user a wrong answer if ACTIVE were flipped.

| # | Finding | Status |
|---|---|---|
| 1 | `rules.py` read one hardcoded corpus. It would certify DECODE numbers as valid BIOBUZZ citations (`verify R615 R207` → all_valid) | **FIXED**: per-season corpora, `--season` (default ACTIVE), every output names its season/manual. MCP server + tests too |
| 2 | Freshness check never checked *which game* the live page is. FIRST reuses the URL, so a DECODE corpus (TU32) vs BIOBUZZ's TU00 page would read CURRENT once a live TU number appeared | **FIXED**: visible-text game identity → `WRONG_SEASON`. Live now: DECODE=WRONG_SEASON, BIOBUZZ=CURRENT. A substring check was fooled by a reused photo's alt text reading "DECODE", so the check uses visible text |
| 3 | Tagger hardcoded rule series A,E,G,I,R,T, dropping BIOBUZZ's C301 | **FIXED**: series read from the manual's own legend. L (§14) is declared but has 0 rules in V1 |
| 4 | Tagger: table text matched exactly. BIOBUZZ Tables 12-1 motors, 12-2 servos, 12-8 wire sizing silently unlinked | **FIXED**: whitespace-insensitive match (33/34 linked; the remaining one is award table 6-6) |
| 5 | Tagger: rule chunks ran to the next *rule*, not the next *heading*. **Pre-existing in DECODE**: A215 (awards) held all of §7–10 game details as "rule" text (47k chars) | **FIXED**: bounded at headings. DECODE regression: 33 chunks strictly truncated, every cut at a real heading, 31 false edges removed. Non-rule text now in `sections.json` |
| 6 | Tagger: BIOBUZZ HTML TOC stops at level 2, so section paths were empty | **FIXED**: 161/161 headings |
| 7 | `*` headline meaning changed: DECODE "relatively unchanged", BIOBUZZ "Evergreen — details may change" | **FIXED**: field renamed `asterisk_marked`; meaning quoted per season |
| 8 | Team configs had no season stamp. A value legal in both games (`intake: roller`) passed silently for a game nobody asked about | **FIXED**: `_meta.season` required with season mechanisms. Mismatch blocks generation with a direction-aware message. 8 fixtures stamped, all states unchanged |
| 9 | Validator accepted a DRAFT season file as ACTIVE, and a string `UNKNOWN` declaration let any value pass | **FIXED** |
| 10 | `config_lint.py` token map was DECODE-only | **FIXED**: tokens come from each season yaml's `code_tokens`. A missing entry is reported `unchecked`, not clean |
| 11 | Season rules that constrain *code* had no machine check | **FIXED**: `code_constraints` with `detect` regexes (R704 regex targets streaming calls, not `@Config`). On the template it now flags only `tuning/DashboardTelemetry.java` (see row 14) |
| 12 | Trajectory solver used DECODE's 5 in / 75 g ball for any season | **FIXED**: `physics/invariants.json` + `physics/<season>/<element>.json`. BIOBUZZ drag-aware angle **abstains** (no measured mass). DECODE output identical to before |
| 13 | Official-document inconsistencies: TU00 "R510" (manual: R501); R601.A→R610 (fuses are R604); R903→R203 (content is R202) | **RECORDED** in season yaml; submit via Q&A |
| 14 | Quickstart template wires Shooter+Turret into `ExampleTeleOp` unconditionally, and streams to FTC Dashboard unconditionally | **FIXED (W3)**: ExampleTeleOp = drivetrain+intake; telemetry Driver-Station-only; Dashboard graphing isolated in `tuning/DashboardTelemetry`. Compiled clean against SDK 11.1 and FIRST's official v12.0 checkout (13 classes). Decision log 0002 |
| 15 | Pattern corpus: 8 of 11 files have no season scope. DECODE shooter/AprilTag-relocalization patterns look "applicable" to a launch game | **FIXED (W4)**: all 77 patterns carry `season_scope` (51 invariant / 26 decode-2025-26) + basis; findings carry `seasons_observed` + transfer caveats; `question_order.py` skips other-season patterns (BIOBUZZ: 25 skipped) |
| 16 | Pedro/SDK field-coordinate docs + examples describe DECODE's field and motif tag IDs 21–23 | **FIXED (W5)**: 17 docs carry SEASON SCOPE headers, 8 AprilTag docs an SDK VERSION SCOPE header (upstream text untouched, verified); BIOBUZZ StarterBot summaries (goBILDA/REV/AndyMark, tier 2). ftc-docs still has no BIOBUZZ coordinate section (checked live) — orientation not asserted |
| 17 | `hub-generations/rev-control-hub.md` cites DECODE rule numbers (R609/R614/R704 mean other things now) | **FIXED (W2)**: per-season citation table, all IDs verified in both corpora. Found: its "libs/ modification is illegal" line was tagged [T1] but no manual rule says so in either season — relabeled as a project rule |
| 18 | Requirement IDs in docs shared the manual's `R1xx` namespace, so `verify` passed a mis-lifted requirement ID | **FIXED (W6)**: 645 requirement references in 43 files → `REQ-n`; the 84 R101–R105 occurrences classified one by one (manual-rule uses kept) |
| 19 | Pre-existing dual-copy drift: plugin `known-failure-modes.md` lacked the 6 newest entries; `cross-team-findings.yaml`, `SOURCES.md`, `15993.yaml`, `extract_feature_vector.py` stale; plugin lacked `19859.yaml` | **FIXED (W7)**: synced source→plugin; 19859 may ship publicly (PHASE-F-G permission scope); 32008 stays out — its SOURCES row dropped from the plugin copy, checklist example anonymized |
| 20 | SDK v12.0 claim was over-broad ("legacy AprilTag loops no longer compile") | **CORRECTED by compiling**: only `.id`/`.metadata`/`.center` left the base `AprilTagDetection`; `.ftcPose`/`.robotPose` still compile. Season yaml, detect regex, SKILL.md, fixture and eval fixed; fixture now fails to compile on v12.0 as the eval states |
| 21 | Tagger truncated table captions ("Legal") for 12-4/12-5/12-6 | **FIXED**: captions only changed, both seasons; rules/tables/cross-refs byte-identical |
| 22 | Field Setup Guide gives GARDEN/LOADING ZONE tiles (A1/F6, A5/F2) the manual text doesn't | **RECORDED** as field-document data in the season yaml (grid orientation still figure-only); guide staged with hash |

## 4. The design rule: the season is part of the key

A season transition is **not** a one-file swap. Everything whose meaning FIRST reuses or replaces
each year is stored under the season slug and read by naming the season:

```
season-extensions/<slug>.yaml          mechanisms, field facts, scoring, code_tokens, code_constraints, open questions
rules/<slug>/                          rules, sections, glossary, cross-refs          (rules.py --season)
manual-tables/<slug>/                  legal-parts tables                             ([[TABLE:id]] per season)
physics/<slug>/<element>.json          scoring-element ballistics                     (trajectory_solver --season --element)
corpus-staging/manual-<slug>/          raw manual + TU + SOURCES.md hashes
team-config.yaml  _meta.season         which game the season layer was confirmed for
evals/<slug>.json                      per-season eval set (evals.json = decode-2025-26, now pinned)
```

Season is resolved as: named in the question → team config's `_meta.season` → `ACTIVE`. Every answer
says which season it used. Core axes (drivetrain, localization, software stack, tuning, frames) carry
across seasons.

## 5. Remaining workstreams, in order

| W | What | Why this order | Size — status |
|---|---|---|---|
| **W1** | **Deliberation + sign-off (§19.5–6).** You review §6 below. Then set `_meta.status: live`, `not_active: false`, and write `biobuzz-2026-27` into both `ACTIVE` files | everything team-facing waits on it | you — **DONE** 2026-09-13 |
| W2 | Re-cite `hub-generations/rev-control-hub.md` by rule headline + season (both copies) | wrong citations surface in team-config today | S — **DONE** |
| W3 | Quickstart template season-scoping: wire `ExampleTeleOp` from the config's mechanisms; gate FTC Dashboard behind one default-off switch for competition builds (R704); rename season comments. Compile-test | legality of generated code | M — **DONE** (compile-tested SDK 11.1 + v12.0) |
| W4 | Pattern corpus `season_scope: invariant \| decode-2025-26` per pattern (11 files, both copies). `cross-team-findings.yaml` gets `seasons_observed`. Declare the `season.*` predicates patterns use, or map them to `season_mechanisms` keys | stops DECODE shooter/relocalization evidence being cited as BIOBUZZ evidence | M, needs per-pattern judgment — **DONE** |
| W5 | Season-tag DECODE-specific library docs (Pedro coordinate conversion "inverted for decode", motif tag IDs, DECODE StarterBot guides, REV decode kickoff folder). Fetch BIOBUZZ StarterBot docs (goBILDA/REV/AndyMark) as T2. Verify field orientation once ftc-docs publishes its BIOBUZZ section | pose conversions are mirrored if the DECODE guidance is applied | M — **DONE** (orientation still unpublished) |
| W6 | Rename requirement IDs `R1xx` → `REQ-1xx` in TRACEABILITY/standing-principles/scripts | a real false-verify path | S, mechanical — **DONE** |
| W7 | Resolve the dual-copy drift in §3 row 19 (sync, or document an intentional public subset) | parity discipline | S — **DONE** |
| W8 | BIOBUZZ ball constants: once a team measures POLLEN/NECTAR mass/diameter (or T1 publishes), add `physics/biobuzz-2026-27/{pollen,nectar}.json` with origin `measured` | unblocks drag-aware launch angles | S, needs data — **BLOCKED on data** — no T1 mass; measure POLLEN/NECTAR |
| W9 | §19 step 4 quant strategy (Opus xhigh subagent): cycle-time / expected-value model from Table 10-2/10-3 + tip calibration **ranges**, provisional, revised after first events | kickoff-week strategy; no rule dependency left except tip-count variance | M — **DRAFT DONE** — `strategy/biobuzz-2026-27/` |
| W10 | Recurring: `check_freshness.py --season biobuzz-2026-27` each session; on TU01+ re-stage + `tag_manual.py --season biobuzz-2026-27`, diff, re-run evals. Ingest Q&A from 2026-09-28 as `clarification` tier | manual changes weekly in-season | ongoing — **ONGOING** — use `ftc-season-transition` Team Update loop |
| W11 | Build `.claude/skills/ftc-season-transition/` (currently an empty directory) as the skill that runs §19 end to end with the scripts above, so the 2027-28 transition is one invocation | next season | L, after W1–W7 — **DONE** — `.claude/skills/ftc-season-transition/` |

## 6. Deliberation checkpoint — what needs a human decision (from the season yaml)

1. **Mechanism taxonomy** in `season_mechanisms`: `intake, hive_launcher, turret, aim_vision,
   element_color_sensing, capacity_limiter, flower_placer, flower_pollen_retrieval, endgame_parking`.
   Every key comes from a rule, but the option names are placeholders unless a rule names them. Keep,
   rename, merge?
2. **Turret.** No rule argues for or against it. BIOBUZZ's aiming target moves (it's on the HIVE), so
   DECODE's turret evidence doesn't transfer. Keep it as an open option, not a recommended archetype?
3. **Intake for two diameters** (2.8 in and 3.6 in) that must stop at 4 elements. Treat it as a new
   category, not a DECODE carry-over?
4. **Ambiguities to file in Q&A (2026-09-28):**
   - Does launching into a FLOWER count as "placing"?
   - POLLEN placed in a FLOWER before 60 s: which rule, if any, penalizes it?
   - How can opponent NECTAR legally reach your GARDEN, given that herding is CONTROL?
   - Can per-TIP NECTAR entries be banked?
   - The three stale cross-references in §3 row 13.
5. **Figure-only geometry** needed before auto paths: GARDEN corners, FLOWER positions, upward CELL
   opening height. These come from CAD / the field setup guide, not the text. Do we pull them from the
   Onshape CAD as T1 and store them as season field data?

## 7. Training run — eval-driven iteration, per season

Refract has no weights; "training" means running each skill against adversarial evals, with and
without the skill loaded, grading, fixing the skill, and repeating (the existing
`.claude/skills/*-workspace/iteration-N/` loop).

**Set up (done):**
- `ftc-rule-check/evals/biobuzz-2026-27.json`: 10 cases. Covers renumbered rules, carried-forward
  limits, R704 Dashboard, TU00's wrong number, physical-vs-software expansion, herding=CONTROL,
  figure-only ambiguity, launch-vs-place, a prior-season question, and Evergreen≠unchanged.
- `ftc-code-review/evals/biobuzz-2026-27.json` + `fixtures/biobuzz-robot/`: 4 planted season issues.
  Lint catches exactly 3; the moving-tag localization issue has no regex on purpose.
- `ftc-team-config/evals/biobuzz-2026-27.json` + `fixtures/biobuzz-veteran-launcher.yaml`: the
  season-boundary carry-core flow, plus the 3 validator states (verified).
- `ftc-hardware-lookup/evals/biobuzz-2026-27.json`: element-abstaining ballistics, season table read.
- Existing `evals.json` files pinned `"season": "decode-2025-26"` as the DECODE regression set.

**Results (run 2026-09-13):**
- Iteration-1 (60 subagents, independent graders re-checking claims with `rules.py --season`):
  **with skill 39/39 assertions (100%), 2 minor factual errors; baseline (web access, no repo) 26/39
  (67%), 9 factual errors.** Per skill, with/without: rule-check 24/24 vs 16/24; hardware 5/5 vs 2/5;
  team-config 4/4 vs 2/4; code-review 6/6 vs 6/6.
- Where the skill made the difference: renumbered R101→R102, TU00's "R510", GARDEN corner (baseline read
  a corner off rendered figures), FLOWER launch-vs-place (baseline gave a confident "no"), DECODE-only
  question, Evergreen meaning + WATTOS table, drag angles (baseline modeled a 3–5 in ball), season-boundary
  config (baseline carried DECODE assumptions). Some baseline misses are grounding-only (right content
  from a downloaded manual, no citable path).
- Not discriminating yet: servo count, R704, expansion, herding, both code-review evals — the baseline
  passed them too; harder variants are the next eval work.
- Iteration-2: fixed the two with-skill slips (servo table flattened to one class; an "only rule" overclaim)
  with a rule-check SKILL.md guard; re-ran both evals: 6/6, 0 factual errors.
- team-config validator-states: deterministic, 3/3 expected states.
- Files: `.claude/skills/*-workspace/biobuzz-iteration-{1,2}/` (answers, commands, grading, benchmark).

**How the loop was run (repeat per iteration):**
1. `iteration-1`: each BIOBUZZ eval × {with_skill, without_skill} in fresh subagents, **ACTIVE left at
   decode** so the season-pinning behavior itself is what gets tested.
2. Grade the assertions (a separate grader subagent per case), write `benchmark.json`.
3. Fix what failed in SKILL.md or scripts. Re-run the failing cases plus the DECODE regression set
   (`evals.json`).
4. After W1 sign-off: flip ACTIVE in a scratch suite root and run everything again (`iteration-2`).
5. Add the ftc-construct generation eval once W3 lands: generate a BIOBUZZ launcher subsystem +
   teleop from the fixture, then gate on config_lint clean (no R704 hit), `emit_tuning verify`, and a
   `rules.py --season` verdict.

Deterministic checks that already pass and serve as the regression floor:
`check_freshness.py --self-test`, `config_lint.py --self-test`, `mcp-server/test_server.py`, all 9
team-config / construct fixtures at their expected states, and DECODE tagger + solver output identical
to before.
