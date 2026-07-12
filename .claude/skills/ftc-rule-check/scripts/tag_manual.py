#!/usr/bin/env python3
"""
Deterministic FTC Competition Manual tagger (Phase 5, §8).

DETERMINISTIC-FIRST (operating rule 1): every fact this emits is computed from
the source text, not generated. No model in the loop. The §12.6 sample proved a
regex edge-scan matches the LLM extraction exactly, so the primary extractor is
this script; an LLM verification pass is a separate optional safety net.

Inputs  : corpus-staging/manual/cm.html  (structure: tables, sections)
          corpus-staging/manual/cm.txt   (flattened text, tag-stripped)
Outputs : ftc-rule-check/references/rules/{rules.json, cross_refs.json,
                                           rule_index.json, dangling_citations.json,
                                           section_map.json, STATS.md}
          ftc-hardware-lookup/references/manual-tables/{table-<id>.json, INDEX.json}

Design decisions grounded in the manual's actual structure:
  * Rule series = A,E,G,I,R,T (verified by definition inventory). Tokens like
    EN166 / RS485 / F310 / C270 are parts/standards, not rules, and are excluded
    by construction (their prefix isn't a rule series).
  * '*' on a rule headline = "relatively unchanged season-to-season" (manual
    §1.6 convention, CONFIRMED not inferred) -> encoded as marked_carryover.
  * Tables are §9-owned: extracted to structured files, referenced from the
    citing rule chunk by [[TABLE:<id>]] pointer, never duplicated/paraphrased
    into rule prose (§8 step 6, the §8<->§9 cross-reference mechanism).
"""
import re, json, os, sys
from html.parser import HTMLParser

ROOT = "/Users/georgehu/Desktop/FTC Training AI"
IN_HTML = f"{ROOT}/corpus-staging/manual/cm.html"
IN_TXT  = f"{ROOT}/corpus-staging/manual/cm.txt"
RULES_DIR  = f"{ROOT}/.claude/skills/ftc-rule-check/references/rules"
TABLES_DIR = f"{ROOT}/.claude/skills/ftc-hardware-lookup/references/manual-tables"

SERIES = set("AEGIRT")
ID_RE = re.compile(r'\b([AEGIRT]\d{3})\b')
DASHES = dict.fromkeys(map(ord, "‐‑‒–—―−"), '-')

MANUAL_META = {
    "manual": "DECODE Competition Manual (2025-2026)",
    "incorporates_through": "Team Update 32",
    "source_url": "https://ftc-resources.firstinspires.org/ftc/game/cm-html",
    "retrieved": "2026-07-03",
    "tier": "rule",            # base-manual body text; Q&A would be clarification-tier
    "effective_date": "base-manual",
}

def norm(s):
    s = s.translate(DASHES)
    s = s.replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', s).strip()

