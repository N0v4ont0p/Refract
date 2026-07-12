I have to hold off on giving you numbers for either of those — and I want to be straight about why, because for gearing decisions a wrong torque figure is exactly the kind of thing that bites later.

**Neither the 26.9:1 nor the 43.7:1 is in my verified spec catalog, so I'm abstaining on both.** My hardware catalog only holds parts whose specs were checked against a manufacturer source. For the 5203 Yellow Jacket line, the seeded ratios right now are **19.2:1** and **13.7:1** — the 26.9:1, 43.7:1 (and 5.2, 50.9, 71.2, 99.5, 139, 188, ...) are not in it. I could produce confident-sounding stall-torque numbers from memory, but that's precisely the failure mode this tool exists to prevent, so I won't.

One thing I specifically won't do: **interpolate** the missing ratios from the 19.2:1 I do have. goBILDA measures gearbox efficiency per-ratio, so stall torque doesn't scale linearly with the gear ratio — scaling the 19.2:1 figure up to 26.9 or 43.7 would give a wrong answer that looks reasonable.

**Where to get the verified numbers** — the goBILDA product pages, which list stall torque per ratio:
- 5203 26.9:1 and 43.7:1: browse the 5203 Yellow Jacket series at https://www.gobilda.com (filter to the 26.9:1 and 43.7:1 listings; each page publishes stall torque in kg·cm and oz-in).

If you paste me the stall-torque values off those two pages, I can add them and then run any gear/torque math you need for the shooter against verified numbers.

For reference, the one seeded 5203 ratio I *can* give you a sourced number for, as a sanity anchor for the format you'll see on those pages:
- **5203 19.2:1** — published stall torque **24.3 kg·cm (338 oz-in)**, no-load 312 RPM, stall current 9.2 A. Source: goBILDA product page (tier-1 manufacturer), retrieved 2026-07-05.

Note that a published stall torque is the *ideal* figure; real delivered torque under load runs lower. Happy to work the shooter math once we have the two ratios' verified specs.
