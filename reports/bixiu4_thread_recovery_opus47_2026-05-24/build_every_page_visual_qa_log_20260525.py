from __future__ import annotations

import csv
import json
import math
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageStat


ROOT = Path(__file__).resolve().parent
RENDER_DIR = ROOT / "word_render_qa_20260525_heading_style_fix"
MANIFEST = RENDER_DIR / "render_manifest.json"
OUT_DIR = ROOT / "every_page_visual_qa_20260525"
OUT_CSV = ROOT / "EVERY_PAGE_VISUAL_QA_LOG_20260525.csv"
OUT_MD = ROOT / "EVERY_PAGE_VISUAL_QA_LOG_20260525.md"
OUT_JSON = ROOT / "EVERY_PAGE_VISUAL_QA_LOG_20260525.json"


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def page_no(path: Path) -> int:
    return int(path.stem.split("_")[1])


def nonwhite_ratio(img: Image.Image, threshold: int = 245) -> float:
    gray = img.convert("L")
    hist = gray.histogram()
    nonwhite = sum(count for value, count in enumerate(hist) if value < threshold)
    return nonwhite / (img.width * img.height)


def dark_ratio(img: Image.Image, threshold: int = 80) -> float:
    gray = img.convert("L")
    hist = gray.histogram()
    dark = sum(count for value, count in enumerate(hist) if value < threshold)
    return dark / (img.width * img.height)


def band_nonwhite_ratio(img: Image.Image, box: tuple[int, int, int, int]) -> float:
    crop = img.crop(box)
    return nonwhite_ratio(crop)


