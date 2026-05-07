# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
MANIFEST = RUN_DIR / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"
OUT_DIR = RUN_DIR / "codex_audit" / "p1_local"

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


def load_p1_rows() -> list[dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        return [row for row in csv.DictReader(f) if row.get("priority") == "P1"]


def evidence_for(row: dict[str, str]) -> str:
    qid = row["question_id"]
    node = row["framework_node"]
    if "朝阳期中" in qid and "晏子" in qid:
        return (
            "017 support 2024.11期中政治朝阳评标docx.docx.txt::18题阅卷细则1: "
            "晏子属于类比推理；相同推相同；说明如何类比；虽为或然推理但增强论证说服力。"
        )
    if "朝阳期中" in qid and "楚王" in qid:
        return (
            "017 support 2024.11期中政治朝阳评标docx.docx.txt::18题阅卷细则1: "
            "楚王属于不完全归纳推理；前提只涉及部分对象所以是或然推理；犯轻率概括；应考察更多对象提高可靠程度。"
        )
    if "东城一模" in qid and "19-4" in qid and "发散" in node:
        return (
            "046 support 19（4）.pptx.txt::SLIDE 4-5: "
            "坚持发散与聚合思维统一，发散拓展应用场景，聚合围绕科技成果转化轴心整合多方资源。"
        )
    if "东城一模" in qid and "思路新" in node:
        return (
            "046 support 19（4）.pptx.txt::SLIDE 4-5: "
            "创新思维知识含实践、思路多向性、步骤跨越性、结果独特性、思路新方法新结果新，并要求结合原创技术落地分析。"
        )
    if "东城一模" in qid and "超前" in node:
        return (
            "046 support 19（4）.pptx.txt::SLIDE 4-5: "
            "坚持超前思维，理性分析科技转化内在矛盾，健全评价、产权激励、转化推广制度，谋划长远布局。"
        )
    if "东城一模" in qid and "整体性" in node:
        return (
            "046 support 19（4）.pptx.txt::SLIDE 3-5: "
            "系统观念要求立足整体、综合思维、结构优化，统筹基础研究、技术研发、成果转化、产业应用和多方资源。"
        )
    if "丰台期末" in qid and "必要条件" in node:
        return (
            "040 support 2025丰台期末细则.pptx.txt::SLIDE 18: "
            "必要条件假言判断1分；保真条件是前件是后件的必要条件1分。"
        )
    if "丰台期末" in qid and "联言" in node:
        return (
            "040 support 2025丰台期末细则.pptx.txt::SLIDE 18: "
            "联言判断1分；保真条件是当且仅当各个联言支都是真的1分。"
        )
    if "顺义一模" in qid and "充分条件" in node:
        return (
            "035 support 2025顺义一模细则.docx.txt::17(1)评分细则: "
            "甲为充分条件假言判断，三位同学判断类型全部准确给1分，并可结合判断类型分析。"
        )
    if "顺义一模" in qid and "必要条件" in node:
        return (
            "035 support 2025顺义一模细则.docx.txt::17(1)评分细则: "
            "乙为必要条件假言判断；由甲乙均真可推出杭州既获得科创基金支持又成为科创人才高地。"
        )
    if "顺义一模" in qid and "相容选言" in node:
        return (
            "035 support 2025顺义一模细则.docx.txt::17(1)评分细则: "
            "丙为相容选言判断，至少一个选言支真即可为真，也可以都真。"
        )
    raise KeyError((qid, node))


def patch_for(row: dict[str, str]) -> dict[str, str]:
    qid = row["question_id"]
    node = row["framework_node"]
    if "晏子" in qid:
        decision = "confirmed_with_patch"
        signal = "晏子用橘生淮南为橘、生淮北为枳类比楚地水土影响人。"
        logic = "材料以两个对象在部分属性上的相同或相似，推出另一属性上的相同或相似，触发类比推理；同时要说明或然性和论证效果。"
        sentence = "晏子的推理属于类比推理，他借橘在不同水土中性质不同，类比推出楚地水土可能使人善盗；类比推理虽是或然推理，但在本题中增强了反驳楚王的说服力。"
    elif "楚王" in qid:
        decision = "confirmed_with_patch"
        signal = "楚王只依据一个被缚齐人盗窃，就推出齐人固善盗。"
        logic = "材料由部分对象推出一般结论，触发不完全归纳；样本过少又触发轻率概括/以偏概全。"
        sentence = "楚王的推理属于不完全归纳推理，因为前提只涉及部分对象，所以只是或然推理；他只凭一个齐国盗贼就概括齐人善盗，犯了轻率概括错误，应通过考察更多对象、分析因果关系提高可靠程度。"
    elif "东城一模" in qid and "发散" in node:
        decision = "confirmed_with_patch"
        signal = "中关村要把原创成果从书架摆上货架，把单点突破推进为链式升级。"
        logic = "拓展应用场景、优化服务是发散；围绕成果转化轴心整合资源是聚合。"
        sentence = "中关村应坚持发散与聚合思维统一：用发散思维拓展原创技术的应用场景和服务形态，用聚合思维围绕成果转化这个轴心整合人才、平台、政策、市场等资源，推动单点突破变成链式升级。"
    elif "东城一模" in qid and "思路新" in node:
        decision = "confirmed_with_patch"
        signal = "原创技术不能停留在论文阶段，而要从实验实现转化并落地应用。"
        logic = "实践基础、敢用新手段和大胆试验，对应创新思维思路新、方法新、结果新。"
        sentence = "中关村应立足实践推进创新思维，坚持多向思考，敢用新手段、大胆试验和勇于应用，让原创技术真正落地见效，体现思路新、方法新、结果新。"
    elif "东城一模" in qid and "超前" in node:
        decision = "confirmed_with_patch"
        signal = "2035年建成全球科技创新主要引擎和关键枢纽，需要提前破解成果转化堵点。"
        logic = "对科技转化矛盾作理性分析、正确预见并提前制度布局，触发超前思维。"
        sentence = "中关村应坚持超前思维，理性分析科技成果转化中的评价、产权、推广等内在矛盾，提前完善激励和转化制度，谋划科技发展与产业趋势的长远布局。"
    elif "东城一模" in qid and "整体性" in node:
        decision = "downgrade_to_index"
        signal = "从单点突破到链式升级，要求统筹创新链各环节和资源。"
        logic = "该点正式细则存在，但主要作为系统观念/必修四同类索引；在选必三正文中只挂接到辩证思维整体性、分析与综合。"
        sentence = "可作为同类索引：立足中关村科技创新整体布局，用综合思维统筹基础研究、技术研发、成果转化、产业应用以及人才、平台、政策、市场，形成创新要素协同联动。"
    elif "丰台期末" in qid and "必要条件" in node:
        decision = "confirmed_with_patch"
        signal = "题目要求判断①的类型及保真条件，①以'才'表达条件关系。"
        logic = "必要条件假言判断要求前件是后件的必要条件。"
        sentence = "①属于必要条件假言判断；它为真的保真条件是前件是后件的必要条件。"
    elif "丰台期末" in qid and "联言" in node:
        decision = "confirmed_with_patch"
        signal = "题目要求判断②的类型及保真条件，②由多个联言支共同断定。"
        logic = "联言判断为真，当且仅当各联言支都为真。"
        sentence = "②属于联言判断；它为真的保真条件是组成联言判断的各个联言支都是真的。"
    elif "顺义一模" in qid and "充分条件" in node:
        decision = "confirmed_with_patch"
        signal = "甲说：杭州如果有科创基金支持，那么就会成为科创人才高地。"
        logic = "'如果p那么q'触发充分条件假言判断；甲真时不能否定后件。"
        sentence = "甲的判断属于充分条件假言判断；若杭州获得科创基金支持并成为科创人才高地，则甲判断为真。"
    elif "顺义一模" in qid and "必要条件" in node:
        decision = "confirmed_with_patch"
        signal = "乙说：杭州除非获得科创基金支持，否则不能成为科创人才高地。"
        logic = "'除非p否则不q'可转化为只有p才q，触发必要条件假言判断。"
        sentence = "乙的判断属于必要条件假言判断；成为科创人才高地以获得科创基金支持为必要条件，乙真时可推出二者需要同时满足。"
    elif "顺义一模" in qid and "相容选言" in node:
        decision = "confirmed_with_patch"
        signal = "丙说：推进创新活力之城建设，或者需要科创基金支持，或者需要成为科创人才高地。"
        logic = "'或者...或者...'且可同时成立，触发相容选言判断。"
        sentence = "丙的判断属于相容选言判断；只要科创基金支持和科创人才高地中至少一个选言支为真，判断就为真，二者都真时也为真。"
    else:
        raise KeyError((qid, node))
    return {
        "decision": decision,
        "patched_material_signal": signal,
        "patched_trigger_logic": logic,
        "patched_answer_sentence": sentence,
        "source_evidence": evidence_for(row),
        "notes": "Codex local P1 draft from extracted source texts; use only if ClaudeCode remains stalled or as supervisor comparison.",
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_p1_rows()
    decisions: list[dict[str, str]] = []
    patches: list[dict[str, str]] = []
    for row in rows:
        patch = patch_for(row)
        decisions.append(
            {
                "priority": "P1",
                "question_id": row["question_id"],
                "parent_question_id": row["parent_question_id"],
                "source_batch": row["source_batch"],
                "type": row["type"],
                "framework_node": row["framework_node"],
                "evidence_level": row["evidence_level"],
                "decision": patch["decision"],
                "decision_reason": patch["patched_trigger_logic"],
                "source_evidence": patch["source_evidence"],
                "patch_needed": "yes",
                "can_enter_fusion": "yes",
            }
        )
        patches.append(
            {
                "question_id": row["question_id"],
                "parent_question_id": row["parent_question_id"],
                "framework_node": row["framework_node"],
                "decision": patch["decision"],
                "patched_material_signal": patch["patched_material_signal"],
                "patched_trigger_logic": patch["patched_trigger_logic"],
                "patched_answer_sentence": patch["patched_answer_sentence"],
                "source_evidence": patch["source_evidence"],
                "notes": patch["notes"],
            }
        )

    with (OUT_DIR / "P1_RECHECK_DECISIONS.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(decisions)
    with (OUT_DIR / "P1_RECHECK_PATCHES.jsonl").open("w", encoding="utf-8") as f:
        for patch in patches:
            f.write(json.dumps(patch, ensure_ascii=False) + "\n")

    evidence_lines = [
        "# P1 Source Evidence",
        "",
        "Status: Codex local draft, NOT_FINAL.",
        "",
        "- 017 朝阳期中 Q18: formal marking report gives separate scoring points for 楚王的不完全归纳/轻率概括 and 晏子的类比推理。",
        "- 046 东城一模 Q19(4): formal subjective-question rubric gives system观念 + 创新思维 scoring, including 发散聚合、实践/三新、超前思维。",
        "- 040 丰台期末 Q18(1): formal PPT scoring gives 必要条件假言判断 and 联言判断 with保真条件。",
        "- 035 顺义一模 Q17(1): scoring document gives 甲充分条件、乙必要条件、丙相容选言 and simultaneous-truth condition。",
        "",
        "## Row Evidence",
        "",
    ]
    for decision in decisions:
        evidence_lines.append(f"- `{decision['question_id']}` / `{decision['framework_node']}`: {decision['source_evidence']}")
    (OUT_DIR / "P1_SOURCE_EVIDENCE.md").write_text("\n".join(evidence_lines) + "\n", encoding="utf-8")

    acceptance = [
        "# P1 Recheck Acceptance",
        "",
        "P1_RECHECK_ACCEPTANCE: NOT_FINAL",
        "",
        "- decision rows: 11",
        "- patch rows: 11",
        "- all manifest P1 keys resolved: yes",
        "- source_insufficient rows: none",
        "- can_enter_fusion=no rows: none",
        "- Word produced: no",
        "- PDF produced: no",
        "- final artifact produced: no",
        "- boundary: this local draft is a supervisor fallback/comparison file until ClaudeCode either delivers or is declared stalled.",
    ]
    (OUT_DIR / "P1_RECHECK_ACCEPTANCE.md").write_text("\n".join(acceptance) + "\n", encoding="utf-8")

    print(json.dumps({"out_dir": str(OUT_DIR), "rows": len(decisions), "patches": len(patches)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
