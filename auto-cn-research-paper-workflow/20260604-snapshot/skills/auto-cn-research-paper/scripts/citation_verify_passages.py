#!/usr/bin/env python3
"""Verify body-citation anchors against extracted source pages."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


PAGE_RE = re.compile(r"^(?:--- page (\d+) ---|===== PAGE (\d+) =====)\s*$", flags=re.MULTILINE | re.IGNORECASE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def split_md_row(line: str) -> list[str]:
    return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]


def normalize(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def parse_sources(matrix_text: str) -> dict[str, dict[str, str]]:
    sources: dict[str, dict[str, str]] = {}
    for line in matrix_text.splitlines():
        if not line.startswith("| S-"):
            continue
        cells = split_md_row(line)
        if len(cells) >= 5:
            sources[cells[0]] = {"authors": cells[2], "title": cells[4]}
    return sources


def parse_evidence_paths(evidence_text: str) -> list[Path]:
    paths: list[Path] = []
    for match in re.finditer(r"`([^`]+fulltext_extract[^`]+\.txt)`", evidence_text):
        paths.append(Path(match.group(1)))
    return paths


def find_source_path(source: dict[str, str], paths: list[Path]) -> Path | None:
    title_norm = normalize(source.get("title", ""))
    author_norms = [normalize(part) for part in re.split(r"[；;、，,\s]+", source.get("authors", "")) if part]
    best: tuple[int, Path | None] = (0, None)
    for path in paths:
        key = normalize(path.stem)
        score = 0
        if "技术治理何以影响乡镇干部行动" in source.get("title", "") and "technicalgovernancetownshipcadres" in key:
            score += 40
        if "傅利平" in source.get("authors", "") and "fuliping" in key:
            score += 20
        if "基层数字形式主义：表现、成因与对策" in source.get("title", "") and "grassrootsdigitalformalism" in key:
            score += 40
        if "欧阳康" in source.get("authors", "") and "ouyangkang" in key:
            score += 20
        if "城市基层数字平台的悬浮化" in source.get("title", "") and "smartcodeplatform" in key:
            score += 40
        if "李春生" in source.get("authors", "") and "lichunsheng" in key:
            score += 20
        if "数字技术何以有效赋能城市基层治理" in source.get("title", "") and "yiwangtongguan" in key:
            score += 40
        if "顾丽梅" in source.get("authors", "") and "gulimei" in key:
            score += 20
        if "双向激活" in source.get("title", "") and "yuexiudigitalgovernance" in key:
            score += 40
        if "陈天祥" in source.get("authors", "") and "chentianxiang" in key:
            score += 20
        for start in range(0, min(len(title_norm), 24), 6):
            frag = title_norm[start : start + 8]
            if frag and frag in key:
                score += len(frag)
        for author in author_norms:
            if author and author in key:
                score += 10
        if score > best[0]:
            best = (score, path)
    return best[1]


def parse_pages(text: str) -> dict[int, str]:
    matches = list(PAGE_RE.finditer(text))
    pages: dict[int, str] = {}
    for idx, match in enumerate(matches):
        page = int(match.group(1) or match.group(2))
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        pages[page] = text[start:end].strip()
    return pages


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


def parse_candidate_terms(suggested: str) -> list[tuple[str, list[int]]]:
    terms: list[tuple[str, list[int]]] = []
    for part in suggested.split(";"):
        if ":" not in part:
            continue
        term, page_text = part.split(":", 1)
        pages = [int(num) for num in re.findall(r"\d+", page_text)]
        if term.strip() and pages:
            terms.append((term.strip(), pages))
    return terms


def chinese_ngrams(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for seq in re.findall(r"[\u4e00-\u9fff]{2,}", text):
        if len(seq) < 2:
            continue
        for n in (2, 3, 4):
            for idx in range(0, max(len(seq) - n + 1, 0)):
                gram = seq[idx : idx + n]
                if not is_generic_ngram(gram):
                    counts[gram] += 1
    return counts


def is_generic_ngram(gram: str) -> bool:
    generic = {
        "本文",
        "认为",
        "研究",
        "治理",
        "基层",
        "数字",
        "形式",
        "主义",
        "问题",
        "可能",
        "需要",
        "指出",
        "说明",
        "成为",
        "机制",
        "路径",
        "工具",
        "平台",
        "技术",
    }
    return gram in generic


def overlap_score(context: str, page_text: str) -> tuple[int, list[str]]:
    context_counts = chinese_ngrams(context)
    page_norm = re.sub(r"\s+", "", page_text)
    hits: list[str] = []
    for gram, _ in context_counts.most_common(80):
        if gram in page_norm:
            hits.append(gram)
        if len(hits) >= 12:
            break
    return len(hits), hits


def cover_penalty(page: int, page_text: str) -> int:
    if page != 1:
        return table_of_contents_penalty(page_text)
    cover_terms = ["网络首发论文", "引用格式", "出版确认", "录用定稿", "不得修改论文题目"]
    return (12 if any(term in page_text for term in cover_terms) else 0) + table_of_contents_penalty(page_text)


def table_of_contents_penalty(page_text: str) -> int:
    compact = re.sub(r"\s+", " ", page_text)
    dot_leaders = len(re.findall(r"(?:\.\s*){3,}", page_text))
    toc_markers = ["PART ", "The Hypothesis of Cultural Lag", "Verification by the Facts", "Illustrations:"]
    marker_hits = sum(1 for marker in toc_markers if marker in compact)
    if dot_leaders >= 3 and marker_hits >= 2:
        return 35
    return 0


def snippet(page_text: str, terms: list[str], grams: list[str]) -> str:
    compact = re.sub(r"\s+", "", page_text)
    anchors = terms + grams
    positions = [compact.find(anchor) for anchor in anchors if anchor and compact.find(anchor) >= 0]
    start = min(positions) if positions else 0
    start = max(start - 50, 0)
    text = compact[start : start + 180]
    return text.replace("|", "/")


def rank_pages(row: dict[str, str], pages: dict[int, str]) -> tuple[int | None, int, list[str], list[str], str]:
    term_pages = parse_candidate_terms(row["suggested"])
    candidate_pages = sorted({page for _, page_list in term_pages for page in page_list if page in pages})
    best: tuple[int, int | None, list[str], list[str], str] = (-999, None, [], [], "")
    for page in candidate_pages:
        page_text = pages.get(page, "")
        matching_terms = [
            term
            for term, page_list in term_pages
            if page in page_list and (term in page_text or term.lower() in page_text.lower())
        ]
        overlap, grams = overlap_score(row["context"], page_text)
        score = len(matching_terms) * 10 + overlap * 3 - cover_penalty(page, page_text)
        if "摘要" in page_text[:1200] or "Abstract" in page_text[:1200]:
            score += 4
        if len(page_text) < 120:
            score -= 8
        if score > best[0]:
            best = (score, page, matching_terms, grams, snippet(page_text, matching_terms, grams))
    _, best_page, terms, grams, best_snippet = best
    return best_page, best[0], terms, grams, best_snippet


def verification_status(score: int, terms: list[str], grams: list[str]) -> str:
    if score >= 18 and terms and (grams or len(terms) >= 2):
        return "keyword_page_candidate"
    if score >= 10 and terms:
        return "needs_close_reading"
    return "needs_manual_anchor"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/citation_passage_verification.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "citation_passage_verification.md"

    matrix_path = next(path for path in run_dir.iterdir() if path.name.startswith("03_") and path.suffix == ".md")
    matrix_text = read(matrix_path)
    evidence_text = read(run_dir / "evidence_index.md")
    suggestions_text = read(run_dir / "citation_page_suggestions.md")

    sources = parse_sources(matrix_text)
    evidence_paths = parse_evidence_paths(evidence_text)
    rows = parse_suggestions(suggestions_text)

    verified = 0
    close = 0
    manual = 0
    lines = [
        "# Citation Passage Verification",
        "",
        "This table creates keyword/page candidates for body citations. `keyword_page_candidate` means the cited source page contains evidence terms and local context overlap; it is not final semantic passage verification or manual page anchoring.",
        "",
        "| No. | Ref | Source | Verified anchor | Status | Score | Evidence terms | Context overlap | Evidence snippet |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for row in rows:
        source = sources.get(row["source"], {})
        source_path = find_source_path(source, evidence_paths) if source else None
        page_text = read(source_path) if source_path else ""
        pages = parse_pages(page_text)
        page, score, terms, grams, evidence = rank_pages(row, pages)
        status = verification_status(score, terms, grams)
        if status == "keyword_page_candidate":
            verified += 1
        elif status == "needs_close_reading":
            close += 1
        else:
            manual += 1
        anchor = f"p.{page}" if page else ""
        lines.append(
            f"| {row['no']} | {row['ref']} | {row['source']} | {anchor} | {status} | {score} | {', '.join(terms[:6])} | {', '.join(grams[:8])} | {evidence} |"
        )

    all_ready = bool(rows) and verified == len(rows)
    lines.extend(
        [
            "",
            f"- body_citation_occurrences: {len(rows)}",
            f"- keyword_page_candidates: {verified}",
            f"- needs_close_reading: {close}",
            f"- needs_manual_anchor: {manual}",
            "- verification_method: keyword_page_term_overlap",
            "- semantic_verified_anchors: 0",
            "- agent_verified_anchors: 0",
            "- citation_level_verified_anchors: 0",
            "- citation_level_verification_ready: no",
            f"- keyword_candidate_generation_ready: {'yes' if all_ready else 'no'}",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"body_citation_occurrences={len(rows)}")
    print(f"keyword_page_candidates={verified}")
    print(f"needs_close_reading={close}")
    print(f"needs_manual_anchor={manual}")
    print("semantic_verified_anchors=0")
    print("agent_verified_anchors=0")
    print("citation_level_verified_anchors=0")
    print("citation_level_verification_ready=no")
    print(f"keyword_candidate_generation_ready={'yes' if all_ready else 'no'}")
    print(f"out={out}")
    return 0 if all_ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
