# Transcript summary — eval-2-crossref-traversal (with_skill)

## Task
User: "once the match is going, how far is our robot actually allowed to expand past the starting size? want to make sure our arm extension is legal."

## Skill procedure followed
Read `.claude/skills/ftc-rule-check/SKILL.md` in full first, then executed its verdict flow: lookup (rule + one-hop cross-refs) → reason → verify citations before shipping.

## Files read
- `/Users/georgehu/Desktop/FTC Training AI/.claude/skills/ftc-rule-check/SKILL.md` (full)
- `references/standing-principles.md` (suite root; via first Bash call — §1 deterministic-first, §2 abstention, §3 tiering, §6 confidence-drift)
- `references/rules/rules.json` meta block — confirmed manual = "DECODE Competition Manual (2025-2026)", incorporates_through = "Team Update 32", retrieved 2026-07-03, tier = rule.
- Full lookup output persisted at `.../tool-results/b8vj0s3ng.txt` (R101, R105, G414, G415 with one-hop cross-refs).

## Commands run (with key output)
1. Located scripts/refs: `scripts/rules.py` at `.claude/skills/ftc-rule-check/scripts/rules.py`; rules data at `.claude/skills/ftc-rule-check/references/rules/`.
2. Keyword scan of `rules.json` for expansion/size terms → surfaced candidate rules: **R101** (STARTING CONFIGURATION 18-inch cube), **R105** (expansion limits), **G414** (horizontal expansion limits), **G415** (vertical expansion limits, with exceptions). Also G304, I304 as neighbors.
3. `python3 scripts/rules.py lookup R105 G414 G415 R101` → returned full rule text + one-hop cross-refs. Cross-ref cluster confirmed self-contained: R101 ↔ R105 ↔ G414 / G415 (plus R101→G304, R101→I304). No further hop needed — the expansion answer lives entirely in this cluster.
4. `python3 scripts/rules.py verify R101 R105 G414 G415` → `all_valid: true`, `missing: []`, exit 0. All four citations verified to exist before shipping.

## Rules cited and how found
- **R101** — starting size is an 18×18×18 in. cube (baseline the expansion is measured against). Found via keyword scan; confirmed as R105's cross-ref neighbor.
- **R105** — the core expansion rule: horizontal fixed 18×18 box (mechanical constraint required, software insufficient), vertical 18 in. normally / 38 in. under G415 conditions; flexible extensions count; two-sided extension rules; inspection demonstration. Found via keyword scan, primary rule.
- **G414** — horizontal expansion limit enforcement + penalty (MINOR FOUL, MAJOR if strategic; damage exception). One-hop cross-ref from R105.
- **G415** — vertical expansion limit enforcement + endgame exception (up to 38 in. only in final 20 s AND outside LAUNCH ZONES) + penalty. One-hop cross-ref from R105.

## Verdict emitted
Legal to expand, within limits. Horizontal: no growth past the fixed 18×18 in. footprint, mechanically hard-stopped (software not sufficient). Vertical: 18 in. anytime, 38 in. only in final 20 s outside LAUNCH ZONES. Penalties per G414/G415.

## Staleness note included in answer
All four rules are base-manual (no TU altered them in local data); snapshot is through TU32, retrieved 2026-07-03 — flagged that a newer Team Update could exist and should be re-checked, per SKILL "Team Updates and staleness."
