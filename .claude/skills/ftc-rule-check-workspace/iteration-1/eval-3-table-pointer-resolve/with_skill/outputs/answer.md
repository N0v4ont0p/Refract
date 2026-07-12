# Is 30 AWG legal for drive motor power leads?

**Verdict: Illegal.** 30 AWG is too thin for motor power leads under the wire-sizing rule. Don't use it.

## The rule

**R615 — Use appropriately sized wire:** "All circuits shall be wired with appropriately sized insulated copper wire (SIGNAL LEVEL cables do not have to be copper): Table 12-8: Wire sizing requirements." The rule delegates the actual numbers to **Table 12-8**, so the verdict turns on that table, not on the rule prose.

## What Table 12-8 requires (resolved from the table, not memory)

| Application | Minimum wire size |
|---|---|
| 12V Main Battery Power | 18 AWG (19 SWG / 1 mm²) |
| **Motor Power (unless otherwise listed)** | **18 AWG (19 SWG / 1 mm²)** |
| 11–20 A fuse-protected circuit | 18 AWG |
| **Motor Power — TETRIX MAX 12V DC Motors, REV Core Hex (REV-14-1300)** | **22 AWG (22 SWG / 0.5 mm²)** |
| PWM / Servo, LEDs, ≤10 A fuse-protected circuit | 22 AWG |
| SIGNAL LEVEL circuits (I2C, DIO, analog, encoder, RS485, ≤1 A) | 28 AWG (29 SWG / .08 mm²) |

Note: "Minimum wire size" here means the **thinnest allowed** — and because AWG numbers run backwards, a *larger* AWG number is a *thinner* wire. So "minimum 18 AWG" means 18 AWG or thicker (18, 16, 14…), i.e. 18 is the highest AWG number permitted.

## Why 30 AWG fails

- A standard FTC drive motor (goBILDA 5203, REV HD Hex, etc.) is "**Motor Power (unless otherwise listed)**" → minimum **18 AWG**. 30 AWG is far thinner than 18 AWG, so it's illegal.
- Even the special-case motors (TETRIX MAX, REV Core Hex) only relax the minimum to **22 AWG** — still much thicker than 30 AWG. So there is no drive-motor category under which 30 AWG passes.
- 30 AWG is thinner than even the **28 AWG** floor for tiny signal-level circuits — it isn't legal anywhere in this table.

R615 also explicitly blocks the obvious workaround: "Combining multiple smaller wires in parallel cannot be used to create an equivalent larger wire which meets minimum wire cross section requirements." So you can't run several 30 AWG strands to fake an 18 AWG conductor.

Beyond the rule, this is a real safety limit: drive motors pull several amps continuously and stall at much higher current; 30 AWG has a tiny cross-section and would overheat, drop voltage, and risk melting/fire on a motor lead. The rule minimum exists for exactly this reason — the weight you'd save is grams, and it'll fail inspection under R615.

## What to run instead

Use **18 AWG or thicker** for your drive motor power leads (16 or 14 AWG is common and fine — thicker always passes). If you're specifically running REV Core Hex or TETRIX MAX motors, 22 AWG is the floor, but for typical drive motors stick to 18 AWG minimum.

One exemption to know: wires **originally attached to a legal COTS device** (e.g., the leads that come pre-attached to your motor from goBILDA/REV) are considered part of the device and are exempt from R615 — you only need to meet the table on wire *you* add or extend. To save weight, choose lighter mechanisms or a smaller battery lead run, not undersized motor leads.

---

**Citations:** R615 (Use appropriately sized wire), R607 (electrical pathway must be appropriately gauged/rated). Both verified against the manual. Requirement value resolved from Table 12-8 (Wire sizing requirements), DECODE Competition Manual (2025-2026). All rules cited carry `effective_date: base-manual` (not changed by a Team Update in local data); a newer Team Update could exist that the local snapshot doesn't reflect.
