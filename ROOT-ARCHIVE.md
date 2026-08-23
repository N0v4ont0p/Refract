# Project Archive — Session 1 & Phase Findings

Consolidated 2026-08-23 from 6 root-level journal/proposal docs (PHASE-C1-C2-FINDINGS.md,
PHASE-D-FINDINGS.md, PHASE-F-G-FINDINGS.md, SESSION-1-CHECKPOINT.md, SESSION-1-WRAPUP.md,
PROPOSAL-construct-port-mode.md) to declutter root. **PLAN.md and ROADMAP.md are unchanged** —
their §-numbers and phase headers are cited throughout the live skill corpus
(`standing-principles.md`, `docs/getting-started.md`, YAML fixtures, `TRACEABILITY.md`) and
remain the authoritative design/roadmap docs. `TICKTREE-FEEDBACK.md` also stays separate — it's
written to be handed to the TickTree project standalone. Current phase status: see ROADMAP.md's
own Status line (as of this archive: A–J all done, Phase E paused mid-build).

---

## Session 1 — Corpus Construction close-out

Team 19859, DECODE season. Built: the season-agnostic core (`core-feature-model.yaml` +
`season-extensions/`), rules reasoning (`tag_manual.py` — 212 rules, 130 cross-refs, 0 dangling,
38 tables, with the §8↔§9 table-pointer mechanism), 4 subagent definitions (pinned full model
IDs), hub-generation research (time-gated `hub_generation` elicitation, ~2027-28), the failure-mode
taxonomy (`known-failure-modes.md` + `failure_mode_lint.py`, 6 deterministic checks), a **64-pattern
corpus across 9 teams** (file+line refs only, provenance-classified before confidence tagging), a
ballistics feasibility artifact (`trajectory_solver.py`, gravity corrected to 386.4 in/s²), and a
season-transition proof (`season-extensions/biobuzz-2026-27.yaml`, draft-only preview).

**Mining coverage:** Tier 1 complete (15993: 10 patterns, 18742: 12, 3543: 13). Tier 2 complete,
7 teams (19043: 11, 16093: 5, 22105: 4, 24089: 3, 12808: 3, 15083: 3). Tier 3: `21813-research`
(PDF-only, tier-2/uncorroborated — spot-check caught a real per-wheel-sign matrix error, not
promoted) and `32477-history` (failure-mode case study — file-versioning-as-VCS + god-OpMode,
recorded in `known-failure-modes.md`). Pioneer-Robotics dropped (slug never confirmed).

### Cross-team findings (final state)

| Finding | Confidence | Rests on |
|---|---|---|
| `orchestration-nonblocking` | medium-high | 3543's cross-platform leg defeats the LinearOpMode forcing discount |
| `shooter-empirical-vs-physics` | high | 6 independent empirical legs; 3 teams built a ballistics solver and still shipped empirical (discount narrowed to spin/slip) |
| `moving-shot-compensation` | medium | 3 genuinely distinct SOTM methods → design space open (descriptive, not prescriptive) |
| `sensing-modality` | medium | 5 teams; modality driven by information-need, not robustness |

### Rule-7 track record (ranked by consequence, not chronology)

1. **21813 mecanum matrix sign error** — worst class: a formula a team could copy straight into
   deployed drivetrain code and rotate wrong on the field. Real downstream harm, not corpus
   imprecision. → verify external formulas/specs by derivation + degeneracy-to-known-case before
   any promotion; "the math looks rigorous" isn't sufficient, check the final artifact a team would
   copy.
2. **24089 "physics counterexample" framing** — would have shipped a false analytical conclusion
   and suppressed the `moving-shot-compensation` finding entirely. Caused by a grep that silently
   failed (unquoted glob eaten by zsh); re-verifying at source caught it.
3. **12808 "concurrency/data-race" architecture** — would have shipped a false failure-mode risk
   class + a linter hunting a non-existent problem. `-Thread`-named classes turned out synchronous.
