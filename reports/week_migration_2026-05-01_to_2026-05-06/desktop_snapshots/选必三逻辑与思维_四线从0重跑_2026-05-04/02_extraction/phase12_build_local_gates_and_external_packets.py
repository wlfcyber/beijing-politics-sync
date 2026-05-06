#!/usr/bin/env python3
"""Create Phase12 local gates and external review packets for the 77-row body."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
BODY = BASE / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
CONTROL = BASE / "09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv"
GAP = BASE / "09_student_draft/phase12_expanded_body_FROM_362_gap_backcheck.csv"
SORT = BASE / "09_student_draft/phase12_sort_key_matrix.csv"
THINKING_INDEX = BASE / "09_student_draft/phase12_thinking_method_index.md"
REASONING_INDEX = BASE / "09_student_draft/phase12_reasoning_typology_index.md"
QGATE = BASE / "08_review/phase12_quantity_and_coverage_gate.md"
DUAL_VERIFY = BASE / "08_review/phase12_dual_index_verification.md"
SUMMARY_362 = BASE / "05_coverage/phase12_362_control_base_rescan_summary.md"

CODEX_GATE = BASE / "08_review/phase12_codexA_local_review_gate.md"
GOVERNOR_GATE = BASE / "governor_confucius/phase12_governor_gate.md"
CONFUCIUS_GATE = BASE / "governor_confucius/phase12_confucius_learning_gate.md"
GPT_PROMPT = BASE / "08_review/gpt_phase_advice/phase_12_77body_prompt_for_gpt55_USER_SUBMIT.md"
CLAUDECODE_PROMPT = BASE / "08_review/claudecode_phase12_visible_77body_audit_prompt.md"
OPUS_PROMPT = BASE / "08_review/opus_writer/phase_12_77body_prompt_for_claude_opus47_adaptive.md"

BANNED = [
    "/Users",
    "OCR",
    "debug",
    "line id",
    "file id",
    "评标",
    "参考答案",
    "answer_confirmed",
    "A-formal",
    "B-choice-signal",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def count_headings(text: str) -> int:
    return len(re.findall(r"^###\s+", text, re.M))


def scan_terms(text: str) -> list[str]:
    return [term for term in BANNED if term in text]


def rel(path: Path) -> str:
    return str(path.relative_to(BASE))


def main() -> None:
    body_text = BODY.read_text(encoding="utf-8")
    thinking_text = THINKING_INDEX.read_text(encoding="utf-8")
    reasoning_text = REASONING_INDEX.read_text(encoding="utf-8")
    rows = read_csv(CONTROL)
    sort_rows = read_csv(SORT)
    gap_rows = read_csv(GAP)
    groups = Counter(row["question_type_group"] for row in rows)
    modules = Counter(row["module"] for row in rows)
    decisions = Counter(row["phase12_decision"] for row in rows)
    gap_counts = Counter(row["coverage_bucket"] for row in gap_rows)
    body_headings = count_headings(body_text)
    thinking_links = len(re.findall(r"^- 第", thinking_text, re.M))
    reasoning_links = len(re.findall(r"^- 第", reasoning_text, re.M))
    banned_hits = sorted(set(scan_terms(body_text) + scan_terms(thinking_text) + scan_terms(reasoning_text)))
    sort_monotonic = all(sort_rows[i]["sort_key"] <= sort_rows[i + 1]["sort_key"] for i in range(len(sort_rows) - 1))

    gate_clear = (
        len(rows) == 77
        and body_headings == 77
        and len(sort_rows) == 77
        and gap_counts.get("missing", 0) == 0
        and not banned_hits
        and sort_monotonic
    )

    local_status = "LOCAL_REVIEW_CLEAR_FOR_EXTERNAL_GATES_ONLY" if gate_clear else "LOCAL_REVIEW_HOLD_REPAIR_REQUIRED"
    remaining = [
        "visible ClaudeCode 77-row audit not captured",
        "GPT-5.5 Pro 77-row content review not captured",
        "Claude Opus 4.7 Adaptive teaching-text review not captured",
        "final student-clean build not created from review-only body",
        "Microsoft Word validation not allowed yet",
    ]

    CODEX_GATE.write_text(
        "\n".join(
            [
                "# Phase12 Codex A Local Review Gate",
                "",
                f"Status: `{local_status}`",
                "",
                "This gate checks the local 77-row review-only body after 362 rescan and dual-index generation. It does not authorize Word/PDF/final.",
                "",
                "## Checks",
                "",
                f"- control rows: {len(rows)}",
                f"- body headings: {body_headings}",
                f"- sort-key rows: {len(sort_rows)}",
                f"- gap missing rows: {gap_counts.get('missing', 0)}",
                f"- question groups: {dict(groups)}",
                f"- modules: {dict(modules)}",
                f"- decisions: {dict(decisions)}",
                f"- thinking index links: {thinking_links}",
                f"- reasoning index links: {reasoning_links}",
                f"- sort monotonic: {sort_monotonic}",
                f"- banned-term hits: {banned_hits or 'none'}",
                "",
                "## Remaining Hard Gates",
                "",
                *[f"- {item}" for item in remaining],
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    GOVERNOR_GATE.write_text(
        "\n".join(
            [
                "# Phase12 Governor Gate",
                "",
                "Status: `GOVERNOR_HOLD_EXTERNAL_GATES_PENDING`",
                "",
                "Governor decision: local structure is ready for external review, but final delivery remains blocked.",
                "",
                "## Governor Findings",
                "",
                "- 29-row packet has been superseded and cannot be used as final.",
                "- 74 locked evidence rows were represented before the 362 rescan.",
                "- 362 control-base rescan is complete at review-only level.",
                "- Current review-only body has 77 rows: 27 subjective and 50 choice.",
                "- Dual indexes exist for thinking methods and reasoning typologies.",
                "- Rows without reliable answers or visual recovery remain blocked; no answer guessing was used.",
                "- Review-only body still contains audit comments and status headers, so a later final student-clean build is required.",
                "",
                "## Governor Blockers Before Word",
                "",
                "- External GPT-5.5 Pro content review of the 77-row packet.",
                "- Visible ClaudeCode audit of the 77-row packet.",
                "- Claude Opus 4.7 Adaptive teaching-text review after content lock.",
                "- Confucius zero-baseline learning-value gate after external corrections.",
                "- Final clean Markdown build without review-only headers or comments.",
                "- Microsoft Word open/save/render validation after all content gates.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    CONFUCIUS_GATE.write_text(
        "\n".join(
            [
                "# Phase12 Confucius Learning Gate",
                "",
                "Status: `CONFUCIUS_HOLD_NEEDS_EXTERNAL_AND_FINAL_CLEAN_BUILD`",
                "",
                "This gate asks whether a zero-baseline student can learn transferable methods from the current review-only body.",
                "",
                "## Learning Checks",
                "",
                "- 思维部分 already uses material signals, methods, why-trigger logic, answer landing, and traps across the 77-row body.",
                "- 推理部分 now has a typology index, so students can return from a rule family to all included same-type questions.",
                "- Choice entries include correct-option reasons and wrong-option traps rather than only answer letters.",
                "- Subjective entries usually show the path from material action to method and answer sentence.",
                "",
                "## Confucius Holds",
                "",
                "- Some review-only entries still need final wording compression into a fully student-clean version.",
                "- The current files are not yet a classroom final because external content criticism has not been captured.",
                "- No Word/PDF should be generated from this version.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    packet_common = f"""本轮任务：审查选必三《逻辑与思维》Phase12 77 条 review-only 扩展正文。

