from __future__ import annotations

import csv
import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path.cwd()
OUT_DIR = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16" / "11_strict_final_rebuild_2026-05-23"
LOG_CSV = OUT_DIR / "01_extraction_log.csv"
OCR_LOG = OUT_DIR / "01_ocr_backfill_log.md"
TESSERACT = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
TESSDATA = Path(r"C:\Users\Administrator\AppData\Local\tessdata")


def cjk_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def quality_flag(text: str, ext: str) -> str:
    visible = re.sub(r"\s+", "", text)
    if len(visible) == 0:
        return "empty"
    if cjk_count(text) < 80 and ext in {".pdf", ".pptx", ".ppt", ".doc"}:
        return "needs_ocr_or_render_review"
    if len(visible) < 120:
        return "thin_text_review"
    return "usable_text"


def ocr_pdf(path: Path, dpi: int = 220) -> str:
    import fitz

    doc = fitz.open(str(path))
    parts: list[str] = []
    with tempfile.TemporaryDirectory(prefix="xuanbiyi_ocr_") as tmp:
        tmpdir = Path(tmp)
        for idx, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=dpi)
            image_path = tmpdir / f"page_{idx:03d}.png"
            pix.save(str(image_path))
            cp = subprocess.run(
                [
                    str(TESSERACT),
                    str(image_path),
                    "-",
                    "--tessdata-dir",
                    str(TESSDATA),
                    "-l",
                    "chi_sim+eng",
                    "--psm",
                    "6",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            parts.append(f"--- page {idx} OCR ---\n{cp.stdout}")
            if cp.returncode != 0:
                parts.append(f"[tesseract stderr] {cp.stderr[:500]}")
    doc.close()
    return "\n".join(parts)


def main() -> None:
    if not TESSERACT.exists():
        raise SystemExit(f"missing tesseract: {TESSERACT}")
    with LOG_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = reader.fieldnames or []

    log_lines = ["# 选必一严格最终版 OCR 回填日志", ""]
    changed = 0
    skipped = 0
    for row in rows:
        path = Path(row["absolute_path"])
        ext = path.suffix.lower()
        if row["quality_flag"] == "usable_text" or ext != ".pdf":
            skipped += 1
            continue
        try:
            original = Path(row["text_path"]).read_text(encoding="utf-8", errors="replace")
            ocr = ocr_pdf(path)
            merged = (original.rstrip() + "\n\n" if original.strip() else "") + ocr
            Path(row["text_path"]).write_text(merged, encoding="utf-8")
            row["method"] = row["method"] + "+tesseract_ocr"
            row["status"] = "ok"
            row["char_count"] = str(len(merged))
            row["cjk_count"] = str(cjk_count(merged))
            row["quality_flag"] = quality_flag(merged, ext)
            row["error"] = ""
            changed += 1
            log_lines.append(f"- OK `{path}` -> {row['quality_flag']} ({row['cjk_count']} CJK)")
        except Exception as exc:
            row["error"] = repr(exc)
            log_lines.append(f"- FAIL `{path}`: {exc!r}")

    with LOG_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    log_lines.extend(["", f"- OCR处理：{changed}", f"- 跳过：{skipped}"])
    OCR_LOG.write_text("\n".join(log_lines).rstrip() + "\n", encoding="utf-8")
    print(f"changed={changed}")
    print(OCR_LOG)


if __name__ == "__main__":
    main()
