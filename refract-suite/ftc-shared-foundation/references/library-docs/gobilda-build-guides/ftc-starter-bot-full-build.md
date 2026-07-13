> Source: https://www.gobilda.com/content/user_manuals/3200-2526-0001_assembly-instructions.min.pdf · Fetched: 2026-07-12

# FTC Starter Bot Assembly Guide (for DECODE™ season)

Full-robot build guide for the goBILDA FTC Starter Bot, built entirely from the **FTC Starter Kit** (SKU: 3200-4008-2526) plus a REV Control Hub. This is goBILDA's reference chassis + mechanism build for the DECODE™ season — a chain-driven drivetrain with a servo-actuated intake/transfer mechanism.

Overview, per goBILDA's resource page (https://www.gobilda.com/ftc-starter-bot-resource-guide-decode/):
- Scores game artifacts from close range, individually or in sequence
- Can transport up to three artifacts simultaneously
- Hand-loadable from designated loading zones
- Compact wheelbase intended for endgame positioning
- Assembled weight with REV Control Hub: 6125 g (13.5 lbs)

Related downloads from the same resource page (not fetched/mirrored here — link out only):
- Example op mode code (Java/Blocks): `https://www.gobilda.com/content/downloads/StarterBotCode.zip`
- CAD (STEP) files: `https://www.gobilda.com/content/step_files/3200-2526-0001.zip`

A separate variant of this same robot swaps the drivetrain wheels for a mecanum chassis — see `ftc-starter-bot-mecanum-drivetrain-variant.md` in this folder, which only documents the delta from this guide.

---

## Kit contents (Bill of Materials)

| Qty | Part | SKU |
|---|---|---|
| 2 | Plastic Gridplate | 1117-0216-0352 |
| 2 | 1-Hole Low U-Channel | 1121-0001-0048 |
| 2 | 5-Hole Low U-Channel | 1121-0005-0144 |
| 2 | 10-Hole Low U-Channel | 1121-0010-0264 |
| 2 | 11-Hole U-Channel | 1120-0011-0288 |
| 2 | 10-Hole U-Channel | 1120-0010-0264 |
| 4 | 90° Gusset | 1126-0090-0001 |
| 1 | 17-Hole U-Channel | 1120-0017-0432 |
| 6 | Quad Block Mount | 1201-0043-0002 |
| 2 | 1-Hole U-Channel | 1120-0001-0048 |
| 2 | 17-Hole Mini U-Channel | 1143-0017-0432 |
| 4 | 43mm Dual Block Mount | 1205-0001-0005 |
| 3 | 27mm Dual Block Mount | 1205-0002-0001 |
| 2 | 8mm Pattern Spacer | 1505-0032-0080 |
| 2 | 10-Hole Mini U-Channel | 1143-0010-0264 |
| 2 | Compact ServoBlock® | 3217-0001-2501 |
| 1 | 3-Hole Mini U-Channel | 1143-0003-0096 |
| 2 | Omni Wheel | 3624-0014-0096 |
| 3 | 19.2:1 Ratio Yellow Jacket Motor | 5203-2402-0019 |
| 80 | 8mm Socket Head Screw | 2800-0004-0008 |
| 70 | 10mm Socket Head Screw | 2800-0004-0010 |
| 32 | 12mm Socket Head Screw | 2800-0004-0012 |
| 4 | Hogback Wheel | 3626-0014-0096 |
| 2 | Speed Servo | 2000-0025-0003 |
| 4 | 14mm Socket Head Screw | 2800-0004-0014 |
| 2 | Gecko® Wheel | 3613-0014-0072 |
| 4 | 20mm Socket Head Screw | 2800-0004-0020 |
| 68 | Chain Link | 3309-0108-0050 |
| 40 | Washer | 2801-0004-0008 |
| 8 | 80mm Length, 8mm REX™ Shaft | 2106-4008-0800 |
| 1 | 11T Conversion Plate | 5105-0209-0019 |
| 2 | 43mm Length, 6mm Round Standoff | 1501-0006-0430 |
| 36 | Locknut | 2812-0004-0007 |
| 1 | 17T Conversion Plate | 5105-0107-0019 |
| 2 | 24mm Length, 8mm REX™ Standoff | 1516-4008-0240 |
| 2 | 8mm ID Spacer | 1522-0010-0120 |
| 5 | 8mm REX™ Hyper Hub | 1310-0016-4008 |
| 4 | 43mm Length, 8mm REX™ Standoff | 1516-4008-0430 |
| 8 | 8mm REX™ Bearing | 1611-0514-4008 |
| 4 | 10-Tooth Sprocket | 3307-4008-0010 |
| 4 | 48mm Length, 8mm REX™ Standoff | 1516-4008-0480 |
| 1 | 7mm Nut Driver | 4206-0070-0001 |
| 11 | Zip-Tie | 2909-0101-0100 |
| 1 | 2.5mm Hex-Plus L-Key | 5027103001 |
| 1 | Battery Mount (incl. Battery Strap) | 1209-0001-0001 |
| 1 | 3mm Hex-Plus L-Key | 5027104001 |
| 1 | REV Control Hub (**not included**) | REV-31-1595 |
| 1 | 12V Battery | 3100-0012-0020 |