4. **Iron Reign/KookyBotz idiom attribution** — would have asserted a false provenance lineage on
   one pattern. Most contained, already gated by §12.

**Synthesis:** two suspicion classes share one root cause. Highest: any external formula/spec that
could be copied into robot code (verify by derivation, regardless of source authority). High: any
claim about what a team's fielded code *does*, restated from a prior conclusion or surface signal
without re-running the check at source — Rule 7 applies hardest to already-agreed claims.

### Phase 8 — BIOBUZZ preview (season-transition proof)

Producing `biobuzz-2026-27.yaml` took **zero edits** to any invariant layer (core-feature-model,
§5/§8/§11/§12) — season-agnosticism tested against real material, not asserted. Deliberation
checkpoint caught PLAN.md's own framing: Pollen (~2.8–3.0in) is ~40% smaller than the
corpus-verified DECODE Artifact (5.0in) — the draft correctly refuses to assume the DECODE
intake/shooter category transfers, leaves launch/turret/zones/endgame `UNKNOWN`. Re-verify at
kickoff (2026-09-12).

### Watch-items (not promoted to patterns)

- **"Comment-out-instead-of-delete"** dead/WIP code, observed across 4 teams — flagged for a future
  taxonomy lens, not yet its own finding.
- **Global mutable static / cross-opmode persistence** — formalized into `known-failure-modes.md` +
  linter check `mutable_static_opmode_write`. Fires medium on 19043 (23 fields)/12808 (32)/15083 (5),
  low on 18742/3543/22105, clean on 15993/16093/24089 (correctly distinguishes lifecycle-writes
  from config constants).

### Open threads carried to Session 2

`22105-D` provenance subagent re-run (queued in `REVIEW-QUEUE.md`); 24089 `lioncore/tasks/`
orchestration-leg extraction (pending in `24089.yaml`); 12808 + 15083 `held:` items; 21813 kept as
a reference for the *standard* mecanum derivation with an explicit "derive per-wheel, don't copy
page 7" warning. Session 2 scope (elicitation §13/§15, QuickStart §16) was out of scope for
Session 1 and became the actual product build in subsequent phases.

---

## Phase C1/C2 — Cross-tool compatibility + continuous input layer

**MCP server** (`mcp-server/server.py`): verified real MCP mechanics before building (discarded a
hallucinating first WebFetch, cross-checked package/import path independently). 4 tools, each a
thin `subprocess` wrapper into the exact script its corresponding skill already runs — no
re-derived grounding logic. Tested MCP-path vs. direct-script-path, byte-compared:

| Tool | Test | Result |
|---|---|---|
| `rule_check` | `ids=["R207"]` | byte-match vs. direct `rules.py` |
| `rule_check` | keyword query `"flywheel scoring element"` | caught and fixed a real bug — OR-semantics matched manual boilerplate words; switched to AND |
| `hardware_lookup` | seeded SKU | byte-match |
| `hardware_lookup` | deliberately unseeded SKU | abstains through MCP path too |
| `corpus_query` | `filter="shooter"` | 17 matches, count + confidence/provenance fields match direct parse |
| `validate_team_config` | confirmed fixture | all fields match direct call |

Also opened a real stdio MCP client session and confirmed `list_tools()`/`CallToolRequest` work
over the actual protocol, not just at the Python-function level.

**Skills-format cross-tool baseline** — first-pass trust in agentskills.io's own client-showcase
listing was wrong; independently verified each tool's own docs instead:

| Tool | `.claude/skills/` scanned directly? |
|---|---|
| VS Code/Copilot | Yes — zero-action |
| OpenCode | Yes — zero-action |
| Cursor | No — needs `.agents/skills/` too |
| OpenAI Codex | No — needs `.agents/skills/` too |
| Gemini CLI | No — needs placement + explicit `/skills enable` |

