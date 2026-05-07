#!/usr/bin/env python3
"""Initialize a Feige Politics Garden full-book run workspace."""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import date
from pathlib import Path


DIRS = [
    "00_control",
    "01_source_inventory",
    "02_extraction/codex_extraction_logs",
    "02_extraction/claudecode_extraction_logs",
    "02_extraction/screenshots",
    "02_extraction/ocr_outputs",
    "02_extraction/ppt_outputs",
    "02_extraction/table_outputs",
    "02_extraction/image_notes",
    "03_entries",
    "04_suite_reports/codex_suite_reports",
    "04_suite_reports/claudecode_suite_reports",
    "04_suite_reports/merged_suite_reports",
    "05_coverage",
    "06_conflicts/source_recheck_notes",
    "07_student_doc/figures",
    "07_student_doc/tables",
    "07_student_doc/exercises",
    "08_review",
    "08_review/phase_reports",
    "08_review/gpt_phase_advice",
    "08_review/gpt_content_review",
    "09_delivery",
    "advisor_prompts",
    "advisor_reports",
    "codex_lane",
    "claudecode_lane",
    "fusion",
    "suite_reports",
    "audit/confucius",
    "audit/render",
    "outputs",
]


def slug(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|\\s]+", "_", text.strip())
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "book"


