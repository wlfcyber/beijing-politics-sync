#!/usr/bin/env python3
"""Build stricter paragraph-level semantic candidates for citation anchors."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


PAGE_RE = re.compile(r"^(?:--- page (\d+) ---|===== PAGE (\d+) =====)\s*$", flags=re.MULTILINE | re.IGNORECASE)

GENERIC_TERMS = {
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
    "文献",
    "材料",
    "分析",
    "进一步",
    "相关",
    "表明",
    "可以",
    "强调",
    "概括",
}


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
    return [Path(match.group(1)) for match in re.finditer(r"`([^`]+fulltext_extract[^`]+\.txt)`", evidence_text)]


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


def compact_text(text: str) -> str:
    return re.sub(r"\s+", "", text)


def context_grams(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    compact = compact_text(text)
    for n in (3, 4, 5, 6):
        for idx in range(0, max(len(compact) - n + 1, 0)):
            gram = compact[idx : idx + n]
            if re.fullmatch(r"[\u4e00-\u9fff]+", gram) and not is_generic(gram):
                counts[gram] += 1
    return counts


def is_generic(gram: str) -> bool:
    return gram in GENERIC_TERMS or any(term == gram for term in GENERIC_TERMS)


def claim_terms(context: str) -> list[str]:
    terms: list[str] = []
    for seq in re.findall(r"[\u4e00-\u9fff]{2,12}", context):
        if seq in GENERIC_TERMS:
            continue
        if len(seq) >= 3:
            terms.append(seq)
    deduped: list[str] = []
    for term in terms:
        if term not in deduped:
            deduped.append(term)
    return deduped[:25]


def paragraph_windows(page_text: str) -> list[str]:
    compact = compact_text(page_text)
    if not compact:
        return []
    sentences = re.split(r"[。！？；;]", compact)
    windows: list[str] = []
    for idx in range(len(sentences)):
        chunk = "".join(sentences[idx : idx + 3])
        if len(chunk) >= 60:
            windows.append(chunk[:420])
    if not windows:
        for idx in range(0, len(compact), 220):
            chunk = compact[idx : idx + 360]
            if len(chunk) >= 60:
                windows.append(chunk)
    return windows[:30]


def candidate_pages(suggested: str, pages: dict[int, str]) -> list[int]:
    term_pages = parse_candidate_terms(suggested)
    return sorted({page for _, page_list in term_pages for page in page_list if page in pages})


def score_window(context: str, suggested: str, window: str) -> tuple[int, list[str], list[str], list[str]]:
    grams = context_grams(context)
    gram_hits: list[str] = []
    for gram, _ in grams.most_common(120):
        if gram in window:
            gram_hits.append(gram)
        if len(gram_hits) >= 14:
            break

    suggested_terms = [term for term, _ in parse_candidate_terms(suggested) if term and term in window]
    claim_hits = [term for term in claim_terms(context) if term in window]
    score = len(gram_hits) * 3 + len(suggested_terms) * 12 + len(claim_hits[:8]) * 5
    return score, suggested_terms[:8], claim_hits[:8], gram_hits[:10]


def classify(score: int, suggested_terms: list[str], claim_hits: list[str], gram_hits: list[str]) -> str:
    if score >= 70 and suggested_terms and (len(claim_hits) >= 2 or len(gram_hits) >= 7):
        return "semantic_alignment_candidate"
    if score >= 42 and suggested_terms and (claim_hits or len(gram_hits) >= 4):
        return "weak_semantic_candidate"
    return "needs_manual_semantic_check"


def best_semantic_candidate(row: dict[str, str], pages: dict[int, str]) -> tuple[str, int, int, list[str], list[str], list[str], str]:
    best: tuple[int, int, str, list[str], list[str], list[str], str] = (-1, 0, "", [], [], [], "")
    for page in candidate_pages(row["suggested"], pages):
        for window in paragraph_windows(pages.get(page, "")):
            score, suggested_terms, claim_hits, gram_hits = score_window(row["context"], row["suggested"], window)
            status = classify(score, suggested_terms, claim_hits, gram_hits)
            if score > best[0]:
                best = (score, page, status, suggested_terms, claim_hits, gram_hits, window[:220].replace("|", "/"))
    score, page, status, suggested_terms, claim_hits, gram_hits, snippet = best
    if score < 0:
        return "needs_manual_semantic_check", 0, 0, [], [], [], ""
    return status, page, score, suggested_terms, claim_hits, gram_hits, snippet


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/citation_semantic_verification.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "citation_semantic_verification.md"

    matrix_text = read(run_dir / "03_文献矩阵.md")
    evidence_text = read(run_dir / "evidence_index.md")
    suggestions_text = read(run_dir / "citation_page_suggestions.md")
    sources = parse_sources(matrix_text)
    evidence_paths = parse_evidence_paths(evidence_text)
    rows = parse_suggestions(suggestions_text)

    strong = 0
    weak = 0
    manual = 0
    lines = [
        "# Citation Semantic Verification",
        "",
        "This worksheet ranks paragraph-level semantic candidates for body citations. These are agent-generated candidates for human or external review, not final anchors.",
        "",
        "| No. | Ref | Source | Candidate anchor | Status | Score | Evidence terms | Claim terms | Context overlap | Candidate snippet |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for row in rows:
        source = sources.get(row["source"], {})
        source_path = find_source_path(source, evidence_paths) if source else None
        pages = parse_pages(read(source_path)) if source_path else {}
        status, page, score, evidence_terms, claim_hits, gram_hits, snippet = best_semantic_candidate(row, pages)
        if status == "semantic_alignment_candidate":
            strong += 1
        elif status == "weak_semantic_candidate":
            weak += 1
        else:
            manual += 1
        anchor = f"p.{page}" if page else ""
        lines.append(
            f"| {row['no']} | {row['ref']} | {row['source']} | {anchor} | {status} | {score} | {', '.join(evidence_terms)} | {', '.join(claim_hits)} | {', '.join(gram_hits)} | {snippet} |"
        )

    lines.extend(
        [
            "",
            f"- body_citation_occurrences: {len(rows)}",
            f"- semantic_alignment_candidates: {strong}",
            f"- weak_semantic_candidates: {weak}",
            f"- needs_manual_semantic_check: {manual}",
            "- semantic_alignment_method: paragraph_window_context_overlap",
            "- semantic_candidates_final_ready: no",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"body_citation_occurrences={len(rows)}")
    print(f"semantic_alignment_candidates={strong}")
    print(f"weak_semantic_candidates={weak}")
    print(f"needs_manual_semantic_check={manual}")
    print("semantic_candidates_final_ready=no")
    print(f"out={out}")
    return 0 if manual == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