Two plastic gridplates are field-cut before assembly per marked cutlines (14th hole at 108mm from each end) to produce the Side Guideplates, Center Guideplate, and Pushplate used later in the build.

---

## 1. Drivetrain base frame (Steps 1–9)

1. Attach two Quad Block Mounts to a 10-Hole U-Channel using eight 10mm Socket Head Screws (SHS).
2. Attach two 24mm Length, 8mm REX™ Standoffs to that channel using two 8mm SHS.
3. Fasten two 1-Hole Low U-Channels together using four 10mm SHS and four locknuts.
4. Attach an 11-Hole U-Channel to the Step 3 subassembly using four 8mm SHS.
5. Attach two more Quad Block Mounts to a second 10-Hole U-Channel using eight 10mm SHS.
6. Attach one more Quad Block Mount to that same channel using four 8mm SHS — note it mounts so its large hole does **not** align with the U-Channel's large holes (deliberate offset).
7. Join the Step 4 and Step 6 subassemblies using four 8mm SHS.
8. Attach a second 11-Hole U-Channel using eight 8mm SHS.
9. Mount two 19.2:1 Ratio Yellow Jacket Motors to the frame using eight 10mm SHS.

## 2. Chain-and-sprocket drive (Steps 10–15)

10. Build a 34-link Chain Loop. Slide the Chain Loop, a 10-Tooth Sprocket, and an 8mm ID Spacer onto the first Yellow Jacket motor's output.
11. Position a second 10-Tooth Sprocket into the chain loop. Slide an 80mm 8mm REX™ Shaft through two 8mm REX™ Bearings, an 8mm REX™ Hyper Hub, and that sprocket (mind bearing orientation), then clamp the shaft in the Hyper Hub's pinch bolts.
12. Repeat Step 10 for the second motor (another 34-link chain loop, sprocket, spacer).
13. Repeat Step 11 for the second motor's driven shaft.
14. Assemble an idler shaft: 80mm 8mm REX™ Shaft through two bearings and a Hyper Hub (no sprocket), pinch-bolted in place.
15. Repeat Step 14 to create the fourth (idler) shaft assembly.

This produces a four-shaft chain-driven drivetrain — two motor-driven shafts and two idler/driven shafts, linked in pairs by chain loops.

## 3. Battery mount & upper frame (Steps 16–28)

