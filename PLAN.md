# FTC Claude Code Skill Suite — Final Plan

## 1. Overview and approach

This is a suite of Claude Code Agent Skills that gives Claude Code deep, reliable FTC robotics competence: citation-grounded rules compliance, structured hardware knowledge, code architecture patterns distilled from elite teams' repos, and a build process that carries forward season to season without a rewrite.

It is deliberately **not** a website/platform, **not** a fine-tuned model, and **not** a custom agent harness. Each of those was considered and rejected for concrete reasons worth keeping on record:

- **Not a website/platform.** Claude Code already has codebase-wide file access (Glob/Grep/Read) and bash execution — the two things a custom platform would otherwise need a vector database, an ingestion backend, hosting, and multi-tenancy to provide. Nobody besides you and your team needs to use this without also having Claude Code, so a website's one real advantage — serving users who don't have the tool — doesn't apply here. If that ever changes (other teams wanting a login-and-use product), that's a different, larger project, not an extension of this one.
- **Not a full agent-harness clone (a "Codex-style" build).** That means rebuilding sandboxed execution, a permission system, and context management — years of engineering Anthropic already maintains and gives away for free through Claude Code. Justified only if the goal were "build an agent harness" as its own project, which it isn't.
- **Not fine-tuning.** The rules corpus changes weekly in-season (Team Updates) and the game itself changes completely every year. Fine-tuning is a poor fit for reliable factual recall in a fast-changing domain, and you'd be re-tuning constantly just to stay current. Retrieval-grounded generation with citation-forcing stays current automatically and — critically — is checkable, since every claim can be traced back to a specific chunk of a specific document.
- **No vector database.** With 1M-token context windows now standard on frontier Claude models, and Claude Code's native Glob/Grep/Read already providing exact-match and structural search over an entire reference tree, embeddings and a vector index add complexity without adding capability at this scale. The entire "retrieval layer" is: well-organized reference files, plus Claude Code reading the relevant one directly.

---

## 2. Skill suite structure

Seven skills, each a directory with `SKILL.md` (required: `name` + `description` frontmatter, preloaded into context; body loaded on trigger) plus `references/`, `scripts/`, and `evals/` as needed. Keep each `SKILL.md` body under roughly 500 lines — split overflow into `references/` — and keep descriptions sharply differentiated from each other so Claude Code's routing doesn't collide between skills that sound similar.

```
.claude/skills/
  ftc-team-config/        # elicitation entry point for a build session (Session 2)
  ftc-rule-check/          # citation-grounded rules Q&A
  ftc-hardware-lookup/     # structured hardware spec lookup + deterministic math
  ftc-code-review/         # pattern-aware, config-aware code review
  ftc-quickstart-builder/  # builds/maintains the opinionated starter template
  ftc-corpus-builder/      # Session 1: elite-code distillation into the pattern library
  ftc-season-transition/   # detects and runs the season-boundary protocol

.claude/agents/            # subagent definitions carrying model/effort routing (§5)
  pattern-extractor.md
  provenance-checker.md
  bulk-tagger.md
  full-review.md
```

---

## 3. Core feature model (season-invariant)

`core-feature-model.yaml` — written once, touched again only if the underlying FTC hardware/software ecosystem itself changes (e.g., the eventual SystemCore/MotionCore transition), never because a new game was announced.

```yaml
drivetrain:
  type: [mecanum, swerve, tank_differential, other_holonomic]
  mecanum:
    wheel_source: [goBILDA_stock, custom]
    wheel_diameter_mm: number
    wheel_durometer: optional   # affects tuning assumptions, not code structure
  swerve:
    module_count: [3, 4]
    module_source: [off_shelf, custom_fabricated]

control_hardware:
  hub_generation: [REV_Control_Hub, SystemCore_MotionCore]
  # SystemCore/MotionCore/the A301 smart actuator are not FTC-legal until the 2027-28 season,
  # with a hybrid-legal transition period through at least 2030-31. This axis exists now
  # specifically so the schema doesn't need restructuring when that transition arrives.
  expansion_hub_count: [0, 1, 2+]

sensing:
  vision: [limelight_3a, webcam_easyopencv, none]
  odometry: [dead_wheels, goBILDA_pinpoint, otos, none]

software_stack:
  pathing: [pedro_pathing, roadrunner, custom, none]
  opmode_style: [ftclib_command_based, raw_linear_opmode]

fabrication:
  capability: [stock_gobilda_rev, 3d_printed_custom, cnc_aluminum_or_carbon]
  # affects tuning parameters (acceleration limits, PID gains) — never gates which code
  # gets recommended, only which tuning values get advised. Keep this boundary sharp.

team_context:
  experience: [rookie, veteran]
  # affects explanation depth only, never gates a recommendation
```

This is modeled as a **feature model** in the formal sense (Feature-Oriented Domain Analysis, Kang et al., 1990 — the origin of software product-line variability modeling), with mandatory/optional/alternative axes and cross-axis constraints, the same discipline used to manage a family of related software systems, applied here to a family of related robots. Modern tooling and successors worth knowing about if this ever needs more rigor than a hand-written YAML file: **FeatureIDE** (the standard open-source feature-modeling tool), Czarnecki's cardinality-based feature models, and Benavides et al.'s survey on automated feature-model analysis.

