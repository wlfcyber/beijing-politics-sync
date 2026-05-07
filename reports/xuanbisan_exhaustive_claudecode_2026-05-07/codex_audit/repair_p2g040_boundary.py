# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
LANE = RUN / "claudecode_lane" / "p2_recheck"
QID = "Q-2025丰台期末-16"
NODE = "辩证思维>质量互变（适度原则）"


def repair_csv() -> None:
    path = LANE / "P2G040_RECHECK_DECISIONS.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
    for row in rows:
        if row.get("question_id") == QID and row.get("framework_node") == NODE:
            row["decision"] = "downgrade_to_index"
            row["decision_reason"] = (
                "丰台期末Q16为哲学边界题，不能作为选必三正文；质量互变/适度原则可保留为同类索引，"
                "用于提示跨模块边界。"
            )
            row["patch_needed"] = "yes"
            row["can_enter_fusion"] = "yes"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def repair_jsonl() -> None:
    path = LANE / "P2G040_RECHECK_PATCHES.jsonl"
    out = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if obj.get("question_id") == QID and obj.get("framework_node") == NODE:
                obj["decision"] = "downgrade_to_index"
                obj["patched_trigger_logic"] = (
                    "这是哲学边界题，不进入选必三正文；其中质量互变/适度原则可作为同类索引帮助学生识别跨模块边界。"
                )
                obj["patched_answer_sentence"] = (
                    "同类索引提示：胸中有数涉及质量互变和适度原则，但本题主答域属于哲学，不作为选必三逻辑与思维正文样题。"
                )
                obj["notes"] = "Codex supervisor repaired P2G040 boundary decision from block to index."
            out.append(obj)
    with path.open("w", encoding="utf-8") as f:
        for obj in out:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def repair_text() -> None:
    for name in ["P2G040_SOURCE_EVIDENCE.md", "P2G040_RECHECK_ACCEPTANCE.md", "P2G040_PROGRESS.md"]:
        path = LANE / name
        text = path.read_text(encoding="utf-8", errors="replace")
        text = text.replace(
            "block_from_student_body` / `yes",
            "downgrade_to_index` / `yes",
        )
        text = text.replace(
            "block_from_student_body | yes",
            "downgrade_to_index | yes",
        )
        text = text.replace(
            "block_from_student_body, can_enter_fusion=yes",
            "downgrade_to_index, can_enter_fusion=yes",
        )
        text = text.replace(
            "decision=block_from_student_body",
            "decision=downgrade_to_index",
        )
        path.write_text(text, encoding="utf-8")


def main() -> int:
    repair_csv()
    repair_jsonl()
    repair_text()
    print(json.dumps({"repaired": True, "question_id": QID, "framework_node": NODE}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
