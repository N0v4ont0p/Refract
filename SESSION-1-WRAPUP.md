# Session 1 — close-out (Phase 6)

Concise wrap-up of the FTC skill-suite construction session (Team 19859, DECODE). The authoritative
live state is [SESSION-1-CHECKPOINT.md](SESSION-1-CHECKPOINT.md); this file is the reader-facing summary.
Governed by [PLAN.md](PLAN.md), which stays authoritative over anything here.

## What was built

- **Season-agnostic core** — `core-feature-model.yaml` + the replaceable `season-extensions/` layer
  (§3/§4/§10). Only `season-extensions/*.yaml` carries season-specific content.
- **Rules reasoning (§8)** — `tag_manual.py`: deterministic manual tagger (212 rules, 130 cross-refs,
  0 dangling, 38 tables), with the §8↔§9 table-pointer mechanism (tables are §9-owned structured data
  referenced by ID, never paraphrased into rule prose).
- **Subagents (§5)** — 4 definitions (pattern-extractor, provenance-checker, bulk-tagger, full-review),
  pinned full model IDs so a model change is a flagged edit, not silent drift.
- **Hub-generation research (§7/§15.2)** — REV Control Hub + SystemCore/MotionCore references, with a
  time-gated `hub_generation` elicitation (asked only once the hybrid-legal window opens, ~2027-28).
- **Failure-mode taxonomy (§9/§17)** — `known-failure-modes.md` + `failure_mode_lint.py` (6 deterministic
  checks). Two risk classes are corpus-derived this session: **global-mutable-static / cross-opmode
  persistence** (with a tiered, validated linter check) and the **file-versioning-as-VCS** case study (32477).
- **Pattern corpus (§4/§12)** — **64 distilled patterns across 9 teams** (file+line refs only, never code
  dumps), each provenance-classified before any confidence tag; `cross-team-findings.yaml`, `SOURCES.md`,
  `REVIEW-QUEUE.md`. Plus a corpus-built ballistics feasibility artifact (`trajectory_solver.py` +
  `decode-artifact-ballistics.json`, gravity corrected to 386.4 in/s²).
- **Season transition proof (§19)** — `season-extensions/biobuzz-2026-27.yaml`, a draft-only preview.

## Cross-team findings

| Finding | Confidence | Rests on |
|---|---|---|
| `orchestration-nonblocking` | **medium-high** | 3543's cross-platform leg defeating the LinearOpMode forcing discount |
| `shooter-empirical-vs-physics` | **high** | 6 empirical legs; 3 teams built a ballistics solver and shipped empirical anyway (discount narrowed to spin/slip) |
| `moving-shot-compensation` | **medium** | 3 genuinely distinct SOTM methods → design space is open (descriptive, not prescriptive) |
| `sensing-modality` | **medium** | 5 teams; modality driven by information-need, not robustness |

## Rule-7 track record — ranked by consequence (the signal Session 2 should inherit)

Four times this session a plausible-sounding claim was corrected against actual source. Ranked by what
**shipping it uncaught would have cost** — not by when it happened. The ranking itself is the lesson:
it tells Session 2 which *class* of claim deserves the most default suspicion.

1. **21813 — mecanum matrix sign error. CATEGORICALLY WORSE THAN THE OTHER THREE.** The paper's headline
   page-7 inverse-kinematics matrix drops per-wheel position signs (yields FR `+ω(rx−ry)` instead of
   `+ω(Lx+Ly)`). A team could have **copied it straight into deployed drivetrain code and rotated wrong on
   the field.** This is not a wrong sentence in the corpus — it is broken math shipping into a real robot.
   Different *kind* of harm: downstream engineering failure, not corpus imprecision. → **Class deserving the
   MOST default suspicion: external formulas/specs that could be copied into code.** Verify by derivation +
   degeneracy-to-known-case before ANY promotion. (Here: the derivation was sound but the printed result
   was not — so "the math looks rigorous" is not sufficient; check the *final* artifact a team would copy.)
2. **24089 — "physics counterexample" framing.** Would have put a wrong analytical CONCLUSION in the corpus
   (physics is a proven fielded shooter approach — false) AND suppressed the `moving-shot-compensation`
   finding entirely. Broad: it misdirects design advice on a core mechanism. Mediated by human review of advice.
3. **12808 — "concurrency/data-race architecture."** Would have shipped a false failure-mode risk class + a
   linter check hunting a non-existent problem → false warnings at scale, eroding trust in the taxonomy.
   Self-limiting (false positives get noticed), but actively misleading while live.
4. **Iron Reign / KookyBotz — idiom attribution.** Would have asserted a false provenance lineage on one
   pattern → confidence mis-weighting, single-pattern scope. Most contained; already gated by §12.

**Synthesis for Session 2 — two suspicion classes, one shared root cause:**
- **Highest:** any external formula/spec/number that could be copied into robot code (the 21813 class). Its
  failure mode is deployed harm, so it earns verification-by-derivation regardless of how authoritative it looks.
- **High:** any claim about *what a team's fielded code does* that was restated from a prior conclusion or a
  surface signal (a name, an earlier note) without **re-running the check at source** — the shared root cause
  of both #2 (24089) and #3 (12808). Rule 7 applies *hardest to already-agreed claims*, where everyone's
  incentive is to move on. `moving-shot-compensation` exists ONLY because that re-check was run one more time.

## Phase 8 — cleanest validation yet of the core/season-extension split

Producing an entire second season's draft (`biobuzz-2026-27.yaml`) took **zero edits to any invariant layer**
— `core-feature-model.yaml`, §5, §8, §11, §12 all untouched; `season-extensions/ACTIVE` still reads
`decode-2025-26`. Season-agnosticism was *tested against real upcoming material*, not asserted. And the
deliberation checkpoint caught **PLAN.md's own framing**: "Pollen is similar to Artifacts" is false on the
dimension that matters — Pollen (~2.8–3.0 in) is ~40% smaller than the corpus-verified DECODE Artifact
(5.0 in, from 24089's ballistics). So the draft refuses to assume the DECODE intake/shooter category transfers
and leaves launch/turret/zones/endgame `UNKNOWN` rather than porting archetypes on a hunch. The same discipline
that caught the four claims above caught the plan document describing itself.

## Open threads carried to Session 2

- **Deferred hardening:** `22105-D` provenance subagent re-run (`REVIEW-QUEUE.md`); 24089 `lioncore/tasks/`
  orchestration-leg extraction (its own review batch); 12808 + 15083 `held:` items. Pioneer-Robotics dropped
  (opportunistic; revisit only if a confirmed slug surfaces).
- **21813:** usable as a reference for the *standard* rigid-body/mecanum derivation, with an explicit
  "derive the matrix per-wheel; do NOT copy page 7" warning; the 6-wheel novelty stays unverified.
- **BIOBUZZ:** at kickoff (2026-09-12) run §19 steps 4–6 against the real manual + a §20 eval refresh; collapse
  the Pollen 2.8–3.0 in range to the official spec before any mechanism math.
- **Out of scope for Session 1 (Session 2 work):** the elicitation build (§13/§15) and the QuickStart repo (§16).
