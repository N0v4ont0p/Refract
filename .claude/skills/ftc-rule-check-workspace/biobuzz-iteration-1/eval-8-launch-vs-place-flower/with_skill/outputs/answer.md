**Season:** BIOBUZZ 2026-27, which is the ACTIVE season. The corpus is the BIOBUZZ Competition Manual V1 with Team Updates through TU 00. `check_freshness.py` returned CURRENT (stored TU 0, live TU 0), so there's no staleness caveat.

## Short answer: unclear. Build it only if you can drop to placing, and file a Q&A.

Nothing in the manual clearly bans shooting POLLEN into a FLOWER. But the manual's scoring section says placing is the only allowed way to score there. I can't settle that conflict from the text, so the honest answer is "ambiguous." I'm not going to guess "legal."

```json
{
  "verdict": "ambiguous — worth filing a Q&A",
  "citations": [
    {"id": "G418", "text": "ROBOTS may not enter SCORING ELEMENTS into or remove SCORING ELEMENTS from a FLOWER except: A. only enter POLLEN and NECTAR into the top of a FLOWER, and B. only remove POLLEN from the bottom of a FLOWER. Violation: VERBAL WARNING. MAJOR FOUL and YELLOW CARD per MATCH, if STRATEGIC. The FLOWERS are designed and intended to only allow POLLEN and NECTAR to enter through the top of the top ring and only allow POLLEN (not NECTAR) to be removed from the bottom of the middle ring. Any other actions to score or remove SCORING ELEMENTS from the FLOWER are considered a violation of this rule. The intent is not to disallow ROBOTS from contacting the FLOWER or interactions that occur when attempting allowed scoring actions. Examples of ROBOT actions that are not violations of this rule include: A. contacting the FLOWER while attempting to enter or remove SCORING ELEMENTS, B. contacting POLLEN or NECTAR scored in a FLOWER while attempting to score, or C. driving into a FLOWER and contacting the POLLEN or NECTAR inside it. Examples of actions that are likely to be perceived as STRATEGIC include, but are not limited to: D. A ROBOT attempts to pull POLLEN through the side of the FLOWER, E. A ROBOT grabs onto the FLOWER and shakes it, F. A ROBOT forces NECTAR out of the middle ring with a MECHANISM, G. A ROBOT deliberately drives into the perimeter wall at high-speed causing a SCORING ELEMENT to fall out of a FLOWER, or H. A ROBOT deliberately holds a NECTAR up to the side of the FLOWER pipes such that it meets the FLOWER scoring criteria. Examples of actions that are likely to not be perceived as STRATEGIC include but are not limited to: I. A ROBOT drives into a FLOWER while attempting to pick up POLLEN off the TILES and causes a POLLEN to fall out the top of a FLOWER, or J. A ROBOT knocks out a scored POLLEN while attempting to score another POLLEN."},
    {"id": "G410", "text": "ROBOTS may not enter NECTAR into the FLOWER scoring volume until the last 60 seconds of the MATCH. Violation: MAJOR FOUL per NECTAR. See Section 10.5.2 FLOWER Scoring Criteria for details on the FLOWER scoring volume. The primary FIELD timer display is the cue to indicate when there is 60 seconds left in the MATCH. Teams are encouraged to make it obvious and unambiguous to REFEREES that they are not placing NECTAR into a FLOWER too early."},
    {"id": "G417", "text": "ROBOTS may not manipulate the motion of the HIVE in any way other than by LAUNCHING SCORING ELEMENTS into an upward-facing CELL. Violation: VERBAL WARNING. MAJOR FOUL and YELLOW CARD per MATCH, if STRATEGIC. HIVES are designed and intended to only have a TIP induced by LAUNCHING POLLEN and NECTAR into an upward-facing CELL. Any other interaction with the HIVE that causes or could cause or impeding a TIP is a violation of this rule. Examples of ROBOT actions that are likely to be perceived as STRATEGIC include, but are not limited to: A. ramming into the HIVE frame at high-speed, B. ramming into the HIVE frame multiple times in a short time period, C. deliberately LAUNCHING NECTAR or POLLEN into the external bottom, sides, or top faces of a CELL, D. impeding the TIP of an opponent’s HIVE by LAUNCHING NECTAR or POLLEN at it, E. contacting a HIVE directly or transitively through a CONTROLLED SCORING ELEMENT, or F. actions that are REPEATED after a warning has been given. Examples of actions that are likely to not be perceived as STRATEGIC include, but are not limited to: G. A ROBOT accidentally bumping into a HIVE frame while attempting to pick up POLLEN, or H. A ROBOT attempting to LAUNCH POLLEN or NECTAR into the upward-facing CELL and missing in a way that hits the bottom, sides, or top of the CELL."}
  ],
  "reasoning": "See below."
}
```

