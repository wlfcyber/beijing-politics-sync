from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
PROJECT = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16"
EXTRACT_ROOT = PROJECT / "12_full_desktop_extract_20260524"
FINAL_DIR = PROJECT / "06_final_handbook"
OUT_MD = EXTRACT_ROOT / "XUANBIYI_FULL_SOURCE_COVERAGE_AUDIT.md"
OUT_CSV = EXTRACT_ROOT / "xuanbiyi_full_source_question_candidates.csv"

DISTRICTS = [
    "东城",
    "西城",
    "朝阳",
    "海淀",
    "丰台",
    "石景山",
    "门头沟",
    "房山",
    "通州",
    "顺义",
    "昌平",
    "大兴",
    "怀柔",
    "平谷",
    "密云",
    "延庆",
]

STAGES = ["一模", "二模", "期中", "期末", "适应性"]

XUANBIYI_TERMS = [
    "当代国际政治与经济",
    "国际政治与经济",
    "世界多极化",
    "经济全球化",
    "国家利益",
    "共同利益",
    "国际竞争",
    "综合国力",
    "新型国际关系",
    "全球治理",
    "人类命运共同体",
    "中国智慧",
    "中国方案",
    "中国力量",
    "联合国",
    "多边主义",
    "国际关系民主化",
    "国际秩序",
    "和平共处五项原则",
    "独立自主",
    "和平外交",
    "开放型世界经济",
    "贸易投资",
    "两个市场",
    "两种资源",
    "供应链",
    "产业链",
    "高水平对外开放",
    "制度型开放",
]


@dataclass
class Source:
    year: str
    suite: str
    role: str
    source: Path
    text_path: Path
    chars: int
    text: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def guess_suite(path: Path) -> tuple[str, str]:
    parts = list(path.parts)
    year = ""
    district = ""
    stage = ""
    for part in parts:
        m = re.search(r"20\d{2}", part)
        if m and not year:
            year = m.group(0)
        if not district:
            for candidate in DISTRICTS:
                if candidate in part:
                    district = candidate
                    break
        if not stage:
            for candidate in STAGES:
                if candidate in part:
                    stage = candidate
                    break
    suite = "".join(x for x in [year, district, stage] if x)
    return year, suite


def guess_role(path: Path) -> str:
    text = " ".join(path.parts).lower()
    if any(x in text for x in ["细则", "评标", "阅卷", "评分", "讲评", "标准"]):
        return "rubric"
    if "答案" in text:
        return "answer"
    if any(x in text for x in ["试卷", "教师版", "政治"]):
        return "paper"
    return "other"


def normalize_ref(s: str) -> str:
    s = s.replace("（", "(").replace("）", ")")
    s = re.sub(r"第\s*(\d+)\s*题\s*第\s*\(?(\d+)\)?\s*问", r"Q\1(\2)", s)
    s = re.sub(r"第\s*(\d+)\s*题", r"Q\1", s)
    s = re.sub(r"\s+", "", s)
    return s


def q_pattern(q: int) -> re.Pattern[str]:
    return re.compile(rf"(?<!\d)(?:第\s*{q}\s*题|Q\s*{q}\b|{q}\s*[\.．、]|{q}\s*[（(][一二三四五12345]?[)）])")


def best_context(text: str, q: int, window: int = 2200) -> str:
    matches = list(q_pattern(q).finditer(text))
    best = ""
    best_score = -1
    for m in matches[:60]:
        start = max(0, m.start() - 40)
        next_starts: list[int] = []
        for later in range(q + 1, 23):
            later_match = q_pattern(later).search(text, m.end())
            if later_match:
                next_starts.append(later_match.start())
        natural_end = min(next_starts) if next_starts else m.end() + window
        end = min(len(text), natural_end, m.end() + window)
        ctx = re.sub(r"\s+", " ", text[start:end]).strip()
        score = sum(1 for term in XUANBIYI_TERMS if term in ctx)
        if "当代国际政治与经济" in ctx:
            score += 5
        if "运用《" in ctx or "结合材料" in ctx:
            score += 1
        if "【细则】" in ctx or "评分" in ctx or "得" in ctx:
            score += 1
        if score > best_score:
            best = ctx
            best_score = score
    return best[:760]


def matched_terms(*texts: str) -> list[str]:
    merged = "\n".join(texts)
    return [term for term in XUANBIYI_TERMS if term in merged]