def make_contact_sheet(paths: list[Path], out_path: Path, title: str) -> None:
    thumb_w, thumb_h = 220, 300
    cols = 5
    rows = math.ceil(len(paths) / cols)
    label_h = 28
    title_h = 48
    margin = 16
    sheet = Image.new("RGB", (cols * (thumb_w + margin) + margin, rows * (thumb_h + label_h + margin) + margin + title_h), "white")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
        small = ImageFont.truetype("arial.ttf", 14)
    except OSError:
        font = ImageFont.load_default()
        small = ImageFont.load_default()
    draw.text((margin, 12), title, fill=(0, 0, 0), font=font)
    for i, path in enumerate(paths):
        r, c = divmod(i, cols)
        x = margin + c * (thumb_w + margin)
        y = title_h + margin + r * (thumb_h + label_h + margin)
        img = Image.open(path).convert("RGB")
        img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        bg = Image.new("RGB", (thumb_w, thumb_h), (248, 248, 248))
        px = x + (thumb_w - img.width) // 2
        py = y + (thumb_h - img.height) // 2
        sheet.paste(img, (px, py))
        draw.rectangle([x, y, x + thumb_w, y + thumb_h], outline=(170, 170, 170), width=1)
        draw.text((x, y + thumb_h + 6), path.stem, fill=(0, 0, 0), font=small)
    sheet.save(out_path)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    for old_sheet in OUT_DIR.glob("visual_contact_sheet_pages_*.png"):
        old_sheet.unlink()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    page_paths = sorted(RENDER_DIR.glob("page_*.png"), key=page_no)
    rows: list[dict[str, object]] = []
    contact_sheets: list[str] = []
    dims = set()
    for path in page_paths:
        img = Image.open(path).convert("RGB")
        dims.add((img.width, img.height))
        stat = ImageStat.Stat(img.convert("L"))
        page = page_no(path)
        left = band_nonwhite_ratio(img, (0, 0, max(1, int(img.width * 0.035)), img.height))
        right = band_nonwhite_ratio(img, (int(img.width * 0.965), 0, img.width, img.height))
        top = band_nonwhite_ratio(img, (0, 0, img.width, max(1, int(img.height * 0.035))))
        bottom = band_nonwhite_ratio(img, (0, int(img.height * 0.965), img.width, img.height))
        nw = nonwhite_ratio(img)
        dark = dark_ratio(img)
        flags = []
        if page > 2 and nw < 0.006:
            flags.append("BLANK_LIKE_BODY_PAGE")
        if len(dims) > 1:
            flags.append("DIMENSION_DRIFT")
        if max(left, right, top, bottom) > 0.20:
            flags.append("HIGH_EDGE_INK_DENSITY_REVIEW")
        if dark > 0.11:
            flags.append("HIGH_DARK_PIXEL_DENSITY_REVIEW")
        rows.append(
            {
                "page": page,
                "file": str(path.relative_to(ROOT)),
                "width": img.width,
                "height": img.height,
                "bytes": path.stat().st_size,
                "mean_gray": round(stat.mean[0], 2),
                "nonwhite_ratio": round(nw, 6),
                "dark_ratio": round(dark, 6),
                "edge_left_nonwhite": round(left, 6),
                "edge_right_nonwhite": round(right, 6),
                "edge_top_nonwhite": round(top, 6),
                "edge_bottom_nonwhite": round(bottom, 6),
                "visual_status": "REVIEW_REQUIRED" if flags else "PASS_METRIC_SCREEN",
                "visual_flags": "|".join(flags),
            }
        )

    batch_size = 30
    for start in range(0, len(page_paths), batch_size):
        batch = page_paths[start : start + batch_size]
        first = page_no(batch[0])
        last = page_no(batch[-1])
        out_path = OUT_DIR / f"visual_contact_sheet_pages_{first:03d}_{last:03d}.png"
        make_contact_sheet(batch, out_path, f"Bixiu4 every-page visual QA pages {first:03d}-{last:03d}")
        contact_sheets.append(str(out_path.relative_to(ROOT)))

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    flag_counts: dict[str, int] = {}
    for row in rows:
        for flag in str(row["visual_flags"]).split("|"):
            if flag:
                flag_counts[flag] = flag_counts.get(flag, 0) + 1
    review_rows = [row for row in rows if row["visual_status"] != "PASS_METRIC_SCREEN"]
    blank_like_body = [row["page"] for row in rows if "BLANK_LIKE_BODY_PAGE" in str(row["visual_flags"])]
    summary = {
        "updated": now(),
        "render_manifest": str(MANIFEST.relative_to(ROOT)),
        "manifest_pdf_pages": manifest.get("pdf_pages"),
        "manifest_rendered_png_count": manifest.get("rendered_png_count"),
        "page_png_count": len(page_paths),
        "dimension_set": sorted([list(item) for item in dims]),
        "rows_written": len(rows),
        "metric_review_required_rows": len(review_rows),
        "blank_like_body_pages": blank_like_body,
        "flag_counts": flag_counts,
        "contact_sheets": contact_sheets,
        "output_csv": OUT_CSV.name,
        "boundary": [
            "This is an every-page metric screen plus contact-sheet review artifact.",
            "It records every rendered page and surfaces pages needing human visual follow-up.",
            "It does not change DOCX/PDF content and does not close thickness or model-confirmation gates.",
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Every Page Visual QA Log 20260525",
        "",
        f"Updated: {summary['updated']}",
        "",
        "Status: `EVERY_PAGE_VISUAL_QA_LOG_CREATED_METRIC_SCREEN_PASS`"
        if not review_rows
        else "Status: `EVERY_PAGE_VISUAL_QA_LOG_CREATED_WITH_REVIEW_FLAGS`",
        "",
        f"- Render manifest: `{summary['render_manifest']}`.",
        f"- Manifest pages/rendered PNGs: `{summary['manifest_pdf_pages']}/{summary['manifest_rendered_png_count']}`.",
        f"- Page PNGs counted: `{summary['page_png_count']}`.",
        f"- Rows written: `{summary['rows_written']}`.",
        f"- Metric review-required rows: `{summary['metric_review_required_rows']}`.",
        f"- Blank-like body pages: `{blank_like_body if blank_like_body else 'none'}`.",
        f"- Dimension set: `{summary['dimension_set']}`.",
        f"- Output CSV: `{OUT_CSV.name}`.",
        f"- JSON summary: `{OUT_JSON.name}`.",
        "",
        "## Contact Sheets",
        "",
    ]
    for item in contact_sheets:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Flag Counts", ""])
    if flag_counts:
        for key, count in sorted(flag_counts.items()):
            lines.append(f"- `{key}`: `{count}`")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            f"- This file is the `{summary['page_png_count']}`-page per-page visual QA log requested by external review, based on the latest retained render.",
            "- Metric screen results are not a semantic content review and do not close the thickness queue.",
            f"- Contact sheets are provided so a human can inspect every page thumbnail without reopening `{summary['page_png_count']}` individual PNGs.",
            "- No final acceptance claim is made by this artifact.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
