---
name: ftc-code-review
description: 'Config-aware, pattern-aware review of FTC robot code: deterministic anti-pattern linting, structural review grounded in the elite-team pattern corpus (confidence and provenance presented faithfully), constraint checks against the team''s confirmed config, and full pre-competition codebase reviews via an isolated read-only subagent. Use whenever the user asks to review, check, audit, or improve FTC robot code, reports a MECHANISM OR OPMODE that "behaves differently for no reason" or works intermittently (a shooter/motor/sensor whose behavior varies match-to-match with no code change), asks "is this a good way to do X" about robot code structure, or is preparing for competition — that specific class of symptom is often a code-structure problem (stale static state, missing telemetry) this skill''s corpus specifically catches. NOT for pure connectivity/networking symptoms (driver-station WiFi drops, field router congestion) — those have no code-review angle and this skill should not claim them.'
---

# FTC Code Review

Two tiers, and keeping them separate is the whole point: a **deterministic tier that is authoritative**
(a script found it, it's a finding) and an **LLM-judgment tier that is heuristic** (a smell, shown with
the code as evidence, never asserted as a verdict). Collapsing them — dressing a heuristic hunch as a
hard finding, or second-guessing a script result — is how a review loses trust.

Read `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/standing-principles.md` (suite root) first. Paths below are relative to the suite root.

## What this reads

| File | Role |
|---|---|
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/failure_mode_lint.py` | 6 deterministic checks (bus-factor, vcs, god-opmode, telemetry, stale-pid, mutable-static) |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/config_lint.py` | flags code referencing a mechanism the confirmed config declares absent (R40/R34) |
| `team-config.yaml` (team's project) | the confirmed config this review is *against* — read it first |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/` | the pattern corpus + `cross-team-findings.yaml` |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/known-failure-modes.md` (suite root) | the failure-mode taxonomy the linter checks operationalize |
| `${CLAUDE_PLUGIN_ROOT}/agents/full-review.md` | the isolated Opus-xhigh read-only full-review subagent |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/check_freshness.py` + `${CLAUDE_PLUGIN_ROOT}/skills/ftc-rule-check/scripts/rules.py` | invoked directly when a review turns legality-flavored (§5 below) — never re-derived inline |

## The review

### 1. Deterministic tier first — authoritative

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/failure_mode_lint.py <repo>     # JSON findings + stats
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/config_lint.py <code_dir>       # undeclared-mechanism references
```

Report these as **findings**, not suggestions — a script confirmed them. `failure_mode_lint`'s
mutable-static check in particular catches the "behaved differently for no reason" class that reads
like a hardware flake but is cross-opmode state (see `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/known-failure-modes.md`). `config_lint` findings
are the R34 case: code for a mechanism the config says the team doesn't have — flag as "not referenced
by current config; confirm if stale or a config mismatch," don't assume which.

### 2. Config-aware structural review against the corpus

Read `team-config.yaml` and review the code *for this robot*, not a generic one. When the code matches
or diverges from a corpus pattern, you may cite the pattern — but **display its confidence and
provenance exactly as stored, never inflated.** A `confidence: single-source` pattern is presented as
single-source; a `shared-ancestry` provenance is stated as such; the pattern's `notes` caveats are
carried verbatim. The corpus already did the hard provenance work (§12); your job is faithful display,
not re-grading. Two specific traps:

- **Never upgrade a pattern's confidence in presentation** because it happens to fit well here. "Six
  teams do this" is not independent confirmation if the corpus tagged them shared-ancestry — repeat the
  corpus's own framing, not a headcount (R43).
- **A pattern candidate you notice mid-review that isn't in the corpus** gets *routed to the corpus
  process*, not classified inline. This review skill displays provenance; it doesn't mint it (R46). Say
  "this looks like a candidate pattern — worth running through corpus construction," and move on.

Every recommendation ties back to a confirmed config feature AND the source pattern/rule that triggered
it (R39) — an untethered "you should refactor this" is not a review, it's an opinion.

### 3. LLM-judgment tier — heuristic, evidence not verdict

For structural smells the linter can't catch deterministically (god classes forming, missing subsystem
separation, tangled control flow), delegate a Sonnet subagent. Its output **shows the flagged code as
evidence and explains the concern** — it never asserts "this is wrong." The reader judges; the tier is
explicitly heuristic (R63). Keep it lean — don't over-invest reasoning in what is by nature a hunch.

### 4. Full pre-competition review

For the high-stakes whole-codebase pass before a competition, delegate the **`full-review` subagent**
(Opus 4.8, xhigh, read-only tools, its own context so it never pollutes the working session). It
reports findings with evidence; it does not edit. This is the one worth the cost — a missed structural
problem at a competition is expensive.

### 5. Legality-flavored questions about existing code — resolve via ftc-rule-check's real flow, don't approximate

If a review request is genuinely a legality question about code that already exists ("is this
mechanism legal", "will this pass inspection") rather than a structural/pattern review question,
don't review it as a code-quality matter and don't guess at a verdict. Resolve it the same way
`ftc-rule-check` would, by invoking its actual tools directly — the same sequential-boundary this
project already uses for hardware tables (R27: a rule citing an embedded table resolves BY POINTER
into HW's structured file, never re-derived inline; here, a review that turns legal resolves BY
POINTER into RC's own scripts, never re-derived inline either):

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/check_freshness.py                 # freshness first
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-rule-check/scripts/rules.py lookup <id>       # rule + one-hop cross-refs
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-rule-check/scripts/rules.py verify <id>       # citation existence, non-negotiable
```

Reason over the retrieved (and cross-referenced) text against what the *existing* code actually
does, and emit the same `{verdict: legal|illegal|ambiguous, citations: [{id, text}], reasoning}`
shape `ftc-rule-check`'s own SKILL.md defines. This mirrors `ftc-construct`'s own post-generation
rule-check (its §5) — same discipline, applied here to code that already exists instead of code
just generated. It is not new legality logic living in this skill; it is this skill invoking
`ftc-rule-check`'s own scripts and structure directly, the same way it already reads the corpus and
config by path rather than re-deriving them. A *pure* legality question with no existing code in
view still belongs to `ftc-rule-check` directly, unchanged — this only fires when a review already
in progress turns out to hinge on legality.

## Boundaries that shape a review, not just decorate it

- **`fabrication.capability` changes tuning values you *advise*, never which pattern you recommend**
  (R4). A CNC team and a stock-goBILDA team get the same architecture, different acceleration limits.
- **`experience: rookie` changes explanation depth, never the finding** (R5) — explain the *why* of a
  God-class smell more, don't soften or omit it.
- **SDK integrity is a hard line** (R52): never suggest modifying or omitting anything in `libs/` —
  that makes the Robot Controller competition-illegal. Flag it if you see it.
- **Attribution stays on cited corpus code** (R51): reference by team + file/line, never present
  distilled elite-team structure as anonymous.

## Not this skill

Legality verdicts (ftc-rule-check), hardware specs/math (ftc-hardware-lookup), establishing or changing
the config itself (ftc-team-config — this skill reviews *against* a confirmed config, it doesn't set
one). If the review reveals the config is wrong, say so and hand back to ftc-team-config rather than
editing the config here. **Narrow exception (§5 above):** when a review already in progress turns out
to hinge on a legality question about that specific existing code, this skill resolves it by invoking
`ftc-rule-check`'s own scripts directly rather than deferring or guessing — it still isn't reviewing
*generically*-posed legality questions with no code in view; those go to `ftc-rule-check` untouched.
