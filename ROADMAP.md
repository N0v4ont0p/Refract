# Refract Expansion Roadmap

Five workstreams now, sequenced by actual dependency rather than the order they came in.

**Sequencing:** Phase A (done) → Phase B (verification + closure pass, in progress) → Phase C (genuinely different kind of work, separate session recommended) → Phase D (final hardening + documentation, done right before the website so it reflects Phase C's expanded compatibility) → Phase E (website, explicitly separate per your instruction, independent of A-D's timing, whenever you're ready).

---

## Phase A — Construction Skill + Grounded Library Documentation

### A1. Fetch broadly and store in house — no diagnosis step, moving straight to building

Per your call: skip investigating why the earlier fetch failed. Target list, fetch what's reachable now: Pedro Pathing (docs + repo), FTCLib (docs + repo), RoadRunner (docs + repo, legacy support), REV Robotics (Control Hub/Expansion Hub/SDK guides), Limelight FTC docs, goBILDA (build guides beyond the existing parts catalog), the official FTC SDK docs, EasyOpenCV, FTC Dashboard, and the FTCLib-Quickstart repo itself.

Two things kept anyway because they cost nothing extra and prevent real harm later, not a reintroduction of the tiered gate you waved off: each stored file gets a one-line header (source URL + fetch date) — free bookkeeping now, the only thing that makes it possible to ever check staleness later without redoing this from scratch. And storage follows the same domain-split pattern already proven to work (`hub-generations`' separate rev/systemcore files) — one file per library, per major topic, not one giant undifferentiated blob, so loading stays cheap per-query. Report what was actually reachable versus not — don't silently skip something that failed, just note it plainly and move on.

### A3. The new skill — construction, not configuration

Worth actually validating "this needs to be separate," not just accepting it: `ftc-team-config`'s job is config establishment and the confirm-before-generate gate — a contained, single-purpose responsibility by design. "Check the repo, clone a template if needed, scaffold structure, then generate code grounded across the corpus, hardware specs, rules, and library docs simultaneously" is a materially larger job. Keeping it separate respects the same single-responsibility principle that kept the original four skills apart — this is the right call, not scope creep.

Relationship to what already exists:
- **`ftc-team-config` still owns the gate.** The new skill reads a *confirmed* config, it doesn't re-elicit one — pointer dependency, not duplicated logic, same pattern as everything else.
- **This is where the long-deferred `ftc-quickstart-builder` (§16, never built) finally gets built** — not as a parallel, redundant effort, but as this skill's actual scaffolding source. The quickstart builder's job (maintain the reusable, interface-based template repo) and this skill's job (materialize one team's real project from a confirmed config) are related but distinct: the new skill *consumes* the quickstart template's `Drivetrain`/`Shooter`/`Turret`/`Intake` abstraction pattern rather than reinventing structure from scratch each time.
- **Concrete behavior, per your spec:** check whether a proper interface-based template already exists first. If yes, use it. If no, don't clone anything automatically — ask explicitly whether to fetch `FTCLib/FTCLib-Quickstart` and build the template from it. Same ask-don't-guess rule as every other skill, applied to template scaffolding specifically.
- **BIOBUZZ note, recorded now, acted on later:** a season transition isn't only a `season_mechanisms` update — the template and the bundled library docs (Pedro especially) may themselves need revision around a new season's release cycle. This gets written into the standing design now as a linkage, not built — the actual Season Transition skill (R66) stays deferred, this just makes sure the connection isn't lost before that skill eventually gets built.

### A4. Same discipline as every prior skill, applied again

New requirement IDs extracted into the matrix. A real boundary-query test against the existing four — specifically the "who generates code" ambiguity this whole expansion started from: does "write me an OpMode" now route cleanly, or does it collide with `ftc-team-config`? The new skill should check for a confirmed config and hand back to `ftc-team-config` if one doesn't exist, exactly the same ask-don't-guess persona rule already proven, just enforced by a bigger-scope actor.

---

## Phase B — Build Pipeline ("the magic")

Design as a thin coordination layer, not a sixth skill that absorbs everything else — the "orchestration harness, not where the intelligence lives" framing already validated as the correct shape for this whole system, applied one level up.

**Confirmed: Option 2.** No new skill. Folded directly into Phase A's construction skill (`ftc-construct`) as a mandatory post-generation step: confirm config → scaffold/construct → automatically re-run `ftc-rule-check`'s constraint logic and `ftc-code-review`'s deterministic linters against what was *just generated* → one consolidated report before declaring done. Fewer skills, less routing-collision surface — this is why Phase A's kickoff prompt already includes it as Step 3 rather than treating it as separate future work.

**What this actually closes, concretely:** right now, newly generated code isn't automatically checked against the same deterministic linters that would catch problems in a review. A generated subsystem could contain the exact `global-mutable-static` pattern the corpus itself flagged as a real risk, and nothing currently re-checks the skill's own output against its own standards. This is a genuine gap, not manufactured busywork.

**Standing requirement, not a one-time check:** Phase A fetched 57 files of real library documentation. Storing it isn't the same as using it — every skill that touches a domain those docs cover needs an actual, verified read-and-cite path to them, not just proximity in the same repo. This applies going forward too: any future reference material added to this project gets the same standard — a stored file with nothing pointing to it is dead weight wearing the shape of depth.

---

## Phase C — Cross-Tool Compatibility + Continuous Pipeline

### C1. The efficient path is not eight separate integrations

Two real findings from actually checking, not assuming:

- **The Skills format itself is an open, published spec** (agentskills.io), not Claude-exclusive by design — and the broader agentic-tooling ecosystem is already converging on it. OpenCode specifically ships real, current, community-built bridges that read Claude Code's own hook format and memory files directly, and multiple skill marketplaces are already branded "for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity" as one shared set.
- **MCP is the complementary, genuinely cross-vendor protocol** for anything requiring live tool execution — the deterministic scripts specifically. This is the same reasoning already used for the deferred live-data layer (§8/§18), one level up.

**The design that follows from this:** expose Refract's core logic — rule lookup, hardware lookup, corpus query, config validation — as one MCP server. Every MCP-speaking client gets it without N separate reimplementations that could quietly drift out of sync with each other, which is exactly the N-copies problem this whole project has fought at every other layer (the feature model, standing-principles, R58's careful pointer-vs-copy distinction) — now one level up, across tools instead of across skills.

