#!/usr/bin/env python3
"""Regression tests for citation evidence workbench generation."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "citation_evidence_workbench.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_workbench_extracts_source_snippet_without_finalizing_anchor() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-citation-workbench-"))
    text_dir = temp / "texts"
    text_dir.mkdir()
    source_text = text_dir / "li_yonghong_digital_formalism.txt"
    source_text.write_text(
        "===== PAGE 1 =====\n"
        "无关内容\n"
        "===== PAGE 2 =====\n"
        "数字形式主义表现为痕迹管理异化、绩效评价唯数据化和治理逻辑算法化。\n",
        encoding="utf-8",
    )
    run_dir = temp / "run"
    run_dir.mkdir()
    (run_dir / "03_文献矩阵.md").write_text(
        "\n".join(
            [
                "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                "| S-001 | PDF_or_user_exported；full_text_read | 李永洪 | 2026 | 树立和践行正确政绩观 破解乡村治理中的数字形式主义 | 测试期刊 | 乡村治理 | 文献分析 | 数字形式主义表现 | 局限 | 支撑表征 | DOI |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "06_论文初稿.md").write_text("正文说痕迹管理异化和绩效评价唯数据化[1]。\n", encoding="utf-8")
    (run_dir / "evidence_index.md").write_text(
        "\n".join(
            [
                "| Source text | Pages | Characters | Top evidence locations |",
                "| --- | --- | --- | --- |",
                f"| `{source_text}` | 2 | 80 | 数字形式主义: p.2 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_page_suggestions.md").write_text(
        "\n".join(
            [
                "| No. | Ref | Source | Suggested pages | Confidence | Context |",
                "| --- | --- | --- | --- | --- | --- |",
                "| 1 | [1] | S-001 | 数字形式主义: 2; 痕迹: 2; 考核: 2 | candidate | 正文说痕迹管理异化和绩效评价唯数据化[1]。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(run_dir)])

    assert result.returncode == 0, result.stdout
    out = (run_dir / "citation_evidence_workbench.md").read_text(encoding="utf-8")
    assert "p.2" in out
    assert "痕迹管理异化" in out
    assert "needs_human_or_visible_advisor_verification" in out
    assert "- citation_level_verified_anchors: 0" in out
    assert "- final_anchor_ready: no" in out


def test_workbench_verified_mode_promotes_visible_reviewed_rows() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-citation-workbench-verified-"))
    run_dir = temp / "run"
    run_dir.mkdir()
    (run_dir / "03_文献矩阵.md").write_text(
        "\n".join(
            [
                "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                "| S-001 | PDF_or_user_exported；full_text_read | 李永洪 | 2026 | 树立和践行正确政绩观 破解乡村治理中的数字形式主义 | 测试期刊 | 乡村治理 | 文献分析 | 数字形式主义表现 | 局限 | 支撑表征 | DOI |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "evidence_index.md").write_text("", encoding="utf-8")
    (run_dir / "citation_page_suggestions.md").write_text(
        "\n".join(
            [
                "| No. | Ref | Source | Suggested pages | Confidence | Context |",
                "| --- | --- | --- | --- | --- | --- |",
                "| 1 | [1] | S-001 | 数字形式主义: 2 | candidate | 正文[1]。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_evidence_overrides.md").write_text(
        "\n".join(
            [
                "| No. | Candidate page | Status | Source-page excerpt |",
                "| --- | --- | --- | --- |",
                "| 1 | p.2 | visible_advisor_repair_candidate | 原文摘录支撑正文断言。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(run_dir), "--verified-citation-pages"])

    assert result.returncode == 0, result.stdout
    out = (run_dir / "citation_evidence_workbench.md").read_text(encoding="utf-8")
    assert "citation_level_visible_verified_anchor" in out
    assert "- citation_level_verified_anchors: 1" in out
    assert "- final_anchor_ready: yes" in out


def test_workbench_prefers_body_page_over_reference_page() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-citation-workbench-ref-"))
    text_dir = temp / "texts"
    text_dir.mkdir()
    source_text = text_dir / "smart_code_platform.txt"
    source_text.write_text(
        "===== PAGE 5 =====\n"
        "标准化平台通过分类和流程改造治理对象，使街面治理事项被工单化和报表化。\n"
        "===== PAGE 9 =====\n"
        "参考文献 References Administrative exclusion through information architecture.\n",
        encoding="utf-8",
    )
    run_dir = temp / "run"
    run_dir.mkdir()
    (run_dir / "03_文献矩阵.md").write_text(
        "\n".join(
            [
                "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                "| S-012 | PDF_or_user_exported；full_text_read | 李春生 | 2023 | 城市基层数字平台的悬浮化及其发生逻辑——基于C镇“智能码”平台的观察 | 城市问题 | C镇 | 案例 | 平台悬浮 | 单案例 | 平台化 | DOI |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "evidence_index.md").write_text(
        "\n".join(
            [
                "| Source text | Pages | Characters | Top evidence locations |",
                "| --- | --- | --- | --- |",
                f"| `{source_text}` | 2 | 80 | 平台: p.5; administrative: p.9 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_page_suggestions.md").write_text(
        "\n".join(
            [
                "| No. | Ref | Source | Suggested pages | Confidence | Context |",
                "| --- | --- | --- | --- | --- | --- |",
                "| 1 | [12] | S-012 | 平台: 5; administrative: 9 | candidate | 标准化平台如何通过分类和流程改造治理对象[12]。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(run_dir)])

    assert result.returncode == 0, result.stdout
    out = (run_dir / "citation_evidence_workbench.md").read_text(encoding="utf-8")
    assert "| 1 | [12] | S-012 | p.5 |" in out
    assert "分类和流程改造治理对象" in out


def test_workbench_prefers_body_page_over_abstract_candidate() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-citation-workbench-abstract-"))
    text_dir = temp / "texts"
    text_dir.mkdir()
    source_text = text_dir / "rural_digital_formalism.txt"
    source_text.write_text(
        "===== PAGE 1 =====\n"
        "题目：数字乡村建设形式主义的生成机理与治理策略\n"
        "作者简介：测试作者。\n"
        "摘要：本文提到碎片化协作、选择性行动、替代性服务、重复性开发。\n"
        "关键词：数字乡村；形式主义\n"
        "===== PAGE 4 =====\n"
        "（一）数字乡村建设形式主义的类型表现。本文将这些现象凝练为碎片化协作、选择性行动、替代性服务以及重复性开发等类型。"
        "碎片化协作指治理主体因权力分散、资源配置失衡而忽视业务服务一体化。\n",
        encoding="utf-8",
    )
    run_dir = temp / "run"
    run_dir.mkdir()
    (run_dir / "03_文献矩阵.md").write_text(
        "\n".join(
            [
                "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                "| S-005 | PDF_or_user_exported；full_text_read | 沈费伟 | 2026 | 数字乡村建设形式主义的生成机理与治理策略 | 天津行政学院学报 | 数字乡村 | 类型划分 | 四类表现 | 局限 | 支撑类型 | DOI |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "evidence_index.md").write_text(
        "\n".join(
            [
                "| Source text | Pages | Characters | Top evidence locations |",
                "| --- | --- | --- | --- |",
                f"| `{source_text}` | 2 | 120 | 碎片化协作: p.1; 选择性行动: p.1 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_page_suggestions.md").write_text(
        "\n".join(
            [
                "| No. | Ref | Source | Suggested pages | Confidence | Context |",
                "| --- | --- | --- | --- | --- | --- |",
                "| 1 | [5] | S-005 | 碎片化协作: 1; 选择性行动: 1 | candidate | 数字乡村建设形式主义研究讨论碎片化协作、选择性行动、替代性服务和重复性开发等类型[5]。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(run_dir)])

    assert result.returncode == 0, result.stdout
    out = (run_dir / "citation_evidence_workbench.md").read_text(encoding="utf-8")
    assert "| 1 | [5] | S-005 | p.4 |" in out
    assert "数字乡村建设形式主义的类型表现" in out


def test_workbench_prefers_page_with_later_context_core_phrase() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-citation-workbench-core-"))
    text_dir = temp / "texts"
    text_dir.mkdir()
    source_text = text_dir / "attention_competition.txt"
    source_text.write_text(
        "===== PAGE 2 =====\n"
        "基层数字形式主义是信息技术进入基层治理场域后出现的负面现象，本页只作概念铺垫。\n"
        "===== PAGE 5 =====\n"
        "在强竞争和高关注情境中，乡村为在高压横向博弈中求生存、争优势，会主动实施以提升数字能见度为核心的创造生产行为。"
        "乡村治理主体围绕上级注意力主动生产数字符号，以争取认可和竞争优势。\n",
        encoding="utf-8",
    )
    run_dir = temp / "run"
    run_dir.mkdir()
    (run_dir / "03_文献矩阵.md").write_text(
        "\n".join(
            [
                "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                "| S-006 | PDF_or_user_exported；full_text_read | 武小龙 | 2026 | 为注意力而生产 | 天津行政学院学报 | 注意力竞争 | 理论建构 | 主动生产 | 局限 | 支撑主动型形式主义 | DOI |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "evidence_index.md").write_text(
        "\n".join(
            [
                "| Source text | Pages | Characters | Top evidence locations |",
                "| --- | --- | --- | --- |",
                f"| `{source_text}` | 2 | 120 | 基层数字形式主义: p.2; 注意力: p.5 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_page_suggestions.md").write_text(
        "\n".join(
            [
                "| No. | Ref | Source | Suggested pages | Confidence | Context |",
                "| --- | --- | --- | --- | --- | --- |",
                "| 1 | [6] | S-006 | 基层数字形式主义: 2 | candidate | 武小龙、曾颖关于注意力竞争的研究显示，基层行动者会围绕上级注意力主动生产数字符号，以争取认可和竞争优势[6]。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(run_dir)])

    assert result.returncode == 0, result.stdout
    out = (run_dir / "citation_evidence_workbench.md").read_text(encoding="utf-8")
    assert "| 1 | [6] | S-006 | p.5 |" in out
    assert "主动生产数字符号" in out


def test_workbench_uses_visible_review_override_rows() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-citation-workbench-override-"))
    text_dir = temp / "texts"
    text_dir.mkdir()
    source_text = text_dir / "risk_discretion.txt"
    source_text.write_text(
        "===== PAGE 7 =====\n"
        "问责机制介入低中高，数字化技术介入低中高，乡镇干部行动倾向变化。\n"
        "===== PAGE 15 =====\n"
        "问责机制介入程度会导致政策风险变化，数字化技术介入程度会影响乡镇干部的政策决策空间。"
        "乡镇干部基于技术治理的风险性与自由裁量权考量采取不同策略。\n",
        encoding="utf-8",
    )
    run_dir = temp / "run"
    run_dir.mkdir()
    (run_dir / "03_文献矩阵.md").write_text(
        "\n".join(
            [
                "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                "| S-010 | PDF_or_user_exported；full_text_read | 傅利平 | 2021 | 技术治理何以影响乡镇干部行动 | 公共行政评论 | X市 | 过程分析 | 风险与裁量 | 局限 | 支撑机制 | DOI |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "evidence_index.md").write_text(
        "\n".join(
            [
                "| Source text | Pages | Characters | Top evidence locations |",
                "| --- | --- | --- | --- |",
                f"| `{source_text}` | 2 | 120 | 问责机制: p.7 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_page_suggestions.md").write_text(
        "\n".join(
            [
                "| No. | Ref | Source | Suggested pages | Confidence | Context |",
                "| --- | --- | --- | --- | --- | --- |",
                "| 6 | [10] | S-010 | 问责机制: 7 | candidate | 基层干部行动选择会随风险和裁量空间变化而变化[10]。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (run_dir / "citation_evidence_overrides.md").write_text(
        "\n".join(
            [
                "| No. | Candidate page | Status | Source-page excerpt |",
                "| --- | --- | --- | --- |",
                "| 6 | p.15 | visible_advisor_repair_candidate | 问责机制介入程度会导致政策风险变化，数字化技术介入程度会影响乡镇干部的政策决策空间。 |",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(run_dir)])

    assert result.returncode == 0, result.stdout
    out = (run_dir / "citation_evidence_workbench.md").read_text(encoding="utf-8")
    assert "| 6 | [10] | S-010 | p.15 | visible_advisor_repair_candidate |" in out
    assert "政策风险变化" in out


def main() -> int:
    tests = [
        test_workbench_extracts_source_snippet_without_finalizing_anchor,
        test_workbench_verified_mode_promotes_visible_reviewed_rows,
        test_workbench_prefers_body_page_over_reference_page,
        test_workbench_prefers_body_page_over_abstract_candidate,
        test_workbench_prefers_page_with_later_context_core_phrase,
        test_workbench_uses_visible_review_override_rows,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
        print(f"PASS {test.__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