`.agents/skills/` is the emerging shared convention across 3 of the 5. Publishing/symlinking
Refract's skills there would cover 4/5 with no code changes — flagged as a Phase D README
candidate, not built this pass. Antigravity unverified either way.

**OpenCode hooks bridge** — a real community plugin (`opencode-claude-hooks`) runs Refract's
existing `.claude/settings.json` hooks (including the `permissionDecision: "deny"` write-block)
under OpenCode. Requires one line in the *OpenCode user's own* global config — no Refract-repo
artifact to change, so documented rather than built.

**Continuous input layer** (`corpus-input-scan.py`, repo root): drafts only, never auto-merges —
the human-gated checkpoint stays the single most load-bearing discipline in the project. Three
checks (`--team-repos`, `--libraries`, `--rules`): new public team repos via GitHub search diffed
against the corpus's own mined-team list; library releases for the 6 bundled libraries with a
GitHub release feed (REV/Limelight/goBILDA excluded — vendor PDFs, no release concept); Team
Updates via the existing `check_freshness.py`. Real-scanned run caught FTC SDK `v11.2` genuinely
stale (3 days) and a real repo-name bug (`Pedro-Pathing/Pedro` 404 → actual name `PedroPathing`).

---

## Phase D — Final hardening (Part 1)

**Rule-7 staleness re-check, live:** FTCLib/RoadRunner/EasyOpenCV/FTC Dashboard/Pedro all CURRENT;
**FTC SDK STALE** (docs fetched 2026-07-12, real release v11.2 published 2026-07-15 — an offseason
toolchain-minimum bump, not a contradiction of anything stored; addendum added citing the release).

**Fresh eval battery, 6 scenarios, all 5 skills, all regression-free** — including a new
ftc-code-review legality-flavored scenario (turret expansion-limit) that correctly generalized §5's
freshness→lookup→verify flow and returned `ambiguous` (code alone can't establish physical
constraint compliance). This eval also surfaced R101.

**R101 — real bug, fixed at root cause.** `config_lint.py` run without `--config` silently picked
up an unrelated `team-config.yaml` via unscoped downward `rglob`, reporting `clean: true` over a
real finding. Fixed: `find_config()` now walks *up* from the code dir through ancestors, stopping
at the first match — deterministic, bounded at the repo root. Fixed identically in source and
plugin copies, confirmed byte-identical. Full record: TRACEABILITY.md R101.

**R100 self-scan** — grepped ROADMAP.md, TRACEABILITY.md, all 5 SKILL.md files for unhedged
absolute language. One genuine wording-clarity fix (a "catches all needles" claim was accurate but
the qualifying "3 test needles" appeared later in the sentence — tightened at first mention). No
claim required substantive correction.

**Corpus depth check:** 0 new team-repo candidates found this pass — honest result, no padding.

---

## Phase F/G — 19859 & 32008 ground-truth corpus, TickTree integration

### F0 — scope, confirmed live

19859 (`19859crucialcodeauthentic/`): real `.git`, 3 commits, full Android Studio project — full
authority, patterns eligible for the **public** plugin corpus. 32008 (`32008teamcode/`): no `.git`,
4 original files unchanged since Feb 2024, plus a Refract-generated `team-config.yaml` (not source
material) — **internal analysis/corpus-quality use only**, held back from public shipping pending
separate reconfirmation. Write-block hook re-verified live against both directories.

**New standing mining rule:** before mining any directory, check first for Refract's own prior
generated output sitting inside it (grep for `suite_generated_code: true`, known
quickstart-derived file names) — prevents citing Refract's own output back to itself as an
independently-observed team pattern. Mirrored as an operational checklist item in `SOURCES.md`.

### G0 — TickTree repo, confirmed substantive

17 commits, 2 modules (`ticktree-core` 55 files, `ticktree-ftc` 11 files), 8 docs, published JitPack
`v0.1.0`, CI + coverage gate. "pre-alpha — API unstable" per its own README. Proceeded to G1.

### F1 — 19859, full Tier-1-equivalent depth

