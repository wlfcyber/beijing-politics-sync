#!/usr/bin/env python3
"""Audit text-quality gates before external final review.

This script treats source integrity and surface word counts as diagnostics, not
as proof that the paper is analytically strong.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REVIEW_VERBS = ("指出", "表明", "认为", "提出", "强调", "提示", "说明")
WORKFLOW_PHRASES = (
    "已核验全文",
    "材料层",
    "工作流",
    "试运行",
    "不仅依赖 2026 年文献",
    "不只依赖 2026 年",
    "文献综合型研究",
    "作为一项文献综合型研究",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def body_text(draft: str) -> str:
    parts = re.split(r"^##\s*参考文献\s*$", draft, flags=re.MULTILINE)
    return parts[0]


def paragraphs(text: str) -> list[str]:
    paras = []
    for raw in re.split(r"\n\s*\n", text):
        para = raw.strip()
        if not para or para.startswith("#") or para.startswith("|") or para.startswith("["):
            continue
        paras.append(re.sub(r"\s+", "", para))
    return paras


def first_sentence(para: str) -> str:
    match = re.search(r"[。！？]", para)
    return para[: match.end()] if match else para[:80]


def lead_review_sentence_ratio(paras: list[str]) -> tuple[int, int, float]:
    checked = [p for p in paras if len(p) >= 20]
    weak = 0
    for para in checked:
        lead = first_sentence(para)
        if any(verb in lead for verb in REVIEW_VERBS) and re.search(r"[\u4e00-\u9fff]{2,6}[、，]", lead):
            weak += 1
    ratio = weak / len(checked) if checked else 0.0
    return weak, len(checked), ratio


def review_verb_density(text: str, paras: list[str]) -> tuple[int, float]:
    count = sum(text.count(verb) for verb in REVIEW_VERBS)
    density = count / len(paras) if paras else 0.0
    return count, density


def extract_title(draft: str) -> str:
    for line in draft.splitlines():
        line = line.strip().lstrip("\ufeff")
        if line.startswith("题目："):
            return line.removeprefix("题目：").strip()
        if line and not line.startswith("#"):
            return line
    return ""


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--max-lead-review-ratio", type=float, default=0.15)
    parser.add_argument(
        "--max-review-verb-density",
        type=float,
        default=None,
        help="Deprecated as a pass/fail gate; retained only for legacy one-off audits.",
    )
    parser.add_argument("--forbid-title-term", action="append", default=[])
    parser.add_argument("--require-quality-plan", action="store_true")
    parser.add_argument("--require-method-data-fit", action="store_true")
    parser.add_argument("--require-comparison-table", action="store_true")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    draft_path = run_dir / "06_论文初稿.md"
    plan_path = run_dir / "20_质量差距诊断与重写方案.md"
    draft = read(draft_path)
    issues: list[str] = []

    if not draft:
        issues.append("missing draft: 06_论文初稿.md")

    if args.require_quality_plan and not plan_path.exists():
        issues.append("missing quality-gap diagnosis: 20_质量差距诊断与重写方案.md")

    title = extract_title(draft)
    for term in args.forbid_title_term:
        if term and term in title:
            issues.append(f"title still contains forbidden framing term: {term}")

    paras = paragraphs(body_text(draft))
    weak, total, ratio = lead_review_sentence_ratio(paras)
    review_count, review_density = review_verb_density(body_text(draft), paras)
    if total and ratio > args.max_lead_review_ratio:
        issues.append(
            f"paragraph lead review-sentence ratio too high: {weak}/{total}={ratio:.2%}, "
            f"limit={args.max_lead_review_ratio:.2%}"
        )
    if args.max_review_verb_density is not None and total and review_density > args.max_review_verb_density:
        issues.append(
            f"review/backing verb density too high: {review_count} occurrences/{total} paragraphs="
            f"{review_density:.2f}, limit={args.max_review_verb_density:.2f}"
        )

    found_workflow = [phrase for phrase in WORKFLOW_PHRASES if phrase in body_text(draft)]
    if found_workflow:
        issues.append("draft contains workflow/meta-review phrases: " + ", ".join(found_workflow))

    if "## 结论" in draft:
        conclusion = draft.split("## 结论", 1)[1]
        conclusion = re.split(r"^##\s*参考文献\s*$", conclusion, flags=re.MULTILINE)[0]
        if "不成立" not in conclusion and "修正" not in conclusion and "限定" not in conclusion:
            issues.append("conclusion lacks an explicit falsification, revision, or boundary condition")

    if "二次比较" in title and "研究设计" not in draft:
        issues.append("title claims secondary comparison but draft lacks a research-design section")

    comparison_claimed = any(term in title for term in ("比较", "二次比较", "案例比较")) or "二次比较" in draft
    has_comparison_table = (
        "同维度" in draft
        and ("对照表" in draft or "比较表" in draft)
        and ("指标化" in draft or "可视化" in draft)
        and ("自治缓冲" in draft or "需求牵引" in draft)
    )
    if args.require_comparison_table and comparison_claimed and not has_comparison_table:
        issues.append("comparison is claimed but no same-dimension case comparison table was found")

    if args.require_method_data_fit:
        if comparison_claimed and "同维度" not in draft:
            issues.append("method-data fit weak: comparison claim lacks same-dimension coding language")
        if any(term in draft for term in ("访谈", "调研", "问卷")) and not any(
            caveat in draft
            for caveat in ("不虚构访谈", "不重新虚构", "没有一手", "尚未引入一手", "二次分析", "二次案例")
        ):
            issues.append("method-data fit weak: draft mentions fieldwork terms without a clear no-primary-data boundary")
        if "正确政绩观" in title:
            issues.append("method-data fit weak: title still uses old normative framing as the main research lens")

    status = "PASS" if not issues else "INCOMPLETE"
    print(f"status={status}")
    print(f"title={title or 'unknown'}")
    print(f"paragraph_lead_review_sentences={weak}/{total}")
    print(f"paragraph_lead_review_ratio={ratio:.2%}")
    print(f"review_verb_occurrences_diagnostic={review_count}")
    print(f"review_verb_density_per_paragraph_diagnostic={review_density:.2f}")
    print(f"comparison_claimed={'yes' if comparison_claimed else 'no'}")
    print(f"same_dimension_comparison_table={'yes' if has_comparison_table else 'no'}")
    print(f"quality_plan_present={'yes' if plan_path.exists() else 'no'}")
    for issue in issues:
        print(f"- {issue}")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
