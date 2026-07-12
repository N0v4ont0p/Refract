# Transcript summary — eval-1 (citation verify trap), with_skill

Question: robot ~19 in. wide sitting on the field right before the match starts —
pass inspection or problem?

Skill followed: `ftc-rule-check/SKILL.md`, read in full first. Verdict flow steps
0 → 3 executed in order.

## Step 0 — corpus currency check

```
$ python3 scripts/check_freshness.py     # repo-root script
{
  "season": "decode-2025-26",
  "stored_incorporates_through": "Team Update 32",
  "stored_tu": 32,
  "live_tu": null,
  "status": "UNVERIFIABLE",
  "flag": true,
  "reason": "could not read a live Team Update number (no marker on page); treat corpus as possibly stale and say so in the answer"
}
EXIT=1
```

Result: UNVERIFIABLE (exit 1) → currency caveat added to the answer per SKILL §0.
Corpus incorporates through Team Update 32, retrieved 2026-07-03.

## Step 1 — retrieve rule + one hop

Located the governing rule by scanning `references/rules/rules.json` (212 rules):
R101 "STARTING CONFIGURATION is limited to an 18-inch Cube" was the direct hit.

```
$ python3 scripts/rules.py lookup R101
```

Returned R101 (18 in. x 18 in. x 18 in. starting volume, sole exception =
pre-loaded scoring elements) plus its one-hop cross-references:
- G304 (cited-by) — robot must be confined to STARTING CONFIGURATION on the field;
  match won't start / DISABLED on violation.
- I304 (cites) — robot inspected in every STARTING CONFIGURATION.
- R105 (cites) — after-start expansion still capped at the same 18 x 18 in.
  horizontal footprint.

All one-hop neighbors reinforce the verdict; no rule offered a 19 in. allowance.

## Step 2 — structured verdict

verdict = "illegal". 19 in. wide > 18 in. width cap; only exception (scoring
elements) inapplicable to robot frame. Each citation carried verbatim `text` from
the lookup output (see answer.md).

## Step 3 — verify citations (non-negotiable)

```
$ python3 scripts/rules.py verify R101 R105 G304 I304
{
  "exists": {"R101": true, "R105": true, "G304": true, "I304": true},
  "missing": [],
  "all_valid": true
}
EXIT=0
```

All 4 cited IDs exist. No hallucinated citations. Answer shipped.

## Verdict

illegal — a 19 in. wide robot fails the R101 18-inch starting cube and will not
pass inspection / will not be allowed to start (G304.E), with the currency caveat
noted.
