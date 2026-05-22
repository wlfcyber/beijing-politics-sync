#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import re
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
TODAY = "20260521"
STAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

SRC_MD = ROOT / "12_final_baodian" / f"选必二法律主观题满分训练宝典_v5_7_27核心38题保分索引小修版_{TODAY}.md"
OUT_MD = ROOT / "12_final_baodian" / f"选必二法律主观题满分训练宝典_v5_8_27核心38题保分索引_P1入口修补候选版_{TODAY}.md"
PATCH_REPORT = ROOT / "10_framework_validation" / f"v5_8_claude_guarded_patch_report_{TODAY}.md"
NON_CORE_V56 = ROOT / "12_final_baodian" / f"non_core_guardrails_v5_6_{TODAY}.csv"
NON_CORE_V58 = ROOT / "12_final_baodian" / f"non_core_guardrails_v5_8_{TODAY}.csv"
RUNS_V55 = ROOT / "12_final_baodian" / f"question_by_question_framework_runs_v5_5_27core65guard_{TODAY}.csv"
RUNS_V58 = ROOT / "12_final_baodian" / f"question_by_question_framework_runs_v5_8_27core65guard_{TODAY}.csv"
OLD70 = ROOT / "tool_outputs" / "pre_cowork_refined_merged_canonical_backup_20260519_175535" / "merged_subjective_law_questions.csv"
CURRENT65 = ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv"
BOUNDARY_LEDGER = ROOT / "04_merge_audit" / "boundary_patched_20260519" / "boundary_patched_excluded_pending_ledger.csv"
DELTA_CSV = ROOT / "04_merge_audit" / f"candidate70_to_current65_delta_ledger_{TODAY}.csv"
DELTA_MD = ROOT / "04_merge_audit" / f"candidate70_to_current65_delta_summary_{TODAY}.md"


