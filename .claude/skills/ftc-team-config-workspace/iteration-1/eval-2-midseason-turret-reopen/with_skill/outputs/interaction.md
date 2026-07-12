# Verbatim message to the user (session stopped here awaiting reply)

Nice — a turret changes the picture, so before I write any aiming code I need to update and re-confirm your config. I've recorded the turret as `single_axis` (from what you just told me), but three things have to be settled first, because the answers change what code gets built. Right now the validator reports `generation_allowed: false`, so nothing generates until we close these out:

**1. What does the turret carry?** Your config says `shooter: none` (confirmed earlier this season), but in DECODE a turret only exists to aim a shooter — the season model literally requires `shooter != none` when a turret is present. So something changed alongside the turret:

   - **flywheel** — spinning wheel(s) launch the artifact
   - **elastic_catapult** — spring/rubber-band powered launcher

   Which one is on the turret? (If the turret is rotating something that *isn't* a shooter, tell me what — that's a different conversation.)

**2. Pathing library — this was never confirmed.** I inferred `none` from your repo a while back, but it was never confirmed, and it's one of the fields that must be confirmed before any code generation (it changes how an aiming subsystem gets its heading reference). Which is it?

   - **none** — no pathing library, plain drive code
   - **pedro_pathing**
   - **roadrunner**
   - **custom**

**3. How will the turret aim?** Your config says `vision: none` and `odometry: none` (both confirmed). That matters a lot for an aiming subsystem:

   - **Driver-aimed for now** — the skeleton exposes manual turret control (gamepad), no auto-aim
   - **You added a camera with the turret** (e.g. Limelight 3A or a webcam) — the skeleton includes an auto-aim hook fed by vision
   - **You added odometry** (dead wheels / Pinpoint / OTOS) — the skeleton can aim from field pose

   Did any sensing hardware change this week, or is it driver-aimed for now?

Once you answer, I'll read the full config back to you for a yes/no, and only then generate the `Turret` aiming subsystem skeleton (as a `raw_linear_opmode`-style subsystem class in TeamCode, matching your confirmed stack).

Why I'm asking instead of just writing the code: a wrong guess that compiles is worse than a question that costs one turn — turret code aimed with hardware you don't have would deploy fine and fail at a match.