### The case that shooting is allowed
- **G418** is the only in-match rule about putting things into a FLOWER. It limits *where* elements go in ("only enter POLLEN and NECTAR into the top of a FLOWER"). It says nothing about *how* they get there.
- **LAUNCH/LAUNCHING** is a defined term: "an action by a ROBOT in which the SCORING ELEMENT is shot into the air, propelled across the floor…, or thrown in a forceful way". No rule in the corpus bans LAUNCHING into a FLOWER.
- The only rule that bans LAUNCHING outright is T405, and it covers field measurement time, not matches.

### The case against it
- **§10.5.2, FLOWER Scoring Criteria** (manual body, not a numbered rule): "Placing SCORING ELEMENTS into the top of the FLOWER is the only allowable way to score. ROBOTS must follow G418 while interacting with the FLOWER."
- **Glossary, FLOWER:** "a structure on the FIELD in which POLLEN and NECTAR can be placed into the top".
- **The manual keeps the two verbs apart.** The HIVE gets "LAUNCHING", the FLOWER gets "placing":
  - §8: "LAUNCHING them into their HIVE and placing them into FLOWERS"
  - §10.1: "to place into the FLOWERS, and to LAUNCH them into their CELLS"
  - §10.5.1: "LAUNCHING into the upward-facing CELL is the only allowed way to earn a HIVE TIP"
  - §10.5.2: "Placing … is the only allowable way to score"

  The "only allowed way" sentences for the HIVE and the FLOWER mirror each other, and they use different verbs.

### Why I can't pick a side
- "placing" is lowercase, so it isn't a defined term. Read in the everyday sense, that sentence may only be stressing "into the top" over the side or bottom, which is what G418 is about.
- Read as the opposite of the defined term LAUNCHING, it would ban shooting.
- The manual text doesn't decide between these readings. The corpus has no official Q&A on it, and even a Q&A would only clarify the rule, not replace it.

### What's at risk
- G418 goes from a VERBAL WARNING to a MAJOR FOUL plus a YELLOW CARD per MATCH if the referee sees it as STRATEGIC. A launcher built to score FLOWERS every match is a planned strategy, so a referee who reads "placing" strictly is likely to call it STRATEGIC.
- G417 has a safe harbour for missed HIVE shots (example H). **G418 has no such example for missed FLOWER shots.** A shot that misses and goes in through the side of the FLOWER isn't covered by anything that excuses it.

### Other rules that apply whichever reading wins
- **Timing:** §10.5.2 says FLOWER scoring can't begin until one minute remains, citing G410. Early scores still count but can be penalised. G410 itself only mentions NECTAR (a MAJOR FOUL per early NECTAR).
- **Where a shot counts:** a ball scores if it is at least partly inside the FLOWER scoring volume, which is the space between the top ring and the middle ring. That space is defined by CAD Reference 10-4, and the corpus stores text only, not figures. Whether a shot that bounces or sits high counts depends on that CAD volume, so check CAD 10-4 directly.
- **Knock-outs:** knocking out an already-scored POLLEN while trying to score another is listed as not STRATEGIC (G418 example J).

### What to do
1. File a Q&A worded like this: "Does §10.5.2's 'Placing SCORING ELEMENTS into the top of the FLOWER is the only allowable way to score' prohibit LAUNCHING POLLEN into the top of a FLOWER, given G418 only restricts entry to the top?"
2. Until you get an answer, plan to score FLOWERS by placing. If you still want the launcher, make sure it can also run as a low-speed drop from just above the top ring. That keeps you on the safe reading.
3. Recheck after each Team Update. This verdict reflects TU 00 only.

All four cited rule numbers (G418, G417, G407, G410) exist in the BIOBUZZ manual (`rules.py verify`: all_valid true). G407 isn't quoted above; it only says that a launched element no longer touching the robot doesn't count toward the 4-element CONTROL limit.

### Questions I'd ask you (no human was available)
1. **How does the ball get into the FLOWER: a real shot through the air from a distance, or a gentle drop from a mechanism held just above the top ring?**
   - If it's a drop, it's much closer to "placing." I'd say it's likely fine under G418 and still suggest a Q&A to confirm.
   - If it's a real shot, the verdict stays ambiguous and I'd say don't rely on it without a Q&A answer.
2. **Has your team or anyone else already had an official Q&A answer on launching into FLOWERS?**
   - If yes, send me the text. I'd present it as a clarification, not the rule, and revise the verdict only if it clearly settles "placing" versus LAUNCHING.
   - If no, go ahead and file the Q&A in step 1.
3. **Is this for NECTAR too, or only POLLEN?**
   - If NECTAR is included, G410's one-minute rule (a MAJOR FOUL per early NECTAR) also applies to every NECTAR shot, so I'd add that timing constraint to the recommendation.