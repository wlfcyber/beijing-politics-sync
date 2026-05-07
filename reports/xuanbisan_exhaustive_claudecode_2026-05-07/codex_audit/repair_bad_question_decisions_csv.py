# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


EXPECTED_HEADER = [
    "question_id",
    "suite_id",
    "original_qno",
    "question_type",
    "codex_current_decision",
    "claudecode_decision",
    "decision_reason",
    "needs_codex_recheck",
]


def repair_line(line: str, line_no: int) -> tuple[list[str] | None, dict | None]:
    parts = line.rstrip("\n\r").split(",")
    if len(parts) < len(EXPECTED_HEADER):
        return None, {"line": line_no, "error": "too_few_fields", "field_count": len(parts), "text": line[:180]}
    prefix = parts[:6]
    suffix = parts[-1].strip()
    reason = ",".join(parts[6:-1]).strip()
    if suffix not in {"yes", "no"}:
        return None, {
            "line": line_no,
            "error": "last_field_not_yes_no",
            "field_count": len(parts),
            "last_field": suffix,
            "text": line[:220],
        }
    return prefix + [reason, suffix], None


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python repair_bad_question_decisions_csv.py <input.csv> <output.csv>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    lines = src.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    if not lines:
        raise SystemExit("empty csv")
    raw_header = lines[0].split(",")
    if raw_header != EXPECTED_HEADER:
        raise SystemExit(f"unexpected header: {raw_header}")

    repaired: list[list[str]] = []
    errors = []
    for line_no, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        row, err = repair_line(line, line_no)
        if err:
            errors.append(err)
        else:
            repaired.append(row)

    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(EXPECTED_HEADER)
        writer.writerows(repaired)

    report = {
        "input": str(src),
        "output": str(dst),
        "input_data_lines": len(lines) - 1,
        "repaired_rows": len(repaired),
        "errors": errors,
    }
    dst.with_suffix(".repair_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