Feature-vector extraction caught one false positive (a `swerve` signature sourced from Pedro's own
bundled tuning utility, not 19859's code — corrected by reading the real `Drivetrain.java`, which
is definitively mecanum). Evolution analysis across all 3 commits: an early 862-line
naming/strategy consolidation, then a real feature commit (Pinpoint CRC detection + PD heading-lock).

**11 candidates extracted, provenance-collapsed to 9 lineages** (C+D+E collapse into one shooter
empirical-fit lineage; F+G share a lineage but stay separable). Shared-ancestry, not
19859-original: B (textbook mecanum FOC+PD), H (standard FTCLib+Pedro integration idiom — also
flagged a broken singleton bug in `getInstance()`), K (ubiquitous auto→teleop static handoff idiom).

7 open questions were sent to the actual author and answered (2026-07-16) rather than inferred —
genuinely unresolved items (two coexisting heading-lock implementations, an unused static pose
handoff, an abandoned thread-pool) recorded as such, not guessed at. **Status: formalized and
merged**, `references/patterns/19859.yaml`, 10 final entries.

**F3 — walked all 4 existing cross-team findings against 19859 individually:**
`shooter-empirical-vs-physics` substantively updated (19859 = 7th empirical leg, a shared
cubic-polynomial evaluator — reinforces the same tier, doesn't escalate it).
`moving-shot-compensation` updated but deliberately not inflated (19859-F kept `is_member: false`
with an explicit fielded-status caveat, since its fielded status is genuinely unresolved).
`orchestration-nonblocking` and `sensing-modality`: checked, no genuine new leg (19859 uses FTCLib's
stock scheduler, not a hand-rolled mechanism; has no game-piece sensing at all).

**F2 — 19859 promoted to the real eval-fixture stand-in.** First pass (static extraction) was
explicitly not eligible; second pass ran `ftc-team-config` live against the user, surfacing two
things the earlier static pass missed entirely: a real gate mechanism (`LEFT_GATE`/`RIGHT_GATE`
servos) and resolution of the AutoAimSubsystem question (confirmed real by the user). Result:
`19859-real-confirmed.yaml`, `validate_config.py` returns fully valid — completing §20's
three-plus-one regression set for the first time.

**F4 — `stale_pid` validation: honestly inconclusive.** 19859's 3-commit history introduced its
only PID constants fresh alongside the hardware they tune — no temporal gap exists to detect. The
heuristic remains unvalidated, not forced further.

### F1 — 32008, lighter no-provenance treatment

3 low-novelty candidates (deadzone, dpad step-adjust, mecanum mixing), all tagged
`public_shippable: false`. **7 real bugs found and reported separately from patterns**, including:
an NPE-guaranteed unassigned hardware field, a `Math.abs(x)<0` no-op that leaves the shooter
flywheel permanently at 0 power, a non-compiling SDK constant typo (`RUN_USING_ENCODERS` vs. the
real `RUN_USING_ENCODER`), and a copy-paste dpad step-size mismatch (0.01 vs 50.0 on the same
servo field). A metadata inconsistency was flagged (Refract's own earlier-generated
`team-config.yaml` says `veteran`, contradicting the code's own rookie/teaching-tier style) —
recorded for whoever owns corpus metadata next, not resolved here. **Status: formalized**,
`references/patterns/32008.yaml`, 3 entries, all internal-only.

### G1 — TickTree, learned from source

Read the architectural spine directly. Confirmed: `BehaviorTree` is a deliberate "dumb driver"
seam; `AbstractNode` centralizes lifecycle specifically to prevent cross-tick state leaks;
`OpModeTreeRunner` is composition-only by design (no base class to extend); `CommandAction` leaves
are RUNNING/SUCCESS only (no native failure signal — must be expressed via
`Timeout`/`Guard`/`Condition`) and self-discloses no subsystem mutual-exclusion between
`CommandScheduler` and TickTree. Docs matched code precisely on everything checked. **6 Refract-side
integration rules recorded** for `ftc-construct` generation (never extend `OpModeTreeRunner`;
explicit `loop()`/`stop()` wiring for iterative OpModes; never assume a Command leaf can signal
FAILURE; never mix scheduling paradigms on one subsystem; get memory-vs-reactive composite choice
right by construction; check the `compileOnly` FTCLib/SolversLib dependency gotcha). **Zero
TickTree-side defects found this pass** — an honest result, not a placeholder (bounded reading: the
spine + 2/11 bridge files + 1/8 docs files).

### G5 — TickTree docs, staleness-instrumented

8 files fetched, headers stamped with the real commit (`998011a`), not the stale `v0.1.0` tag.
`corpus-input-scan.py` extended with a genuinely different **commit-tracked** (not release-tracked)
staleness check for this one library, since TickTree's single release predates its current docs —
explicitly marked in-code as temporary, to be deleted once TickTree's release practice stabilizes.

### G2/G3 — recognition + real config option

`extract_feature_vector.py` given TickTree's real import signature so mining doesn't misattribute
its orchestration to a team's own work (verified against both a real negative case and a synthetic
positive case). `core-feature-model.yaml`'s `software_stack.behavior_layer: [ticktree, none]` axis
added as optional-detected (not mandatory-ask, matching the `sensing.*` convention) — TickTree
composes with whichever pathing/command choice a team already made, confirmed from source in G1.
`ftc-construct` grounds generation against it, carrying forward both hard API constraints from G1.

**Status: G2/G3/G5 done, G4 (the bidirectional feedback mechanism) implicit** in this document's
own Refract-side/TickTree-side split — no dedicated `TICKTREE-FEEDBACK.md` existed yet at the time
this section was written, since G1 found 0 TickTree-side defects. (It exists now — see the
standalone `TICKTREE-FEEDBACK.md`, first populated in Phase I.)

---

## Proposal: a "port and adapt existing code" mode for `ftc-construct`

**Status: proposal, not built.** Both real invocations of `ftc-construct` during a live tuning
session were, in substance, "take our own already-working code and adapt it" — not "scaffold from
the interface template." The team said so explicitly and repeatedly. The skill's core (interface
derivation, template adaptation) went entirely unused both times; only the tail (config gate,
linters, rule-check, tuning verify) delivered value. **One session is not a trend** — treated
honestly as "this may be the common case," not "this is the common case."

