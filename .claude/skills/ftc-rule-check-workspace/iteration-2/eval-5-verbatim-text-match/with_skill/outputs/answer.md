# Do we have to display our team number on the robot?

**Short answer: Yes — and it's a hard inspection requirement, not optional.** Your team number must be displayed on ROBOT SIGNS, you need at least **two** of them on the robot, and they have specific size/color/material rules. Skipping or getting this wrong is exactly the kind of thing that gets caught at inspection.

> ⚠️ **Currency flag:** The freshness check came back `UNVERIFIABLE` — the tool could not read a live Team Update number from the FIRST site to confirm my local corpus is the newest. My data incorporates **Team Update 32** for the DECODE 2025-26 season (retrieved 2026-07-03). All the rules below are `base-manual` (none were changed by a Team Update in my snapshot), so this is very likely still current — but confirm against the live manual at https://ftc-resources.firstinspires.org/ftc/game/cm-html before your event, since I can't guarantee no newer update exists.

## What you actually need to do (plain-language)

1. **At least 2 ROBOT SIGNS**, on opposite or adjacent surfaces ≥90° apart, viewable by field staff from 12 ft away (R401).
2. Each sign has a **solid red OR blue rectangle** (≥6.5 in × 2.5 in) showing your alliance color — reversible/swappable is fine as long as the wrong color is never showing (R402).
3. Your **team number in solid white Arabic numerals, 2.25 in ±0.5 in tall**, on that sign, not vertically stacked, not powered/LED (R403).
4. During play, your number and alliance color must **not become unreadable** — if a sign falls off or gets covered, that's a penalty (G411).

Signs made of robust material (acrylic, laminated paper, wood, metal; vinyl/mailbox numbers are fine). No edge-lit engraved plastic, no LED-display numbers.

---

## Structured verdict