硬背景：
- 29 条候选稿已被用户否决为题量过少，只能叫 controlled packet，不得称终稿。
- 已按你的 Phase12 指挥稿完成 74-row 全裁决、45 non-body repair、362-row rescan。
- 当前正文 77 条：主观题 27，选择题 50。
- 正文排序规则：主观题在前，选择题在后；每类内部按海淀、西城、东城、朝阳、丰台、其他区；年份 2026 > 2025 > 2024。
- 已生成双索引：思维方法索引、推理题型索引。
- 未找到可靠答案或视觉证据的题继续 blocked，没有逻辑猜答案。
- 请不要授权 Word/PDF/final；只做内容审查和下一步修补建议。

请重点审：
1. 77 条里有没有明显漏题、误入、重复或该 blocked 却入正文的题。
2. 主观题四要件是否像哲学宝典：材料信号、可写方法、为什么能想到、答案落点都足够具体。
3. 推理题是否有逻辑形式、规则口令、有效/无效式、错项陷阱。
4. 选择题是否都不是只写答案字母，而是有正确项理由和错项陷阱。
5. 双索引是否真正把同类题挂全，而不是只放代表例。
6. 哪些条目必须回源修复，哪些只是表达可优化。

请输出：
- verdict: GO_EXTERNAL_PATCH / MUST_FIX_CONTENT / HOLD_SOURCE_REPAIR / READY_FOR_FINAL_CLEAN_BUILD_BUT_NO_WORD
- must_fix
- should_fix
- source_or_scope_risks
- index_risks
- merge_policy
- next_commands_for_codex

需要审的文件：
- {rel(BODY)}
- {rel(CONTROL)}
- {rel(THINKING_INDEX)}
- {rel(REASONING_INDEX)}
- {rel(SORT)}
- {rel(SUMMARY_362)}
- {rel(CODEX_GATE)}
- {rel(GOVERNOR_GATE)}
- {rel(CONFUCIUS_GATE)}
"""

    GPT_PROMPT.write_text(
        "# Phase12 77-Row GPT-5.5 Pro Review Prompt\n\n"
        "把本文件和上面列出的 review-only 正文、双索引、控制矩阵一起提交给 GPT-5.5 Pro。Codex 不再自行点击 GPT 页面，避免误停。\n\n"
        + packet_common,
        encoding="utf-8",
    )
    CLAUDECODE_PROMPT.write_text(
        "# ClaudeCode Phase12 Visible 77-Row Audit Prompt\n\n"
        "你必须在真实可见 ClaudeCode 窗口工作，不得用旧 29-row Word 当底稿，不得生成 Word/PDF/final。\n\n"
        + packet_common
        + "\n输出到 `claudecode_lane/phase12_visible_77row_audit/`，至少生成 audit_matrix.csv、audit_report.md、patch_queue.csv、visible_status.md。\n",
        encoding="utf-8",
    )
    OPUS_PROMPT.write_text(
        "# Claude Opus 4.7 Adaptive Phase12 77-Row Teaching Review Prompt\n\n"
        "你是教学成文化审稿线，不是证据源。任何新表达必须能回到 Codex source lock。不要输出 Word/PDF/final。\n\n"
        + packet_common
        + "\n请特别用弱学生视角检查：是否看完能迁移到新题，哪些条目仍像审计话而不像卷面答案。\n",
        encoding="utf-8",
    )

    print(local_status)
    print(f"rows={len(rows)} headings={body_headings} thinking_links={thinking_links} reasoning_links={reasoning_links}")
    print(f"banned={banned_hits or 'none'}")


if __name__ == "__main__":
    main()
