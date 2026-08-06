#!/usr/bin/env python3
"""
ftc-construct — physical tuning constants: emit them, then prove nothing else got in (R114).

WHY THIS SCRIPT EXISTS. `core-feature-model.yaml` + `validate_config.py` already make a fabricated
tuning constant unrepresentable IN THE CONFIG (standing-principles §13: `origin` is a closed set of
{measured, untuned}, a number cannot be recorded without asserting it was measured on this robot).
That closes the AUTHORING path. It does not close the GENERATION path: generated Java is model
output, and nothing stopped a model from typing a plausible number straight into a `.mass(...)`
call that never passed through the config at all.

`failure_mode_lint.py`'s `template_default_tuning_constant` check was the only backstop, and its
coverage boundary is real and was measured: given `.mass(13.2)` — an invented value that is not any
library or template default — it correctly reports nothing, because knowing every default in the
world says nothing about an arbitrary number.

So this script eliminates the failure mode structurally instead of trying to catch it after the
fact, the same way `motor_math.py` eliminates invented motor specs — not by instructing a model to
be careful, but by making the value come from a lookup:

  render  — the model writes STRUCTURE with `{{tuning.<field>}}` / `{{device.<key>}}` placeholders
            and never types a tuning number. Substitution is a dict lookup against the confirmed
            config. A measured+confirmed constant renders as its exact value; anything else renders
            as a loud fail-fast marker, never a plausible number.
  verify   — scans generated code for numeric literals in tuning-field positions and requires each
            to match the confirmed config EXACTLY. This is the part that actually closes the gap:
            it does not need to recognise a value as "a default" or "invented", only as
            "not the number the config says". Any literal with no config provenance is an error.

Usage:
  emit_tuning.py render <template_file> --config <team-config.yaml> [-o <out>]
  emit_tuning.py verify <code_path>     --config <team-config.yaml>

verify exits 1 on any violation. Read-only in both modes unless -o is given.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(json.dumps({"ok": False, "errors": ["pyyaml not installed"]}))
    sys.exit(1)

# The generated-code form of "no value here, and do not let this be mistaken for one". NaN is the
# convention this suite already uses for an ungroundable number (a spec outside the seeded catalog):
# it propagates, it is never silently plausible, and it fails loudly the moment it reaches hardware.
UNTUNED_LITERAL = "Double.NaN"

_NUM = r'(-?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?|-?\.\d+)'
_PLACEHOLDER = re.compile(r'\{\{\s*(tuning|device)\.([A-Za-z0-9_.]+)\s*\}\}')


def strip_comments(src):
    """Blank out Java comments, preserving offsets so reported line numbers stay right.

    Necessary, and found by running the checks against real generated output rather than by
    reading them: a generated file that WARNS against copying Pedro's defaults ("do NOT copy
    mass = 10.65 ...") was itself flagged for containing those numbers. A tuning-constant check
    that fires on prose telling people not to use a value is worse than useless — it trains
    readers to ignore the one check that catches the silent case.
    """
    out, i, n = [], 0, len(src)
    state = None  # None | 'line' | 'block' | 'str' | 'char'
    while i < n:
        c = src[i]
        nxt = src[i + 1] if i + 1 < n else ''
        if state is None:
            if c == '/' and nxt == '/':
                state = 'line'; out.append('  '); i += 2; continue
            if c == '/' and nxt == '*':
                state = 'block'; out.append('  '); i += 2; continue
            if c == '"':
                state = 'str'
            elif c == "'":
                state = 'char'
            out.append(c); i += 1; continue
        if state == 'line':
            if c == '\n':
                state = None; out.append(c)
            else:
                out.append(' ')
            i += 1; continue
        if state == 'block':
            if c == '*' and nxt == '/':
                state = None; out.append('  '); i += 2; continue
            out.append(c if c == '\n' else ' '); i += 1; continue
        # inside a string/char literal
        if c == '\\':
            out.append(c); out.append(nxt); i += 2; continue
        if (state == 'str' and c == '"') or (state == 'char' and c == "'"):
            state = None
        out.append(c); i += 1
    return ''.join(out)


def load_config(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def flatten_tuning(cfg: dict) -> dict:
    """Leaf tuning constants, keyed BOTH by dotted path and by bare field name.

    Bare-name keying is what lets `verify` work on generated Java, where `.mass(14.45)` carries no
    trace of which config group the value came from. A bare name that is ambiguous (the same leaf
    under two groups with different values) is recorded as a conflict and treated as un-lookupable
    rather than silently resolved to one of them.
    """
    out, bare, conflicts = {}, {}, set()
    tc = cfg.get("tuning_constants") or {}

    def walk(prefix, node):
        for k, v in node.items():
            if k in ("tuning_status", "notes") or k.startswith("_"):
                continue
            path = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict) and ("origin" in v or "value" in v):
                out[path] = v
                if k in bare and bare[k] is not v:
                    prev = bare[k]
                    if prev.get("value") != v.get("value") or prev.get("origin") != v.get("origin"):
                        conflicts.add(k)
                bare[k] = v
            elif isinstance(v, dict):
                walk(path, v)

    if isinstance(tc, dict):
        walk("", tc)
    for k in conflicts:
        bare.pop(k, None)
    return {"by_path": out, "by_name": bare, "ambiguous": sorted(conflicts)}


def entry_value(entry: dict):
    """(rendered_literal, is_real_number, reason). The ONLY place a number becomes output."""
    origin = entry.get("origin")
    if origin == "measured" and bool(entry.get("confirmed", False)) and entry.get("value") is not None:
        return repr(entry["value"]), True, "measured"
    if origin == "measured":
        return UNTUNED_LITERAL, False, "measured but unconfirmed or valueless — not usable"
    return UNTUNED_LITERAL, False, "untuned"


# --------------------------------------------------------------------------- render
def cmd_render(args):
    cfg = load_config(Path(args.config))
    tuning = flatten_tuning(cfg)
    devices = cfg.get("device_map") or {}
    src = Path(args.template).read_text()
    errors, substitutions = [], []

    def sub(m):
        kind, key = m.group(1), m.group(2)
        if kind == "device":
            node = devices.get(key)
            if node is None:
                errors.append(f"device_map has no entry '{key}' — hand back to ftc-team-config "
                              f"rather than inventing a hardwareMap name")
                return m.group(0)
            value = node.get("value") if isinstance(node, dict) else node
            if not (isinstance(node, dict) and node.get("confirmed")):
                errors.append(f"device_map.{key} is not confirmed")
            substitutions.append({"placeholder": m.group(0), "rendered": f'"{value}"'})
            return f'"{value}"'
        entry = tuning["by_path"].get(key) or tuning["by_name"].get(key)
        if entry is None:
            if key in tuning["ambiguous"]:
                errors.append(f"tuning field '{key}' is ambiguous (same leaf name under multiple "
                              f"groups with different values) — use the full dotted path")
            else:
                errors.append(f"tuning_constants has no entry '{key}' — a tuning field with no "
                              f"config provenance must not be generated (standing-principles §13)")
            return m.group(0)
        literal, real, reason = entry_value(entry)
        substitutions.append({"placeholder": m.group(0), "rendered": literal, "reason": reason})
        return literal

    rendered = _PLACEHOLDER.sub(sub, src)
    # Attach the real procedure to every field that rendered as untuned — a marker with no
    # instruction is a dead end for the team that has to actually fix it.
    todos = []
    for path, entry in sorted(tuning["by_path"].items()):
        _, real, _ = entry_value(entry)
        if not real:
            todos.append({"field": path,
                          "procedure_ref": entry.get("tuning_procedure_ref"),
                          "units": entry.get("units")})
    result = {"ok": not errors, "errors": errors, "substitutions": substitutions,
              "untuned_fields": todos}
    if args.out and not errors:
        Path(args.out).write_text(rendered)
        result["written"] = args.out
    else:
        result["rendered"] = rendered
    print(json.dumps(result, indent=2))
    sys.exit(0 if not errors else 1)


# --------------------------------------------------------------------------- verify
def _known_fields(tuning):
    names = set(tuning["by_name"]) | {p.rsplit(".", 1)[-1] for p in tuning["by_path"]}
    # Fields the config may legitimately omit but which are still physical constants: reuse
    # failure_mode_lint's default table as the vocabulary, read by path rather than duplicated.
    try:
        lint = (Path(__file__).resolve().parents[2] / "ftc-code-review" / "scripts"
                / "failure_mode_lint.py").read_text()
        ns = {}
        blk = lint[lint.index("TEMPLATE_DEFAULTS = {"):]
        blk = blk[:blk.index("\n}\n") + 3]
        exec("PHYSICAL, GAIN = 'physical', 'gain'\n" + blk, ns)
        for tbl in ns["TEMPLATE_DEFAULTS"].values():
            names |= set(tbl)
    except Exception:
        pass  # vocabulary shrinks to the config's own fields; still closes the config-backed cases
    return names


def cmd_verify(args):
    cfg = load_config(Path(args.config))
    tuning = flatten_tuning(cfg)
    fields = _known_fields(tuning)
    root = Path(args.code_path)
    files = [root] if root.is_file() else [p for p in root.rglob("*.java")
                                           if "/build/" not in str(p) and "/libs/" not in str(p)]
    violations, checked = [], 0
    for path in files:
        # Comment-stripped: a TODO(UNTUNED) comment naming a library default must not itself
        # trip the check it exists to explain. See strip_comments().
        src = strip_comments(path.read_text(errors="replace"))
        for field in fields:
            pat = re.compile(r'(?<!\w)' + re.escape(field) + r'\s*(?:=\s*|\(\s*)' + _NUM)
            for m in pat.finditer(src):
                checked += 1
                literal = m.group(1)
                line = src[:m.start()].count("\n") + 1
                entry = tuning["by_name"].get(field)
                if entry is None:
                    violations.append({
                        "file": str(path), "line": line, "field": field, "literal": literal,
                        "reason": "no confirmed tuning_constants entry for this field — a physical "
                                  "constant with no config provenance (standing-principles §13)"})
                    continue
                expected, real, why = entry_value(entry)
                if not real:
                    violations.append({
                        "file": str(path), "line": line, "field": field, "literal": literal,
                        "reason": f"config says {why}; generated code must carry "
                                  f"{UNTUNED_LITERAL}, not a number"})
                elif float(literal) != float(entry["value"]):
                    violations.append({
                        "file": str(path), "line": line, "field": field, "literal": literal,
                        "expected": entry["value"],
                        "reason": "does not match the confirmed measured value — a tuning constant "
                                  "is carried forward verbatim, never regenerated or adjusted"})
    print(json.dumps({"ok": not violations, "files_scanned": len(files),
                      "tuning_literals_checked": checked, "violations": violations}, indent=2))
    sys.exit(0 if not violations else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("render"); r.add_argument("template"); r.add_argument("--config", required=True)
    r.add_argument("-o", "--out"); r.set_defaults(func=cmd_render)
    v = sub.add_parser("verify"); v.add_argument("code_path"); v.add_argument("--config", required=True)
    v.set_defaults(func=cmd_verify)
    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
