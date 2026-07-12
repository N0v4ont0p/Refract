# Transcript Summary — source of each number

This is the "without_skill" run: I answered entirely from my own knowledge and did
mental arithmetic. I did **not** open any spec table, datasheet, or calculation
script. Below is an honest accounting of where each figure came from.

| Figure | Value used | Source |
|---|---|---|
| HD Hex Motor free speed | 6,000 RPM | Memory of REV HD Hex datasheet — not verified |
| HD Hex Motor stall torque | 0.105 N·m | Memory of REV HD Hex datasheet — not verified |
| HD Hex Motor stall current | ~11 A | Memory — not verified |
| Gear ratio | 20:1 | Given by user |
| Output free speed (6000 ÷ 20) | 300 RPM | Head math from the memory value above |
| "Real-world" 250–280 RPM | 250–280 RPM | Estimate / rule of thumb, not a source |
| Spur gear efficiency | 85–90% | Estimate / general knowledge, not verified |
| Theoretical stall torque (0.105 × 20) | 2.1 N·m | Head math |
| N·m → in-lb conversion (×8.85) | 18.6 in-lb | Head math, standard conversion |
| Realistic stall ~1.8–1.9 N·m | 1.8–1.9 N·m | Head math applying the estimated efficiency |
| "Design for 25–30% of stall" holding guideline | ~0.5 N·m | Rule of thumb / engineering judgment, not a source |
| Arm holding-torque formula (W × d) | — | Standard statics, from knowledge |

## Honesty notes / risk flags

- **No source was checked.** Every hardware constant (free speed, stall torque,
  current) is recalled from memory of the REV datasheet. These could be off. In
  particular I'm least confident on the exact stall-torque figure.
- The efficiency percentage and the "25–30% of stall for continuous holding"
  guideline are engineering rules of thumb I supplied, not looked-up values.
- I flagged in the answer that the 20:1 spur cartridge has its own **rated
  mechanical torque limit** which may be below the motor's output — I did not look
  up that number and told the user to verify it.
- The output speed (300 RPM) is the one figure I'm confident in, because it's just
  6000/20 and the ratio was user-given; its accuracy still depends on the free-speed
  value being correct.
