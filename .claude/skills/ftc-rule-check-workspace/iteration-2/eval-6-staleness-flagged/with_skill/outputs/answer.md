# Is our 18-inch robot still legal?

**Short answer: Yes — an 18-inch robot is legal at the start of a match — but with an important freshness caveat you flagged correctly. Read the caveat below before you treat this as final.**

## Verdict (from the local rules corpus): LEGAL

An 18-inch robot in its STARTING CONFIGURATION is legal, because the rule requires the robot to fit *within* an 18-inch cube, and 18 inches is the allowed maximum (inclusive), not a value you must stay under.

**R101 — STARTING CONFIGURATION is limited to an 18-inch Cube** (effective: base-manual)
> "In the STARTING CONFIGURATION (the physical configuration in which a ROBOT starts a MATCH), the ROBOT must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. (45.70 cm) long, by 18 in. (45.70 cm) high volume. The only exception is that: A. pre-loaded SCORING ELEMENTS may extend outside the starting size constraint. If a ROBOT uses interchangeable MECHANISMS per I304, teams should be prepared to show compliance with this rule and R105 in all configurations."

Two things that "18 inches" alone doesn't settle, so check them before you call it done:

- **It must actually *fit within* 18 in., measured at inspection.** An 18.0 in. robot is legal only if it truly measures 18 in. or less on every axis — no bumpers, fasteners, wire loom, or decorations pushing any dimension past 18. Build to 18 and you have zero margin; inspectors measure the real thing.
- **Expansion is a separate limit (R105 / G414 / G415).** Starting at 18 in. is fine, but once the match starts your horizontal footprint must stay within a fixed 18 in. × 18 in. (R105.A, enforced by G414). Vertical may go to 18 in. generally, or up to 38 in. under the G415 conditions. If your 18-inch robot has an arm/intake that pushes the *horizontal* envelope past 18 in. at full mechanical extension, that's the illegal part — not the starting size.

**R105 — There are expansion limits** (effective: base-manual)
> "After the MATCH has started, ROBOTS may expand beyond the STARTING CONFIGURATION but are still subject to sizing constraints... A. ...ROBOTS may expand horizontally but must remain within a fixed 18 in. (45.70 cm) by 18 in. (45.70 cm) when fully expanded per G414. ROBOTS must be physically constrained to fit within these horizontal limits without the use of software. B. ...vertically up to 18 in. (45.70 cm)... C. Within the limitations per G415, ROBOTS may expand vertically up to 38 in. (96.50 cm)..."

## Freshness caveat — you were right to raise this

Your instinct that our rules data might be behind is correct. Our local rules corpus incorporates Team Updates **through TU 32**. The live manual is at **TU 34**, so **TU 33 and TU 34 are NOT in our data** (freshness check reported `STALE`).

- The 18-inch cube rule (R101) is a foundational sizing rule and, in our corpus, has **not** been touched by any Team Update (it's still `base-manual`) — it has been stable all season.
- **But I can't see TU 33 or TU 34.** I have no basis to claim they changed R101, and historically this rule doesn't move — but I also can't *guarantee* it wasn't touched. So treat the LEGAL verdict as "correct as of TU 32, and almost certainly still correct, but not confirmed against the two newest updates."

**What to do:** Before you rely on this at an event, spend 30 seconds confirming against the live manual — check R101 and R105 in the current DECODE Competition Manual and skim the TU 33 and TU 34 change lists for anything touching robot size or expansion:
https://ftc-resources.firstinspires.org/ftc/game/cm-html

If R101 still reads "18 in. cube" there (it almost certainly does), you're clear.

## Citations verified
R101, R105, G414, G415 — all confirmed to exist in the manual (`rules.py verify`, all_valid: true).
