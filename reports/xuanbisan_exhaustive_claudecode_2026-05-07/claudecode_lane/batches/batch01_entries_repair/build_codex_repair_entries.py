# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BATCH = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng")
REPAIR = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_entries_repair")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    REPAIR.mkdir(parents=True, exist_ok=True)
    entries_path = REPAIR / "codex_repair_batch01_entries.jsonl"
    main_rows = read_csv(BATCH / "MAIN_THINKING_LEDGER.csv")
    choice_rows = read_csv(BATCH / "CHOICE_TRAP_LEDGER.csv")

    entries = []
    for r in main_rows:
        entries.append({
            "question_id": r.get("question_id", ""),
            "type": "main_thinking",
            "framework_node": r.get("框架落点", ""),
            "material_signal": r.get("材料动作", ""),
            "trigger_logic": r.get("触发逻辑", ""),
            "answer_sentence": r.get("答案句", ""),
            "evidence_level": r.get("证据等级", ""),
            "needs_codex_recheck": "yes" if "needs" in (r.get("证据等级", "") + r.get("题型标签", "")).lower() else "no",
            "source_batch": "batch01_haidian_xicheng",
            "source_file": "MAIN_THINKING_LEDGER.csv",
            "source": r.get("来源", ""),
            "prompt": r.get("完整设问", ""),
            "method_hat": r.get("总帽子", ""),
            "method_detail": r.get("小方法", ""),
            "question_family": r.get("题型标签", ""),
        })
    for r in choice_rows:
        entries.append({
            "question_id": r.get("question_id", ""),
            "type": "choice_trap",
            "framework_node": r.get("陷阱类型", ""),
            "material_signal": r.get("题干信号", ""),
            "trigger_logic": r.get("正确项理由", ""),
            "answer_sentence": r.get("诱人错项", ""),
            "evidence_level": r.get("答案源", ""),
            "needs_codex_recheck": "yes" if "blocked" in r.get("是否可入学生稿", "").lower() or "recheck" in r.get("是否可入学生稿", "").lower() else "no",
            "source_batch": "batch01_haidian_xicheng",
            "source_file": "CHOICE_TRAP_LEDGER.csv",
            "options": r.get("完整选项或选项单位", ""),
            "student_permission": r.get("是否可入学生稿", ""),
        })

    with entries_path.open("w", encoding="utf-8", newline="\n") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    report = [
        "# Codex Repair Batch01 Entries",
        "",
        "Status: `CODEX_REPAIR_GENERATED_WHILE_CLAUDECODE_STILL_RUNNING`",
        "",
        f"- generated_at: {datetime.now().isoformat(timespec='seconds')}",
        f"- source main rows: {len(main_rows)}",
        f"- source choice rows: {len(choice_rows)}",
        f"- jsonl entries: {len(entries)}",
        f"- output: `{entries_path}`",
        "",
        "This is a mechanical packaging repair from ClaudeCode Batch01 ledgers. It does not replace content review, source verification, or final artifact generation.",
    ]
    (REPAIR / "CODEX_REPAIR_REPORT.md").write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({
        "main_rows": len(main_rows),
        "choice_rows": len(choice_rows),
        "entries": len(entries),
        "entries_path": str(entries_path),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
