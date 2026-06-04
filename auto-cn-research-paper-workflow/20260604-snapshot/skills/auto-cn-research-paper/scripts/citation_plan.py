#!/usr/bin/env python3
"""Map draft citation markers to verified sources and evidence pages."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def normalize(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def split_md_row(line: str) -> list[str]:
    return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]


def parse_sources(matrix_text: str) -> dict[int, dict[str, str]]:
    sources: dict[int, dict[str, str]] = {}
    for line in matrix_text.splitlines():
        if not line.startswith("| S-"):
            continue
        cells = split_md_row(line)
        if len(cells) < 11:
            continue
        match = re.search(r"S-(\d+)", cells[0])
        if not match:
            continue
        idx = int(match.group(1))
        sources[idx] = {
            "id": cells[0],
            "status": cells[1],
            "authors": cells[2],
            "year": cells[3],
            "title": cells[4],
            "source": cells[5],
            "relation": cells[10] if len(cells) > 10 else "",
        }
    return sources


def parse_evidence_summary(evidence_text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in evidence_text.splitlines():
        if not line.startswith("| `"):
            continue
        cells = split_md_row(line)
        if len(cells) < 4:
            continue
        rows.append(
            {
                "path": cells[0],
                "pages": cells[1],
                "characters": cells[2],
                "locations": cells[3],
                "norm_path": normalize(Path(cells[0]).stem),
            }
        )
    return rows


def find_evidence(source: dict[str, str], evidence_rows: list[dict[str, str]]) -> dict[str, str] | None:
    title_norm = normalize(source["title"])
    best: tuple[int, dict[str, str] | None] = (0, None)
    for row in evidence_rows:
        score = 0
        if "技术治理何以影响乡镇干部行动" in source["title"] and "technicalgovernancetownshipcadres" in row["norm_path"]:
            score += 40
        if "傅利平" in source["authors"] and "fuliping" in row["norm_path"]:
            score += 20
        if "基层数字形式主义：表现、成因与对策" in source["title"] and "grassrootsdigitalformalism" in row["norm_path"]:
            score += 40
        if "欧阳康" in source["authors"] and "ouyangkang" in row["norm_path"]:
            score += 20
        if "城市基层数字平台的悬浮化" in source["title"] and "smartcodeplatform" in row["norm_path"]:
            score += 40
        if "李春生" in source["authors"] and "lichunsheng" in row["norm_path"]:
            score += 20
        if "数字技术何以有效赋能城市基层治理" in source["title"] and "yiwangtongguan" in row["norm_path"]:
            score += 40
        if "顾丽梅" in source["authors"] and "gulimei" in row["norm_path"]:
            score += 20
        if "双向激活" in source["title"] and "yuexiudigitalgovernance" in row["norm_path"]:
            score += 40
        if "陈天祥" in source["authors"] and "chentianxiang" in row["norm_path"]:
            score += 20
        for start in range(0, min(len(title_norm), 18), 6):
            frag = title_norm[start : start + 8]
            if frag and frag in row["norm_path"]:
                score += len(frag)
        for author in re.split(r"[；;、，,\s]+", source["authors"]):
            if author and normalize(author) in row["norm_path"]:
                score += 10
        if score > best[0]:
            best = (score, row)
    return best[1] if best[0] else None


def citation_occurrences(draft_text: str) -> list[dict[str, str]]:
    occurrences: list[dict[str, str]] = []
    body_text = re.split(r"^##\s*参考文献\s*$", draft_text, flags=re.MULTILINE)[0]
    for match in re.finditer(r"\[(\d+)\]", body_text):
        start = max(0, match.start() - 90)
        end = min(len(body_text), match.end() + 90)
        context = re.sub(r"\s+", "", body_text[start:end])
        occurrences.append({"index": match.group(1), "context": context})
    return occurrences


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/citation_plan.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "citation_plan.md"

    matrix_text = (run_dir / "03_文献矩阵.md").read_text(encoding="utf-8")
    draft_text = (run_dir / "06_论文初稿.md").read_text(encoding="utf-8")
    evidence_text = (run_dir / "evidence_index.md").read_text(encoding="utf-8") if (run_dir / "evidence_index.md").exists() else ""

    sources = parse_sources(matrix_text)
    evidence_rows = parse_evidence_summary(evidence_text)
    occurrences = citation_occurrences(draft_text)
    cited_refs = {int(occurrence["index"]) for occurrence in occurrences}
    cited_sources = {idx: source for idx, source in sources.items() if idx in cited_refs}
    background_source_count = len(sources) - len(cited_sources)

    lines = [
        "# Citation Plan",
        "",
        "This file maps draft citation markers to verified source records and page/location candidates from `evidence_index.md`.",
        "",
        "## Cited Source Map",
        "",
        "Only sources actually cited in the draft body are listed here; background reading sources stay in the literature matrix.",
        "",
        "| Ref | Source ID | Authors | Title | Evidence pages | Top locations |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for idx in sorted(cited_sources):
        source = cited_sources[idx]
        evidence = find_evidence(source, evidence_rows)
        pages = evidence["pages"] if evidence else ""
        locations = evidence["locations"] if evidence else "missing evidence row"
        lines.append(
            f"| [{idx}] | {source['id']} | {source['authors']} | {source['title']} | {pages} | {locations} |"
        )

    lines.extend(["", "## Draft Citation Occurrences", "", "| Ref | Context | Status |", "| --- | --- | --- |"])
    missing = 0
    for occurrence in occurrences:
        idx = int(occurrence["index"])
        status = "mapped" if idx in sources else "missing source"
        if status != "mapped":
            missing += 1
        context = occurrence["context"].replace("|", "/")
        lines.append(f"| [{idx}] | {context} | {status} |")

    lines.extend(
        [
            "",
            f"- source_count: {len(cited_sources)}",
            f"- matrix_source_count: {len(sources)}",
            f"- background_source_count: {background_source_count}",
            f"- citation_occurrences: {len(occurrences)}",
            f"- missing_citation_sources: {missing}",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"source_count={len(cited_sources)}")
    print(f"matrix_source_count={len(sources)}")
    print(f"background_source_count={background_source_count}")
    print(f"citation_occurrences={len(occurrences)}")
    print(f"missing_citation_sources={missing}")
    print(f"out={out}")
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
