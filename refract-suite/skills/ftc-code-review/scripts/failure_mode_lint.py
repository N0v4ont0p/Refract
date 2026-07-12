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

CHECKS = [check_bus_factor, check_vcs_discipline, check_god_opmode, check_missing_telemetry,
          check_stale_pid, check_mutable_static_opmode_write]

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
