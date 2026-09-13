**Season:** BIOBUZZ 2026-27, the active season. The rules corpus is BIOBUZZ Competition Manual V1 through Team Update 00, and `check_freshness.py` says CURRENT (live TU 0 matches the stored TU 0).

## Verdict: I can't tell you which corner from the text I have. Check Figure 9-2 before you plan paths.

```json
{"verdict": "ambiguous — decided by a figure the corpus doesn't store (Figure 9-2 / 9-4 / 9-5)",
 "citations": [{"id": "G411", "text": "An ALLIANCE may not STRATEGICALLY prevent the opposing ALLIANCE from accessing SCORING ELEMENTS. Violation: MAJOR FOUL and YELLOW CARD per MATCH. An ALLIANCE using their own NECTAR and/or POLLEN for scoring is not a violation of this rule. Corralling relevant SCORING ELEMENTS into a limited portion of the FIELD and/or actively positioning a ROBOT to prevent opposing ALLIANCE access is a violation of this rule. A GARDEN is not a protected zone."}],
 "reasoning": "See below."}
```

**What the manual text says:**
- **Glossary (§16) and §9.3:** the GARDEN is "defined by the outside edge of blue or red tape in opposite corners of the FIELD, as shown in Figure 9-2." So the red and blue GARDENs sit in diagonally opposite corners. Which corner is red is only shown in Figure 9-2.
- **§10.3.1 setup:** "POLLEN in the GARDEN is placed in a line starting in the corner closest to the ALLIANCE AREA and contacting the audience or rear perimeter wall." That means the GARDEN touches the audience or rear wall and runs from a corner next to an ALLIANCE AREA. It doesn't say whether that's the red or the blue ALLIANCE AREA.
- The text is explicit for the LOADING ZONE, which "belong[s] to the ALLIANCE with the adjacent ALLIANCE AREA" (§9.3). There's no matching sentence for the GARDEN, so I can't carry the LOADING ZONE logic over.
- **Our season file** (`season-extensions/biobuzz-2026-27.yaml`) takes tile labels from the Event Field Setup Guide V1.0 §8.3-8.4. That's an official field document, not rule text. It lists red GARDEN at tile A1, blue at F6, red LOADING ZONE at A5 and blue at F2. Red GARDEN and red LOADING ZONE share letter A. But which way the A-F / 1-6 grid runs relative to the audience and the ALLIANCE AREAs is only drawn in the manual's tile-grid figures (Fig 9-4/9-5). I won't guess "near" or "far" from the labels alone. Getting the side wrong means a mirrored auto path.

**What to look at (live manual, §9.3):** in Figure 9-2, and Fig 9-4/9-5 for the tile grid, find:
1. Which corner has red GARDEN tape.
2. Whether that corner touches the red ALLIANCE AREA side or the blue one.
3. Whether it runs along the audience wall or the rear wall.
4. Which way the A-F and 1-6 labels run, so you can match A1 and A5 to real positions.

**Things that matter for auto planning (all from manual text):**
- **No GARDEN points in AUTO.** §10.5 item E says GARDEN scoring is assessed "at the end of TELEOP when all ROBOTS and SCORING ELEMENTS have come to rest." The season file only lists a TELEOP GARDEN value (1 point per element). Pushing elements into the GARDEN during AUTO only counts if they're still there at the end of the match.
- **Anyone can use either GARDEN.** A GARDEN scores for its own color "regardless of which ALLIANCE placed the POLLEN or NECTAR." §10.5.3 and G411 both say it "is not a protected zone," and either alliance can remove elements from it. Opponents can take elements out of your GARDEN.
- **4 POLLEN start in each GARDEN** (§10.3.1). Those can be targets for an auto path.
- **Careful with opponent NECTAR.** Our season file has an open Q&A item: §10.5.3 lets opponent NECTAR score in a GARDEN, but herding counts as CONTROL (§16) and G408 bans CONTROL of opponent NECTAR. I only verified G411 in this session, so treat the G408 point as a flag to check, not a ruling. Don't build a path that herds opponent NECTAR until that's answered.

**What I'd need from you** (no one was available to ask):
1. "Can you open Figure 9-2 in the live manual (§9.3) and tell me which corner the red GARDEN tape is in, relative to the red ALLIANCE AREA and the audience?" If you give me the corner, I'll re-check it against the §10.3.1 staging text and the A1/A5 labels, then give a firm near-side or far-side answer for red, and the mirror for blue.
2. "Which alliance and starting position is the path for?" If red, I'll give the GARDEN's position relative to your start. If blue, I'll use F6. Either way I'll flag that GARDEN points only count at the end of TELEOP.

Only one rule (G411) was cited, and `rules.py verify G411` passed. Everything else comes from manual sections (§9.3, §10.1, §10.3.1/10.3.2, §10.5, §10.5.3, §16), not rule numbers. Every rule involved is still at its base-manual version, with no Team Update changes.