---

## 4. Season extension (current: DECODE)

`season-extensions/decode-2025-26.yaml` — this is the file that gets replaced by the Season Transition Protocol (§19) when the game changes. Everything else in this plan is unaffected by that replacement.

```yaml
season: DECODE presented by RTX (2025-2026)
rules_current_through: Team Update 32 (Apr 2026)   # re-verify against the live manual — don't trust a stale TU number

season_mechanisms:
  intake: [roller, claw, other]
  shooter: [flywheel, elastic_catapult, none]
  turret: [none, single_axis, multi_axis]         # requires shooter != none
  gate_mechanism: [present, none]
  classifier_interaction: [present, none]
  endgame_parking: [mandatory]

known_archetypes:
  - turreted_shooter          # turret decouples aim from drivetrain heading, enables shoot-while-moving
  - fixed_shooter_on_swerve   # the drivetrain itself provides aim

constraints_on_core:
  # A season concept constraining a core axis: the fixed-shooter archetype only
  # makes sense on a swerve drivetrain (the drivetrain itself provides aim).
  # Gives §11's constraint-checker and §20's evals a real entry to fire against.
  - archetype: fixed_shooter_on_swerve
    requires:
      core.drivetrain.type: swerve
```
**Formalized (Session 1, Phase 2, Flag C).** The block above is no longer illustrative-empty — it is the actual live entry in `season-extensions/decode-2025-26.yaml`, keeping this example in sync with the real file.

---

## 5. Model and effort routing

Claude Code runs one model per interactive session, but subagents (`.claude/agents/*.md`, each with its own `model:` frontmatter field) route specific sub-tasks to a different tier automatically when a skill invokes them — that's the real mechanism behind this table, configured once per task type rather than chosen manually each time.

One thing worth being precise about: the "effort" dial isn't uniform across models. **Haiku models don't expose an effort parameter at all** — Haiku's cost/speed profile is the entire lever, there's no separate depth control layered on top. **Sonnet 5 runs adaptive thinking by default**, scaling its own reasoning depth automatically based on the task; manual overrides aren't available. **Opus 4.8 is the one model in this table where a manual effort dial (`low`/`medium`/`high`/`xhigh`/`max`) genuinely applies**, and `xhigh` is the right choice for the highest-stakes steps below.

| Task | Model | Effort | Why this tier |
|---|---|---|---|
| Interviewing you about corpus sources, scope, edge cases (Session 1 start) | Sonnet 5, main session | adaptive | open-ended interview judgment |
| Repo clone + static feature-vector extraction | script, no LLM | n/a | mechanical; never let a model guess what a deterministic parse can answer |
| Candidate pattern extraction from elite code | Sonnet 5 subagent (`pattern-extractor`) | adaptive | real code comprehension and judgment |
| Provenance / convergence analysis | Opus 4.8 subagent (`provenance-checker`) | **xhigh, manually set** | the highest-leverage reasoning step in the pipeline — get this wrong and the whole confidence system is corrupted |
| Chunking/tagging the rules manual + Team Updates | Haiku 4.5 subagent (`bulk-tagger`) | n/a | cheap, mechanical, well within 200K context per document |
| Human review checkpoint before merge | you | n/a | irreplaceable |
| Team-config elicitation (Session 2 start) | Sonnet 5, main session | adaptive | adaptive follow-ups within a bounded scope |
| Inference pass over provided repo/CAD/BOM before asking anything | Haiku 4.5 first, escalate to Sonnet 5 if ambiguous | n/a → adaptive | cheap first pass, pay for reasoning only when needed |
| Rule-legality verdict with citations | Sonnet 5, main session | adaptive | high-stakes, citation-forced |
| Hardware spec lookup | script, no LLM | n/a | eliminates the highest hallucination-risk category by construction |
| OpMode/subsystem code generation | Sonnet 5; escalate to Opus 4.8 subagent for novel architecture decisions | adaptive (**xhigh manually set** on Opus escalation) | reliability matters most here — this ships to the robot |
| Rule-based anti-pattern lint | script, no LLM | n/a | deterministic checks stay deterministic |
| LLM-judgment structural-smell pass | Sonnet 5 subagent | adaptive | heuristic by nature, don't over-invest |
| Verification pass on generated claims | Haiku 4.5 first, escalate to Sonnet 5 on mismatch | n/a → adaptive | two-tier check, most claims pass the cheap pass |
| Full pre-competition codebase review | Opus 4.8 subagent (`full-review`), run via `context: fork` + `agent: Explore` | **xhigh, manually set** | highest stakes, whole-codebase, isolated so it doesn't pollute the working session |
| Season Transition: mechanism-taxonomy draft | Sonnet 5, main session | adaptive | open-ended extraction from a brand-new document |
| Season Transition: quantitative strategy modeling | Opus 4.8 subagent | **xhigh, manually set** | genuine quantitative reasoning under uncertainty |
| Routine interactive Q&A during a build session | Sonnet 5, main session default | adaptive | right balance for ordinary back-and-forth |

Confirm the exact current effort/thinking parameter surface against live Claude Code docs when wiring subagent configs — this specific parameter space moves fast; the routing logic in this table is the stable part.

