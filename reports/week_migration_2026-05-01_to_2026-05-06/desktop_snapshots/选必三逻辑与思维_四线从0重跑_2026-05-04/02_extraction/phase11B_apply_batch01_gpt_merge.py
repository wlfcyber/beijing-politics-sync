#!/usr/bin/env python3
"""Apply the GPT-approved Phase11B Batch01 merge boundary.

This produces review-only artifacts. It does not generate Word/PDF/final output.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STUDENT_DIR = ROOT / "09_student_draft"
REVIEW_DIR = ROOT / "08_review"
GPT_DIR = REVIEW_DIR / "gpt_phase_advice"

BASE_BODY = STUDENT_DIR / "phase11A_student_body_PATCHED_REVIEW_ONLY.md"
BASE_CONTROL = STUDENT_DIR / "phase10_polish_control_matrix.csv"
BATCH_CANDIDATES = STUDENT_DIR / "phase11B_batch01_P1_candidate_entries.md"
GPT_RAW = GPT_DIR / "phase_11B_batch01_gpt55_raw.md"

OUT_BODY = STUDENT_DIR / "phase11B_batch01_student_body_30_REVIEW_ONLY.md"
OUT_CONTROL = STUDENT_DIR / "phase11B_batch01_merge_control_matrix.csv"
OUT_INDEX = STUDENT_DIR / "phase11B_batch01_index_only_register.md"
OUT_INTERNAL = STUDENT_DIR / "phase11B_batch01_internal_terms_scan.md"
OUT_GATE = REVIEW_DIR / "phase11B_batch01_merge_local_gate.md"
OUT_GPT_DIGEST = GPT_DIR / "phase_11B_batch01_gpt55_digest.md"

INSERT_BEFORE = "### 2024 朝阳一模第9题（选择题）"
BODY_CANDIDATE_TITLE = "2025 东城期末第18题第(2)问（主观题）"

INTERNAL_PATTERNS = [
    "Phase",
    "phase",
    "packet",
    "source locator",
    "lane",
    "Governor",
    "Confucius",
    "L3",
    "L4",
    "B-choice-signal",
    "路径",
    "细则编号",
    "评标",
    "参考答案",
    "可从",
    "PASS",
    "review_only",
]

HARD_EXCLUDED_VISIBLE_HEADINGS = [
    "2024 西城一模第11题",
    "2025 海淀二模第12题",
    "2025 海淀二模第13题",
    "2026 顺义一模第3题",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def extract_candidate(markdown: str) -> str:
    start_token = f"### {BODY_CANDIDATE_TITLE}"
    start = markdown.index(start_token)
    end = markdown.index("\n## 只修索引、不进正文的条目", start)
    return markdown[start:end].strip()


def section_for_title(markdown: str, title: str) -> str:
    pattern = re.compile(r"(?m)^###\s+(.+)$")
    matches = list(pattern.finditer(markdown))
    for idx, match in enumerate(matches):
        found = match.group(1).strip()
        if found == title:
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
            return markdown[match.start() : end]
    return ""


def heading_titles(markdown: str) -> list[str]:
    return re.findall(r"(?m)^###\s+(.+)$", markdown)


def build_body() -> str:
    base = BASE_BODY.read_text(encoding="utf-8")
    candidates = BATCH_CANDIDATES.read_text(encoding="utf-8")
    candidate = extract_candidate(candidates)
    if BODY_CANDIDATE_TITLE in base:
        raise RuntimeError("body candidate already present in base body")
    if INSERT_BEFORE not in base:
        raise RuntimeError(f"insert marker missing: {INSERT_BEFORE}")
    return base.replace(INSERT_BEFORE, candidate + "\n\n" + INSERT_BEFORE)


def build_control() -> list[dict[str, str]]:
    rows = read_csv(BASE_CONTROL)
    new_row = dict.fromkeys(rows[0].keys(), "")
    new_row.update(
        {
            "entry_no": str(len(rows) + 1),
            "question_id": "Q-2025东城期末-18-2",
            "visible_title": BODY_CANDIDATE_TITLE,
            "module": "思维",
            "draft_section": "思维",
            "question_type": "主观题",
            "source_entry_status": "L3_repaired_from_index_cluster",
            "input_permission": "include_as_review_only_body_candidate_after_gpt",
            "primary_mount": "思维",
            "secondary_mount": "",
            "same_type_ids": "Q-2024朝阳一模-7；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9",
            "gpt_named_risk_status": "phase11B_batch01_gpt_merge_allowed_one_body_candidate",
            "student_body_origin": "phase11B_batch01_source_repair",
            "no_expansion_policy": "only_one_body_candidate_two_index_only_no_word_pdf_final",
            "phase10_title_strategy": "student_readable_heading_body_control_matrix_qid_trace",
            "phase10_same_type_style": "readable_titles_in_body_raw_qids_in_matrix",
            "same_type_visible": "2024 朝阳一模第7题；2025 海淀期末第18题；2025 西城二模第16题第(3)问；2026 东城一模第19题第(4)问；2026 朝阳期中第21题第(2)问；2026 通州期末第9题",
            "phase10_scope_lock": "review_only_no_word_pdf_final",
        }
    )
    return rows + [new_row]


def internal_hits(markdown: str) -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []
    for line_no, line in enumerate(markdown.splitlines(), 1):
        for pat in INTERNAL_PATTERNS:
            if pat in line:
                hits.append((pat, line_no, line))
    return hits


def write_gpt_digest(raw: str) -> None:
    digest = [
        "# Phase11B Batch01 GPT-5.5 Pro Digest",
        "",
        "- verdict: `PASS_BATCH01_MERGE_ONE_BODY_CANDIDATE`",
        "- allowed_body_candidate: `Q-2025东城期末-18-2`",
        "- index_only: `Q-2026通州期末-9`; `Q-2024朝阳二模-7`",
        "- must_fix: none blocking",
        "- merge_boundary: add only one body candidate; keep two other rows index-only; no Word/PDF/final PASS",
        "",
        "## Hard Constraints Accepted",
        "",
        "- `Q-2025东城期末-18-2` must not be mounted as 形式推理 / 三段论.",
        "- `Q-2026通州期末-9` must not enter subjective body text.",
        "- `Q-2024朝阳二模-7` must not enter thought-method body text.",
        "",
        f"Raw response: `{GPT_RAW}`",
        "",
    ]
    if "PASS_BATCH01_MERGE_ONE_BODY_CANDIDATE" not in raw:
        digest.append("WARNING: raw GPT text did not contain the expected verdict string.")
    OUT_GPT_DIGEST.write_text("\n".join(digest), encoding="utf-8")


def write_index_register() -> None:
    lines = [
        "# Phase11B Batch01 Index-Only Register",
        "",
        "This file records rows GPT allowed only as index material. They are not full student-body entries.",
        "",
        "## Q-2026通州期末-9",
        "",
        "- index_node: 创新思维选择题陷阱 / 数字化治理材料事实与选必三方法区分索引",
        "- answer: D",
        "- trap_note: 医保 + 商保清分结算中心打通数据壁垒、一站式结算，是材料事实中的系统化、数字化整合；不能把“系统化、数字化整合”直接搬成选必三主观题方法。",
        "- safe_wrong_option_note: B/C 错在选项与材料或知识指向不匹配。",
        "- body_candidate: no",
        "",
        "## Q-2024朝阳二模-7",
        "",
        "- index_node: 推理题型索引 / 三段论谬误 / 项的周延 / 小项扩大易错索引",
        "- answer: D",
        "- trap_note: A 项错误不宜写成中项不周延；问题在小项“娱乐工具”前提中不周延、结论中被扩大，属于小项不当周延 / 小项扩大。",
        "- body_candidate: no",
        "",
        "## Boundary",
        "",
        "- Do not expand either row into full body text before a later source/GPT/Governor gate.",
        "- Do not use this register to generate Word/PDF/final output.",
        "",
    ]
    OUT_INDEX.write_text("\n".join(lines), encoding="utf-8")


def run_gate(markdown: str, control_rows: list[dict[str, str]]) -> None:
    titles = heading_titles(markdown)
    candidate_section = section_for_title(markdown, BODY_CANDIDATE_TITLE)
    hits = internal_hits(markdown)
    hard_heading_hits = [h for h in HARD_EXCLUDED_VISIBLE_HEADINGS if f"### {h}" in markdown]

    checks: list[tuple[str, bool, str]] = []
    checks.append(("row_count_check", len(titles) == 30 and len(control_rows) == 30, f"headings={len(titles)} control_rows={len(control_rows)}"))
    checks.append(("index_only_check_tongzhou9", "### 2026 通州期末第9题" not in markdown, "Q-2026通州期末-9 is not a body heading"))
    checks.append(("index_only_check_chaoyangermo7", "### 2024 朝阳二模第7题" not in markdown, "Q-2024朝阳二模-7 is not a body heading"))
    checks.append(("dongcheng_mount_no_formal_reasoning", "三段论" not in candidate_section and "形式推理" not in candidate_section, "candidate section has no 三段论/形式推理 mount"))

    required_terms = ["联想", "发散", "聚合", "思路新", "方法新", "结果新"]
    required_facts = ["登月任务", "月面环境", "航天员", "登月服"]
    missing_terms = [term for term in required_terms if term not in candidate_section]
    missing_facts = [fact for fact in required_facts if fact not in candidate_section]
    checks.append(("dongcheng_trigger_terms", not missing_terms, "missing_terms=" + "；".join(missing_terms)))
    checks.append(("dongcheng_material_facts", not missing_facts, "missing_facts=" + "；".join(missing_facts)))
    checks.append(("tongzhou9_method_phrase_not_body", "系统化、数字化整合" not in markdown, "method phrase absent from body"))
    chaoyang7_old_label_lines = [
        line
        for line in markdown.splitlines()
        if "朝阳二模第7题" in line and "中项不周延" in line
    ]
    checks.append(
        (
            "chaoyangermo7_old_fallacy_not_body",
            not chaoyang7_old_label_lines,
            "same_line_hits=" + "；".join(chaoyang7_old_label_lines),
        )
    )
    checks.append(("internal_terms_scan", len(hits) == 0, f"hits={len(hits)}"))
    checks.append(("hard_excluded_heading_scan", len(hard_heading_hits) == 0, "heading_hits=" + "；".join(hard_heading_hits)))
    checks.append(("no_word_pdf_final_check", True, "this script writes only review/audit/student-draft markdown/csv artifacts"))

    verdict = "PASS_FOR_REVIEW_ONLY_BATCH01_MERGE" if all(ok for _, ok, _ in checks) else "FAIL_REPAIR_REQUIRED"
    lines = [
        "# Phase11B Batch01 Merge Local Gate",
        "",
        f"Verdict: `{verdict}`",
        "",
        "## Checks",
        "",
    ]
    for name, ok, detail in checks:
        lines.append(f"- {'PASS' if ok else 'FAIL'} `{name}`: {detail}")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This authorizes only a review-only 30-row body candidate set.",
            "- Word/PDF/final PASS remain blocked.",
            "",
        ]
    )
    OUT_GATE.write_text("\n".join(lines), encoding="utf-8")

    OUT_INTERNAL.write_text(
        "\n".join(
            [
                "# Phase11B Batch01 Internal Terms Scan",
                "",
                f"- hits: {len(hits)}",
                "",
                "## Hits",
                "",
                *[f"- `{pat}` line {line_no}: {line}" for pat, line_no, line in hits],
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    raw = GPT_RAW.read_text(encoding="utf-8")
    markdown = build_body()
    control_rows = build_control()

    OUT_BODY.write_text(markdown, encoding="utf-8")
    write_csv(OUT_CONTROL, control_rows, list(control_rows[0].keys()))
    write_index_register()
    write_gpt_digest(raw)
    run_gate(markdown, control_rows)

    print(f"wrote {OUT_BODY}")
    print(f"wrote {OUT_CONTROL}")
    print(f"wrote {OUT_INDEX}")
    print(f"wrote {OUT_GPT_DIGEST}")
    print(f"wrote {OUT_GATE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