```json
{
  "verdict": "illegal (to run WITHOUT a displayed team number) — displaying it is mandatory",
  "citations": [
    {
      "id": "R403",
      "text": "Team numbers must be displayed and positioned on the ROBOT SIGN as shown in Figure 12-3, Figure 12-6, and Figure 12-7 and meet the following additional criteria: A. consist of solid opaque white Arabic numbers (e.g., 1,2,3,4) which are 2.25 in. +/-0.5 in. (5.70 cm +/- 1.25 cm) tall, B. there must be a minimum of 0.25 in. (0.60 cm) of background surrounding the numbers, C. numbers may not be vertically stacked (Figure 12-7), D. be made of robust materials, and E. cannot be powered or rely on power from any sources to illuminate/reveal numbers. Figure 12-6: Legal number for team 21001 playing on the blue ALLIANCE Figure 12-7: Team number orientation examples for team 1355 playing on the blue ALLIANCE If a team at an event does not have completely legal ROBOT SIGNS, and there is no color printer or other means available at the event to create a legal ROBOT SIGN, the Head REFEREE may approve an alternate substitute for use at the event. Team numbers must be robust enough to withstand the rigors of MATCH play. Example robust materials include: - self-adhesive numbers (mailbox or vinyl numbers) - ink jet or laser printed numbers on paper and laminated or protected from ROBOT-to-ROBOT interaction. Examples of prohibited team numbers on ROBOT SIGNS include but are not limited to: - team numbers only visible by edge lit engraved plastic - LED Display numbers 12.5 Motors & Actuators"
    },
    {
      "id": "R401",
      "text": "ROBOT SIGNS must be placed in at least 2 separate locations on the ROBOT. These locations must be on opposite or adjacent surfaces of the ROBOT, ≥90 degrees apart. All ROBOT surfaces visible to FIELD STAFF can be used for placing ROBOT SIGNS including the top of the ROBOT. ROBOT SIGNS must meet the following criteria: A. be made of a robust material, B. minimally be 6.5 inches (16.5 cm) wide, C. minimally be 2.5 inches (6.4 cm) tall (Figure 12-3), and D. be supported by the structure/frame of the ROBOT. The intent of this rule is for FIELD STAFF to easily view ROBOT SIGNS from at least 12 feet (3.65 meters) away before, during, and after the MATCH. Examples of robust materials that satisfy this rule include, but are not limited to, acrylic, plastic laminated paper, wood, and metal. ROBOT SIGNS must be designed to withstand vigorous game play. Figure 12-3: Team Number ROBOT SIGN Sizing"
    },
    {
      "id": "R402",
      "text": "Each ROBOT SIGN must contain a rectangle with a solid red or blue opaque background at least 6.5 in. by 2.5 in. (16.50 cm by 6.35 cm) in size to indicate their ALLIANCE color (Figure 12-3), as assigned in the MATCH schedule at the event. Visible markings on ROBOT SIGNS when installed on the ROBOT, other than the following, are prohibited: A. those required per R403 , B. solid white FIRST logos no larger than 1.5 in. (3.80 cm) in height (Figure 12-5), C. small amounts of hook-and-loop tape, hard fasteners, or functional equivalents, D. narrow areas of differing colors exposed at corners, folds, or cutouts, E. dark narrow markings on background solely for template purposes, and F. cannot be powered or rely on power from any sources to illuminate/reveal ALLIANCE color. ROBOT SIGNS that are reversible or configurable must not allow the opposite ALLIANCE color to be visible to FIELD STAFF, except where permitted by this rule. Figure 12-4: Minimum sized ALLIANCE rectangle Figure 12-54: Legal team number display for team 117 playing on the red ALLIANCE"
    },
    {
      "id": "G411",
      "text": "A ROBOT’S team number and ALLIANCE color must not become indeterminate by determination of the Head REFEREE. Violation: VERBAL WARNING. MINOR FOUL if subsequent violations occur during the event. Teams are encouraged to robustly affix their ROBOT SIGNS to their ROBOT in highly visible locations such that they do not easily fall off or become obscured during normal gameplay."
    },
    {
      "id": "G303",
      "text": "A ROBOT must meet all following MATCH-start requirements: A. does not pose a hazard to humans, FIELD elements, or other ROBOTS. B. has passed inspection, i.e., it is compliant with all ROBOT rules . C. if modified after initial Inspection, it is compliant with I305 . D. is the only team-provided item left in the FIELD. E. ROBOT SIGNS must indicate the correct ALLIANCE color (see R402 ). F. ROBOT must be motionless following completion of OpMode initialization. If a ROBOT is DISABLED prior to the start of the MATCH, the DRIVE TEAM may not remove the ROBOT from the FIELD without permission from the Head REFEREE or the FTA. For assessment of many of the items listed above, the Head REFEREE is likely to consult with the LRI. Violation: The MATCH will not start until all requirements are met if there is a quick remedy. DISABLED if it is not a quick remedy, and, at the discretion of the Head REFEREE, ROBOT must be re-inspected. RED CARD if a team’s ROBOT is not compliant with part B or C participates."
    }
  ],
  "reasoning": "The direct answer lives in R403: team numbers 'must be displayed and positioned on the ROBOT SIGN' — mandatory language, with concrete criteria (solid white Arabic numerals 2.25 in ±0.5 in tall, 0.25 in background margin, not vertically stacked, robust material, not powered/LED). R403 does not stand alone: R401 (found via the one-hop cross-reference from R402) requires at least TWO ROBOT SIGNS on opposite/adjacent surfaces ≥90° apart, visible from 12 ft, so 'display' means on two robust signs, not one sticker. R402 requires each sign to carry the alliance-color rectangle and lists what other markings are allowed — it cites R403 for the number itself. The inspection/penalty teeth: G303 makes passing inspection (compliance with all ROBOT rules, which includes R401-R403) a MATCH-start requirement, and G411 makes the number/alliance-color going indeterminate during play a VERBAL WARNING escalating to MINOR FOUL. So NOT displaying the team number is non-compliant at inspection and puts you at risk of a red card / not starting the match. Verdict is that displaying the team number is mandatory; running without it is illegal. All five cited rules verify as existing (rules.py verify: all_valid=true) and all carry effective_date 'base-manual' — none was altered by a Team Update in the local corpus. Confidence is high on the rule content; the only caveat is corpus currency (freshness UNVERIFIABLE), flagged above."
}
```

## Bottom line for inspection

You will get dinged if the team number is missing, on only one sign, too small, wrong color background, stacked vertically, or an LED/edge-lit display. Build two robust signs, white numbers ~2.25 in tall on a solid red-or-blue rectangle, mount them ≥90° apart and high enough that a ref can read them from across the field. Do that and this line item is a non-issue.
