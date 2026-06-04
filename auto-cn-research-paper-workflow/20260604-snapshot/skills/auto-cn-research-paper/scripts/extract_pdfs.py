#!/usr/bin/env python3
"""Extract text from authorized PDF files into UTF-8 text files."""

from __future__ import annotations

import argparse
from pathlib import Path


def safe_name(stem: str) -> str:
    return "".join(ch if ch not in '\\/:*?"<>|' else "_" for ch in stem)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-dir", required=True, help="Directory containing authorized PDFs.")
    parser.add_argument("--out-dir", required=True, help="Directory for extracted text.")
    parser.add_argument("--manifest", help="Optional Markdown manifest path.")
    parser.add_argument("--pattern", default="*.pdf", help="Glob pattern for task-relevant PDFs, e.g. '*形式主义*.pdf'.")
    parser.add_argument("--skip-existing", action="store_true", help="Do not rewrite existing text files.")
    args = parser.parse_args()

    try:
        import fitz  # type: ignore
    except Exception as exc:  # pragma: no cover - depends on host environment
        raise SystemExit("PyMuPDF is required: install or use a Python runtime with fitz.") from exc

    pdf_dir = Path(args.pdf_dir).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    rows: list[str] = [
        "# Full Text Extraction Manifest",
        "",
        "| PDF | Text | Pages | Characters | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    processed = 0
    for src in sorted(pdf_dir.glob(args.pattern), key=lambda p: p.stat().st_mtime):
        out = out_dir / f"{safe_name(src.stem)}.txt"
        if out.exists() and args.skip_existing:
            rows.append(f"| `{src}` | `{out}` |  |  | existing |")
            continue
        doc = fitz.open(src)
        parts: list[str] = []
        for i, page in enumerate(doc, start=1):
            parts.append(f"\n\n===== PAGE {i} =====\n")
            parts.append(page.get_text("text"))
        text = "".join(parts)
        out.write_text(text, encoding="utf-8")
        rows.append(f"| `{src}` | `{out}` | {doc.page_count} | {len(text)} | extracted |")
        processed += 1

    if args.manifest:
        Path(args.manifest).expanduser().resolve().write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(f"processed={processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
