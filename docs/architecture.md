# Architecture — why this isn't just prompting an LLM and hoping

A model that's good at reasoning is still bad at recall under confidence. The failure mode this
project is built against isn't "the model doesn't know things" — it's narrower and more dangerous:
**a capable model answers from memory exactly when it feels confident, and that's exactly when a
wrong recall does the most damage**, because it's stated plainly, unhedged, and built upon. This
project's own history has three independent, observed instances of this: a corpus-mining pass that
confidently restated an earlier conclusion nobody had re-checked against the actual code; a
hardware-lookup baseline that verified a hard-looking multi-ratio comparison but answered a
seemingly-easy question from memory — and drifted (recalled a motor's stall current as roughly 30%
off, and a gravity constant one significant figure short); a review pass that almost logged a real
bug as "non-blocking" on confident, typical-case reasoning that turned out not to hold for the
actual game geometry. Three different domains, one shape: confidence, not question difficulty, is
what predicts whether a check gets skipped.

The response isn't "the model should be more careful." Telling a model to be careful doesn't
survive the moment careful stops feeling necessary. The response is structural: **route every fact
through something that can't get confident — a stored table, a deterministic script, a verified
citation — and reserve judgment for the parts that genuinely need it.**

## Two files, two update rhythms

`core-feature-model.yaml` and `season-extensions/<slug>.yaml` are split specifically so that two
things that change on different schedules don't corrupt each other. The core model — drivetrain
types, control hardware, software-stack axes — changes only when the FTC hardware/software
ecosystem itself changes (the eventual SystemCore/MotionCore transition is the next one on the
horizon, and the schema already has a slot for it). The season extension — this year's mechanisms,
scoring rules, archetypes — gets replaced wholesale every season. A file that mixed both concerns
would need careful, error-prone surgery every season to avoid deleting something structural by
accident. Splitting them means a season transition is "swap one file," not "carefully edit a
monolith and hope nothing load-bearing got touched."

`software_stack.behavior_layer` (added when a third-party behavior-tree library became a real
config option) is deliberately modeled as *optional and detected* rather than mandatory-always-ask,
the same way `sensing.vision`/`sensing.odometry` are — because forcing every team through a
question about a niche library most have never heard of would be worse UX than just detecting it
when it's there. Not every axis earns the same weight; the schema tracks that distinction on
purpose.

## The pattern corpus — and the discipline that keeps it honest

The corpus is code patterns mined from real competitive teams' repositories, each tagged with a
**confidence level** and a **provenance classification**: `independently-derived` (the team's own
design) or `shared-ancestry` (adopted from a common library or a widely-taught convention). This
distinction is the entire point. A convention six teams all use because they all imported the same
library, or because the platform itself nudges every team toward the same shape, is not six
independent confirmations that the convention is good — it's one data point wearing six coats.
Adoption of a shared library is never treated as independent validation of a design choice.

This gets tested against real, worked cases, not asserted as a policy. One corpus finding
(non-blocking cooperative orchestration over blocking sleeps) rests specifically on a *third* leg
that happens to run cross-platform — because the first two legs are both FTC teams, and FTC's own
OpMode model nudges every team toward that shape regardless of whether the design is actually
good. The confidence in that finding is pinned to the leg that isn't explained away by the
platform, not to the leg count. Elsewhere, mining a team's own real repository surfaced two
patterns that shared one underlying body of work (a single calibration-fit lineage, drafted as two
candidates before being merged into one) — counted as one data point, not two, specifically so a
prolific single source doesn't get to outvote genuine independent convergence.

## Retrieval grounding, deterministic scripts, calibrated abstention

Three mechanisms, one goal — a fact never gets stated because it sounded right:

- **Retrieval grounding.** Library API calls, rule text, hardware specs — all read from a stored,
  source-cited file at the moment they're needed, never recalled. Every stored file is timestamped
  and tied back to a URL, so "grounded" means something a person could go re-check, not a vibe.
- **Deterministic scripts.** Motor math, trajectory solving, config validation, rule
  lookup/cross-reference, freshness checks against a live source — all real, runnable scripts, not
  prose describing what the calculation should be. A script either produces the right number or it
  crashes; it can't produce a *confident wrong* number, which is the specific failure mode this
  whole architecture is built against.
- **Calibrated abstention.** When a part isn't in the seeded catalog, or a season's manual can't
  be confirmed current, the correct output is an explicit "I don't have this — here's what I'd
  need," not a plausible fill-in. A filled gap that turns out wrong costs more than an admitted
  gap, because the person builds on it. This is enforced at the script level (a real exit code, a
  real abstention reason), not left to the model's judgment on a given day.

None of these three is sufficient alone — a deterministic script still needs a human decision about
*when* to invoke it instead of answering from memory, which is why the skills' own instructions
name specific trigger conditions rather than leaving "use the tool when it seems hard" to
after-the-fact judgment. The discipline is in the routing, not just the existence of the tools.