def load_sources() -> list[Source]:
    sources: list[Source] = []
    for manifest in sorted(EXTRACT_ROOT.glob("20*/manifest.csv")):
        with manifest.open("r", encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "ok" or not row.get("text_path"):
                    continue
                source_path = Path(row["source"])
                text_path = Path(row["text_path"])
                text = read_text(text_path)
                year, suite = guess_suite(source_path)
                if not suite:
                    continue
                sources.append(
                    Source(
                        year=year,
                        suite=suite,
                        role=guess_role(source_path),
                        source=source_path,
                        text_path=text_path,
                        chars=int(row.get("chars") or 0),
                        text=text,
                    )
                )
    return sources


def load_final_texts() -> tuple[str, str]:
    student = next(
        p
        for p in FINAL_DIR.glob("*.md")
        if "当代" in p.name and "学生版" in p.name and "backup" not in p.name
    )
    text = read_text(student)
    boundary_marker = "# 附：模块边界"
    idx = text.find(boundary_marker)
    if idx < 0:
        return normalize_ref(text), ""
    return normalize_ref(text[:idx]), normalize_ref(text[idx:])


def final_location(suite: str, question: str, final_main: str, final_boundary: str) -> str:
    key = normalize_ref(f"{suite}{question}")
    if key in final_main:
        return "main"
    if key in final_boundary:
        return "boundary"
    return "absent"


def main() -> None:
    sources = load_sources()
    final_main, final_boundary = load_final_texts()
    by_suite: dict[str, list[Source]] = defaultdict(list)
    for source in sources:
        by_suite[source.suite].append(source)

    rows: list[dict[str, str]] = []
    for suite, group in sorted(by_suite.items()):
        roles: dict[str, list[Source]] = defaultdict(list)
        for source in group:
            roles[source.role].append(source)
        for q in range(16, 23):
            paper_ctx = ""
            scoring_ctx = ""
            paper_source = ""
            scoring_source = ""
            for source in roles["paper"] + roles["answer"] + roles["other"]:
                ctx = best_context(source.text, q)
                if ctx:
                    paper_ctx = ctx
                    paper_source = str(source.source)
                    break
            for source in roles["rubric"]:
                ctx = best_context(source.text, q)
                if ctx:
                    scoring_ctx = ctx
                    scoring_source = str(source.source)
                    break
            if not paper_ctx and not scoring_ctx:
                continue
            terms = matched_terms(paper_ctx, scoring_ctx)
            book_named = "当代国际政治与经济" in paper_ctx or "当代国际政治与经济" in scoring_ctx
            has_scoring = bool(scoring_ctx)
            likely = book_named or (has_scoring and len(terms) >= 2) or any(
                term in terms for term in ["经济全球化", "世界多极化", "人类命运共同体", "新型国际关系", "联合国"]
            )
            location = final_location(suite, f"Q{q}", final_main, final_boundary)
            if likely or location != "absent":
                rows.append(
                    {
                        "suite": suite,
                        "question": f"Q{q}",
                        "likely_xuanbiyi": "yes" if likely else "no_but_in_final",
                        "final_location": location,
                        "matched_terms": "；".join(terms),
                        "book_named": "yes" if book_named else "no",
                        "has_scoring_context": "yes" if has_scoring else "no",
                        "paper_source": paper_source,
                        "scoring_source": scoring_source,
                        "paper_context": paper_ctx,
                        "scoring_context": scoring_ctx,
                    }
                )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "suite",
        "question",
        "likely_xuanbiyi",
        "final_location",
        "matched_terms",
        "book_named",
        "has_scoring_context",
        "paper_source",
        "scoring_source",
        "paper_context",
        "scoring_context",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["final_location"] for row in rows)
    likely_absent = [row for row in rows if row["likely_xuanbiyi"] == "yes" and row["final_location"] == "absent"]
    no_scoring_absent = [
        row
        for row in likely_absent
        if row["has_scoring_context"] == "no"
    ]
    scoring_absent = [
        row
        for row in likely_absent
        if row["has_scoring_context"] == "yes"
    ]

    lines = [
        "# 选必一 2024-2026 桌面原始材料覆盖反查",
        "",
        "- 口径：只反查主观题 Q16-Q22；候选来自题面/答案/细则/讲评中的《当代国际政治与经济》书名或选必一关键词。",
        "- 匹配：最终稿题源匹配已把“第20题”和“Q20”统一，避免题号写法造成误判。",
        "- 注意：本表是覆盖审计，不直接把普通参考答案升格为细则；有评分/评标/讲评上下文的缺口优先回填。",
        "",
        "## 总览",
        "",
        f"- 候选/已入终稿题源行：{len(rows)}",
        f"- 主链已出现：{counts['main']}",
        f"- 边界附录已出现：{counts['boundary']}",
        f"- 候选但当前终稿未出现：{counts['absent']}",
        f"- 其中有细则/讲评上下文仍未出现：{len(scoring_absent)}",
        f"- 其中暂只见题面/答案上下文：{len(no_scoring_absent)}",
        "",
        "## 有细则/讲评上下文但当前终稿未出现",
        "",
        "| 套卷 | 题号 | 匹配词 | 细则/讲评来源 | 细则/讲评摘录 |",
        "|---|---|---|---|---|",
    ]
    for row in scoring_absent:
        snippet = row["scoring_context"].replace("|", "｜")[:220]
        lines.append(
            f"| {row['suite']} | {row['question']} | {row['matched_terms'] or '未命中'} | `{row['scoring_source']}` | {snippet} |"
        )

    lines.extend(
        [
            "",
            "## 暂只见题面/答案上下文，需继续确认细则",
            "",
            "| 套卷 | 题号 | 匹配词 | 题面/答案来源 | 摘录 |",
            "|---|---|---|---|---|",
        ]
    )
    for row in no_scoring_absent:
        snippet = row["paper_context"].replace("|", "｜")[:220]
        lines.append(
            f"| {row['suite']} | {row['question']} | {row['matched_terms'] or '未命中'} | `{row['paper_source']}` | {snippet} |"
        )

    lines.extend(
        [
            "",
            "## 已进入边界附录",
            "",
            "| 套卷 | 题号 | 匹配词 |",
            "|---|---|---|",
        ]
    )
    for row in rows:
        if row["final_location"] == "boundary":
            lines.append(f"| {row['suite']} | {row['question']} | {row['matched_terms'] or '未命中'} |")

    lines.extend(
        [
            "",
            "## 主链已出现",
            "",
            "| 套卷 | 题号 | 匹配词 |",
            "|---|---|---|",
        ]
    )
    for row in rows:
        if row["final_location"] == "main":
            lines.append(f"| {row['suite']} | {row['question']} | {row['matched_terms'] or '未命中'} |")

    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"rows={len(rows)}")
    print(f"counts={dict(counts)}")
    print(OUT_CSV)
    print(OUT_MD)


if __name__ == "__main__":
    main()
