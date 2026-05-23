from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path.cwd()
RUN = ROOT / "reports" / "bixiu4_philosophy_strict_v8_2026-05-23"

ROSTER = ROOT / "artifacts" / "desktop_exports_2026-04-29" / "4.29凌晨跑完的结果v6" / "04_过程日志" / "SUITE_ROSTER.csv"
V6_MD = ROOT / "artifacts" / "desktop_exports_2026-04-29" / "4.29凌晨跑完的结果v6" / "01_学生版Word" / "必修四哲学材料-知识触发框架_v6.md"
V7_MD = ROOT / "artifacts" / "desktop_exports_2026-05-23" / "5.23哲学宝典漏题排查与二模补丁v7" / "01_学生版Word" / "必修四哲学材料-知识触发框架_v7_纯学生版.md"
V7_SUITE = ROOT / "artifacts" / "desktop_exports_2026-05-23" / "5.23哲学宝典漏题排查与二模补丁v7" / "03_结构化CSV" / "suite_coverage_audit_v7.csv"
OLD_SUBJECT = ROOT / "artifacts" / "desktop_exports_2026-05-23" / "5.23哲学宝典漏题排查与二模补丁v7" / "03_结构化CSV" / "old_missing_subjective_rows_v7.csv"
OLD_CHOICE = ROOT / "artifacts" / "desktop_exports_2026-05-23" / "5.23哲学宝典漏题排查与二模补丁v7" / "03_结构化CSV" / "old_missing_choice_rows_v7.csv"
SECOND_A = ROOT / "artifacts" / "desktop_exports_2026-05-23" / "5.23哲学宝典漏题排查与二模补丁v7" / "03_结构化CSV" / "second_mock_philosophy_entries_v7.csv"
SECOND_C = ROOT / "artifacts" / "desktop_exports_2026-05-23" / "5.23哲学宝典漏题排查与二模补丁v7" / "03_结构化CSV" / "second_mock_choice_candidates_v7.csv"

FORBIDDEN_STUDENT_TOKENS = [
    "补漏",
    "补入",
    "补丁",
    "审计",
    "证据",
    "CSV",
    "评标",
    "评分细则",
    "阅卷细则",
    "阅卷总结",
    "讲评",
    "参考答案",
    "可从",
    "给分点",
    "pdf",
    "docx",
    "pptx",
    "OCR",
]

TEMPLATE_LANDING = "答题时先点出"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def qnorm(text: str) -> str:
    m = re.search(r"第\s*（?(\d+)）?\s*题", text)
    if m:
        return m.group(1)
    m = re.search(r"(\d+)", text)
    return m.group(1) if m else ""


def source_index(markdown: str, roster: list[dict[str, str]]) -> tuple[Counter[str], set[tuple[str, str]]]:
    suite_counts: Counter[str] = Counter()
    keys: set[tuple[str, str]] = set()
    for line in markdown.splitlines():
        if not line.startswith("**来源题目**"):
            continue
        source = line.split("：", 1)[-1].strip()
        q = qnorm(source)
        for row in roster:
            suite = row["suite_name"]
            if suite and suite in source:
                suite_counts[suite] += 1
                keys.add((suite, q))
                break
    return suite_counts, keys


def token_counts(text: str) -> Counter[str]:
    return Counter({token: text.count(token) for token in FORBIDDEN_STUDENT_TOKENS if text.count(token)})


def sample_lines(text: str, token: str, limit: int = 5) -> list[str]:
    out: list[str] = []
    for idx, line in enumerate(text.splitlines(), 1):
        if token in line:
            out.append(f"{idx}: {line[:180]}")
            if len(out) >= limit:
                break
    return out


