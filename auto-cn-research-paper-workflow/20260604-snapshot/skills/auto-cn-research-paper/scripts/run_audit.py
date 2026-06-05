#!/usr/bin/env python3
"""Audit a Chinese research-paper run directory for evidence readiness."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = [
    "00_运行状态.md",
    "01_选题评分表.md",
    "02_检索日志.md",
    "03_文献矩阵.md",
    "04_优秀论文范式提取.md",
    "05_论证骨架.md",
    "06_论文初稿.md",
    "07_引用与证据审查.md",
    "08_终稿修改清单.md",
    "09_完成度审计.md",
]

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_ID_FREEZE_AUDIT = SCRIPT_DIR / "source_id_freeze_audit.py"


def count_verified_sources(matrix_text: str) -> int:
    count = 0
    for line in matrix_text.splitlines():
        if not line.startswith("| S-"):
            continue
        if "PDF_or_user_exported" in line or "full_text_read" in line:
            count += 1
    return count


def count_public_reprint_sources(matrix_text: str) -> int:
    return sum(1 for line in matrix_text.splitlines() if line.startswith("| S-") and "public_reprint_full_text_read" in line)


def citation_numbers(draft_text: str) -> set[int]:
    found: set[int] = set()
    for match in re.finditer(r"\[(\d+)\]", draft_text):
        found.add(int(match.group(1)))
    return found


def parse_summary_value(text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def parse_boolish(text: str, key: str) -> bool:
    return parse_summary_value(text, key).lower() in {"true", "yes", "1"}


def parse_summary_count(text: str, key: str) -> int:
    match = re.search(rf"{re.escape(key)}:\s*(\d+)", text)
    return int(match.group(1)) if match else 0


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
    missing = []
    for line in ref_lines:
        if "页码待核对" in line or "原刊页码待核对" in line:
            missing.append(line)
            continue
        if page_range.search(line):
            continue
        if "[M]" in line:
            continue
        if "[EB/OL]" in line and ("http" in line or "访问日期" in line):
            continue
        if "[J/OL]" in line and ("URLID" in line or "http" in line or "doi.org" in line):
            continue
        missing.append(line)
    return not missing and "页码待核对" not in refs


def citation_final_ready(text: str) -> bool:
    return "- final_anchor_ready: yes" in text


def citation_working_anchor_ready(text: str) -> bool:
    return "- working_anchor_ready: yes" in text


def source_provenance_ready(text: str) -> bool:
    return "- provenance_ready: yes" in text


def run_source_id_freeze_audit(run_dir: Path) -> tuple[bool, str]:
    completed = subprocess.run(
        [sys.executable, str(SOURCE_ID_FREEZE_AUDIT), str(run_dir)],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return completed.returncode == 0, completed.stdout.strip()


def external_review_gate_issues(text: str, run_dir: Path) -> list[str]:
    issues: list[str] = []
    external_review_passed = parse_summary_value(text, "external_review_passed")
    if external_review_passed != "yes":
        issues.append("external advisor review gate has not passed")

    required = [
        ("claude_opus", "Claude Opus / Opus 4.8 Max"),
        ("gpt_pro", "GPT Pro / GPT-5.5 Pro"),
    ]
    allowed_channels = {"web_session", "app_session"}
    for prefix, label in required:
        status = parse_summary_value(text, f"{prefix}_review_status")
        channel = parse_summary_value(text, f"{prefix}_review_channel")
        review_scope = parse_summary_value(text, f"{prefix}_review_scope")
        raw_record = parse_summary_value(text, f"{prefix}_raw_record")
        review_run_id = parse_summary_value(text, f"{prefix}_review_run_id")
        recorded_at = parse_summary_value(text, f"{prefix}_review_recorded_at")
        real_submission = parse_boolish(text, f"{prefix}_real_submission")

        if status != "pass":
            issues.append(f"{label} review status is not pass: {status}")
        if channel not in allowed_channels:
            issues.append(f"{label} review channel is not a web/app visible session: {channel}")
        if review_scope != "full_draft":
            issues.append(f"{label} review scope is not full_draft: {review_scope}")
        if not real_submission:
            issues.append(f"{label} review does not prove real_submission=true")
        if review_run_id != run_dir.name:
            issues.append(f"{label} review run_id mismatch: {review_run_id} != {run_dir.name}")
        if recorded_at in {"unknown", "", "omitted"}:
            issues.append(f"{label} review recorded_at is missing")
        if raw_record in {"unknown", "", "omitted"} or "omitted" in raw_record:
            issues.append(f"{label} review raw record is missing or omitted")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", help="Run directory to audit.")
    parser.add_argument("--min-fulltext", type=int, default=8, help="Minimum verified full-text sources for a formal paper.")
    parser.add_argument(
        "--require-browser-gate",
        action="store_true",
        help="Require 12_浏览器准入验收.md to prove hands-free browser/database access.",
    )
    parser.add_argument(
        "--require-primary-fulltext",
        action="store_true",
        help="Fail when any formal source is only a public reprint rather than PDF/user-exported/database full text.",
    )
    parser.add_argument(
        "--require-external-review",
        action="store_true",
        help="Require 15_外部评审与迭代计划.md to show both external advisor lanes have passed.",
    )
    parser.add_argument(
        "--require-policy-citation-merged",
        action="store_true",
        help="Require verified official policy sources to be merged into the draft references or formal notes.",
    )
    parser.add_argument(
        "--require-page-numbers",
        action="store_true",
        help="Require reference metadata/page ranges to be complete, with no page-number placeholders.",
    )
    parser.add_argument(
        "--require-source-id-freeze",
        action="store_true",
        help="Require stable S/C source-number freeze checks to pass.",
    )
    parser.add_argument(
        "--require-source-provenance",
        action="store_true",
        help="Require source_provenance_ledger.md to prove verified sources have retrieval/file/hash provenance.",
    )
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    issues: list[str] = []

    for name in REQUIRED_FILES:
        path = run_dir / name
        if not path.exists():
            issues.append(f"missing required file: {name}")

    matrix_path = run_dir / "03_文献矩阵.md"
    draft_path = run_dir / "06_论文初稿.md"
    search_path = run_dir / "02_检索日志.md"
    audit_path = run_dir / "07_引用与证据审查.md"
    queue_path = run_dir / "10_候选下载队列.md"
    evidence_index_path = run_dir / "evidence_index.md"
    citation_plan_path = run_dir / "citation_plan.md"
    citation_page_suggestions_path = run_dir / "citation_page_suggestions.md"
    citation_final_path = run_dir / "citation_final.md"
    source_provenance_path = run_dir / "source_provenance_ledger.md"
    browser_gate_path = run_dir / "12_浏览器准入验收.md"
    external_review_path = run_dir / "15_外部评审与迭代计划.md"
    policy_check_path = run_dir / "14_S008原刊与政策核验记录.md"

    matrix_text = matrix_path.read_text(encoding="utf-8") if matrix_path.exists() else ""
    draft_text = draft_path.read_text(encoding="utf-8") if draft_path.exists() else ""
    search_text = search_path.read_text(encoding="utf-8") if search_path.exists() else ""
    audit_text = audit_path.read_text(encoding="utf-8") if audit_path.exists() else ""
    queue_text = queue_path.read_text(encoding="utf-8") if queue_path.exists() else ""
    evidence_index_text = evidence_index_path.read_text(encoding="utf-8") if evidence_index_path.exists() else ""
    citation_plan_text = citation_plan_path.read_text(encoding="utf-8") if citation_plan_path.exists() else ""
    citation_page_suggestions_text = (
        citation_page_suggestions_path.read_text(encoding="utf-8") if citation_page_suggestions_path.exists() else ""
    )
    citation_final_text = citation_final_path.read_text(encoding="utf-8") if citation_final_path.exists() else ""
    source_provenance_text = source_provenance_path.read_text(encoding="utf-8") if source_provenance_path.exists() else ""
    browser_gate_text = browser_gate_path.read_text(encoding="utf-8") if browser_gate_path.exists() else ""
    external_review_text = external_review_path.read_text(encoding="utf-8") if external_review_path.exists() else ""
    policy_check_text = policy_check_path.read_text(encoding="utf-8") if policy_check_path.exists() else ""
    user_verification_status = parse_summary_value(browser_gate_text, "user_verification_status")
    external_review_passed = parse_summary_value(external_review_text, "external_review_passed")
    claude_review_status = parse_summary_value(external_review_text, "claude_opus_review_status")
    gpt_pro_review_status = parse_summary_value(external_review_text, "gpt_pro_review_status")
    claude_review_scope = parse_summary_value(external_review_text, "claude_opus_review_scope")
    gpt_pro_review_scope = parse_summary_value(external_review_text, "gpt_pro_review_scope")
    policy_ready = policy_citation_merged(draft_text, policy_check_text)
    final_pages_ready = citation_final_ready(citation_final_text)
    working_pages_ready = citation_working_anchor_ready(citation_final_text)
    source_provenance_ok = source_provenance_ready(source_provenance_text)
    manual_verified_anchors = parse_summary_count(citation_final_text, "manual_verified_anchors")
    agent_verified_anchors = parse_summary_count(citation_final_text, "agent_verified_anchors")
    citation_level_verified_anchors = parse_summary_count(citation_final_text, "citation_level_verified_anchors")
    citation_alignment_method = parse_summary_value(citation_final_text, "citation_alignment_method")
    pages_ready = page_numbers_ready(draft_text) and final_pages_ready
    source_id_freeze_ready = "not_required"

    verified = count_verified_sources(matrix_text)
    public_reprints = count_public_reprint_sources(matrix_text)
    if verified < args.min_fulltext:
        issues.append(f"verified full-text sources below target: {verified}/{args.min_fulltext}")
    if args.require_primary_fulltext and public_reprints:
        issues.append(f"public reprint sources require primary PDF/database verification: {public_reprints}")

    if "libproxy.ruc.edu.cn" not in search_text and "人大图书馆" not in search_text:
        issues.append("search log does not prove RUC library proxy route")

    citations = citation_numbers(draft_text)
    if citations and max(citations) > verified:
        issues.append(f"draft cites [{max(citations)}] but only {verified} verified sources are counted")

    if "未发现" not in audit_text and "must_fix" not in audit_text:
        issues.append("citation/evidence audit appears incomplete")

    if verified and not evidence_index_text:
        issues.append("evidence_index.md is missing for page/location checks")
    elif verified and "source_count:" not in evidence_index_text:
        issues.append("evidence_index.md does not contain source_count")

    if citations and not citation_plan_text:
        issues.append("citation_plan.md is missing for draft citation mapping")
    elif citations and "missing_citation_sources: 0" not in citation_plan_text:
        issues.append("citation_plan.md does not prove all draft citations map to sources")

    if citations and not citation_page_suggestions_text:
        issues.append("citation_page_suggestions.md is missing for page-candidate checks")
    elif citations and "missing_page_suggestions: 0" not in citation_page_suggestions_text:
        issues.append("citation_page_suggestions.md does not prove all body citations have page candidates")

    if args.require_page_numbers:
        if citations and not citation_final_text:
            issues.append("citation_final.md is missing for final citation anchoring")
        elif citations and not final_pages_ready:
            issues.append("citation_final.md does not prove all body citations have final anchors")
        if working_pages_ready and not final_pages_ready:
            issues.append("citation_final.md only has keyword-derived working anchors; citation-level page verification is still required")

    if args.require_browser_gate:
        if not browser_gate_text:
            issues.append("browser access gate report is missing: 12_浏览器准入验收.md")
        elif "- hands_free_ready: yes" not in browser_gate_text:
            issues.append("browser access gate does not prove hands-free RUC/CNKI automation")

    if args.require_external_review:
        if not external_review_text:
            issues.append("external review report is missing: 15_外部评审与迭代计划.md")
        else:
            issues.extend(external_review_gate_issues(external_review_text, run_dir))

    if args.require_policy_citation_merged and not policy_ready:
        issues.append("verified official policy source has not been merged into formal draft references/notes")

    if args.require_page_numbers and not pages_ready:
        issues.append("reference page ranges or page-number placeholders are still incomplete")

    if args.require_source_id_freeze:
        freeze_passed, freeze_output = run_source_id_freeze_audit(run_dir)
        source_id_freeze_ready = "yes" if freeze_passed else "no"
        if not freeze_passed:
            issues.append("source ID freeze audit has not passed")
            for line in freeze_output.splitlines():
                if line.startswith("- "):
                    issues.append(line.removeprefix("- ").strip())

    if args.require_source_provenance:
        if not source_provenance_text:
            issues.append("source provenance ledger is missing: source_provenance_ledger.md")
        elif not source_provenance_ok:
            issues.append("source provenance ledger is incomplete or invalid")

    if verified < args.min_fulltext and queue_text:
        if user_verification_status == "waiting_user" or (
            user_verification_status == "unknown"
            and any(term in queue_text for term in ["拼图", "验证码", "滑块", "安全验证", "SSO", "身份确认"])
        ):
            issues.append("candidate queue is waiting for user verification before more downloads")
        if browser_gate_text and "- hands_free_ready: no" in browser_gate_text:
            issues.append("browser access gate is not hands-free ready for additional downloads")
        if "| C-" in queue_text:
            issues.append("candidate queue has pending sources to try after browser recovery or verification")

    status = "PASS" if not issues else "INCOMPLETE"
    print(f"status={status}")
    print(f"verified_fulltext={verified}")
    print(f"public_reprint_fulltext={public_reprints}")
    print(f"external_review_passed={external_review_passed}")
    print(f"claude_opus_review_status={claude_review_status}")
    print(f"claude_opus_review_scope={claude_review_scope}")
    print(f"gpt_pro_review_status={gpt_pro_review_status}")
    print(f"gpt_pro_review_scope={gpt_pro_review_scope}")
    print(f"policy_citation_merged={'yes' if policy_ready else 'no'}")
    print(f"working_anchor_ready={'yes' if working_pages_ready else 'no'}")
    print(f"manual_verified_anchors={manual_verified_anchors}")
    print(f"agent_verified_anchors={agent_verified_anchors}")
    print(f"citation_level_verified_anchors={citation_level_verified_anchors}")
    print(f"citation_alignment_method={citation_alignment_method}")
    print(f"citation_final_ready={'yes' if final_pages_ready else 'no'}")
    print(f"page_numbers_ready={'yes' if pages_ready else 'no'}")
    print(f"source_id_freeze_ready={source_id_freeze_ready}")
    print(f"source_provenance_ready={'yes' if source_provenance_ok else 'no'}")
    for issue in issues:
        print(f"- {issue}")

    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
