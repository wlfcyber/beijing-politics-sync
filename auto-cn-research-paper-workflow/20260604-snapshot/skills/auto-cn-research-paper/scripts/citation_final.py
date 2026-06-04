#!/usr/bin/env python3
"""Build a final citation anchoring worksheet from page suggestions."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PUBLIC_REPRINT_STATUSES = ["public_reprint_full_text_read"]
DEFAULT_ALIGNMENT_METHOD = "keyword_candidate_evidence_index"
VERIFIED_ALIGNMENT_METHOD = "verified_citation_page_alignment"
KEYWORD_PAGE_ALIGNMENT_METHOD = "keyword_page_candidate_not_final"


def split_md_row(line: str) -> list[str]:
    return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]


def parse_source_statuses(matrix_text: str) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for line in matrix_text.splitlines():
        if not line.startswith("| S-"):
            continue
        cells = split_md_row(line)
        if len(cells) >= 2:
            statuses[cells[0]] = cells[1]
    return statuses


def parse_suggestions(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = split_md_row(line)
        if len(cells) < 6 or cells[0] in {"No.", "---"}:
            continue
        if not re.fullmatch(r"\d+", cells[0]):
            continue
        rows.append(
            {
                "no": cells[0],
                "ref": cells[1],
                "source": cells[2],
                "suggested": cells[3],
                "confidence": cells[4],
                "context": cells[5],
            }
        )
    return rows


def parse_verification(text: str) -> tuple[bool, dict[str, dict[str, str]]]:
    ready = "- keyword_candidate_generation_ready: yes" in text or "- citation_level_verification_ready: yes" in text
    rows: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = split_md_row(line)
        if len(cells) < 5 or cells[0] in {"No.", "---"}:
            continue
        if not re.fullmatch(r"\d+", cells[0]):
            continue
        rows[cells[0]] = {
            "ref": cells[1],
            "source": cells[2],
            "anchor": cells[3],
            "status": cells[4],
        }
    return ready, rows


def first_page(suggested: str) -> str:
    match = re.search(r"(?<!\d)(\d+)(?!\d)", suggested)
    return match.group(1) if match else ""


def anchor_row(row: dict[str, str], source_status: str) -> tuple[str, str, str]:
    if any(status in source_status for status in PUBLIC_REPRINT_STATUSES):
        return "", "blocked_public_reprint_primary_needed", "公开转载来源不生成正式页码；需原刊 PDF/数据库全文。"
    page = first_page(row["suggested"])
    if not page:
        return "", "needs_manual_anchor", "候选页为空，需要人工核对。"
    if row["confidence"] not in {"candidate", "weak_candidate"}:
        return "", "needs_manual_anchor", f"候选置信度为 {row['confidence']}，需要人工核对。"
    return f"p.{page}", "anchored_from_evidence_index", "从 evidence_index/citation_page_suggestions 选取首个匹配页；正式提交前按学校格式转写。"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/citation_final.md")
    parser.add_argument(
        "--verified-citation-pages",
        action="store_true",
        help=(
            "Mark anchors as final only after each body citation has been checked against "
            "the cited source passage/page, not merely against keyword candidates."
        ),
    )
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "citation_final.md"

    matrix_text = (run_dir / "03_文献矩阵.md").read_text(encoding="utf-8")
    suggestions_text = (run_dir / "citation_page_suggestions.md").read_text(encoding="utf-8")
    verification_text = (run_dir / "citation_passage_verification.md").read_text(encoding="utf-8") if (
        run_dir / "citation_passage_verification.md"
    ).exists() else ""
    statuses = parse_source_statuses(matrix_text)
    rows = parse_suggestions(suggestions_text)
    verification_ready, verification_rows = parse_verification(verification_text)

    anchored = 0
    blocked = 0
    needs_manual = 0
    keyword_page_candidates = 0
    use_keyword_candidates = verification_ready and bool(verification_rows)
    if args.verified_citation_pages:
        alignment_method = VERIFIED_ALIGNMENT_METHOD
    elif use_keyword_candidates:
        alignment_method = KEYWORD_PAGE_ALIGNMENT_METHOD
    else:
        alignment_method = DEFAULT_ALIGNMENT_METHOD
    lines = [
        "# Citation Final Anchors",
        "",
        "This worksheet promotes source-backed page suggestions into working anchors for final footnote polishing.",
        "Rows marked `blocked_public_reprint_primary_needed` must not be treated as formal page anchors.",
        "By default, keyword-derived page candidates are working anchors only. Use `--verified-citation-pages` only after citation-level passage/page verification.",
        "",
        "| No. | Ref | Source | Anchor | Verified | Status | Note | Context |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for row in rows:
        source_status = statuses.get(row["source"], "")
        verification_row = verification_rows.get(row["no"], {}) if use_keyword_candidates else {}
        if (
            verification_row
            and verification_row.get("status") == "keyword_page_candidate"
            and verification_row.get("source") == row["source"]
        ):
            anchor = verification_row.get("anchor", "")
            status = "keyword_page_candidate_anchor"
            note = "由 citation_passage_verification.md 生成关键词页候选；正式提交前仍需语义段落核验或人工读页。"
        else:
            anchor, status, note = anchor_row(row, source_status)
        if status == "anchored_from_evidence_index":
            anchored += 1
        elif status == "keyword_page_candidate_anchor":
            anchored += 1
            keyword_page_candidates += 1
        elif status == "blocked_public_reprint_primary_needed":
            blocked += 1
        else:
            needs_manual += 1
        context = row["context"].replace("|", "/")
        verified = "yes" if args.verified_citation_pages and status in {
            "anchored_from_evidence_index",
            "keyword_page_candidate_anchor",
        } else "no"
        lines.append(
            f"| {row['no']} | {row['ref']} | {row['source']} | {anchor} | {verified} | {status} | {note} | {context} |"
        )

    working_anchor_ready = bool(rows) and blocked == 0 and needs_manual == 0
    manual_verified = anchored if args.verified_citation_pages else 0
    agent_verified = 0
    citation_level_verified = manual_verified
    final_anchor_ready = working_anchor_ready and args.verified_citation_pages and citation_level_verified == len(rows)
    lines.extend(
        [
            "",
            f"- body_citation_occurrences: {len(rows)}",
            f"- anchored_citations: {anchored}",
            f"- blocked_public_reprint_citations: {blocked}",
            f"- needs_manual_anchor: {needs_manual}",
            f"- working_anchor_ready: {'yes' if working_anchor_ready else 'no'}",
            f"- keyword_page_candidates: {keyword_page_candidates}",
            f"- manual_verified_anchors: {manual_verified}",
            f"- agent_verified_anchors: {agent_verified}",
            f"- citation_level_verified_anchors: {citation_level_verified}",
            f"- citation_alignment_method: {alignment_method}",
            f"- citation_alignment_scope: {'citation_level_verified' if final_anchor_ready else 'keyword_candidate_not_final'}",
            f"- final_anchor_ready: {'yes' if final_anchor_ready else 'no'}",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"body_citation_occurrences={len(rows)}")
    print(f"anchored_citations={anchored}")
    print(f"blocked_public_reprint_citations={blocked}")
    print(f"needs_manual_anchor={needs_manual}")
    print(f"working_anchor_ready={'yes' if working_anchor_ready else 'no'}")
    print(f"keyword_page_candidates={keyword_page_candidates}")
    print(f"manual_verified_anchors={manual_verified}")
    print(f"agent_verified_anchors={agent_verified}")
    print(f"citation_level_verified_anchors={citation_level_verified}")
    print(f"citation_alignment_method={alignment_method}")
    print(f"citation_alignment_scope={'citation_level_verified' if final_anchor_ready else 'keyword_candidate_not_final'}")
    print(f"final_anchor_ready={'yes' if final_anchor_ready else 'no'}")
    print(f"out={out}")
    return 0 if working_anchor_ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