ENTRY_BY_CORE_INDEX = {
    1: ("分关系·定责任", "推价值"),
    2: ("分关系·定责任", "推价值"),
    3: ("推价值", "分关系·定责任"),
    4: ("分关系·定责任", "推价值"),
    5: ("分关系·定责任", "推价值"),
    6: ("推价值", "认产权·抓侵权"),
    7: ("分关系·定责任", "排维权步骤"),
    8: ("分关系·定责任", "排维权步骤"),
    9: ("分关系·定责任", "排维权步骤"),
    10: ("分关系·定责任", ""),
    11: ("分关系·定责任", "推价值"),
    12: ("认产权·抓侵权", "分关系·定责任"),
    13: ("推价值", "分关系·定责任"),
    14: ("认产权·抓侵权", "推价值"),
    15: ("分关系·定责任", ""),
    16: ("分关系·定责任", "排维权步骤"),
    17: ("分关系·定责任", "推价值"),
    18: ("一格一答", "认产权·抓侵权"),
    19: ("一格一答", "分关系·定责任"),
    20: ("排维权步骤", ""),
    21: ("排维权步骤", ""),
    22: ("认产权·抓侵权", "划风险边界"),
    23: ("排维权步骤", "划风险边界"),
    24: ("分关系·定责任", "划风险边界"),
    25: ("分关系·定责任", "划风险边界"),
    26: ("排维权步骤", "划风险边界"),
    27: ("分关系·定责任", ""),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def entry_text(primary: str, secondary: str) -> str:
    if secondary:
        return f"入口：主卡={primary}；辅卡={secondary}"
    return f"入口：主卡={primary}；辅卡=无"


def patch_core_entries(text: str) -> str:
    current_index = 0
    out: list[str] = []
    for line in text.splitlines():
        m = re.match(r"## 核心题 (\d+)$", line)
        if m:
            current_index = int(m.group(1))
        if line.startswith("入口：") and current_index in ENTRY_BY_CORE_INDEX:
            primary, secondary = ENTRY_BY_CORE_INDEX[current_index]
            out.append(entry_text(primary, secondary))
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def patch_cc0025(text: str) -> str:
    text = text.replace(
        "- 意义写劳动者权益和平台经济",
        "- 意义写裁判参照、劳动者权益、平台经济\n- 补道德意义：公平诚信原则和社会主义核心价值观",
    )
    text = text.replace(
        "该典型案例为仲裁机构和人民法院处理平台经济劳动争议提供参照，有利于提高以事实为依据、以法律为准绳公正裁决的能力；有利于保障新就业形态劳动者合法权益，发展和谐稳定的劳动关系；也有利于引导平台企业规范用工，促进平台经济良性发展和经济社会发展。",
        "该典型案例为仲裁机构和人民法院处理平台经济劳动争议提供参照，有利于提高以事实为依据、以法律为准绳公正裁决的能力；有利于保障新就业形态劳动者合法权益，发展和谐稳定的劳动关系；符合民法公平、诚信等基本原则，践行社会主义核心价值观；也有利于引导平台企业规范用工，促进平台经济良性发展和经济社会发展。",
    )
    text = text.replace(
        "- 该案例有利于统一裁判尺度，保护新就业形态劳动者权益，引导平台经济良性发展。",
        "- 该案例有利于统一裁判尺度，保护新就业形态劳动者权益，引导平台经济良性发展。\n- 该裁决符合公平、诚信等民法基本原则，践行社会主义核心价值观。",
    )
    text = text.replace(
        "人格从属性、经济从属性、组织从属性、事实劳动关系、平台派单、奖惩制度、新就业形态劳动者权益、平台经济良性发展",
        "人格从属性、经济从属性、组织从属性、事实劳动关系、平台派单、奖惩制度、新就业形态劳动者权益、公平诚信原则、社会主义核心价值观、平台经济良性发展",
    )
    text = text.replace(
        "意义部分要分别落到裁判参照、劳动者权益和平台经济发展。",
        "意义部分要分别落到裁判参照、劳动者权益、民法公平诚信原则/社会主义核心价值观和平台经济发展。",
    )
    return text


def patch_non_core_headings_and_redlines(text: str) -> tuple[str, int]:
    rows = read_csv(NON_CORE_V56)
    start = text.index("## 其余 38 题逐题保分索引")
    prefix = text[:start]
    body = text[start:]
    replacements = 0
    for row in rows:
        source = row["source_label"]
        qid = row["question_id"]
        pattern = f"### {source}｜"
        pos = body.find(pattern)
        if pos == -1:
            continue
        replacement = f"### {source}（{qid}）｜"
        body = body[:pos] + body[pos:].replace(pattern, replacement, 1)
        replacements += 1

    redlines = {
        "类型：设问或题面需要教师再核对的题。先按最低保分句写；这不是闭合满分题。正式课堂使用前，教师必须回看原卷设问：若问意义，补价值帽；若问原因，按法律依据、材料事实、结果写；若问怎么办，补证据、请求和路径。":
            "类型：设问或题面需要教师再核对的题。先按最低保分句写；这不是闭合满分题。正式课堂使用前，教师必须回看原卷设问：若问意义，补价值帽；若问原因，按法律依据、材料事实、结果写；若问怎么办，补证据、请求和路径。\n\n> 【醒目红线｜SOURCE-CHECK】本卡只保最低分方向，不是闭合满分真题；进 PDF 时必须保留红底/边框/角标。",
        "类型：普通答案练习题。可以考场练笔，但不支撑核心框架；只练思路，不背成正式给分模板。":
            "类型：普通答案练习题。可以考场练笔，但不支撑核心框架；只练思路，不背成正式给分模板。\n\n> 【醒目红线｜REFERENCE-ONLY】只有普通参考答案，不得支撑核心框架节点，不得当正式细则满分题。",
        "类型：综合边界题。只守住《法律与生活》能写的部分；如果原题还要求《政治与法治》《逻辑与思维》等其他模块，必须另开该模块段落，不能把本卡当全题答案。":
            "类型：综合边界题。只守住《法律与生活》能写的部分；如果原题还要求《政治与法治》《逻辑与思维》等其他模块，必须另开该模块段落，不能把本卡当全题答案。\n\n> 【醒目红线｜BOUNDARY】本卡只覆盖《法律与生活》可写层，不覆盖整题全部模块。",
        "类型：转出本书题。这不是本书主观题入口；只在题目明确问法律小问时使用法律材料。":
            "类型：转出本书题。这不是本书主观题入口；只在题目明确问法律小问时使用法律材料。\n\n> 【醒目红线｜TRANSFER】主问不从选必二启动，不能用法律框架硬答。",
    }
    for old, new in redlines.items():
        body = body.replace(old, new)
    return prefix + body, replacements


def patch_cc0245_crossref(text: str) -> str:
    pattern = re.compile(
        r"### 2026 东城 期末 第18题（CC0245_2026_东城_期末_18_2）｜无人机纠纷的维权准备和策略\n\n"
        r".*?(?=\n### 2026 丰台 一模 第20题)",
        re.S,
    )
    replacement = """### 2026 东城 期末 第18题（CC0245_2026_东城_期末_18_2）｜无人机纠纷维权准备交叉引用

类型：交叉引用题。它不是新的独立保分卡，而是核心题 16（CC0244）第（2）问的维权准备部分。

> 【醒目红线｜DUPLICATE-CROSSREF】不要把本卡当作第 28 道核心题，也不要重复背两套答案。完整合同责任、侵权责任和维权准备，统一看核心题 16。

最低可写三句：

1. 维权准备先收集并固定证据，包括交易合同、邮件转账记录、无人机故障、受伤事实和经济损失等证据。
2. 再明确请求，区分违约责任与侵权责任，提出退费、医疗费、误工费、损失赔偿等合理诉求。
3. 路径上可以选择调解、仲裁或诉讼；若材料已经协商未果，就不要只写继续协商。

别这样写：不要把它和核心题 16 分成两套模板；不要写上诉、行政诉讼；不要只罗列证据而不写请求。

能不能背：只作为核心题 16 的维权准备补充，不单独计为核心满分样章。
"""
    new_text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("CC0245 cross-reference section was not patched exactly once.")
    return new_text


def write_non_core_v58_csv() -> None:
    rows = read_csv(NON_CORE_V56)
    out = []
    for r in rows:
        guard = ""
        if r["audit_category"] == "source_check_pending":
            guard = "SOURCE-CHECK: only minimum-score direction; not closed full-score."
        elif r["audit_category"] == "reference_only_locked":
            guard = "REFERENCE-ONLY: ordinary answer only; not formal rubric support."
        elif r["audit_category"] == "boundary_open_container":
            guard = "BOUNDARY: only the Legal and Life layer; other modules separate."
        elif r["audit_category"] == "excluded_logic_boundary":
            guard = "TRANSFER: main task belongs outside Legal and Life."
        elif r["audit_category"] == "low_frequency_container":
            guard = "LOW-FREQUENCY: trainable but not high-frequency trunk."
        duplicate = "crossref_to_core_CC0244" if r["question_id"] == "CC0245_2026_东城_期末_18_2" else ""
        nr = dict(r)
        nr["title_with_id"] = f"{r['source_label']}（{r['question_id']}）"
        nr["visual_guard"] = guard
        nr["duplicate_or_crossref"] = duplicate
        out.append(nr)
    fields = list(rows[0].keys()) + ["title_with_id", "visual_guard", "duplicate_or_crossref"]
    write_csv(NON_CORE_V58, out, fields)


def write_runs_v58_csv() -> None:
    rows = read_csv(RUNS_V55)
    out = []
    for r in rows:
        nr = dict(r)
        try:
            idx = int(r.get("display_index") or "0")
        except ValueError:
            idx = 0
        if idx in ENTRY_BY_CORE_INDEX:
            primary, secondary = ENTRY_BY_CORE_INDEX[idx]
            nr["framework_entry_nodes"] = entry_text(primary, secondary).removeprefix("入口：")
        if r["question_id"] == "CC0025_2024_朝阳_二模_17":
            extra = "该裁决符合民法公平、诚信等基本原则，践行社会主义核心价值观。"
            for field in ["complete_answer_generated", "clean_exam_answer"]:
                if extra not in nr[field]:
                    nr[field] = nr[field].replace("也有利于引导平台企业规范用工", f"{extra}也有利于引导平台企业规范用工")
            if extra not in nr["full_score_sentence_bank"]:
                nr["full_score_sentence_bank"] += " | " + extra
            if "公平诚信原则" not in nr["must_have_keywords"]:
                nr["must_have_keywords"] += "、公平诚信原则、社会主义核心价值观"
            if "道德意义" not in nr["student_score_checklist_v5_5"]:
                nr["student_score_checklist_v5_5"] += " | 意义补道德意义"
        out.append(nr)
    write_csv(RUNS_V58, out, list(rows[0].keys()))


def write_delta_ledger() -> None:
    old_rows = {r["question_id"]: r for r in read_csv(OLD70)}
    current_rows = {r["question_id"]: r for r in read_csv(CURRENT65)}
    boundary = {}
    if BOUNDARY_LEDGER.exists():
        for r in read_csv(BOUNDARY_LEDGER):
            boundary[r.get("source_question_id") or r.get("case_id") or r.get("question_id", "")] = r
    rows = []
    for qid in sorted(set(old_rows) - set(current_rows)):
        src = old_rows[qid]
        b = boundary.get(qid, {})
        rows.append({
            "question_id": qid,
            "old70_status": "present",
            "current65_status": "absent",
            "year": src.get("year", ""),
            "district": src.get("district", ""),
            "exam_stage": src.get("exam_stage", ""),
            "question_no": src.get("question_no", ""),
            "evidence_level": src.get("evidence_level", ""),
            "delta_type": b.get("final_count_bucket") or b.get("action_bucket") or "removed_or_replaced_after_source_audit",
            "replacement_or_tracking_id": b.get("canonical_output_question_id") or b.get("new_question_id") or "",
            "reason": b.get("reason") or "Removed/replaced during suite-exhaustive + ClaudeCode/Cowork correction; see current 65 corpus.",
        })
    for qid in sorted(set(current_rows) - set(old_rows)):
        src = current_rows[qid]
        rows.append({
            "question_id": qid,
            "old70_status": "absent",
            "current65_status": "present",
            "year": src.get("year", ""),
            "district": src.get("district", ""),
            "exam_stage": src.get("exam_stage", ""),
            "question_no": src.get("question_no", ""),
            "evidence_level": src.get("evidence_level", ""),
            "delta_type": "added_recovered_split_or_stage_corrected",
            "replacement_or_tracking_id": "",
            "reason": src.get("notes", "")[:240],
        })
    write_csv(
        DELTA_CSV,
        rows,
        [
            "question_id",
            "old70_status",
            "current65_status",
            "year",
            "district",
            "exam_stage",
            "question_no",
            "evidence_level",
            "delta_type",
            "replacement_or_tracking_id",
            "reason",
        ],
    )
    removed = [r for r in rows if r["current65_status"] == "absent"]
    added = [r for r in rows if r["old70_status"] == "absent"]
    DELTA_MD.write_text(
        f"""# 70 候选到当前 65 工作集去向说明

生成时间：{STAMP}

## 结论

`70 -> 65` 不是简单删掉 5 道题，而是旧 70 候选包经过套卷穷尽、ClaudeCode/Cowork 复核、父题拆分、阶段纠错、非法律题剔除和新题恢复后的重建结果。

- 旧 70 包中不再出现在当前 65 工作集的 ID：{len(removed)} 个。
- 当前 65 工作集中新增/恢复/拆分/阶段纠错后的 ID：{len(added)} 个。
- 净变化：{len(added) - len(removed)}，因此当前工作集为 65。
- 当前成稿仍按 `61 formal + 4 reference_only + 0 missing` 作为证据底座；24 道 source-check 不升核心。

## 明细文件

- `{DELTA_CSV}`

## 使用限制

这份台账只解释题号工作集变化，不把任何 removed/pending 项恢复为核心满分题。若要恢复，必须回源重抽题面和正式细则。
""",
        encoding="utf-8",
    )


def main() -> None:
    text = SRC_MD.read_text(encoding="utf-8")
    text = text.replace("# 选必二法律主观题满分训练宝典 V5.7", "# 选必二法律主观题满分训练宝典 V5.8 候选版")
    text = text.replace("生成时间：2026-05-21 03:43:00", f"生成时间：{STAMP}")
    marker = "## 这版到底是什么\n\n"
    insert = (
        "> 状态：V5.8 candidate_pending_gptpro_capture。已吸收 Claude Opus V5.7 终审的 P1/P2 修补意见；"
        "仍等待 GPTPro V5.7 自然完成并交叉裁决后，才允许进入正式 Word/PDF。\n\n"
        "> 封面口径：27 道核心满分训练 + 38 题保分/边界/回源索引。不是 65 题全部核心满分闭环。\n\n"
    )
    text = text.replace(marker, marker + insert, 1)
    text = patch_core_entries(text)
    text = patch_cc0025(text)
    text, heading_count = patch_non_core_headings_and_redlines(text)
    text = patch_cc0245_crossref(text)
    text += f"""

---

## 附录：70 候选到当前 65 工作集的去向

本版新增台账：`04_merge_audit/candidate70_to_current65_delta_ledger_{TODAY}.csv`。

结论先写给学生和老师看：当前训练稿只使用当前 65 工作集；旧 70 候选包中的多余项，主要是非法律题、父题、待拆分题、阶段错标或待回源项，不作为本书核心满分题。若以后恢复，必须重新锁定题面和正式细则。
"""
    OUT_MD.write_text(text, encoding="utf-8")
    write_non_core_v58_csv()
    write_runs_v58_csv()
    write_delta_ledger()
    PATCH_REPORT.write_text(
        f"""# V5.8 Claude Guarded Patch Report

生成时间：{STAMP}

## 输入

- Claude Opus V5.7 终审：`06_open_observations/claude_opus_v5_7_review_20260521.md`
- V5.7 学生稿：`{SRC_MD}`

## 已修补

1. 27 道核心题入口全部改为 `主卡 + 最多 1 张辅卡`，修复 Claude/GPTPro 均指出的 P1 入口过宽问题。
2. CC0025 平台用工题补入道德意义：公平、诚信等民法基本原则和社会主义核心价值观。
3. 38 道非核心标题补入 question_id，方便和证据底座、覆盖矩阵对账。
4. source-check / reference-only / boundary / transfer 非核心卡加入醒目红线文案，供 PDF 视觉标记沿用。
5. CC0245 无人机维权准备改为核心题 16 的交叉引用，不再作为独立新核心样章。
6. 生成 70 候选到当前 65 工作集的差额台账，回应 Claude P2-5。

## 输出

- 学生稿候选：`{OUT_MD}`
- 非核心护栏 CSV：`{NON_CORE_V58}`
- 27 核心逐题运行 CSV：`{RUNS_V58}`
- 70->65 去向 CSV：`{DELTA_CSV}`
- 70->65 去向说明：`{DELTA_MD}`

## 当前裁定

V5.8 是本地候选补丁，状态为 `candidate_pending_gptpro_capture`。GPTPro V5.7 输出尚未捕获和交叉验证，故不得进入最终 Word/PDF 定稿。

## 计数

- 非核心标题补 ID：{heading_count} 个。
- 核心入口修补：{len(ENTRY_BY_CORE_INDEX)} 个。
""",
        encoding="utf-8",
    )
    print(OUT_MD)
    print(PATCH_REPORT)
    print(DELTA_CSV)


if __name__ == "__main__":
    main()