def write_once(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Beijing politics workspace root")
    parser.add_argument("--book", required=True, help="Book name, e.g. 必修四")
    parser.add_argument("--scope", default="", help="Scope, e.g. 哲学")
    parser.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD")
    parser.add_argument("--name", default="", help="Optional run folder name")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    run_name = args.name or f"{slug(args.book)}_{slug(args.scope or '整本书')}_三线总控_{args.date}"
    run_dir = root / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    for rel in DIRS:
        (run_dir / rel).mkdir(parents=True, exist_ok=True)

    meta = {
        "book": args.book,
        "scope": args.scope,
        "date": args.date,
        "run_dir": str(run_dir),
        "status": "not_started",
    }
    write_once(run_dir / "RUN_MANIFEST.json", json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    write_once(
        run_dir / "00_control" / "RUN_MANIFEST.yaml",
        f"run_id: {run_name}\nbook_or_module: {args.book}\nscope: {args.scope or '整本书'}\nmode:\nstart_type:\nsource_range: 2024-2026 Beijing district papers unless narrowed\nskill_route:\nnotebooks_required:\nmaster_requirements_version:\nevidence_priority_rule: P0 scoring/marking rules > P1 reference answers > P2 lecture/analysis > P3 paper text > P4 AI/advisor drafts\nstudent_doc_goal: material trigger -> why this principle/term -> answer landing\ndeliverables:\n  - Markdown\n  - Word\n  - acceptance_report\ncreated_at: {args.date}\ncontroller: Codex\ncodex_line_status: not_started\nclaudecode_line_status: not_started\ngovernor_status: not_started\nconfucius_status: not_started\n",
    )
    write_once(
        run_dir / "00_control" / "START_CARD.md",
        "# Start Card\n\n- 用户原始启动语:\n- 本轮书目:\n- 本轮范围:\n- 本轮模式:\n- 从0/续跑声明:\n- 用户给定考题框架:\n- 默认证据范围:\n- 特殊禁区:\n- 交付要求:\n- 待确认但不阻塞项:\n",
    )
    write_once(
        run_dir / "00_control" / "ZERO_START_DECLARATION.md",
        "# Zero Start Declaration\n\nUse when the user says 从0开始, 旧线作废, or 不继承旧结论.\n\n- 本轮不继承旧结论。\n- 旧文件只允许用于定位源材料、差异审计、查找遗漏风险。\n- 所有结论必须由本轮 entries 和本轮源证据重新支持。\n- 若发现旧结论被复用，必须登记并返工。\n",
    )
    write_once(
        run_dir / "00_control" / "EVIDENCE_PRIORITY_RULES.md",
        "# Evidence Priority Rules\n\n- P0: formal scoring rubrics, marking rules, marking reports, or explicit marking-standard lecture/report fragments.\n- P1: official/district/school reference answers and 答案及评分参考. P1 is not P0 unless the user confirms.\n- P2: lecture slides, teacher explanations, test analysis, and teaching materials.\n- P3: paper text, question materials, options, charts, cartoons, and tables.\n- P4: AI summaries, advisor suggestions, and working drafts. P4 never proves facts.\n",
    )
    write_once(run_dir / "00_control" / "NOTEBOOK_DIGEST.md", "# Notebook Digest\n\n")
    write_once(run_dir / "00_control" / "GOVERNOR_GATES.md", "# Governor Gates\n\n- G0 startup:\n- G1 notebook:\n- G2 source inventory:\n- G3 non-text handling:\n- G4 evidence levels:\n- G5 coverage:\n- G6 conflicts:\n- G7 student transfer:\n- G8 Word/PDF visual QA:\n- G9 Confucius:\n- G10 GPT phase mechanism: phase report complete, GPT raw advice saved or fallback logged, Codex digestion complete, late review scheduled when needed.\n- G11 GPT content review: outline, section_batch, final_markdown, and word_pdf reviewed by GPT-5.5 Pro or covered by fallback/waiver; raw review saved; correction log complete; substantive fixes evidence-verified; accepted fixes patched and verified closed; rejected fixes locally justified; deferred fixes moved to user decision; no unresolved must_fix_content and no transfer-blocking should_fix_transfer; Markdown PASS and Word/PDF PASS recorded separately.\n")
    write_once(run_dir / "00_control" / "MODEL_ADVICE_LOG.md", "# Model Advice Log\n\n")
    write_once(run_dir / "00_control" / "DECISION_LOG.md", "# Decision Log\n\n")
    write_once(run_dir / "00_control" / "PROGRESS_LEDGER.jsonl", "")

    write_once(
        run_dir / "TASK_BRIEF.md",
        f"# Task Brief\n\n- Book: {args.book}\n- Scope: {args.scope or '整本书'}\n- Date: {args.date}\n- Final target: Markdown + Word teaching document + final acceptance report.\n",
    )
    write_once(
        run_dir / "task_plan.md",
        f"# Task Plan\n\nGoal: Run {args.book} {args.scope or '整本书'} through three lanes into a final teaching document: Codex leader, Codex production, and Claude Code independent rerun.\n\n## Current Status\n\n- status: not_started\n- current_phase: Phase 0 Intake\n\n## Phase Boundary Rule\n\nAfter each phase or substantial milestone: write a sanitized phase report, send it to GPT-5.5 Pro when available, save the raw commander advice, digest it into local tasks, and continue. If GPT/web/thread stalls, log the fallback and keep running authorized local work. Governor, not GPT, owns phase release; fallback phases need late review when GPT returns.\n\n## GPT Content Review Rule\n\nAfter each fixed trigger object (`outline`, `section_batch`, `final_markdown`, `word_pdf`): send the generated content itself to GPT-5.5 Pro in chunks, save raw review, digest concrete content corrections, locally verify substantive fixes, patch, and rerun until no unresolved `must_fix_content` remains and no `should_fix_transfer` blocks student transfer. Missing trigger objects need fallback/waiver. Markdown PASS and Word/PDF PASS are separate. Final PASS is blocked until this is complete unless the user disables it.\n\n## Phases\n\n- [ ] Phase 0: Intake and user framework lock\n- [ ] Phase 1: Workspace, notebooks, and master requirements\n- [ ] Phase 2: Source inventory and evidence map\n- [ ] Phase 3: Three-lane production by suite/question\n- [ ] Phase 4: Advisor review and governor checks\n- [ ] Phase 5: Fusion into student artifact\n- [ ] Phase 6: Word/PDF production and visual QA\n- [ ] Phase 7: Confucius artifact-only learning verification\n- [ ] Phase 8: Final acceptance report\n\n## Decisions Made\n\n\n## Errors Encountered\n\n| Attempt | Error/Symptom | Different Next Step | Resolution |\n|---|---|---|---|\n",
    )
    write_once(
        run_dir / "findings.md",
        "# Findings\n\nRecord source discoveries here, especially after PDF/image/browser/OCR/visual reads.\n\n## Source Findings\n\n",
    )
    write_once(
        run_dir / "progress.md",
        "# Progress Log\n\nChronological session log. Update after phases, worker wakeups, errors, and validation checks.\n\n",
    )
    write_once(
        run_dir / "MASTER_REQUIREMENTS.md",
        "# Master Requirements\n\nFill this before production. Resolve conflicts as: user message > lane notebook > branch skill > old artifacts.\n",
    )
    write_once(
        run_dir / "USER_FRAMEWORK.md",
        "# User Framework\n\nPaste or summarize the user's book logic, framework nodes, hard samples, and boundary rules here.\n",
    )
    write_once(run_dir / "USER_QUESTIONS.md", "# User Questions\n\n")
    write_once(run_dir / "PROGRESS.md", "# Progress\n\n- status: not_started\n- current_suite: \n- current_lane: \n- next_step: \n")
    write_once(run_dir / "DECISION_LOG.md", "# Decision Log\n\n")
    write_once(run_dir / "FINAL_ACCEPTANCE_REPORT.md", "# Final Acceptance Report\n\nStatus: not_started\n")
    write_once(run_dir / "02_extraction" / "failed_extractions.md", "# Failed Extractions\n\n")
    write_once(run_dir / "06_conflicts" / "conflict_register.md", "# Conflict Register\n\n")
    write_once(run_dir / "06_conflicts" / "resolved_conflicts.md", "# Resolved Conflicts\n\n")
    write_once(run_dir / "06_conflicts" / "unresolved_conflicts.md", "# Unresolved Conflicts\n\n")
    write_once(run_dir / "07_student_doc" / "student_doc_outline.md", "# Student Document Outline\n\n")
    write_once(run_dir / "07_student_doc" / "student_doc_draft.md", "# Student Document Draft\n\n")
    write_once(run_dir / "07_student_doc" / "student_doc_final.md", "# Student Document Final\n\n")
    write_once(run_dir / "07_student_doc" / "glossary.md", "# Glossary\n\n")
    write_once(run_dir / "08_review" / "gpt_context_pack.md", "# GPT Context Pack\n\n")
    write_once(run_dir / "08_review" / "gpt_advice.md", "# GPT Advice\n\n")
    write_once(
        run_dir / "08_review" / "phase_reports" / "phase_report_template.md",
        "# Phase Report Template\n\nUse this after every phase before asking GPT-5.5 Pro for commander advice. Keep it sanitized. Missing required fields means Governor G10 fails.\n\n- phase_name:\n- phase_goal:\n- completed_actions:\n- unfinished_actions:\n- changed_artifacts:\n- source_coverage_summary:\n- non_text_material_summary:\n- evidence_level_counts_P0_P1_P2_P3_P4:\n- missing_suites_questions_or_file_types:\n- codex_vs_claudecode_differences:\n- conflict_summary:\n- blockers:\n- governor_gate_status:\n- three_uncertainties:\n  1. \n  2. \n  3. \n- most_likely_missing_material_types:\n- most_likely_evidence_level_mislabels:\n- most_likely_student_misleading_phrases:\n- do_not_enter_student_doc_list:\n- questions_for_gpt_commander:\n- candidate_next_tasks:\n\nForbidden in GPT-facing text: accounts, secrets, local absolute paths, environment details, large raw exam passages, large raw scoring-rule passages, private drafts, or unverified source claims. Preserve review structure with source_id/year/district-or-exam-type/file-type/question-type/evidence-level/status/non-text flags/blocker status when relevant.\n",
    )
    write_once(
        run_dir / "08_review" / "gpt_phase_advice" / "gpt_phase_advice_index.md",
        "# GPT Phase Advice Index\n\n| Phase | Sent To GPT | Raw Advice File | Codex Digestion | Local Tasks Created | Fallback | Late Review | Governor G10 Status |\n|---|---|---|---|---|---|---|---|\n",
    )
    write_once(
        run_dir / "08_review" / "gpt_phase_fallback_log.md",
        "# GPT Phase Fallback Log\n\nWhen GPT-5.5 Pro, the web page, browser automation, or another advisor thread stalls, log the phase, symptom, fallback decision, retry point, and late-review requirement here. Do not let advisor delay alone freeze authorized local work.\n\n| Time | Phase | Symptom | Missing GPT Questions | Temporary Codex Decision | Degraded Scope | Retry Point | Late Review Required | Late Review Result |\n|---|---|---|---|---|---|---|---|---|\n",
    )
    write_once(
        run_dir / "08_review" / "gpt_content_review" / "content_review_template.md",
        "# GPT Content Review Template\n\nUse this after every fixed trigger object: `outline`, `section_batch`, `final_markdown`, and `word_pdf`. Send generated content itself in chunks; do not send accounts, local absolute paths, full source files, or large raw exam/scoring passages. A missing trigger object needs fallback or user waiver.\n\n- trigger_object:\n- artifact:\n- chunk_id:\n- title_path:\n- book_scope:\n- user_framework_summary:\n- target_student:\n- evidence_fusion_status_summary:\n- content_sent_to_gpt:\n- questions_for_content_review:\n\nAsk GPT for: conceptual mistakes, missing material triggers, unsupported answer landings, weak transfer chains, incomplete choice-question logic, contradictions, misleading wording, and concrete rewrites. `must_fix_content` blocks final PASS; `should_fix_transfer` blocks student-facing final PASS when it breaks transfer; `style_or_readability` may be fast-fixed only when it does not change facts.\n",
    )
    write_once(
        run_dir / "08_review" / "gpt_content_review" / "gpt_content_review_index.md",
        "# GPT Content Review Index\n\n| Trigger Object | Artifact | Chunk | Sent To GPT | Raw Review File | Correction Log Rows | Must-Fix Open | Transfer-Fix Open | Fallback/Waiver | Markdown PASS | Word/PDF PASS | Governor G11 Status |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n",
    )
    write_once(
        run_dir / "08_review" / "gpt_content_review" / "content_correction_log.md",
        "# Content Correction Log\n\n| issue_id | artifact | location | severity | gpt_claim | proposed_correction | local_evidence_check_needed | local_check_result | codex_decision | patch_status | affects_student_doc | verified_closed_at |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n",
    )
    write_once(run_dir / "08_review" / "claude_context_pack.md", "# Claude Context Pack\n\n")
    write_once(run_dir / "08_review" / "claude_advice.md", "# Claude Advice\n\n")
    write_once(run_dir / "08_review" / "codex_response_to_advice.md", "# Codex Response To Advice\n\n")
    write_once(run_dir / "08_review" / "confucius_report.md", "# Confucius Report\n\n")
    write_once(run_dir / "08_review" / "confucius_fix_log.md", "# Confucius Fix Log\n\n")
    write_once(run_dir / "09_delivery" / "word_visual_check.md", "# Word Visual Check\n\n")
    write_once(run_dir / "09_delivery" / "pdf_visual_check.md", "# PDF Visual Check\n\n")
    write_once(run_dir / "09_delivery" / "acceptance_report.md", "# Acceptance Report\n\n")
    write_once(run_dir / "09_delivery" / "delivery_manifest.md", "# Delivery Manifest\n\n")

    ledger = run_dir / "SOURCE_LEDGER.csv"
    if not ledger.exists():
        with ledger.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["source_id", "suite", "path", "source_type", "evidence_type", "extraction_method", "status", "notes"])

    coverage = run_dir / "COVERAGE_MATRIX.csv"
    if not coverage.exists():
        with coverage.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["suite", "question", "module_scope", "status", "codex_entry", "claudecode_entry", "fusion_status", "evidence_status", "notes"])
    for rel, headers in {
        "01_source_inventory/SOURCE_INVENTORY.csv": ["source_id", "year", "district", "exam_type", "path", "file_type", "has_answer", "has_rubric", "has_lecture", "status", "notes"],
        "01_source_inventory/FILE_TYPE_ROUTING.csv": ["source_id", "file_type", "required_method", "actual_method", "status", "blocker"],
        "03_entries/evidence_level_index.csv": ["entry_id", "source_id", "question", "evidence_level", "scoring_source_type", "notes"],
        "04_suite_reports/suite_completion_matrix.csv": ["suite", "source_id", "codex_status", "claudecode_status", "merged_status", "missing_questions", "non_text_status"],
        "05_coverage/coverage_by_book_unit.csv": ["book", "unit", "question_count", "entry_count", "evidence_status", "notes"],
        "05_coverage/coverage_by_question_type.csv": ["question_type", "question_count", "entry_count", "evidence_status", "notes"],
        "05_coverage/coverage_by_year_district_exam.csv": ["year", "district", "exam_type", "question_count", "entry_count", "status"],
        "05_coverage/coverage_by_evidence_level.csv": ["evidence_level", "count", "notes"],
    }.items():
        path = run_dir / rel
        if not path.exists():
            with path.open("w", encoding="utf-8", newline="") as f:
                csv.writer(f).writerow(headers)
    write_once(run_dir / "05_coverage" / "missing_questions.md", "# Missing Questions\n\n")
    write_once(run_dir / "05_coverage" / "unresolved_blockers.md", "# Unresolved Blockers\n\n")

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