**Scope, per your call:** build the MCP server plus lean on the Skills format's own openness as the baseline — that alone reaches a real portion of the eight tools without any tool-specific research, since it's the same underlying mechanism already proven to work. Don't gate this phase on a dedicated deep-dive per remaining tool (Cursor's rules format, Copilot CLI's config, Gemini CLI's extensions, Antigravity's IDE model, Codex/ChatGPT's surface) — that's real future work, not required now. But take any genuinely cheap win that surfaces along the way without needing new research — a config flag, a small manifest addition, anything on the order of what was just found for OpenCode (a real, already-existing community bridge reading Claude Code's own hook/memory formats directly, which may only need a thin pointer or config tweak to pick up Refract specifically, not a new integration built from scratch). Cheap and available now: yes. A new research project per tool: not this phase.

### C2. "Continuous" means continuous input, not continuous auto-merge

Worth being precise here, because there's a real way to get this wrong. "Active pipeline, not build-once-and-frozen" is the right instinct — but it should mean continuously *detecting and drafting* new candidate material (newly public elite-team repos, library release updates, new Team Updates), never continuously *auto-merging* it. The human-gated merge checkpoint (nothing enters the corpus without sign-off) is the single most load-bearing discipline in this entire project — it's the mechanism that caught 21813's matrix error, corrected the 24089 shooter-finding reframe, and validated R58's exception. Relaxing it in the name of "continuous" would trade away the thing that made everything built so far trustworthy. The right design: a genuinely active input layer feeding the *same* human-checkpointed pipeline already built, not a new autonomous system bypassing it.

---

## Phase D — Final Hardening & Documentation Pass

Deliberately positioned right before the website, not earlier — Phase C's compatibility expansion changes what needs to be true and what needs to be said, and this phase should reflect that final state rather than be written twice.

### D1. Depth, sophistication, and accuracy — a real final inspection, not a formality

Same standard as everything else in this project, applied as one last comprehensive pass across all five skills before anything public links to this repo:

- Re-run Rule-7 verification on every reference claim for staleness — leverage the library-version-checking extension to `check_freshness.py` built in Phase A, and actually exercise it against each bundled library's current real release, not just confirm the mechanism exists.
- Re-run the full eval battery fresh across all five skills, including `ftc-construct`'s generation-quality suite, using whatever real usage patterns have surfaced by then as additional test cases — not just the original synthetic set.
- Expand corpus depth where real opportunity exists (further teams, if findable and legitimate per the same provenance discipline as Session 1) — genuine expansion, not padding for its own sake.
- Tighten every skill's description and body based on actual observed behavior rather than the original design-time guess, the same way HW/RC's descriptions already got sharpened once real routing collisions surfaced.

