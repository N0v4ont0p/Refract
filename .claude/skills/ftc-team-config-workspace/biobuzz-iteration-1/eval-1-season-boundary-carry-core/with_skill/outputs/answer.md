Happy kickoff! I haven't written any code or files yet. Your config from last season was for DECODE, and the robot code can't be generated until the BIOBUZZ parts are confirmed.

**What the checks found**
- The active season is BIOBUZZ (`biobuzz-2026-27`). Your file is marked `decode-2025-26`. Running `validate_config.py` on it gave `valid: true` but `generation_allowed: false`, because its mechanism list was confirmed for DECODE.
- There's no `team-config.yaml` in the project yet.
- I didn't run the repo scanner (`extract_feature_vector.py`). You didn't point me to last season's code, and the other team folders in this repo belong to other teams.
- I made a test copy that keeps your drivetrain and software settings, drops the DECODE mechanisms and marks the rest unconfirmed. The validator says these still block code generation:
  - drivetrain type
  - pathing library
  - OpMode style
  - the BIOBUZZ mechanism set
  - tuning status

**What carries over, pending your OK:** your drivetrain, control hub, sensors, software stack, build capability and experience level. The DECODE mechanism list and the `fixed_shooter_on_swerve` archetype don't carry over. BIOBUZZ has no defined archetypes, and I won't turn old mechanisms into new names (your shooter is not automatically a BIOBUZZ launcher).

**Not asked:** control hub. Through 2026-27 the REV Control Hub is the only legal option, so it's recorded as inferred.

## Questions for you, most important first

**1. Is the core robot the same? (one line)**
"Still 4-module custom-built swerve, Pinpoint odometry, Limelight 3A, 1 Expansion Hub, Pedro Pathing, FTCLib command-based, CNC fabrication?"
- **Yes:** I mark these confirmed as asked, keeping the same values.
- **Something changed at kickoff:** I re-ask only that item. If the drivetrain changed, I also drop the drivetrain tuning. If pathing changed, the tuning section is rebuilt for the new library. Pedro does support swerve; its setup, constants and tuning guides are in `library-docs/pedro-pathing/docs/pathing/tuning/swerve/`.
- **If FTCLib command-based stays:** I'll ask one follow-up only if you mention wanting to interrupt, prioritize or fall back between behaviors. There's also TickTree, a behavior-tree layer that sits on top of whichever command framework you picked. It's pre-alpha and its API is unstable, so it's a real option but not a safe default. If you don't take it up, I record `behavior_layer: none` and don't bring it up again.

**2. Which BIOBUZZ mechanisms will you have?** Options come from the season file; last season's robot is shown for reference only.
- `intake`: roller / other / none. Last season: roller. One intake must handle 2.8 in POLLEN and 3.6 in NECTAR and stop at 4 held elements, so the DECODE intake shouldn't be assumed to carry over.
- `hive_launcher`: flywheel / other / none. Last season: flywheel shooter.
- `turret`: none / single_axis / other. Last season: single-axis. A turret requires a launcher.
- `aim_vision`: upward_apriltag / other / none. Requires a launcher. BIOBUZZ tags sit on the moving HIVE, so they can't be used for field localization.
- `element_color_sensing`: present / none
- `capacity_limiter`: present / none
- `flower_placer`: present / none
- `flower_pollen_retrieval`: present / none
- `endgame_parking`: loading_zone_park / none. Parking is scored but not mandatory this year.

I record each answer as asked, then re-run the validator. It rejects a turret or aim vision without a launcher. Each mechanism you pick gets its own subsystem interface; anything marked `none` gets no code at all.

**3. How are the swerve modules steered, by motors or servos?** The season file notes rule R503's limit of 8 motors and 8 servos (servos cut from 10 in Team Update 00). Four drive motors plus four steering motors would use the whole motor budget before any intake or launcher. Your answer decides which hardware names I need. If it looks over budget, the legality question goes to ftc-rule-check; I won't rule on it here.

**4. Do you have tuning constants from running the tuning procedure on this BIOBUZZ robot, or not yet?** Last season's file said `untuned` with no values, and mass changes with a new robot.
- **Not built or wired enough to tune yet:** `not_yet_tunable`. Code is scaffolded with every tuning value marked untuned.
- **Could tune but haven't:** `untuned`. Same scaffold, with the Pedro swerve tuning steps attached.
- **Tuned:** give me the numbers or the code and I copy them exactly as `measured`. Any constant you don't know stays empty and marked `untuned`; I never fill in a guess. If there's a repo, I'll also run `failure_mode_lint.py`. It flags constants still sitting at library or template defaults, which can look tuned when they aren't.

**5. What are your hardware device names?** Please give them exactly as typed in the Robot Controller configuration: 4 drive motors, the steering actuators, Pinpoint, Limelight, and one per mechanism from question 2.
- **If you point me to last season's code instead:** I'll run the repo scanner, pull the real names (following constants back to the actual strings) and show them as one block for you to confirm.
- **Otherwise:** I'll use exactly what you type, with no naming convention of my own.

## After you answer
I'll read the full BIOBUZZ robot description back to you and ask for a clear yes. Then I'll mark the fields confirmed and write `team-config.yaml` with `_meta.season: biobuzz-2026-27` and a history entry noting the move from DECODE 2025-26 to BIOBUZZ 2026-27. Once `validate_config.py` reports `generation_allowed: true`, I'll hand off to ftc-construct to write the code.

The scratch copy I validated is at `/private/tmp/claude-501/-Users-georgehu-Desktop-FTC-Training-AI/95cb109b-9a3f-4bed-97ed-a0ec2881d9b9/scratchpad/evalruns/carry-core.yaml`.