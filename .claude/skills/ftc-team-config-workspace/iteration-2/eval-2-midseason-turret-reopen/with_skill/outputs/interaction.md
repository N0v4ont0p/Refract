# Interaction — STOPPED for required confirmation (non-interactive run)

The following is exactly what I would say to the user. I cannot proceed past this
point without their answer, so I am stopping here rather than guessing.

---

Before I write the turret aiming subsystem, I hit a contradiction I can't resolve on my own.

Your confirmed config (team 99902) records **no shooter** (`shooter: none`). I updated it to
reflect the turret you added this week (`turret: single_axis`), then re-ran the validator, and it
blocked generation:

> mechanism constraint violated: a turret aims a shooter; a turret with no shooter is incoherent
> — requires season_mechanisms.shooter {"not": "none"}, config has 'none'

A single-axis turret rotates something to aim it. In DECODE that something is normally a shooter.
So one of these is true, and they generate very different code:

1. **You also added a shooter this week** (the usual reason to add a turret). If so, which type —
   `flywheel` or `elastic_catapult`? I'll record the shooter, re-confirm both fields, and then the
   aiming subsystem has an actual thing to aim.
2. **The turret aims something else** (e.g. a camera/sensor, not a shooter). If so, tell me what
   it carries — that may be outside the DECODE season mechanism set, and I don't want to model it
   as a shooter turret when it isn't.
3. **No turret was actually added / I misread the request.** Say so and I'll revert the config.

One more thing while the config is open: `software_stack.pathing` is still unconfirmed
(`confirmed: false`) from before. It's not blocking the turret question, but generation stays
blocked until it's confirmed too — is it `pedro_pathing`, `roadrunner`, `custom`, or `none`?

I have not written any turret code yet — a turret aiming subsystem that assumes a shooter which
may not exist is exactly the wrong-guess-that-compiles this step exists to prevent.

---

## Why this is a hard stop (not a judgment call)

- SKILL §7 "keep the config live": the request contradicts the recorded config (`turret: none`),
  so the turret field is re-opened before anything generates.
- SKILL §4 / standing-principles §4 "ask, don't guess": whether a shooter exists changes what code
  gets written, so it must be asked, not inferred.
- `validate_config.py` reports `generation_allowed: false` — generation is not permitted until the
  contradiction is resolved and the re-opened fields (`shooter`, and pre-existing `pathing`) are
  confirmed.
