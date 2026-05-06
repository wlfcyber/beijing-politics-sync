#!/usr/bin/env python3
"""Phase11A: content review for the locked 29-row Phase10 student body.

No expansion is performed here. Claude/ClaudeCode lanes are suspended by user
instruction, so this script only performs Codex-local checks and prepares files
for the next GPT review.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BODY = ROOT / "09_student_draft" / "phase10_polished_outline_FROM_29.md"
CONTROL = ROOT / "09_student_draft" / "phase10_polish_control_matrix.csv"
OUT_DIR = ROOT / "09_student_draft"
REVIEW_CSV = OUT_DIR / "phase11_29row_content_review_matrix.csv"
PATCH_PLAN = OUT_DIR / "phase11_29row_patch_plan.md"
QID_LOCK = OUT_DIR / "phase11_QID_lock_recheck.md"
INTERNAL_SCAN = OUT_DIR / "phase11_internal_terms_scan.md"
INDEX_CHECK = OUT_DIR / "phase11_same_type_index_no_expansion_check.md"
PATCHED_BODY = OUT_DIR / "phase11A_student_body_REVIEW_ONLY.md"
PATCHED_BODY_AFTER_GPT = OUT_DIR / "phase11A_student_body_PATCHED_REVIEW_ONLY.md"
VERIFY = ROOT / "08_review" / "phase11A_codex_local_verification.md"
PATCH_RESOLUTION = ROOT / "08_review" / "phase11A_content_patch_resolution.md"
LOCAL_RECHECK = ROOT / "08_review" / "phase11A_codex_local_recheck.md"

THINKING_FIELDS = [
    "材料信号",
    "可写思维/方法",
    "为什么能想到",
    "答题动作",
    "答案落点",
    "易错陷阱",
    "同类题索引",
]
REASONING_FIELDS = [
    "题型",
    "逻辑形式",
    "规则口诀",
    "有效式或错误式",
    "解题动作",
    "答案落点",
    "易错陷阱",
    "同类题索引",
]

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
    "filled",
    "correct_option_chain",
]

HARD_EXCLUDED = [
    "Q-2024西城一模-11",
    "Q-2025海淀二模-12",
    "Q-2025海淀二模-13",
    "Q-2026顺义一模-3",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def split_sections(text: str) -> dict[str, str]:
    pattern = re.compile(r"^### (.+)$", re.M)
    matches = list(pattern.finditer(text))
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[title] = text[start:end]
    return sections


def count_choice_answer(text: str) -> str:
    m = re.search(r"答案落点：[^。\n]*(选\s*[A-D](?:[，。][^。\n]*)?)", text)
    return m.group(1).strip() if m else ""


def visible_without_kind(title: str) -> str:
    return re.sub(r"（(?:选择题|主观题)）", "", title).strip()


def find_title(control_title: str, sections: dict[str, str]) -> tuple[str, str]:
    if control_title in sections:
        return control_title, sections[control_title]
    base = visible_without_kind(control_title)
    for title, body in sections.items():
        if title.startswith(base):
            return title, body
    return "", ""


def row_review(row: dict[str, str], sections: dict[str, str]) -> dict[str, str]:
    qid = row["question_id"]
    title, section = find_title(row["visible_title"], sections)
    module = row["module"]
    qtype = row["question_type"]

    expected = REASONING_FIELDS if module == "推理" else THINKING_FIELDS
    if module == "交叉":
        # Cross rows can be written in thinking or reasoning language, but must
        # visibly preserve primary/secondary mount.
        expected = THINKING_FIELDS if row.get("primary_mount") == "思维" else REASONING_FIELDS

    missing = [field for field in expected if f"- {field}：" not in section]

    choice_style = "not_choice"
    if qtype == "选择题":
        ans = count_choice_answer(section)
        choice_style = "pass" if re.match(r"选\s*[A-D][，。]", ans) else "needs_check"

    subjective_answer = "not_subjective"
    if qtype == "主观题":
        m = re.search(r"- 答案落点：(.+)", section)
        subjective_answer = "pass" if m and len(m.group(1).strip()) >= 18 else "needs_check"

    cross_mount = "not_cross"
    if module == "交叉":
        text = section
        primary = row.get("primary_mount", "")
        secondary = row.get("secondary_mount", "")
        if primary and secondary and primary in text and secondary in text:
            cross_mount = "pass"
        else:
            cross_mount = "needs_check"

    raw_qid = "present" if qid in section else "absent"
    status = "PASS"
    notes: list[str] = []
    if not section:
        status = "FAIL"
        notes.append("visible heading not found")
    if missing:
        status = "REVIEW"
        notes.append("missing fields: " + "；".join(missing))
    if choice_style == "needs_check":
        status = "REVIEW"
        notes.append("choice answer style needs check")
    if subjective_answer == "needs_check":
        status = "REVIEW"
        notes.append("subjective answer landing weak/missing")
    if cross_mount == "needs_check":
        status = "REVIEW"
        notes.append("cross mount not explicit enough")

    return {
        "entry_no": row["entry_no"],
        "question_id": qid,
        "visible_title_control": row["visible_title"],
        "visible_title_found": title,
        "module": module,
        "question_type": qtype,
        "primary_mount": row.get("primary_mount", ""),
        "secondary_mount": row.get("secondary_mount", ""),
        "expected_fields": "；".join(expected),
        "missing_fields": "；".join(missing),
        "choice_style": choice_style,
        "subjective_answer": subjective_answer,
        "cross_mount": cross_mount,
        "raw_qid_in_section": raw_qid,
        "review_status": status,
        "notes": "；".join(notes),
    }


def internal_hits(text: str) -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []
    for i, line in enumerate(text.splitlines(), 1):
        for pat in INTERNAL_PATTERNS:
            if pat in line:
                hits.append((pat, i, line))
    return hits


def apply_review_only_patches(text: str) -> tuple[str, list[str]]:
    patches: list[str] = []
    new = text
    replacements = {
        "沿“杂多现象→抽出核心因果→回到整体规律”路径理解共变法的认识价值。": "沿“杂多现象→抽出核心因果→回到整体规律”链条理解共变法的认识价值。",
        "- 材料信号：从老龄化人口需求出发的产品研发、对老龄化趋势的市场判断、对产品的反复测试与迭代。\n- 答题动作：把客观性、预见性、可检验性逐条对应材料：从老人真实需求出发，体现客观性；研判老龄化趋势和市场潜力，体现预见性；反复测试、多轮迭代，体现可检验性。": "- 材料信号：从老龄化人口需求出发的产品研发、对老龄化趋势的市场判断、对产品的反复测试与迭代。\n- 可写思维/方法：科学思维三特征，具体是客观性、预见性、可检验性。\n- 为什么能想到：材料把研发依据、趋势判断、测试迭代连在一起：真实需求指向客观性，趋势判断指向预见性，测试迭代指向可检验性。\n- 答题动作：把客观性、预见性、可检验性逐条对应材料：从老人真实需求出发，体现客观性；研判老龄化趋势和市场潜力，体现预见性；反复测试、多轮迭代，体现可检验性。",
        "- 易错陷阱：①把“想象”当作思维的基本单元(基本单元是概念，不是想象)；③把本诗当作抽象思维(本诗用形象，不用抽象)。": "- 易错陷阱：①错在把“想象”当作形象思维的基本单元；形象思维依托感性形象，抽象思维的基本单元才是概念。③错在把本诗当作抽象思维；本诗主要通过具体意象展开，不属于抽象思维。",
        "- 答案落点：逐角度一句话作答，每条带“调查内容/调查动作 + 思维方法 + 作用结论”。": "- 答案落点：逐角度一句话作答，每条带“调查内容/调查动作 + 思维方法 + 作用结论”。每个角度至少写一组“材料动作 + 思维方法 + 作用结论”，不要只列方法名。",
        "- 答题动作：调查了解对应感性具体；分析研究对应思维抽象和思维具体；两阶段相互依赖、不可割裂。": "- 答题动作：调查了解对应感性具体；分析研究对应思维抽象和思维具体；两阶段相互依赖、不可割裂。先拿到杂多表象，再抽出本质联系，最后回到完整认识。",
        "- 题型：综合推理题(实践调研 + 矛盾分析 + 推理想象 + 超前思维)。": "- 题型：综合方法链 / 超前思维链(调研实践 + 因果分析 + 矛盾分析 + 推理想象 + 超前思维)。",
        "- 逻辑形式：由实践→因果规律→矛盾分析→由过去现在推未来→超前思维的整链。": "- 逻辑形式：这不是形式逻辑题型正例，而是由实践→因果规律→矛盾分析→由过去现在推未来→超前思维的综合方法链。",
        "- 题型：类比推理 + 联言判断作辅助；本题要求填动态性 + 类比推理。": "- 题型：填空组合题，第一空考辩证思维动态性，第二空考类比推理。联言判断留到第(2)问，不在第(1)问题型名中出现。",
    }
    for old, repl in replacements.items():
        if old in new:
            new = new.replace(old, repl)
            if old.startswith("沿"):
                patches.append("Replace student-facing `路径` with `链条` in Q-2026通州期末-19-2 to satisfy strict internal-term scan without changing knowledge content.")
            elif "老龄化人口需求" in old:
                patches.append("Normalize Q-2026顺义一模-19-2 primary thinking line by adding `可写思维/方法` and `为什么能想到` fields from its existing material/action content; no new source claim.")
            elif "想象" in old and "基本单元" in old:
                patches.append("GPT must-fix: correct Q-2025丰台期末-8 so 形象思维 depends on 感性形象 and 概念 is only abstract thinking's basic unit.")
            elif "逐角度一句话" in old:
                patches.append("GPT optional transfer patch: add answer-length control to Q-2024海淀二模-17(1).")
            elif "调查了解对应感性具体" in old:
                patches.append("GPT optional transfer patch: add weak-student explanation to Q-2024海淀二模-17(2).")
            elif "综合推理题" in old:
                patches.append("GPT should-fix: mark Q-2024西城一模-19(5) as a 综合方法链/超前思维链, not a formal logic type.")
            elif "由实践→因果规律" in old:
                patches.append("GPT should-fix: state Q-2024西城一模-19(5) is not a formal logic positive example.")
            elif "类比推理 + 联言判断作辅助" in old:
                patches.append("GPT should-fix: remove 联言判断 from Q-2024朝阳二模-19(1) type name and leave it to Q19(2).")
    return new, patches


def main() -> None:
    text = BODY.read_text(encoding="utf-8")
    patched_text, patches = apply_review_only_patches(text)
    control = read_csv(CONTROL)
    sections = split_sections(patched_text)

    review_rows = [row_review(row, sections) for row in control]
    with REVIEW_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(review_rows[0].keys()))
        writer.writeheader()
        writer.writerows(review_rows)

    PATCHED_BODY.write_text(patched_text, encoding="utf-8")
    PATCHED_BODY_AFTER_GPT.write_text(patched_text, encoding="utf-8")

    post_hits = internal_hits(patched_text)
    pre_hits = internal_hits(text)
    INTERNAL_SCAN.write_text(
        "\n".join(
            [
                "# Phase11 Internal Terms Scan",
                "",
                f"- pre_patch_hits: {len(pre_hits)}",
                f"- post_patch_hits: {len(post_hits)}",
                "",
                "## Pre-Patch Hits",
                *[f"- `{pat}` line {ln}: {line}" for pat, ln, line in pre_hits],
                "",
                "## Post-Patch Hits",
                *[f"- `{pat}` line {ln}: {line}" for pat, ln, line in post_hits],
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    hard_lines: list[str] = ["# Phase11 QID Lock Recheck", ""]
    hard_fail = False
    if "小项不当扩大”作为正确结论" in patched_text or "小项不当扩大”为正确结论" in patched_text:
        hard_fail = True
        hard_lines.append("- FAIL: 顺义一模 Q7 risk phrasing looks like correct conclusion.")
    else:
        hard_lines.append("- PASS: 顺义一模 Q7 keeps 大项不当扩大 as true error and 小项不当扩大 only as A项错误表述.")

    if "B=①④" in patched_text or "①④" in patched_text and "2024 西城一模第11题" in patched_text:
        hard_fail = True
        hard_lines.append("- FAIL: possible forbidden Q11 pairing expansion.")
    else:
        hard_lines.append("- PASS: no forbidden Q11 `B=①④` pairing in student body.")

    for qid in HARD_EXCLUDED:
        hard_lines.append(f"- PASS: `{qid}` raw QID absent from student body." if qid not in patched_text else f"- FAIL: `{qid}` raw QID appears in student body.")
        if qid in patched_text:
            hard_fail = True

    QID_LOCK.write_text("\n".join(hard_lines) + "\n", encoding="utf-8")

    heading_text = "\n".join(re.findall(r"^### .+$", patched_text, re.M))
    control_ids = {r["question_id"] for r in control}
    index_failures: list[str] = []
    for row in control:
        for qid in [x.strip() for x in row.get("same_type_ids", "").replace(",", "；").split("；") if x.strip()]:
            if qid not in control_ids and qid in heading_text:
                index_failures.append(qid)
    INDEX_CHECK.write_text(
        "\n".join(
            [
                "# Phase11 Same-Type Index No-Expansion Check",
                "",
                f"- control body rows: {len(control)}",
                f"- visible headings: {len(re.findall(r'^### ', patched_text, re.M))}",
                f"- same-type index accidental heading expansions: {len(index_failures)}",
                f"- status: {'FAIL' if index_failures else 'PASS'}",
                "",
                "## Failures",
                *(f"- `{qid}`" for qid in sorted(set(index_failures))),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    status_counts = Counter(r["review_status"] for r in review_rows)
    patch_lines = [
        "# Phase11 29-Row Patch Plan",
        "",
        "Status: `CODEX_LOCAL_REVIEW_ONLY_NO_EXPANSION`",
        "",
        "## Summary",
        "",
        f"- reviewed_rows: {len(review_rows)}",
        f"- PASS rows: {status_counts.get('PASS', 0)}",
        f"- REVIEW rows: {status_counts.get('REVIEW', 0)}",
        f"- FAIL rows: {status_counts.get('FAIL', 0)}",
        f"- review-only patches: {len(patches)}",
        "",
        "## Accepted Review-Only Patches",
        "",
        *(f"- {p}" for p in patches),
        "",
        "## Rows Needing Human/GPT Attention",
        "",
    ]
    for row in review_rows:
        if row["review_status"] != "PASS":
            patch_lines.append(f"- `{row['question_id']}` {row['visible_title_found']}: {row['notes']}")
    if status_counts.get("REVIEW", 0) == 0 and status_counts.get("FAIL", 0) == 0:
        patch_lines.append("- none")
    PATCH_PLAN.write_text("\n".join(patch_lines) + "\n", encoding="utf-8")

    verify_lines = [
        "# Phase11A Codex Local Verification",
        "",
        "Verdict: `PASS_CODEX_PHASE11A_29ROW_CONTENT_REVIEW_NO_EXPANSION`" if not hard_fail and not index_failures and not post_hits else "Verdict: `REVIEW_CODEX_PHASE11A_PATCHES_PENDING`",
        "",
        f"- control rows: {len(control)}",
        f"- review rows: {len(review_rows)}",
        f"- patched body: `{PATCHED_BODY.relative_to(ROOT)}`",
        f"- post-patch internal term hits: {len(post_hits)}",
        f"- same-type accidental expansions: {len(index_failures)}",
        f"- hard-lock failure: {hard_fail}",
        "- Claude/ClaudeCode: suspended by user membership constraint.",
        "- Word/PDF/final: still forbidden.",
    ]
    VERIFY.write_text("\n".join(verify_lines) + "\n", encoding="utf-8")
    LOCAL_RECHECK.write_text("\n".join(verify_lines) + "\n", encoding="utf-8")
    PATCH_RESOLUTION.write_text(
        "\n".join(
            [
                "# Phase11A Content Patch Resolution",
                "",
                "Status: `PATCHED_AFTER_GPT_MUST_FIX_NO_EXPANSION`",
                "",
                "## GPT Verdict",
                "",
                "- GPT verdict: `MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION`",
                "- Raw reply: `08_review/gpt_phase_advice/phase_11A_gpt55_raw.md`",
                "",
                "## Patch Resolution",
                "",
                *[f"- {p}" for p in patches],
                "",
                "## Recheck",
                "",
                f"- reviewed_rows: {len(review_rows)}",
                f"- PASS rows: {status_counts.get('PASS', 0)}",
                f"- REVIEW rows: {status_counts.get('REVIEW', 0)}",
                f"- FAIL rows: {status_counts.get('FAIL', 0)}",
                f"- post_patch_internal_term_hits: {len(post_hits)}",
                f"- same_type_accidental_expansions: {len(index_failures)}",
                f"- hard_lock_failure: {hard_fail}",
                "- expansion: none",
                "- Word/PDF/final: still forbidden",
                "- Claude/ClaudeCode: still suspended by user membership constraint",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
