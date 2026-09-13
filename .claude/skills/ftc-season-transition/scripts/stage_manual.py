#!/usr/bin/env python3
"""Stage a season's official Competition Manual + Team Updates for tag_manual.py (PLAN §19 step 2).

  stage_manual.py --season biobuzz-2026-27 --game BIOBUZZ [--out-root DIR]

Writes <out-root or repo>/corpus-staging/manual-<season>/:
  cm.html  (official HTML edition)   cm.txt  (macOS `textutil -convert txt -stdout` of cm.html — the text form
  tag_manual.py was validated against)   cm-pdf-layout.txt (`pdftotext -layout` of the PDF, for reading
  tables/figure captions)   tu-NN.pdf/.txt (every Team Update linked from the game index page)
  SOURCES.md (URL, Last-Modified, sha256 per file).
Refuses if the fetched manual's visible text doesn't name --game (FIRST reuses the manual URL every
season — staging last season's manual under a new slug is the failure this guards).
"""
import argparse, hashlib, html, re, shutil, subprocess, sys, urllib.request
from datetime import date
from pathlib import Path

BASE = "https://ftc-resources.firstinspires.org"
UA = {"User-Agent": "refract-stage-manual/1.0"}


def fetch(url):
    req = urllib.request.Request(url.replace(" ", "%20"), headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.geturl(), r.headers.get("Last-Modified", "n/a")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", required=True)
    ap.add_argument("--game", required=True, help="game name as printed in the manual, e.g. BIOBUZZ")
    ap.add_argument("--out-root", default=str(Path(__file__).resolve().parents[4]))
    a = ap.parse_args()
    for tool in ("textutil", "pdftotext"):
        if not shutil.which(tool):
            sys.exit(f"refusing: `{tool}` not found (textutil ships with macOS; pdftotext is poppler)")

    out = Path(a.out_root) / "corpus-staging" / f"manual-{a.season}"
    out.mkdir(parents=True, exist_ok=True)
    rows = []

    body, final, lm = fetch(f"{BASE}/ftc/game/cm-html")
    visible = re.sub(r"<[^>]+>", " ", body.decode("windows-1252", "replace"))
    n = len(re.findall(r"\b" + re.escape(a.game) + r"\b", visible))
    if n < 5:
        sys.exit(f"refusing: live manual names {a.game!r} only {n} times in visible text — not this season's manual")
    (out / "cm.html").write_bytes(body)
    rows.append(("cm.html", f"{BASE}/ftc/game/cm-html (→ {final}, Last-Modified {lm})", out / "cm.html"))
    txt = subprocess.run(["textutil", "-convert", "txt", "-stdout", str(out / "cm.html")], check=True, capture_output=True).stdout
    (out / "cm.txt").write_bytes(txt)  # -stdout form: byte-identical to the text tag_manual.py was validated on
    rows.append(("cm.txt", "`textutil -convert txt -stdout` of cm.html", out / "cm.txt"))

    pdf, _, plm = fetch(f"{BASE}/ftc/game/manual")
    pdf_path = out / "cm.pdf"
    pdf_path.write_bytes(pdf)
    subprocess.run(["pdftotext", "-layout", str(pdf_path), str(out / "cm-pdf-layout.txt")], check=True)
    rows.append(("cm-pdf-layout.txt", f"`pdftotext -layout` of {BASE}/ftc/game/manual (Last-Modified {plm}, pdf sha256 {sha(pdf_path)})",
                 out / "cm-pdf-layout.txt"))
    pdf_path.unlink()  # the text is what's used; the PDF is re-fetchable and large

    index, _, _ = fetch(f"{BASE}/ftc/game")
    tus = sorted(set(re.findall(r'href="(/ftc/game/tu-(\d{2}))"', index.decode("utf-8", "replace"))))
    for href, num in tus:
        data, _, tlm = fetch(BASE + href)
        p = out / f"tu-{num}.pdf"
        p.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(p), str(out / f"tu-{num}.txt")], check=True)
        rows.append((p.name, f"{BASE}{href} (Last-Modified {tlm})", p))
        rows.append((f"tu-{num}.txt", f"`pdftotext -layout` of tu-{num}.pdf", out / f"tu-{num}.txt"))

    lines = [f"# {a.game} {a.season} — staged official sources", "",
             f"Retrieved {date.today().isoformat()} by `stage_manual.py`. Inputs to `tag_manual.py --season {a.season}`.",
             f"Latest Team Update linked from the game index: {('tu-' + tus[-1][1]) if tus else 'none'}.", "",
             "| file | source | sha256 |", "|---|---|---|"]
    lines += [f"| {name} | {src} | {sha(p)} |" for name, src, p in rows]
    lines += ["", "Figures and the 3D CAD model are not stored as text — geometry defined only there is FIGURE-ONLY.", ""]
    (out / "SOURCES.md").write_text("\n".join(lines))
    print(f"staged {len(rows)} files into {out}; latest TU: {tus[-1][1] if tus else 'none'}")


if __name__ == "__main__":
    main()