**Correction (Session 1 — verified against live docs, [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents), tier-1).** The subagent-frontmatter field surface as actually shipped: `name, description, tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory, background, effort, isolation, color, initialPrompt`. Consequences for this table:
- `effort` IS a real field — values `low, medium, high, xhigh, max`, "available levels depend on the model." This validates the `xhigh` calls above and confirms the effort dial is Opus-only in practice: only the two Opus agents (`provenance-checker`, `full-review`) carry `effort: xhigh`; the Sonnet and Haiku agents carry no `effort` field (adaptive / none), exactly as the table's prose says.
- `model` accepts `sonnet | opus | haiku | fable | <full-id> | inherit`. The agent files use **pinned full model IDs** — `claude-sonnet-5` (pattern-extractor), `claude-opus-4-8` (provenance-checker, full-review), `claude-haiku-4-5-20251001` (bulk-tagger) — not tier aliases, so an unannounced model change is a flagged edit rather than silently absorbed drift, consistent with how every other layer of this plan treats drift.
- **There is no `context` or `agent` frontmatter field.** The `full-review` row's "`context: fork` + `agent: Explore`" is not literal syntax. Context isolation is *inherent* — every subagent runs in its own context window (that is what keeps the full review from polluting the working session). The "Explore" behavior is reproduced by a **read-only `tools` allowlist** (Read/Grep/Glob/Bash, no Edit/Write). `isolation: worktree` exists but is for agents that mutate files in parallel, so it is deliberately NOT used for a read-only review.

---

## 6. Architecture layer allocation

Four layers, each doing what it's actually good at — don't force everything into `SKILL.md`:

- **Skills** — domain reference (rules, hardware, patterns) and the elicitation logic itself.
- **Scripts** — anything deterministic: gear-ratio math, rule-based linting, feature-vector extraction, constraint checking. If a script can answer it, a model never guesses at it.
- **Subagents** — implement the §5 routing table; also isolate the full-codebase review so it doesn't consume the main session's context.
- **MCP servers** — live data instead of static snapshots: a Team Update feed, FTCScout's documented API for OPR/ranking lookups, the goBILDA catalog via the existing open-source STEP-file scraper (don't rebuild one).
- **Hooks** — deterministic enforcement, e.g., a `PreToolUse` hook matching `git commit` invocations through the Bash tool to block a commit that references a config field that was never confirmed (confirm the exact current hook-event name against Claude Code docs at build time).

---

## 7. Knowledge ingestion — what populates each skill's `references/`

| Source | Feeds | Where |
|---|---|---|
| Competition Manual Part 1 (General/Admin) | `ftc-rule-check` | ftc-resources.firstinspires.org |
| Competition Manual Part 2 (season-specific) | `ftc-rule-check` | same |
| Robot Inspection Checklist | `ftc-rule-check` | firstinspires.org |
| Team Update history, diffed and dated | `ftc-rule-check`, live via MCP | ftc-resources.firstinspires.org/ftc/game/tu-latest |
| FTC Q&A archive, tagged clarification-tier not rule-tier | `ftc-rule-check` | FTC-Events Q&A (Lead Coach login) |
| REV Robotics catalog + datasheets | `ftc-hardware-lookup` | revrobotics.com |
| goBILDA catalog (via existing open-source scraper) | `ftc-hardware-lookup` | gobilda.com |
| FtcRobotController SDK source | `ftc-quickstart-builder`, `ftc-code-review` | github.com/FIRST-Tech-Challenge/FtcRobotController |
| Pedro Pathing docs + source | `ftc-quickstart-builder`, `ftc-code-review` | pedropathing.com, GitHub |
| RoadRunner docs + source (legacy support) | same | GitHub |
| FTCLib docs + source | same | GitHub |
| FTC Dashboard | same | GitHub |
| EasyOpenCV | same | GitHub |
| Limelight FTC docs | same | limelightvision.io |
| Curated public team repos, attributed | `ftc-corpus-builder` | GitHub, findable public repos — not repos that don't publish code |
| FTCScout OPR/ranking data | `ftc-season-transition`, strategy modeling | FTCScout's documented GraphQL/REST API |

---

## 8. Rules reasoning architecture

Retrieving the right rule text is necessary but not sufficient — "is X legal" questions require reasoning about how rules interact, which is the actual hard part:

