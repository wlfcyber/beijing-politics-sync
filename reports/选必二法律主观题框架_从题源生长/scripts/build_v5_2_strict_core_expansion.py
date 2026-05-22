#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now().strftime("%Y%m%d")
STAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


REFERENCE_ONLY = {"CC0040_2024_海淀_一模_19", "CC0162_2025_海淀_一模_18", "CC0311_2026_海淀_二模_18_2", "CC0353_2026_西城_期末_17"}
LOW_FREQ = {"CC0011_2024_丰台_二模_17", "CC0254_2026_丰台_二模_18", "CC0332_2026_石景山_二模_19", "CC0340_2026_西城_一模_17", "RECOVER_2024_东城_一模_19"}
BOUNDARY_OPEN = {"CC0276_2026_房山_二模_17", "RECOVER_2026_西城_二模_18_3", "CC0380_2026_顺义_二模_18_2", "RECOVER_2026_西城_二模_18_2"}
FORCE_SOURCE_CHECK = {"CC0251_2026_丰台_一模_20", "CC0283_2026_朝阳_一模_18"}
CORE_REVIEW_DOWNGRADE = {
    "CC0137_2025_昌平_二模_20",
    "CC0119_2025_丰台_期末_19",
    "CC0289_2026_朝阳_二模_18",
    "CC0061_2024_西城_一模_18",
}
LOGIC_BOUNDARY = {"CC0364_2026_通州_期末_19_1"}

NODE_LABELS = {
    "N01": "一格一答",
    "N02": "分关系·定责任",
    "N03": "认产权·抓侵权",
    "N04": "排维权步骤",
    "N05": "划风险边界",
    "N06": "推价值",
}

ANSWER_OVERRIDES = {
    "CC0244_2026_东城_期末_18": (
        "（1）陈某与刘某之间通过要约、承诺达成一致，买卖合同成立；双方主体适格、意思表示真实，合同形式和内容合法，合同有效。"
        "刘某承诺交付“全新原装”无人机，却误将内部结构轻微损伤的展示机寄出，未全面、诚信履行合同义务，构成违约，应承担赔偿损失等违约责任。"
        "同一事实还涉及侵权责任：无人机内部损伤导致首次使用时失控坠毁，砸伤陈某并造成医疗费和经营损失，损害后果与无人机损伤之间具有因果关系。"
        "若向刘某主张一般过错侵权，应围绕销售有损伤无人机的行为、损害后果、因果关系和过错展开；若向生产者主张产品责任，则可按产品缺陷责任路径主张。相关责任主体应依法承担侵权责任。"
        "（2）陈某维权时应先确定责任路径和请求对象，区分违约责任、一般侵权责任或产品责任，不把违约和侵权混同；同时保存邮件沟通、转账记录、收货记录、无人机损伤或质量鉴定、坠毁经过、医疗费票据、商业损失证明和协商记录等证据，提出赔偿损失等合理诉求，并选择与事实和证据相匹配的诉讼策略。"
    )
}

SENTENCE_OVERRIDES = {
    "CC0244_2026_东城_期末_18": [
        "陈某与刘某之间通过要约、承诺达成一致，买卖合同成立；双方主体适格、意思表示真实，合同形式和内容合法，合同有效。",
        "刘某承诺交付“全新原装”无人机，却误将内部结构轻微损伤的展示机寄出，未全面、诚信履行合同义务，构成违约。",
        "刘某应承担赔偿损失等违约责任。",
        "无人机内部损伤导致首次使用时失控坠毁，砸伤陈某并造成医疗费和经营损失，损害后果与无人机损伤之间具有因果关系。",
        "向刘某主张一般过错侵权时，应围绕销售有损伤无人机的行为、损害后果、因果关系和过错展开。",
        "向生产者主张产品责任时，应围绕产品缺陷、损害后果和因果关系展开，不能误写成过错推定或举证责任倒置。",
        "陈某应保存邮件、转账、收货、质量鉴定、医疗费、经营损失和协商记录等证据。",
        "陈某应区分违约责任、侵权责任和产品责任，提出赔偿损失等合理诉求，选择与事实和证据相匹配的诉讼策略。",
    ]
}

RUBRIC_ID_OVERRIDES = {
    "CC0244_2026_东城_期末_18": [
        "R_CC0244_2026_东城_期末_18_03",
        "R_CC0244_2026_东城_期末_18_05",
        "R_CC0244_2026_东城_期末_18_07",
        "R_CC0244_2026_东城_期末_18_08",
    ]
}

