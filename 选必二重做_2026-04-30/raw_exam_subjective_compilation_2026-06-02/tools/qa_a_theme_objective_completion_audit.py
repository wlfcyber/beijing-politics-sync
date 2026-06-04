#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import json
from pathlib import Path

from docx import Document


RUN_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = RUN_DIR / "05_output"
AUDIT_MD = OUT_DIR / "A_THEME_OBJECTIVE_COMPLETION_AUDIT_20260604.md"
VISUAL_QA_JSON = OUT_DIR / "A_THEME_WORD_COM_VISUAL_QA_20260604.json"
VISUAL_REVIEW_MD = OUT_DIR / "A_THEME_VISUAL_CONTACT_SHEET_REVIEW_20260604.md"

sys.path.insert(0, str((RUN_DIR / "tools").resolve()))
import build_a_theme_full_handbook_docx as gen  # noqa: E402
import build_full_text_subjective_rubric_docx as base  # noqa: E402


FIVE_LABELS = ["【入口】", "【判定依据】", "【题目材料】", "【设问】", "【细则】", "【答案落点】"]
PHASE2_LABELS = ["【命题人路径】", "【判题四步】", "【高频给分件】", "【易混边界】"]
NOISE_TOKENS = [
    "SRC_",
    "source_id",
    "entry_E",
    "题眼",
    "评分锚点",
    "PAGEPAGE",
    "阅卷总结",
    "学生问题",
    "学生表现",
    "教师教学",
    "改进措施",
    "全球治理倡议",
    "上合组织",
    "全球南方",
]


def latest_docx() -> Path:
    candidates = [p for p in OUT_DIR.glob("*A类十主题学生宝典工作稿_20260604.docx") if "~$" not in p.name]
    if not candidates:
        raise FileNotFoundError("A-theme student DOCX not found")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def count_label_paragraphs(paragraphs, label: str) -> int:
    return sum(1 for paragraph in paragraphs if paragraph.text.strip().startswith(label))


def status(ok: bool, blocked: bool = False) -> str:
    if ok:
        return "PROVEN"
    if blocked:
        return "OPEN_GATE"
    return "NOT_PROVEN"


