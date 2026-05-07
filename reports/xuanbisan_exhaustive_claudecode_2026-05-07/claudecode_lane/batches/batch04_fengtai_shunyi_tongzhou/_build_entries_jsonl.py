# -*- coding: utf-8 -*-
"""Build entries/batch04_entries.jsonl from MAIN_THINKING_LEDGER.csv + CHOICE_TRAP_LEDGER.csv.

Each line MUST contain at least:
    question_id, type, framework_node, material_signal, trigger_logic,
    answer_sentence, evidence_level, needs_codex_recheck, source_batch
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAIN_LEDGER = ROOT / "MAIN_THINKING_LEDGER.csv"
CHOICE_LEDGER = ROOT / "CHOICE_TRAP_LEDGER.csv"
OUT_DIR = ROOT / "entries"
OUT_FILE = OUT_DIR / "batch04_entries.jsonl"

SOURCE_BATCH = "batch04_fengtai_shunyi_tongzhou"


def load_question_decisions() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    with (ROOT / "QUESTION_DECISIONS.csv").open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            out[row["question_id"]] = row
    return out


def main() -> None:
    decisions = load_question_decisions()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, object]] = []

    # Main thinking entries
    with MAIN_LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row["question_id"]
            decision = decisions.get(qid, {})
            entry = {
                "question_id": qid,
                "suite_id": decision.get("suite_id", ""),
                "original_qno": decision.get("original_qno", ""),
                "question_type": "subjective",
                "framework_node": row["框架落点"],
                "evidence_level": row["证据等级"],
                "题型标签": row["题型标签"],
                "设问": row["完整设问"],
                "材料触发点": row["材料动作"],
                "为什么能想到": row["触发逻辑"],
                "答案落点": row["答案句"],
                "type": "main_thinking",
                "material_signal": row["材料动作"],
                "trigger_logic": row["触发逻辑"],
                "answer_sentence": row["答案句"],
                "needs_codex_recheck": "yes",
                "source_batch": SOURCE_BATCH,
                "来源": row["来源"],
                "总帽子": row["总帽子"],
                "小方法": row["小方法"],
            }
            entries.append(entry)

    # Choice trap entries
    with CHOICE_LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row["question_id"]
            decision = decisions.get(qid, {})
            framework_node = ""
            # Pick the primary framework node from row note
            # We'll synthesize a primary anchor by extracting the chain category line
            注 = row["陷阱类型"]
            primary_anchor = 注.split("/")[0].strip() if 注 else ""
            entry = {
                "question_id": qid,
                "suite_id": decision.get("suite_id", ""),
                "original_qno": decision.get("original_qno", ""),
                "question_type": "choice",
                "framework_node": primary_anchor,
                "evidence_level": "B-choice-signal",
                "题干信号": row["题干信号"],
                "完整选项": row["完整选项或选项单位"],
                "答案源": row["答案源"],
                "正确项理由": row["正确项理由"],
                "诱人错项": row["诱人错项"],
                "陷阱类型": row["陷阱类型"],
                "type": "choice_trap",
                "material_signal": row["题干信号"],
                "trigger_logic": row["正确项理由"] + " || 诱人错项与陷阱类型：" + row["诱人错项"] + " ｜ 陷阱类型：" + row["陷阱类型"],
                "answer_sentence": row["正确项理由"],
                "needs_codex_recheck": row["needs_codex_recheck"],
                "source_batch": SOURCE_BATCH,
            }
            entries.append(entry)

    with OUT_FILE.open("w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"wrote {OUT_FILE}: {len(entries)} entries")


if __name__ == "__main__":
    main()
