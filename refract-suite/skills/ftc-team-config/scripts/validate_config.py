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

# --- physical-tuning-constant enforcement (standing-principles §13) ---------------------------
# These two sets are the STRUCTURAL enforcement of "a fabricated-but-plausible tuning constant is
# never acceptable output". They are closed on purpose. There is no `estimated`, `default`,
# `typical`, or `library_recommended` origin, so a number has no representable form in this schema
# unless it is asserted to have been measured on this specific robot. A model that wants to emit a
# reasonable-sounding guess has nowhere to put it — the failure is a validation error at config
# time, not a wrong constant discovered on a field.
TUNING_ORIGINS = {"measured", "untuned"}
# Groups whose constants are GEOMETRIC: a number in one of these is meaningless without knowing the
# axis convention it was stated in, so `frame` is mandatory there (core-feature-model.yaml's
# tuning_constants.frame_required_categories). Read from the model rather than duplicated, so a new
# category is added in one place.
FRAME_REQUIRED_DEFAULT = ["localizer", "goal_positions", "mechanism_offsets", "poses"]
TUNING_STATUS = {"not_yet_tunable", "untuned", "tuned"}
# Keys inside a tuning entry that are metadata, not nested constants.
_ENTRY_KEYS = {"value", "origin", "units", "source", "confirmed", "tuning_procedure_ref", "notes"}


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

    # No team-config.yaml yet is a normal, expected state (a fresh repo, before any elicitation) —
    # not a crash. Treat it as an empty config: every mandatory field falls out as unconfirmed via
    # the existing logic below, same as a sparse-but-present file. `config_found` lets a caller
    # distinguish "nothing confirmed yet" from "file exists but incomplete".
    config_found = cfg_path.exists()
    cfg = (yaml.safe_load(cfg_path.read_text()) or {}) if config_found else {}
    errors, warnings, unconfirmed = [], [], []

    core_axes = {k: v for k, v in core.items() if not k.startswith("_")}

    # --- 1. core-axis validation (R3) ---
    for axis, fields in cfg.items():
        if axis in ("_meta", "team", "season_mechanisms", "archetypes", "config_history",
                    "device_map", "tuning_constants", "reference_frames", "device_ownership",
                    "cross_opmode_state"):
            # device_map/tuning_constants are [generative]: their KEY SET is derived per team, so
            # they can't be checked against a fixed field list. Dedicated checks 5 and 6 below.
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

    # --- 5. device_map (generative key set; free-form name strings) ---
    # A wrong device name fails LOUDLY at init, so this block gates generation only on being
    # confirmed — not on any name-shape rule. There is deliberately no naming convention enforced:
    # a survey of 578 team-authored hardwareMap.get() calls across 16 mined repos found 105
    # distinct names in four different casing styles, with the front-left drive motor alone
    # spelled `leftFront`, `lf`, and `motorFrontLeft`. Any convention check would be wrong for
    # most real teams.
    dmap = cfg.get("device_map") or {}
    if not isinstance(dmap, dict):
        errors.append("device_map must be a mapping of device-key -> {value, source, confirmed}")
        dmap = {}
    for dev, node in dmap.items():
        value, ok = unwrap(node)
        if not isinstance(value, str) or not value:
            errors.append(f"device_map.{dev} must carry a non-empty hardwareMap name string, got {value!r}")
        elif value.strip() != value:
            # leading/trailing whitespace in a hardwareMap name is a real, silent init failure
            errors.append(f"device_map.{dev} = {value!r} has leading/trailing whitespace — "
                          f"hardwareMap names match exactly")
        if not ok:
            unconfirmed.append(f"device_map.{dev}")

    # --- 6. tuning_constants — the hard rule, enforced here (standing-principles §13) ---
    tc = cfg.get("tuning_constants")
    _tuning_entries = {}
    pathing = resolve("software_stack.pathing")
    if tc is None:
        if pathing not in (None, "none"):
            unconfirmed.append("tuning_constants (missing; required once software_stack.pathing "
                               f"= {pathing!r} — set tuning_status at minimum)")
    elif not isinstance(tc, dict):
        errors.append("tuning_constants must be a mapping")
    else:
        status, status_ok = unwrap(tc.get("tuning_status"))
        if status is None:
            unconfirmed.append("tuning_constants.tuning_status (missing)")
        elif status not in TUNING_STATUS:
            errors.append(f"tuning_constants.tuning_status = {status!r} not in {sorted(TUNING_STATUS)}")
        elif not status_ok:
            unconfirmed.append("tuning_constants.tuning_status")

        measured, untuned_n = [], []

        def check_entry(path, node):
            """One leaf constant. This is where a fabricated value becomes a hard error."""
            origin = node.get("origin")
            value = node.get("value")
            if origin is None:
                errors.append(f"tuning_constants.{path}: no `origin` — every physical constant must "
                              f"declare where its number came from")
                return
            if origin not in TUNING_ORIGINS:
                # The single most important line in this file. `estimated`, `default`, `typical`,
                # `library_recommended` and every other invented origin die here.
                errors.append(
                    f"tuning_constants.{path}: origin {origin!r} is not one of {sorted(TUNING_ORIGINS)}. "
                    f"A physical tuning constant is either carried forward from a real measurement on "
                    f"this robot (`measured`) or has no number at all (`untuned`). There is no third "
                    f"state by design — see standing-principles.md §13.")
                return
            if origin == "untuned":
                untuned_n.append(path)
                if value is not None:
                    errors.append(
                        f"tuning_constants.{path}: origin `untuned` but carries value {value!r}. "
                        f"An untuned constant must be null. A plausible number under an `untuned` "
                        f"label is exactly the failure this schema exists to make unrepresentable.")
                return
            # origin == measured
            measured.append(path)
            if value is None:
                errors.append(f"tuning_constants.{path}: origin `measured` but value is null — "
                              f"a measurement with no number is not a measurement")
            if not bool(node.get("confirmed", False)):
                unconfirmed.append(f"tuning_constants.{path}")

        def walk(prefix, node):
            for k, v in node.items():
                if k in ("tuning_status", "notes") or k.startswith("_"):
                    continue
                path = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict) and ("origin" in v or "value" in v):
                    _tuning_entries[path] = v
                if not isinstance(v, dict):
                    errors.append(f"tuning_constants.{path}: bare value {v!r} — a physical constant "
                                  f"must be a mapping carrying `origin` (see standing-principles §13)")
                elif "origin" in v or "value" in v or (set(v) & _ENTRY_KEYS):
                    check_entry(path, v)
                else:
                    walk(path, v)   # a grouping level (e.g. Pedro's follower/mecanum/localizer split)

        walk("", tc)

        # status/entry coherence — a claim of `tuned` that still has untuned constants under it is
        # a config that would read as ready and generate real numbers for a robot that has none.
        if status == "tuned" and untuned_n:
            errors.append(f"tuning_constants.tuning_status = 'tuned' but {len(untuned_n)} constant(s) "
                          f"still have origin `untuned`: {', '.join(sorted(untuned_n)[:6])}"
                          + (" ..." if len(untuned_n) > 6 else ""))
        if status in ("untuned", "not_yet_tunable") and measured:
            warnings.append(f"tuning_constants.tuning_status = {status!r} but {len(measured)} constant(s) "
                            f"are marked `measured` — if real values exist, status is probably 'tuned'")

    # --- 7. reference_frames + frame tagging (R123) ---
    # A coordinate's correctness is a property of the number AND the frame it is stated in.
    # `origin: measured` covers the first and is silent on the second.
    frames = cfg.get("reference_frames") or {}
    conversions = []
    if isinstance(frames, dict):
        conversions = frames.get("_conversions") or []
    declared_frames = {k for k in frames if not k.startswith("_")} if isinstance(frames, dict) else set()
    for fname in sorted(declared_frames):
        node = frames[fname]
        if not isinstance(node, dict):
            errors.append(f"reference_frames.{fname} must be a mapping describing the frame")
            continue
        if not bool(node.get("confirmed", False)):
            unconfirmed.append(f"reference_frames.{fname}")
    conv_index = set()
    for c in conversions if isinstance(conversions, list) else []:
        if not isinstance(c, dict):
            continue
        fr, to = c.get("from"), c.get("to")
        for side, val in (("from", fr), ("to", to)):
            if val not in declared_frames:
                errors.append(f"reference_frames._conversions: '{side}: {val}' is not a declared frame")
        if c.get("status") == "declared" and bool(c.get("confirmed", False)):
            conv_index.add((fr, to))

    frame_required = set(
        (core.get("tuning_constants") or {}).get("frame_required_categories") or FRAME_REQUIRED_DEFAULT
    )
    if tc and isinstance(tc, dict):
        for path, entry in _tuning_entries.items():
            group = path.split(".")[0] if "." in path else ""
            fr = entry.get("frame")
            if fr is not None and fr not in declared_frames:
                errors.append(
                    f"tuning_constants.{path}: frame {fr!r} is not declared in reference_frames. "
                    f"A free-text frame name is the original bug wearing a label — two constants "
                    f"can both say 'field' and mean different things.")
            elif group in frame_required and fr is None and entry.get("value") is not None:
                # UNCONFIRMED, not an error. An undeclared frame NAME is malformed (above) — but a
                # config written before this dimension existed is incomplete, not wrong, and the
                # suite already has a precise word for that. This keeps `valid` meaning "well
                # formed" and routes the real consequence through generation_allowed, where a
                # missing frame belongs: it is a question to ask, not a file to reject.
                unconfirmed.append(
                    f"tuning_constants.{path}.frame (geometric constant in group '{group}' with a "
                    f"value but no frame — measured and confirmed is not the same as unambiguous)")
    # More than one frame in play with no confirmed conversion between them is the exact
    # precondition for a silent mismatch — surface it rather than waiting for it to bite.
    if len(declared_frames) > 1:
        missing = [f"{a} -> {b}" for a in sorted(declared_frames) for b in sorted(declared_frames)
                   if a != b and (a, b) not in conv_index]
        if missing:
            warnings.append(
                f"{len(declared_frames)} reference frames declared with no confirmed conversion for: "
                f"{', '.join(missing[:4])}{' ...' if len(missing) > 4 else ''}. Generation will refuse "
                f"to cross an undeclared conversion rather than guess one.")

    # --- 8. device_ownership: exactly one owner per (device, opmode_type) (R125) ---
    own = cfg.get("device_ownership") or []
    if own and not isinstance(own, list):
        errors.append("device_ownership must be a list of {device, owner, opmode_type} entries")
        own = []
    seen_owner = {}
    for e in own:
        if not isinstance(e, dict):
            continue
        dev, owner, ot = e.get("device"), e.get("owner"), e.get("opmode_type", "both")
        if dev not in dmap:
            errors.append(f"device_ownership: '{dev}' is not a key in device_map")
        for scope in (["auto", "teleop"] if ot == "both" else [ot]):
            key = (dev, scope)
            if key in seen_owner and seen_owner[key] != owner:
                errors.append(
                    f"device_ownership: '{dev}' claimed by BOTH {seen_owner[key]!r} and {owner!r} "
                    f"in {scope}. Two subsystems constructing one device is a silent conflict — the "
                    f"second hardwareMap.get() succeeds and both write to the same hardware.")
            seen_owner[key] = owner
        if not bool(e.get("confirmed", False)):
            unconfirmed.append(f"device_ownership.{dev}[{ot}]")

    # --- 9. cross_opmode_state: the handoff channel (R126) ---
    xstate = cfg.get("cross_opmode_state") or []
    if xstate and not isinstance(xstate, list):
        errors.append("cross_opmode_state must be a list")
        xstate = []
    for e in xstate:
        if not isinstance(e, dict):
            continue
        fld = e.get("field")
        if e.get("written_by") == e.get("read_by"):
            warnings.append(f"cross_opmode_state.{fld}: written and read by the same opmode type — "
                            f"that is ordinary state, not a cross-opmode handoff")
        if e.get("required_before_read") and not e.get("staleness_guard"):
            errors.append(
                f"cross_opmode_state.{fld}: required_before_read is true but no `staleness_guard` is "
                f"declared. Without one, a teleop run standalone reads whatever the last auto left "
                f"(or a default) and nothing distinguishes that from a fresh handoff.")
        if not bool(e.get("confirmed", False)):
            unconfirmed.append(f"cross_opmode_state.{fld}")

    result = {
        "valid": not errors,
        "generation_allowed": not errors and not unconfirmed,
        "active_season": active_slug,
        "config_found": config_found,
        "errors": errors,
        "warnings": warnings,
        "unconfirmed_mandatory": unconfirmed,
    }
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
