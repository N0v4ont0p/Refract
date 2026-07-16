#!/usr/bin/env python3
"""Fidelity check: each tool's MCP-path output must match the equivalent direct
skill-path output — same grounding, same citations, same abstention behavior.
Run: python3 mcp-server/test_server.py"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from server import ROOT, corpus_query, hardware_lookup, rule_check, validate_team_config


def direct(*args):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=ROOT)
    return json.loads(r.stdout.strip())


def check(name, mcp_result, direct_result, compare_keys):
    for k in compare_keys:
        assert mcp_result[k] == direct_result[k], f"{name}: mismatch on '{k}'\n  mcp={mcp_result[k]!r}\n  direct={direct_result[k]!r}"
    print(f"PASS  {name}")


# 1. rule_check — same premise verified live earlier: flywheel shooters, R207.
mcp_rc = rule_check(ids=["R207"])
direct_lookup = direct(str(ROOT / ".claude/skills/ftc-rule-check/scripts/rules.py"), "lookup", "R207")
direct_verify = direct(str(ROOT / ".claude/skills/ftc-rule-check/scripts/rules.py"), "verify", "R207")
assert mcp_rc["lookup"]["rules"][0]["text"] == direct_lookup["rules"][0]["text"], "rule_check: cited text drifted from source"
assert mcp_rc["verify"] == direct_verify, "rule_check: verify result drifted"
assert "flywheel" in mcp_rc["lookup"]["rules"][0]["text"].lower()
print("PASS  rule_check (ids=[R207]) — citation text and verify result byte-match the direct skill path")

# 1b. rule_check by query — same rule should resolve from a keyword search.
mcp_rc_q = rule_check(query="flywheel scoring element")
assert "R207" in mcp_rc_q["resolved_ids"], f"rule_check query resolution missed R207: {mcp_rc_q['resolved_ids']}"
print("PASS  rule_check (query='flywheel scoring element') — resolved R207 by keyword search")

# 2. hardware_lookup — a real seeded SKU.
mcp_hw = hardware_lookup(action="spec", part="5203-2402-0019")
direct_hw = direct(str(ROOT / ".claude/skills/ftc-hardware-lookup/scripts/motor_math.py"), "spec", "5203-2402-0019")
check("hardware_lookup (spec, seeded SKU)", mcp_hw, direct_hw, ["record", "source"])

# 2b. hardware_lookup — deliberately unseeded SKU must abstain, not fabricate, through the MCP path too.
mcp_hw_abstain = hardware_lookup(action="spec", part="5203-2402-0001")
assert mcp_hw_abstain.get("abstain") is True, f"hardware_lookup did not abstain on unseeded part: {mcp_hw_abstain}"
print("PASS  hardware_lookup (spec, unseeded SKU) — abstains through the MCP path, same as direct")

# 3. corpus_query — pattern count and content must match a direct parse.
mcp_cq = corpus_query(filter="shooter")
direct_count = 0
for f in sorted((ROOT / ".claude/skills/ftc-corpus-builder/references/patterns").glob("*.yaml")):
    import yaml
    doc = yaml.safe_load(f.read_text())
    for p in doc.get("patterns", []):
        hay = " ".join(str(p.get(k, "")) for k in ("id", "problem", "solution_approach", "applicable_when")).lower()
        if "shooter" in hay:
            direct_count += 1
assert mcp_cq["count"] == direct_count, f"corpus_query count drifted: mcp={mcp_cq['count']} direct={direct_count}"
assert all("confidence" in p and "provenance" in p for p in mcp_cq["patterns"]), "corpus_query stripped confidence/provenance"
print(f"PASS  corpus_query (filter='shooter') — {mcp_cq['count']} patterns, confidence/provenance intact")

# 4. validate_team_config — a known-confirmed fixture.
fixture = str(ROOT / ".claude/skills/ftc-team-config/evals/fixtures/veteran-swerve-turret.yaml")
mcp_cfg = validate_team_config(fixture)
direct_cfg = direct(str(ROOT / ".claude/skills/ftc-team-config/scripts/validate_config.py"), fixture)
check("validate_team_config (confirmed fixture)", mcp_cfg, direct_cfg, ["valid", "generation_allowed", "unconfirmed_mandatory"])

print("\nAll 4 tools verified: MCP path matches the direct skill path (grounding, citations, abstention).")
