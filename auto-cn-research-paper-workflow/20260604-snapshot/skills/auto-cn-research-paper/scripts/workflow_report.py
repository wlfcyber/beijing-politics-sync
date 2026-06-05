#!/usr/bin/env python3
"""Create a one-page workflow status report for a research-paper run."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CAPTCHA_TERMS = ["拼图", "验证码", "滑块", "SSO", "身份确认", "安全验证"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def count_verified_sources(matrix_text: str) -> int:
    return sum(
        1
        for line in matrix_text.splitlines()
        if line.startswith("| S-") and ("PDF_or_user_exported" in line or "full_text_read" in line)
    )


def count_public_fulltext_sources(matrix_text: str) -> int:
    return sum(1 for line in matrix_text.splitlines() if line.startswith("| S-") and "public_reprint_full_text_read" in line)


def parse_summary_count(text: str, key: str) -> int:
    match = re.search(rf"{re.escape(key)}:\s*(\d+)", text)
    return int(match.group(1)) if match else 0


def parse_summary_value(text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def parse_boolish(text: str, key: str) -> bool:
    return parse_summary_value(text, key).lower() in {"true", "yes", "1"}


def external_review_gate_passed(text: str, run_dir: Path) -> bool:
    if parse_summary_value(text, "external_review_passed") != "yes":
        return False
    for prefix in ["claude_opus", "gpt_pro"]:
        if parse_summary_value(text, f"{prefix}_review_status") != "pass":
            return False
        if parse_summary_value(text, f"{prefix}_review_channel") not in {"web_session", "app_session"}:
            return False
        if parse_summary_value(text, f"{prefix}_review_scope") != "full_draft":
            return False
        if not parse_boolish(text, f"{prefix}_real_submission"):
            return False
        if parse_summary_value(text, f"{prefix}_review_run_id") != run_dir.name:
            return False
        if parse_summary_value(text, f"{prefix}_review_recorded_at") in {"unknown", "", "omitted"}:
            return False
        raw_record = parse_summary_value(text, f"{prefix}_raw_record")
        if raw_record in {"unknown", "", "omitted"} or "omitted" in raw_record:
            return False
    return True


def parse_queue_rows(text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| C-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 6:
            if "->" in cells[0] or "无需继续下载" in cells[-1] or "已进入正式文献矩阵" in line:
                continue
            rows.append((cells[0], cells[1], cells[-1]))
    return rows


def references_section(draft_text: str) -> str:
    parts = re.split(r"^##\s*参考文献\s*$", draft_text, flags=re.MULTILINE)
    return parts[-1] if len(parts) > 1 else ""


def policy_citation_merged(draft_text: str, policy_text: str) -> bool:
    policy_title = "政务移动互联网应用程序规范化管理办法"
    if policy_title not in policy_text:
        return True
    refs = references_section(draft_text)
    return policy_title in draft_text and (policy_title in refs or "国办函〔2026〕12号" in refs or "国办函[2026]12号" in refs)


def page_numbers_ready(draft_text: str) -> bool:
    refs = references_section(draft_text)
    ref_lines = [line.strip() for line in refs.splitlines() if re.match(r"^\[\d+\]", line.strip())]
    if not ref_lines:
        return False
    page_range = re.compile(r"[:：]\s*\d+\s*[-–—]\s*\d+")
    for line in ref_lines:
        if "页码待核对" in line or "原刊页码待核对" in line:
            return False
        if page_range.search(line):
            continue
        if "[M]" in line:
            continue
        if "[EB/OL]" in line and ("http" in line or "访问日期" in line):
            continue
        if "[J/OL]" in line and ("URLID" in line or "http" in line or "doi.org" in line):
            continue
        return False
    return True


def final_anchor_ready(text: str) -> bool:
    return "- final_anchor_ready: yes" in text


def working_anchor_ready(text: str) -> bool:
    return "- working_anchor_ready: yes" in text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--target-fulltext", type=int, default=8)
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/workflow_status.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve() if args.out else run_dir / "workflow_status.md"

    matrix_text = read(run_dir / "03_文献矩阵.md")
    draft_text = read(run_dir / "06_论文初稿.md")
    inventory_text = read(run_dir / "source_inventory.md")
    evidence_text = read(run_dir / "evidence_index.md")
    citation_plan_text = read(run_dir / "citation_plan.md")
    citation_page_suggestions_text = read(run_dir / "citation_page_suggestions.md")
    citation_final_text = read(run_dir / "citation_final.md")
    browser_gate_text = read(run_dir / "12_浏览器准入验收.md")
    external_review_text = read(run_dir / "15_外部评审与迭代计划.md")
    policy_check_text = read(run_dir / "14_S008原刊与政策核验记录.md")
    queue_text = read(run_dir / "10_候选下载队列.md")
    audit_text = read(run_dir / "09_完成度审计.md")
    resume_card_text = read(run_dir / "11_断点续跑操作卡.md")

    verified = count_verified_sources(matrix_text)
    public_fulltext = count_public_fulltext_sources(matrix_text)
    primary_fulltext_ready = public_fulltext == 0
    usable_inventory = parse_summary_count(inventory_text, "usable_fulltext")
    incomplete_inventory = parse_summary_count(inventory_text, "candidate_or_incomplete")
    evidence_sources = parse_summary_count(evidence_text, "source_count")
    citation_occurrences = parse_summary_count(citation_plan_text, "citation_occurrences")
    missing_citation_sources = parse_summary_count(citation_plan_text, "missing_citation_sources")
    body_citation_occurrences = parse_summary_count(citation_page_suggestions_text, "body_citation_occurrences")
    missing_page_suggestions = parse_summary_count(citation_page_suggestions_text, "missing_page_suggestions")
    anchored_citations = parse_summary_count(citation_final_text, "anchored_citations")
    blocked_public_reprint_citations = parse_summary_count(citation_final_text, "blocked_public_reprint_citations")
    needs_manual_anchor = parse_summary_count(citation_final_text, "needs_manual_anchor")
    manual_verified_anchors = parse_summary_count(citation_final_text, "manual_verified_anchors")
    agent_verified_anchors = parse_summary_count(citation_final_text, "agent_verified_anchors")
    citation_level_verified_anchors = parse_summary_count(citation_final_text, "citation_level_verified_anchors")
    citation_working_anchor_ready = working_anchor_ready(citation_final_text)
    citation_alignment_method = parse_summary_value(citation_final_text, "citation_alignment_method")
    citation_alignment_scope = parse_summary_value(citation_final_text, "citation_alignment_scope")
    citation_final_ready = final_anchor_ready(citation_final_text)
    hands_free_ready = parse_summary_value(browser_gate_text, "hands_free_ready")
    browser_path_status = parse_summary_value(browser_gate_text, "browser_path_status")
    current_url_status = parse_summary_value(browser_gate_text, "current_url_status")
    computer_use_status = parse_summary_value(browser_gate_text, "computer_use_status")
    user_verification_status = parse_summary_value(browser_gate_text, "user_verification_status")
    external_review_passed = "yes" if external_review_gate_passed(external_review_text, run_dir) else "no"
    claude_review_status = parse_summary_value(external_review_text, "claude_opus_review_status")
    if claude_review_status == "unknown":
        claude_review_status = "not_run"
    gpt_pro_review_status = parse_summary_value(external_review_text, "gpt_pro_review_status")
    if gpt_pro_review_status == "unknown":
        gpt_pro_review_status = "not_run"
    policy_ready = policy_citation_merged(draft_text, policy_check_text)
    pages_ready = page_numbers_ready(draft_text) and citation_final_ready
    waiting_user_scan = any(term in queue_text or term in audit_text for term in CAPTCHA_TERMS)
    human_in_the_loop_required = "human_in_the_loop_required" in resume_card_text or any(
        term in resume_card_text for term in CAPTCHA_TERMS
    )
    waiting_user = user_verification_status == "waiting_user" if user_verification_status != "unknown" else waiting_user_scan
    remaining = max(args.target_fulltext - verified, 0)
    queue_rows = parse_queue_rows(queue_text)
    next_rows = queue_rows[:remaining] if remaining else []
    paper_material_ready = remaining == 0 and evidence_sources >= verified and not waiting_user
    hands_free_workflow_ready = paper_material_ready and hands_free_ready == "yes" and external_review_passed == "yes"
    formal_ready = hands_free_workflow_ready

    lines = [
        "# 自动科研流状态报告",
        "",
        "## 结论",
        "",
        f"- formal_ready: {'yes' if formal_ready else 'no'}",
        f"- paper_material_ready: {'yes' if paper_material_ready else 'no'}",
        f"- primary_fulltext_ready: {'yes' if primary_fulltext_ready else 'no'}",
        f"- hands_free_workflow_ready: {'yes' if hands_free_workflow_ready else 'no'}",
        f"- verified_fulltext: {verified}/{args.target_fulltext}",
        f"- usable_fulltext_inventory: {usable_inventory}",
        f"- public_reprint_fulltext: {public_fulltext}",
        f"- candidate_or_incomplete: {incomplete_inventory}",
        f"- evidence_index_sources: {evidence_sources}",
        f"- citation_occurrences: {citation_occurrences}",
        f"- missing_citation_sources: {missing_citation_sources}",
        f"- body_citation_occurrences: {body_citation_occurrences}",
        f"- missing_page_suggestions: {missing_page_suggestions}",
        f"- anchored_citations: {anchored_citations}",
        f"- blocked_public_reprint_citations: {blocked_public_reprint_citations}",
        f"- needs_manual_anchor: {needs_manual_anchor}",
        f"- working_anchor_ready: {'yes' if citation_working_anchor_ready else 'no'}",
        f"- manual_verified_anchors: {manual_verified_anchors}",
        f"- agent_verified_anchors: {agent_verified_anchors}",
        f"- citation_level_verified_anchors: {citation_level_verified_anchors}",
        f"- citation_alignment_method: {citation_alignment_method}",
        f"- citation_alignment_scope: {citation_alignment_scope}",
        f"- citation_final_ready: {'yes' if citation_final_ready else 'no'}",
        f"- browser_hands_free_ready: {hands_free_ready}",
        f"- browser_path_status: {browser_path_status}",
        f"- current_url_status: {current_url_status}",
        f"- computer_use_status: {computer_use_status}",
        f"- user_verification_status: {user_verification_status}",
        f"- human_in_the_loop_required: {'yes' if human_in_the_loop_required else 'no'}",
        f"- waiting_user_verification: {'yes' if waiting_user else 'no'}",
        f"- external_review_passed: {external_review_passed}",
        f"- claude_opus_review_status: {claude_review_status}",
        f"- gpt_pro_review_status: {gpt_pro_review_status}",
        f"- policy_citation_merged: {'yes' if policy_ready else 'no'}",
        f"- page_numbers_ready: {'yes' if pages_ready else 'no'}",
        "",
        "## 当前判断",
        "",
    ]

    if paper_material_ready:
        lines.append("当前证据满足正式研究生课程论文的默认全文数量与证据索引门槛。仍需按学校格式做最终人工格式确认。")
    else:
        if remaining:
            lines.append(f"当前距离默认正式门槛还差 {remaining} 篇可读全文。")
        if waiting_user:
            lines.append("当前候选队列或审计记录显示仍等待用户本人完成知网拼图/验证码/身份确认后续跑。")
        if evidence_sources < verified:
            lines.append("页码/位置证据索引未覆盖全部已核验全文。")
        if citation_occurrences and missing_citation_sources:
            lines.append(f"仍有 {missing_citation_sources} 个正文引用编号未映射到已核验来源。")
        elif not citation_occurrences:
            lines.append("尚未生成或识别正文引用映射计划。")
        if body_citation_occurrences and missing_page_suggestions:
            lines.append(f"仍有 {missing_page_suggestions} 个正文引用缺少页码候选。")
        elif not body_citation_occurrences:
            lines.append("尚未生成正文引用页码建议表。")
        if citation_occurrences and not citation_final_ready:
            lines.append("正文引用仍未全部进入终稿定锚状态。")
    if hands_free_ready != "yes":
        lines.append("浏览器准入验收尚未通过，因此不能声称当前数据库检索/下载链路已经达到彻底解放双手。")
    if external_review_passed != "yes":
        lines.append("外部强模型双评审尚未通过，因此不能声称当前论文与自动科研流达到最终验收标准。")
    if not primary_fulltext_ready:
        lines.append(f"当前有 {public_fulltext} 篇正式来源为公开转载全文，正式提交前应优先核对原刊、数据库全文或 PDF 页码。")
    if not policy_ready:
        lines.append("已核验的政策原文尚未进入正式参考文献或脚注，正式稿仍需补齐。")
    if not pages_ready:
        lines.append("参考文献页码或页码占位仍未补齐，不能按正式提交标准验收。")
    if citation_working_anchor_ready and not citation_final_ready:
        lines.append("正文引用目前只有关键词候选页形成的工作锚点，尚不是逐条引文-原文页码核验后的最终锚点。")
    if blocked_public_reprint_citations:
        lines.append(f"当前有 {blocked_public_reprint_citations} 处正文引用因公开转载来源未升级而不能生成正式页码。")
    if needs_manual_anchor:
        lines.append(f"当前有 {needs_manual_anchor} 处正文引用仍需人工定锚。")

    lines.extend(["", "## 下一步候选", ""])
    if next_rows:
        lines.append("| 编号 | 题名 | 下一步 |")
        lines.append("| --- | --- | --- |")
        for cid, title, next_step in next_rows:
            lines.append(f"| {cid} | {title} | {next_step} |")
    else:
        lines.append("无待补候选，或候选队列尚未建立。")

    lines.extend(
        [
            "",
            "## 证据文件",
            "",
            f"- 文献矩阵：`{run_dir / '03_文献矩阵.md'}`",
            f"- 下载清单：`{run_dir / 'source_inventory.md'}`",
            f"- KDH/CAJ 转换清单：`{run_dir / 'kdh_caj_conversion_manifest.md'}`",
            f"- 转换全文提取清单：`{run_dir / 'fulltext_manifest_converted_caj.md'}`",
            f"- 页码/位置索引：`{run_dir / 'evidence_index.md'}`",
            f"- 引用映射计划：`{run_dir / 'citation_plan.md'}`",
            f"- 正文引用页码建议：`{run_dir / 'citation_page_suggestions.md'}`",
            f"- 正文引用终稿定锚：`{run_dir / 'citation_final.md'}`",
            f"- 浏览器准入验收：`{run_dir / '12_浏览器准入验收.md'}`",
            f"- 浏览器恢复尝试记录：`{run_dir / '13_浏览器恢复尝试记录.md'}`",
            f"- S-008 原刊与政策核验：`{run_dir / '14_S008原刊与政策核验记录.md'}`",
            f"- 外部评审与迭代计划：`{run_dir / '15_外部评审与迭代计划.md'}`",
            f"- 总闸口矩阵：`{run_dir / '16_总闸口矩阵.md'}`",
            f"- 外部评审修订单：`{run_dir / '17_外部评审修订单.md'}`",
            f"- 候选队列：`{run_dir / '10_候选下载队列.md'}`",
            f"- 完成度审计：`{run_dir / '09_完成度审计.md'}`",
        ]
    )

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"formal_ready={'yes' if formal_ready else 'no'}")
    print(f"paper_material_ready={'yes' if paper_material_ready else 'no'}")
    print(f"primary_fulltext_ready={'yes' if primary_fulltext_ready else 'no'}")
    print(f"hands_free_workflow_ready={'yes' if hands_free_workflow_ready else 'no'}")
    print(f"verified_fulltext={verified}/{args.target_fulltext}")
    print(f"remaining_fulltext={remaining}")
    print(f"waiting_user_verification={'yes' if waiting_user else 'no'}")
    print(f"external_review_passed={external_review_passed}")
    print(f"policy_citation_merged={'yes' if policy_ready else 'no'}")
    print(f"working_anchor_ready={'yes' if citation_working_anchor_ready else 'no'}")
    print(f"manual_verified_anchors={manual_verified_anchors}")
    print(f"agent_verified_anchors={agent_verified_anchors}")
    print(f"citation_level_verified_anchors={citation_level_verified_anchors}")
    print(f"citation_alignment_method={citation_alignment_method}")
    print(f"citation_final_ready={'yes' if citation_final_ready else 'no'}")
    print(f"page_numbers_ready={'yes' if pages_ready else 'no'}")
    print(f"out={out_path}")
    return 0 if formal_ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
