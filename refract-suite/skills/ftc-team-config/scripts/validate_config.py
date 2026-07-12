#!/usr/bin/env python3
"""Deterministic team-config validator (R3, R7, R50, R55 support).

Validates a team-config.yaml against:
  1. core-feature-model.yaml axes            — every value must come from a declared axis (R3)
  2. the ACTIVE season extension's mechanisms — season mechanism values from its declared lists
  3. constraints_on_core                      — e.g. fixed_shooter_on_swerve requires swerve (R7)
  4. the mandatory-ask set                    — present AND confirmed before generation (R50/R55)

Output: JSON {valid, errors, warnings, unconfirmed_mandatory} on stdout. Exit 1 if invalid.
Usage: validate_config.py <team-config.yaml> [--suite-root <path>]

Field values may be plain scalars (treated as UNCONFIRMED) or dicts:
  {value: mecanum, source: inferred|asked, confirmed: true|false}
Only confirmed: true satisfies the mandatory set — an inferred value is a pre-fill, not a decision.
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(json.dumps({"valid": False, "errors": ["pyyaml not installed"]}))
    sys.exit(1)

MANDATORY = [
    # §13/§15: asked/confirmed regardless of inferability — they gate too much to risk a bad guess.
    "drivetrain.type",
    "software_stack.pathing",
    "software_stack.opmode_style",
    "season_mechanisms",  # the season's mechanism set as a whole
]


def find_suite_root(start: Path) -> Path:
    # Plugin layout: the shared foundation is $CLAUDE_PLUGIN_ROOT/ftc-shared-foundation. If the env
    # var is unset, derive the plugin root from this script's own location
    # (scripts -> skill -> skills -> PLUGIN_ROOT). Fall back to the source-repo walk for dev use.
    import os
    cands = []
    pr = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if pr:
        cands.append(Path(pr) / "ftc-shared-foundation")
    cands.append(Path(__file__).resolve().parents[3] / "ftc-shared-foundation")
    for c in cands:
        if (c / "core-feature-model.yaml").exists():
            return c
    for p in [start, *start.parents]:
        if (p / "core-feature-model.yaml").exists():
            return p
    raise FileNotFoundError("core-feature-model.yaml not found (plugin or source layout)")


def unwrap(node):
    """Return (value, confirmed) from either a plain scalar or a {value, confirmed} dict."""
    if isinstance(node, dict) and "value" in node:
        return node["value"], bool(node.get("confirmed", False))
    return node, False  # plain scalar = present but unconfirmed


def allowed_values(axis_node):
    """A leaf list in the model = the allowed values. 'number'/'optional' = free-typed."""
    if isinstance(axis_node, list):
        return axis_node
    return None


def main():
    args = sys.argv[1:]
    if not args:
        print(json.dumps({"valid": False, "errors": ["usage: validate_config.py <team-config.yaml>"]}))
        sys.exit(1)
    cfg_path = Path(args[0])
    if "--suite-root" in args:
        suite = Path(args[args.index("--suite-root") + 1])
    else:
        suite = find_suite_root(Path(__file__).resolve())

    core = yaml.safe_load((suite / "core-feature-model.yaml").read_text())
    active_slug = (suite / "season-extensions" / "ACTIVE").read_text().strip()
    season = yaml.safe_load((suite / "season-extensions" / f"{active_slug}.yaml").read_text())

    cfg = yaml.safe_load(cfg_path.read_text()) or {}
    errors, warnings, unconfirmed = [], [], []

    core_axes = {k: v for k, v in core.items() if not k.startswith("_")}

    # --- 1. core-axis validation (R3) ---
    for axis, fields in cfg.items():
        if axis in ("_meta", "team", "season_mechanisms", "archetypes", "config_history"):
            continue
        if axis not in core_axes:
            errors.append(f"unknown core axis '{axis}' — not in core-feature-model.yaml")
            continue
        if not isinstance(fields, dict):
            warnings.append(f"'{axis}' should be a mapping of fields")
            continue
        for field, node in fields.items():
            value, _ = unwrap(node)
            model_node = core_axes[axis].get(field) if isinstance(core_axes[axis], dict) else None
            if model_node is None:
                # nested variant blocks (e.g. drivetrain.mecanum.*) — validate one level down
                type_val, _ = unwrap(cfg[axis].get("type", {}))
                variant = core_axes[axis].get(type_val) if type_val else None
                if isinstance(variant, dict) and field in variant:
                    model_node = variant[field]
                elif isinstance(core_axes[axis].get(field), dict):
                    model_node = core_axes[axis][field]
                else:
                    # unknown field under a known axis: check variant sub-blocks before erroring
                    known_anywhere = any(
                        isinstance(v, dict) and field in v for v in core_axes[axis].values()
                    )
                    if not known_anywhere:
                        errors.append(f"unknown field '{axis}.{field}'")
                        continue
            allowed = allowed_values(model_node)
            if allowed is not None and value not in allowed:
                errors.append(f"'{axis}.{field}' = {value!r} not in declared axis {allowed}")

    # --- 2. season mechanisms ---
    mechs = cfg.get("season_mechanisms", {})
    declared = season.get("season_mechanisms", {})
    for mech, node in (mechs or {}).items():
        value, _ = unwrap(node)
        decl = declared.get(mech)
        opts = decl if isinstance(decl, list) else (decl or {}).get("options") if isinstance(decl, dict) else None
        if decl is None:
            errors.append(f"season mechanism '{mech}' not declared in {active_slug}.yaml")
        elif opts and value not in opts:
            errors.append(f"season_mechanisms.{mech} = {value!r} not in {opts}")

    # --- 3. constraints_on_core (R7) ---
    for c in season.get("constraints_on_core", []) or []:
        arch = c.get("archetype")
        if arch and arch in (cfg.get("archetypes") or []):
            for path, required in (c.get("requires") or {}).items():
                # path like core.drivetrain.type
                parts = path.split(".")[1:]  # drop leading 'core'
                node = cfg
                for p in parts:
                    node = node.get(p, {}) if isinstance(node, dict) else {}
                actual, _ = unwrap(node)
                if actual != required:
                    errors.append(
                        f"constraint violated: archetype '{arch}' requires {path}={required!r}, config has {actual!r}"
                    )

    # --- 3b. constraints_on_mechanisms (generic if/requires; eval-2 gap patch) ---
    def resolve(dotted):
        node = cfg
        for p in dotted.split("."):
            node = node.get(p) if isinstance(node, dict) else None
            if node is None:
                return None
        v, _ = unwrap(node)
        return v

    def cond_ok(actual, expected):
        if isinstance(expected, dict) and "not" in expected:
            return actual != expected["not"]
        return actual == expected

    for c in season.get("constraints_on_mechanisms", []) or []:
        conds = c.get("if") or {}
        resolved = {k: resolve(k) for k in conds}
        if any(v is None for v in resolved.values()):
            continue  # a field the config doesn't declare can't trigger the constraint
        if all(cond_ok(resolved[k], v) for k, v in conds.items()):
            for k, v in (c.get("requires") or {}).items():
                if not cond_ok(resolve(k), v):
                    errors.append(
                        f"mechanism constraint violated: {c.get('reason', k)} — requires {k} "
                        f"{json.dumps(v)}, config has {resolve(k)!r}"
                    )

    # --- 4. mandatory-ask set confirmed (R50/R55) ---
    for m in MANDATORY:
        if m == "season_mechanisms":
            if not mechs:
                unconfirmed.append("season_mechanisms (none recorded)")
            else:
                for mech, node in mechs.items():
                    _, ok = unwrap(node)
                    if not ok:
                        unconfirmed.append(f"season_mechanisms.{mech}")
            continue
        axis, field = m.split(".")
        node = (cfg.get(axis) or {}).get(field)
        if node is None:
            unconfirmed.append(f"{m} (missing)")
        else:
            _, ok = unwrap(node)
            if not ok:
                unconfirmed.append(m)

    result = {
        "valid": not errors,
        "generation_allowed": not errors and not unconfirmed,
        "active_season": active_slug,
        "errors": errors,
        "warnings": warnings,
        "unconfirmed_mandatory": unconfirmed,
    }
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
