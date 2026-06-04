#!/usr/bin/env python3
"""Convert CNKI KDH/CAJ files already downloaded locally into readable PDFs."""

from __future__ import annotations

import argparse
from pathlib import Path


KDH_PASSPHRASE = b"FZHMEI"


def convert_one(src: Path, out_dir: Path) -> tuple[Path | None, int | None, str]:
    try:
        import fitz  # PyMuPDF
    except Exception as exc:  # pragma: no cover - depends on local environment
        return None, None, f"missing_pymupdf: {exc}"

    data = src.read_bytes()
    if not data.startswith(b"KDH"):
        return None, None, "not_kdh"

    origin = data[254:]
    output = bytes(byte ^ KDH_PASSPHRASE[i % len(KDH_PASSPHRASE)] for i, byte in enumerate(origin))
    eof = output.rfind(b"%%EOF")
    if eof < 0:
        return None, None, "pdf_eof_not_found"

    raw_pdf = output[: eof + 5]
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_path = out_dir / f"{src.stem}.raw.pdf"
    out_path = out_dir / f"{src.stem}.pdf"
    raw_path.write_bytes(raw_pdf)
    try:
        doc = fitz.open(raw_path)
        pages = doc.page_count
        doc.save(out_path, garbage=4, deflate=True)
        doc.close()
    except Exception as exc:
        return raw_path, None, f"raw_pdf_written_but_repair_failed: {exc}"
    finally:
        if raw_path.exists():
            raw_path.unlink()
    return out_path, pages, "converted"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="KDH/CAJ files to convert.")
    parser.add_argument("--out-dir", required=True, help="Directory for converted PDFs.")
    parser.add_argument("--manifest", help="Optional Markdown conversion manifest.")
    args = parser.parse_args()

    out_dir = Path(args.out_dir).expanduser().resolve()
    rows: list[tuple[Path, Path | None, int | None, str]] = []
    converted = 0
    for file_arg in args.files:
        src = Path(file_arg).expanduser().resolve()
        out_path, pages, status = convert_one(src, out_dir)
        rows.append((src, out_path, pages, status))
        if status == "converted":
            converted += 1

    if args.manifest:
        lines = [
            "# KDH/CAJ Conversion Manifest",
            "",
            "| Source | Output | Pages | Status |",
            "| --- | --- | --- | --- |",
        ]
        for src, out_path, pages, status in rows:
            out_cell = f"`{out_path}`" if out_path else ""
            page_cell = str(pages) if pages is not None else ""
            lines.append(f"| `{src}` | {out_cell} | {page_cell} | {status} |")
        Path(args.manifest).expanduser().resolve().write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"converted={converted}")
    for src, out_path, pages, status in rows:
        out_label = str(out_path) if out_path else ""
        pages_label = "" if pages is None else str(pages)
        print(f"{src}\t{status}\t{pages_label}\t{out_label}")
    return 0 if converted else 1


if __name__ == "__main__":
    raise SystemExit(main())
