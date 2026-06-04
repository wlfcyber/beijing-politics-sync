#!/usr/bin/env python3
"""Suggest page candidates for each body citation from evidence_index.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ALIASES = {
    "正确政绩观": ["政绩观", "为民造福", "真抓实干"],
    "痕迹": ["留痕", "痕迹"],
    "考核": ["指标", "考核", "排名", "评价"],
    "平台": ["平台", "APP", "应用程序", "政务应用"],
    "算法": ["算法"],
    "理念": ["理念", "价值"],
    "制度": ["制度", "机制", "权责", "监督"],
    "技术": ["技术", "数字工具"],
    "数字负担": ["数字负担", "技术负担"],
    "基层减负": ["基层减负", "减负"],
    "治理路径": ["治理路径", "路径", "纠治", "治理"],
    "基层治理": ["基层治理"],
    "乡村治理": ["乡村治理"],
    "数字形式主义": ["数字形式主义", "形式主义"],
    "Cultural Lag": ["文化堕距", "三重堕距", "堕距", "技术堕距"],
    "cultural lag": ["文化堕距", "三重堕距", "堕距", "技术堕距"],
    "Bureaucratic": ["官僚制", "规则", "流程机械", "形式主义", "平台冗余"],
    "bureaucratic": ["官僚制", "规则", "流程机械", "形式主义", "平台冗余"],
    "rules": ["规则", "流程机械", "制度"],
    "discipline": ["规训", "纪律", "制度"],
    "Decision-Making": ["决策", "科学决策", "行政决策", "考核"],
    "decision-making": ["决策", "科学决策", "行政决策", "考核"],
    "Administrative": ["行政", "治理", "考核", "制度"],
    "administrative": ["行政", "治理", "考核", "制度"],
    "数字循环": ["数字循环", "形式空转", "脱离基层治理实践", "群众需要"],
    "数字隔离": ["数字隔离", "数据精确性", "基层社会模糊性", "真实情况"],
    "数字行政": ["数字行政", "数字行政平台", "政务APP", "小程序"],
    "公共价值空间": ["公共价值空间", "公共服务", "服务导向"],
    "数字素养": ["数字素养", "数字能力"],
}


def normalize(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def split_md_row(line: str) -> list[str]:
    return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]


def body_text(draft_text: str) -> str:
    return re.split(r"^##\s*参考文献\s*$", draft_text, flags=re.MULTILINE)[0]


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
            "authors": cells[2],
            "title": cells[4],
            "status": cells[1],
        }
    return sources


def parse_evidence_terms(evidence_text: str) -> dict[str, dict[str, str]]:
    current = ""
    terms: dict[str, dict[str, str]] = {}
    for line in evidence_text.splitlines():
        if line.startswith("### "):
            current = normalize(Path(line.removeprefix("### ").strip()).stem)
            terms[current] = {}
            continue
        if not current or not line.startswith("| "):
            continue
        cells = split_md_row(line)
        if len(cells) < 3 or cells[0] in {"Term", "---"}:
            continue
        pages = cells[1].strip()
        if pages and pages != "---":
            terms[current][cells[0]] = pages
    return terms


def source_key(source: dict[str, str], evidence_terms: dict[str, dict[str, str]]) -> str:
    title_norm = normalize(source["title"])
    author_norms = [normalize(part) for part in re.split(r"[；;、，,\s]+", source["authors"]) if part]
    best_score = 0
    best_key = ""
    for key in evidence_terms:
        score = 0
        if "技术治理何以影响乡镇干部行动" in source["title"] and "technicalgovernancetownshipcadres" in key:
            score += 40
        if "傅利平" in source["authors"] and "fuliping" in key:
            score += 20
        if "基层数字形式主义：表现、成因与对策" in source["title"] and "grassrootsdigitalformalism" in key:
            score += 40
        if "欧阳康" in source["authors"] and "ouyangkang" in key:
            score += 20
        if "城市基层数字平台的悬浮化" in source["title"] and "smartcodeplatform" in key:
            score += 40
        if "李春生" in source["authors"] and "lichunsheng" in key:
            score += 20
        if "数字技术何以有效赋能城市基层治理" in source["title"] and "yiwangtongguan" in key:
            score += 40
        if "顾丽梅" in source["authors"] and "gulimei" in key:
            score += 20
        if "双向激活" in source["title"] and "yuexiudigitalgovernance" in key:
            score += 40
        if "陈天祥" in source["authors"] and "chentianxiang" in key:
            score += 20
        for start in range(0, min(len(title_norm), 18), 6):
            frag = title_norm[start : start + 8]
            if frag and frag in key:
                score += len(frag)
        for author in author_norms:
            if author and author in key:
                score += 10
        if score > best_score:
            best_score = score
            best_key = key
    return best_key


def citation_occurrences(text: str) -> list[dict[str, str]]:
    body = body_text(text)
    rows: list[dict[str, str]] = []
    for number, match in enumerate(re.finditer(r"\[(\d+)\]", body), start=1):
        start = max(0, match.start() - 90)
        end = min(len(body), match.end() + 90)
        context = re.sub(r"\s+", "", body[start:end])
        rows.append({"n": str(number), "ref": match.group(1), "context": context})
    return rows


def candidate_pages(context: str, source_terms: dict[str, str]) -> tuple[str, str]:
    hits: list[str] = []
    for term, pages in source_terms.items():
        aliases = ALIASES.get(term, [term])
        if any(alias in context for alias in aliases):
            hits.append(f"{term}: {pages}")
    if hits:
        return "; ".join(hits[:5]), "candidate"
    if source_terms:
        first_terms = [f"{term}: {pages}" for term, pages in list(source_terms.items())[:3]]
        return "; ".join(first_terms), "weak_candidate"
    return "", "missing_evidence_terms"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/citation_page_suggestions.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "citation_page_suggestions.md"

    matrix_text = (run_dir / "03_文献矩阵.md").read_text(encoding="utf-8")
    draft_text = (run_dir / "06_论文初稿.md").read_text(encoding="utf-8")
    evidence_text = (run_dir / "evidence_index.md").read_text(encoding="utf-8")

    sources = parse_sources(matrix_text)
    evidence_terms = parse_evidence_terms(evidence_text)
    source_term_map: dict[int, dict[str, str]] = {}
    for idx, source in sources.items():
        key = source_key(source, evidence_terms)
        source_term_map[idx] = evidence_terms.get(key, {})

    occurrences = citation_occurrences(draft_text)
    weak = 0
    missing = 0

    lines = [
        "# Citation Page Suggestions",
        "",
        "This file suggests page candidates for body citations. It is not a final footnote formatter; verify pages before final submission.",
        "",
        "| No. | Ref | Source | Suggested pages | Confidence | Context |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for occurrence in occurrences:
        ref = int(occurrence["ref"])
        source = sources.get(ref)
        if not source:
            missing += 1
            lines.append(f"| {occurrence['n']} | [{ref}] | missing source |  | missing | {occurrence['context']} |")
            continue
        pages, confidence = candidate_pages(occurrence["context"], source_term_map.get(ref, {}))
        if confidence == "weak_candidate":
            weak += 1
        elif confidence == "missing_evidence_terms":
            missing += 1
        context = occurrence["context"].replace("|", "/")
        lines.append(f"| {occurrence['n']} | [{ref}] | {source['id']} | {pages} | {confidence} | {context} |")

    lines.extend(
        [
            "",
            f"- body_citation_occurrences: {len(occurrences)}",
            f"- weak_page_suggestions: {weak}",
            f"- missing_page_suggestions: {missing}",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"body_citation_occurrences={len(occurrences)}")
    print(f"weak_page_suggestions={weak}")
    print(f"missing_page_suggestions={missing}")
    print(f"out={out}")
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
