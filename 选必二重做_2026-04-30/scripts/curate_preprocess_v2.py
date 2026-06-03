#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/preprocess_v2_2026-05-03")
CURATED = BASE / "curated"

PRIVATE_ANCHORS = [
    "民法典", "民事", "合同", "要约", "承诺", "格式条款", "违约", "侵权", "赔偿", "消费者", "经营者",
    "知情权", "自主选择权", "公平交易权", "劳动合同", "劳动关系", "劳动仲裁", "用人单位", "知识产权",
    "著作权", "专利", "商标", "商业秘密", "不正当竞争", "人格权", "名誉权", "肖像权", "隐私权",
    "所有权", "物权", "质权", "相邻关系", "继承", "遗嘱", "遗赠扶养", "婚姻", "夫妻", "监护",
    "民事诉讼", "调解", "仲裁", "司法确认", "举证责任", "诉讼代理人", "回避制度",
]

LEGAL_TASK = [
    "运用《法律与生活》", "运用法律与生活", "运用法律知识", "法律依据", "案件事实", "案情", "法院",
    "人民法院", "判决", "裁判", "诉至法院", "仲裁", "合同纠纷", "侵权", "违约", "不正当竞争",
    "劳动争议", "民法典",
]

POLITICAL_NOISE = [
    "政治与法治", "依法治国", "法治政府", "人大", "政协", "国家机关", "基层治理", "行政机关",
    "检察机关", "行政公益诉讼", "公益诉讼典型案例", "全过程人民民主", "党的领导", "改革与法治",
    "国家治理体系", "粮食安全保障法", "国务院组织法", "乡村振兴促进法",
]

NONLEGAL_MODULES = [
    "经济与社会", "社会主义基本经济制度", "新质生产力", "全球南方", "经济全球化", "哲学", "逻辑与思维",
    "创新思维", "辩证思维", "充分条件假言推理", "三段论", "文化", "红色资源",
]


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow({field: row.get(field, "") for field in fields})


def count_terms(text: str, terms: list[str]) -> int:
    return sum((text or "").count(term) for term in terms)


def explicit_life_law(text: str) -> bool:
    return bool(re.search(r"运用《?法律与生活》?", text or "")) or "法律与生活" in (text or "")


def has_private_task(text: str) -> bool:
    return count_terms(text, PRIVATE_ANCHORS) >= 2 and any(cue in text for cue in LEGAL_TASK)


def noisy_without_private(text: str) -> bool:
    private = count_terms(text, PRIVATE_ANCHORS)
    if private >= 2:
        return False
    return any(cue in text for cue in POLITICAL_NOISE + NONLEGAL_MODULES)


def curation_decision(row: dict) -> tuple[str, str]:
    text = " ".join([row.get("question_excerpt", ""), row.get("rubric_excerpt", "")])
    qtype = row.get("question_type", "")
    evidence = row.get("evidence_type", "")
    qno = int(row.get("question_no") or 0)
    has_nonlegal_module = any(cue in text for cue in NONLEGAL_MODULES)
    hard_nonlegal_prompt = bool(re.search(r"运用《?(?:当代国际政治与经济|经济与社会|逻辑与思维|政治与法治)》?", text))
    if hard_nonlegal_prompt and explicit_life_law(text):
        return "defer_mixed_module", "同一题段含《法律与生活》和其他模块显性设问，需拆分小问后再进入 accepted。"
    if hard_nonlegal_prompt and not explicit_life_law(text):
        if has_private_task(text):
            return "defer_mixed_module", "含非选必二显性设问，同时有法律材料，需拆分小问后再决定。"
        return "reject_non_xuanbier", "显性设问属于非选必二模块。"
    if has_nonlegal_module and not explicit_life_law(text) and has_private_task(text):
        return "defer_mixed_module", "法律材料与非选必二模块混在同一题段，需人工拆分或复核。"
    if noisy_without_private(text):
        return "reject_non_xuanbier", "政治法治/经济哲学逻辑等噪声强，私法或程序法锚点不足。"
    if qtype == "subjective":
        if explicit_life_law(text):
            return "accept_high", "题面/设问明确《法律与生活》。"
        if evidence == "formal_or_scoring_source" and has_private_task(text):
            return "accept_high", "正式细则支撑，且有稳定私法/程序法任务。"
        if has_private_task(text):
            return "defer_needs_rubric", "题面像选必二，但正式细则或题号块未锁定。"
        return "reject_weak_signal", "主观题缺明确《法律与生活》或稳定私法/程序法任务。"
    if qtype == "choice":
        if qno > 15:
            return "reject_bad_type", "题号与选择题类型不一致。"
        if explicit_life_law(text) or count_terms(text, PRIVATE_ANCHORS) >= 2:
            if row.get("answer"):
                return "accept_high", "选择题私法/程序法锚点清楚且答案已锁定。"
            return "defer_answer_missing", "选择题像选必二，但答案未锁定，暂不生成正式错项。"
        return "reject_weak_signal", "选择题私法/程序法锚点不足。"
    return "reject_bad_type", "未知题型。"


