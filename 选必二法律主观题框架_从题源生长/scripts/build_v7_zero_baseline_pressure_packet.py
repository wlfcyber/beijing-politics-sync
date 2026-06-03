#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
OUT_DIR = ROOT / "10_framework_validation" / "v7_method_first_zero_baseline_pressure_20260521"
PACKET = OUT_DIR / "clean_student_packet_v7_method_first_20260521.md"
KEY = OUT_DIR / "internal_grading_key_v7_method_first_20260521.csv"

SAMPLE_QIDS = [
    "CC0143_2025_朝阳_一模_19",
    "CC0054_2024_石景山_一模_17",
    "CC0373_2026_顺义_一模_18",
    "CC0244_2026_东城_期末_18",
    "RECOVER_2025_海淀_二模_18",
    "CC0103_2025_丰台_一模_19",
    "RECOVER_2026_房山_一模_17_1",
    "CC0325_2026_石景山_一模_18",
    "CC0277_2026_房山_二模_18",
    "CC0040_2024_海淀_一模_19",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def clean(text: str | None, limit: int | None = None) -> str:
    s = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    if limit and len(s) > limit:
        return s[:limit].rstrip() + "……"
    return s


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    questions = {
        r["question_id"]: r
        for r in read_csv(ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv")
    }

    batch_rows: dict[str, dict[str, str]] = {}
    for path in sorted((ROOT / "05_reasoner_packets" / "v7_method_learning_batched_rebuild_20260521" / "batches").glob("BATCH_*.csv")):
        for row in read_csv(path):
            batch_rows[row["question_id"]] = row

    blocks: list[str] = []
    key_rows: list[dict[str, str]] = []
    for i, qid in enumerate(SAMPLE_QIDS, 1):
        q = questions.get(qid, {})
        b = batch_rows.get(qid, {})
        title = f"{q.get('year','')} {q.get('district','')} {q.get('exam_stage','')} 第{q.get('question_no','')}题"
        ask = clean(q.get("ask_text") or b.get("ask_text"), 300)
        material = clean(q.get("material_text") or b.get("material_trigger"), 900)
        evidence = q.get("evidence_level") or b.get("evidence_level") or ""
        if not ask:
            ask = "【压力测试故意保留】本题 canonical ask_text 为空，请学生只能按材料与保险箱纪律判断是否应降级。"
        blocks.append(
            f"""## 样题 {i}：{title}（{qid}）

证据等级：{evidence}

设问：
{ask}

材料：
{material}
"""
        )
        key_rows.append(
            {
                "sample_no": str(i),
                "question_id": qid,
                "evidence_level": evidence,
                "expected_entry": b.get("batch_subtype") or b.get("student_category") or b.get("framework_entry_nodes") or "",
                "must_have_keywords": b.get("must_have_keywords") or b.get("minimum_sentence_1") or "",
                "rubric_atom_ids": b.get("clean_rubric_atom_ids") or "",
                "reference_answer_for_grader": b.get("clean_exam_answer") or b.get("full_score_sentence_bank") or " / ".join(
                    x for x in [b.get("minimum_sentence_1"), b.get("minimum_sentence_2"), b.get("minimum_sentence_3")] if x
                ),
                "known_gate_risk": "ask_text_empty_source_repair_required" if not clean(q.get("ask_text") or b.get("ask_text")) else (
                    "reference_only_no_full_score_closure" if evidence == "reference_only" else ""
                ),
            }
        )

    md = f"""# V7 方法先行零基础压力测试包

使用者身份：聪明但没有学过这套框架的高三学生。

只许使用下面的 V7 简版框架和样题题面作答，不许看评分细则和内部答案。

## 可用框架

第一步，先判断设问要交什么答案产品：

1. 判断表态：先写支持/不支持、有效/无效、构成/不构成。
2. 合同链：要约 -> 承诺 -> 成立/有效 -> 履行或违约。
3. 多主体多请求：一人一段，一请求一段。
4. 证据请求路径：请求 + 证据 + 路径。
5. 表格补全：看列名、看示例、一格一句。
6. 意义价值：先写本案处理，再写价值。
7. 创新与 AI 边界：保护对象、主体资格、意思表示、责任边界。
8. 非核心保险箱：低频、待回源、边界、转出、仅参考练笔，不能硬升核心。

第二步，把材料翻译成法律话：

材料事实 -> 法律术语 -> 得分句。

第三步，能进责任链的题，只走三条链：

- 违约链：合同成立 -> 合同有效 -> 未按约履行 -> 违约责任。
- 侵权链：权利受保护 -> 行为越界 -> 损害 -> 因果 -> 归责。
- 知识产权/竞争链：保护对象或竞争关系 -> 越界行为 -> 损害权利或秩序 -> 责任与价值。

第四步，价值只能收尾：

先写本案怎样处理，再写维护权利、规范秩序、裁判示范、法治社会。

## 作答任务

对每道题写：

1. 框架入口；
2. 第一判断；
3. 材料翻译；
4. 考场答案。

{chr(10).join(blocks)}
"""
    PACKET.write_text(md, encoding="utf-8")

    with KEY.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "sample_no",
                "question_id",
                "evidence_level",
                "expected_entry",
                "must_have_keywords",
                "rubric_atom_ids",
                "reference_answer_for_grader",
                "known_gate_risk",
            ],
        )
        writer.writeheader()
        writer.writerows(key_rows)

    print(PACKET)
    print(KEY)


if __name__ == "__main__":
    main()