16. Fasten the Battery Mount and Battery Strap to the frame using four 10mm SHS and four locknuts.
17. Assemble a 5-Hole Low U-Channel with four 90° Gussets using eight 10mm SHS and eight locknuts — leave these fasteners slightly loose for now.
18. Attach two 43mm Length, 6mm Round Standoffs using two 8mm SHS.
19. Attach a 17-Hole Mini U-Channel using four 10mm SHS and four locknuts — leave loose.
20. Assemble a 5-Hole Low U-Channel with two 43mm Dual Block Mounts using four 12mm SHS (mind Dual Block Mount orientation).
21. Attach an 80mm 8mm REX™ Shaft with one 8mm SHS, noting the E-Clip location.
22. Attach the Step 18 assembly using one 8mm SHS, one 12mm SHS, and one locknut.
23. Fasten a second 17-Hole Mini U-Channel using one 8mm SHS, one 12mm SHS, and one locknut.
24. Secure that 17-Hole Mini U-Channel with four 10mm SHS and four locknuts, then fully tighten the fasteners left loose in Steps 17 and 19.
25. Assemble two 10-Hole Mini U-Channels with two 27mm Dual Block Mounts using four 12mm SHS.
26. Combine the Step 24 and Step 25 subassemblies using four 8mm SHS.
27. Assemble two 10-Hole Low U-Channels with two 43mm Dual Block Mounts using four 12mm SHS.
28. Combine the Step 26 and Step 27 subassemblies using four 8mm SHS (mounting locations differ from Step 26's join).

## 4. Shaft & pushplate subassembly (Steps 29–35)

29. Attach two 80mm 8mm REX™ Shafts using two 8mm SHS (note E-Clip locations).
30. Attach one more 80mm 8mm REX™ Shaft using one 8mm SHS (E-Clip).
31. Mount four 48mm Length, 8mm REX™ Standoffs to a 17-Hole U-Channel using four 8mm SHS.
32. Attach a Quad Block Mount using four 10mm SHS.
33. Attach the Pushplate (one of the field-cut gridplate pieces) using four 10mm SHS, four washers, and four locknuts.
34. Combine the Step 30 and Step 33 subassemblies using four 8mm SHS.
35. Combine the Step 16 and Step 34 subassemblies in four sub-steps (A–D): four 10mm SHS; four 10mm SHS + four locknuts; two 8mm SHS; two 10mm SHS + two locknuts.

## 5. Artifact ramps (Steps 36–37)

36. Zip-tie two Ramps in place — make sure zip-tie heads sit below the 1-Hole Low U-Channel and both ramps lie flat against it.
37. Push the first ramp into place and fix it with four washers and four 8mm SHS. Push the second ramp into place and secure it with two zip-ties (heads inside the 5-Hole Low U-Channel, behind the ramp).

## 6. Second motor conversion & hogback wheel arm (Steps 38–43)

38. Attach a 27mm Dual Block Mount to a 3-Hole Mini U-Channel using two 12mm SHS.
39. Convert a third 19.2:1 Ratio Yellow Jacket Motor to a 1:1 ratio using the included Conversion Plate, then mount it with four 10mm SHS. (goBILDA's motor-conversion video: `http://bit.ly/41fQtuj`.)
40. Attach an 8mm REX™ Hyper Hub to the converted motor's output — a standard credit card (~1mm thick) is a handy spacer for setting the hub's clearance from the mounting screws.
41. Attach a Hogback Wheel and an 8mm Pattern Spacer using four 14mm SHS.
42. Attach a second Hogback Wheel and Pattern Spacer using four 20mm SHS and four washers.
43. Combine the Step 37 and Step 42 subassemblies using two 8mm SHS.

## 7. Servo-driven intake rollers — Gecko® Wheels (Steps 44–48)

44. Assemble two 1-Hole U-Channels with four 43mm Length, 8mm REX™ Standoffs using four 8mm SHS.
45. Assemble two Compact ServoBlocks® with two Speed Servos.
46. Combine the ServoBlock® assemblies with the Step 44 channels using eight 8mm SHS.
47. Attach two Gecko® Wheels using eight 8mm SHS and eight washers.
48. Combine the Step 43 and Step 47 subassemblies using four 8mm SHS.

The Gecko® Wheels are the servo-actuated, high-friction intake/transfer rollers referenced in the "hand-loadable" and "transport up to three artifacts" capabilities above.

## 8. Guideplates (Steps 49–50)

49. Zip-tie the two field-cut Side Guideplates in place (four zip-ties).
50. Fasten the Center Guideplate using two 8mm SHS and four washers — its height should match the Side Guideplates.

## 9. Final drivetrain wheels (Steps 51–52)

51. Attach two Hogback Wheels using eight 12mm SHS and eight washers.
52. Attach two Omni Wheels using eight 12mm SHS and eight washers — mount them to the 8mm REX™ Hyper Hubs from the wheel's "deep" side.

Drivetrain result: 2 driven chain-linked wheel pairs + Hogback + Omni wheels forming the compact 4(+2)-wheel base.

## 10. Electronics (Steps 53–54)

53. Zip-tie the REV Control Hub in place (three zip-ties).
54. Install the 12V Battery.

Assembly complete — wiring and programming are covered separately (not part of this build guide).
