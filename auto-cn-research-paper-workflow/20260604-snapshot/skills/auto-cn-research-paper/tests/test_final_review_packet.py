#!/usr/bin/env python3
"""Regression tests for visible final-review prompt packet generation."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "final_review_packet.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def make_run_dir() -> Path:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-final-review-packet-"))
    (run_dir / "06_论文初稿.md").write_text("# 论文初稿\n\n正文[1]\n", encoding="utf-8")
    (run_dir / "15_外部评审与迭代计划.md").write_text(
        "\n".join(
            [
                "# 外部评审与迭代计划",
                "",
                "- external_review_passed: no",
                "- claude_opus_review_status: revise",
                "- gpt_pro_review_status: real_call_pending",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "16_总闸口矩阵.md").write_text(
        "\n".join(
            [
                "# 自动科研流总闸口矩阵",
                "",
                "- final_user_goal_ready: no",
                "",
                "| Gate | 状态 |",
                "| --- | --- |",
                "| 页码层 | INCOMPLETE |",
                "| 外部评审层 | INCOMPLETE |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_final.md").write_text(
        "\n".join(
            [
                "# Citation Final Anchors",
                "",
                "| No. | Ref | Source | Anchor | Verified | Status | Note | Context |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |",
                "| 1 | [1] | S-001 | p.1 | no | anchored_from_evidence_index | 工作锚点 | 正文[1] |",
                "",
                "- body_citation_occurrences: 1",
                "- anchored_citations: 1",
                "- working_anchor_ready: yes",
                "- citation_level_verified_anchors: 0",
                "- citation_alignment_method: keyword_candidate_evidence_index",
                "- final_anchor_ready: no",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_evidence_workbench.md").write_text(
        "\n".join(
            [
                "# Citation Evidence Workbench",
                "",
                "- body_citation_occurrences: 1",
                "- rows_with_source_excerpt: 1",
                "- missing_source_text: 0",
                "- missing_excerpt: 0",
                "- citation_level_verified_anchors: 0",
                "- final_anchor_ready: no",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return run_dir


def test_packet_blocks_final_pass_when_anchors_are_not_final() -> None:
    run_dir = make_run_dir()

    result = run_script([str(run_dir)])

    assert result.returncode == 0, result.stdout
    citation_packet = (run_dir / "25_引用页码终核包.md").read_text(encoding="utf-8")
    review_packet = (run_dir / "26_最终外部评审包.md").read_text(encoding="utf-8")
    web_packet = (run_dir / "27_网页外审精简包.md").read_text(encoding="utf-8")
    claude_full_packet = (run_dir / "29_Claude可见外审全证据包.md").read_text(encoding="utf-8")
    assert "- final_anchor_ready: no" in citation_packet
    assert "工作锚点不能视为最终页码" in citation_packet
    assert "如果 `final_anchor_ready` 不是 `yes`，不得给出 `PASS`" in review_packet
    assert "只审修订差异、引用页码抽查包、登录预检或交接提示" in review_packet
    assert "不得仅因该 lane 尚未登记通过" in review_packet
    assert "研究生课程论文/机制性二次分析" in review_packet
    assert "review_scope: full_draft" in review_packet
    assert "full_text_reviewed: yes/no" in review_packet
    assert "timestamp_note: generated_at uses UTC" in web_packet
    assert "不得仅因论文诚实声明无一手访谈" in web_packet
    assert "授权数据库来源不要求公开 URL" in web_packet
    assert "review_scope: full_draft" in web_packet
    assert "verdict: PASS / REVISE" in review_packet
    assert "GPT Pro / GPT-5.5 Pro" in review_packet
    assert "## 论文全文" in web_packet
    assert "正文[1]" in web_packet
    assert "引用逐条表见 `25_引用页码终核包.md`" in web_packet
    assert "citation_evidence_workbench.md" in web_packet
    assert "- rows_with_source_excerpt: 1" in web_packet
    assert "workbench_role: excerpt review table only" in web_packet
    assert "workbench_final_anchor_ready" not in web_packet
    assert "Claude 专用防循环规则" in claude_full_packet
    assert "citation_evidence_workbench.md 来源摘录表" in claude_full_packet
    assert "source_provenance_ledger.md 来源获取与 hash 台账" in claude_full_packet
    assert "网络首发 J/OL 文献若尚无正式卷期页码" in claude_full_packet
    assert "if your verdict is PASS" in claude_full_packet
    assert "review_scope: full_draft" in claude_full_packet
    assert "早期 `citation_page_suggestions.md` 只是关键词候选生成物" in claude_full_packet
    assert "## citation_page_suggestions.md 页码候选来源" not in claude_full_packet


def main() -> int:
    tests = [test_packet_blocks_final_pass_when_anchors_are_not_final]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_packet_blocks_final_pass_when_anchors_are_not_final")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
