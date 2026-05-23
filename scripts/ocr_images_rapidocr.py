from __future__ import annotations

import argparse
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR


def line_rows(result):
    rows = []
    if not result:
        return rows
    for box, text, score in result:
        if not text:
            continue
        y = sum(point[1] for point in box) / 4
        x = sum(point[0] for point in box) / 4
        rows.append((y, x, text.strip(), float(score)))
    rows.sort(key=lambda row: (row[0], row[1]))
    return rows


def slide_number(path: Path) -> tuple[int, str]:
    digits = "".join(ch for ch in path.stem if ch.isdigit())
    return (int(digits) if digits else 0, path.name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    image_dir = Path(args.image_dir)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    ocr = RapidOCR()
    parts = []
    for image in sorted(image_dir.glob("*.PNG"), key=slide_number):
        result, elapsed = ocr(str(image))
        parts.append(f"--- {image.name} OCR items={0 if result is None else len(result)} elapsed={elapsed} ---")
        parts.extend(text for _, _, text, _ in line_rows(result))
    out.write_text("\n".join(parts), encoding="utf-8")
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