def main() -> None:
    RUN.mkdir(parents=True, exist_ok=True)
    roster = read_csv(ROSTER)
    v7_suite = read_csv(V7_SUITE)
    old_subject = read_csv(OLD_SUBJECT)
    old_choice = read_csv(OLD_CHOICE)
    second_a = read_csv(SECOND_A)
    second_c = read_csv(SECOND_C)
    v6_text = V6_MD.read_text(encoding="utf-8", errors="replace")
    v7_text = V7_MD.read_text(encoding="utf-8", errors="replace")

    v6_suite_counts, v6_keys = source_index(v6_text, roster)
    v7_suite_counts, v7_keys = source_index(v7_text, roster)

    old_subject_remaining: list[dict[str, object]] = []
    old_subject_present_but_invalid: list[dict[str, object]] = []
    for row in old_subject:
        suite = row["suite_name"]
        q = row["question_no_norm"] or qnorm(row.get("question", ""))
        out = dict(row)
        out["present_by_suite_question_in_v7"] = (suite, q) in v7_keys
        out["quality_gate"] = "FAIL_NEEDS_FULL_PROMPT_AND_CONCRETE_LANDING"
        if (suite, q) in v7_keys:
            old_subject_present_but_invalid.append(out)
        else:
            old_subject_remaining.append(out)

    old_choice_remaining: list[dict[str, object]] = []
    for row in old_choice:
        suite = row["suite_name"]
        q = row["question_no_norm"] or qnorm(row.get("question", ""))
        out = dict(row)
        out["present_by_suite_question_in_v7"] = (suite, q) in v7_keys
        out["quality_gate"] = "FAIL_NEEDS_CHOICE_CHAIN_AND_WRONG_OPTION_TYPES"
        if (suite, q) not in v7_keys:
            old_choice_remaining.append(out)

    suite_rows: list[dict[str, object]] = []
    old_v7_by_suite = {row["suite_name"]: row for row in v7_suite}
    subj_by_suite = Counter(row["suite_name"] for row in old_subject)
    subj_remaining_by_suite = Counter(row["suite_name"] for row in old_subject_remaining)
    choice_by_suite = Counter(row["suite_name"] for row in old_choice)
    choice_remaining_by_suite = Counter(row["suite_name"] for row in old_choice_remaining)
    for row in roster:
        suite = row["suite_name"]
        old = old_v7_by_suite.get(suite, {})
        suite_rows.append(
            {
                "suite_id": row["suite_id"],
                "suite_name": suite,
                "priority_bucket": row["priority_bucket"],
                "v6_source_lines": v6_suite_counts[suite],
                "v7_source_lines": v7_suite_counts[suite],
                "present_in_v6_student_md": v6_suite_counts[suite] > 0,
                "present_in_v7_student_md": v7_suite_counts[suite] > 0,
                "old_v3_missing_subjective_rows_A_B": old.get("old_v3_missing_subjective_rows_A_B", subj_by_suite[suite]),
                "remaining_subjective_presence_gap_after_v7": subj_remaining_by_suite[suite],
                "subjective_quality_gate": "FAIL" if subj_by_suite[suite] else "NO_ADDED_SUBJECTIVE_GAP",
                "old_v3_missing_choice_rows_C": old.get("old_v3_missing_choice_rows_C", choice_by_suite[suite]),
                "remaining_choice_presence_gap_after_v7": choice_remaining_by_suite[suite],
                "choice_quality_gate": "FAIL" if choice_by_suite[suite] else "NO_ADDED_CHOICE_GAP",
                "v7_audit_status": old.get("audit_status", ""),
            }
        )

    status_counts = Counter(row["v7_audit_status"] for row in suite_rows)
    forbidden = token_counts(v7_text)
    patch_start = v7_text.find("# 2026-05-23 漏题与二模补丁 v7")
    patch_text = v7_text[patch_start:] if patch_start >= 0 else ""
    patch_source_count = patch_text.count("**来源题目**")
    patch_prompt_count = patch_text.count("**完整设问**")
    template_count = patch_text.count(TEMPLATE_LANDING)

    write_csv(
        RUN / "v8_rework_control_matrix.csv",
        suite_rows,
        [
            "suite_id",
            "suite_name",
            "priority_bucket",
            "v6_source_lines",
            "v7_source_lines",
            "present_in_v6_student_md",
            "present_in_v7_student_md",
            "old_v3_missing_subjective_rows_A_B",
            "remaining_subjective_presence_gap_after_v7",
            "subjective_quality_gate",
            "old_v3_missing_choice_rows_C",
            "remaining_choice_presence_gap_after_v7",
            "choice_quality_gate",
            "v7_audit_status",
        ],
    )
    write_csv(
        RUN / "old_subjective_rows_present_but_quality_failed_v8.csv",
        old_subject_present_but_invalid,
        list(old_subject_present_but_invalid[0].keys()) if old_subject_present_but_invalid else ["empty"],
    )
    write_csv(
        RUN / "remaining_old_subjective_presence_gaps_after_v7.csv",
        old_subject_remaining,
        list(old_subject_remaining[0].keys()) if old_subject_remaining else ["empty"],
    )
    write_csv(
        RUN / "remaining_old_choice_presence_gaps_after_v7.csv",
        old_choice_remaining,
        list(old_choice_remaining[0].keys()) if old_choice_remaining else ["empty"],
    )

    never_in_v7 = [row for row in suite_rows if not row["present_in_v7_student_md"]]
    report = [
        "# 必修四哲学宝典 v8 严格返工闸门报告",
        "",
        f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 结论",
        "",
        "**v7 判定：FAIL，不能作为学生版终稿。**",
        "",
        "它可以保留为覆盖审计和补丁证据，但不能直接改名交付。三个独立 Codex 审计线程和 ClaudeCode 审计一致指出：v7 新增内容没有并入原理框架、缺完整设问、答案落点大量为模板空话，且选择题旧漏项未闭环。",
        "",
        "## 核心数字",
        "",
        f"- 旧 roster：{len(roster)} 套。",
        f"- 旧 v6 学生版出现来源题目的套卷：{sum(1 for r in roster if v6_suite_counts[r['suite_name']] > 0)} / {len(roster)}。",
        f"- v7 学生版出现来源题目的旧套卷：{sum(1 for r in roster if v7_suite_counts[r['suite_name']] > 0)} / {len(roster)}。",
        f"- v7 后仍完全没有来源题目行的旧套卷：{len(never_in_v7)} 套。",
        f"- v7 补丁区来源题目：{patch_source_count} 条；完整设问：{patch_prompt_count} 条。",
        f"- v7 补丁区模板答案落点 `{TEMPLATE_LANDING}`：{template_count} 次。",
        f"- 旧 56 套 A/B 主观漏项：{len(old_subject)} 条；其中 v7 只做到来源行出现但质量失败：{len(old_subject_present_but_invalid)} 条；仍无同套同题来源行：{len(old_subject_remaining)} 条。",
        f"- 旧 56 套 C 级选择题漏项：{len(old_choice)} 条；v7 后仍未以同套同题来源行出现：{len(old_choice_remaining)} 条。",
        f"- 2026 二模 A 类主观/综合哲学条目：{len(second_a)} 条；二模 C 类选择题候选：{len(second_c)} 条。",
        "",
        "## v7 后仍完全未进入学生版的旧套卷",
        "",
    ]
    for row in never_in_v7:
        report.append(
            f"- {row['suite_name']}：旧主观漏项 {row['old_v3_missing_subjective_rows_A_B']}，旧选择题漏项 {row['old_v3_missing_choice_rows_C']}。"
        )
    report.extend(
        [
            "",
            "## 学生版禁词命中",
            "",
        ]
    )
    for token, count in forbidden.most_common():
        report.append(f"- `{token}`：{count} 次。")
        for line in sample_lines(v7_text, token, 3):
            report.append(f"  - {line}")

    report.extend(
        [
            "",
            "## 必须返工的验收口径",
            "",
            "1. 学生版正文必须按飞哥原理方法论框架节点重排，不能再保留 `[旧题补漏]`、`[2026二模补入]`、`补丁`、`索引`等过程标题。",
            "2. 每条主观题必须补齐完整设问；没有完整设问的条目只能留在审计版，不得进学生版正文。",
            "3. `答案落点` 必须改成本题可直接使用的答案句，不能写“先点出原理、再扣材料、最后回设问”这种操作说明。",
            "4. 选择题必须单独成册或散入选择题专册；每题要有完整题干、正确项链、错肢错误类型，不能只列“触发知识/证据要点”。",
            "5. 朝阳二模21、房山二模21、顺义二模21必须标为“综合题中的哲学维度”，房山21降为弱补入，不得与普通哲学主观题等价。",
            "6. B 类二模候选必须在审计版挂账，不能在学生版默默消失，也不能凭方向词进正文。",
            "7. 最终签字前必须更新控制矩阵、Governor/Confucius 报告、Word 文件，并完成 Word 结构或视觉核验。",
            "",
            "## 输出文件",
            "",
            "- `v8_rework_control_matrix.csv`：v7 后验套卷矩阵。",
            "- `old_subjective_rows_present_but_quality_failed_v8.csv`：已出现但质量失败的旧主观补漏。",
            "- `remaining_old_subjective_presence_gaps_after_v7.csv`：v7 后仍未出现的旧主观漏项。",
            "- `remaining_old_choice_presence_gaps_after_v7.csv`：v7 后仍未出现的旧选择题漏项。",
        ]
    )
    write_text(RUN / "STRICT_GATE_REPORT.md", "\n".join(report) + "\n")


if __name__ == "__main__":
    main()