1. During ingestion, extract cross-references between rules (rules cite each other, e.g., "see R201") via regex plus LLM-assisted parsing, stored as edges in a `rule_references` table or file.
2. On a legality question, retrieve the directly relevant chunk(s) **and** traverse one hop of cross-references, feeding all of it as context.
3. Force structured output: `{"verdict": "legal | illegal | ambiguous", "citations": ["R301", "R305"], "reasoning": "..."}`. This doesn't eliminate hallucination, but makes it checkable — every cited rule number can be programmatically verified to exist and to say what the reasoning claims.
4. Tag Q&A-sourced content as clarification-tier, distinct from rule-tier, since the manual itself states Q&A doesn't supersede the text.
5. When retrieval confidence is low or the Q&A shows genuine unresolved disagreement, the answer is "ambiguous — worth filing a Q&A," not a confidently wrong verdict.
6. **Embedded tables are structured data referenced by pointer, never rule prose (§8↔§9 cross-reference mechanism).** Many rules embed tables of legal parts/specs (motors → R501/Table 12‑1, batteries → R601/Table 12‑4, wire gauges → R615/Table 12‑8). A table is *never* duplicated into or paraphrased inside the rule chunk. Each manual table is extracted once into a §9‑owned structured file keyed by its manual table ID; the citing rule chunk holds only a pointer to that ID. A legality question that turns on a table resolves the pointer into the deterministic §9 hardware data — so the spec the verdict depends on comes from the structured layer, not from prose an LLM could mangle. Mechanically this is the same one‑hop traversal as a rule→rule cross‑reference (step 2), but crossing the §8→§9 boundary, and it is enforced at ingestion: a table found inside a rule is split out into §9, not tagged as rule text. (Added Session 1, Phase 5, after the §12.6 sample showed table contents being paraphrased into rule prose.)

---

## 9. Hardware knowledge architecture

Hardware questions are lookup and arithmetic problems, not semantic-search problems, and this is the single highest hallucination-risk area in the whole system if modeled wrong — a system answering "what's the max RPM of a goBILDA 5203 series motor at a 19.2:1 ratio" via semantic search over scraped prose will confidently invent a number.

- REV and goBILDA catalogs live as **structured tables** (JSON/CSV: part number, dimensions, electrical specs, mechanical compatibility), not embedded prose.
- CAD (goBILDA publishes STEP files) is treated as a link/reference field, not ingestible text content.
- A deterministic script (`scripts/motor_math.py` or similar) does gear-ratio, torque, and speed arithmetic from the structured spec table — the model reads the script's output, it never generates the number itself.
- **Tables embedded inside Competition Manual rules** (legal-motor, battery, wire-gauge, power-regulation tables, etc.) are ingested here as well, as structured files keyed by their manual table ID, and are referenced from the citing rule chunk by pointer only — the §8↔§9 cross-reference mechanism (§8 step 6). A manual table is never stored as prose inside a rule chunk.

---

## 10. Config-driven code generation architecture

The mechanism that makes "every line of generated code relevant" actually true rather than aspirational: `Drivetrain`, `Shooter`, `Turret`, and `Intake` are interfaces, not concrete classes. A `RobotConfig` object — generated directly from the confirmed feature-model instance (§3 + §4, filled per team) — selects which implementation gets instantiated (`DrivetrainMecanumGoBilda` vs. `DrivetrainSwerveCustom`, standard Strategy pattern). Code for a feature a team didn't declare is either never generated into their fork, or, if kept as a shared reference implementation elsewhere in the corpus, is clearly isolated and flagged by the linter as "not referenced by current config, confirm if stale" rather than sitting silently as dead weight.

**Correction (Session 1 — dynamic interface generation).** Do not treat `Drivetrain, Shooter, Turret, Intake` as a fixed interface list. **`Drivetrain` is the one always-core-fixed interface.** Every other mechanism interface is generated **dynamically — one interface per key present in the active season extension's `season_mechanisms` block** (`season-extensions/<active>.yaml`, resolved through `season-extensions/ACTIVE`). No hardcoded mechanism list, and no schema restructuring when a season adds or removes a mechanism category — the interface set is *derived*, not enumerated. This is the agreed resolution of the core-vs-season boundary raised in Phase 2: mechanisms stay 100% in the season layer (including `intake`, with no special-casing), core carries only the perennial `Drivetrain` interface, and no `extension_point` indirection is added to the YAML — the "extension point" is the generation logic reading `season_mechanisms`, not a new nested field.

---

## 11. Hallucination control stack

1. **Retrieval grounding** — no hardware/rule claim without a citation to a chunk actually read this turn. Standard RAG-grounding principle (Lewis et al., 2020).
2. **Chain-of-Verification** (Dhuliawala et al., *Findings of the ACL 2024*) — a verification-question pass on generated claims, checked independently against the source before finalizing.
3. **Semantic-entropy hallucination detection** (Farquhar, Kossen, Kuhn & Gal, *Nature*, 2024) — where feasible, treat high-variance answers across resampled generations as a flag for the same abstention behavior as low retrieval confidence.
4. **Calibrated abstention** (Kadavath et al., 2022) — no support found, no answer given, not a filled gap. "Unknown — need the BOM/CAD entry for X" is a valid, expected output.
5. **Deterministic computation for anything numeric** — gear ratios, torque/speed, kinematics — always scripted, never generated. This eliminates the failure mode rather than mitigating it.
6. **Structured, citation-required output** on every recommendation, tying it to the confirmed config feature(s) and source pattern/rule that triggered it.
7. **Feature-model constraint checking** — a deterministic script mechanically rejects any generated code that references a feature the confirmed config doesn't declare.
8. **Multi-source verification (Rule 7)** — no claim that isn't settled, official, and stable is trusted on a single source. Official FIRST/WPILib documentation and source code are **tier-1**; alpha-tester reports, community forum posts, and third-party summaries are **tier-2** — usable, but any claim resting only on tier-2 is *labeled as such*, never presented with tier-1 confidence. A single source, tier-1 or not, is insufficient for anything forward-looking or still-evolving: cross-check against at least one independent source before relying on it. Standing requirement for the whole project, most load-bearing exactly where §22 already flags reliability as thin — hardware specs, and hardware-*generation* specs for a system still in alpha (SystemCore/MotionCore/A301).

