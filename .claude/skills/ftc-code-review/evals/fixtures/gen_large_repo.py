#!/usr/bin/env python3
"""Generate a realistic multi-file FTC repo that is too large to read exhaustively — so the
determinism advantage (linters fire every time; a skimming reviewer misses buried needles) is
actually stressed. Deterministic output (no randomness). Usage: gen_large_repo.py <out_dir>

Three NEEDLES buried among ~20 plausible files:
  N1 config mismatch : hardware/TurretController.java (config says turret:none)
  N2 mutable static  : opmodes/TeleOpMain.java — public static autoAlignOffset written in runOpMode
  N3 god opmode      : TeleOpMain.java (>400 lines, many hardwareMap)
Plus a shared-ancestry signal: subsystems/Shooter.java imports SolversLib command framework.
"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "large-repo")
TC = OUT / "TeamCode"


def w(rel, text):
    p = TC / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def subsystem(name, hw_lines, methods):
    body = [f"package org.firstinspires.ftc.teamcode.subsystems;",
            "import com.qualcomm.robotcore.hardware.DcMotor;",
            "import com.qualcomm.robotcore.hardware.HardwareMap;",
            f"public class {name} {{",
            "    private DcMotor a, b;",
            "    public void init(HardwareMap hw) {"]
    for i in range(hw_lines):
        body.append(f'        a = hw.get(DcMotor.class, "{name.lower()}{i}");')
    body.append("    }")
    for m in range(methods):
        body += [f"    public double compute{m}(double x) {{",
                 "        double acc = 0;",
                 *[f"        acc += x * {k}.0 / ({k}.0 + 1);" for k in range(1, 12)],
                 "        return acc;",
                 "    }"]
    body.append("}")
    return "\n".join(body) + "\n"


def main():
    w("../team-config.yaml",
      "_meta: {schema: 1}\nteam: {number: 45021, experience: veteran}\n"
      "drivetrain: {type: {value: mecanum, confirmed: true}}\n"
      "software_stack: {opmode_style: {value: raw_linear_opmode, confirmed: true}, pathing: {value: none, confirmed: true}}\n"
      "fabrication: {capability: {value: cnc_aluminum_or_carbon, confirmed: true}}\n"
      "season_mechanisms:\n  intake: {value: roller, confirmed: true}\n  shooter: {value: flywheel, confirmed: true}\n"
      "  turret: {value: none, confirmed: true}\n  gate_mechanism: {value: none, confirmed: true}\n"
      "  classifier_interaction: {value: none, confirmed: true}\n  endgame_parking: {value: mandatory, confirmed: true}\n")

    # plausible subsystems (realistic filler, not obviously junk)
    for name, hw, meth in [("Drivetrain", 4, 14), ("Intake", 2, 10), ("Vision", 2, 12),
                           ("Odometry", 3, 14), ("Climber", 2, 10), ("Lighting", 1, 8),
                           ("Deposit", 2, 12), ("Hang", 2, 10), ("Sensors", 3, 12)]:
        w(f"subsystems/{name}.java", subsystem(name, hw, meth))

    # Shooter with SolversLib command import (shared-ancestry signal)
    w("subsystems/Shooter.java",
      "package org.firstinspires.ftc.teamcode.subsystems;\n"
      "import com.seattlesolvers.solverslib.command.SubsystemBase;\n"
      "import com.qualcomm.robotcore.hardware.DcMotorEx;\n"
      "public class Shooter extends SubsystemBase {\n"
      "    private DcMotorEx fly;\n"
      "    public void spinUp(double rpm) { fly.setVelocity(rpm); }\n"
      "    public double ff(double d) { double a=0; for(int k=1;k<15;k++) a+=d*k/(k+0.5); return a; }\n}\n")

    # control helpers (more realistic bulk)
    for name in ("PIDController", "MotionProfile", "Kinematics", "FeedForward", "Localizer", "PathFollower", "Filters"):
        w(f"control/{name}.java",
          f"package org.firstinspires.ftc.teamcode.control;\npublic class {name} {{\n" +
          "".join(f"    public double step{i}(double e) {{ double u=0; for(int k=1;k<20;k++) u+=e*{i}.0/k; return u; }}\n" for i in range(16)) +
          "}\n")

    # autonomous opmodes (several, plausible)
    for auto in ("AutoBlueLeft", "AutoBlueRight", "AutoRedLeft", "AutoRedRight"):
        lines = ["package org.firstinspires.ftc.teamcode.opmodes;",
                 "import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;",
                 f"public class {auto} extends LinearOpMode {{",
                 "    @Override public void runOpMode() {",
                 '        var d = hardwareMap.get(Object.class, "drive");',
                 "        waitForStart();"]
        lines += [f'        telemetry.addData("step{i}", {i});' for i in range(40)]
        lines += ["    }", "}"]
        w(f"opmodes/{auto}.java", "\n".join(lines) + "\n")

    # N3 GOD OPMODE + N2 MUTABLE STATIC (buried deep in a 400+ line file)
    g = ["package org.firstinspires.ftc.teamcode.opmodes;",
         "import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;",
         "public class TeleOpMain extends LinearOpMode {",
         "    // tuning carried between runs so drivers don't re-tune each match",
         "    public static double autoAlignOffset = 0.0;   // N2: non-final public static",
         "    @Override public void runOpMode() {"]
    for m in ["fl", "fr", "bl", "br", "intake", "shoot", "climb"]:
        g.append(f'        var {m} = hardwareMap.get(Object.class, "{m}");')
    g.append("        autoAlignOffset += 0.05;   // N2: written from lifecycle, NOT reset -> real persistence")
    g.append("        waitForStart();")
    g.append("        while (opModeIsActive()) {")
    for i in range(360):
        g.append(f'            telemetry.addData("d{i}", {i} + autoAlignOffset);')
    g += ["        }", "    }", "}"]
    w("opmodes/TeleOpMain.java", "\n".join(g) + "\n")

    # N1 CONFIG MISMATCH: turret code buried in hardware/, config says turret:none
    w("hardware/TurretController.java",
      "package org.firstinspires.ftc.teamcode.hardware;\n"
      "import com.qualcomm.robotcore.hardware.Servo;\n"
      "// Turret azimuth control.\n"
      "public class TurretController {\n"
      "    private Servo azimuth;\n"
      "    public void pointAt(double headingDeg) { azimuth.setPosition(headingDeg / 360.0); }\n"
      "    public double solveLead(double range) { double a=0; for(int k=1;k<10;k++) a+=range/k; return a; }\n}\n")

    total = sum(len(p.read_text().splitlines()) for p in TC.rglob("*.java"))
    files = len(list(TC.rglob("*.java")))
    print(f"generated {files} java files, {total} lines under {TC}")


if __name__ == "__main__":
    main()