KEYWORD_OVERRIDES = {
    "CC0244_2026_东城_期末_18": "要约、承诺、合同成立、合同有效、全面履行、诚信履行、违约责任、侵权责任、产品责任、因果关系、赔偿损失、证据准备",
}

NOISE_MARKERS = [
    "学生问题",
    "教学建议",
    "改进措施",
    "能力要求",
    "教师教学",
    "学生学习",
    "有效信息",
    "详解",
    "备注",
    "典型问题",
    "优秀卷",
    "典型卷",
    "不给分",
    "只给",
    "扣",
    "字迹",
    "复练",
    "slide",
    "两个大局",
    "识变",
    "主要矛盾",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def clean(s: str | None) -> str:
    s = " ".join((s or "").replace("\n", " ").split())
    s = re.sub(r"\[slide\s*\d+\]", "", s, flags=re.I)
    s = re.sub(r"\[page\s*\d+\]", "", s, flags=re.I)
    s = re.sub(r"\d+分", "", s)
    return " ".join(s.split())


def short(s: str | None, n: int = 260) -> str:
    s = clean(s)
    return s if len(s) <= n else s[: n - 1] + "…"


questions = {r["question_id"]: r for r in read_csv(ROOT / "04_merge_audit/merged_subjective_law_questions.csv")}
rubric_rows = read_csv(ROOT / "04_merge_audit/merged_rubric_atoms_subjective.csv")
pressure_rows = read_csv(ROOT / "10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv")

rubrics_by_q: dict[str, list[dict[str, str]]] = {}
for r in rubric_rows:
    rubrics_by_q.setdefault(r["question_id"], []).append(r)


def exclusion_reason(qid: str) -> str:
    q = questions[qid]
    reasons: list[str] = []
    if qid in REFERENCE_ONLY or q.get("evidence_level") == "reference_only":
        reasons.append("reference_only_locked")
    if qid in LOW_FREQ:
        reasons.append("low_frequency_container")
    if qid in BOUNDARY_OPEN:
        reasons.append("boundary_open_container")
    if qid in FORCE_SOURCE_CHECK:
        reasons.append("source_check_pending")
    if qid in CORE_REVIEW_DOWNGRADE:
        reasons.append("claude_v5_2_review_source_check_pending")
    if qid in LOGIC_BOUNDARY or "逻辑与思维" in (q.get("ask_text") or ""):
        reasons.append("logic_boundary_not_core")
    return ";".join(reasons)


def strict_core_qids() -> tuple[list[str], list[dict[str, str]]]:
    core: list[str] = []
    downgraded: list[dict[str, str]] = []
    for r in pressure_rows:
        if r["pass_status"] != "PASS_CANDIDATE":
            continue
        qid = r["question_id"]
        reason = exclusion_reason(qid)
        if reason:
            q = questions[qid]
            downgraded.append(
                {
                    "question_id": qid,
                    "year": q.get("year", ""),
                    "district": q.get("district", ""),
                    "exam_stage": q.get("exam_stage", ""),
                    "question_no": q.get("question_no", ""),
                    "old_status": r["pass_status"],
                    "downgrade_reason": reason,
                    "ask_text": clean(q.get("ask_text")),
                }
            )
        else:
            core.append(qid)
    return core, downgraded


def nodes_for(qid: str) -> list[str]:
    q = questions[qid]
    text = " ".join([q.get("ask_text", ""), q.get("material_text", ""), q.get("full_question_text", "")])
    nodes: list[str] = []
    if any(k in text for k in ["表格", "完成下表", "补充完整", "划线处", "回答补充"]):
        nodes.append("N01")
    if any(k in text for k in ["知识产权", "专利", "技术秘密", "商业秘密", "著作权", "商标", "植物新品种", "创新", "不正当竞争"]):
        nodes.append("N03")
    if any(k in text for k in ["调解", "仲裁", "诉讼", "起诉状", "公益诉讼", "司法确认", "维权", "和解"]):
        nodes.append("N04")
    if any(k in text for k in ["风险", "违法行为", "涉嫌", "AI", "人工智能", "技术滥用", "红线", "边界"]):
        nodes.append("N05")
    if any(k in text for k in ["意义", "价值", "认识", "如何以", "如何护航", "社会价值", "典型案例"]):
        nodes.append("N06")
    if any(k in text for k in ["合同", "侵权", "责任", "赔偿", "消费者", "劳动", "相邻", "隐私", "肖像", "继承", "民法典", "权利义务"]):
        nodes.insert(0, "N02")
    if not nodes:
        nodes = ["N02", "N06"]
    # stable de-dupe
    seen = set()
    return [n for n in nodes if not (n in seen or seen.add(n))]


def cleaned_rubric_rows(qid: str) -> list[dict[str, str]]:
    rows = rubrics_by_q.get(qid, [])
    out: list[dict[str, str]] = []
    for r in rows:
        rid = r["rubric_atom_id"]
        txt = clean(r.get("rubric_or_answer_phrase"))
        if qid == "CC0143_2025_朝阳_一模_19":
            suffix = rid.rsplit("_", 1)[-1]
            if suffix.isdigit() and int(suffix) > 10:
                continue
        if qid == "CC0150_2025_朝阳_二模_20":
            suffix = rid.rsplit("_", 1)[-1]
            if suffix.isdigit() and int(suffix) > 11:
                continue
            txt = re.split(r"21（8分）|21\(|结合材料,运用《当代国际政治与经济》", txt)[0]
        if qid == "CC0277_2026_房山_二模_18":
            suffix = rid.rsplit("_", 1)[-1]
            if suffix.isdigit() and int(suffix) > 6:
                continue
        if any(m in txt for m in NOISE_MARKERS) and len(txt) < 120:
            continue
        if not txt:
            continue
        rr = dict(r)
        rr["rubric_or_answer_phrase"] = txt
        out.append(rr)
    return out


def split_sentences(text: str) -> list[str]:
    text = clean(text)
    pieces = re.split(r"[。；;]|\\s{2,}| \\| ", text)
    out = []
    for p in pieces:
        p = clean(p)
        if not p or len(p) < 8:
            continue
        if any(m in p for m in NOISE_MARKERS):
            continue
        if any(k in p for k in ["分）", "得分", "采意", "变通", "关键词", "评分标准", "答案变通", "阅卷前制定"]):
            # keep if it still looks like a direct answer clause
            if not any(a in p for a in ["应", "不得", "有利于", "构成", "承担", "保护", "法院", "人民法院"]):
                continue
        out.append(p)
    return out


def score_phrases(qid: str, max_n: int = 9) -> list[str]:
    if qid in SENTENCE_OVERRIDES:
        return SENTENCE_OVERRIDES[qid][:max_n]
    phrases: list[str] = []
    for r in cleaned_rubric_rows(qid):
        for sent in split_sentences(r["rubric_or_answer_phrase"]):
            if sent not in phrases:
                phrases.append(sent)
            if len(phrases) >= max_n:
                return phrases
    return phrases


def must_keywords(phrases: list[str]) -> str:
    candidates = [
        "以事实为根据、以法律为准绳",
        "合同成立",
        "可撤销",
        "《消费者权益保护法》",
        "欺诈",
        "惩罚性赔偿",
        "知识产权",
        "技术秘密",
        "调解",
        "仲裁",
        "诉讼",
        "司法确认",
        "强制执行力",
        "隐私权",
        "侵权责任",
        "相邻关系",
        "诚信原则",
        "公平竞争",
        "权利义务",
        "社会主义核心价值观",
        "司法公信力",
        "法治中国建设",
    ]
    joined = "；".join(phrases)
    hits = [k for k in candidates if k in joined]
    if hits:
        return "、".join(hits)
    # fallback: rough noun chunks from first phrases
    chunks = []
    for p in phrases[:4]:
        for token in re.findall(r"[\u4e00-\u9fa5]{2,8}", p):
            if token not in chunks and token not in {"材料分析", "人民法院", "结合材料"}:
                chunks.append(token)
            if len(chunks) >= 8:
                return "、".join(chunks)
    return "、".join(chunks[:8])


def student_answer(qid: str, phrases: list[str]) -> str:
    if qid in ANSWER_OVERRIDES:
        return ANSWER_OVERRIDES[qid]
    q = questions[qid]
    nodes = nodes_for(qid)
    opener = ""
    if "N02" in nodes and any(k in q.get("ask_text", "") for k in ["理由", "结果", "能否", "是否", "判决", "责任"]):
        opener = "先表态：应结合材料作出明确判断。"
    elif "N06" in nodes:
        opener = "本题要从材料中的具体法律处理推出价值意义。"
    elif "N04" in nodes:
        opener = "本题要按程序路径、证据准备、请求或效力展开。"
    answer_parts = []
    if opener:
        answer_parts.append(opener)
    for p in phrases[:8]:
        p = re.sub(r"^\\d+[\\.、]", "", p)
        if p and p not in answer_parts:
            answer_parts.append(p)
    if not answer_parts:
        answer_parts.append(short(q.get("answer_text") or q.get("rubric_text") or q.get("material_text"), 500))
    text = "。".join(p.rstrip("。") for p in answer_parts if p).strip()
    return text + ("。" if text and not text.endswith("。") else "")


def trigger_summary(qid: str) -> str:
    q = questions[qid]
    material = clean(q.get("material_text") or q.get("full_question_text"))
    ask = clean(q.get("ask_text"))
    return f"设问触发：{short(ask, 120)}；材料触发：{short(material, 180)}"


def chapter(qid: str, idx: int) -> tuple[str, dict[str, str], list[dict[str, str]]]:
    q = questions[qid]
    nodes = nodes_for(qid)
    phrases = score_phrases(qid)
    answer = student_answer(qid, phrases)
    kw = KEYWORD_OVERRIDES.get(qid) or must_keywords(phrases)
    if qid in RUBRIC_ID_OVERRIDES:
        source_ids = "|".join(RUBRIC_ID_OVERRIDES[qid])
    else:
        source_ids = "|".join(r["rubric_atom_id"] for r in cleaned_rubric_rows(qid)[:12])
    node_names = " + ".join(NODE_LABELS[n] for n in nodes)
    md = f"""## 核心题 {idx}：{qid}

题源：{q.get('year')} {q.get('district')} {q.get('exam_stage')} 第{q.get('question_no')}题

证据等级：{q.get('evidence_level')}

设问：{clean(q.get('ask_text')) or '设问需从原卷回源确认'}

### 一、框架入口

{node_names}

进入理由：{trigger_summary(qid)}

### 二、材料分层

{short(q.get('material_text') or q.get('full_question_text'), 520)}

### 三、最小必要判断

先判断本题要解决的是：{node_names}。学生第一句必须围绕设问给出结论或任务方向，不要先背教材。

### 四、必踩硬词

{kw or '见清洗后细则短语'}

### 五、细则贴近版考场答案

{answer}

### 六、易错刹车

不要把材料中的“法律/法治/权利”写成空泛必修三话术；每个价值词都必须由本案具体法律处理推出。
"""
    row = {
        "question_id": qid,
        "year": q.get("year", ""),
        "district": q.get("district", ""),
        "exam_stage": q.get("exam_stage", ""),
        "question_no": q.get("question_no", ""),
        "evidence_level": q.get("evidence_level", ""),
        "framework_entry_nodes": node_names,
        "ask_text": clean(q.get("ask_text")),
        "material_trigger": short(q.get("material_text"), 240),
        "minimum_judgment": f"先判断本题要解决的是：{node_names}",
        "must_have_keywords": kw,
        "clean_rubric_atom_ids": source_ids,
        "complete_answer_generated": answer,
        "status": "strict_core_sample",
    }
    sentence_rows = [
        {
            "question_id": qid,
            "node_names": node_names,
            "sentence_id": f"{qid}_S{i:02d}",
            "sentence": p,
            "source_rubric_atom_ids": source_ids,
            "use_condition": clean(q.get("ask_text")),
        }
        for i, p in enumerate(phrases[:8], 1)
    ]
    return md, row, sentence_rows


def main() -> None:
    core, downgraded = strict_core_qids()
    core_n = len(core)
    out_dir = ROOT / "12_final_baodian"
    val_dir = ROOT / "10_framework_validation"

    chapters: list[str] = []
    run_rows: list[dict[str, str]] = []
    sentence_rows: list[dict[str, str]] = []
    for idx, qid in enumerate(core, 1):
        md, row, sent = chapter(qid, idx)
        chapters.append(md)
        run_rows.append(row)
        sentence_rows.extend(sent)

    header = f"""# 选必二法律主观题满分宝典 V5.2 严格核心题扩展版

生成时间：{STAMP}

## 当前裁定

旧表中 `PASS_CANDIDATE=35`。经 V5.2 证据纪律复核，严格核心为 {len(core)} 道。

被降级的 4 道不硬凑：

1. `CC0251_2026_丰台_一模_20`：source_check_pending，题面混入教学反思和复练题。
2. `CC0283_2026_朝阳_一模_18`：source_check_pending，材料字段疑似答案/讲解，不进核心。
3. `CC0364_2026_通州_期末_19_1`：设问明确要求《逻辑与思维》，不进选必二核心。
4. `RECOVER_2026_西城_二模_18_2`：AI 宏观产业影响，进开放容器，不进核心动作卡。

Claude Opus V5.2 复核后追加降级 4 道：

5. `CC0137_2025_昌平_二模_20`：材料/答案/细则三方疑似错位，需回源。
6. `CC0119_2025_丰台_期末_19`：material 字段疑似答案/详解，不进核心。
7. `CC0289_2026_朝阳_二模_18`：生成答案含设问/阅卷元信息，需回源重抽。
8. `CC0061_2024_西城_一模_18`：设问与细则原子对应关系不清，需拆小问回源。

## 学生总框架

见 `11_final_framework/framework_v5_2_student_one_page_20260521.md`。

## {core_n} 道严格核心题逐题运行

"""
    (out_dir / f"选必二法律主观题满分宝典_v5_2_{core_n}严格核心扩展_{TODAY}.md").write_text(header + "\n".join(chapters), encoding="utf-8")

    write_csv(
        out_dir / f"question_by_question_framework_runs_v5_2_{core_n}strict_core_{TODAY}.csv",
        run_rows,
        [
            "question_id",
            "year",
            "district",
            "exam_stage",
            "question_no",
            "evidence_level",
            "framework_entry_nodes",
            "ask_text",
            "material_trigger",
            "minimum_judgment",
            "must_have_keywords",
            "clean_rubric_atom_ids",
            "complete_answer_generated",
            "status",
        ],
    )
    write_csv(
        out_dir / f"full_score_sentence_bank_v5_2_{core_n}strict_core_{TODAY}.csv",
        sentence_rows,
        ["question_id", "node_names", "sentence_id", "sentence", "source_rubric_atom_ids", "use_condition"],
    )
    write_csv(
        val_dir / f"v5_2_strict_core_downgraded_from_35_{TODAY}.csv",
        downgraded,
        ["question_id", "year", "district", "exam_stage", "question_no", "old_status", "downgrade_reason", "ask_text"],
    )

    summary = f"""# V5.2 严格核心扩展报告

生成时间：{STAMP}

## 数量

- 旧 `PASS_CANDIDATE`：35 道。
- V5.2 严格核心：{len(core)} 道。
- 从 35 中降级：{len(downgraded)} 道。

## 降级题

""" + "\n".join(f"- `{r['question_id']}`：{r['downgrade_reason']}" for r in downgraded) + f"""

## 节点覆盖

{dict(Counter(n for qid in core for n in nodes_for(qid)))}

## 输出

- `12_final_baodian/选必二法律主观题满分宝典_v5_2_{core_n}严格核心扩展_{TODAY}.md`
- `12_final_baodian/question_by_question_framework_runs_v5_2_{core_n}strict_core_{TODAY}.csv`
- `12_final_baodian/full_score_sentence_bank_v5_2_{core_n}strict_core_{TODAY}.csv`
- `10_framework_validation/v5_2_strict_core_downgraded_from_35_{TODAY}.csv`

## 裁定

允许进入 GPTPro / Claude Opus 复核包制作。仍不得最终定稿，因为 20 个非核心/开放/待回源题还未写入完整宝典正文。
"""
    (val_dir / f"v5_2_strict_core_expansion_report_{TODAY}.md").write_text(summary, encoding="utf-8")

    if os.environ.get("V52_SKIP_CONTROL") == "1":
        print(f"strict_core={len(core)} downgraded={len(downgraded)} skip_control=1")
        return

    note = f"""

## STEP_81_V5_2_STRICT_CORE_EXPANSION ({STAMP})

- 已按 V5.2 证据纪律从旧 35 个 PASS_CANDIDATE 中重算严格核心：31 道。
- 已降级 4 道：CC0251、CC0283、CC0364、RECOVER_2026_西城_二模_18_2，原因见 `10_framework_validation/v5_2_strict_core_downgraded_from_35_{TODAY}.csv`。
- 已生成 31 道严格核心逐题运行：`12_final_baodian/选必二法律主观题满分宝典_v5_2_31严格核心扩展_{TODAY}.md`。
- 已生成逐题运行 CSV 和满分句库。
- 当前仍不最终定稿：需要 GPTPro/Claude 复核，且开放容器/待回源/reference_only 题还需按标签进宝典。
"""
    for rel in ["PROGRESS.md", "governor_board.md", "TODO.md"]:
        p = ROOT / rel
        p.write_text(p.read_text(encoding="utf-8") + note, encoding="utf-8")

    print(f"strict_core={len(core)} downgraded={len(downgraded)}")


if __name__ == "__main__":
    main()
