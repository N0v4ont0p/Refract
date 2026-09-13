#!/usr/bin/env python3
"""Corpus-currency check (REQ-79). Calibrated abstention for currency, not just completeness:
a correct citation against a STALE manual is still a wrong answer, so flag it instead of answering.

Parameterized by the ACTIVE season. Resolves that season's stored manual metadata
(source_url, game_name, incorporates_through, tu_index_url), fetches the live pages, and checks:
  1. SEASON IDENTITY — the live manual page still names this season's game. FIRST reuses the same
     manual URL every season (cm-html served DECODE, now serves BIOBUZZ). Without this check a
     prior season's corpus compared against the new season's low TU number (e.g. 5 < 32) reads
     CURRENT — a false clear.
  2. TU currency — highest "Team Update N" on the TU index page (or the manual page) vs stored.
Any of {wrong season, live newer, fetch failed, no marker found} => flagged, not silently passed.

  check_freshness.py                 # check the ACTIVE season
  check_freshness.py --season <slug> # check a specific season (BIOBUZZ later = just this arg)
  check_freshness.py --live-tu 34    # skip the network; supply the current TU (tests / manual use)
  check_freshness.py --self-test     # runnable check of the compare logic

Reusable later for hardware-catalog currency: same fetch->extract-marker->compare shape.
"""
import argparse, json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_RULES_BASE = ROOT / ".claude/skills/ftc-rule-check/references/rules"
# each ingested season's corpus lives at <rules base>/<season slug>/rules.json (tag_manual.py --season)


def active_season():
    return (ROOT / "season-extensions/ACTIVE").read_text().strip()


def tu_num(s):
    nums = [int(n) for n in re.findall(r"Team Update\s+0*(\d+)", s or "", re.I)]
    return max(nums) if nums else None


def names_game(page, game, min_mentions=5):
    """Visible-text, whole-word, case-sensitive count of the game name. A substring test is fooled:
    the BIOBUZZ manual HTML carries a reused photo whose alt attribute reads "...DECODE Presented by
    RTX playing field" — 0 visible DECODE mentions vs 36 BIOBUZZ; the DECODE manual has 27 DECODE."""
    text = re.sub(r"<[^>]+>", " ", page)
    return len(re.findall(r"\b" + re.escape(game) + r"\b", text)) >= min_mentions


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ftc-skill-freshness/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read(2_000_000).decode("utf-8", "replace"), None
    except Exception as e:  # network/parse/403 — abstain, don't guess currency
        return None, f"{type(e).__name__}: {e}"


def check(season, live_tu=None, live_game=None):
    corpus = _RULES_BASE / season / "rules.json"
    if not corpus.exists():
        return {"status": "UNVERIFIABLE", "flag": True, "season": season,
                "reason": f"no stored corpus registered for season '{season}' — cannot judge currency"}
    meta = json.loads(corpus.read_text())["meta"]
    stored = tu_num(meta.get("incorporates_through"))
    err = None
    game = meta.get("game_name")
    if live_tu is None or live_game is None:
        page, err = fetch(meta.get("source_url", ""))
        if live_game is None and page is not None:
            live_game = game if (game and names_game(page, game)) else "OTHER"
        if live_tu is None:
            tu_page, err2 = fetch(meta["tu_index_url"]) if meta.get("tu_index_url") else (page, err)
            live_tu, err = tu_num(tu_page), (err2 if meta.get("tu_index_url") else err)

    out = {"season": season, "stored_incorporates_through": meta.get("incorporates_through"),
           "stored_tu": stored, "live_tu": live_tu, "source_url": meta.get("source_url"),
           "game_name": game, "retrieved": meta.get("retrieved")}
    if not game:
        out.update(status="UNVERIFIABLE", flag=True,
                   reason="stored corpus meta has no game_name — cannot confirm the live manual is still this season's")
    elif live_game == "OTHER":
        out.update(status="WRONG_SEASON", flag=True,
                   reason=f"the live manual at source_url no longer names {game} — FIRST has moved to a new season; "
                          f"this corpus is a PRIOR season's. Answer from it only if the question is explicitly about "
                          f"{game}, and say so.")
    elif live_tu is None:
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
    assert check("decode-2025-26", live_tu=32, live_game="DECODE")["status"] == "CURRENT"
    assert check("decode-2025-26", live_tu=40, live_game="DECODE")["status"] == "STALE"
    # the false clear this guards: new season's low TU number vs old corpus's high one
    assert check("decode-2025-26", live_tu=5, live_game="OTHER")["status"] == "WRONG_SEASON"
    assert check("biobuzz-2026-27", live_tu=0, live_game="BIOBUZZ")["status"] == "CURRENT"
    assert check("biobuzz-2026-27", live_tu=3, live_game="BIOBUZZ")["status"] == "STALE"
    assert check("no-such-season", live_tu=1)["status"] == "UNVERIFIABLE"
    assert tu_num("incorporates Team Update 09 and Team Update 32") == 32
    assert not names_game('<img alt="DECODE Presented by RTX playing field">' + "BIOBUZZ " * 40, "DECODE")
    assert names_game("<p>BIOBUZZ</p> " * 6, "BIOBUZZ")
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
