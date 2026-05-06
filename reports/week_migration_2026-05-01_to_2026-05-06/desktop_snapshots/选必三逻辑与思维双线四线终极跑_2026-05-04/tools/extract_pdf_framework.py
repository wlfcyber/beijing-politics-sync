#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz


def safe_name(path: Path) -> str:
    return path.stem.replace(" ", "_").replace("（", "_").replace("）", "_")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--render-dir", type=Path, required=True)
    parser.add_argument("--render-pages", type=int, default=6)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.render_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(args.pdf)
    base = safe_name(args.pdf)
    text_path = args.out_dir / f"{base}.txt"
    page_jsonl_path = args.out_dir / f"{base}.pages.jsonl"
    outline_path = args.out_dir / f"{base}.outline.json"
    meta_path = args.out_dir / f"{base}.meta.json"

    meta = {
        "source_pdf": str(args.pdf),
        "page_count": doc.page_count,
        "metadata": doc.metadata,
        "toc_entries": len(doc.get_toc(simple=False)),
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    outline = doc.get_toc(simple=False)
    outline_path.write_text(json.dumps(outline, ensure_ascii=False, indent=2), encoding="utf-8")

    all_text: list[str] = []
    with page_jsonl_path.open("w", encoding="utf-8") as fp:
        for i, page in enumerate(doc, start=1):
            text = page.get_text("text")
            all_text.append(f"\n\n===== PAGE {i} =====\n{text}")
            fp.write(json.dumps({"page": i, "text": text}, ensure_ascii=False) + "\n")

    text_path.write_text("".join(all_text), encoding="utf-8")

    render_subdir = args.render_dir / base
    render_subdir.mkdir(parents=True, exist_ok=True)
    for idx in range(min(args.render_pages, doc.page_count)):
        page = doc.load_page(idx)
        pix = page.get_pixmap(matrix=fitz.Matrix(1.8, 1.8), alpha=False)
        pix.save(render_subdir / f"page_{idx + 1:03d}.png")

    print(json.dumps({
        "pdf": str(args.pdf),
        "pages": doc.page_count,
        "text": str(text_path),
        "pages_jsonl": str(page_jsonl_path),
        "outline": str(outline_path),
        "meta": str(meta_path),
        "render_dir": str(render_subdir),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
