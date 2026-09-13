#!/usr/bin/env python3
"""Deterministic rule retrieval + citation verification (REQ-22, REQ-24), per season.

  lookup <ID...>    -> each rule's text + ONE hop of cross-references (both directions), with the
                       neighbor rules' text, tier, and effective_date. Feed this to the verdict step;
                       don't recall rule text from memory.
  verify <ID...>    -> which cited rule IDs actually EXIST in the manual (REQ-24). Run this on every
                       citation before an answer ships — a hallucinated rule number fails here.
  section <NUM...>  -> manual body text of a numbered section (e.g. 10.5.5) — game overview, ARENA,
                       scoring, point values. Tier "manual-body": describes the game; rules govern.
  term <TERM...>    -> the manual's own Glossary definition of an ALL-CAPS term, verbatim.

  --season <slug>   which season's corpus (default: season-extensions/ACTIVE). Every output names
                    the season and manual it came from: a correct citation from the WRONG SEASON's
                    manual is a wrong answer (rule numbers are reused across seasons with new text).

Unknown IDs/sections/terms are reported as missing, never invented. Data: references/rules/<season>/.
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RULES_BASE = HERE.parent / "references" / "rules"


def active_season():
    # source tree: <root>/season-extensions/ACTIVE; plugin: <root>/ftc-shared-foundation/season-extensions/ACTIVE
    for d in HERE.parents:
        for cand in (d / "season-extensions" / "ACTIVE", d / "ftc-shared-foundation" / "season-extensions" / "ACTIVE"):
            if cand.is_file():
                return cand.read_text().strip()
    sys.exit("no season-extensions/ACTIVE found — pass --season explicitly")


def load(season):
    d = RULES_BASE / season
    if not (d / "rules.json").is_file():
        have = sorted(p.name for p in RULES_BASE.iterdir() if (p / "rules.json").is_file())
        print(json.dumps({"season": season, "found": False,
                          "abstain": f"no rules corpus ingested for season '{season}' (have: {have}) — do not answer from memory"}, indent=2))
        sys.exit(2)
    rj = json.loads((d / "rules.json").read_text())
    rules = {r["rule_id"]: r for r in rj["rules"]}
    edges = json.loads((d / "cross_refs.json").read_text())["edges"]
    return d, rj["meta"], rules, edges


def neighbors(rid, edges):
    out = []
    for e in edges:
        if e["from_rule"] == rid:
            n = (e["to_rule"], e.get("to_rule_found", None), "cites")
        elif e["to_rule"] == rid:
            n = (e["from_rule"], True, "cited-by")
        else:
            continue
        if n not in out:  # a rule citing another N times is still one neighbor
            out.append(n)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["lookup", "verify", "section", "term"])
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--season")
    a = ap.parse_args()
    season = a.season or active_season()
    d, meta, rules, edges = load(season)
    src = {"season": season, "manual": meta.get("manual"),
           "incorporates_through": meta.get("incorporates_through"), "retrieved": meta.get("retrieved")}

    if a.cmd == "verify":
        res = {i: (i in rules) for i in a.ids}
        missing = [i for i, ok in res.items() if not ok]
        print(json.dumps({**src, "exists": res, "missing": missing,
                          "all_valid": not missing,
                          "note": "missing IDs do not exist in this season's manual — a citation listing one is a hallucination (or a prior season's number); do not ship it"}, indent=2))
        sys.exit(0 if not missing else 1)

    if a.cmd == "section":
        secs = {s["number"]: s for s in json.loads((d / "sections.json").read_text())["sections"]}
        out = [({**secs[n], "found": True} if n in secs else
                {"number": n, "found": False, "abstain": f"section {n} is not in this manual"}) for n in a.ids]
        print(json.dumps({**src, "sections": out}, indent=2, ensure_ascii=False))
        return

    if a.cmd == "term":
        terms = {t["term"].upper(): t for t in json.loads((d / "glossary.json").read_text())["terms"]}
        out = [({**terms[t.upper()], "found": True} if t.upper() in terms else
                {"term": t, "found": False, "abstain": f"'{t}' is not a defined term in this manual's Glossary"}) for t in a.ids]
        print(json.dumps({**src, "terms": out}, indent=2, ensure_ascii=False))
        return

    # lookup
    out = []
    for rid in a.ids:
        r = rules.get(rid)
        if not r:
            out.append({"rule_id": rid, "found": False,
                        "abstain": f"{rid} is not in the {season} manual — do not answer as if it exists"})
            continue
        hop = []
        for nid, found, rel in neighbors(rid, edges):
            nr = rules.get(nid)
            hop.append({"rule_id": nid, "relation": rel, "exists": nid in rules,
                        "short_title": nr["short_title"].strip() if nr else None,
                        "text": nr["text"] if nr else None})
        out.append({"rule_id": rid, "found": True,
                    "series": r["series"], "short_title": r["short_title"].strip(),
                    "text": r["text"], "section_path": r.get("section_path"), "table_pointers": r.get("table_pointers"),
                    "tier": r.get("tier"), "effective_date": r.get("effective_date"),
                    "cross_references_one_hop": hop})
    print(json.dumps({**src, "asterisk_meaning": meta.get("asterisk_meaning"), "rules": out}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
