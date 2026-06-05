#!/usr/bin/env python3
"""Build strict citation and visible external-review prompt packets."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


REVIEW_FILES = [
    "06_论文初稿.md",
    "05_论证骨架.md",
    "20_质量差距诊断与重写方案.md",
    "source_inventory.md",
    "source_provenance_ledger.md",
    "28_政策原始发布源一致性记录.md",
    "citation_final.md",
    "16_总闸口矩阵.md",
    "15_外部评审与迭代计划.md",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def scrub_paths(text: str) -> str:
    home = str(Path.home())
    text = text.replace(f"{home}/Documents/论文写作/", "<workspace>/")
    text = text.replace(f"{home}/Documents/论文写作", "<workspace>")
    text = text.replace(f"{home}/GaokaoPolitics/", "<repo>/")
    text = text.replace(f"{home}/", "<user-home>/")
    text = text.replace(home, "<user-home>")
    text = text.replace(r"C:\Users\Administrator\Documents\论文写作\\", r"<workspace>\\")
    text = text.replace(r"C:\Users\Administrator\Documents\论文写作", "<workspace>")
    text = text.replace(r"C:\Users\Administrator", "<user-home>")
    return text


def parse_summary_value(text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def extract_table(text: str, header_start: str) -> list[str]:
    lines = text.splitlines()
    out: list[str] = []
    capture = False
    for line in lines:
        if line.startswith(header_start):
            capture = True
        if capture:
            if line.startswith("|"):
                out.append(line)
            elif out:
                break
    return out


def citation_status_block(citation_text: str) -> list[str]:
    keys = [
        "body_citation_occurrences",
        "anchored_citations",
        "blocked_public_reprint_citations",
        "needs_manual_anchor",
        "working_anchor_ready",
        "manual_verified_anchors",
        "agent_verified_anchors",
        "citation_level_verified_anchors",
        "citation_alignment_method",
        "citation_alignment_scope",
        "final_anchor_ready",
    ]
    return [f"- {key}: {parse_summary_value(citation_text, key)}" for key in keys]


def build_citation_packet(run_dir: Path) -> str:
    citation_text = read(run_dir / "citation_final.md")
    page_suggestions = read(run_dir / "citation_page_suggestions.md")
    semantic = read(run_dir / "citation_semantic_verification.md")
    citation_table = extract_table(citation_text, "| No. |")
    suggestions_table = extract_table(page_suggestions, "| No. |")

    lines = [
        "# 引用页码终核包",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "## 当前状态",
        "",
        *citation_status_block(citation_text),
        "",
        "## 终核规则",
        "",
        "- 工作锚点不能视为最终页码；`anchored_from_evidence_index` 只说明当前页候选来自全文索引。",
        "- 只有逐条核对正文断言、原文页码和语义对应后，才可把该条改为最终页码。",
        "- 不得为了通过审阅而补写不存在的页码、引文、作者、刊物、DOI、CNKI 记录或原文表述。",
        "- 如果某条正文断言无法在来源中确认，应改正文断言、移除引用或降格为背景材料。",
        "",
        "## 正文引用逐条清单",
        "",
    ]
    if citation_table:
        lines.extend(citation_table)
    else:
        lines.append("_未找到 citation_final.md 的逐条表。_")

    lines.extend(["", "## 页码建议来源", ""])
    if suggestions_table:
        lines.extend(suggestions_table)
    else:
        lines.append("_未找到 citation_page_suggestions.md 的页码建议表。_")

    semantic_summary = "\n".join(
        line
        for line in semantic.splitlines()
        if line.startswith("- body_citation_occurrences:")
        or line.startswith("- strong_semantic_candidates:")
        or line.startswith("- weak_semantic_candidates:")
        or line.startswith("- needs_manual_semantic_check:")
        or line.startswith("- semantic_alignment_ready:")
    )
    if semantic_summary:
        lines.extend(["", "## 语义候选摘要", "", semantic_summary])

    return scrub_paths("\n".join(lines).rstrip() + "\n")


def build_review_packet(run_dir: Path, citation_packet_text: str) -> str:
    citation_text = read(run_dir / "citation_final.md")
    final_anchor_ready = parse_summary_value(citation_text, "final_anchor_ready")

    lines = [
        "# 最终外部评审包",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "- timestamp_note: generated_at uses UTC; Chinese access dates in the draft use Asia/Shanghai local date",
        "- target_lanes: Claude Opus / Opus 4.8 Max; GPT Pro / GPT-5.5 Pro",
        "- required_channel: visible web_session or app_session",
        "",
        "## 提交给外部模型的硬规则",
        "",
        "- 你正在审阅一篇中文人文社科研究生课程论文及其自动化工作流。",
        "- 本轮目标是研究生课程论文/机制性二次分析，不是学位论文、期刊投稿或一手田野实证论文。",
        "- 你不能发明作者、刊物、年份、DOI、CNKI 记录、页码、原文、访谈、问卷或政策事实。",
        "- 如果 `final_anchor_ready` 不是 `yes`，不得给出 `PASS`。",
        "- 不得仅因论文诚实声明无一手访谈、问卷或统计数据就判 `REVISE`；请判断既有案例材料是否足以支撑其课程论文层级的机制性论证。",
        "- 授权数据库来源不要求公开 URL；若有合法获取路径、本地全文文件和 hash 台账，可视为工作流内可复验。",
        "- 如果外部评审记录不是可见网页或 App 会话，也不得认定最终目标完成。",
        "- 最终 PASS 必须基于本包内论文全文及证据材料的完整审阅；只审修订差异、引用页码抽查包、登录预检或交接提示，不得给 `safe_to_record_as_final_visible_review_pass=yes`。",
        "- 如果你就是当前被请求的最终可见审阅 lane，不得仅因该 lane 尚未登记通过、`external_review_passed=no` 或 `final_user_goal_ready=no` 而判 `REVISE`；这些字段需要用你的本次可见结论更新。",
        "- 请按论文质量、引用页码、材料诚信、方法-材料匹配和工作流目标分别判断。",
        "",
        "## 请返回以下字段",
        "",
        "```text",
        "verdict: PASS / REVISE",
        "graduate_quality_judgment: ...",
        "citation_anchor_judgment: ...",
        "source_and_metadata_judgment: ...",
        "method_data_fit_judgment: ...",
        "workflow_goal_judgment: ...",
        "must_fix_before_pass: ...",
        "review_scope: full_draft",
        "full_text_reviewed: yes/no",
        "safe_to_record_as_final_visible_review_pass: yes/no",
        "```",
        "",
        "## 本地闸口摘要",
        "",
        f"- final_anchor_ready: {final_anchor_ready}",
        f"- external_review_passed: {parse_summary_value(read(run_dir / '15_外部评审与迭代计划.md'), 'external_review_passed')}",
        f"- claude_opus_review_status: {parse_summary_value(read(run_dir / '15_外部评审与迭代计划.md'), 'claude_opus_review_status')}",
        f"- gpt_pro_review_status: {parse_summary_value(read(run_dir / '15_外部评审与迭代计划.md'), 'gpt_pro_review_status')}",
        "",
        "## 引用页码终核状态",
        "",
        citation_packet_text,
        "",
        "## 审阅材料",
        "",
    ]

    for name in REVIEW_FILES:
        content = scrub_paths(read(run_dir / name)).strip()
        if not content:
            continue
        lines.extend([f"### File: {name}", "", "```markdown", content, "```", ""])

    return "\n".join(lines).rstrip() + "\n"


def selected_gate_lines(gate_text: str) -> list[str]:
    selected: list[str] = []
    for line in gate_text.splitlines():
        if (
            "final_user_goal_ready" in line
            or "topic_selection_ready" in line
            or "paper_material_ready" in line
            or "| 页码层" in line
            or "| 外部评审层" in line
            or "| 文本质量层" in line
            or "| 浏览器层" in line
            or "| 原刊层" in line
        ):
            selected.append(line)
    return selected


def build_web_packet(run_dir: Path) -> str:
    draft = scrub_paths(read(run_dir / "06_论文初稿.md")).strip()
    citation_text = read(run_dir / "citation_final.md")
    workbench_text = read(run_dir / "citation_evidence_workbench.md")
    external_text = read(run_dir / "15_外部评审与迭代计划.md")
    gate_text = read(run_dir / "16_总闸口矩阵.md")
    inventory_text = read(run_dir / "source_inventory.md")

    inventory_summary = "\n".join(
        line
        for line in inventory_text.splitlines()
        if line.startswith("- usable_fulltext:")
        or line.startswith("- candidate_or_incomplete:")
        or line.startswith("- total_files:")
    )

    lines = [
        "# 网页外审精简包",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "- timestamp_note: generated_at uses UTC; Chinese access dates in the draft use Asia/Shanghai local date",
        "- target_lanes: Claude Opus / Opus 4.8 Max; GPT Pro / GPT-5.5 Pro",
        "- use: paste into a visible ChatGPT/Claude web or app session",
        "",
        "## 审阅硬规则",
        "",
        "- 不能发明作者、刊物、年份、DOI、CNKI 记录、页码、原文、访谈、问卷或政策事实。",
        "- 本轮目标是研究生课程论文/机制性二次分析，不是学位论文、期刊投稿或一手田野实证论文。",
        "- 如果 `final_anchor_ready` 不是 `yes`，不得给出 `PASS`。",
        "- 不得仅因论文诚实声明无一手访谈、问卷或统计数据就判 `REVISE`；请判断既有案例材料是否足以支撑其课程论文层级的机制性论证。",
        "- 授权数据库来源不要求公开 URL；若有合法获取路径、本地全文文件和 hash 台账，可视为工作流内可复验。",
        "- 如果你认为论文质量尚未达到强研究生课程论文，也请给出 `REVISE`。",
        "- 最终 PASS 必须基于本包内论文全文及证据材料的完整审阅；只审修订差异、引用页码抽查包、登录预检或交接提示，不得给 `safe_to_record_as_final_visible_review_pass=yes`。",
        "- 如果你就是当前被请求的最终可见审阅 lane，不得仅因该 lane 尚未登记通过、`external_review_passed=no` 或 `final_user_goal_ready=no` 而判 `REVISE`；这些字段需要用你的本次可见结论更新。",
        "- 引用逐条表见 `25_引用页码终核包.md`；本包只放网页粘贴所需摘要。",
        "",
        "## 请返回",
        "",
        "```text",
        "verdict: PASS / REVISE",
        "graduate_quality_judgment: ...",
        "citation_anchor_judgment: ...",
        "source_and_metadata_judgment: ...",
        "method_data_fit_judgment: ...",
        "workflow_goal_judgment: ...",
        "must_fix_before_pass: ...",
        "review_scope: full_draft",
        "full_text_reviewed: yes/no",
        "safe_to_record_as_final_visible_review_pass: yes/no",
        "```",
        "",
        "## 本地状态摘要",
        "",
        *citation_status_block(citation_text),
        f"- external_review_passed: {parse_summary_value(external_text, 'external_review_passed')}",
        f"- claude_opus_review_status: {parse_summary_value(external_text, 'claude_opus_review_status')}",
        f"- gpt_pro_review_status: {parse_summary_value(external_text, 'gpt_pro_review_status')}",
        "",
    ]
    if workbench_text:
        lines.extend(
            [
                "## 引用证据工作台摘要",
                "",
                "- evidence_workbench: `citation_evidence_workbench.md`",
                f"- rows_with_source_excerpt: {parse_summary_value(workbench_text, 'rows_with_source_excerpt')}",
                f"- missing_source_text: {parse_summary_value(workbench_text, 'missing_source_text')}",
                f"- missing_excerpt: {parse_summary_value(workbench_text, 'missing_excerpt')}",
                "- workbench_role: excerpt review table only; final anchor authority is `citation_final.md`",
                "",
            ]
        )
    gates = selected_gate_lines(gate_text)
    if gates:
        lines.extend(["## 总闸口摘录", "", *gates, ""])
    if inventory_summary:
        lines.extend(["## 材料清单摘要", "", inventory_summary, ""])

    lines.extend(["## 论文全文", "", "```markdown", draft, "```", ""])
    return "\n".join(lines).rstrip() + "\n"


def build_claude_full_packet(run_dir: Path, web_packet_text: str, citation_packet_text: str) -> str:
    """Build a fuller visible-app packet for strict Claude reviews."""

    external_text = read(run_dir / "15_外部评审与迭代计划.md")
    citation_text = read(run_dir / "citation_final.md")
    workbench_text = read(run_dir / "citation_evidence_workbench.md")
    provenance = read(run_dir / "source_provenance_ledger.md")

    lines = [
        "# Claude 可见外审全证据包",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "- target_lane: Claude Opus / Opus 4.8 Max visible app_session or web_session",
        "",
        "## Claude 专用防循环规则",
        "",
        "- 你正在承担 Claude Opus / Opus 4.8 Max 这一路最终可见审阅；因此 `external_review_passed=no` 或 `claude_opus_review_status=revise/pending` 在你作答前是正常状态。",
        "- 不得仅因 Claude 这一路尚未登记通过、总闸口尚未最终完成、或 `final_user_goal_ready=no` 而判 `REVISE`；这些字段需要用你的本次可见结论来更新。",
        "- 可以因为论文质量、引用锚点、来源元数据、材料-方法不匹配或证据链不足而判 `REVISE`。",
        "- 如果本包内 `final_anchor_ready=yes`、逐条表显示 `citation_level_visible_verified_anchor`、且工作台给出对应来源摘录，你应直接审查这些材料，而不是要求额外文件名。",
        "- CNKI/人大代理来源不要求公共网页可检索；若本包提供合法获取路径、本地全文/hash 台账、页码/位置和来源摘录，可按工作流内可复验材料判断。",
        "- 网络首发 J/OL 文献若尚无正式卷期页码，只要参考文献明确披露网络首发状态、URLID/获取路径、本地全文和待定版页码边界，不得仅因未出版最终页码判 `REVISE`。",
        "- 官方 HTML 来源若正文没有页码引用且参考文献标注无独立页码，不得要求为其补造页码。",
        "- 最终 PASS 必须基于本包内论文全文及证据材料的完整审阅；只审修订差异、引用页码抽查包、登录预检或交接提示，不得给 `safe_to_record_as_final_visible_review_pass=yes`。",
        "",
        "## 当前外审状态说明",
        "",
        f"- external_review_passed_before_this_claude_response: {parse_summary_value(external_text, 'external_review_passed')}",
        f"- claude_opus_review_status_before_this_response: {parse_summary_value(external_text, 'claude_opus_review_status')}",
        f"- gpt_pro_review_status: {parse_summary_value(external_text, 'gpt_pro_review_status')}",
        "- interpretation: if your verdict is PASS and `safe_to_record_as_final_visible_review_pass=yes`, Codex will record this response as the missing Claude lane and then rerun the total gate.",
        "",
        "## 请返回",
        "",
        "```text",
        "verdict: PASS / REVISE",
        "graduate_quality_judgment: ...",
        "citation_anchor_judgment: ...",
        "source_and_metadata_judgment: ...",
        "method_data_fit_judgment: ...",
        "workflow_goal_judgment: ...",
        "must_fix_before_pass: ...",
        "review_scope: full_draft",
        "full_text_reviewed: yes/no",
        "safe_to_record_as_final_visible_review_pass: yes/no",
        "```",
        "",
        "## 最终引用定锚状态摘要",
        "",
        *citation_status_block(citation_text),
        "",
        "说明：以下 `citation_final.md` 和 `citation_evidence_workbench.md` 是本轮 Claude 审阅的实际引用证据层；早期 `citation_page_suggestions.md` 只是关键词候选生成物，不作为最终页码证据，因此不放入本 Claude 全证据包。",
        "",
        "## citation_final.md 原表",
        "",
        "```markdown",
        scrub_paths(citation_text).strip(),
        "```",
        "",
        "## citation_evidence_workbench.md 来源摘录表",
        "",
        "说明：该 workbench 按设计只提供逐条来源摘录和候选复核材料，文件内若出现 `final_anchor_ready=no` 不代表最终定锚失败；最终定锚权威以 `citation_final.md` 的 `final_anchor_ready` 和逐条 `citation_level_visible_verified_anchor` 为准。",
        "",
        "```markdown",
        scrub_paths(workbench_text).strip(),
        "```",
        "",
        "## source_provenance_ledger.md 来源获取与 hash 台账",
        "",
        "```markdown",
        scrub_paths(provenance).strip(),
        "```",
        "",
        "## 网页外审精简包与论文全文",
        "",
        web_packet_text.strip(),
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--citation-out", default="25_引用页码终核包.md")
    parser.add_argument("--review-out", default="26_最终外部评审包.md")
    parser.add_argument("--web-out", default="27_网页外审精简包.md")
    parser.add_argument("--claude-full-out", default="29_Claude可见外审全证据包.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    if not run_dir.exists():
        raise SystemExit(f"run_dir does not exist: {run_dir}")

    citation_packet = build_citation_packet(run_dir)
    citation_out = run_dir / args.citation_out
    citation_out.write_text(citation_packet, encoding="utf-8")

    review_packet = build_review_packet(run_dir, citation_packet)
    review_out = run_dir / args.review_out
    review_out.write_text(review_packet, encoding="utf-8")

    web_packet = build_web_packet(run_dir)
    web_out = run_dir / args.web_out
    web_out.write_text(web_packet, encoding="utf-8")

    claude_full_packet = build_claude_full_packet(run_dir, web_packet, citation_packet)
    claude_full_out = run_dir / args.claude_full_out
    claude_full_out.write_text(claude_full_packet, encoding="utf-8")

    print(f"citation_out={citation_out}")
    print(f"review_out={review_out}")
    print(f"web_out={web_out}")
    print(f"claude_full_out={claude_full_out}")
    print(f"final_anchor_ready={parse_summary_value(read(run_dir / 'citation_final.md'), 'final_anchor_ready')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
