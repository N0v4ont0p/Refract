#!/usr/bin/env python3
"""Config-constraint check (R40/R34): flag robot code that references a mechanism the team's
CONFIRMED config declares absent. A team with turret:none should have no turret code — if it does,
it's either dead weight (stale) or a config mismatch. Either way the human confirms, not the model.

  config_lint.py <code_dir> [--config team-config.yaml] [--self-test]

Deterministic. Output JSON {findings:[{mechanism, token, files}]}, exit 1 if any finding.

ponytail: token grep over .java/.kt, could match a comment or a same-named unrelated symbol. That's
fine — this flags for HUMAN confirmation ("confirm if stale"), it doesn't auto-delete. Tighten the
token map only if a real repo shows noise.
"""
import argparse, json, re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    print(json.dumps({"error": "pyyaml not installed"})); sys.exit(2)

# mechanism key -> identifier tokens that would appear in code for it
TOKENS = {
    "turret": ["Turret"], "shooter": ["Shooter", "Flywheel", "Launcher"],
    "intake": ["Intake"], "gate_mechanism": ["Gate"], "classifier_interaction": ["Classifier"],
}


def val(node):
    return node["value"] if isinstance(node, dict) and "value" in node else node


def find_config(explicit):
    if explicit:
        return Path(explicit)
    for p in (Path("team-config.yaml"), *Path(".").rglob("team-config.yaml")):
        if p.exists():
            return p
    return None


def check(code_dir, config_path):
    cfg = yaml.safe_load(Path(config_path).read_text()) or {}
    mechs = cfg.get("season_mechanisms", {})
    absent = {k: TOKENS[k] for k, node in mechs.items() if k in TOKENS and val(node) == "none"}
    files = [p for p in Path(code_dir).rglob("*") if p.suffix in (".java", ".kt")]
    findings = []
    for mech, tokens in absent.items():
        hits = {}
        pat = re.compile(r"\b(" + "|".join(tokens) + r")\w*", re.I if False else 0)
        for f in files:
            try:
                if pat.search(f.read_text(errors="ignore")):
                    hits.setdefault(mech, []).append(str(f))
            except Exception:
                pass
        if hits.get(mech):
            findings.append({"mechanism": mech, "tokens": tokens, "files": hits[mech],
                             "note": f"config declares {mech}: none, but code references it — "
                                     f"not referenced by current config; confirm if stale or a config mismatch"})
    return {"config": str(config_path), "code_dir": str(code_dir),
            "declared_absent": list(absent), "findings": findings, "clean": not findings}


def _self_test():
    import tempfile, os
    d = tempfile.mkdtemp()
    Path(d, "team-config.yaml").write_text(
        "season_mechanisms:\n  turret: {value: none, confirmed: true}\n  shooter: {value: flywheel, confirmed: true}\n")
    src = Path(d, "src"); src.mkdir()
    (src / "TurretSubsystem.java").write_text("class TurretSubsystem {}")
    (src / "Shooter.java").write_text("class Shooter {}")
    r = check(src, Path(d, "team-config.yaml"))
    assert not r["clean"] and r["findings"][0]["mechanism"] == "turret", r
    assert all(f["mechanism"] != "shooter" for f in r["findings"]), "shooter is declared, must not flag"
    print("self-test OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("code_dir", nargs="?")
    ap.add_argument("--config")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return _self_test()
    cfg = find_config(a.config)
    if not cfg:
        print(json.dumps({"error": "no team-config.yaml found; run ftc-team-config first"})); sys.exit(2)
    r = check(a.code_dir or ".", cfg)
    print(json.dumps(r, indent=2))
    sys.exit(1 if r["findings"] else 0)


if __name__ == "__main__":
    main()