The Season Transition Protocol (§19) reuses this exact stack for ingesting a brand-new manual rather than running a separate, less-rigorous path — first-pass extraction from an unfamiliar document is exactly where this matters most, not least.

---

## 12. Provenance-aware confidence weighting

FTC teams heavily share ancestry — a common quickstart, Game Manual 0, or one influential repo can make several teams' code agree without several independent inventions. Raw vote-counting across teams is therefore invalid as a confidence signal on its own:

- Every pattern's provenance is traced during corpus construction (§14), not assumed. "Present in N teams" only counts as evidence of quality if those N teams arrived at it independently — shared lineage collapses to a single source for confidence purposes, however many repos display it.
- Weight by **diversity of reasoning**, not count of repos: two teams solving the same problem via visibly different approaches that converge is real evidence; two teams with near-identical code tracing to the same quickstart is one data point wearing two coats.
- Treat quickstart-derived code — including this system's own Session 2 output, once it starts getting reused — as a single lineage going forward, so the corpus never ends up citing itself as independent confirmation of its own recommendations.
- A pattern seen in a single team's repo with no independent replication is still legitimate to keep, tagged `confidence: single-source` rather than silently promoted to something stronger.
- **Shared-library import gating (standing detection rule).** Before provenance classification runs on any candidate whose apparent novelty is an *orchestration / command / scheduling* framework, an explicit **library-import check must gate it** — the same way an FTCLib/SolversLib import check already distinguishes independent reimplementations from adopted-library code elsewhere in this pipeline. The specific trigger that forced this into the plan: **Pedro Pathing now ships `com.pedropathing.ivy`**, a command framework (`Command`/`ICommand`/`groups.Sequential`, `.then()`/`.with()`). A run of Pedro-based teams that each adopt `ivy` would *false-converge* into looking like an independent second orchestration finding — surfaced concretely in Session 1, Phase 4 on team 12808 (its `StateMachine`/`channel` pub-sub are team layers **on top of** ivy, not own invention → `shared-ancestry`, not a leg). Rule: **any Pedro-based orchestration candidate requires an explicit `com.pedropathing.ivy` import check before it can be classified `independently-derived`.** Generalize the gate to any future shared orchestration substrate (a new quickstart command lib, etc.) — the detection is "does the candidate's command substrate come from a shared dependency?", checked deterministically by import, not inferred from surface shape. (Contrast held as the canonical example: 24089's `lioncore/tasks/` passes the same check — no such import — and remains a genuine candidate leg. Same surface shape, opposite provenance; only the import check separates them.) Added Session 1, Phase 4.

---

## 13. Elicitation methodology

A question earns a place in the flow only if answering it changes which reference patterns or recommendations apply — nonzero information gain regarding the applicable-pattern set. This is grounded in **Bayesian experimental design / mutual-information item selection**, the same principle behind Computerized Adaptive Testing (Chang & Ying, 1996: sequential item selection by mutual-information/KL criteria over a running posterior, shown to reduce bias and error specifically in short or early-stage adaptive tests — exactly the "minimize questions" regime this system operates in). The selection is explicitly **myopic/greedy** — the single best next question isn't guaranteed to produce the best overall question *sequence* — worth knowing as a real limitation, not a guarantee of optimality.

Practically, this becomes a two-pass bootstrap, since exact entropy can't be computed before the pattern corpus exists:

- **Pass 1 (during corpus construction, §14):** as patterns get extracted and tagged with `applicable_when` conditions, the count of how many patterns key off each feature becomes an empirical information-gain proxy. A feature 40 of 60 patterns branch on has real information value; one only 2 patterns reference doesn't.
- **Pass 2 (at runtime, §15):** order elicitation by that empirically-measured branching factor, highest first, refined as a soft ranking over the season rather than fixed once.

**Inference before elicitation** is the second load-bearing mechanism, and it's what resolves the apparent tension between "ask about every aspect" and "every question must have a purpose": before asking the human anything, infer what's recoverable from provided artifacts (repo imports, hardware-map class contents, a BOM, CAD if uploaded) via deterministic grep/parse scripts, never LLM guessing. Only the residual — information that genuinely isn't recoverable from artifacts (physical properties like wheel durometer, or intent/roadmap questions like "are you planning to add a turret later this season") — becomes a direct question. Coverage comes from inspection first, elicitation second; thoroughness and purposefulness stop competing once the cheap, recoverable information is handled by inference and elicitation is reserved for genuinely load-bearing unknowns.

A small set of features gets asked directly regardless of inferability, because they gate too much downstream logic to risk a bad guess: drivetrain topology, the season's mechanism set, and software stack.

---

## 14. Session 1 — Skill Construction

The meta-level session: not building a robot, building the thing that helps build robots. The elicitation here runs toward you, and needs to be genuinely thorough, because everything downstream inherits whatever gaps exist here.

### 14.1 What gets asked before any code gets touched

Not a static checklist filled once — a real conversation, but these categories all need answers before this session produces anything trustworthy:

- **Data access and scope.** Which repos you actually have rights to use — your own team's full history, teammates' or alliance partners' repos with permission, or only publicly-published ones. Public GitHub is fine to cite; privately shared material needs your explicit confirmation of permission; scraping non-public material is out regardless of season. FIRST's own culture explicitly expects credited use of *shared* code — treating uncredited copying as plagiarism — which is favorable to this project's design as long as attribution is kept, and there is no FTC rule against studying other teams' publicly shared code. The one hard software rule to respect: modifying or omitting compiled libraries in the SDK's `libs/` folder makes a Robot Controller app competition-illegal, so any generated code has to respect SDK integrity, not just game rules.
- **Season depth.** Current season only, or prior seasons mined for architecture patterns that outlive mechanism changes? Architecture patterns live in the core layer (§3) and genuinely do transfer across seasons; mechanism-specific patterns live in the season extension (§4) and mostly don't.
- **Your own team's repo status.** Is it the ground-truth reference config, and does hardware change mid-season in ways that need versioning — a mechanism added in week 6 shouldn't silently overwrite what the corpus says about week 1?
- **Priority order.** Which subsystem category gets distilled first — drivetrain, shooter, turret, vision? Doing all categories simultaneously dilutes review bandwidth.
- **Review bandwidth.** How much time can realistically be committed to reviewing extracted patterns before they're trusted? This sets how conservative the auto-merge threshold needs to be.
- **Ambiguity tolerance.** When a rule interpretation is genuinely unclear, should the skill always flag it and stop, or give a best-guess with a visible caveat? A policy decision, not something to infer.

### 14.2 Construction pipeline

1. **Clone + static feature-vector extraction** (script, not a model) — detect imports, OpMode style, hub/hardware-map declarations, drivetrain kinematics class per repo. Output: one filled feature-model instance per team.
2. **Candidate pattern extraction** (Sonnet 5 subagent, §5) — for each team, propose 5-15 entries in the form `{problem, solution_approach, code_reference, applicable_when, source_team, confidence}`. Reference file-and-line-range, don't duplicate whole snippets into the corpus.
3. **Provenance analysis** (Opus 4.8 subagent, xhigh, §5) — before any confidence score is assigned, trace whether a pattern's cross-team presence reflects independent invention or shared ancestry (§12). Nothing skips this step.
4. **Human review checkpoint** — nothing merges into `references/patterns/` without sign-off. Review bandwidth from §14.1 sets the actual bar here.
5. **Rules/Team Update ingestion** (Haiku 4.5 subagent, §5, for tagging; §18 for the live-feed mechanism rather than a one-time scrape).

Confidence bar, concretely: a pattern doesn't move past "candidate" until (a) provenance analysis has classified it as independently-derived or explicitly flagged as shared-ancestry and weighted accordingly, and (b) the actual code reference has been reviewed, not just the model's summary of it.

---

## 15. Session 2 — Skill Usage

The runtime session: an actual build session, either your own or another team's, where the skills do their real job. The standing instruction baked into every relevant `SKILL.md` is non-negotiable: **when a question would change what code gets generated, ask it — don't guess, and don't wait to be asked to check.** Inference is for pre-filling defaults; it never silently decides what ships. Confirmed config generates code; unconfirmed config generates a question.

### 15.1 Flow

1. **Inference pass** (Haiku 4.5, §5) — read whatever's available (existing repo, BOM, CAD if provided) and pre-fill as much of the feature model as can be determined mechanically.
2. **Gap-driven elicitation** (Sonnet 5, §5) — ask only about what inference couldn't resolve, ordered per §13. The mandatory-regardless-of-inferability set (drivetrain topology, the season's mechanism set, software stack) gets confirmed explicitly even when it looks inferable.
3. **Confirmation before generation** — once config is filled (inferred plus elicited), state it back explicitly before writing any hardware-specific code. No generation step fires against an unconfirmed field.
4. **Build.** These skills are authorized to actually write and edit files using Claude Code's native tools, not just describe what to write — that's the point of running inside Claude Code rather than a chat window. Once config is confirmed, generate/modify the actual OpMode, subsystem, and config classes (per §10's architecture), then explain what was done.
5. **Continuous re-elicitation, not one-shot.** As a build progresses and new mechanisms come up mid-session (a turret added in week 6 that wasn't in the original config), notice the mismatch and re-open that part of the config rather than silently working from a stale snapshot. Treat an unconfirmed assumption as worse than an extra question, every time — this is a persona instruction as much as a technical one, and it's the concrete meaning of "continuously urge, not afraid to ask": *"If a recommendation would differ depending on information you don't have, stop and ask before generating code. A wrong guess that compiles is worse than a question that costs one turn."*

### 15.2 Time-gated elicitation: `control_hardware.hub_generation` (added Session 1, Phase 7)

The `hub_generation` axis is elicited on a **time gate**, not always:

- **Now through the end of the 2026-27 season** — REV Control Hub is the *sole*
  FTC-legal control system, so the axis has **zero information gain** and is **not
  asked** (asking it would violate §13's purposefulness principle).
- **When the hybrid-legal window opens (targeted 2027-28)** — `hub_generation`
  **joins the mandatory-ask set** (alongside drivetrain topology, the season
  mechanism set, and software stack), but is **preceded by a short briefing, not
  asked cold.** The briefing explains: what SystemCore/MotionCore/A301 changes about
  the team's code; that **both systems stay legal for years** (through at least
  2030-31), not a forced cutover; and that a **hybrid REV+SystemCore configuration**
  may be a real option, not just "old or new." Only then does the skill ask which
  platform (or hybrid) the team is on — presenting the choice with real tradeoffs,
  never defaulting silently to either system.

The gate keys off the active season (`season-extensions/ACTIVE`) reaching 2027-28,
not a hardcoded date. Full tier-tagged rationale and sources live in
`ftc-hardware-lookup/references/hub-generations/systemcore-motioncore.md`. This is a
standing behavioral rule, not a one-time research note.

---

## 16. QuickStart repo build

A standalone deliverable within this system: a refactored, opinionated starter template that new or rookie teams actually build from, separate from the elicitation/review skills above.

Start from the official FtcRobotController quickstart (or a Pedro Pathing quickstart, matching whichever is the team's baseline). Refactor toward:

- Interface-based hardware abstraction for every mechanism category in the feature model (`Drivetrain`, `Shooter`, `Turret`, `Intake`), each with a `RobotConfig`-selected implementation (§10).
- The patterns extracted in Session 1 become the actual bodies of the "recommended default" implementations, with alternates present as clearly separate, clearly labeled classes — not commented-out branches inside one god-class.
- FTCLib command-based structure as the default path, with a raw-OpMode fallback for teams not using FTCLib — don't force an opinionated dependency on teams who've already invested elsewhere.
- Vision and odometry as pluggable modules gated by config flags, so a team with no vision system doesn't inherit a `VisionSubsystem` they never call.

This repo's job is to be *generically well-architected*, not to encode one team's specific hardware — the variability handling here is structural (interfaces plus config), which is a different mechanism from Session 2's conversational elicitation, and the two shouldn't be conflated: one solves "how do we build a template that fits many teams," the other solves "how do we build one specific team's actual robot."

---

## 17. Anti-pattern detection

Two-tier, deliberately not fully automated:

- **Rule-based** (script) catches known bad patterns deterministically — blocking calls inside the OpMode loop, hardcoded `Thread.sleep`, missing telemetry. This tier is authoritative.
- **LLM-judgment** (Sonnet 5 subagent, medium reasoning) catches structural smells — God classes, missing subsystem separation. This tier is heuristic, and always shows the flagged code as evidence rather than asserting a verdict outright.

---

## 18. Live data ingestion

- **Team Updates.** The manual isn't static — this season alone had 32 updates, several changing RP thresholds and gate rules. Built as a periodic MCP-fetched diff against the live manual, tagged with effective date, not a single PDF conversion done once at the start of the project.
- **FTCScout.** Use its documented API for OPR/ranking data rather than scraping or asserting stats from memory — this is also how to get a current, verifiable ranking figure for any team rather than repeating something stale.
- **goBILDA catalog.** Reuse the existing open-source scraper that already pulls the STEP-file catalog rather than building a new one.

**A structural constraint worth stating plainly, because it's the actual reason the deliberation step in §19 is mandatory rather than a nice-to-have:** FIRST publishes the manual as PDF/HTML, not as structured data — there's no official machine-readable rules format to parse against. First-pass automated extraction from a brand-new document is not going to be perfectly reliable, especially in the first weeks of a new season before the document's specific numbering and structural conventions are well understood by the ingestion pipeline.

---

## 19. Season Transition Protocol

The mechanism that makes this system genuinely reusable across seasons rather than describing itself as reusable while being built around one game's specifics. Concrete near-term trigger, not a hypothetical: **BIOBUZZ, part of FIRST CANOPY, kicks off September 12, 2026** — roughly ten weeks from now as of this writing. Pre-season material is already public: the scoring element is Pollen (plastic balls, roughly 2.8-3 inches in diameter across different sources, with physical characteristics similar to this season's Artifacts), and ecosystem partners — REV, goBILDA, AndyMark, Studica — have already published preliminary "StarterBot Base" drivetrain-plus-intake designs ahead of full kickoff. That means the protocol below doesn't have to wait entirely for September; steps 1-3 can start now against preview material, with step 4 onward waiting for the full manual.

1. **Detection** — the §18 live-feed layer flags a season-boundary event (a new manual or game name detected).
2. **Full-manual ingestion** — the same pipeline as any rules ingestion: chunk by rule ID, prepend parent-section context before embedding or indexing (contextual retrieval — Anthropic's published technique for improving retrieval accuracy on structured, numbered documents), tag with effective date. No new mechanism required, reuse §8 and §18 directly.
3. **Mechanism-taxonomy extraction, draft only** (Sonnet 5, main session, §5) — propose a draft `season-extensions/<new-slug>.yaml`: scoring elements, mechanisms, zones, endgame conditions, structured the same way `decode-2025-26.yaml`'s `season_mechanisms` block is structured (§4). Explicitly a draft, not a merge.
4. **Quantitative strategy modeling, draft only** (Opus 4.8 subagent, xhigh, §5) — cycle-time and expected-value modeling of the new season's point values and time constraints, using the same class of math as OPR estimation, Bayesian shrinkage, and Monte Carlo simulation — genuinely established FRC/FTC community practice (cycle-time optimization guides and kickoff-week scoring-analysis threads are a standard part of how competitive teams approach a new season), not a novel technique invented for this project. This step produces a **mathematically-grounded, explicitly provisional estimate** of which mechanism archetypes are likely to be time-efficient, derived from the manual's stated point values and time constraints alone — not a proof of optimal strategy. No rigorous optimality proof exists for this class of problem, for this system or anyone else in the FTC community: match strategy is adversarial, incomplete-information, and subject to human execution variance. The honest output here is "here's what the math suggests, given these stated assumptions, revised once real match data exists" — not a settled answer.
5. **Deliberation checkpoint, mandatory.** Present steps 3 and 4 as a structured proposal before anything merges: the extracted mechanism taxonomy, the quantitative reasoning behind candidate efficient archetypes, and — just as important — what's still genuinely ambiguous in the manual. The clarifying questions here are engineering-specific, not a generic approval prompt — e.g., "Pollen's dimensions are close to this season's Artifacts; does the existing intake mechanism category transfer directly, or does the new field geometry likely force a new one?" This is where a mathematically-derived candidate gets checked against context the system doesn't have: regional meta, actual fabrication constraints, anything known from the Game Preview that isn't in the manual yet.
6. **Merge** — only after sign-off does the new `season-extensions/<slug>.yaml` go live. The core feature model (§3) and every other layer (§5, §11, §12) carry forward completely untouched, because none of it was ever season-specific to begin with.

---

## 20. Testing and evals

Three-plus-one synthetic configurations form the standing regression set: the real current config for your own team, a synthetic rookie/stock-goBILDA/no-turret config, and a synthetic veteran/CNC/swerve/turret config. For each, verify:

- No hardware spec appears without a traceable catalog citation.
- No recommended pattern violates the config's declared features (§11's constraint check should fire and be observed firing).
- Every rule citation resolves to a real, current rule number.
- The system abstains rather than guesses when information it would need is deliberately withheld.
- The provenance/confidence system correctly downgrades a pattern seeded with a known shared-ancestry case (e.g., two synthetic "teams" both derived from the same quickstart) rather than treating it as independently confirmed.
- The "confirm before generate" rule actually blocks code generation when a mandatory field is left ambiguous in a test transcript.
- Live Team Update ingestion correctly surfaces a rule change dated after the base manual.

Each Season Transition Protocol run (§19) needs its own eval refresh — synthetic configs rebuilt against the new season extension before a build session is trusted with the new season, not carried over from the prior season's test cases.

---

## 21. Order of operations

1. Draft `core-feature-model.yaml` (§3) — the one-time investment.
2. Have the Session 1 conversation (§14.1) — don't skip straight to running the pipeline.
3. Run the construction pipeline (§14.2) through the human review checkpoint.
4. Stand up the MCP/live-data layer (§18), including season-boundary detection.
5. Assemble the skill suite (§2) with the §5 routing wired into subagent definitions.
6. Build the QuickStart repo (§16), informed by the patterns from step 3.
7. Run the evals (§20).
8. Dogfood on your own team in a real Session 2 build session (§15), watching specifically for whether it asks when it should and builds when confirmed — iterate on the persona instruction in §15.1 if it's either too quiet or too chatty.
9. **Recurring, not one-time:** when §18 detects a season boundary, run the Season Transition Protocol (§19) before treating the new season's corpus as trustworthy. First real occurrence: BIOBUZZ, September 12, 2026.

---

## 22. Risks and known limitations

- **Hardware spec hallucination** is the sharpest edge case in the system — get the structured-data modeling in §9 right before trusting any hardware answer.
- **Rule cross-reference extraction** (§8, regex plus LLM-assisted) needs manual QA on a sample before it's trusted — LLM-assisted parsing of legal-style cross-references isn't perfectly reliable at extraction time either. A useful, reusable QA technique proven on the §12.6 sample: run the deterministic regex edge-extraction and the LLM (`bulk-tagger`) pass over the same section and diff the edge sets — exact agreement confirms *extraction fidelity to the source text*. This is explicitly a fidelity check, **not** Rule-7 independent corroboration: both methods read the same document, so agreement says nothing about whether the source itself is current. The citation-staleness risk Rule 7 targets (a cross-reference invalidated by a later Team Update) is caught by §18's live feed, not by extraction-method agreement.
- **The strategic/meta layer has no shortcut** — it's curation work, not a scraping pipeline. Budget real time for it, especially during the deliberation step of a season transition.
- **First-pass extraction from a brand-new manual will contain errors** — this is structural (no machine-readable format exists to parse against, §18), not a implementation bug to eventually eliminate, which is exactly why the Season Transition Protocol's deliberation step is mandatory rather than optional.
- **The quantitative strategy modeling in §19 is an estimate, explicitly not a proof** — treat any kickoff-week "efficient archetype" conclusion as provisional and revise it once real scouting data exists, the same way any team's own kickoff-week strategy session would.
