# Will a 19-inch-wide robot pass inspection?

**Short answer: No — that's a problem.** A 19 in. wide robot in its starting
configuration is over the hard 18 in. limit and would fail inspection / not be
allowed to start the match. You need to get it inside 18 in. before you go.

> **Currency caveat:** The freshness check came back `UNVERIFIABLE` — I could not
> confirm against the live FIRST manual page that no newer Team Update exists. The
> local corpus incorporates through **Team Update 32** (retrieved 2026-07-03). The
> 18-inch starting-size limit is a long-standing base-manual rule and is extremely
> unlikely to have changed, but double-check the live manual to be safe.

## Structured verdict

```json
{
  "verdict": "illegal",
  "citations": [
    {
      "id": "R101",
      "text": "In the STARTING CONFIGURATION ( the physical configuration in which a ROBOT starts a MATCH ), the ROBOT must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. (45.70 cm) long, by 18 in. (45.70 cm) high volume. The only exception is that: A. pre-loaded SCORING ELEMENTS may extend outside the starting size constraint. If a ROBOT uses interchangeable MECHANISMS per I304 , teams should be prepared to show compliance with this rule and R105 in all configurations."
    },
    {
      "id": "R105",
      "text": "After the MATCH has started, ROBOTS may expand beyond the STARTING CONFIGURATION but are still subject to sizing constraints relative to the ROBOT, based on the initial STARTING CONFIGURATION. The sizing constraints are: A. After the start of the MATCH, ROBOTS may expand horizontally but must remain within a fixed 18 in. (45.70 cm) by 18 in. (45.70 cm) when fully expanded per G414 . ROBOTS must be physically constrained to fit within these horizontal limits without the use of software. B. After the start of the MATCH, ROBOTS may expand vertically up to 18 in. (45.70 cm). ROBOTS may be physically constrained or software limited to fit within this vertical limit. C. Within the limitations per G415 , ROBOTS may expand vertically up to 38 in. (96.50 cm). ROBOTS may be physically constrained or software limited to fit within this vertical limit. Figure 12-1: Horizontal Expansion Limit Figure 12-2: Vertical Expansion Limit Examples Any extension beyond the maximum expansion limit during ROBOT operation is considered a violation of this rule. This includes flexible extensions (e.g., surgical tubing flappers, star intakes) that cause the ROBOT to exceed the expansion limit. Teams should be prepared to show compliance with this rule and demonstrate their ROBOT expansions during the inspection process. During inspection, each team will be asked to show the ROBOT’S STARTING CONFIGURATIONS and additionally its configurations at maximum mechanical (horizontal) extensions and mechanical/software (vertical) extensions. Software limits are not sufficient to demonstrate maximum extensions for horizontal expansion. ROBOTS must show their maximum mechanical extensions during the inspection process. A ROBOT that can mechanically exceed the horizontal limit would be in violation even if the ROBOT has software limiting the position of the extension during the MATCH. A ROBOT with a single mechanism that can extend out of both sides of a ROBOT would be allowed as long as the overall horizontal dimension at maximum mechanical extension does not exceed 18 in. A ROBOT with multiple mechanisms that are not mechanically linked that can extend out of both sides of a ROBOT simultaneously would NOT be allowed if the overall horizontal dimension at maximum mechanical extension exceeds the 18 in. limit. At maximum extension, a ROBOT in compliance will not exceed the maximum allowable vertical extension of 38 in. (96.50 cm) in one direction while maintaining the horizontal expansion requirements of 18 in. (45.70 cm) length and width perpendicular to the vertical height. Teams are responsible for maintaining compliance with expansion limits and subject to penalties listed in G414 and G415 for any violations during the MATCH. 12.2 ROBOT Safety & Damage Prevention"
    },
    {
      "id": "G304",
      "text": "A ROBOT must be positioned on the FIELD such that it meets all of the following requirements: A. is over a LAUNCH LINE, B. is either touching its own ALLIANCE’s GOAL or the FIELD perimeter, C. is fully contained on its own ALLIANCE’s side of the FIELD (FIELD columns A, B, C for blue, or FIELD columns D, E, F for red) ( Figure 9-4), D. not attached to, entangled with, or suspended from any FIELD element, E. confined to its STARTING CONFIGURATION (see R101 and R102 ), and F. in contact with no more than the allowed pre-load possession limit as described in section 10.3.1 SCORING ELEMENTS . Violation: The MATCH will not start until all requirements are met if there is a quick remedy. DISABLED if it is not a quick remedy. G304 . C requires the ROBOT to be fully contained within the FIELD perimeter and not overhang the FIELD perimeter wall. Figure 11-1 shows examples of several possible legal ROBOT starting locations. Figure 11 - 1 : Examples of allowed ROBOT starting locations"
    },
    {
      "id": "I304",
      "text": "At the time of inspection, the OPERATOR CONSOLE and the ROBOT with battery must be presented with all MECHANISMS (including all COMPONENTS of each MECHANISM), configurations, and decorations that will be used on the ROBOT in MATCHES without re-inspection per I305 . A. ROBOTS are allowed to play MATCHES with a subset of the mechanisms that were present during inspection. Only mechanisms that were present during inspection may be added, removed, or reconfigured between MATCHES. The ROBOT should be assembled in a typical configuration used for MATCH play when reporting for inspection. ROBOT and all mechanisms must be inspected in every STARTING CONFIGURATION. B. If MECHANISMS are swapped out between MATCHES, the reconfigured ROBOT must still meet all rules. C. The total of all electronics (motors, servos, Android Devices, etc.) used to build all mechanisms and base ROBOT, whether they are used on the ROBOT at the same time or not, may not exceed the constraints specified in section 12 ROBOT Construction Rules (R) ."
    }
  ],
  "reasoning": "R101 requires the ROBOT to be fully self-contained within an 18 in. x 18 in. x 18 in. volume in its STARTING CONFIGURATION — the configuration it is in on the field right before the match starts, exactly the situation described. 19 in. wide exceeds the 18 in. width limit, so the robot is out of spec by ~1 in. The only R101 exception is pre-loaded SCORING ELEMENTS extending past the box, which does not cover robot structure. I304 requires the ROBOT to be presented and inspected in every STARTING CONFIGURATION, so an oversized starting box is caught at inspection, not just at match time. G304.E independently requires the robot to be confined to its STARTING CONFIGURATION when set up on the field; its violation clause means the match will not start until remedied, and DISABLED if it is not a quick remedy. R105 (the after-start expansion limits) does not help — it caps expansion at the SAME 18 in. horizontal footprint, so there is no configuration in which 19 in. wide is legal. Verdict: illegal."
}
```

## What this means for you

- **You will not pass size inspection at 19 in. wide.** The starting box is a hard
  18 in. cube (R101). 19 in. is about 1 in. (2.5 cm) over on width.
- It is not just an inspection problem: even if you somehow got to the field, G304.E
  means the referee won't start the match until you're confined to the legal
  starting configuration.
- Expanding after the match starts doesn't save you either — R105 keeps the
  horizontal footprint locked at 18 x 18 in.
- The one R101 exception (pre-loaded scoring elements poking out of the box) is about
  game pieces, not your robot's frame, so it doesn't apply to a 19 in. chassis.

**Fix before you go:** trim the width down so the whole robot fits inside 18 in.
Measure with the frame in its true starting configuration (bumpers, any pre-set
mechanisms, everything), and give yourself a little margin — inspectors use a
sizing tool and there's no rounding in your favor. Also confirm you're still inside
18 in. long and 18 in. high.
