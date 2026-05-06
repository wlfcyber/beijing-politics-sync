#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30")
RUN = BASE / "preprocess_v2_2026-05-03"
CACHE = RUN / "text_cache"
BACKUP = RUN / "text_cache_pre_vision_ocr_backup"
OCR_BIN = BASE / "scripts" / "vision_ocr"
REPORT = RUN / "VISION_OCR_REPORT_2026-05-04.md"


def parse_cache(path: Path) -> tuple[str, str, str]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    lines = raw.splitlines()
    source = lines[0].replace("source: ", "", 1).strip() if lines and lines[0].startswith("source: ") else ""
    status = lines[1].replace("status: ", "", 1).strip() if len(lines) > 1 and lines[1].startswith("status: ") else ""
    text = raw.split("\n\n", 1)[1] if "\n\n" in raw else raw
    return source, status, text


def needs_ocr(path: Path) -> bool:
    source, status, text = parse_cache(path)
    if not source.lower().endswith(".pdf"):
        return False
    if "scan_ocr_needed" in status or len(text.strip()) < 120:
        return Path(source).exists()
    return False


def render_page(pdf: fitz.Document, page_index: int, out_path: Path, zoom: float = 2.2) -> None:
    page = pdf[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    pix.save(out_path)


def split_pages(output: str) -> list[str]:
    parts = output.split("---PAGE-END---")
    return [part.strip() for part in parts if part.strip()]


def ocr_pdf(source: Path) -> tuple[str, int]:
    doc = fitz.open(source)
    pages_text: list[str] = []
    with tempfile.TemporaryDirectory(prefix="xuanbier_vision_ocr_") as tmp:
        tmpdir = Path(tmp)
        batch: list[Path] = []
        batch_indices: list[int] = []
        for idx in range(len(doc)):
            img = tmpdir / f"page_{idx + 1:03d}.png"
            render_page(doc, idx, img)
            batch.append(img)
            batch_indices.append(idx + 1)
            if len(batch) == 4 or idx == len(doc) - 1:
                proc = subprocess.run(
                    [str(OCR_BIN), *map(str, batch)],
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=False,
                )
                chunks = split_pages(proc.stdout)
                for page_no, chunk in zip(batch_indices, chunks):
                    pages_text.append(f"[ocr page {page_no}]\n{chunk}")
                if len(chunks) < len(batch_indices):
                    for page_no in batch_indices[len(chunks):]:
                        pages_text.append(f"[ocr page {page_no}]\n")
                batch = []
                batch_indices = []
    return "\n\n".join(pages_text), len(doc)


def main() -> int:
    if not OCR_BIN.exists():
        raise SystemExit(f"missing OCR binary: {OCR_BIN}")
    BACKUP.mkdir(parents=True, exist_ok=True)
    candidates = [path for path in sorted(CACHE.glob("*.txt")) if needs_ocr(path)]
    report = [
        "# Vision OCR 补跑报告",
        "",
        f"- 候选 PDF cache：{len(candidates)}",
        "",
    ]
    done = 0
    failed = 0
    for cache_path in candidates:
        source, status, old_text = parse_cache(cache_path)
        source_path = Path(source)
        backup_path = BACKUP / cache_path.name
        if not backup_path.exists():
            shutil.copy2(cache_path, backup_path)
        try:
            text, page_count = ocr_pdf(source_path)
            if len(text.strip()) < 120:
                failed += 1
                report.append(f"- FAIL `{source_path}`：OCR 文本仍过短，pages={page_count}")
                continue
            cache_path.write_text(f"source: {source_path}\nstatus: vision_ocr\n\n{text}", encoding="utf-8")
            done += 1
            report.append(f"- OK `{source_path}`：pages={page_count}, chars={len(text)}")
        except Exception as exc:
            failed += 1
            report.append(f"- FAIL `{source_path}`：{type(exc).__name__}: {exc}")
    report.extend(["", f"- 成功：{done}", f"- 失败：{failed}", f"- 备份目录：`{BACKUP}`", ""])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"candidates={len(candidates)} done={done} failed={failed}")
    print(REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
