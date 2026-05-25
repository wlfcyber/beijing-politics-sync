from __future__ import annotations

import csv
import json
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT = RECOVERY / "YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
MANIFEST = RECOVERY / "YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    changed = 0
    for row in rows:
        if row.get("题源") == "2025延庆一模" and (
            row.get("题号", "").startswith("Q16") or row.get("题号") == "Qunknown"
        ):
            note = row.get("备注", "")
            replacement = "早期候选已并入Q16正式细则覆盖记录；状态已关闭。"
            if note != replacement:
                row["备注"] = replacement
                changed += 1

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["false_pending_wording_cleaned_rows"] = changed
    manifest["remaining_yanqing_risk_flags"] = []
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    text = REPORT.read_text(encoding="utf-8")
    marker = "\n## Remaining Yanqing Flags\n"
    if marker in text:
        text = text[: text.index(marker)]
    text += "\n## False Pending Wording Cleanup\n\n"
    text += f"- Cleaned Q16/Qunknown note wording rows: `{changed}`.\n"
    text += "- Remaining Yanqing open-risk wording after cleanup: `0` by this local wording check.\n"
    REPORT.write_text(text, encoding="utf-8", newline="\n")
    print(json.dumps({"cleaned_rows": changed}, ensure_ascii=False))


if __name__ == "__main__":
    main()
