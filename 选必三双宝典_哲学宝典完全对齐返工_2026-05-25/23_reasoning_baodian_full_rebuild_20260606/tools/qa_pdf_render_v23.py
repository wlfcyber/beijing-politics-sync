from __future__ import annotations

import json
import math
from pathlib import Path

import fitz
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "qa" / "word_export_simplified" / "reasoning_baodian_v23_word_export.pdf"
OUT_DIR = ROOT / "qa" / "pdf_render_qa"
SUMMARY = ROOT / "qa" / "PDF_RENDER_QA_20260606.json"

MARKERS = [
    "【题目材料信息】",
    "【设问/选项】",
    "【细则要点】",
    "【为什么能想到】",
    "【考生优秀答案】",
    "【本类做题方法】",
]
FORBIDDEN = [
    "/Users",
    "C:\\",
    "source_extracted",
    "OCR",
    "A-formal",
    "B-choice-signal",
    "题号 |",
    "评标",
    "评分标准",
    "参考答案",
]


def nonwhite_ratio(image: Image.Image) -> float:
    rgb = image.convert("RGB")
    bg = Image.new("RGB", rgb.size, "white")
    diff = ImageChops.difference(rgb, bg).convert("L")
    hist = diff.histogram()
    nonwhite = sum(hist[8:])
    return nonwhite / float(rgb.size[0] * rgb.size[1])


def render_page(page: fitz.Page, output: Path, zoom: float) -> Image.Image:
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    pix.save(output)
    return Image.open(output)


def build_contact_sheet(paths: list[Path], output: Path) -> None:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((180, 240))
        canvas = Image.new("RGB", (190, 250), "white")
        x = (190 - img.width) // 2
        y = (250 - img.height) // 2
        canvas.paste(img, (x, y))
        thumbs.append(canvas)

    cols = 5
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * 190, rows * 250), "white")
    for idx, thumb in enumerate(thumbs):
        x = (idx % cols) * 190
        y = (idx // cols) * 250
        sheet.paste(thumb, (x, y))
    sheet.save(output)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    full_text_parts: list[str] = []
    page_stats = []
    thumb_paths: list[Path] = []
    blank_pages = []

    for idx, page in enumerate(doc, start=1):
        text = page.get_text("text")
        full_text_parts.append(text)
        thumb_path = OUT_DIR / f"page_{idx:03d}_thumb.png"
        thumb_img = render_page(page, thumb_path, zoom=0.45)
        ratio = nonwhite_ratio(thumb_img)
        page_stats.append(
            {
                "page": idx,
                "text_chars": len(text.strip()),
                "nonwhite_ratio": round(ratio, 5),
            }
        )
        if len(text.strip()) == 0 and ratio < 0.005:
            blank_pages.append(idx)
        thumb_paths.append(thumb_path)

    page_count = len(doc)
    sample_pages = sorted(set([1, max(1, page_count // 2), page_count]))
    sample_outputs = []
    for page_no in sample_pages:
        output = OUT_DIR / f"sample_page_{page_no:03d}.png"
        render_page(doc[page_no - 1], output, zoom=1.25)
        sample_outputs.append(str(output.relative_to(ROOT)))

    contact_sheet = OUT_DIR / "all_pages_contact_sheet.png"
    build_contact_sheet(thumb_paths, contact_sheet)

    full_text = "\n".join(full_text_parts)
    marker_counts = {marker: full_text.count(marker) for marker in MARKERS}
    forbidden_counts = {marker: full_text.count(marker) for marker in FORBIDDEN}

    result = {
        "pdf": str(PDF.relative_to(ROOT)),
        "page_count": page_count,
        "marker_counts": marker_counts,
        "forbidden_counts": forbidden_counts,
        "blank_pages": blank_pages,
        "min_text_chars_on_page": min(item["text_chars"] for item in page_stats),
        "min_nonwhite_ratio": min(item["nonwhite_ratio"] for item in page_stats),
        "sample_outputs": sample_outputs,
        "contact_sheet": str(contact_sheet.relative_to(ROOT)),
        "pass": (
            page_count > 0
            and not blank_pages
            and marker_counts["【题目材料信息】"] == 83
            and marker_counts["【设问/选项】"] == 83
            and marker_counts["【细则要点】"] == 83
            and marker_counts["【为什么能想到】"] == 83
            and marker_counts["【考生优秀答案】"] == 83
            and marker_counts["【本类做题方法】"] == 62
            and all(count == 0 for count in forbidden_counts.values())
        ),
        "page_stats": page_stats,
    }

    SUMMARY.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