**The real design difficulty:** template mode can check its output against a known-good structure;
port mode has no such reference. What still applies unchanged: `validate_config.py`,
`emit_tuning.py verify` (more valuable here, not less — porting is exactly when constants get
quietly altered), `failure_mode_lint.py`, the rules/freshness gates. What doesn't apply and must
not be faked: interface derivation from `season_mechanisms`, template-conventions adaptation.
**Missing entirely — the actual proposal:** a port-fidelity obligation, roughly in order of value:
(1) a constant-preservation diff (every source literal must appear unchanged or be on an explicit
change list — cheap, deterministic, catches the most likely porting error); (2) a control-flow
shape check (states/transitions/guards survive 1:1 unless a change was requested); (3) an explicit
change manifest the port declares up front.

A later, fuller retrospective of the same engagement (Phase J) supplied a concrete number for the
"deviations should be rare and self-documenting" norm — 2 marked deviations across an entire ported
subsystem — but is explicitly **elaboration of the same one data point**, not a second engagement.

**Three options considered — A (build port mode now), B (fix the wording, no new mechanism), C
(gather evidence, revisit later). Recommendation: B now, A when a second independent engagement
shows the same shape.** B is honest, immediate, and removes the real mismatch the team hit. A is
the right eventual end state but the verification family it needs is substantial enough that
building it against one observation risks designing for the wrong case. Explicitly not proposed:
loosening any existing gate, or auto-detecting which mode applies (that stays a question for the
team).
