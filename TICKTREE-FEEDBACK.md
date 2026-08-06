# TickTree-side findings — feedback for the TickTree project

Per **ROADMAP §G4**: findings that look like a bug, gap, or inconsistency **in TickTree itself** get
logged here, in their own file, rather than being quietly absorbed into Refract's integration layer
as a workaround. This file is meant to be readable standalone and handed to the TickTree project as
real feedback. Nothing here is a Refract design note.

The previous pass (G0/G1, 2026-07) closed with **"none found"** — an honest result at the time,
bounded by what had actually been read. This is the first pass with real content, and it exists
because Phase I ran the thing G3 never did: an actual end-to-end generation against
`behavior_layer: ticktree`, rather than only verifying the wiring.

**Basis for this pass.** TickTree repo re-read 2026-08-06. `main` HEAD = `998011a20399` — the same
commit Refract's stored docs were fetched at, so the docs themselves had not moved. Tags: `v0.1.0`
→ `c1f6b13`, `v0.1.1` → `998011a`. All 7 `docs/*.md` files read in full, plus `README.md`.

---

## 1. The docs make a claim about Refract that is no longer true

`docs/getting-started.md`, in the "Generating robot code with Claude Code?" tip:

> …mention TickTree alongside FTCLib/SolversLib/raw LinearOpMode so generated subsystem code gets
> wired as TickTree leaves rather than raw command bindings — **there's no formal TickTree option in
> its config schema yet**, but its skills pick up context from what you tell them.

That was accurate when written. It is not now: Refract's `core-feature-model.yaml` has carried
`software_stack.behavior_layer: [ticktree, none]` since Phase G3, `extract_feature_vector.py`
detects TickTree from imports, and as of Phase I `ftc-team-config` proactively raises TickTree at
the orchestration question. A team following the current wording will work around a limitation that
no longer exists.

**Suggested fix:** drop the "no formal option yet" clause; the axis is `software_stack.behavior_layer`.

*(Noted without editorial comment on the cross-promotion itself — the point is only that the factual
claim inside it has expired. This is the same class of problem as Refract's own standing-principles
§12: a claim that was correctly verified and then went stale.)*

## 2. Tags exist, but there are no published releases — and the docs pin the older tag

Two related, independently checkable facts:

- `GET /repos/N0v4ont0p/Ticktree/releases/latest` returns **404**, and the releases list is empty.
  `v0.1.0` and `v0.1.1` are **git tags only**, not published GitHub releases.
- `docs/getting-started.md` at commit `998011a` shows install coordinates pinned to **`v0.1.0`**
  (`com.github.N0v4ont0p.Ticktree:ticktree-core:v0.1.0`, and likewise `ticktree-ftc`) — but that
  very commit is what `v0.1.1` points at. A team following the current docs installs an artifact
  one tag behind the docs they are reading.

**Why this matters beyond tidiness:** any consumer that tracks library freshness through the
standard GitHub releases feed gets nothing back for TickTree. Refract has to carry a bespoke
commit-tracked staleness check for TickTree alone, explicitly marked in its own source as temporary
special-case logic to be deleted once TickTree publishes real releases. It is the only bundled
library in the corpus needing that.

**Suggested fix:** publish `v0.1.1` as an actual GitHub release, and bump the install snippet's
coordinates to match the tag the docs commit belongs to.

## 3. No documented wiring for FTCLib's `CommandOpMode` — the most likely host

`docs/getting-started.md` §4 documents two OpMode shapes: iterative `OpMode`
(`tree.tick()` in `loop()`, `tree.halt()` in `stop()`) and `LinearOpMode`
(`OpModeTreeRunner.runLinear`). Both are correct and clear.

Neither covers **FTCLib's `CommandOpMode`** — which is the base most FTCLib teams' TeleOps already
extend, and therefore the most probable place a team first tries to add a tree. That case is not
simply undocumented, it is *constrained*, and the constraint is not obvious from the outside:

- `CommandOpMode.run()` drives the `CommandScheduler` every loop.
- The node reference's own danger note says a subsystem must be driven "entirely through TickTree
  or entirely through the `CommandScheduler`, never both", since the command shims ignore
  `Command.getRequirements()` and do no resource arbitration.
- So a tree hosted inside a `CommandOpMode` and given the same subsystems is exactly the dual-drive
  case the library warns against — even though nothing in the code will complain, and the two
  documented wirings both look like they should transfer.

There is also no shutdown hook: `CommandOpMode` exposes no `stop()` override point, so the
`tree.halt()` actuator-stop guarantee has nowhere natural to live on that base.

Refract resolved this on its own side by generating a `LinearOpMode` that uses
`OpModeTreeRunner.runLinear` and deliberately not extending its own `CommandOpMode`-derived base —
recorded here only so the TickTree project can see what a real integration had to work out
unaided. That is an integration decision, not a claim about what TickTree should do.

**Suggested fix:** a short third tab in §4 for `CommandOpMode`, stating plainly that the scheduler
and the tree must not share subsystems, and showing whichever shape the project considers correct
(a plain `LinearOpMode`, or subsystems partitioned so the scheduler and the tree own disjoint sets).

## 4. `guard(condition, …)` cannot take a `Condition` — a naming trap a code generator walks into

`node-reference.md` documents these adjacently but never together, and the obvious composition
does not compile:

- **`guard(condition, child)`** — "The condition is either a `BooleanSupplier` (`() -> ...`) or a
  `Predicate<Blackboard>` (`bb -> ...`)."
- **`Conditions.gamepad(name, gamepad, test)`** — "Build a **`Condition`** from live gamepad state."

`Condition extends AbstractNode`. It is a **node**, not a functional interface, so
`guard(Conditions.gamepad("shootHeld", gamepad1, g -> g.right_bumper), child)` fails to typecheck
against both `guard` overloads. The parameter is *named* `condition`, there is a class *called*
`Condition`, the FTC bridge ships a factory *called* `Conditions` — and the one combination all
three names suggest is the one that is invalid.

This was hit for real: Refract's first generated TickTree TeleOp used exactly that call, grounded in
a correct reading of both doc entries, and it took reading `Condition.java` in the source to see
why it was wrong. The working form is the lambda one from `getting-started.md`
(`guard(() -> gamepad1.a, …)`).

**Suggested fix:** one line under `Conditions.gamepad` saying a `Condition` is a node — use it as a
child (e.g. the first element of a `sequence`), and use a lambda for `guard`. A short
counter-example would carry more than the type signature does.

---

## Scope and honesty notes

- Findings 1 and 2 are **verified facts** about the repo as of 2026-08-06 — anyone can re-check
  them against the same commit and API endpoints.
- Finding 4 is a **verified compile-level fact** (checked against `Condition.java`, not inferred
  from the docs alone), reported as a documentation trap rather than a code defect — the types are
  behaving as designed; the names point the wrong way.
- Finding 3 is a **documentation-coverage observation**, not a defect claim. Nothing in TickTree is
  broken; the constraint is disclosed, just not at the place a `CommandOpMode` user would meet it.
- No finding here was worked around silently on the Refract side. Where Refract had to make a local
  decision (finding 3), that decision is stated above rather than left implicit.
- This pass read the docs and repo metadata. It did **not** re-read the FTC-bridge source files or
  run TickTree's own test suite, so it says nothing about runtime behavior.
