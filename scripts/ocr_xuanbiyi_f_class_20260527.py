from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, "/tmp/codex_ocr_deps")

import fitz
from ocrmac import ocrmac


ROOT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync")
OUT = ROOT / "reports/选必一_哲学宝典式重建_2026-05-16/19_error_report_patch_20260527/f_class_ocr"

PDFS = [
    ("2026海淀一模_试卷", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模/试卷/试卷.pdf")),
    ("2026海淀一模_细则", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模/细则/细则.pdf")),
    ("2026房山二模_试卷", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026房山二模/试卷/2026北京房山高三二模政治（教师版）.pdf")),
    ("2026朝阳期末_试卷", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/试卷/试卷.pdf")),
    ("2026朝阳期末_细则", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf")),
    ("2026顺义二模_试卷", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026顺义二模/试卷/26顺义二模(1).pdf")),
    ("2026丰台期末_试卷", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/试卷/试卷.pdf")),
    ("2026丰台期末_细则", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/细则/细则.pdf")),
    ("2024海淀期中_试卷", Path("/Users/wanglifei/Desktop/2024模拟题/2024海淀期中/试卷/试卷.pdf")),
    ("2024海淀期中_细则", Path("/Users/wanglifei/Desktop/2024模拟题/2024海淀期中/细则/细则.pdf")),
    ("2024东城二模_试卷", Path("/Users/wanglifei/Desktop/2024模拟题/东城二模/试卷/试卷.pdf")),
    ("2024东城二模_细则", Path("/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/补充材料/细则.pdf")),
    ("2026西城期末_细则", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/细则.pdf")),
    ("2026西城期末_参考答案", Path("/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/补充材料/高三思想政治参考答案.pdf")),
]


def text_layer(page) -> str:
    return (page.get_text("text") or "").strip()


def ocr_image(image_path: Path) -> str:
    ocr = ocrmac.OCR(
        str(image_path),
        framework="vision",
        recognition_level="accurate",
        language_preference=["zh-Hans", "en-US"],
        confidence_threshold=0.0,
        detail=True,
    )
    rows = []
    for text, confidence, bbox in ocr.recognize(px=True):
        x0, y0, x1, y1 = bbox
        rows.append((round(y0 / 18) * 18, x0, text, confidence, bbox))
    rows.sort(key=lambda r: (r[0], r[1]))
    lines: list[str] = []
    current_y = None
    current: list[str] = []
    for y, _x, text, _confidence, _bbox in rows:
        if current_y is None or abs(y - current_y) <= 18:
            current.append(text)
            current_y = y if current_y is None else current_y
        else:
            lines.append(" ".join(current))
            current = [text]
            current_y = y
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines).strip()


def process_pdf(label: str, path: Path, rows: list[dict[str, object]]) -> None:
    label_dir = OUT / label
    label_dir.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        rows.append({"label": label, "path": str(path), "status": "missing", "pages": 0, "text_pages": 0, "ocr_pages": 0})
        return
    doc = fitz.open(str(path))
    combined_parts: list[str] = [f"# {label}", "", f"- source: {path}", f"- pages: {len(doc)}", ""]
    text_pages = 0
    ocr_pages = 0
    for i in range(len(doc)):
        page = doc.load_page(i)
        layer = text_layer(page)
        if len(layer) > 20:
            text_pages += 1
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
        image_path = label_dir / f"page_{i + 1:03d}.png"
        pix.save(str(image_path))
        ocr_text = ocr_image(image_path)
        if ocr_text:
            ocr_pages += 1
        page_text = [
            f"# {label} page {i + 1}",
            "",
            "## text_layer",
            "",
            layer,
            "",
            "## vision_ocr",
            "",
            ocr_text,
            "",
        ]
        (label_dir / f"page_{i + 1:03d}.md").write_text("\n".join(page_text), encoding="utf-8")
        combined_parts.extend(page_text)
    (OUT / f"{label}.md").write_text("\n".join(combined_parts), encoding="utf-8")
    rows.append(
        {
            "label": label,
            "path": str(path),
            "status": "ok",
            "pages": len(doc),
            "text_pages": text_pages,
            "ocr_pages": ocr_pages,
        }
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    for label, path in PDFS:
        print(f"OCR {label}", flush=True)
        process_pdf(label, path, rows)
    with (OUT / "F_CLASS_OCR_MANIFEST_20260527.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["label", "path", "status", "pages", "text_pages", "ocr_pages"])
        writer.writeheader()
        writer.writerows(rows)
    print(OUT)


if __name__ == "__main__":
    main()
