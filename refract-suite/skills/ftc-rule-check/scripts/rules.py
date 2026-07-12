#!/usr/bin/env python3
"""Deterministic rule retrieval + citation verification (R22, R24).

  lookup <ID...>  -> each rule's text + ONE hop of cross-references (both directions), with the
                     neighbor rules' text, tier, and effective_date. Feed this to the verdict step;
                     don't recall rule text from memory.
  verify <ID...>  -> which cited rule IDs actually EXIST in the manual (R24). Run this on every
                     citation before an answer ships — a hallucinated rule number fails here.

Unknown IDs are reported as missing, never invented. Data: references/rules/ next to this script.
"""
import argparse, json, sys
from pathlib import Path

RULES_DIR = Path(__file__).resolve().parent.parent / "references" / "rules"


def load():
    rules = {r["rule_id"]: r for r in json.loads((RULES_DIR / "rules.json").read_text())["rules"]}
    edges = json.loads((RULES_DIR / "cross_refs.json").read_text())["edges"]
    return rules, edges


def neighbors(rid, edges):
    out = []
    for e in edges:
        if e["from_rule"] == rid:
            out.append((e["to_rule"], e.get("to_rule_found", None), "cites"))
        elif e["to_rule"] == rid:
            out.append((e["from_rule"], True, "cited-by"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["lookup", "verify"])
    ap.add_argument("ids", nargs="+")
    a = ap.parse_args()
    rules, edges = load()

    if a.cmd == "verify":
        res = {i: (i in rules) for i in a.ids}
        missing = [i for i, ok in res.items() if not ok]
        print(json.dumps({"exists": res, "missing": missing,
                          "all_valid": not missing,
                          "note": "missing IDs do not exist in the manual — a citation listing one is a hallucination; do not ship it"}, indent=2))
        sys.exit(0 if not missing else 1)

    # lookup
    out = []
    for rid in a.ids:
        r = rules.get(rid)
        if not r:
            out.append({"rule_id": rid, "found": False,
                        "abstain": f"{rid} is not in the manual — do not answer as if it exists"})
            continue
        hop = []
        for nid, found, rel in neighbors(rid, edges):
            nr = rules.get(nid)
            hop.append({"rule_id": nid, "relation": rel, "exists": nid in rules,
                        "short_title": nr["short_title"].strip() if nr else None,
                        "text": nr["text"] if nr else None})
        out.append({"rule_id": rid, "found": True,
                    "series": r["series"], "short_title": r["short_title"].strip(),
                    "text": r["text"], "tier": r.get("tier"), "effective_date": r.get("effective_date"),
                    "cross_references_one_hop": hop})
    print(json.dumps({"rules": out}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
