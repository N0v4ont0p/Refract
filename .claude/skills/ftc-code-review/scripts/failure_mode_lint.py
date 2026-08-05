#!/usr/bin/env python3
"""
ftc-code-review — deterministic failure-mode linter (§17 rule-based tier, Phase 9).

Maps concrete, DETERMINISTIC checks to categories in repo-root known-failure-modes.md.
No model judgment: pure pattern-matching over git history and repo structure
(operating rule 1, §17 "authoritative" tier — distinct from the §17 LLM-judgment
smell tier). Read-only.

Usage: python3 failure_mode_lint.py <repo_path>

Checks (each cites the known-failure-modes.md category it proxies):
  1 bus_factor        People / "Single lead-coder bottleneck" (bus factor of 1)
  2 vcs_discipline    Process / "No version control/code review"
  3 god_opmode        Software+People silo / God class  [also named independently
                      in the SystemCore comparison material — cite both when it fires]
  4 missing_telemetry Measurement / "No pre-match checklists or telemetry"
  5 stale_pid         Software / "PID instability" (constants not retuned after a
                      mechanical change) — HEURISTIC proxy, see caveat in output
  7 template_default_tuning_constant
                      Software / physical tuning constant never measured — a constant sitting at
                      its template/library default value (standing-principles.md §13). Scoped to
                      fields a tuning PROCEDURE physically produces; policy caps and optional
                      damping terms are deliberately excluded (see the check's own note).
  6 mutable_static_opmode_write
                      Process/runtime-semantics / "Global mutable static / cross-opmode
                      persistence" (corpus-derived, Session 1). Scoped: a non-final public
                      static WRITTEN from an OpMode/command lifecycle method — not any static.
"""
import subprocess, sys, re, json, os, glob

def git(repo, *args):
    try:
        r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, timeout=90)
        return r.stdout
    except Exception:
        return ""

def code_files(repo):
    out = []
    for ext in ("*.java", "*.kt"):
        out += glob.glob(os.path.join(repo, "**", ext), recursive=True)
    # ignore build/generated/vendored SDK dirs
    skip = ("/build/", "/.git/", "/libs/", "/FtcRobotController/", "/gradle/")
    return [f for f in out if not any(s in f for s in skip)]