### D2. README — a real rewrite, not a touch-up

The existing README covers install for the state Refract was in right after Packaging. It needs to reflect five skills, the MCP/cross-tool surface from Phase C, and cover the full lifecycle, not just the happy-path install:

- **Install** — as it already has, kept current.
- **Update** — `/plugin marketplace update refract`, stated plainly, with what it actually does (pulls the latest pushed commit).
- **Uninstall** — the real fallback sequence: `/plugin uninstall refract-suite@refract` → `/plugin marketplace remove refract` (and re-add, if switching sources).
- Reflect whatever Phase C actually shipped — if other tools can now use Refract via MCP or a Skills-format bridge, the README needs to say so clearly, not just describe the original Claude Code path.
- Same "stunning, clear, no confusion about which skill does what" bar as the original README, raised to match everything that's been added since.

---

## Phase D2 — Full Documentation System

Added after Phase D closed, once real usage surfaced a real gap: the README alone doesn't cover per-platform installation depth, and two platforms specifically (Copilot CLI, Antigravity) were never actually verified — Phase C's table covers the VS Code Copilot *extension*, a different product from the standalone Copilot CLI tool. This builds a real `docs/` folder at repo root (not inside `refract-suite/` — user-facing repo documentation, not shipped plugin content) as a complete guide, and trims the README back to a clean entry point that links into it rather than trying to contain everything itself.

Same constraint as the website phase carries over here: no generated visual assets. Diagrams are Mermaid or plain ASCII (both render natively in GitHub markdown), or a real request back to you if an actual image is genuinely needed.

---

## Phase E — Website (separate session, scoped lightly here on purpose)

Full detail waits for its own dedicated session and prompt, per your instruction — capturing constraints now so nothing gets lost before then:

- Static site, hosted on Render.com.
- Aesthetic bar: impeccable.style and tasteskill.dev — that future session should actually *view* both sites directly before designing anything, not work from the names alone.
- "No AI slop" — genuinely considered design decisions, not generic template output. Reference whatever frontend-design guidance is available in that environment when the time comes.
- **Hard constraint, stated plainly so it can't get lost:** no Claude-generated SVGs, logos, or diagrams, ever. Any visual asset need becomes an explicit question back to you — you have your own generation tools for this. This goes into that future prompt as a rule, not a suggestion.
- Content will presumably cover: what Refract is, install instructions, the skill lineup, credits, a link to the repo — finalized when that phase actually starts.

**Status: paused mid-build (Stage 4 complete, deployed).** Phase H below takes priority over resuming this — a safety-critical gap in code generation outranks finishing the marketing site for it.

---

## Phase H — Physical Tuning & Device-Naming Safety

**Elevated priority — this jumps ahead of resuming Phase E, despite being added later.** Discovered while tuning 32008's autonomous, surfaced by a real `Constants.java`. This is categorically higher-stakes than any prior finding in this project: every other hallucination-risk category this project has fought produces a wrong *answer*. This one, left unfixed, lets `ftc-construct` generate code carrying a fabricated-but-plausible physical constant that directly drives a real robot's path-following behavior.

**Source-handling note:** the discovered `Constants.java` is 32008-derived — `public_shippable: false` by the same default established at F5. It's real, valuable evidence for this phase's design; it is not a corpus pattern to extract, and it is never a public or shippable example.

### H0. Two distinct problems — different fixes, don't conflate them

- **Device naming** (DS hardwareMap config names — `"rf"`, `"pp"`, etc.): universal, needed by every team regardless of library choice, currently has no schema field at all.
- **Physical tuning constants** (mass, PIDF gains, velocity constants, pod offsets): library-shape-dependent — Pedro's shape is not RoadRunner's shape is not a raw/custom drivetrain's shape — and fundamentally unmeasurable by any source lookup. No catalog, no library doc, nothing can ever supply these; they only exist once physically tuned on the actual robot. This is a different category from an "unseeded SKU" abstention case — it can never be seeded, by nature, not just not-yet.

### H1. Schema additions

- A `device_map` structure, dynamically generated per declared mechanism/sensor — same dynamic-generation principle already used for `season_mechanisms`' interfaces, not a fixed field list.
- A `tuning_constants` block, shaped per the selected `pathing`/`software_stack` choice — explicitly not hardcoded to Pedro's field shape as if it were universal. Carries a real `tuning_status` state (`not_yet_tunable` / `untuned` / `tuned`), because "config confirmed" and "robot physically tuned" are two separate real milestones in a team's build, not one.

