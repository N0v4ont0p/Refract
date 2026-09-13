# BIOBUZZ 2026-27 — staged official sources

Retrieved 2026-09-13 (kickoff was 2026-09-12). Inputs to `tag_manual.py --season biobuzz-2026-27`.

| file | source URL | sha256 |
|---|---|---|
| cm.html | https://ftc-resources.firstinspires.org/ftc/game/cm-html (302 → `BIOBUZZ Competition Manual - V1.htm`, Last-Modified Sat, 12 Sep 2026 16:05:02 GMT) | a2a849925a04b41a63296d6a277fa25cad95a32486e3ee4a246d15a3aac0d082 |
| cm.txt | `textutil -convert txt` of cm.html (macOS) | d7bcc51c03ffff87bd940e064e885fef8447ad985270ec5c141d2af8daaad060 |
| cm-pdf-layout.txt | `pdftotext -layout` of https://ftc-resources.firstinspires.org/ftc/game/manual (PDF, 173 pages, Last-Modified Sat, 12 Sep 2026 16:02:42 GMT, sha256 2ee0ea8327da47deb871e33307898c13ee5310d5af260007dc11bb4471181f5a) | e350307e8d3c7f31a778d74f73c2cd7ab76484065b21609078cb7d89ae994bf4 |
| tu-00.pdf | https://ftc-resources.firstinspires.org/ftc/game/tu-00 | 94f9322b279ba196b1ef0dfd120d29689d85046d83259ec711242c1ff9fc157e |
| tu-00.txt | `pdftotext -layout` of tu-00.pdf | b8d76e1200b6cda3ff0e6ddd3570ecbb96ebddcf957e975de5c0409a98ca6cab |

| field-setup-guide-v1.0.pdf | https://ftc-resources.firstinspires.org/ftc/archive/2027/field/eventfieldguide (Event Field Setup Guide V1.0, 2026-09-12; official field document, NOT manual rule text) | 89b82c72061a0d862635be85a7a19e29df6fa4b58fbfad753d3a4196a51da15f |
| field-setup-guide-v1.0.txt | `pdftotext -layout` of the guide | 05829db537cd2dc9ec346a16bbaad5d6db68f1c2cf3d41e5847f1dd5dfe888d7 |

The user-supplied `BIOBUZZ_Competition_Manual_V1.pdf` (repo root, sha256 3740e18c…) has byte-different PDF packaging but **identical extracted text** to the official PDF (whitespace-normalized diff: no differences) — so it is the same V1 manual, not a different revision.

## Known extraction caveats
- The PDF layout text drops some digit glyphs (AprilTag IDs, Table 12-2 servo stall current "4", R710 "62471"). The HTML edition has them intact; rules/tables are extracted from HTML.
- Figures and the 3D CAD model are not stored as text. Geometry defined only there is FIGURE-ONLY.
