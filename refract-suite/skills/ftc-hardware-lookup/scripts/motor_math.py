#!/usr/bin/env python3
"""Deterministic FTC motor/drivetrain arithmetic (R30). The model NEVER computes these numbers;
it calls this script and reports the output. Every base value comes from the catalog files, cited
there. The script ABSTAINS (exit 3, clear message) on any part not in the catalog — a coverage gap
is an abstention, never a guess (R38, INDEX.json abstain_rule).

Subcommands:
  spec        <PART>                             — dump the catalog record + its source (no math)
  external    <PART> --driver T --driven T       — add an external gear/belt/chain stage
  wheel-speed <PART> --wheel-mm D [--ext R]       — free-running linear wheel speed (m/s, ft/s)
  ticks       <PART> --wheel-mm D [--ext R]       — encoder ticks per meter of wheel travel

Unit conversions (kg.cm/oz-in -> N.m) are done here, deterministically, from the catalog's
as-published values — the catalog never stores a pre-baked conversion.

Usage: motor_math.py <subcommand> <PART> [options]   (PART = catalog SKU, e.g. 5203-2402-0019)
"""
import argparse
import json
import math
import sys
from pathlib import Path

KGCM_TO_NM = 0.0980665
OZIN_TO_NM = 0.00706155


def load_catalog():
    root = Path(__file__).resolve().parent.parent / "references" / "catalogs"
    parts = {}
    for f in ("motors.json", "servos.json"):
        fp = root / f
        if fp.exists():
            data = json.loads(fp.read_text())
            for sku, rec in data.get("parts", {}).items():
                rec["_catalog_file"] = f
                parts[sku] = rec
    return parts


def get_part(parts, sku):
    if sku not in parts:
        # ABSTAIN — do not guess. This is the enforcement point for INDEX.json's abstain_rule.
        print(json.dumps({
            "abstain": True,
            "reason": f"'{sku}' is not in the verified catalog. I don't have a sourced spec for it.",
            "do_not": "Do not fill this from memory — report the abstention and point to the manufacturer page.",
            "known_skus": sorted(parts.keys()),
        }, indent=2))
        sys.exit(3)
    return parts[sku]


def stall_nm(rec):
    st = rec.get("stall_torque_published")
    if not st:
        return None, "stall torque not listed for this part (manufacturer page did not publish it)"
    unit = st["unit"]
    if unit == "N.m":
        return st["value"], f"{st['value']} N.m (published)"
    if unit == "kg.cm":
        nm = round(st["value"] * KGCM_TO_NM, 4)
        return nm, f"{st['value']} kg.cm published -> {nm} N.m (converted, 1 kg.cm=0.0980665 N.m)"
    if unit == "oz-in":
        nm = round(st["value"] * OZIN_TO_NM, 4)
        return nm, f"{st['value']} oz-in published -> {nm} N.m (converted)"
    return None, f"unrecognized torque unit {unit}"


def out_rpm(rec):
    for k in ("no_load_rpm_output", "free_speed_rpm"):
        if k in rec:
            return rec[k], k
    return None, None


def out_cpr(rec, ext_ratio=1.0):
    if "encoder_cpr_output" in rec:
        return rec["encoder_cpr_output"], "encoder_cpr_output (published at output shaft)"
    if "encoder_cpr_motor" in rec:
        # bare motor: output CPR depends on the gearbox the user actually attaches
        return rec["encoder_cpr_motor"] * ext_ratio, f"{rec['encoder_cpr_motor']} motor CPR * external {ext_ratio}"
    return None, "no encoder resolution listed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["spec", "external", "wheel-speed", "ticks"])
    ap.add_argument("part")
    ap.add_argument("--driver", type=float, help="driving gear/pulley teeth")
    ap.add_argument("--driven", type=float, help="driven gear/pulley teeth")
    ap.add_argument("--ext", type=float, default=None, help="external reduction ratio (driven/driver) directly")
    ap.add_argument("--wheel-mm", type=float, help="wheel diameter in mm (from the team's confirmed config)")
    args = ap.parse_args()

    parts = load_catalog()
    rec = get_part(parts, args.part)
    src = rec.get("_source", {})

    ext = args.ext
    if ext is None and args.driver and args.driven:
        ext = args.driven / args.driver
    ext = ext or 1.0

    base_rpm, rpm_key = out_rpm(rec)
    result = {"part": args.part, "name": rec.get("name"),
              "source": {"url": src.get("url"), "tier": src.get("tier"), "retrieved": src.get("retrieved")}}

    if args.cmd == "spec":
        result["record"] = {k: v for k, v in rec.items() if not k.startswith("_catalog")}

    elif args.cmd == "external":
        if base_rpm is None:
            print(json.dumps({"abstain": True, "reason": "no output speed listed for this part"})); sys.exit(3)
        nm, nm_note = stall_nm(rec)
        result["external_stage"] = {"ratio_driven_over_driver": round(ext, 4)}
        result["output_rpm_after_stage"] = round(base_rpm / ext, 2)
        if nm is not None:
            result["output_stall_torque_nm_ideal"] = round(nm * ext, 4)
            result["torque_note"] = f"ideal (no efficiency loss); base {nm_note}; real torque is lower — gearboxes/belts lose 10-30%"
        result["speed_note"] = f"base output {base_rpm} rpm ({rpm_key}); divided by external ratio {round(ext,4)}"

    elif args.cmd == "wheel-speed":
        if base_rpm is None or not args.wheel_mm:
            print(json.dumps({"abstain": True, "reason": "need both an output RPM (from catalog) and --wheel-mm (from config)"})); sys.exit(3)
        rpm = base_rpm / ext
        circ_m = math.pi * (args.wheel_mm / 1000.0)
        mps = rpm / 60.0 * circ_m
        result["free_wheel_speed_m_s"] = round(mps, 3)
        result["free_wheel_speed_ft_s"] = round(mps * 3.28084, 3)
        result["assumptions"] = {"output_rpm": round(rpm, 1), "wheel_diameter_mm": args.wheel_mm,
                                 "external_ratio": round(ext, 4),
                                 "note": "FREE speed (no load); real drivetrain speed is lower. Wheel diameter is a config input, not a catalog value."}

    elif args.cmd == "ticks":
        cpr, cpr_note = out_cpr(rec, ext)
        if cpr is None or not args.wheel_mm:
            print(json.dumps({"abstain": True, "reason": "need encoder CPR (catalog) and --wheel-mm (config)"})); sys.exit(3)
        circ_m = math.pi * (args.wheel_mm / 1000.0)
        result["ticks_per_meter"] = round(cpr / circ_m, 2)
        result["ticks_per_wheel_rev"] = cpr
        result["cpr_source"] = cpr_note

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
