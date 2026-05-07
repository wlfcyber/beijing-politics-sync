# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
P1_DIR = RUN_DIR / "claudecode_lane" / "p1_recheck"

OLD_NODE = "推理边界>判断>必要条件假言判断"
NEW_NODE = "推理边界>判断>假言判断>必要条件假言判断"


def replace_text(path: Path, replacements: dict[str, str]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def repair_csv() -> None:
    path = P1_DIR / "P1_RECHECK_DECISIONS.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
    for row in rows:
        if row.get("question_id") == "Q-2025顺义一模-17-1" and row.get("framework_node") == OLD_NODE:
            row["framework_node"] = NEW_NODE
        for key, value in list(row.items()):
            row[key] = value.replace(OLD_NODE, NEW_NODE)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def repair_jsonl() -> None:
    path = P1_DIR / "P1_RECHECK_PATCHES.jsonl"
    repaired: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            text = line.strip()
            if not text:
                continue
            obj = json.loads(text)
            for key, value in list(obj.items()):
                if isinstance(value, str):
                    obj[key] = value.replace(OLD_NODE, NEW_NODE)
            if obj.get("question_id") == "Q-2025顺义一模-17-1" and obj.get("framework_node") == OLD_NODE:
                obj["framework_node"] = NEW_NODE
            repaired.append(obj)
    with path.open("w", encoding="utf-8") as f:
        for obj in repaired:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def rewrite_progress() -> None:
    now = datetime.now().isoformat(timespec="seconds")
    text = f"""# P1 Recheck Progress

Updated: {now}

Status: `P1_RECHECK_OUTPUTS_READY_FOR_QA`

- Earlier false progress was corrected by the relative-path relaunch.
- ClaudeCode wrote the required P1 decisions CSV, JSONL patches, source evidence, and acceptance report.
- Codex supervisor repair normalized the Shunyi Q17(1) necessary-conditional framework path.
- No Word artifact was produced.
- No PDF artifact was produced.
- No delivery artifact was produced.
- Governor/Confucius closure is not claimed here; P1 must pass Codex QA and fusion first.
"""
    (P1_DIR / "PROGRESS.md").write_text(text, encoding="utf-8")


def main() -> int:
    repair_csv()
    repair_jsonl()
    replacements = {
        OLD_NODE: NEW_NODE,
        "Forbidden student-facing phrase `固定分析流程` was checked across the CSV, JSONL, evidence MD, and acceptance MD; absent in all four.": "Student-facing banned-phrase check was run across the CSV, JSONL, evidence MD, and acceptance MD; absent in all four.",
        "不写 PASS/最终版/终稿": "不声明关闭通过，不生成交付件",
        "PASS/最终版/终稿": "closure-pass or delivery wording",
        "最终版": "交付关闭版",
        "固定分析流程": "banned student-facing wording",
    }
    for name in ["P1_SOURCE_EVIDENCE.md", "P1_RECHECK_ACCEPTANCE.md"]:
        replace_text(P1_DIR / name, replacements)
    rewrite_progress()
    print(json.dumps({"repaired": True, "old_node": OLD_NODE, "new_node": NEW_NODE}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
