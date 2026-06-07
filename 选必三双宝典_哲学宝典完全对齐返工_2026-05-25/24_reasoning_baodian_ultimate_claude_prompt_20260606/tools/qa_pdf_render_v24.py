from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import fitz
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "delivery" / "选必三逻辑与思维_推理宝典_终极版_20260606.pdf"
OUT_DIR = ROOT / "qa" / "pdf_render_qa"
SUMMARY = ROOT / "qa" / "PDF_RENDER_QA_V24_20260606.json"

MARKERS = [
    "【题目材料】",
    "【判断依据】",
    "【满分作答示范】",
    "【采分点对照】",
]

OPTIONAL_MARKERS = [
    "【设问】",
]

FORBIDDEN = [
    "回源",
    "底座",
    "汇编",
    "答案落点",
    "学生化",
    "细则要点",
    "材料触发点",
    "/Users",
    "C:\\",
    "source_extracted",
    "OCR",
    "**• **",
    "本题应围绕",
    "本题考查",
    "本题应",
    "高三政治",
    "成沟",
    "供训练使用",
    "材料栏",
    "不作为完整真题",
    "【这道题考什么】",
    "【怎么想到的】",
    "【本类怎么做】",
    "【本类常见坑】",
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
        canvas.paste(img, ((190 - img.width) // 2, (250 - img.height) // 2))
        thumbs.append(canvas)
    cols = 5
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * 190, rows * 250), "white")
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % cols) * 190, (idx // cols) * 250))
    sheet.save(output)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    full_text_parts = []
    page_stats = []
    thumb_paths = []
    blank_pages = []
    for idx, page in enumerate(doc, start=1):
        text = page.get_text("text")
        full_text_parts.append(text)
        thumb_path = OUT_DIR / f"page_{idx:03d}_thumb.png"
        thumb_img = render_page(page, thumb_path, zoom=0.45)
        ratio = nonwhite_ratio(thumb_img)
        stat = {"page": idx, "text_chars": len(text.strip()), "nonwhite_ratio": round(ratio, 5)}
        page_stats.append(stat)
        if stat["text_chars"] == 0 and ratio < 0.005:
            blank_pages.append(idx)
        thumb_paths.append(thumb_path)

    page_count = len(doc)
    sample_pages = sorted(set([1, max(1, page_count // 2), page_count]))
    samples = []
    for page_no in sample_pages:
        out = OUT_DIR / f"sample_page_{page_no:03d}.png"
        render_page(doc[page_no - 1], out, zoom=1.25)
        samples.append(str(out.relative_to(ROOT)))
    contact_sheet = OUT_DIR / "all_pages_contact_sheet.png"
    build_contact_sheet(thumb_paths, contact_sheet)

    full_text = "\n".join(full_text_parts)
    marker_counts = {m: full_text.count(m) for m in MARKERS}
    optional_marker_counts = {m: full_text.count(m) for m in OPTIONAL_MARKERS}
    forbidden_counts = {m: full_text.count(m) for m in FORBIDDEN}
    result = {
        "pdf": str(PDF.relative_to(ROOT)),
        "page_count": page_count,
        "marker_counts": marker_counts,
        "optional_marker_counts": optional_marker_counts,
        "forbidden_counts": forbidden_counts,
        "blank_pages": blank_pages,
        "min_text_chars_on_page": min(item["text_chars"] for item in page_stats),
        "min_nonwhite_ratio": min(item["nonwhite_ratio"] for item in page_stats),
        "sample_outputs": samples,
        "contact_sheet": str(contact_sheet.relative_to(ROOT)),
        "pass": (
            page_count > 0
            and not blank_pages
            and all(marker_counts[m] == 83 for m in MARKERS)
            and all(count <= 83 for count in optional_marker_counts.values())
            and all(count == 0 for count in forbidden_counts.values())
        ),
        "page_stats": page_stats,
    }
    SUMMARY.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
