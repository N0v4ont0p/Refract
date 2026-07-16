# Review: Shooter.java / TurretAimer.java (sample-robot fixture)

## §§1-4 Structural review (ftc-code-review)

**Deterministic tier (authoritative):**
- `config_lint.py` (run against the fixture's own config via `--config`, since the default
  search picked up an unrelated repo's `32008teamcode/team-config.yaml`):
  **Finding** — `TurretAimer.java` references `Turret`, but `team-config.yaml` declares
  `turret: {value: none, confirmed: true}`. Per R34/config_lint framing: *"not referenced by
  current config; confirm if stale or a config mismatch"* — not asserting which. This is a
  real config/code divergence worth resolving with ftc-team-config before this code ships.
- `failure_mode_lint.py` ran repo-wide (fixture has no per-file target); findings were
  general-repo (vcs_discipline, god_opmode, mutable_static) and not specific to these two files.

**Corpus-grounded (§2), confidence/provenance as stored, not inflated:**
- `Shooter.java extends SubsystemBase` (`com.seattlesolvers.solverslib.command.SubsystemBase`)
  matches corpus pattern `15083-B-solverslib-command-adoption` — **confidence: single-source,
  provenance: shared-ancestry** (basis: subsystem/command substrate is SolversLib, the
  FTCLib-successor; not an independently-derived orchestration leg). Presented as-is: this is
  "a shared library's command pattern," not "N teams independently converged on this."
- `Shooter.spinUp()` is a stub with no body — too thin to evaluate against the empirical
  flywheel patterns in the corpus (e.g. 15083-A LUT/bang-bang); flagging as incomplete rather
  than reviewing logic that isn't there.

## §5 Legality question — resolved via ftc-rule-check's real flow

**1. Freshness check (run for real):**
```
$ python3 scripts/check_freshness.py
{
  "season": "decode-2025-26",
  "stored_incorporates_through": "Team Update 32",
  "stored_tu": 32,
  "live_tu": null,
  "status": "UNVERIFIABLE",
  "flag": true,
  "reason": "could not read a live Team Update number ... treat corpus as possibly stale and say so"
}
```
Per the flag: this verdict is against TU32-incorporated rules text; live currency is
unverifiable this run — said explicitly, not suppressed.

**2. Rule lookup + cross-refs (run for real):**
```
$ python3 .claude/skills/ftc-rule-check/scripts/rules.py lookup R207 R801
```
`R207` ("ROBOTS don't use air"), text (verbatim): *"ROBOTS may not use any closed air devices
such as but not limited to pneumatic solenoids or cylinders... B. ROBOTS may not use any
device which creates high-speed airflow... High-speed flywheels or rollers used for
manipulating SCORING ELEMENTS would not on their own be considered a high-speed airflow
device."* One-hop cross-ref → `R801` ("No Pneumatics"): *"No closed air systems are allowed
on FIRST Tech Challenge ROBOTS except for those explicitly listed in R207."*

**3. Verify (existence check, run for real):**
```
$ python3 .claude/skills/ftc-rule-check/scripts/rules.py verify R207 R801
{"exists": {"R207": true, "R801": true}, "missing": [], "all_valid": true}
```

**Reasoning:** the user's worry ("pneumatic-adjacent") maps to R207/R801, which restrict
*closed air systems* and *high-speed-airflow devices*. R207.B explicitly carves out flywheels:
a high-speed flywheel used to manipulate a scoring element is named as NOT a high-speed-airflow
device on its own. `Shooter.java`'s flywheel mechanism (`spinUp()`, motor-driven, no closed air
path, no compressor/cylinder) does not trip R207.A (no closed air device present) or R207.B
(the flywheel exemption applies directly). No inspection-relevant restriction found on
flywheel-type launchers as a mechanism category; separate rules (G416/G419, not air-related)
govern LAUNCH ZONE and scoring-direction rules for gameplay, not inspection legality.

### {verdict, citations, reasoning}
```json
{
  "verdict": "legal",
  "citations": [
    {"id": "R207", "text": "ROBOTS are restricted in their use of air in the following ways: A. ROBOTS may not use any closed air devices such as but not limited to pneumatic solenoids or cylinders, gas storage vessels, gas springs, compressors, or vacuum generating devices. Air-filled (pneumatic) wheels are exempt from this rule. B. ROBOTS may not use any device which creates high-speed airflow, except COTS computing devices manufactured with integrated cooling fans. Examples of a \"device which creates high-speed airflow\" include but are not limited to a fan designed to move SCORING ELEMENTS on the FIELD. High-speed flywheels or rollers used for manipulating SCORING ELEMENTS would not on their own be considered a high-speed airflow device."},
    {"id": "R801", "text": "No closed air systems are allowed on FIRST Tech Challenge ROBOTS except for those explicitly listed in R207."}
  ],
  "reasoning": "Shooter.java's motor-driven flywheel has no closed air device (no solenoid/cylinder/compressor/gas spring) so R207.A does not apply, and R207.B explicitly names high-speed flywheels used to manipulate scoring elements as NOT counting as a high-speed-airflow device on their own -- so the mechanism class itself is not restricted by the air rules. Freshness check flagged live TU currency as UNVERIFIABLE this run (stored through TU32); verdict is grounded in TU32 text and that caveat is carried forward, not silently dropped."
}
```

## Note back to ftc-team-config
The turret/config divergence found above is a config question, not a code-quality opinion —
routed back to `ftc-team-config` to confirm whether `TurretAimer.java` is stale or the config
needs updating, per this skill's boundary.
