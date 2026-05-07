# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
LANE = RUN / "claudecode_lane" / "p2_recheck"
MANIFEST = RUN / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"
SOURCE_ID = "003_Desktop_2026模拟题_2026各区期末和期中_2026朝阳期中_试卷_试卷.pdf"
PREFIX = "P2G003"
FIELDS = [
    "priority",
    "question_id",
    "parent_question_id",
    "source_batch",
    "type",
    "framework_node",
    "evidence_level",
    "decision",
    "decision_reason",
    "source_evidence",
    "patch_needed",
    "can_enter_fusion",
]

PATCH = {
    "Q-2026朝阳期中-11": {
        "answer": "A",
        "signal": "题干要求为三段论补充大前提：小前提指向北京街头大部分绿化花草，结论指向适应北京夏季高温环境。",
        "logic": "答案A把中项“耐干旱月季花”和大项“适应北京夏季高温环境”连起来，使从小前提到结论的推理成立。",
        "sentence": "Q11答案A；选择陷阱在于补大前提时必须连接中项和大项，不能把“有些”或反向外延关系误作保真前提。",
    },
    "Q-2026朝阳期中-12": {
        "answer": "B",
        "signal": "题干要求判断哪一说法符合逻辑规则，B项使用“或者……或者……”表达可能并存的选择。",
        "logic": "B项符合相容选言判断的逻辑要求，至少一个选言支为真即可为真，也允许两个选言支同时为真。",
        "sentence": "Q12答案B；应抓住相容选言判断不是排他二选一，不能把所有“或者”都误解为不相容选言。",
    },
    "Q-2026朝阳期中-13": {
        "answer": "D",
        "signal": "“石榴籽”由植物形象联结到民族关系和守望相助，考查联想思维与类比表达。",
        "logic": "答案D对应②④：比喻含类比推理的表达功能，也体现联想思维把不同对象的认识联结起来。",
        "sentence": "Q13答案D；选择陷阱在于不要把感性具体直接说成思维抽象，核心是联想思维的跨对象联结。",
    },
    "Q-2026朝阳期中-14": {
        "answer": "B",
        "signal": "天气谚语来自生活经验，用若干现象预测天气，题干强调经验总结和预测。",
        "logic": "答案B对应①④：天气谚语产生于生活实践并反作用于生活，同时未考察全部对象，结论具有或然性。",
        "sentence": "Q14答案B；选择陷阱在于把经验性不完全归纳误当作必然结论，或把生活经验拔高为完全揭示本质规律。",
    },
    "Q-2026朝阳期中-15": {
        "answer": "D",
        "signal": "小华作出“文笔生动且富有哲理”的联言判断，小浩承认前一支而否定后一支。",
        "logic": "联言判断全真才真，一假即假；否定一个联言支即可否定整个联言判断。",
        "sentence": "Q15答案D；选择陷阱在于小浩不是自相矛盾，而是否定了一个支判断，从而否定整个联言判断。",
    },
}


def load_rows() -> list[dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [row for row in rows if row.get("priority") == "P2" and row.get("source_id") == SOURCE_ID]


def main() -> int:
    rows = load_rows()
    decisions: list[dict[str, str]] = []
    patches: list[dict[str, str]] = []
    for row in rows:
        data = PATCH[row["question_id"]]
        source = (
            "003 paper.txt::Q11-Q15 stems/options; answer table line 241-242 gives "
            "11 A, 12 B, 13 D, 14 B, 15 D."
        )
        decisions.append(
            {
                "priority": "P2",
                "question_id": row["question_id"],
                "parent_question_id": row["parent_question_id"],
                "source_batch": row["source_batch"],
                "type": row["type"],
                "framework_node": row["framework_node"],
                "evidence_level": row["evidence_level"],
                "decision": "confirmed_with_patch",
                "decision_reason": data["logic"],
                "source_evidence": source,
                "patch_needed": "yes",
                "can_enter_fusion": "yes",
            }
        )
        patches.append(
            {
                "question_id": row["question_id"],
                "parent_question_id": row["parent_question_id"],
                "framework_node": row["framework_node"],
                "decision": "confirmed_with_patch",
                "patched_material_signal": data["signal"],
                "patched_trigger_logic": data["logic"],
                "patched_answer_sentence": data["sentence"],
                "source_evidence": source,
                "notes": "Codex local repair after ClaudeCode P2G003 stall; answer table verified in extracted paper text.",
            }
        )

    with (LANE / f"{PREFIX}_RECHECK_DECISIONS.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(decisions)
    with (LANE / f"{PREFIX}_RECHECK_PATCHES.jsonl").open("w", encoding="utf-8") as f:
        for row in patches:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    evidence = [
        f"# {PREFIX} Source Evidence",
        "",
        "Status: Codex local repair, NOT_FINAL.",
        "",
        "- Source: `003_...__paper.txt` contains Q11-Q15 stems/options and the answer table.",
        "- Answer table: `11 A / 12 B / 13 D / 14 B / 15 D`.",
        "",
        "## Rows",
        "",
    ]
    for patch in patches:
        evidence.append(f"- `{patch['question_id']}` / `{patch['framework_node']}`: {patch['source_evidence']} {patch['patched_answer_sentence']}")
    (LANE / f"{PREFIX}_SOURCE_EVIDENCE.md").write_text("\n".join(evidence) + "\n", encoding="utf-8")
    acceptance = [
        f"# {PREFIX} Recheck Acceptance",
        "",
        f"{PREFIX}_RECHECK_ACCEPTANCE: NOT_FINAL",
        "",
        "- decision rows: 5",
        "- patch rows: 5",
        "- all manifest keys resolved: yes",
        "- source_insufficient rows: none",
        "- can_enter_fusion=no rows: none",
        "- Word produced: no",
        "- PDF produced: no",
        "- delivery artifact produced: no",
    ]
    (LANE / f"{PREFIX}_RECHECK_ACCEPTANCE.md").write_text("\n".join(acceptance) + "\n", encoding="utf-8")
    progress = [
        f"# {PREFIX} Progress",
        "",
        f"Updated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "- ClaudeCode source-group run stalled without files and was stopped.",
        "- Codex local repair wrote decisions, patches, evidence, acceptance, and this progress file.",
        "- QA required before merge.",
    ]
    (LANE / f"{PREFIX}_PROGRESS.md").write_text("\n".join(progress) + "\n", encoding="utf-8")
    print(json.dumps({"prefix": PREFIX, "rows": len(decisions), "patches": len(patches)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
