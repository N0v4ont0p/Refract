# Changelog

Pulled from the actual git history — real commits, not a reconstructed narrative.

## 2026-07-16 — `c27b0c4` — Team 32008 formalized (internal-only); TickTree made a real config option

- Team 32008's mined patterns formalized into the corpus, tagged internal-only per its confirmed
  permission scope (not eligible for the public plugin corpus without separate reconfirmation).
- TickTree (a companion behavior-tree library) made a genuinely selectable config option:
  `software_stack.behavior_layer`, grounded generation against real fetched docs, a working
  staleness check.
- `standing-principles.md` extended with two more instances of the same failure shape as an
  earlier bug: a fix that reads as correct isn't verified until it's actually run and checked
  against real output.

## 2026-07-16 — `96b083b` — Team 19859 formalized at full depth; permission scope, cross-team findings re-checked

- Team 19859 (a real team's own repo, not a public clone) mined at full depth: feature-vector
  extraction, git-evolution analysis, pattern extraction, provenance classification.
- Every existing cross-team corpus finding re-checked against the new data individually, not
  bulk-appended.
- A new standing rule: check for the suite's own prior generated output before mining any
  directory, closing a real circular-provenance risk.

## 2026-07-16 — `6047121` — Final hardening: real staleness re-checks, a fresh eval battery, a real bug found and fixed

- Every bundled library's freshness re-checked for real against its live GitHub release feed —
  one was genuinely stale, characterized and closed with a sourced addendum.
- A fresh 6-scenario eval battery across all 5 skills, all regression-free.
- A real bug (a config-discovery script silently picking the wrong file) caught live by that
  battery, fixed at root cause, and used to correct a standing-principles claim rather than
  buried in a commit message.

## 2026-07-16 — `65c3d31` — Standing principle: the unhedged claim is the one that needed the check

- A cross-tool compatibility claim ("5 of 8 tools, zero bridge") didn't survive independent
  per-tool verification. The correction became a standing rule: a claim with no caveat attached
  is the one that most needs one checked for.

## 2026-07-16 — `b58d4fd` — MCP server, verified cross-tool reach, a continuous input layer

- `mcp-server/` built: the same deterministic scripts every skill already calls, exposed over MCP
  for any MCP-speaking client.
- The Agent Skills format's cross-tool support verified directly against each tool's own current
  documentation, not assumed.
- `corpus-input-scan.py`: a draft-only scanner for new team repos, stale library releases, and
  Team Update drift — never auto-merges, always drafts for human review.

## 2026-07-16 — `b3ec9a4` — Rule-check parity, a 57-file library-docs audit

- `ftc-construct`'s post-generation verification brought to genuine parity with `ftc-rule-check`'s
  real flow (freshness gate, explicit reason-to-verdict).
- Every one of the 57 fetched library-doc files checked for a real, reachable path from a skill's
  actual instructions — not just presence in a sibling directory.

## 2026-07-13 — `3430ed2` — `ftc-construct` added: grounded code generation

- The fifth skill: config-gated code generation, scaffolding from a quickstart template, grounding
  every API call and tuning value in real library docs and the hardware catalog, running a
  mandatory rules-and-review pass on its own output before calling anything done.

## 2026-07-12 — `5195108` — README and MIT license

## 2026-07-12 — `7e2feca` — Refract v1.0.0

The initial plugin release: 4 skills (`ftc-team-config`, `ftc-hardware-lookup`, `ftc-rule-check`,
`ftc-code-review`), the pattern corpus, and the Claude Code plugin marketplace structure.
