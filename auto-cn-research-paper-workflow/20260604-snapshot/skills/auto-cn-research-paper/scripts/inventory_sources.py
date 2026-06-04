#!/usr/bin/env python3
"""Inventory downloaded PDFs/CAJ files and extracted text readiness."""

from __future__ import annotations

import argparse
from pathlib import Path


def safe_stem(stem: str) -> str:
    return "".join(ch if ch not in '\\/:*?"<>|' else "_" for ch in stem)


def normalized(stem: str) -> str:
    return "".join(ch.lower() for ch in stem if ch.isalnum())


def first_bytes(path: Path, count: int = 16) -> str:
    try:
        return " ".join(f"{b:02X}" for b in path.read_bytes()[:count])
    except Exception:
        return ""


def find_text(stem: str, text_dir: Path) -> Path | None:
    safe = safe_stem(stem)
    candidates = list(text_dir.glob(f"{safe}.txt"))
    if candidates:
        return candidates[0]
    norm = normalized(stem)
    if norm:
        for path in text_dir.glob("*.txt"):
            other = normalized(path.stem)
            if norm in other or other in norm:
                return path
    short = safe[:10]
    if short:
        fuzzy = [p for p in text_dir.glob("*.txt") if short in p.stem]
        if fuzzy:
            return fuzzy[0]
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--download-dir",
        action="append",
        required=True,
        help="Directory containing downloaded or converted PDF/CAJ files. Can be passed more than once.",
    )
    parser.add_argument("--text-dir", required=True)
    parser.add_argument("--pattern", action="append", default=None, help="Glob pattern. Can be passed more than once.")
    parser.add_argument("--out", help="Markdown output path.")
    args = parser.parse_args()

    download_dirs = [Path(path).expanduser().resolve() for path in args.download_dir]
    text_dir = Path(args.text_dir).expanduser().resolve()
    patterns = args.pattern or ["*"]
    files: list[Path] = []
    for download_dir in download_dirs:
        for pattern in patterns:
            files.extend(p for p in download_dir.glob(pattern) if p.suffix.lower() in {".pdf", ".caj"})
    files = sorted(set(files), key=lambda p: (str(p.parent), p.name))

    lines = [
        "# Source Inventory",
        "",
        "| File | Type | Size | Header | Text | Evidence status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    usable = 0
    candidates = 0
    for path in files:
        ext = path.suffix.lower().lstrip(".")
        text = find_text(path.stem, text_dir)
        if ext == "pdf" and text:
            status = "PDF_or_user_exported; full_text_read"
            usable += 1
        elif ext == "pdf":
            status = "needs_text_extraction"
            candidates += 1
        elif ext == "caj" and text:
            status = "caj_has_readable_fulltext_elsewhere"
        else:
            status = "candidate_only_caj_needs_reader_or_pdf"
            candidates += 1
        text_cell = f"`{text}`" if text else ""
        lines.append(
            f"| `{path}` | {ext} | {path.stat().st_size} | `{first_bytes(path)}` | {text_cell} | {status} |"
        )

    lines.append("")
    lines.append(f"- usable_fulltext: {usable}")
    lines.append(f"- candidate_or_incomplete: {candidates}")

    output = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).expanduser().resolve().write_text(output, encoding="utf-8")
    print(f"usable_fulltext={usable}")
    print(f"candidate_or_incomplete={candidates}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
