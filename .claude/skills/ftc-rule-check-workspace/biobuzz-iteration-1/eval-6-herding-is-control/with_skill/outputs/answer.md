**No. If you push a pile of 6 POLLEN across the field on purpose, that breaks G407. The manual's word "bulldozing" doesn't mean what you mean by it.**

Season: BIOBUZZ 2026-27, checked against Competition Manual V1 plus Team Update 00. The freshness check says the rules on file match the latest Team Update, so no warning about outdated rules.

**Why picking them up doesn't matter:** in BIOBUZZ, you don't have to pick an element up to CONTROL it. The glossary definition of CONTROL (quoted exactly) includes a robot that:
> "intentionally pushes a SCORING ELEMENT to a desired location or in a preferred direction (i.e., herding)"

It also says CONTROL "requires contact with a ROBOT, either directly or transitively through other SCORING ELEMENTS", and typically applies when "The ROBOT is moving the SCORING ELEMENT in a preferred direction with a flat or concave face of the ROBOT". The front of a drivetrain is a flat face. Balls pushed by other balls in the pile count too. So all 6 POLLEN (a SCORING ELEMENT) are CONTROLLED.

**Verdict:**
```json
{"verdict": "illegal",
 "citations": [
  {"id": "G407", "text": "A ROBOT may not simultaneously CONTROL more than 4 SCORING ELEMENTS. Violation: VERBAL WARNING. MAJOR FOUL and YELLOW CARD per MATCH, if STRATEGIC. The intent of this rule is that ROBOTS play MATCHES while only CONTROLLING a maximum of 4 SCORING ELEMENTS at a time. ROBOTS that CONTROL 5 or more SCORING ELEMENTS at any time during the MATCH will be under scrutiny to determine whether it is STRATEGIC. Examples of actions that are likely to be perceived as STRATEGIC include, but are not limited to: A. A ROBOT that picks up and CONTROLS 6 or more SCORING ELEMENTS, moving them to a scoring location. B. Multiple instances of greater than MOMENTARY CONTROL of 5 or more SCORING ELEMENTS by a ROBOT throughout a MATCH. Examples of actions that are likely to not be perceived as STRATEGIC include, but are not limited to: C. A ROBOT MOMENTARILY CONTROLS 5 SCORING ELEMENTS which they “reverse” quickly so that at least one SCORING ELEMENT returns to approximately its original state. Teams are encouraged to design their ROBOTS to prevent inadvertent or deliberate CONTROL of more than 4 SCORING ELEMENTS. This could involve guards to prevent SCORING ELEMENTS from accidentally becoming stuck on top of the ROBOT and systems to prevent active pickup/intaking of more than 4 SCORING ELEMENTS. Examples of interaction with a SCORING ELEMENT that are not “CONTROL” and would not be a violation of this rule include, but are not limited to: D. “bulldozing” (inadvertent contact with a SCORING ELEMENT while in the path of the ROBOT moving about the FIELD) E. “deflecting” (being hit by a SCORING ELEMENT that bounces into or off a ROBOT), or F. SCORING ELEMENTS that have been LAUNCHED by a ROBOT that are no longer in contact with the ROBOT."}
 ],
 "reasoning": "Intentionally pushing 6 POLLEN across the field is herding, which the glossary defines as CONTROL, so the robot is CONTROLLING 6 SCORING ELEMENTS, over G407's limit of 4. G407's 'bulldozing' exception (item D) only covers inadvertent contact with elements that happen to be in the robot's path, not a deliberate push. A planned push to gain position or points meets STRATEGIC ('actions done with the aim of gaining a competitive advantage'), and a push across the field lasts longer than MOMENTARY (under about 3 seconds). That is the pattern the rule lists as likely STRATEGIC (items A and B)."}
```

**What it costs you:**
- **Penalty:** a verbal warning at minimum. If the refs judge it STRATEGIC, which a planned push across the field almost certainly is, it's a MAJOR FOUL and a YELLOW CARD per match.
- **Example A** in the rule mentions "picks up", but the glossary definition of CONTROL includes herding. So not picking them up doesn't get you out of it.

**What's legal:**
- Push **4 or fewer** POLLEN at a time.
- Contact that really is accidental while you drive (the manual's "bulldozing") is fine.
- Touching 5 for less than about 3 seconds and quickly backing off so at least one ball returns to roughly where it was (item C) is not likely to be seen as STRATEGIC. Don't build a strategy on that.
- G407 suggests adding guards so extra elements can't pile up against the robot.

**Related rule, G411 ("Do not hoard SCORING ELEMENTS"):** if the goal is to push a pile into a corner or away from the other alliance, this rule also applies. Quoted exactly: "Corralling relevant SCORING ELEMENTS into a limited portion of the FIELD and/or actively positioning a ROBOT to prevent opposing ALLIANCE access is a violation of this rule." The penalty is a MAJOR FOUL and a YELLOW CARD per match. Moving your own POLLEN to score doesn't break this rule. G411 isn't part of the verdict above; it only matters if your plan is to keep the other alliance away from the POLLEN.

**Checks:** G407 and G411 both exist in the BIOBUZZ manual, confirmed by the citation check. Neither has been changed by a Team Update. The CONTROL, STRATEGIC and MOMENTARY definitions come straight from the manual's glossary. This is manual rule text, not an official Q&A answer.