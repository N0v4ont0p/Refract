# Corpus source-legitimacy record

Legitimacy + license status of every mined repo (§14.1). Corpus convention holds
regardless of license: **file+line references only, never reproduce substantial
code blocks.** Public GitHub is fine to cite with attribution.

| Team | Repo | Category | License | Notes |
|---|---|---|---|---|
| 15993 | info1robotics/DECODE (V1), info1robotics/Ryuu-DECODE (V2) | public | **default-copyright** (none stated) | study + file/line refs only |
| 18742 | WoEN239/Decode18742 | public | **MIT-style** | siblings Decode17517/Decode33333 = same team (one lineage) |
| 3543 | trc492/Ftc2026Decode (+ submodules trc492/trclib, trc492/ftclib) | public | **MIT** | see correction below |

## Correction (Session 1, Phase 4) — team 3543

Phase 1's source list stated 3543 had **"no stated license → default-copyright."**
**That is inaccurate.** Verified in the checkout:
- Root `LICENSE` — MIT, "Copyright (c) 2025 **Titan Robotics Club**"; duplicate in `teamcode/`.
- Submodules `trclib` (2020) and `ftclib` carry their own MIT LICENSE files; per-file
  MIT copyright headers throughout.
- **`trc492` = Titan Robotics Club = the same organization as FTC team 3543**
  (trc492 is their FRC-492 GitHub org). The `trclib`/`ftclib` framework is
  therefore **Titan's own multi-year, cross-FRC/FTC library**, pulled via git
  submodules — **NOT a third-party framework.**

Weighting consequence (not just a license-field change): 3543's framework-layer
patterns are Titan's **own** cross-season engineering, mined as high-value —
distinct from a team merely consuming an external library.

## Framework-lineage provenance rule (applies to 3543 framework-layer patterns)

The `trclib`/`ftclib` framework is a **single Titan lineage**. Keep these two
claims **explicitly separate** (they are easy to conflate):
- **Maturity/popularity:** many teams adopt TRC → evidence the framework is
  mature and battle-tested.
- **Design validation:** adoption is **NOT** independent validation of a design
  choice (§12: adoption ≠ independent invention). Only genuine cross-team
  *independent* convergence corroborates a design.

So framework patterns are tagged **high-value `single-source`** (Titan lineage)
with a maturity note — not promoted on adoption count.

## Tier 3 (Session 1, Phase 4) — a DIFFERENT KIND of source, recorded honestly

Tier 3 is not a positive-pattern tier like Tier 1/2. Both repos are public; neither is a
Tier-1/2-style robot codebase.

| Team | Repo | What it actually is | Disposition |
|---|---|---|---|
| 21813 | `ayaan-gupta/ftc21813-opensource-research` | RESEARCH docs only (2 PDFs + README, **zero code**): "6 Wheeled Mecanum Drive for FTC" (W. Wang, Sep 2025) + "DECODE FoV" | §7 reference candidate, **tier-2/uncorroborated** — see spot-check |
| 32477 | `fu-silent/FTC-32477-Decode-Program-History` | LEARNING team; file-versioned program history (folder-copy snapshots) | **NOT a pattern source.** Recorded as a failure-mode **case study** in `known-failure-modes.md` (file-versioning + god-OpMode compounding) |

### 21813 spot-check (requested before finalizing tier) — 6-wheel mecanum kinematics PDF

Two tests were run against the corpus before deciding the tier:

1. **Degeneracy to standard 4-wheel mecanum — PASSES at the derivation level.** The rigid-body
   foundation (`v_a = v_b + ω × r`) and roller projection (`v_w = √2·û·v`) are textbook-correct.
   Substituting each wheel's *actual signed position* into the per-wheel formula reproduces the
   standard 4-wheel inverse kinematics exactly (verified all four: FL `(vx−vy)−ω(Lx+Ly)`, FR
   `(vx+vy)+ω(Lx+Ly)`, BL `(vx+vy)−ω(Lx+Ly)`, BR `(vx−vy)+ω(Lx+Ly)`). NWU coordinate convention
   matches the DECODE field frame the corpus teams use.
2. **Consistency with corpus fielded vector math — CONSISTENT (framework-level).** The rigid-body +
   vector-projection toolkit is the SAME one the corpus fields (24089's normal/tangential
   decomposition, 12808's orthogonal-basis projection, 15083's pose kinematics). No inconsistency —
   but note it addresses DRIVETRAIN kinematics, not ballistics, so this is framework-consistency, not
   an equation-level cross-check of SOTM/`trajectory_solver.py`.

**Errors the spot-check DID catch (why it stays tier-2, not promoted):**
- The final compact **matrix (p.7) is wrong as printed**: it uses a single symbolic `(rx, ry)` across
  all six rows, dropping the per-wheel position signs — so it yields e.g. FR `+ω(rx−ry)` instead of the
  correct `+ω(Lx+Ly)`. A team copying the page-7 matrix directly would get wrong rotation behavior. The
  *derivation* is right; the *final matrix* loses the per-wheel signs.
- Multiple **copy-paste label errors** in the derivations (p.6: Back-Left, Front-Right, Middle-Right all
  mislabeled `⃗v_fml`).
- The **6-wheel novelty itself** (middle-wheel roller assignment `ML=(î−ĵ)`, `MR=(î+ĵ)`) is the paper's
  unverified "novel configuration" claim — not independently corroborated.

**Verdict:** the tier-2 caution did its job — the spot-check found a real, copy-me-and-break error in the
headline result. **Not promoted past tier-2.** Usable as a §7 *reference for the standard rigid-body /
mecanum derivation* (that part checks out), with an explicit warning to derive the matrix per-wheel and
NOT copy the paper's page-7 matrix; the 6-wheel extension is unverified.
