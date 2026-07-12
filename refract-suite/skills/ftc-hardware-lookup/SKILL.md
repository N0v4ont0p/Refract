---
name: ftc-hardware-lookup
description: 'Answers FTC hardware questions from structured spec tables and deterministic math scripts: motor/servo/battery specs, gear-ratio, torque and speed calculations, part dimensions and compatibility, the game manual''s legal-parts tables, and mechanism/projectile physics. Use whenever the user needs ANY hardware number, spec, part selection, or performance calculation — including casual mid-conversation asks ("what''s the free speed of a 5203", "what ratio do I need for this arm", "will this motor fit") — because hardware values must come from the structured tables and scripts, never from memory, and a confident-sounding spec from memory is exactly the failure this skill exists to prevent.'
---

# FTC Hardware Lookup

This is the highest hallucination-risk domain in the whole suite. A model asked "what's the free
speed of a goBILDA 5203 at 19.2:1" will produce a confident, plausible, wrong number — and a team
will gear a drivetrain around it. The single rule that makes this skill trustworthy:

**A hardware value comes from a structured file or a script's output. It is never generated,
never recalled, never estimated — no matter how confident the recalled number feels.**

Confidence is not the safeguard; it's the hazard. This project has already caught two cases where a
value that *looked* right was wrong at the source: a physics constant a real team shipped (gravity
385 vs 386.4 in/s²), and an external kinematics paper whose derivation was sound but whose final
printed matrix had a sign error. Both were caught only by going to the data and re-deriving, not by
judgment. In this domain, "I'm confident it's about 6000 RPM" is precisely the move that fails.
Route to the file or the script. Read `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/standing-principles.md` at the suite root first —
its deterministic-first, abstention, and Rule-7 sections are the backbone of everything below.

## Files this skill owns and reads

| File | Role |
|---|---|
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/catalogs/{motors,servos}.json` | verified part specs, each value carrying its own `_source` |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/catalogs/INDEX.json` | coverage map + the **abstain rule** for gaps |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/motor_math.py` | ALL gear/torque/speed/tick arithmetic; abstains on unseeded parts |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/manual-tables/*.json` + `INDEX.json` | the game manual's legal-parts tables (§9 side of the §8↔§9 pointer) |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/physics/decode-artifact-ballistics.json` + `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/trajectory_solver.py` | projectile/ballistics constants + solver |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/hub-generations/*.md` | control-system briefings — **hosted here, read by ftc-team-config** on its time gate |

Other skills read these by path directly (the R77 canonical path table in standing-principles);
this skill never restates their content when *it* needs another skill's data either.

## Answering a hardware question — route by type

### 1. A part's spec ("free speed of a 5203 19.2:1", "Core Hex stall torque")

Read it from the catalog — do not answer from memory even for a spec you think you know.

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/motor_math.py spec <SKU>      # e.g. 5203-2402-0019
```

This returns the record **and its source**. Surface the value *with* its citation — a spec without
its source is not a finished answer here (that's R68, and the catalog is structured so you can't
honestly give one without the other). If the part isn't in the catalog, the script abstains (exit 3)
and so do you: *"I don't have a verified spec for that part — it's not in the catalog"* plus the
manufacturer link. **Do not fill the gap from memory.** The seed is deliberately small; a gap is a
safe abstention, a fabricated spec is the one unsafe outcome (see `catalogs/INDEX.json`).

### 2. Anything numeric (gear ratios, output RPM/torque, wheel speed, encoder ticks)

Never do the arithmetic yourself — call the script. It reads base values from the catalog and shows
its assumptions:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/motor_math.py external    <SKU> --ext 20          # add a 20:1 external stage
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/motor_math.py wheel-speed <SKU> --wheel-mm 96     # free linear speed
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/motor_math.py ticks       <SKU> --wheel-mm 96     # encoder ticks per meter
```

Two things the script handles that hand-math gets wrong, and why they matter:
- **Encoder CPR is read from the published output-shaft value, not recomputed from the round ratio
  label.** goBILDA's "19.2:1" is a rounded label; the true ratio is 19.20 and the published CPR
  (537.7) reflects it. Recomputing 28×19.2 gives a subtly wrong tick count — the same shape of error
  as the 21813 matrix. Let the script use the source value.
- **Ideal vs real torque.** The script reports ideal gear-multiplied torque and says so — real
  torque is 10–30% lower from gearbox losses. Never present the ideal figure as the delivered one.

Wheel diameter is a **config input** (from the team's confirmed `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/core-feature-model.yaml`), not a
catalog value — pass it in with `--wheel-mm`. If you don't have it confirmed, that's an ask, not a
guess (standing-principles §4).

### 3. "Is this part legal" tables (motors, batteries, wire gauge, power)

The competition manual embeds legal-parts tables. Those live here as structured files keyed by
manual table ID (`${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/manual-tables/table-12-1.json` etc.; see `INDEX.json`). A legality
*verdict* is ftc-rule-check's job — but when its reasoning turns on a table, it resolves the pointer
into these files (the §8↔§9 mechanism). When *you* answer a "what parts are allowed" question, read
the table file; never paraphrase legal-parts data from memory or from the rule prose.

### 4. Physics / ballistics (launch angle, projectile, shoot-on-the-move)

Use the solver, which reads its constants from the physics JSON (gravity is 386.4 in/s², corrected
and stored there, not hardcoded):

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/scripts/trajectory_solver.py -d 120 -t 24 -v 400   # distance, target height, launch speed (in, in/s)
```

It returns both no-drag and drag-aware launch angles (report the drag-aware one if the user acts on
it), the gravity value and its source, and abstains (exit 3) if distance or speed is missing rather
than guessing. It carries the same not-fielded caveat the corpus does: a correct solver proves the
math is tractable, it is not evidence any team fields physics-based power.

### 5. Control-system generation (REV Control Hub vs SystemCore)

This skill **hosts** the tier-tagged briefing (`${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/hub-generations/systemcore-motioncore.md`)
but does not decide when to raise it — ftc-team-config reads it on its time gate. If a hardware
question here touches the topic, read that file fresh and preserve its tier tags; never restate its
dates or claims from memory (they're still-evolving, exactly where Rule 7 bites hardest).

## Rule 7 and tiering

Every value surfaced carries its source tier. The catalog is tier-1 (manufacturer pages). If you
ever add or cross-check against a community source, it's tier-2 and must be labeled as such wherever
it surfaces — and anything forward-looking (SystemCore specs, still in alpha) needs two independent
sources before it's stated plainly. This is not optional politeness; it's how a reader knows what
weight a number can bear.

## CAD and datasheets

CAD (goBILDA STEP files) is a **link**, never ingested as text — point the user to it. A datasheet
you haven't fetched this turn is not a source you can cite; fetch it or abstain.

## Explanation depth

`team_context.experience: rookie` means explain more around the number — what free speed means, why
ideal torque isn't delivered torque — never a different or withheld number. The spec is the spec for
everyone; only the surrounding explanation scales (standing-principles §5).

## What this skill does not do

Legality verdicts (ftc-rule-check — though it reads these tables by pointer), robot config and code
generation (ftc-team-config), code review (ftc-code-review). When a question is really one of those,
it belongs there — but the hardware *data* it needs is read from here by path, not by handing the
user off mid-answer.
