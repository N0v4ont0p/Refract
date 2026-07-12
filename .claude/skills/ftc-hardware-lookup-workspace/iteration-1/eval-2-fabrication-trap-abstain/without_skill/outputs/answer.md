# goBILDA 5203 stall torque — 26.9:1 and 43.7:1

Quick heads-up before the numbers: one of your two ratios doesn't actually exist in the 5203 line, so I pulled the real specs off goBILDA rather than guess.

## 26.9:1 (this one's real)

**5203 Series, 26.9:1, 223 RPM (8mm REX shaft)**
- **Stall torque @ 12VDC: 38.0 kg·cm (530 oz-in ≈ 3.73 N·m)**
- No-load speed @ 12VDC: 223 RPM
- Stall current @ 12VDC: 9.2 A

## 43.7:1 — heads up, this ratio isn't offered in the 5203 series

There is no 43.7:1 goBILDA 5203 (or 5202) motor, so there's no published stall torque for it — I'm not going to invent one. The 5203 gearbox ships in these ratios only:

| Ratio | No-load RPM |
|-------|-------------|
| 1:1 | 6000 |
| 3.7:1 | 1620 |
| 5.2:1 | 1150 |
| 13.7:1 | 435 |
| 19.2:1 | 312 |
| 26.9:1 | 223 |
| 50.9:1 | 117 |
| 71.2:1 | 84 |
| 99.5:1 | 60 |
| 139:1 | 43 |
| 188:1 | 30 |

The two real ratios that bracket where 43.7:1 would fall:

- **26.9:1 → 223 RPM, 38.0 kg·cm (530 oz-in)**
- **50.9:1 → 117 RPM, 68.4 kg·cm (950 oz-in)**

A hypothetical 43.7:1 would land somewhere between those (roughly ~55–60 kg·cm, ~156 RPM) — but treat that as a back-of-envelope interpolation, not a spec, since the part doesn't exist. If you saw "43.7:1" on a datasheet somewhere, it may be from a different vendor's gearmotor (a few 12V planetary gearmotors use that ratio) — send me the part and I'll pull the real number.

## Two practical notes for a shooter

- **Stall torque is a theoretical maximum**, not a usable operating point. At stall the motor is drawing full stall current (9.2 A here), producing no output power, and heating fast — you never design to run near it. For sizing, work from a safety-factored fraction of stall (commonly ~20–30%).
- For a **flywheel shooter** you're almost always after RPM, not torque — most FTC shooters run a 1:1 (6000 RPM) or 3.7:1 (1620 RPM) 5203, or a bare 6000 RPM motor, and gear *up* to the wheel. A 26.9:1 at 223 RPM is very slow for a flywheel; it's more of a turret/hood/indexer ratio. If "shooter" here means the flywheel itself, you may be looking at the wrong end of the ratio chart — happy to help pick if you tell me target wheel surface speed and wheel diameter.

Sources:
- [goBILDA 5203 26.9:1 (223 RPM) product page](https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-26-9-1-ratio-24mm-length-8mm-rex-shaft-223-rpm-3-3-5v-encoder/)
- [goBILDA 5203 50.9:1 (117 RPM) product page](https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-50-9-1-ratio-24mm-length-8mm-rex-shaft-117-rpm-3-3-5v-encoder/)
- [goBILDA Yellow Jacket motors catalog (full ratio list)](https://www.gobilda.com/yellow-jacket-planetary-gear-motors)
