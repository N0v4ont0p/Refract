# Transcript summary — provenance of each number

Task constraint: answer directly, no skills, no SKILL.md, no lookup tool. So every hardware number below came from my own memory, NOT from a verified source or catalog file. I did not read any spec table or fetch the goBILDA page.

| Value | Source | Confidence |
|-------|--------|-----------|
| Free speed 312 RPM (19.2:1) | Memory (recalled goBILDA spec) | Fairly high, but unverified |
| Base motor encoder 28 CPR (7 × 4 quadrature) | Memory | High — this is the standard 5203/5202 bare-motor value |
| Output encoder 537.7 CPR | Memory; also cross-checked arithmetically (28 × 19.2 = 537.6, goBILDA publishes 537.7 due to exact gear tooth counts) | Medium-high, unverified against source |
| Wheel circumference 301.6 mm | Computed by me: π × 96mm = 301.59 mm | High (pure math) |
| Ticks/mm ≈ 1.783 | Computed by me: 537.7 / 301.6 | High (pure math, but inherits the 537.7 assumption) |

## Honesty notes
- I did NOT check the ftc-hardware-lookup skill's spec tables or any datasheet — the task forbade it. In a real session those numbers should come from the structured table, not memory.
- I flagged this limitation explicitly in the answer and told the user to confirm 537.7 against the goBILDA listing for part 5203-2402-0019 before locking odometry constants.
- I added the direct-drive assumption caveat (537.7 only holds if the wheel is on the output shaft with no further reduction) and a note that dead wheels are usually preferred over drive-encoder odometry — these are reasoning/engineering-judgment additions, not looked-up facts.
- Risk: if my recalled 537.7 / 312 RPM were slightly off, the answer would be confidently wrong. This is exactly the failure mode the hardware-lookup skill exists to prevent.
