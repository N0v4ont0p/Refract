> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-barcode/barcodes · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Decoding and Tracking Barcodes | Limelight Documentation

 Skip to main content

# Decoding and Tracking Barcodes

LLOS supports QR Code, DataMatrix, UPC, EAN, Code128, and PDF417 code tracking and decoding

With the LL3 Series of Smart Cameras, you can expect:

- 50-60FPS Multi QR Code Detection and Decoding at 1280x800

- 50-60FPS Multi DataMatrix Detection and Decoding at 1280x800

- 30FPS Multi UPC, EAN, Code128, and PDF417 decoding at 1280x800

Keep the following in mind:

- Barcode data strings are posted to the "rawbarcodes" nt array.

- Barcode data is also posted to the "Barcode" array in the JSON Results output.

- The Barcodes pipeline will populate all 2D metrics such as tx, ty, ta, tcornxy, etc across all APIs