def main() -> int:
    CURATED.mkdir(parents=True, exist_ok=True)
    index = read_csv(BASE / "LEGAL_QUESTION_INDEX_V2.csv")
    subjects = read_csv(BASE / "SUBJECTIVE_SOURCE_PACKS_V2.csv")
    choices = read_csv(BASE / "CHOICE_LEGAL_KNOWLEDGE_V2.csv")

    decisions: dict[tuple[str, str], tuple[str, str]] = {}
    accepted_index: list[dict] = []
    deferred_index: list[dict] = []
    rejected_index: list[dict] = []
    for row in index:
        decision, reason = curation_decision(row)
        key = (row["suite_id"], row["question_no"])
        decisions[key] = (decision, reason)
        row["curation_status"] = decision
        row["curation_reason"] = reason
        if decision.startswith("accept"):
            accepted_index.append(row)
        elif decision.startswith("defer"):
            deferred_index.append(row)
        else:
            rejected_index.append(row)

    accepted_keys = {(r["suite_id"], r["question_no"]) for r in accepted_index}
    deferred_keys = {(r["suite_id"], r["question_no"]) for r in deferred_index}

    accepted_subjects = []
    deferred_subjects = []
    for row in subjects:
        key = (row["suite_id"], row["question_no"])
        decision, reason = decisions.get(key, ("reject_missing_index", "未在 index 中找到。"))
        row["curation_status"] = decision
        row["curation_reason"] = reason
        if key in accepted_keys:
            accepted_subjects.append(row)
        elif key in deferred_keys:
            deferred_subjects.append(row)

    accepted_choices = []
    deferred_choices = []
    for row in choices:
        key = (row["suite_id"], row["question_no"])
        decision, reason = decisions.get(key, ("reject_missing_index", "未在 index 中找到。"))
        row["curation_status"] = decision
        row["curation_reason"] = reason
        if key in accepted_keys:
            accepted_choices.append(row)
        elif key in deferred_keys:
            deferred_choices.append(row)

    index_fields = list(index[0].keys()) + ["curation_status", "curation_reason"]
    subject_fields = list(subjects[0].keys()) + ["curation_status", "curation_reason"]
    choice_fields = list(choices[0].keys()) + ["curation_status", "curation_reason"]
    # Remove duplicate field names after adding curation columns.
    index_fields = list(dict.fromkeys(index_fields))
    subject_fields = list(dict.fromkeys(subject_fields))
    choice_fields = list(dict.fromkeys(choice_fields))

    write_csv(CURATED / "ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv", accepted_index, index_fields)
    formal_accepted_index = [r for r in accepted_index if r.get("evidence_type") == "formal_or_scoring_source"]
    write_csv(CURATED / "FORMAL_ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv", formal_accepted_index, index_fields)
    write_csv(CURATED / "DEFERRED_LEGAL_QUESTION_INDEX_V2.csv", deferred_index, index_fields)
    write_csv(CURATED / "REJECTED_LEGAL_QUESTION_INDEX_V2.csv", rejected_index, index_fields)
    write_csv(CURATED / "ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv", accepted_subjects, subject_fields)
    formal_accepted_subjects = [r for r in accepted_subjects if r.get("evidence_type") == "formal_or_scoring_source"]
    write_csv(CURATED / "FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv", formal_accepted_subjects, subject_fields)
    write_csv(CURATED / "DEFERRED_SUBJECTIVE_SOURCE_PACKS_V2.csv", deferred_subjects, subject_fields)
    write_csv(CURATED / "ACCEPTED_CHOICE_LEGAL_KNOWLEDGE_V2.csv", accepted_choices, choice_fields)
    write_csv(CURATED / "DEFERRED_CHOICE_LEGAL_KNOWLEDGE_V2.csv", deferred_choices, choice_fields)

    report = [
        "# v2 Curated 预处理报告",
        "",
        "本目录是在 v2 raw 重新抽取基础上的正式候选闸门。旧预处理没有作为输入证据。",
        "",
        f"- raw 候选：{len(index)}",
        f"- accepted：{len(accepted_index)}",
        f"- deferred：{len(deferred_index)}",
        f"- rejected：{len(rejected_index)}",
        f"- accepted subjective：{len(accepted_subjects)}",
        f"- formal accepted subjective：{len(formal_accepted_subjects)}",
        f"- deferred subjective：{len(deferred_subjects)}",
        f"- accepted choice：{len(accepted_choices)}",
        f"- deferred choice：{len(deferred_choices)}",
        "",
        "闸门规则：",
        "",
        "- 明确写《法律与生活》的题优先保留。",
        "- 没写《法律与生活》的题，必须有两个以上稳定私法/程序法锚点，并且设问或细则确实要求法律判断。",
        "- 政治法治、经济、哲学、逻辑、泛法治治理题若私法/程序法锚点不足，先 reject 或 defer。",
        "- 选择题必须答案已锁定才进入 accepted；答案未锁定但题面像选必二的进入 deferred。",
        "- 后续框架统计只允许读取 `FORMAL_ACCEPTED_*`；普通 `ACCEPTED_*` 只能作为待补原料池。",
        "",
        "## Accepted Subjective",
        "",
    ]
    for row in accepted_subjects:
        report.append(f"- `{row['year']} {row['district']} {row['stage']} {row['suite_name']} 第{row['question_no']}题`：{row['curation_reason']}")
    report.extend(["", "## Deferred Subjective", ""])
    for row in deferred_subjects:
        report.append(f"- `{row['year']} {row['district']} {row['stage']} {row['suite_name']} 第{row['question_no']}题`：{row['curation_reason']}")
    report.extend(["", "## Rejected Sample", ""])
    for row in rejected_index[:40]:
        report.append(f"- `{row['year']} {row['district']} {row['stage']} {row['suite_name']} 第{row['question_no']}题`：{row['curation_reason']}")
    (CURATED / "CURATION_REPORT_V2.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"accepted={len(accepted_index)} deferred={len(deferred_index)} rejected={len(rejected_index)}")
    print(f"accepted_subjective={len(accepted_subjects)} accepted_choice={len(accepted_choices)}")
    print(CURATED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