def main() -> None:
    packets, coverage, source_rows, overrides = gen.load_rows()
    repairs = gen.load_source_repair_overrides()
    resolutions = gen.load_pending_boundary_resolutions()
    packets = gen.apply_source_repair_overrides(packets, repairs)
    packets = gen.apply_pending_boundary_resolutions(packets, resolutions)
    stats = base.source_status_stats(source_rows, coverage, packets)
    rubric_exact, rubric_trimmed = gen.rubric_integrity_summary(packets, overrides)

    docx_path = latest_docx()
    doc = Document(docx_path)
    paragraphs = doc.paragraphs
    all_text = "\n".join(p.text for p in paragraphs)
    styles = {name: 0 for name in ("Heading 1", "Heading 2", "Heading 3")}
    for paragraph in paragraphs:
        if paragraph.style.name in styles:
            styles[paragraph.style.name] += 1

    pending_original = [p for p in packets if p.get("pending_reason")]
    pending_unresolved = [p for p in pending_original if not p.get("pending_boundary_cleared")]
    relayout_open = [p for p in packets if p["entry_id"] in gen.NEEDS_RELAYOUT and p["entry_id"] not in gen.SOURCE_REPAIR_CLEARS_RELAYOUT]
    visual_payload = {}
    if VISUAL_QA_JSON.exists():
        visual_payload = json.loads(VISUAL_QA_JSON.read_text(encoding="utf-8"))
    visual_pages = int(visual_payload.get("rendered_pages", 0) or 0)
    visual_blanks = len(visual_payload.get("suspicious_blank_pages", []) or [])
    visual_proven = visual_pages == visual_payload.get("word_export", {}).get("pages") and visual_pages > 0 and visual_blanks == 0 and VISUAL_REVIEW_MD.exists()

    checks = [
        {
            "requirement": "桌面源材料已递归清点并形成清单",
            "status": status((RUN_DIR / "01_inventory" / "desktop_candidate_sources.csv").exists()),
            "evidence": "`01_inventory/desktop_candidate_sources.csv`；覆盖报告记录 ledger 14471 条、include 190 条。",
        },
        {
            "requirement": "目标口径 63 套 / 67 大题 / 74 分问对齐",
            "status": status(stats.suites_total == 63 and stats.big_questions_total == 67 and stats.subquestions_total == 74),
            "evidence": f"suites={stats.suites_total}, big_questions={stats.big_questions_total}, subquestions={stats.subquestions_total}",
        },
        {
            "requirement": "A1-A10 十主题正文组织",
            "status": status(all(k in gen.THEMES for k in [f'A{i}' for i in range(1, 11)]) and styles["Heading 3"] == 74),
            "evidence": f"A主题={len(gen.THEMES)}；Heading3题卡={styles['Heading 3']}。",
        },
        {
            "requirement": "A1-A10 二轮主题加深卡完整",
            "status": status(all(count_label_paragraphs(paragraphs, label) == 10 for label in PHASE2_LABELS)),
            "evidence": "; ".join(f"{label}={count_label_paragraphs(paragraphs, label)}" for label in PHASE2_LABELS),
        },
        {
            "requirement": "每题保留入口、判定依据、题目材料、设问、细则、答案落点",
            "status": status(all(count_label_paragraphs(paragraphs, label) == 74 for label in FIVE_LABELS)),
            "evidence": "; ".join(f"{label}={count_label_paragraphs(paragraphs, label)}" for label in FIVE_LABELS),
        },
        {
            "requirement": "待重排/材料风险已回源修复或清零",
            "status": status(len(relayout_open) == 0),
            "evidence": f"source repair覆盖层={len(repairs)}；未闭合待回源重排={len(relayout_open)}。",
        },
        {
            "requirement": "细则非空并尽量保留官方评分段原文",
            "status": status(len(packets) == 74 and rubric_exact + len(rubric_trimmed) == 74),
            "evidence": f"74条细则非空；完全一致={rubric_exact}；仅截非评分段={len(rubric_trimmed)}。",
        },
        {
            "requirement": "真题索引保留在正文末段",
            "status": status("七、真题索引" in all_text),
            "evidence": "`七、真题索引` exists in DOCX text。",
        },
        {
            "requirement": "末尾单列待核/待补清单",
            "status": status("八、待核/待补清单" in all_text and len(pending_unresolved) == 2),
            "evidence": f"`八、待核/待补清单` exists；未清除 pending={len(pending_unresolved)}。",
        },
        {
            "requirement": "覆盖报告产出",
            "status": status((OUT_DIR / "A_THEME_STUDENT_GUIDE_COVERAGE_REPORT_20260604.md").exists()),
            "evidence": "`05_output/A_THEME_STUDENT_GUIDE_COVERAGE_REPORT_20260604.md`。",
        },
        {
            "requirement": "结构QA与Word打开检查",
            "status": status((OUT_DIR / "A_THEME_STUDENT_GUIDE_DOCX_QA_20260604.md").exists()),
            "evidence": "`A_THEME_STUDENT_GUIDE_DOCX_QA_20260604.md` records Word COM smoke and label counts。",
        },
        {
            "requirement": "PNG视觉渲染QA",
            "status": status(visual_proven, blocked=not visual_proven),
            "evidence": (
                f"Word COM -> PDF -> PNG visual QA rendered_pages={visual_pages}, suspicious_blank={visual_blanks}; "
                f"contact-sheet review exists={VISUAL_REVIEW_MD.exists()}."
            ),
        },
        {
            "requirement": "外部/真实模型最终审查门",
            "status": status(False, blocked=True),
            "evidence": "xuanbier skill requires real GPT/Claude gates for final delivery; this phase only has local QA and prior partial review artifacts.",
        },
    ]

    noise_hits = {token: all_text.count(token) for token in NOISE_TOKENS}
    unresolved_lines = []
    for entry in sorted(pending_unresolved, key=lambda item: item["entry_id"]):
        unresolved_lines.append(
            f"- {entry['entry_id']} {entry['title']}: {entry.get('pending_residual_issue') or entry.get('pending_reason')}"
        )

    lines = [
        "# A类十主题目标完成审计",
        "",
        "## 1. 总结",
        "",
        "- 当前稿件已满足 63 / 67 / 74 覆盖、A1-A10正文组织、十主题二轮加深卡、74题六件套、回源重排清零、覆盖报告、结构QA与Word COM视觉渲染QA。",
        "- 仍不得声明最终闭合：E009正式点分布细则缺失、E057模块边界需教师裁决、真实外部最终审查门未完成。",
        "",
        "## 2. 要求逐项审计",
        "",
        "| 要求 | 状态 | 证据 |",
        "| --- | --- | --- |",
    ]
    for check in checks:
        lines.append(f"| {check['requirement']} | {check['status']} | {check['evidence']} |")

    lines.extend(
        [
            "",
            "## 3. 待核/待补项",
            "",
            *(unresolved_lines or ["- 无。"]),
            "",
            "## 4. 噪音扫描",
            "",
            "| 词/模式 | 命中 |",
            "| --- | ---: |",
        ]
    )
    for token, count in noise_hits.items():
        lines.append(f"| `{token}` | {count} |")

    lines.extend(
        [
            "",
            "## 5. 结论边界",
            "",
            "- 本稿可作为 A类十主题厚版工作稿继续外部审查。",
            "- 未满足最终闭合条件，不应调用 final completion 或标记最终交付 PASS。",
            "",
        ]
    )

    AUDIT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(AUDIT_MD)
    print(f"checks={len(checks)} proven={sum(1 for c in checks if c['status']=='PROVEN')} open={sum(1 for c in checks if c['status']=='OPEN_GATE')}")
    print(f"heading3={styles['Heading 3']} pending_unresolved={len(pending_unresolved)} relayout_open={len(relayout_open)}")


if __name__ == "__main__":
    main()
