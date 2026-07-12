#!/usr/bin/env python3
"""Corpus-currency check (R79). Calibrated abstention for currency, not just completeness:
a correct citation against a STALE manual is still a wrong answer, so flag it instead of answering.

Parameterized by the ACTIVE season. Resolves that season's stored manual metadata
(source_url, incorporates_through), fetches the live page, extracts the highest "Team Update N",
and compares. Any of {live newer, fetch failed, no marker found} => flagged, not silently passed.

  check_freshness.py                 # check the ACTIVE season
  check_freshness.py --season <slug> # check a specific season (BIOBUZZ later = just this arg)
  check_freshness.py --live-tu 34    # skip the network; supply the current TU (tests / manual use)
  check_freshness.py --self-test     # runnable check of the compare logic

Reusable later for hardware-catalog currency: same fetch->extract-marker->compare shape.
"""
import argparse, json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Dual-mode: in the installed plugin this file sits at PLUGIN/ftc-shared-foundation/, so ROOT is the
# plugin root and the rules corpus is under skills/; in the source repo ROOT is the repo root and the
# corpus is under .claude/skills/. Detect by which layout actually exists.
_PLUGIN = (ROOT / "skills" / "ftc-rule-check").exists()
_RULES = (ROOT / "skills/ftc-rule-check/references/rules/rules.json") if _PLUGIN \
    else (ROOT / ".claude/skills/ftc-rule-check/references/rules/rules.json")
_SEASON_DIR = (ROOT / "ftc-shared-foundation/season-extensions") if _PLUGIN else (ROOT / "season-extensions")
# season slug -> where that season's stored rules meta lives. One entry today; BIOBUZZ is one line later.
SEASON_CORPUS = {
    "decode-2025-26": _RULES,
}


def active_season():
    return (_SEASON_DIR / "ACTIVE").read_text().strip()


def tu_num(s):
    nums = [int(n) for n in re.findall(r"Team Update\s+0*(\d+)", s or "", re.I)]
    return max(nums) if nums else None


def fetch_live_tu(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ftc-skill-freshness/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return tu_num(r.read(2_000_000).decode("utf-8", "replace")), None
    except Exception as e:  # network/parse/403 — abstain, don't guess currency
        return None, f"{type(e).__name__}: {e}"


def check(season, live_tu=None):
    corpus = SEASON_CORPUS.get(season)
    if not corpus or not corpus.exists():
        return {"status": "UNVERIFIABLE", "flag": True, "season": season,
                "reason": f"no stored corpus registered for season '{season}' — cannot judge currency"}
    meta = json.loads(corpus.read_text())["meta"]
    stored = tu_num(meta.get("incorporates_through"))
    err = None
    if live_tu is None:
        live_tu, err = fetch_live_tu(meta.get("source_url", ""))

    out = {"season": season, "stored_incorporates_through": meta.get("incorporates_through"),
           "stored_tu": stored, "live_tu": live_tu, "source_url": meta.get("source_url"),
           "retrieved": meta.get("retrieved")}
    if live_tu is None:
        out.update(status="UNVERIFIABLE", flag=True,
                   reason=f"could not read a live Team Update number ({err or 'no marker on page'}); "
                          "treat corpus as possibly stale and say so in the answer")
    elif stored is None:
        out.update(status="UNVERIFIABLE", flag=True, reason="stored corpus has no Team Update marker to compare")
    elif live_tu > stored:
        out.update(status="STALE", flag=True,
                   reason=f"live manual is at Team Update {live_tu} but corpus stops at {stored} — "
                          f"{live_tu - stored} update(s) not ingested; verdicts may be out of date")
    else:
        out.update(status="CURRENT", flag=False,
                   reason=f"corpus TU {stored} >= live TU {live_tu}")
    return out


def _self_test():
    assert check("decode-2025-26", live_tu=32)["status"] == "CURRENT"
    assert check("decode-2025-26", live_tu=40)["status"] == "STALE"
    assert check("no-such-season", live_tu=1)["status"] == "UNVERIFIABLE"
    assert tu_num("incorporates Team Update 09 and Team Update 32") == 32
    print("self-test OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season")
    ap.add_argument("--live-tu", type=int)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return _self_test()
    res = check(a.season or active_season(), a.live_tu)
    print(json.dumps(res, indent=2))
    sys.exit(1 if res["flag"] else 0)


if __name__ == "__main__":
    main()
