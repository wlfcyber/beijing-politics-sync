#!/usr/bin/env python3
import csv
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: run_vision_ocr_for_inventory.py SOURCE_FILE_INVENTORY.csv OCR_SWIFT_SCRIPT LOG_DIR", file=sys.stderr)
        return 2
    inv_path = Path(sys.argv[1])
    swift_script = Path(sys.argv[2])
    log_dir = Path(sys.argv[3])
    log_dir.mkdir(parents=True, exist_ok=True)

    with inv_path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys())

    for row in rows:
        if row["status"] != "NEEDS_OCR":
            continue
        # Long lecture decks are not original paper/rubric pages for this audit.
        if row["kind"] == "其他" and int(row["pages"] or 0) > 30:
            row["status"] = "OCR_SKIPPED_LONG_OTHER"
            row["error"] = "Skipped long non-paper/non-rubric PDF"
            continue
        output_path = Path(row["text_path"])
        log_path = log_dir / f"{row['file_id']}.log"
        cmd = ["swift", str(swift_script), row["path"], str(output_path)]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace", timeout=900)
        log_path.write_text(proc.stdout + "\n--- STDERR ---\n" + proc.stderr, encoding="utf-8")
        if proc.returncode != 0:
            row["status"] = "OCR_ERROR"
            row["error"] = proc.stderr[:500]
            continue
        try:
            text = output_path.read_text(encoding="utf-8")
        except Exception as exc:
            row["status"] = "OCR_ERROR"
            row["error"] = f"Cannot read OCR output: {exc}"
            continue
        row["text_len"] = str(len(text))
        if len(text.strip()) >= 80:
            row["status"] = "OCR_OK"
            row["error"] = ""
        else:
            row["status"] = "OCR_EMPTY"
            row["error"] = "OCR output too short"
        print(f"{row['status']} {row['pages']}p {row['kind']} {row['path']}")

    with inv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
