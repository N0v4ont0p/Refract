# Wire gauge for drive motor power leads — 30 AWG

**Verdict: ILLEGAL** — 30 AWG is thinner than the minimum wire size required for motor power. Do not use it for drive motor leads.

> Corpus-currency note: the local freshness check returned `UNVERIFIABLE` (could not read a live Team Update number from the FIRST site; corpus incorporates through Team Update 32, retrieved 2026-07-03). The verdict below is from the local corpus. Wire-sizing (R615 / Table 12-8) is base-manual content and has not been a Team Update target, so this is very unlikely to have changed — but confirm against the live manual before inspection.

## Structured verdict

```json
{
  "verdict": "illegal",
  "citations": [
    {
      "id": "R615",
      "text": "All circuits shall be wired with appropriately sized insulated copper wire (SIGNAL LEVEL cables do not have to be copper): Table 12-8: Wire sizing requirements [[TABLE:12-8]] Integrated wires originally attached to legal COTS devices or wires included/sold by the manufacturer are considered part of the device and by default legal. Such wires are exempt from this rule. In order to show compliance with these rules, teams should use wire with clearly labeled sizes if possible. If unlabeled wiring is used, teams should be prepared to demonstrate that the wire used meets the requirements of this rule (e.g., wire samples and evidence that they are the required size). Combining multiple smaller wires in parallel cannot be used to create an equivalent larger wire which meets minimum wire cross section requirements."
    }
  ],
  "reasoning": "R615 requires appropriately sized wire per Table 12-8, which sets a MINIMUM wire size per application (minimum size = maximum AWG number, since higher AWG = thinner wire). For 'Motor Power (unless otherwise listed)' the minimum is 18 AWG. Even the most lenient motor category (TETRIX MAX 12V DC Motors and REV Core Hex REV-14-1300) allows only down to 22 AWG. 30 AWG is thinner than both 18 AWG and 22 AWG, so it fails the minimum for every motor category. It is even thinner than the 28 AWG minimum for signal-level circuits. Standard FTC drive motors (goBILDA 5203, NeveRest, REV HD Hex, etc.) fall under 'Motor Power (unless otherwise listed)' = 18 AWG minimum."
}
```

## Table 12-8 (resolved via [[TABLE:12-8]] pointer — verbatim minimums)

Higher AWG number = thinner wire, so a "minimum wire size" is the *thinnest* (largest AWG) you may use.

| Application | Minimum wire size |
|---|---|
| 12V Main Battery Power | 18 AWG (19 SWG or 1 mm²) |
| Motor Power (unless otherwise listed) | 18 AWG |
| 11–20A fuse protected circuit | 18 AWG |
| Motor Power — TETRIX MAX 12V DC Motors, REV Robotics Core Hex (REV-14-1300) | 22 AWG (22 SWG or 0.5 mm²) |
| PWM / Servo | 22 AWG |
| LEDs (5V / 12V) | 22 AWG |
| ≤10A fuse protected circuit | 22 AWG |
| SIGNAL LEVEL circuits (draw ≤1A continuous, source incapable of >1A: I2C, DIO, Analog, encoder, RS485) | 28 AWG (29 SWG or .08 mm²) |

Source: `manual-tables/table-12-8.json`, caption "Wire sizing requirements", DECODE Competition Manual (2025-2026).

## Why 30 AWG fails

- Your drive motors run on **Motor Power**. Unless they are specifically TETRIX MAX 12V DC or the REV Core Hex, the minimum is **18 AWG**. 30 AWG is far thinner — illegal.
- Even if they *were* the exempt small motors (22 AWG floor), 30 AWG is still thinner — still illegal.
- 30 AWG is thinner than even the 28 AWG signal-level minimum, so there is no category in the table under which 30 AWG passes for motor power.
- R615 also blocks the common workaround: you **cannot** parallel multiple 30 AWG wires to fake an equivalent 18 AWG cross-section.

## Weight-saving alternative that stays legal

If the goal is weight, the lowest-mass compliant option for standard drive motors is **18 AWG** (the minimum for "Motor Power unless otherwise listed") rather than a heavier 16/14 AWG. You do not have to exceed the minimum. Note the one exemption in R615: integrated wires that came attached to a legal COTS device (or manufacturer-supplied leads) are legal as-is regardless of gauge.
