from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
BUNDLE = (
    Path.home()
    / "Desktop"
    / "beijing_politics_research"
    / "data"
    / "preprocessed_corpus"
    / "gpt_suite_bundles"
    / "2025各区模拟题__2025各区一模__2025石景山一模.md"
)
DOCX_CONTEXT = RECOVERY / "CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md"
REPORT = RECOVERY / "SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
MANIFEST = RECOVERY / "SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = MATRIX.with_name(
        f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_2025_shijingshan_yimo_candidate_repair_{timestamp}.csv"
    )
    shutil.copy2(MATRIX, backup)

    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    changed = 0
    touched_ids: list[str] = []

    def update(row: dict[str, str], **values: str) -> None:
        nonlocal changed
        local = False
        for key, value in values.items():
            if row.get(key, "") != value:
                row[key] = value
                local = True
        if local:
            changed += 1
            touched_ids.append(row.get("matrix_row_id", ""))

    source = "data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025石景山一模.md:"
    q16_support = (
        "2025石景山一模Q16正式非选择题评分细则明确：可选用联系观、发展观、矛盾观等相关哲理，"
        "解析“不数既往，不能知将来；不求远因，不能明近果”，并阐明中华优秀传统文化的特点和当代价值。"
    )
    q21_support = (
        "2025石景山一模Q21正式评分细则要求综合运用改革的实质、全面深化改革总目标和原则、党的领导、"
        "坚持中国特色社会主义、社会发展普遍规律等模块，阐述统筹破立关系对现代化强国建设的意义。"
    )

    choice_in_docx = {
        "Q3": {
            "node": "选择题链条：实践检验/主客观相符合/法宝话语辨析",
            "support": "教师版答案键Q3=A；当前DOCX已有“法宝”选择题链条，作为选择题正确项/错误项辨析，不冒充主观题评分细则。",
            "artifact": source + "466-470; CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md",
        },
        "Q4": {
            "node": "选择题链条：一切从实际出发/适度原则/政策弹性",
            "support": "教师版答案键Q4=D；当前DOCX已有“自愿/自主/允许”选择题链条，作为选择题正确项/错误项辨析，不冒充主观题评分细则。",
            "artifact": source + "466-470; CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md",
        },
    }

    choice_non_body = {f"Q{i}" for i in range(1, 16)} - set(choice_in_docx)

    for row in rows:
        if row.get("题源") != "2025石景山一模":
            continue
        row_id = row.get("matrix_row_id", "")
        q = row.get("题号", "")

        if q in choice_in_docx:
            item = choice_in_docx[q]
            update(
                row,
                **{
                    "是否进宝典": "是：当前DOCX已有选择题链条覆盖",
                    "宝典节点": item["node"],
                    "细则支持原理": item["support"],
                    "证据等级": "选择题官方答案键+题干正确项；选择题边界已明示",
                    "是否误放": "否",
                    "是否需补厚": "否",
                    "当前处理": "COVERED_BY_CURRENT_DOCX_CHOICE_CHAIN_SHIJINGSHAN_2025",
                    "备注": "选择题只作为正确项/错误项辨析链条；不作为主观题评分细则证据。",
                    "source_artifact": item["artifact"],
                },
            )
        elif q in choice_non_body:
            update(
                row,
                **{
                    "是否进宝典": "否：选择题候选词命中，非当前DOCX正文",
                    "宝典节点": "选择题客观题边界",
                    "细则支持原理": "教师版答案键Q1-Q15仅支持客观题正误判定；本行是早期术语命中，不是主观题评分细则落点。",
                    "证据等级": "官方答案键+题面；非主观题评分细则",
                    "是否误放": "否：未进正文",
                    "是否需补厚": "否",
                    "当前处理": "CHOICE_TERM_CANDIDATE_REVIEWED_NON_BODY_SHIJINGSHAN_2025",
                    "备注": "按选择题边界裁决；未在当前DOCX作为独立条目保留。",
                    "source_artifact": source + "466-470",
                },
            )
        elif q.startswith("Q16") or row_id in {"M0092", "M0093", "M0094", "M0182", "M0212", "M0462"}:
            update(
                row,
                **{
                    "是否进宝典": "是：当前DOCX已有Q16覆盖",
                    "宝典节点": "联系观/发展观/矛盾观/中华优秀传统文化特点及当代价值",
                    "细则支持原理": q16_support,
                    "证据等级": "正式评分细则",
                    "是否误放": "否",
                    "是否需补厚": "否",
                    "当前处理": "COVERED_BY_CURRENT_DOCX_SHIJINGSHAN_2025_Q16",
                    "备注": "纠正旧节点：Q16正式细则支持联系观、发展观、矛盾观及文化价值，不支持将其落为“尊重客观规律与发挥主观能动性相结合”的独立节点。",
                    "source_artifact": source + "22-31; CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md",
                },
            )
        elif q == "Q17":
            update(
                row,
                **{
                    "是否进宝典": "否：政治与法治/当代国际政治经济边界",
                    "宝典节点": "-",
                    "细则支持原理": "Q17(1)为接诉即办与大城善治，Q17(2)为完善全球治理的中国主张；不作为必修四哲学与文化正文条目。",
                    "证据等级": "正式评分细则+题干模块边界",
                    "是否误放": "否：未进正文",
                    "是否需补厚": "否",
                    "当前处理": "MODULE_BOUNDARY_EXCLUDED_SHIJINGSHAN_2025_Q17_POLITICS_IR",
                    "备注": "跨模块候选词命中已按题干模块排除。",
                    "source_artifact": source + "34-61",
                },
            )
        elif q == "Q18":
            update(
                row,
                **{
                    "是否进宝典": "否：经济与社会/低空经济边界",
                    "宝典节点": "-",
                    "细则支持原理": "Q18要求运用《经济与社会》知识概括低空经济优势并提出发展方案；不作为必修四正文条目。",
                    "证据等级": "正式评分细则+题干模块边界",
                    "是否误放": "否：当前DOCX无低空经济正文命中",
                    "是否需补厚": "否",
                    "当前处理": "MODULE_BOUNDARY_EXCLUDED_SHIJINGSHAN_2025_Q18_ECONOMICS",
                    "备注": "当前DOCX复查低空经济命中为0。",
                    "source_artifact": source + "70-82; CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md",
                },
            )
        elif q == "Q19" or row_id in {"M0183", "M0213"}:
            update(
                row,
                **{
                    "题号": "Q19",
                    "是否进宝典": "否：选必三《逻辑与思维》边界",
                    "宝典节点": "-",
                    "细则支持原理": "Q19细则明确从科学思维特征、归纳推理、创新思维方法等角度分析获奖建议，属选必三边界。",
                    "证据等级": "正式评分细则+题干模块边界",
                    "是否误放": "否：当前DOCX无科学建议奖正文命中",
                    "是否需补厚": "否",
                    "当前处理": "MODULE_BOUNDARY_EXCLUDED_SHIJINGSHAN_2025_Q19_LOGIC",
                    "备注": "纠正旧题号：原Q21(1)科学思维记录实际对应本套Q19。",
                    "source_artifact": source + "87-99; CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md",
                },
            )
        elif q == "Q20":
            update(
                row,
                **{
                    "是否进宝典": "否：法律与生活/司法护航边界",
                    "宝典节点": "-",
                    "细则支持原理": "Q20围绕民法典违约责任、反不正当竞争法及司法护航新质生产力，属法律模块。",
                    "证据等级": "正式评分细则+题干模块边界",
                    "是否误放": "否：未进正文",
                    "是否需补厚": "否",
                    "当前处理": "MODULE_BOUNDARY_EXCLUDED_SHIJINGSHAN_2025_Q20_LAW",
                    "备注": "候选词命中来自法律题细则，已按模块边界排除。",
                    "source_artifact": source + "104-118",
                },
            )
        elif q == "Q21":
            update(
                row,
                **{
                    "是否进宝典": "是：当前DOCX已有Q21必修四相关覆盖",
                    "宝典节点": "改革的实质/社会发展普遍规律/生产关系与生产力/上层建筑与经济基础",
                    "细则支持原理": q21_support,
                    "证据等级": "正式评分细则",
                    "是否误放": "否",
                    "是否需补厚": "否",
                    "当前处理": "COVERED_BY_CURRENT_DOCX_SHIJINGSHAN_2025_Q21_BIXIU4_RELEVANT_POINTS",
                    "备注": "当前DOCX保留两条Q21相关落点；只保留必修四相关社会发展规律/改革意义，不把党的领导等跨模块点扩写为哲学节点。",
                    "source_artifact": source + "121-130; CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md",
                },
            )
        elif q == "Qunknown":
            update(
                row,
                **{
                    "是否进宝典": "否：教师版全文索引行，已拆入逐题裁决",
                    "宝典节点": "SOURCE_INDEX_ONLY",
                    "细则支持原理": "本行是教师版全文片段索引，不是独立题号；2025石景山一模已按Q1-Q21逐题裁决。",
                    "证据等级": "来源索引+逐题裁决已完成",
                    "是否误放": "不适用",
                    "是否需补厚": "否",
                    "当前处理": "SOURCE_INDEX_SUPERSEDED_BY_ROW_REVIEW_SHIJINGSHAN_2025",
                    "备注": "不再作为独立候选风险行。",
                    "source_artifact": source + "150-530",
                },
            )
        elif q == "SUITE_LEVEL":
            update(
                row,
                **{
                    "是否进宝典": "套卷级索引：已拆为逐题处置",
                    "宝典节点": "SUITE_LEVEL_SUMMARY",
                    "细则支持原理": "2025石景山一模已按Q1-Q21逐题裁决；套卷级行只作索引，不能替代逐题证据。",
                    "证据等级": "套卷索引+逐题裁决已完成",
                    "是否误放": "不适用",
                    "是否需补厚": "否",
                    "当前处理": "SUITE_LEVEL_INDEX_SUPERSEDED_BY_ROW_REVIEW_SHIJINGSHAN_2025",
                    "备注": "风险队列中的套卷级补厚标记已由逐题回源处置替代。",
                    "source_artifact": source + "7-130; 466-530",
                },
            )

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    remaining = []
    for row in rows:
        if row.get("题源") != "2025石景山一模":
            continue
        if any(
            token in " ".join(row.values())
            for token in ["待核", "需逐题", "term_hit_needs_review", "needs_review", "疑似遗漏"]
        ):
            remaining.append(
                {
                    "matrix_row_id": row.get("matrix_row_id", ""),
                    "题号": row.get("题号", ""),
                    "当前处理": row.get("当前处理", ""),
                    "是否进宝典": row.get("是否进宝典", ""),
                }
            )

    manifest = {
        "status": "SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIRED",
        "timestamp": timestamp,
        "matrix_backup": str(backup),
        "rows_changed": changed,
        "touched_ids": touched_ids,
        "remaining_local_open_wording": remaining,
        "bundle": str(BUNDLE),
        "docx_context": str(DOCX_CONTEXT),
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 2025石景山一模候选队列修复记录",
        "",
        "- Status: `SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIRED`.",
        f"- Matrix backup before rewrite: `{backup}`.",
        f"- Source bundle: `{BUNDLE}`.",
        f"- Current DOCX context: `{DOCX_CONTEXT}`.",
        f"- Rows changed: `{changed}`.",
        "",
        "## Current DOCX Finding",
        "",
        "- Current DOCX contains 7 suite heading blocks: Q16 x3, Q21 x2, choice Q3 x1, choice Q4 x1.",
        "- Current DOCX has no low-altitude-economy Q18 hit, no scientific-suggestion Q19 hit, and no legal Q20 body hit.",
        "- No DOCX deletion was required for this suite.",
        "",
        "## Row-Level Adjudication",
        "",
        "- Q1-Q2/Q5-Q15: closed as choice-question candidate or module boundary unless already present in DOCX.",
        "- Q3/Q4: retained as current-DOCX choice-question chains with official answer-key boundary, not as main-question scoring evidence.",
        "- Q16: retained as current-DOCX formal-rubric coverage. The old independent node “尊重客观规律与发挥主观能动性相结合” was corrected because the formal scoring rules support 联系观、发展观、矛盾观 and culture value, not that standalone node.",
        "- Q17: excluded as 政治与法治 / 当代国际政治经济 boundary.",
        "- Q18: excluded as 经济与社会 low-altitude-economy boundary.",
        "- Q19: excluded as 选必三《逻辑与思维》 boundary; old Q21(1) scientific-thinking rows were corrected to Q19.",
        "- Q20: excluded as 法律与生活 boundary.",
        "- Q21: retained only for Bixiu4-relevant reform/social-development-law points already present in current DOCX.",
        "",
        "## Remaining Boundaries",
        "",
        "- This is local source/matrix/DOCX-context repair only; it is not GPTPro or Claude Opus web acceptance.",
        "- GPTPro web external review remains `real_call_pending`.",
        "- Claude Opus web/app external review remains `real_call_pending`; direct `https://claude.ai` auto-login is the required route.",
        "- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
        "- ORDER_063 GitHub upload remains deferred; no push was attempted.",
    ]
    if remaining:
        lines.extend(["", "## Remaining Local Open Wording", ""])
        for item in remaining:
            lines.append(f"- `{item['matrix_row_id']}` `{item['题号']}` `{item['当前处理']}` `{item['是否进宝典']}`")
    else:
        lines.extend(["", "## Remaining Local Open Wording", "", "- `0`."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
