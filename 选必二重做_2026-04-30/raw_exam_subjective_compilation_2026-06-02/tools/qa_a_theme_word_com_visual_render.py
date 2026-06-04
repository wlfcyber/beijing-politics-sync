#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageOps


RUN_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = RUN_DIR / "05_output"
QA_DIR = OUT_DIR / "word_com_visual_qa_a_theme_20260604"
QA_MD = OUT_DIR / "A_THEME_WORD_COM_VISUAL_QA_20260604.md"
QA_JSON = OUT_DIR / "A_THEME_WORD_COM_VISUAL_QA_20260604.json"


def latest_docx() -> Path:
    candidates = [
        p
        for p in OUT_DIR.glob("*A类十主题学生宝典工作稿_20260604.docx")
        if "~$" not in p.name
    ]
    if not candidates:
        raise FileNotFoundError("A-theme student DOCX not found")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def export_pdf_with_word(docx_path: Path, pdf_path: Path) -> dict:
    script = f"""
$ErrorActionPreference = 'Stop'
$docx = '{docx_path.as_posix()}'
$pdf = '{pdf_path.as_posix()}'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($docx, $false, $true)
$pages = $doc.ComputeStatistics(2)
$paras = $doc.Paragraphs.Count
$doc.ExportAsFixedFormat($pdf, 17)
$doc.Close($false)
$word.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($doc) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
"WORD_EXPORT_OK pages=$pages paragraphs=$paras"
"""
    proc = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
        cwd=str(RUN_DIR),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    line = proc.stdout.strip().splitlines()[-1]
    result = {"raw": line}
    for part in line.split():
        if "=" in part:
            key, value = part.split("=", 1)
            if value.isdigit():
                result[key] = int(value)
            else:
                result[key] = value
    return result


def content_bbox_and_ratio(image: Image.Image) -> tuple[tuple[int, int, int, int] | None, float]:
    gray = ImageOps.grayscale(image)
    # Anything not very close to white counts as rendered content.
    mask = gray.point(lambda p: 0 if p > 248 else 255)
    bbox = mask.getbbox()
    nonwhite = 0
    for value in mask.getdata():
        if value:
            nonwhite += 1
    ratio = nonwhite / (image.width * image.height)
    return bbox, ratio


def render_pdf(pdf_path: Path) -> tuple[list[dict], list[Path]]:
    for old in QA_DIR.glob("page-*.png"):
        old.unlink()
    doc = fitz.open(pdf_path)
    page_rows = []
    page_paths = []
    matrix = fitz.Matrix(1.6, 1.6)
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        out = QA_DIR / f"page-{page_index + 1:03d}.png"
        pix.save(out)
        image = Image.open(out).convert("RGB")
        bbox, ratio = content_bbox_and_ratio(image)
        row = {
            "page": page_index + 1,
            "width": image.width,
            "height": image.height,
            "content_bbox": bbox,
            "nonwhite_ratio": round(ratio, 6),
            "suspicious_blank": bbox is None or ratio < 0.002,
        }
        page_rows.append(row)
        page_paths.append(out)
    doc.close()
    return page_rows, page_paths


def make_contact_sheets(page_paths: list[Path], page_rows: list[dict]) -> list[Path]:
    for old in QA_DIR.glob("contact-sheet-*.png"):
        old.unlink()
    sheets = []
    per_sheet = 24
    cols = 6
    thumb_w, thumb_h = 150, 210
    pad = 18
    label_h = 28
    for sheet_index in range(0, len(page_paths), per_sheet):
        subset = page_paths[sheet_index : sheet_index + per_sheet]
        rows = (len(subset) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad, rows * (thumb_h + label_h + pad) + pad), "white")
        draw = ImageDraw.Draw(sheet)
        for local_index, path in enumerate(subset):
            page_no = sheet_index + local_index + 1
            image = Image.open(path).convert("RGB")
            thumb = ImageOps.contain(image, (thumb_w, thumb_h))
            x = pad + (local_index % cols) * (thumb_w + pad)
            y = pad + (local_index // cols) * (thumb_h + label_h + pad)
            sheet.paste(thumb, (x, y + label_h))
            row = page_rows[page_no - 1]
            label = f"p{page_no:03d} r={row['nonwhite_ratio']:.3f}"
            if row["suspicious_blank"]:
                label += " !"
            draw.text((x, y), label, fill=(180, 0, 0) if row["suspicious_blank"] else (0, 0, 0))
            draw.rectangle((x, y + label_h, x + thumb.width, y + label_h + thumb.height), outline=(120, 120, 120))
        out = QA_DIR / f"contact-sheet-{len(sheets) + 1:02d}.png"
        sheet.save(out)
        sheets.append(out)
    return sheets


def main() -> None:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    source_docx = latest_docx()
    stage_dir = Path(tempfile.gettempdir()) / "a_theme_visual_qa_stage_20260604"
    if stage_dir.exists():
        shutil.rmtree(stage_dir)
    stage_dir.mkdir(parents=True, exist_ok=True)
    ascii_docx = stage_dir / "input.docx"
    stage_pdf = stage_dir / "rendered.pdf"
    pdf_path = QA_DIR / "rendered.pdf"
    shutil.copy2(source_docx, ascii_docx)
    export = export_pdf_with_word(ascii_docx, stage_pdf)
    shutil.copy2(stage_pdf, pdf_path)
    shutil.rmtree(stage_dir)
    page_rows, page_paths = render_pdf(pdf_path)
    sheets = make_contact_sheets(page_paths, page_rows)
    suspicious = [row for row in page_rows if row["suspicious_blank"]]

    payload = {
        "source_docx": str(source_docx),
        "qa_dir": str(QA_DIR),
        "pdf": str(pdf_path),
        "word_export": export,
        "rendered_pages": len(page_rows),
        "suspicious_blank_pages": suspicious,
        "contact_sheets": [str(path) for path in sheets],
        "pages": page_rows,
    }
    QA_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# A类十主题 Word COM 视觉渲染 QA",
        "",
        "## 1. 结论",
        "",
        f"- 源 DOCX：`{source_docx}`",
        f"- Word COM 导出 PDF：`{pdf_path}`",
        f"- Word COM：`{export.get('raw', '')}`",
        f"- PDF 渲染页数：{len(page_rows)}。",
        f"- 可疑空白页：{len(suspicious)}。",
        f"- 接触表数量：{len(sheets)}。",
        "",
        "## 2. 接触表",
        "",
        *[f"- `{path}`" for path in sheets],
        "",
        "## 3. 自动页级检查",
        "",
        "| 页码 | 尺寸 | 非白像素比例 | 可疑空白 |",
        "| ---: | --- | ---: | --- |",
    ]
    for row in page_rows:
        lines.append(
            f"| {row['page']} | {row['width']}x{row['height']} | {row['nonwhite_ratio']:.6f} | {'YES' if row['suspicious_blank'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## 4. 状态边界",
            "",
            "- 本报告使用 Word COM -> PDF -> PyMuPDF PNG 渲染路径，不依赖缺失的 `render_docx.py`。",
            "- 自动检查可发现空白/未渲染页；接触表用于人工快速检查整体版面。最终外部审查门仍需另行完成。",
            "",
        ]
    )
    QA_MD.write_text("\n".join(lines), encoding="utf-8")
    print(QA_MD)
    print(f"WORD_COM_VISUAL_QA pages={len(page_rows)} suspicious_blank={len(suspicious)} sheets={len(sheets)}")


if __name__ == "__main__":
    main()
