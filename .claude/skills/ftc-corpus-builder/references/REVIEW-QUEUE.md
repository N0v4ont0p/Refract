# Corpus review queue — deferred hardening tasks

Items merged on lighter evidence (usually because a subagent was unavailable due to the
account session limit) that should be re-run through the provenance-checker subagent when
it's available again. Merged entries stay usable meanwhile, tagged with the open question.

## Pending

- [ ] **22105-D-batch-color-sensor** — harden the origin/attribution of the same-package
  I2C-batch-read of REV color sensors. Merged `undetermined`/`medium` via the inline pass
  (subagent was session-limited). The batch-read-via-`com.qualcomm.hardware.broadcom`-package
  is a recognized circulated FTC trick that I could not source inline. Re-run to confirm
  22105-original vs adapted-from-a-community-source — same standard as the Iron Reign/KookyBotz
  case (an unsourced community-trick claim must not rest on the lighter inline pass).
  *Queued 2026-07-03; subagents reset ~midnight Europe/London.*