# ---------------------------------------------------------------- tables (HTML)
class TableGrabber(HTMLParser):
    """Collect top-level <table> elements as row/cell text matrices."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0; self.tables = []
        self.cur = None; self.row = None; self.cell = None
    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.depth += 1
            if self.depth == 1:
                self.cur = []
        elif self.depth >= 1 and tag == 'tr':
            self.row = []
        elif self.depth >= 1 and tag in ('td', 'th'):
            self.cell = []
    def handle_endtag(self, tag):
        if tag == 'table' and self.depth >= 1:
            if self.depth == 1 and self.cur is not None:
                self.tables.append(self.cur); self.cur = None
            self.depth -= 1
        elif self.depth >= 1 and tag == 'tr' and self.row is not None:
            self.cur.append(self.row); self.row = None
        elif self.depth >= 1 and tag in ('td', 'th') and self.cell is not None:
            self.row.append(norm(' '.join(self.cell))); self.cell = None
    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

def extract_tables(raw):
    g = TableGrabber(); g.feed(raw)
    out = []
    for rows in g.tables:
        rows = [r for r in rows if any(c.strip() for c in r)]
        cells = [c for r in rows for c in r]
        # keep DATA tables only: >=2 rows and >=4 non-empty cells, some text
        if len(rows) >= 2 and len([c for c in cells if c.strip()]) >= 4:
            flat = norm(' '.join(cells))
            if len(flat) >= 20:
                out.append({"rows": rows, "flat": flat})
    return out

# --------------------------------------------------- caption alignment (in text)
CAPTION_RE = re.compile(r'Table\s+(\d+-\d+)\s*:?\s*([^\n]{0,80})')

def align_captions(tables, ntext):
    """For each HTML data table, find where its flattened text sits in the
    normalized manual text, then attach the nearest preceding 'Table N-M' caption."""
    for t in tables:
        probe = t["flat"][:60]
        pos = ntext.find(probe)
        t["pos"] = pos
        cap_id, cap_txt = None, None
        if pos >= 0:
            back = ntext.rfind("Table ", max(0, pos-160), pos)
            if back >= 0:
                m = CAPTION_RE.match(ntext, back)
                if m:
                    cap_id = m.group(1)
                    cap_txt = m.group(2).strip(' :')
                    # trim caption where the header row begins (it over-grabs on one line)
                    if t["rows"] and t["rows"][0] and t["rows"][0][0]:
                        j = cap_txt.find(t["rows"][0][0])
                        if j > 0:
                            cap_txt = cap_txt[:j].strip(' :')
        t["table_id"] = cap_id
        t["caption"] = cap_txt
    return tables

# ------------------------------------------------------------- section headings
def parse_toc(raw):
    """Authoritative (number -> full title) map from the manual's own TOC anchors
    (<a href="#_Toc...">1.6 This Document & Its Conventions . 10</a>)."""
    num_title = {}; order = []
    for m in re.finditer(r'<a href="#_Toc\d+">(.*?)</a>', raw, re.S):
        s = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(1))).replace('&amp;', '&').strip()
        mm = re.match(r'^(\d+(?:\.\d+){0,3})\s+(.*?)\s*\.*\s*\d*$', s)
        if not mm:
            continue
        num = mm.group(1); title = mm.group(2).strip().rstrip('.').strip()
        if num not in num_title and title:
            num_title[num] = title; order.append((num, title))
    return num_title, order

def build_heads(work, body_start, toc_order):
    """Anchor each TOC section to its body position via a tolerant 'number + first
    few title words' match (tolerant to &, ®, spacing). A FORWARD CURSOR enforces
    document order: since the TOC is ordered, each heading must anchor after the
    previous one — this stops a later section (e.g. '6 Awards') from matching an
    earlier inline mention and mis-parenting a rule."""
    def probe_for(num, title):
        words = [w for w in re.split(r'\W+', title) if w][:3]
        if not words:
            return None
        return re.escape(num) + r'\W+' + r'\W+'.join(re.escape(w) for w in words)

    # Locate the end of the Contents/TOC block: the LAST TOC entry's first
    # occurrence in the text is its TOC line (its body heading is far later), so
    # everything after it is body. Start the ordered cursor there.
    toc_end = body_start
    if toc_order:
        lp = probe_for(*toc_order[-1])
        lm = re.search(lp, work) if lp else None
        if lm:
            toc_end = lm.end()

    heads = []
    cursor = toc_end
    for num, title in toc_order:
        probe = probe_for(num, title)
        if not probe:
            continue
        m = re.search(probe, work[cursor:])
        if m:
            pos = cursor + m.start()
            heads.append((pos, num))
            cursor = pos + 1
    heads.sort()
    return heads

def section_path_for(pos, heads, num_title):
    """Ancestry chain (full titles) of the nearest heading at/above pos."""
    prev = [h for h in heads if h[0] <= pos]
    if not prev:
        return []
    num = prev[-1][1]; parts = num.split('.')
    chain = []
    for i in range(1, len(parts) + 1):
        pref = '.'.join(parts[:i])
        if pref in num_title:
            chain.append(f"{pref} {num_title[pref]}")
    if not chain:
        chain = [f"{num} {num_title.get(num, '')}".strip()]
    return chain

# --------------------------------------------------------- rule definition scan
# Strong inline-citation cues only. Deliberately NOT "rules"/"in"/"by"/etc: a
# section heading like "5.1 General Rules E101 ..." ends in "Rules" and must not
# be mistaken for a citation to E101. The headline requirement below is the
# primary guard; this is a secondary one.
CITE_CUE = re.compile(r'(per|see|violat\w*|specified)\s*$', re.I)

def find_definitions(ntext, body_start):
    """A definition = an in-series ID that starts a rule block: preceded by a
    sentence boundary (not a citation cue), followed by optional '*' + a
    capitalized headline. Returns dict id -> def offset (earliest)."""
    defs = {}
    for m in ID_RE.finditer(ntext):
        if m.start() < body_start:
            continue
        rid = m.group(1)
        pre = ntext[max(0, m.start()-24):m.start()]
        after = ntext[m.end():m.end()+60]
        # headline: optional '*' then a title starting with a capital OR a digit
        # (headlines like "A responsible adult..." or "1 STUDENT, 1 Head REFEREE.").
        head = re.match(r'\s+(\*?)\s*([A-Z0-9].{2,})', after)
        if not head:
            continue
        # reject if this ID is being cited (preceded by a citation cue word)
        if CITE_CUE.search(pre.strip()):
            continue
        # reject if immediately preceded by '(' or ',' or 'and R' list context
        if pre.rstrip().endswith(('(', ',', 'and', 'or')):
            continue
        if rid not in defs:
            defs[rid] = {"pos": m.start(), "carryover": bool(head.group(1))}
    return defs

# ------------------------------------------------------------------------ main
def main():
    raw = open(IN_HTML, 'r', encoding='windows-1252', errors='replace').read()
    txt = open(IN_TXT, 'r', encoding='utf-8').read()
    ntext = norm(txt)

    # body starts after the TOC: use first real rule headline region.
    # Heuristic: the TOC lists section titles with page numbers; the body proper
    # begins at "1 Introduction" heading well past the Contents block. We anchor
    # body_start at the first occurrence of a rule definition-looking headline
    # that has a '*' (carryover rules only exist in the body, never the TOC).
    first_star = re.search(r'\b[AEGIRT]\d{3}\s+\*', ntext)
    body_start = first_star.start()-2000 if first_star else 0

    # ---- tables ----
    tables = extract_tables(raw)
    tables = align_captions(tables, ntext)
    id_seen = {}
    tbl_by_id = {}
    for t in tables:
        tid = t["table_id"]
        if not tid:
            continue
        # de-dupe identical table ids (Word sometimes splits a table)
        tbl_by_id.setdefault(tid, t)

    # ---- substitute table pointers into working text ----
    work = ntext
    replaced = []
    for tid, t in tbl_by_id.items():
        flat = t["flat"]
        if flat and flat in work:
            work = work.replace(flat, f" [[TABLE:{tid}]] ")
            replaced.append(tid)
    work = re.sub(r'\s+', ' ', work)

    # recompute body_start on 'work'
    fs = re.search(r'\b[AEGIRT]\d{3}\s+\*', work)
    body_start = max(0, fs.start()-2000) if fs else 0

    num_title, toc_order = parse_toc(raw)
    heads = build_heads(work, body_start, toc_order)
    defs = find_definitions(work, body_start)

    ordered = sorted(defs.items(), key=lambda kv: kv[1]["pos"])
    index = sorted(defs.keys())

    # ---- chunk rules ----
    rules = []
    for i, (rid, d) in enumerate(ordered):
        start = d["pos"]
        end = ordered[i+1][1]["pos"] if i+1 < len(ordered) else len(work)
        block = work[start:end]
        # strip the leading ID token
        block = re.sub(r'^\s*'+rid+r'\s*', '', block, count=1)
        star = block.lstrip().startswith('*')
        block = block.lstrip()
        if block.startswith('*'):
            block = block[1:].lstrip()
        # short_title = up to first period; text = remainder
        mt = re.match(r'(.{3,140}?\.)\s*(.*)$', block, re.S)
        if mt:
            short_title = norm(mt.group(1)).rstrip('.')
            text = norm(mt.group(2))
        else:
            short_title = norm(block[:100]); text = norm(block)
        rules.append({
            "rule_id": rid,
            "series": rid[0],
            "short_title": short_title,
            "text": text,
            "marked_carryover": d["carryover"],   # * = relatively unchanged season-to-season (manual §1.6)
            "section_path": section_path_for(start, heads, num_title),
            **{k: MANUAL_META[k] for k in ("manual","tier","effective_date")},
            "table_pointers": sorted(set(re.findall(r'\[\[TABLE:(\d+-\d+)\]\]', block))),
        })

    # ---- cross-references (regex on each rule body) ----
    idset = set(index)
    edges = []; dangling = []
    for r in rules:
        rid = r["rule_id"]
        body = r["short_title"] + " " + r["text"]
        for m in ID_RE.finditer(body):
            tgt = m.group(1)
            if tgt == rid:
                continue
            ctx = norm(body[max(0, m.start()-30):m.end()+2])
            found = tgt in idset
            edge = {"from_rule": rid, "to_rule": tgt, "cite_text": ctx, "to_rule_found": found}
            edges.append(edge)
            if not found:
                dangling.append(edge)

    # ---- write outputs ----
    os.makedirs(RULES_DIR, exist_ok=True)
    os.makedirs(TABLES_DIR, exist_ok=True)
    json.dump({"meta": MANUAL_META, "rules": rules}, open(f"{RULES_DIR}/rules.json","w"), indent=2)
    json.dump({"meta": MANUAL_META, "edges": edges}, open(f"{RULES_DIR}/cross_refs.json","w"), indent=2)
    json.dump({"meta": MANUAL_META, "rule_ids": index,
               "by_series": {s: sorted(x for x in index if x[0]==s) for s in sorted(SERIES)}},
              open(f"{RULES_DIR}/rule_index.json","w"), indent=2)
    json.dump({"meta": MANUAL_META, "note":"target rule number not found anywhere in the manual — FLAG FOR HUMAN REVIEW (possible stale cross-ref from a Team Update, or a manual typo)",
               "dangling": dangling}, open(f"{RULES_DIR}/dangling_citations.json","w"), indent=2)
    json.dump({"meta": MANUAL_META, "headings":[{"pos":p,"number":n,"title":num_title.get(n,'')} for p,n in heads]},
              open(f"{RULES_DIR}/section_map.json","w"), indent=2)

    tindex = []
    for tid, t in sorted(tbl_by_id.items()):
        rec = {"table_id": tid, "caption": t["caption"], "rows": t["rows"],
               "source_manual": MANUAL_META["manual"], "note": "structured copy of a manual table; rules reference this by [[TABLE:%s]] pointer (§8<->§9)" % tid}
        json.dump(rec, open(f"{TABLES_DIR}/table-{tid}.json","w"), indent=2)
        tindex.append({"table_id": tid, "caption": t["caption"], "rows": len(t["rows"])})
    json.dump({"meta": MANUAL_META, "tables": tindex}, open(f"{TABLES_DIR}/INDEX.json","w"), indent=2)

    # ---- stats to stdout + STATS.md ----
    from collections import Counter
    ser = Counter(r["series"] for r in rules)
    carry = sum(1 for r in rules if r["marked_carryover"])
    lines = []
    P = lambda s: (lines.append(s), print(s))
    P(f"RULES chunked        : {len(rules)}")
    P(f"  by series          : {dict(sorted(ser.items()))}")
    P(f"  marked_carryover(*) : {carry}/{len(rules)}")
    P(f"CROSS-REF edges      : {len(edges)}")
    P(f"  dangling (FLAGGED)  : {len(dangling)}")
    P(f"TABLES extracted     : {len(tbl_by_id)}  (pointers substituted: {len(replaced)})")
    P(f"SECTION headings     : {len(heads)}")
    # regression check vs known sample
    r_ids = [r['rule_id'] for r in rules if r['rule_id'].startswith('R6')]
    P(f"REGRESSION §12.6 R6xx present: {sorted(r_ids)[:25]}")
    s126 = [e for e in edges if e['from_rule'].startswith('R6') and e['from_rule']<='R619' and e['from_rule']>='R601']
    P(f"REGRESSION §12.6 edges count : {len(s126)} (sample had 14)")
    if dangling:
        sample = sorted({d['from_rule'] + "->" + d['to_rule'] for d in dangling})[:20]
        P("DANGLING sample: " + ", ".join(sample))
    open(f"{RULES_DIR}/STATS.md","w").write("# Manual tagging stats\n\n```\n"+"\n".join(lines)+"\n```\n")

if __name__ == "__main__":
    main()