### H2. `ftc-team-config` elicitation updates

- Device names: inferred-then-confirmed for a team with existing code (same inference-first principle as everywhere else), directly asked for a team building from scratch.
- A new branch: does the team already have real tuned constants (existing code, or pasted directly) or are they pre-tuning? This determines `ftc-construct`'s downstream path entirely.

### H3. `ftc-construct` generation rules — the actual safety fix

- Real tuned values, from any source: carried forward verbatim, never regenerated, never "helpfully" adjusted.
- No tuned values yet: generate the correctly-structured scaffold with every tuning-dependent field loudly, explicitly marked untuned — reusing the same fail-fast abstention convention already established (and literally shown on the website's own R92/R93 demo) — never a plausible-looking placeholder. Attach a real walkthrough of the actual tuning procedure, sourced from the library docs already fetched in Phase A.
- **Hard rule, no exceptions:** a fabricated-but-plausible tuning constant is never acceptable output, under any circumstance. This is the one category where "plausible" is strictly worse than "loudly missing."

### H4. `ftc-code-review` — a new deterministic check

Add to `failure_mode_lint.py`: flag any tuning constant matching or near-matching a known quickstart-template default value, unchanged — a strong, checkable signal the team never actually tuned their robot and may be running on fabricated example constants that happen to compile.

### H5. `standing-principles.md` addition

Name this as its own hallucination-control category, distinct from the unseeded-catalog-SKU case: physical tuning constants can never be source-derived, by nature. The only legitimate states are "carried forward from real measurement" or "explicitly, loudly marked untuned" — never a middle ground.

### H6. Retroactive fixture check

`19859-real-confirmed.yaml` (F2's promoted ground-truth fixture) predates this schema. Once the new fields exist, it needs a follow-up amendment — run through the real live `ftc-team-config` confirmation flow again, same discipline as its original promotion, not patched in after the fact.

### H7. 32008 boundary, explicit

`Constants.java` informs this phase's design. It stays internal-only per F5's existing default — never surfaced as a public example, corpus pattern, or documentation sample.

---

## Phase F — 19859 & 32008: The Ground-Truth Corpus Completion

Runs on the **original Refract session, not the website session** — starts once Phase E's kickoff prompt has been sent, in parallel with it, not blocked by it and not blocking it. This closes the single oldest open item in the entire project: Session 1's very first checkpoint deferred both 19859's and any teammate/partner repo's inclusion, back when neither was available. It's available now, and it deserves more rigor than a routine mining pass, not less — full permissioned access to your own team's actual competition code, described as fully validated and tuned, is categorically better source material than anything mined so far, and the process should be redesigned around that, not just pointed at a new folder.

### F0. Scope confirmation before anything else touches this material

Don't assume — confirm explicitly, first: the exact directory path(s) for both the 19859 material and the 32008 material now available; whether 32008 is genuinely upgraded to a full repo with real git history (unlocking the same evolution/provenance analysis every Tier 1/2 team got) or still the four partial files from before, now just relocated; and, separately for each source, the actual scope of permission granted — internal analysis only, or permission that extends to shipping derived patterns in the public plugin corpus. These are different questions with different answers likely for each source, and nothing downstream should assume an answer to any of them.

**Immediate action, not deferred:** extend the existing `PreToolUse` write-block hook (already protecting `corpus-sources/` and `32008teamcode/`) to cover wherever this new material actually lives, before any mining work touches it. This is genuinely sensitive, permissioned competition data — it gets at least the same structural protection as the public third-party repos already have, arguably more given the stakes.

### F1. A genuinely different mining methodology — not the same static pipeline pointed at a new folder

Every prior team was mined through static analysis alone, because that's all that was available — code, commit messages, whatever a README happened to say. This source is different in kind: the actual person who wrote it is available to answer directly. The pipeline should be built around that difference — where static analysis produces an ambiguous finding ("why was X abandoned," "was Y intentional or a workaround"), the correct move is to ask you directly and record the real answer, not infer one the way every external team's repo required. This is a methodological upgrade worth naming explicitly, not just a nicer version of the same process.

Otherwise, the full Tier-1-equivalent treatment applies, at full depth: feature-vector extraction, pattern extraction in reviewed batches (same 5-8 batch size, same provenance-before-confidence discipline, no shortcuts for familiarity), evolution analysis across the real commit history if F0 confirms it exists for either source.

### F2. 19859 becomes the actual ground-truth eval fixture

§20's synthetic evals have been using a stand-in for "the real current config" since no confirmed real one existed yet. Once 19859's actual config is extracted and confirmed, it replaces that stand-in across the eval suite — this was always the intended design, just waiting on real data.

### F3. Every existing cross-team finding gets re-checked against the new data, one at a time

Not a bulk append. Walk orchestration-nonblocking, shooter-empirical-vs-physics, moving-shot-compensation, and sensing-modality individually against whatever 19859 (and 32008, if fully available) actually shows — same rigor as every prior update to these findings, including the possibility that a finding's confidence moves in either direction, not just up.

### F4. "100% validated, tuned and tested" may close a real open item

The `stale_pid` failure-mode check has been sitting since Phase 9 as "implemented as heuristic, not yet validated — needs a real positive case." A team's actual tuning history, confirmed accurate rather than inferred from commit timing, is exactly the kind of source that could finally validate or correct that heuristic. Check this specifically, don't let it get lost among the routine extraction work.

### F5. The attribution checkpoint — explicit, not assumed

Before any pattern derived from either source becomes eligible for the **public** corpus (the one that ships inside the Refract plugin, visible to anyone who installs it): confirm the actual scope of permission separately for each source, per F0. The sensible default absent explicit confirmation otherwise — patterns from both sources inform internal corpus quality and the eval ground-truth immediately, but are held back from the publicly-shipped corpus specifically until permission for public inclusion is separately and explicitly confirmed, especially for 32008 where the permission wasn't yours alone to grant.

---

## Phase G — TickTree Integration

Runs **alongside Phase F**, same session, same window — both are the last real work before the website goes live, and both share a defining trait: the actual author of the source material is available to ask directly, unlike every publicly-mined team so far. Repo: `github.com/N0v4ont0p/Ticktree`.

### G0. Check the repo's actual state before committing effort to it

It may currently be empty or too early-stage to meaningfully analyze — it's under active development, not a finished library like Pedro or FTCLib. Confirm what's actually there first. If there's nothing substantive yet, don't force a mining pass on it — note the state plainly, defer, and check again later. Same discipline already applied to Pioneer-Robotics: don't manufacture analysis out of material that isn't ready for it.

### G1. If real content exists — learn it the same way Phase F learns 19859's code

Full read of whatever's there — source, docs, README, examples — with the same advantage Phase F has and no other source in this corpus does: the actual author is reachable for anything ambiguous. Ask directly rather than inferring, same methodology as F1.

### G2. Recognition, the same way FTCLib/Pedro/RoadRunner are recognized (R21)

TickTree needs to be identified as a legitimate library dependency, not mistaken for a team's own hand-rolled code, anywhere it appears — in corpus mining going forward, and in `ftc-construct`'s own reasoning about what a team is building on.

### G3. Make it a real, selectable option — not just documented, actually usable

This is the concrete meaning of "let the skill utilize it": add TickTree as a genuine choice in the config space (a new axis alongside `opmode_style`/`pathing`, or an extension of one of them — whichever fits its actual architecture once G1 clarifies that) so a team can select it, and `ftc-construct` can scaffold and generate against TickTree's real API — grounded in what G1 actually learned, same citation discipline as every other library, never inventing an API call that wasn't confirmed to exist.

### G4. The bidirectional feedback loop — the distinctive part of this phase

TickTree is your own project, still being built. When learning it or trying to generate against it, Refract will find things — and those findings split into two categories that need to stay explicitly separate, not blurred together:

- **Refract-side**: "here's how Refract should account for TickTree's current actual behavior" — normal integration work, same as any other library.
- **TickTree-side**: "this looks like an unintended bug, gap, or inconsistency in TickTree itself, not something to just quietly work around" — this does **not** get silently absorbed into Refract's integration layer as a workaround. It gets logged explicitly, in its own file, clearly separable from Refract's own documentation, so it can be handed directly to the TickTree project as real feedback. Two projects improving off one analysis pass, not one project quietly patching around the other's rough edges.

### G5. Treat TickTree's docs with the same staleness discipline as everything else

It's actively changing, more than any other bundled library. Whatever gets stored from G1 goes through the same version-stamped, freshness-checkable treatment already built for the Phase A library docs — this is the one bundled library most likely to drift out of date quickly, and it should be the best-instrumented for catching that, not the most likely to go silently stale.

---

## Phase I — Starter Choice, Full Documentation Sweep, TickTree Activation

Three distinct threads, none safety-critical like Phase H, all real gaps worth closing.

### I1. Starter-template choice — Pedro's own quickstart, not just FTCLib's

`ftc-construct`'s no-template branch currently offers only `FTCLib/FTCLib-Quickstart`. Verify Pedro Pathing's own official starter/quickstart repo actually exists and get its real name — don't assume a name. Once confirmed, the choice a new team faces should be filtered by what they've already declared, not an unconditional menu: a team that's already confirmed `pathing: pedro_pathing` sees Pedro's own starter as a real option alongside FTCLib's generic one; a team on `pathing: roadrunner` should see RoadRunner's own starter checked for and offered the same way, if one exists. If starter choice would need to happen *before* `pathing` is even confirmed for some team, that's a real sequencing question — surface it rather than deciding unilaterally which comes first.

### I2. Full documentation sweep — exhaustive this time, not curated

Per your explicit instruction: re-run the fetch for every library in `library-docs/`, this time downloading everything reachable rather than judging what's "high value." Reuse Phase D2's completeness-audit mechanism (the real page-list-against-live-source comparison) to find every gap, then close all of them, not just the top pick per library the way D2 did for RoadRunner and Pedro. Same lightweight hygiene as always — source and fetch-date headers, domain-split storage — the instruction changes scope, not the tagging discipline. Worth making this repeatable going forward: extend `corpus-input-scan.py` to flag completeness gaps the same way it already flags staleness, so this doesn't need to be a manual sweep every time.

### I3. TickTree activation — it's wired, but it's never actually been offered or used

`software_stack.behavior_layer` was deliberately built as optional-detected, not mandatory-ask — correct, given TickTree's pre-alpha status, teams shouldn't be forced through a question about it. But optional-and-never-mentioned is functionally invisible to anyone who doesn't already know the exact schema key. Fix: `ftc-team-config`'s elicitation should proactively *mention* TickTree exists, with its honest pre-alpha caveat attached, at the point where orchestration approach naturally comes up (near the FTCLib-command-based vs. raw-LinearOpMode branch) — offered, not forced, but discoverable. Separately: run an actual real generation test selecting TickTree end-to-end through `ftc-construct`, the same standard already applied to Pedro/FTCLib/RoadRunner in Phase B's utilization audit — G3 was verified as wired, never verified as working. This is also the first real chance for G4's feedback loop to have something to catch; re-check TickTree's actual repo for updates since G0/G1's initial read before running this, given how actively it's still developing.

---

## Status

Phase A: done. Phase B: done. Phase C: done. Phase D: done. Phase D2: done. Phase E: paused mid-build (Stage 4 shipped and deployed; visual polish pass outstanding). Phase F: done. Phase G: done. Phase H: done — closed to full standard, including the generation-path gap that was honestly left open mid-phase. Phase I: done (I1/I2/I3).

**G4 is no longer empty.** It stayed empty through G0/G1 because nothing had exercised TickTree hard enough to surface anything — an honest result, but a result of not looking rather than of looking and finding nothing. Phase I's real end-to-end generation test (the thing G3 never did: G3 verified TickTree was *wired*, never that it *worked*) produced four TickTree-side findings on first contact, now in `TICKTREE-FEEDBACK.md`. Two are verified facts about the repo, one is a documentation-coverage gap, and one is a compile-level naming trap that a correct reading of the docs walks straight into. All kept TickTree-side per G4's split rather than absorbed into Refract as workarounds.

**Open, carried forward — not silently dropped:**

- **Starter-choice sequencing (from I1).** `ftc-construct` can filter starter offers by confirmed config because `pathing`/`opmode_style` are mandatory-ask and already gated. A team with no project at all asking "how do we start" arrives at `ftc-team-config` *before* any stack is confirmed, where the filter has nothing to filter on. Whether to offer unfiltered there, or to simply ask pathing first, is a real question-ordering decision — flagged rather than resolved unilaterally.
- **TickTree's staleness special case (G5).** `corpus-input-scan.py`'s commit-tracked branch for TickTree is still required. Re-checked 2026-08-06: the revisit condition is closer (tag `v0.1.1` now points at the docs commit, where `v0.1.0` predated them) but not met — those are tags only, `/releases/latest` 404s, so a release-based check would error. Move it back and delete the branch when real releases exist.
