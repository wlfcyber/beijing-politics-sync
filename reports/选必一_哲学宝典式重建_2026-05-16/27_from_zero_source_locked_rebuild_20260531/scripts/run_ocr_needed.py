#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import subprocess
from pathlib import Path


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
OCR_NEEDED = RUN / "01_inputs" / "OCR_NEEDED.csv"
OUT_ROOT = RUN / "01_inputs" / "ocr_vision"
LOG = RUN / "01_inputs" / "OCR_RUN_LOG.csv"


def main():
    rows = list(csv.DictReader(OCR_NEEDED.open(encoding="utf-8-sig")))
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    out_rows = []
    for row in rows:
        out_dir = OUT_ROOT / row["source_id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        cmd = ["ocr-vision", "--out", str(out_dir), row["path"]]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        out_rows.append({
            "source_id": row["source_id"],
            "path": row["path"],
            "out_dir": str(out_dir),
            "returncode": proc.returncode,
            "stdout": proc.stdout[-1000:],
            "stderr": proc.stderr[-1000:],
        })
        print(row["source_id"], proc.returncode, row["path"])
    with LOG.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)


if __name__ == "__main__":
    main()
