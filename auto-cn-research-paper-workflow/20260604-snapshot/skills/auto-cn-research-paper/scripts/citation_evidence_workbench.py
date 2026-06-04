#!/usr/bin/env python3
"""Build a citation-by-citation evidence workbench with source snippets."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from build_evidence_index import split_pages
from citation_plan import find_evidence, parse_evidence_summary, parse_sources, split_md_row


STATUS_WITH_EXCERPT = "needs_human_or_visible_advisor_verification"
VISIBLE_VERIFIED_STATUS = "citation_level_visible_verified_anchor"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def parse_suggestion_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = split_md_row(line)
        if len(cells) < 6 or cells[0] in {"No.", "---"}:
            continue
        if not cells[0].isdigit():
            continue
        rows.append(
            {
                "no": cells[0],
                "ref": cells[1],
                "source": cells[2],
                "suggested_pages": cells[3],
                "confidence": cells[4],
                "context": cells[5],
            }
        )
    return rows


def parse_override_rows(text: str) -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = split_md_row(line)
        if len(cells) < 4 or cells[0] in {"No.", "---"}:
            continue
        if not cells[0].isdigit():
            continue
        overrides[cells[0]] = {
            "page": cells[1],
            "status": cells[2] if len(cells) > 2 else STATUS_WITH_EXCERPT,
            "excerpt": cells[3],
        }
    return overrides


def visible_verified_candidate(status: str, page_label: str, excerpt: str) -> bool:
    if not excerpt.strip():
        return False
    if "not_page_anchor" in status or "official HTML" in page_label:
        return False
    if page_label.strip().startswith("p."):
        return status.startswith("visible_advisor_") or status == VISIBLE_VERIFIED_STATUS
    return False


def parse_page_numbers(value: str) -> list[int]:
    pages: list[int] = []
    for match in re.finditer(r"(?<!S-)(?<!S)(?<!-)\b(\d{1,3})\b", value):
        page = int(match.group(1))
        if page not in pages:
            pages.append(page)
    return pages


def suggested_terms(value: str, context: str) -> list[str]:
    terms: list[str] = []
    for part in value.split(";"):
        term = part.split(":", 1)[0].strip()
        if len(term) >= 2 and term not in terms:
            terms.append(term)
    for token in re.findall(r"[\u4e00-\u9fff]{2,8}", context):
        if len(token) >= 2 and token not in terms:
            terms.append(token)
    return terms[:18]


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def page_score(page_text: str, terms: list[str]) -> int:
    page = compact(page_text)
    score = 0
    for term in terms:
        if term and term in page:
            score += len(term)
    if any(marker in page for marker in ("一、", "二、", "三、", "（一）", "（二）", "（三）", "(一)", "(二)", "(三)")):
        score += 12
    if "摘要" in page and "关键词" in page:
        score -= 35
    if "题目：" in page and "作者" in page:
        score -= 30
    if "作者简介" in page and "基金项目" in page:
        score -= 20
    if "网络首发论文" in page or "引用格式" in page or "出版确认" in page:
        score -= 80
    if "参考文献" in page or "References" in page or "REFERENCE" in page:
        score -= 60
    latin = sum(1 for ch in page if ("a" <= ch.lower() <= "z"))
    chinese = sum(1 for ch in page if "\u4e00" <= ch <= "\u9fff")
    if latin > chinese and latin > 120:
        score -= 40
    return score


def excerpt(page_text: str, terms: list[str], width: int = 80) -> str:
    page = compact(page_text)
    best_pos = -1
    best_term = ""
    for term in terms:
        pos = page.find(term)
        if pos >= 0 and (best_pos < 0 or len(term) > len(best_term)):
            best_pos = pos
            best_term = term
    if best_pos < 0:
        return page[: width * 2]
    start = max(0, best_pos - width)
    end = min(len(page), best_pos + len(best_term) + width)
    return page[start:end]


def choose_page(pages: list[tuple[int, str]], candidate_pages: list[int], terms: list[str]) -> tuple[int, str, int]:
    # Treat upstream page suggestions as a weak hint, not a hard boundary:
    # citation-level support often sits in the article body even when a
    # keyword index points at the title or abstract page.
    candidate_set = set(candidate_pages)
    candidates = pages
    best: tuple[int, str, int] = (0, "", -1)
    for page_no, page_text in candidates:
        score = page_score(page_text, terms)
        if page_no in candidate_set:
            score += 8
        if score > best[2]:
            best = (page_no, page_text, score)
    return best


def ref_number(ref: str) -> int | None:
    match = re.search(r"\[(\d+)\]", ref)
    return int(match.group(1)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/citation_evidence_workbench.md")
    parser.add_argument(
        "--verified-citation-pages",
        action="store_true",
        help=(
            "After visible/manual citation-level review has accepted every row, "
            "mark the workbench as final-anchor-consistent with citation_final.md."
        ),
    )
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "citation_evidence_workbench.md"

    matrix_text = read(run_dir / "03_文献矩阵.md")
    evidence_text = read(run_dir / "evidence_index.md")
    suggestions_text = read(run_dir / "citation_page_suggestions.md")
    overrides = parse_override_rows(read(run_dir / "citation_evidence_overrides.md"))
    sources = parse_sources(matrix_text)
    evidence_rows = parse_evidence_summary(evidence_text)
    rows = parse_suggestion_rows(suggestions_text)

    with_excerpt = 0
    missing_source_text = 0
    missing_excerpt = 0
    output_rows: list[str] = []

    for row in rows:
        number = ref_number(row["ref"])
        source = sources.get(number or -1)
        status = STATUS_WITH_EXCERPT
        source_path = ""
        page_label = ""
        evidence_excerpt = ""
        override = overrides.get(row["no"])
        if override:
            page_label = override["page"]
            status = override["status"] or STATUS_WITH_EXCERPT
            evidence_excerpt = override["excerpt"].replace("|", "/")
            if evidence_excerpt:
                with_excerpt += 1
            else:
                missing_excerpt += 1
                status = "needs_source_page_review"
        elif not source:
            status = "missing_source_record"
            missing_source_text += 1
        else:
            evidence = find_evidence(source, evidence_rows)
            if not evidence and len(evidence_rows) == 1:
                evidence = evidence_rows[0]
            if not evidence:
                status = "missing_source_text"
                missing_source_text += 1
            else:
                source_path = evidence["path"]
                path = Path(source_path)
                if not path.exists():
                    status = "missing_source_text"
                    missing_source_text += 1
                else:
                    text = path.read_text(encoding="utf-8", errors="ignore")
                    pages = split_pages(text)
                    terms = suggested_terms(row["suggested_pages"], row["context"])
                    page_no, page_text, score = choose_page(pages, parse_page_numbers(row["suggested_pages"]), terms)
                    page_label = f"p.{page_no}" if page_no else ""
                    evidence_excerpt = excerpt(page_text, terms).replace("|", "/")
                    if evidence_excerpt and score > 0:
                        with_excerpt += 1
                    else:
                        missing_excerpt += 1
                        status = "needs_source_page_review"

        context = row["context"].replace("|", "/")
        display_status = status
        if args.verified_citation_pages and visible_verified_candidate(status, page_label, evidence_excerpt):
            display_status = VISIBLE_VERIFIED_STATUS
        output_rows.append(
            f"| {row['no']} | {row['ref']} | {row['source']} | {page_label} | {display_status} | {evidence_excerpt} | {context} |"
        )

    citation_level_verified = 0
    final_anchor_ready = False
    if args.verified_citation_pages and len(rows) and missing_source_text == 0 and missing_excerpt == 0:
        verified_rows = [
            line
            for line in output_rows
            if f"| {VISIBLE_VERIFIED_STATUS} |" in line
        ]
        citation_level_verified = len(verified_rows)
        final_anchor_ready = citation_level_verified == len(rows)

    lines = [
        "# Citation Evidence Workbench",
        "",
        "This workbench attaches source-page excerpts to body citations. By default it supports citation-level review without finalizing anchors; with `--verified-citation-pages`, it records visible/manual citation-level verification already accepted elsewhere.",
        "",
        "| No. | Ref | Source | Candidate page | Status | Source-page excerpt | Citation context |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        *output_rows,
        "",
        f"- body_citation_occurrences: {len(rows)}",
        f"- rows_with_source_excerpt: {with_excerpt}",
        f"- missing_source_text: {missing_source_text}",
        f"- missing_excerpt: {missing_excerpt}",
        f"- citation_level_verified_anchors: {citation_level_verified}",
        f"- final_anchor_ready: {'yes' if final_anchor_ready else 'no'}",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"body_citation_occurrences={len(rows)}")
    print(f"rows_with_source_excerpt={with_excerpt}")
    print(f"missing_source_text={missing_source_text}")
    print(f"missing_excerpt={missing_excerpt}")
    print(f"out={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
