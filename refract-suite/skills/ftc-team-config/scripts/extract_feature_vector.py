#!/usr/bin/env python3
"""
Static feature-vector extraction (§14.2 step 1) — SCRIPT ONLY, NO MODEL.

Fills a core-feature-model instance for one team's repo by detecting import/class
signatures deterministically. Anything not recoverable from code (hardware BOM,
wheel diameter/durometer, fabrication, expansion-hub count, team experience) is
emitted as "unknown" — NEVER guessed (operating rule 1; §13 inference-before-
elicitation: only what a script can recover with certainty). Every asserted value
carries file+line evidence.

Usage: python3 extract_feature_vector.py <repo_path> [team_label]
Output: JSON feature-vector instance to stdout.
"""
import sys, os, re, glob, json

SIGS = {
    # axis, value : list of regex signatures
    ("software_stack.pathing", "pedro_pathing"): [r'com\.pedropathing', r'\bpedropathing\b', r'\bPedroPathing\b'],
    ("software_stack.pathing", "roadrunner"): [r'com\.acmerobotics\.roadrunner', r'\bRoadRunner\b', r'roadrunner'],
    ("software_stack.opmode_style", "ftclib_command_based"): [r'com\.arcrobotics\.ftclib\.command', r'\bCommandOpMode\b', r'\bCommandScheduler\b', r'\bSubsystemBase\b', r'extends\s+CommandBase'],
    ("software_stack.opmode_style", "raw_linear_opmode"): [r'extends\s+LinearOpMode', r'extends\s+OpMode\b', r':\s*LinearOpMode'],
    # G2 (Phase G): recognize TickTree as a legitimate library dependency, not hand-rolled
    # orchestration code — same reason FTCLib's CommandScheduler gets its own signature above
    # instead of being silently attributed to the team (see 19859-J's provenance note).
    ("software_stack.behavior_layer", "ticktree"): [r'io\.github\.n0v4ont0p\.ticktree', r'\bBehaviorTree\b', r'\bOpModeTreeRunner\b'],
    ("sensing.vision", "limelight_3a"): [r'Limelight3A', r'limelightvision', r'\bLimelight\b'],
    ("sensing.vision", "webcam_easyopencv"): [r'org\.openftc\.easyopencv', r'OpenCvCamera', r'EasyOpenCV'],
    ("sensing.odometry", "goBILDA_pinpoint"): [r'Pinpoint', r'GoBildaPinpoint', r'GoBildaPinpointDriver'],
    ("sensing.odometry", "otos"): [r'SparkFunOTOS', r'\bOTOS\b'],
    ("sensing.odometry", "dead_wheels"): [r'ThreeWheel', r'TwoWheel', r'DeadWheel', r'StandardTrackingWheelLocalizer', r'ThreeDeadWheel'],
    ("drivetrain.type", "mecanum"): [r'\bMecanumDrive\b', r'\bmecanum\b', r'MecanumKinematics', r'MecanumDrivetrain'],
    ("drivetrain.type", "swerve"): [r'\bSwerveModule\b', r'\bSwerveDrive\b', r'\bswerve\b'],
    ("drivetrain.type", "tank_differential"): [r'\bTankDrive\b', r'DifferentialDrive'],
}
# control-system evidence => REV Control Hub (the only FTC-legal option this season)
REV_SIG = [r'hardwareMap', r'com\.qualcomm\.robotcore', r'DcMotorEx', r'RevHubOrientation']

SKIP = ("/build/", "/.git/", "/libs/", "/FtcRobotController/", "/gradle/", "/.gradle/")

def code_files(repo):
    out = []
    for ext in ("*.java", "*.kt"):
        out += glob.glob(os.path.join(repo, "**", ext), recursive=True)
    return [f for f in out if not any(s in f for s in SKIP)]

def scan(repo):
    hits = {}   # (axis,value) -> [evidence]
    rev = []
    lang = {"java": 0, "kotlin": 0}
    for path in code_files(repo):
        rel = os.path.relpath(path, repo)
        lang["kotlin" if path.endswith(".kt") else "java"] += 1
        try:
            lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
            for (axis, val), sigs in SIGS.items():
                for s in sigs:
                    if re.search(s, line):
                        ev = hits.setdefault((axis, val), [])
                        if len(ev) < 3:
                            ev.append(f"{rel}:{i}")
                        break
            if len(rev) < 3:
                for s in REV_SIG:
                    if re.search(s, line):
                        rev.append(f"{rel}:{i}"); break
    return hits, rev, lang

def resolve(hits, axis):
    """Pick detected value(s) for an axis; multiple => list with evidence; none => unknown."""
    found = {v: ev for (a, v), ev in hits.items() if a == axis}
    if not found:
        return {"value": "unknown", "evidence": []}
    if len(found) == 1:
        v, ev = next(iter(found.items()))
        return {"value": v, "evidence": ev}
    return {"value": sorted(found.keys()), "evidence": {v: ev for v, ev in found.items()}, "note": "multiple detected — human to disambiguate primary"}

def main():
    repo = sys.argv[1]
    team = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(repo.rstrip("/"))
    hits, rev, lang = scan(repo)
    fv = {
        "team": team,
        "extracted_by": "extract_feature_vector.py (deterministic, no model)",
        "language": "kotlin" if lang["kotlin"] > lang["java"] else "java",
        "language_file_counts": lang,
        "drivetrain": {"type": resolve(hits, "drivetrain.type"),
                       "mecanum_wheel_source": {"value": "unknown", "evidence": [], "note": "BOM/CAD not in code"},
                       "wheel_diameter_mm": "unknown", "wheel_durometer": "unknown"},
        "control_hardware": {
            "hub_generation": ({"value": "REV_Control_Hub", "evidence": rev, "note": "FTC SDK usage present; REV is the sole legal option this season"} if rev else {"value": "unknown", "evidence": []}),
            "expansion_hub_count": {"value": "unknown", "note": "not reliably recoverable from code"}},
        "sensing": {"vision": resolve(hits, "sensing.vision"),
                    "odometry": resolve(hits, "sensing.odometry")},
        "software_stack": {"pathing": resolve(hits, "software_stack.pathing"),
                           "opmode_style": resolve(hits, "software_stack.opmode_style"),
                           "behavior_layer": resolve(hits, "software_stack.behavior_layer")},
        "fabrication": {"capability": {"value": "unknown", "note": "not recoverable from code — needs BOM/CAD/human"}},
        "team_context": {"experience": {"value": "unknown", "note": "not recoverable from code"}},
    }
    print(json.dumps(fv, indent=2))

if __name__ == "__main__":
    main()
