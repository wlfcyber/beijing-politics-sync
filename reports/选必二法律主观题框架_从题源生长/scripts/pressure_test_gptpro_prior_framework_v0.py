#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pressure-test GPTPro prior-framework v0 against the STEP_29 65-row corpus.

This is a conservative routing test, not a final scoring claim. It checks
whether each question can start from GPTPro's seven action nodes and records
where local evidence or source hygiene must still block promotion.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "04_merge_audit/merged_subjective_law_questions.csv"
RUBRICS = ROOT / "04_merge_audit/merged_rubric_atoms_subjective.csv"
OUT_CSV = ROOT / "10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv"
OUT_MD = ROOT / "10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.md"


NODES = {
    "LAW_V0_N01": "一格一答",
    "LAW_V0_N02": "先判后证",
    "LAW_V0_N03": "切责成链",
    "LAW_V0_N04": "护创新",
    "LAW_V0_N05": "走救济",
    "LAW_V0_N06": "划边界",
    "LAW_V0_N07": "补价值",
}


REFERENCE_ONLY = {"CC0040", "CC0162", "CC0311", "CC0353"}
BOUNDARY_OPEN = {
    "CC0276",
    "CC0380",
    "RECOVER_2026_西城_二模_18_3",
}
LOW_FREQ_CONTAINER = {
    "CC0011",
    "CC0332",
    "CC0340",
    "RECOVER_2024_东城_一模_19",
    "CC0254",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def short_id(qid: str) -> str:
    return qid.split("_", 1)[0] if qid.startswith("CC") else qid


def has_any(text: str, words: list[str]) -> bool:
    return any(w in text for w in words)


def route_nodes(row: dict[str, str]) -> tuple[list[str], list[str]]:
    ask = row.get("ask_text", "") or ""
    mat = row.get("material_text", "") or ""
    rub = row.get("rubric_text", "") or row.get("answer_text", "") or ""
    text = ask + "\n" + mat + "\n" + rub
    reasons: list[str] = []
    nodes: list[str] = []

    if has_any(text, ["表格", "表中", "填入", "填写", "项目", "维度"]) and has_any(text, ["理由", "依据", "措施", "意义", "机制", "内容", "观点"]):
        nodes.append("LAW_V0_N01")
        reasons.append("材料/设问呈现表格、格子或分栏任务，优先一格一答。")

    if has_any(ask + rub, ["评析", "是否", "谈谈对", "认识", "判决", "法院", "支持", "不支持", "有效", "无效", "构成", "法理依据", "判定", "理由"]):
        nodes.append("LAW_V0_N02")
        reasons.append("设问或细则要求先给判断、裁判理由、是否支持/有效/构成。")

    if has_any(text, ["合同", "要约", "承诺", "履行", "违约", "解除", "侵权", "赔偿", "责任", "消费者", "欺诈", "劳动", "用人单位", "劳动者", "相邻", "共有", "物权", "人格权", "名誉权", "健康权", "生命权", "肖像权"]):
        nodes.append("LAW_V0_N03")
        reasons.append("材料/细则触发合同、侵权、消费、劳动、相邻或人格权等责任成立链。")

    if has_any(text, ["知识产权", "著作权", "商标", "专利", "商业秘密", "不正当竞争", "商业诋毁", "混淆", "创新", "核心代码", "数字人", "AI 图案", "人工智能生成"]):
        nodes.append("LAW_V0_N04")
        reasons.append("材料/细则触发知识产权、竞争秩序或创新保护。")

    if has_any(text, ["调解", "仲裁", "诉讼", "起诉状", "证据", "举证", "司法确认", "强制执行", "公益诉讼", "维权", "请求", "诉讼请求", "和解"]):
        nodes.append("LAW_V0_N05")
        reasons.append("材料/设问触发纠纷解决、证据、诉求或程序救济。")

    if has_any(text, ["风险", "合规", "边界", "人工智能", "AI", "开源", "智能体", "数据", "算法", "数字员工", "治理", "涉外法治", "国家治理"]):
        nodes.append("LAW_V0_N06")
        reasons.append("材料/细则出现 AI、数据、合规风险或治理边界，需要先划边界。")

    if has_any(ask + rub, ["意义", "价值", "作用", "有利于", "弘扬", "促进", "维护", "规范", "秩序", "公平", "正义", "诚信", "核心价值观", "社会整体福祉"]):
        nodes.append("LAW_V0_N07")
        reasons.append("设问/细则要求从具体法律处理推出权益、秩序或价值意义。")

    # Stable order and de-duplication.
    ordered = []
    for node in NODES:
        if node in nodes and node not in ordered:
            ordered.append(node)
    return ordered, reasons


def main() -> None:
    rows = read_csv(QUESTIONS)
    rubrics = defaultdict(list)
    for r in read_csv(RUBRICS):
        rubrics[r.get("question_id", "")].append(r.get("rubric_atom_id", ""))

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    out_rows: list[dict[str, str]] = []
    status_counter: Counter[str] = Counter()
    node_counter: Counter[str] = Counter()
    risk_rows: list[dict[str, str]] = []

    for row in rows:
        qid = row["question_id"]
        sid = short_id(qid)
        nodes, reasons = route_nodes(row)
        flags: list[str] = []
        notes: list[str] = []
        ask = (row.get("ask_text") or "").strip()
        evidence = row.get("evidence_level", "")

        if not ask or ask.lower() == "nan" or "设问待" in ask:
            flags.append("ask_source_check")
        if evidence == "reference_only" or sid in REFERENCE_ONLY:
            flags.append("reference_only_lock")
            status = "PARTIAL_REFERENCE_ONLY"
            notes.append("只可作写法参考，不能支撑核心节点。")
        elif sid in BOUNDARY_OPEN or qid in BOUNDARY_OPEN:
            flags.append("formal_boundary_open")
            status = "PARTIAL_BOUNDARY_OPEN"
            notes.append("formal 但边界/综合明显，需单列开放容器，不升核心私法节点。")
        elif sid in LOW_FREQ_CONTAINER or qid in LOW_FREQ_CONTAINER:
            flags.append("low_freq_singleton")
            status = "PARTIAL_LOW_FREQ_CONTAINER"
            notes.append("低频 formal singleton，可教但暂不生成稳定核心套路。")
        elif not nodes:
            flags.append("no_entry_node")
            status = "FAIL_NO_ENTRY"
            notes.append("GPTPro v0 七节点无法稳定启动，需回源或补节点。")
        elif "ask_source_check" in flags:
            status = "PARTIAL_SOURCE_CHECK"
            notes.append("节点可试跑，但设问层需要回源补正。")
        else:
            status = "PASS_CANDIDATE"
            notes.append("可从 GPTPro v0 动作节点启动；仍需逐句对齐细则后才能写入宝典。")

        for node in nodes:
            node_counter[f"{node}:{NODES[node]}"] += 1
        status_counter[status] += 1

        patch_needed = "no" if status == "PASS_CANDIDATE" else "yes"
        if flags:
            risk_rows.append({"question_id": qid, "status": status, "flags": "|".join(flags)})

        out_rows.append(
            {
                "question_id": qid,
                "year": row.get("year", ""),
                "district": row.get("district", ""),
                "exam_stage": row.get("exam_stage", ""),
                "question_no": row.get("question_no", ""),
                "evidence_level": evidence,
                "ask_text": ask,
                "entry_nodes": "|".join(f"{n}:{NODES[n]}" for n in nodes),
                "primary_node": f"{nodes[0]}:{NODES[nodes[0]]}" if nodes else "",
                "entry_reason": "；".join(reasons),
                "rubric_atom_count": str(len([x for x in rubrics.get(qid, []) if x])),
                "rubric_atom_ids_sample": "|".join(rubrics.get(qid, [])[:8]),
                "source_check_flags": "|".join(flags),
                "pass_status": status,
                "patch_needed": patch_needed,
                "pressure_notes": "；".join(notes),
            }
        )

    fieldnames = list(out_rows[0].keys())
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    lines: list[str] = []
    lines.append("# GPTPro Prior-Framework v0 65-Question Pressure Test")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append("`CONDITIONAL_PASS_NEEDS_PATCHES`")
    lines.append("")
    lines.append("GPTPro v0 比之前的审计式版本更像学生框架，但仍不能直接升为最终框架。它可以启动多数题，真正的门槛在于：reference_only 锁死、边界综合题不升核心、低频 singleton 只进容器、设问缺失题先回源。")
    lines.append("")
    lines.append("## Corpus")
    lines.append("")
    lines.append(f"- Questions tested: {len(rows)}")
    lines.append(f"- Evidence levels: {dict(Counter(r.get('evidence_level', '') for r in rows))}")
    lines.append("")
    lines.append("## Status Counts")
    lines.append("")
    for k, v in status_counter.most_common():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("## Node Coverage")
    lines.append("")
    for k, v in node_counter.most_common():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("## Rows Needing Patch Or Guard")
    lines.append("")
    for r in risk_rows:
        lines.append(f"- {r['question_id']}: {r['status']} ({r['flags']})")
    lines.append("")
    lines.append("## Promotion Rule")
    lines.append("")
    lines.append("Only `PASS_CANDIDATE` rows may be used to draft core student answer examples, and even those require rubric-atom sentence matching before entering a new宝典. `PARTIAL_*` rows can appear only as reference, boundary, open-container, or teacher caution examples.")
    lines.append("")
    lines.append("## Next Step")
    lines.append("")
    lines.append("Build a revised framework draft from the passing core while writing a separate open-container chapter for partial rows. Do not flatten all 65 into equal full-score templates.")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {OUT_CSV}")
    print(f"wrote {OUT_MD}")
    print("status", dict(status_counter))
    print("nodes", dict(node_counter))


if __name__ == "__main__":
    main()
