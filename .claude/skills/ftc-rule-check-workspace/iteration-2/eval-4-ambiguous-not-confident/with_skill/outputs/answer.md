# Is it legal to spray mecanum wheels with silicone traction spray for extra grip?

**Short answer: No — don't do it. This reads as illegal, and the risk is not worth it.**

> **Corpus currency note:** The freshness check returned `UNVERIFIABLE` — the tool could not read a live Team Update number from the FIRST site to confirm my local copy is current. My corpus incorporates through **Team Update 32** for the DECODE 2025-26 season, retrieved 2026-07-03. The verdict below is grounded in that local snapshot; a newer Team Update could exist that I can't see. For a definitive ruling, confirm against the live manual and/or file an official Q&A. The rules this turns on (R205, R201, G412) are all base-manual rules, so they are unlikely to have changed — but I can't guarantee it.

---

## Verdict

```json
{
  "verdict": "illegal",
  "confidence": "high on the rule, with one honest gap (see below)",
  "citations": [
    {
      "id": "R205",
      "text": "ROBOTS may not contain any materials which if unintentionally released would damage the FIELD, other ROBOTS or delay the start of a MATCH due to required clean-up or decontamination. Lubricants may be used only to reduce friction within the ROBOT and must not contaminate the FIELD or other ROBOTS. Lubricants (e.g., grease) used on the ROBOT must not be excessively applied such that they spin off or drip off during normal ROBOT operations on the FIELD. Additional examples of items that will violate this rule include (but are not limited to): - any ballast not secured sufficiently, including loose ballast such as sand, coffee beans, kitty litter, or ball bearings, such that it may be released on the FIELD during a MATCH - liquid or gel materials - tire sealant, and - other lubricants including graphite powder"
    },
    {
      "id": "G412",
      "text": "A ROBOT may not damage FIELD elements. Violation: VERBAL WARNING. DISABLED if the Head REFEREE infers that additional damage is likely. YELLOW CARD for any subsequent damage during the event. Corrective action (such as eliminating sharp edges, removing the damaging MECHANISM, and/or re-inspection) may be required before the ROBOT will be allowed to compete in subsequent MATCHES. SCORING ELEMENT damage is specifically covered in G407 . G407 and G412 do not stack. G412 does not apply to damage caused by normal gameplay actions. FIELD damage includes, but is not limited to: - contaminating the FIELD with a liquid or fine solid as in R205 , - damaging TILE in R201 , - causing the GATE to bend or break off FIELD damage does not include: - normal GATE interaction resulting in a GATE that “sticks” open - normal interaction with the GOAL that causes it to lift off the TILES"
    },
    {
      "id": "R201",
      "text": "Traction devices must not have surface features which are known to damage the TILE floor. Traction devices are all parts of the ROBOT that are designed to transmit any propulsive and/or braking forces between the ROBOT and the FIELD. Examples of traction devices known to cause damage when used directly on TILE floors are high traction wheels (for example, AndyMark am-2256) and high grip tread (for example, Roughtop, AndyMark am-3309). While these (and other) COMPONENTS are not outright prohibited, e.g., used as part of an intake, MECHANISMS that involve these COMPONENTS contacting the TILE floor are not allowed."
    }
  ],
  "reasoning": "A traction spray is applied to the exact wheel surface that rides on the shared TILE field, so it is designed to sit where it will transfer onto the field during a MATCH. R205 prohibits ROBOTS from containing materials that, if released, would contaminate the FIELD or require clean-up/decontamination, and explicitly lists 'liquid or gel materials' and 'tire sealant' as violating examples. Its lubricant allowance is limited to reducing friction 'within the ROBOT' — a coating on the tile-contacting tread is the opposite of 'within the ROBOT.' G412 removes any doubt about how this is treated in-match: it names 'contaminating the FIELD with a liquid or fine solid as in R205' as FIELD damage, carrying a verbal warning, possible DISABLED, and a yellow card for repeats. The one honest gap: the manual never names 'silicone traction spray' by product, so this is a reading of the general contamination prohibition rather than a rule that calls it out by name — hence a Q&A gives 100% certainty. But the reading is straightforward and the downside is severe, so the safe and almost-certainly-correct answer is: do not do this."
}
```

---

## Why — in plain terms

The manual does not name "silicone traction spray" specifically, but it does not need to. The controlling idea in **R205** is: nothing on your robot may end up on the field. A traction spray is, by design, on the part of the wheel that touches the tiles — so it *will* transfer to the field surface every team shares. That is exactly the "contaminate the FIELD... required clean-up or decontamination" case R205 forbids. R205 even lists "liquid or gel materials" and "tire sealant" as example violations; a wheel-applied grip chemical is in that same family.

**R205's one allowance does not cover you.** Lubricants are permitted *only* "to reduce friction **within the ROBOT**." A coating on the outside tread that contacts the field is not "within the ROBOT," so the allowance does not apply.

**G412 shows the in-match consequence.** It explicitly defines "contaminating the FIELD with a liquid or fine solid as in R205" as FIELD damage: verbal warning, DISABLED if a referee thinks more damage is coming, and a yellow card for any repeat. So even setting inspection aside, using this in a match invites a penalty.

**R201 context (why the "extra grip" goal is itself risky):** the tile floor is protected. R201 already bans traction *surfaces* known to damage the tile (high-traction wheels, Roughtop tread) from contacting the floor. A chemical that alters the tile surface for grip runs against the same intent — keep the shared tiles unaltered.

## The one honest caveat

Because no rule names this product by name, I can't point to a line that says "silicone traction spray is banned" in those words. My verdict rests on R205's general contamination prohibition plus G412. That reading is strong and I'm confident in it — but if you want a black-and-white official answer for your inspector, **file an FTC Q&A** ("May we apply a silicone traction spray to our drive wheels?"). Q&A is clarification, not rule text, but it will tell you how officials will call it. Until then, treat it as not allowed.

## What to do instead for grip

Grip on the tiles is a legal design problem, not a chemistry one:
- Use compliant wheels/tread rated for the tile that don't damage it (stay clear of the R201 examples on the floor).
- Tune wheel durometer, tread pattern, and weight distribution.
- For mecanum specifically, verify roller condition and even weight over all four wheels before reaching for a spray.

**Bottom line: skip the spray. It reads as an R205 violation, it's callable as FIELD damage under G412 in a match, and it can get your robot flagged at inspection or DISABLED in play — all to solve a grip problem you can solve legally through wheel and weight choices.**
