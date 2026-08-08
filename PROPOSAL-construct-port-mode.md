# Proposal: a first-class "port and adapt existing code" mode for ftc-construct

**Status: proposal, not built.** Per the Step 6 brief — this changes the skill's shape, so it gets a
decision checkpoint before implementation, not a silent patch.

## The observation

Every real invocation of `ftc-construct` in the tuning session that produced this was, in substance,
*"take our own already-working code and adapt it"* — not *"scaffold a new mechanism from the
interface template."* The team said so explicitly and repeatedly: read the original code and put it
here, the only change is the path; the real teleop is this one, the others are junk.

Both invocations operated on hand-authored state-machine code that never resembled the quickstart
template's interface shape. The consequence is measurable rather than impressionistic: the skill's
**core** — interface derivation from `season_mechanisms`, template adaptation — went entirely
unused both times. Only the **tail** ran: the config gate, the linters, the rule-check, the tuning
verify. Those are the parts that delivered value.

## Why this is a product-shape question, not a bug

The template path is not wrong. It is right for the case it was designed for: a team with no code,
or a team adding a mechanism they have never built. That case is real and the template serves it
well.

But a *returning* team — which is most teams, most of the season — walks in with code that already
works, has been driven at a competition, and encodes hard-won tuning nobody wants regenerated. For
them, "scaffold from an interface template" is not a helpful offer. It is a proposal to throw away
the thing they trust. Their rejection of it was not confusion about the feature; it was a correct
read of their own situation.

**One session is not a trend.** This is a single engagement with one team, and the honest weight of
the evidence is "this may be the common case", not "this is the common case". That uncertainty is
precisely why this is a proposal.

## What a port mode would actually be

Not a second scaffolder. The distinguishing question is **what the generated code is checked
against**, and that is where the real design work is.

| | Template mode (today) | Port mode (proposed) |
|---|---|---|
| Input | confirmed config + quickstart template | confirmed config + the team's existing source |
| Structure comes from | the template's interfaces | **the team's own existing structure** |
| Primary risk | generating something that doesn't fit the robot | **silently changing behaviour that already worked** |
| "Correct" means | matches the template's conventions | **is a faithful port — behaviour preserved except where change was requested** |

### The verification problem, stated honestly

Template mode can check its output against a known-good structure. Port mode has no such reference —
and that is the whole difficulty. The current mandatory gates split cleanly:

**Still work unchanged**, because they check against the config or the world, not the template:

- `validate_config.py` — the `generation_allowed` precondition.
- `emit_tuning.py verify` — every tuning literal must match the confirmed config. *More* valuable
  here, not less: porting is exactly when constants get retyped, reordered, and quietly altered.
- `failure_mode_lint.py` — `template_default_tuning_constant`, `duplicate_tuning_literal`,
  `mutable_static_opmode_write` and the rest are properties of the code, not of its lineage.
- `rules.py` legality re-check and the freshness gate.

**Do not apply, and must not be faked:**

- Interface derivation from `season_mechanisms` — the team's structure is the structure.
- Template-conventions adaptation — there is no template in the picture.

**Missing, and this is the actual proposal:** a *port-fidelity* obligation with no current
equivalent. Candidates, roughly in order of how much they'd earn their cost:

1. **Constant-preservation diff.** Every numeric literal in the source must appear unchanged in the
   port, or be explicitly listed as an intended change. Deterministic, cheap, and catches the single
   most likely porting error. This is `emit_tuning verify` generalised from tuning fields to all
   literals, with the *source file* as the reference instead of the config.
2. **Control-flow shape check.** State-machine states, transitions, and their guards should survive
   a port one-for-one unless a change was requested. Harder; probably starts as a reported summary
   ("14 states in, 14 states out, 1 guard differs") rather than a pass/fail gate.
3. **Explicit change manifest.** The port declares what it intended to change. Anything that
   differs and is not on the manifest is a finding. This is the honest version of "did you change
   anything you didn't mean to", and it composes with both checks above.

Without at least (1), port mode would be *less* verified than template mode while operating on code
the team already trusts — a strictly worse trade, and a reason not to ship it half-built.

## Addendum (Phase J): a fuller retrospective of the same engagement — not a second one

A more detailed narrative of the same 32008/slowstart build later became available, covering the
same session this proposal was already built on: verbatim porting explicitly chosen over the
template, an explicit accounting of every deviation from the ported source (two added methods
across the whole session, each with an inline comment stating what it does and does not touch), and
the team's own repeated, escalating insistence on porting real code over scaffolding new.

**This is elaboration, not a second data point.** It does not move the count from one engagement to
two, and it is flagged here explicitly so the added detail doesn't get miscounted as reinforcement
toward Option A later — the recommendation below is unchanged by it. What it does usefully supply is
a concrete number for a claim Option B and a future Option A both need eventually: this session's
own actual deviation-from-source discipline was two methods, both marked, across the entire ported
subsystem — real evidence for "deviations from a port should be rare, small, and self-documenting"
as an operating norm, not a hoped-for one. Worth carrying into Option B's wording now (a port is
expected to stay close to its source, with any departure marked at the point it happens) and into
Option A's `_entry_shape` design later (an explicit change manifest, item 3 above, is exactly what
this norm would be checked against) — but as a *design input* for whichever option gets built, not
as the second engagement that would justify building A now.

## The three ways this could go

**A. Build port mode as a first-class second path.** Highest value if the observation generalises.
Cost is real: a new verification family (above), a mode-selection question early in the flow, and
`ftc-construct`'s description rewritten so routing actually reaches it.

**B. Do nothing structural; sharpen the existing wording.** Note in `ftc-construct` §2 that adapting
a team's own working code is legitimate and the template is skippable. Nearly free. Leaves the
verification gap open — a port still gets no fidelity check — but stops the skill implying the
template is the only road.

**C. Gather evidence first.** Treat the single session as a signal, not a finding. Record port-shaped
requests when they occur; revisit after a few more real engagements. Costs a season.

**Recommendation: B now, A when a second independent engagement shows the same shape.** B is honest
and immediate, and removes the mismatch the team actually hit. A is the right end state but rests on
one data point today, and the verification family it needs is substantial enough that building it
against a single observation risks designing for the wrong case. C alone is too passive — the
wording problem is real and fixable now.

## What is explicitly NOT proposed

- Loosening any existing gate. Port mode would keep every one that still applies.
- Auto-detecting mode. Which mode is a question for the team, not an inference from repo shape.
- Anything about the team-specific code this observation came from. That stays internal-only per the
  existing default; nothing from it is cited, shipped, or promoted here.