def read(f):
    try:
        return open(f, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

# ---------------------------------------------------------------- 1 bus factor
def check_bus_factor(repo):
    out = git(repo, "shortlog", "-sn", "--all", "--no-merges")
    authors = []
    for line in out.splitlines():
        m = re.match(r'\s*(\d+)\s+(.*)', line)
        if m:
            authors.append((int(m.group(1)), m.group(2).strip()))
    total = sum(n for n, _ in authors)
    f = []
    stats = {"distinct_authors": len(authors), "total_commits": total}
    if total >= 10 and authors:
        share = authors[0][0] / total
        stats["top_author_share"] = round(share, 3)
        if share >= 0.80:
            f.append({"check": "bus_factor", "severity": "high",
                      "category": "People / Single lead-coder bottleneck (bus factor ~1)",
                      "evidence": f"{authors[0][1]} authored {authors[0][0]}/{total} commits ({share:.0%}); {len(authors)} distinct authors",
                      "why": "Knowledge concentrated in one contributor; loss on graduation is high-impact and structural (known-failure-modes.md).",
                      "caveat": "STANDING CAVEAT: this is commit-author CONCENTRATION, not confirmed sole-authorship. A high share may reflect a squashed/curated public history (a public mirror of private team work) rather than actual single-author team process — especially on repos with few total commits. Do NOT state a bus-factor problem as settled; report it as a signal to investigate, and weigh any independent evidence of team strength."})
    return f, stats

# ------------------------------------------------------------- 2 vcs discipline
TRIVIAL = re.compile(r'^(update|fix|.|wip|stuff|changes|commit|\.+|test)$', re.I)
def check_vcs_discipline(repo):
    msgs = git(repo, "log", "--all", "--no-merges", "--pretty=%s").splitlines()
    dates = git(repo, "log", "--all", "--no-merges", "--pretty=%ad", "--date=short").splitlines()
    f = []
    stats = {"commits": len(msgs), "distinct_days": len(set(dates))}
    if msgs:
        trivial = sum(1 for m in msgs if TRIVIAL.match(m.strip()) or len(m.strip()) < 6)
        frac = trivial / len(msgs)
        stats["trivial_msg_frac"] = round(frac, 2)
        if len(msgs) < 8:
            f.append({"check": "vcs_discipline", "severity": "medium",
                      "category": "Process / No version control discipline",
                      "evidence": f"only {len(msgs)} non-merge commits across {len(set(dates))} day(s)",
                      "why": "Little version-control history — work is easily overwritten with no rollback (known-failure-modes.md)."})
        if frac >= 0.6 and len(msgs) >= 8:
            f.append({"check": "vcs_discipline", "severity": "low",
                      "category": "Process / No version control discipline",
                      "evidence": f"{trivial}/{len(msgs)} commit messages are trivial (e.g. 'update','fix','.')",
                      "why": "Poor commit-message discipline; design decisions become untraceable (known-failure-modes.md)."})
    return f, stats

# --------------------------------------------------------------- 3 god opmode
OPMODE = re.compile(r'@TeleOp|@Autonomous|extends\s+LinearOpMode|extends\s+OpMode|:\s*LinearOpMode|:\s*OpMode\b')
HWGET = re.compile(r'hardwareMap\s*\.\s*(get|dcMotor|servo|crservo|analogInput|digitalChannel|i2cDevice|colorSensor)')
def check_god_opmode(repo):
    f = []; scanned = 0; worst = None
    for path in code_files(repo):
        src = read(path)
        if not OPMODE.search(src):
            continue
        scanned += 1
        lines = src.count("\n") + 1
        hw = len(HWGET.findall(src))
        if lines > 300 and hw >= 6:
            rel = os.path.relpath(path, repo)
            f.append({"check": "god_opmode", "severity": "medium",
                      "category": "God OpMode — Software+People silo (known-failure-modes.md) AND named independently in the SystemCore comparison material",
                      "evidence": f"{rel}: {lines} lines, {hw} direct hardwareMap accesses in one OpMode",
                      "why": "Hardware wiring + control logic concentrated in one class — no subsystem separation; the interface-based architecture (PLAN §10) is the structural fix."})
    return f, {"opmodes_scanned": scanned}

# ---------------------------------------------------------- 4 missing telemetry
LOOP = re.compile(r'opModeIsActive|while\s*\(\s*!?\s*isStopRequested|for\s*\(')
# broadened: SDK telemetry, FTC Dashboard, and common framework tracers (e.g. TRC),
# and detected repo-wide (telemetry commonly lives in subsystems, not the OpMode file)
TELEM = re.compile(r'telemetry\s*\.\s*(addData|addLine|update)|FtcDashboard|TelemetryPacket'
                   r'|\.sendTelemetryPacket|globalTracer|TrcDbgTrace|tracer\s*\.\s*trace|Telemetry\s+\w+')
def check_missing_telemetry(repo):
    files = {p: read(p) for p in code_files(repo)}
    any_telem = any(TELEM.search(s) for s in files.values())
    opmodes = loop_opmodes = 0
    for s in files.values():
        if OPMODE.search(s):
            opmodes += 1
            if LOOP.search(s):
                loop_opmodes += 1
    f = []
    # repo-level signal only — file-local flagging is false-positive-prone under a
    # subsystem/command-based architecture where telemetry lives outside the OpMode.
    if loop_opmodes > 0 and not any_telem:
        f.append({"check": "missing_telemetry", "severity": "medium",
                  "category": "Measurement / No telemetry",
                  "evidence": f"{loop_opmodes} OpMode(s) with run loops and NO telemetry-like signal anywhere in the repo",
                  "why": "Intermittent faults become undiagnosable without telemetry; symptoms get fixed, not causes (known-failure-modes.md)."})
    return f, {"opmodes": opmodes, "opmodes_with_loops": loop_opmodes, "telemetry_signal_found": any_telem}

# ---------------------------------------------------------------- 5 stale PID
PID = re.compile(r'PIDFCoefficients|PIDCoefficients|\bk[PIDpid]\s*=|\bkF\s*=|setPIDF|new\s+PIDF?')
HWCONF = re.compile(r'hardwareMap|DcMotorEx|MecanumDrive|Drivetrain|RobotConfig|\.xml$', re.I)
def _last_commit_epoch(repo, path):
    out = git(repo, "log", "-1", "--format=%ct", "--", os.path.relpath(path, repo)).strip()
    return int(out) if out.isdigit() else 0
def check_stale_pid(repo):
    pid_files, hw_files = [], []
    for path in code_files(repo):
        src = read(path)
        if PID.search(src):
            pid_files.append(path)
        if re.search(r'hardwareMap|DcMotorEx|class\s+\w*(Drive|Drivetrain|Robot|Hardware)', src):
            hw_files.append(path)
    f = []
    stats = {"pid_files": len(pid_files), "hardware_files": len(hw_files)}
    if pid_files and hw_files:
        newest_pid = max(_last_commit_epoch(repo, p) for p in pid_files)
        newest_hw = max(_last_commit_epoch(repo, p) for p in hw_files)
        # heuristic: hardware config changed clearly AFTER the newest PID tune (> ~14 days)
        if newest_hw and newest_pid and (newest_hw - newest_pid) > 14 * 86400:
            days = (newest_hw - newest_pid) // 86400
            f.append({"check": "stale_pid", "severity": "low", "heuristic": True,
                      "category": "Software / PID instability after mechanical change",
                      "evidence": f"newest hardware-config commit is ~{days} days AFTER the newest PID-constant commit",
                      "why": "PID constants may not have been retuned after a later mechanical change (known-failure-modes.md). HEURISTIC — verify against actual commit history before trusting."})
    return f, stats

# ------------------------------------- 6 mutable static written in lifecycle method
# Global-mutable-static / cross-opmode persistence (known-failure-modes.md, corpus-derived).
# SCOPED narrowly (per review): flags a non-final public static ONLY when it is WRITTEN from
# inside an OpMode/command lifecycle method — NOT every non-final static (that would false-
# positive on ordinary static config constants and train people to ignore the check).
MUT_STATIC_DECL = re.compile(
    r'\bpublic\s+static\s+(?!final\b)(?:volatile\s+)?[A-Za-z_][\w.<>\[\]]*\s+([A-Za-z_]\w*)\s*[=;]')
# lifecycle method signatures whose body ends the match at the opening '{'
LIFECYCLE_SIG = re.compile(
    r'\bvoid\s+(?:runOpMode|init|init_loop|initialize|start|loop|stop|update|execute|periodic|end|run)\b'
    r'\s*\([^)]*\)\s*(?:throws[^;{]*)?\{')
def _brace_end(src, open_idx):
    depth = 0
    for i in range(open_idx, len(src)):
        c = src[i]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i + 1
    return len(src)
def check_mutable_static_opmode_write(repo):
    files = {p: read(p) for p in code_files(repo)}
    mut_global, mut_by_file = set(), {}
    for p, s in files.items():
        names = set(MUT_STATIC_DECL.findall(s))
        if names:
            mut_by_file[p] = names
            mut_global |= names
    f = []
    stats = {"mutable_public_statics": len(mut_global)}
    if not mut_global:
        return f, stats
    # qualified write to ANY repo mutable static:  Class.NAME <op>= (not ==)
    qual_re = re.compile(r'\b[A-Z]\w*\s*\.\s*(' + '|'.join(re.escape(n) for n in mut_global)
                         + r')\s*(?:[+\-*/%&|^]|<<|>>)?=(?!=)')
    hits = {}  # field -> set(relpath)
    for p, s in files.items():
        local = mut_by_file.get(p, set())
        # unqualified write only for statics DECLARED IN THIS FILE (else it's likely a local/instance)
        unq_re = (re.compile(r'(?<![\w.])(' + '|'.join(re.escape(n) for n in local)
                             + r')\s*(?:[+\-*/%&|^]|<<|>>)?=(?!=)') if local else None)
        for m in LIFECYCLE_SIG.finditer(s):
            open_idx = m.end() - 1  # position of '{'
            body = s[open_idx:_brace_end(s, open_idx)]
            for wm in qual_re.finditer(body):
                hits.setdefault(wm.group(1), set()).add(os.path.relpath(p, repo))
            if unq_re:
                for wm in unq_re.finditer(body):
                    hits.setdefault(wm.group(1), set()).add(os.path.relpath(p, repo))
    stats["fields_written_in_lifecycle"] = len(hits)
    if hits:
        items = sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        sample = ", ".join(f"{fld} ({len(ps)} file/s)" for fld, ps in items[:6])
        # SEVERITY TIERED by count/breadth (a run across the corpus showed a binary 'medium'
        # equated 3543's single 'alliance' field with 19043's 23 — training readers to ignore it).
        # medium = a genuine spread (>=5 such fields, OR one written across >=5 files); else low.
        widest = max(len(ps) for ps in hits.values())
        severity = "medium" if (len(hits) >= 5 or widest >= 5) else "low"
        stats["severity"] = severity
        f.append({"check": "mutable_static_opmode_write", "severity": severity,
                  "category": "Process/runtime-semantics — Global mutable static / cross-opmode persistence (known-failure-modes.md, corpus-derived Session 1)",
                  "evidence": f"{len(hits)} non-final public-static field(s) ASSIGNED inside OpMode/command lifecycle methods (widest: {widest} file/s), e.g. {sample}",
                  "why": "Statics live on the app process and outlive a LinearOpMode run; state written during a run silently carries into the NEXT run. Invisible in code review AND in single-match testing (a static only leaks into the FOLLOWING run) — surfaces as a 'behaved differently for no reason' symptom read as a hardware/environment flake (known-failure-modes.md).",
                  "caveat": "SIGNAL, not a settled bug: a static UNCONDITIONALLY RESET on an init path before its first read is safe. Flag = go verify each of these is reset each run. A live-tunable @Config static is fine ONLY if also reset per run."})
    return f, stats

# ------------------------- 7 tuning constant left at a template/library default value
# Physical-tuning-constant hallucination control (standing-principles.md §13). A tuning constant
# sitting at its template/library default is a strong, CHECKABLE signal that a robot is running on
# somebody else's numbers: the code compiles, deploys, and drives — wrongly, and silently.
#
# DEFAULT VALUES BELOW ARE VERIFIED, NOT RECALLED. Each was read from the real current upstream
# source at the fetch date noted; re-verify on the R107 shelf-life cadence, these are external-
# project facts with an expiration date.
#
#   RoadRunner   acmerobotics/road-runner-quickstart @ master, MecanumDrive.java `Params`
#                (fetched 2026-08-05)
#   Pedro        THREE sources, because Pedro has three distinct live default sets (fetched
#                2026-08-05, all read from the real upstream repos):
#                  - Pedro-Pathing/PedroPathing @ main — the *library* class field initializers.
#                    These are the dangerous ones: Pedro's current quickstart Constants.java ships
#                    `new FollowerConstants()` with NO numbers at all, so the library's own values
#                    apply SILENTLY to any team that never calls the corresponding builder method.
#                    Nothing appears in team code to review, and nothing looks unset.
#                  - Pedro-Pathing/Beginner-Quickstart @ master — a team-editable FollowerConstants
#                    with example numbers (mass = 10.65942, distinct from the library's 10.65).
#                  - Pedro-Pathing/Quickstart-1.0.9 @ master — Pedro 0.x FConstants/LConstants,
#                    a third set again (mass = 13, forwardZeroPowerAcceleration = -41.278).
#
# SCOPED DELIBERATELY — a naive "any field at its default" check was tested against a real tier-1
# corpus repo (15993, RoadRunner) and would have fired on 8 of 20 `Params` fields that are
# LEGITIMATELY left alone: maxWheelVel, min/maxProfileAccel, maxAngVel, maxAngAccel and the three
# *VelGain fields are policy caps and optional damping terms, not measurements of a robot. Flagging
# those trains people to ignore the check. Only fields a tuning PROCEDURE physically produces are
# in `PHYSICAL`; controller gains shipped as placeholders are separated into `GAIN` at lower
# severity.
#
# A FIELD MAPS TO A TUPLE OF DEFAULTS, NOT ONE — and that is the whole point for Pedro. Checking a
# single value set would have left the more dangerous cases open. Four distinct Pedro sources ship
# DIFFERENT numbers for the same physical field, all of them plausible, none of them this robot's:
#
#   field                        library (current)   Beginner-Quickstart   Quickstart-1.0.9
#   mass                         10.65               10.65942              13
#   forwardZeroPowerAcceleration -34.62719           -34.62719             -41.278
#   lateralZeroPowerAcceleration -78.15554           -78.15554             -59.7819
#   xVelocity / xMovement        81.34056            81.34056              57.8741
#   yVelocity / yMovement        65.43028            65.43028              52.295
#
# 10.65 vs 10.65942 is NOT bridged by the near-match tolerance below (they differ by ~9x it), so
# the library-only table genuinely missed the quickstart values and vice versa. Old-API field
# aliases (xMovement/yMovement, leftY/rightY/strafeX) are included because a repo on Pedro 0.x
# uses those names for the same physical quantities.
PHYSICAL, GAIN = "physical", "gain"
TEMPLATE_DEFAULTS = {
    "roadrunner": {
        # RoadRunner is the mirror-image case: its defaults live in the QUICKSTART's `Params`
        # class (the library ships no such numbers), so one source covers it.
        # field:            (defaults, tier, what actually produces the real value)
        "inPerTick":        ((1.0,),   PHYSICAL, "ForwardPushTest"),
        "trackWidthTicks":  ((0.0,),   PHYSICAL, "AngularRampLogger"),
        "kS":               ((0.0,),   PHYSICAL, "ForwardRampLogger"),
        "kV":               ((0.0,),   PHYSICAL, "ForwardRampLogger"),
        "kA":               ((0.0,),   PHYSICAL, "ManualFeedforwardTuner"),
        "axialGain":        ((0.0,),   GAIN,     "ManualFeedbackTuner"),
        "lateralGain":      ((0.0,),   GAIN,     "ManualFeedbackTuner"),
        "headingGain":      ((0.0,),   GAIN,     "ManualFeedbackTuner"),
    },
    "pedro_pathing": {
        # --- follower / drivetrain (all three Pedro sources) ---
        "mass":                          ((10.65, 10.65942, 13.0), PHYSICAL, "weigh the robot"),
        "forwardZeroPowerAcceleration":  ((-34.62719, -41.278), PHYSICAL, "ForwardZeroPowerAccelerationTuner"),
        "lateralZeroPowerAcceleration":  ((-78.15554, -59.7819), PHYSICAL, "LateralZeroPowerAccelerationTuner"),
        "xVelocity":                     ((81.34056, 57.8741, 80.0), PHYSICAL, "ForwardVelocityTuner"),
        "yVelocity":                     ((65.43028, 52.295, 80.0), PHYSICAL, "StrafeVelocityTuner"),
        "xMovement":                     ((81.34056, 57.8741), PHYSICAL, "ForwardVelocityTuner (Pedro 0.x name for xVelocity)"),
        "yMovement":                     ((65.43028, 52.295), PHYSICAL, "StrafeVelocityTuner (Pedro 0.x name for yVelocity)"),
        # --- localizers: Pinpoint / ThreeWheel / TwoWheel / DriveEncoder / OTOS ---
        "forwardPodY":                   ((1.0,),    PHYSICAL, "measure the pod offset on the robot"),
        "strafePodX":                    ((-2.5,),   PHYSICAL, "measure the pod offset on the robot"),
        "leftPodY":                      ((1.0,),    PHYSICAL, "measure the pod offset on the robot"),
        "rightPodY":                     ((-1.0,),   PHYSICAL, "measure the pod offset on the robot"),
        "leftY":                         ((1.0,),    PHYSICAL, "measure the pod offset (Pedro 0.x name)"),
        "rightY":                        ((-1.0,),   PHYSICAL, "measure the pod offset (Pedro 0.x name)"),
        "strafeX":                       ((-2.5,),   PHYSICAL, "measure the pod offset (Pedro 0.x name)"),
        "forwardTicksToInches":          ((0.001989436789, 1.0), PHYSICAL, "ForwardTuner"),
        "strafeTicksToInches":           ((0.001989436789, 1.0), PHYSICAL, "LateralTuner"),
        "turnTicksToInches":             ((0.001989436789, 1.0), PHYSICAL, "TurnTuner"),
        "robot_Width":                   ((1.0,),    PHYSICAL, "measure the robot"),
        "robot_Length":                  ((1.0,),    PHYSICAL, "measure the robot"),
        "linearScalar":                  ((1.0,),    PHYSICAL, "OTOSLinearScalarTuner"),
        "angularScalar":                 ((1.0,),    PHYSICAL, "OTOSAngularScalarTuner"),
        # --- gains / placeholders ---
        "centripetalScaling":            ((0.0005,), GAIN,     "CentripetalTuner"),
        "translationalPIDFFeedForward":  ((0.015,),  GAIN,     "translational PIDF tuning"),
        "headingPIDFFeedForward":        ((0.01,),   GAIN,     "heading PIDF tuning"),
        "drivePIDFFeedForward":          ((0.01,),   GAIN,     "drive PIDF tuning"),
    },
}
# `name(value)` builder call (Pedro) or `name = value` field assignment (RoadRunner/plain Java).
_NUM = r'(-?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?|-?\.\d+)'
def _assign_re(field):
    # Lookbehind excludes \w only, NOT '.', because Pedro's entire constants API is a builder
    # chain — `.mass(10.65)`, `.xVelocity(81.34056)`. Excluding '.' (the obvious first guess, and
    # what this originally did) silently matched nothing on every Pedro repo while still passing
    # on RoadRunner's plain `field = value` form. Caught by running a synthetic Pedro positive,
    # not by reading the regex.
    return re.compile(r'(?<!\w)' + re.escape(field) + r'\s*(?:=\s*|\(\s*)' + _NUM)
# RoadRunner's quickstart ships `lateralInPerTick = inPerTick`. Left as-is it means LateralPushTest
# was never run — a distinct signal from a numeric match, so it gets its own pattern.
_LATERAL_ALIAS = re.compile(r'lateralInPerTick\s*=\s*inPerTick\s*;')

# The RoadRunner quickstart's TuningOpModes designates the live drive class in one place.
_DRIVE_CLASS = re.compile(r'DRIVE_CLASS\s*=\s*(\w+)\s*\.class')
def _live_drive_class(srcs):
    for path, src in srcs.items():
        if os.path.basename(path) != "TuningOpModes.java":
            continue
        m = _DRIVE_CLASS.search(src)
        if m:
            return m.group(1)
    return None

def _near(a, b):
    # near-match, not just equality: a truncated copy of a default (-34.627 for -34.62719) is the
    # same borrowed number, and is exactly how a default gets laundered into looking measured.
    if b == 0.0:
        return a == 0.0
    return abs(a - b) <= abs(b) * 1e-4

def check_template_default_tuning(repo):
    f = []
    stats = {"files_with_tuning_constants": 0, "physical_at_default": 0, "gains_at_default": 0}
    # Read every file ONCE. The liveness fallback below compares against all other files, so
    # re-reading per hit is O(n^2) — it timed out on a real repo before this cache existed.
    srcs = {p: read(p) for p in code_files(repo)}
    for path, src in srcs.items():
        if not re.search(r'FollowerConstants|MecanumConstants|\w+Constants\s*\(|class\s+Params\b'
                         r'|inPerTick|trackWidthTicks', src):
            continue
        lib = "pedro_pathing" if "pedropathing" in src.lower() or "FollowerConstants" in src \
              else ("roadrunner" if ("inPerTick" in src or "trackWidthTicks" in src) else None)
        if lib is None:
            continue
        stats["files_with_tuning_constants"] += 1
        rel = os.path.relpath(path, repo)
        hits = []
        for field, (defaults, tier, procedure) in TEMPLATE_DEFAULTS[lib].items():
            for m in _assign_re(field).finditer(src):
                try:
                    val = float(m.group(1))
                except ValueError:
                    continue
                if any(_near(val, d) for d in defaults):
                    line = src[:m.start()].count("\n") + 1
                    hits.append((field, val, tier, procedure, line))
                break   # first assignment per field is the declaration; later ones are usually reads
        if lib == "roadrunner" and _LATERAL_ALIAS.search(src):
            line = src[:_LATERAL_ALIAS.search(src).start()].count("\n") + 1
            hits.append(("lateralInPerTick", "inPerTick (template expression, unchanged)",
                         PHYSICAL, "LateralPushTest", line))
        if not hits:
            continue
        # Is this class the one the robot actually drives on? The RoadRunner quickstart vendors
        # BOTH MecanumDrive and TankDrive into TeamCode; a mecanum team never runs TankDrive, so
        # its untuned constants are dead template scaffolding, not a robot on borrowed numbers.
        #
        # Found by running this check across the real corpus, not predicted: a tier-1 mecanum repo
        # reported 4 high-severity findings in TankDrive.java — the same "trains readers to ignore
        # the check" failure this check is already scoped against. An "is it instantiated" test does
        # NOT resolve it: the quickstart's own tuning OpModes do construct TankDrive, but only
        # inside `DRIVE_CLASS.equals(TankDrive.class)` branches that are dead when DRIVE_CLASS is
        # MecanumDrive. So read the selector the template itself designates as the answer, rather
        # than inferring liveness — grounded in the quickstart's convention, not a guess about it.
        cls = os.path.basename(path)[:-5]
        live = _live_drive_class(srcs)
        if live is not None and cls in ("MecanumDrive", "TankDrive"):
            used_elsewhere = (cls == live)
        else:
            used_elsewhere = any(
                re.search(r'(?<![\w.])' + re.escape(cls) + r'\s*(?:\(|\w)', osrc)
                for other, osrc in srcs.items() if other != path)
        phys = [h for h in hits if h[2] == PHYSICAL]
        gains = [h for h in hits if h[2] == GAIN]
        stats["physical_at_default"] += len(phys)
        stats["gains_at_default"] += len(gains)
        if not used_elsewhere:
            stats.setdefault("unreferenced_classes", []).append(rel)
        for group, tier, sev in ((phys, PHYSICAL, "high"), (gains, GAIN, "low")):
            if not group:
                continue
            if not used_elsewhere:
                sev = "low"
            ev = "; ".join(f"{n} = {v} (line {ln}) — real value comes from {proc}"
                           for n, v, _, proc, ln in group)
            f.append({
                "check": "template_default_tuning_constant", "severity": sev, "tier": tier,
                "category": "Software / physical tuning constant never measured "
                            "(standing-principles.md §13; Software / PID instability in "
                            "known-failure-modes.md)",
                "evidence": f"{rel} [{lib}]: {len(group)} constant(s) at the template/library "
                            f"default — {ev}"
                            + ("" if used_elsewhere else
                               f"  [NOTE: `{cls}` is not referenced anywhere else in this repo — "
                               f"likely unused vendored template scaffolding, severity lowered]"),
                "why": ("A physical constant cannot be derived from documentation or reasoning — it "
                        "only comes off a specific robot. A default left in place is another "
                        "robot's number: it compiles, deploys, and drives, so nothing fails until "
                        "path following is wrong on a field."
                        if tier == PHYSICAL else
                        "Controller gain still at its shipped placeholder — the loop is running "
                        "with no tuned correction term."),
                "caveat": ("SIGNAL, not a settled bug: a default can coincidentally equal a real "
                           "measured value, and a team may legitimately not have tuned yet. The "
                           "finding is 'this number's origin is unverified', which is exactly what "
                           "team-config's `tuning_constants.origin` field is meant to record. "
                           "Defaults are external-project facts with a shelf life (R107) — "
                           "re-verify them against the library's current source before treating a "
                           "non-match as proof of tuning."),
            })
    return f, stats

CHECKS = [check_bus_factor, check_vcs_discipline, check_god_opmode, check_missing_telemetry,
          check_stale_pid, check_mutable_static_opmode_write, check_template_default_tuning]

def main():
    if len(sys.argv) < 2:
        print("usage: failure_mode_lint.py <repo_path>"); sys.exit(2)
    repo = sys.argv[1]
    findings, stats = [], {}
    for chk in CHECKS:
        fs, st = chk(repo)
        findings += fs
        stats[chk.__name__.replace("check_", "")] = st
    result = {"repo": os.path.basename(repo.rstrip("/")), "findings": findings, "stats": stats}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
