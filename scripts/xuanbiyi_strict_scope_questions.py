from __future__ import annotations

import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
OUT_DIR = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16" / "11_strict_final_rebuild_2026-05-23"
EXTRACTION_LOG = OUT_DIR / "01_extraction_log.csv"
SCOPE_CSV = OUT_DIR / "02_subjective_question_scope.csv"
SCOPE_MD = OUT_DIR / "02_subjective_question_scope.md"

Q_NUMS = [str(n) for n in range(16, 23)]
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
]


@dataclass
class QuestionScope:
    suite: str
    year_root: str
    year: str
    district: str
    stage: str
    question: str
    paper_files: list[str]
    rubric_files: list[str]
    answer_files: list[str]
    lecture_files: list[str]
    other_files: list[str]
    paper_evidence: str
    scoring_evidence: str
    likely_xuanbiyi: str
    matched_terms: str
    evidence_status: str
    next_action: str


def read_text(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def question_pattern(q: str) -> re.Pattern[str]:
    return re.compile(
        rf"(?<!\d)(?:第\s*{q}\s*题|{q}\s*[\.．、]|{q}\s*[（(][一二三四五12345]?[)）])"
    )


def best_context(text: str, q: str, window: int = 260) -> str:
    pat = question_pattern(q)
    matches = list(pat.finditer(text))
    if not matches:
        return ""
    # Prefer contexts that also mention one of the xuanbiyi terms.
    best = ""
    best_score = -1
    for match in matches[:30]:
        start = max(0, match.start() - 60)
        end = min(len(text), match.end() + window)
        ctx = re.sub(r"\s+", " ", text[start:end]).strip()
        score = sum(1 for term in XUANBIYI_TERMS if term in ctx)
        if score > best_score:
            best = ctx
            best_score = score
    return best[:520]


def mentioned_questions(text: str) -> set[str]:
    found: set[str] = set()
    for q in Q_NUMS:
        if question_pattern(q).search(text):
            found.add(f"Q{q}")
    return found


def matched_terms(*texts: str) -> list[str]:
    merged = "\n".join(texts)
    return [term for term in XUANBIYI_TERMS if term in merged]


def evidence_status(roles: dict[str, list[dict[str, str]]], q: str) -> str:
    scoring_roles = ["rubric", "lecture"]
    for role in scoring_roles:
        for item in roles.get(role, []):
            if question_pattern(q).search(read_text(item["text_path"])):
                return "scoring_located"
    for item in roles.get("answer", []):
        if question_pattern(q).search(read_text(item["text_path"])):
            return "answer_only"
    return "scoring_not_located"


def output_status(status: str, terms: list[str]) -> tuple[str, str]:
    if status == "scoring_located" and terms:
        return "candidate_xuanbiyi_review", "进入覆盖对照，判断是否已入库或需补录"
    if status == "scoring_located":
        return "non_xuanbiyi_or_unclear", "保留细则证据，后续按模块边界复核"
    if status == "answer_only" and terms:
        return "xuanbiyi_answer_only", "继续寻找细则；未定位前不得入主表"
    return "evidence_or_module_review", "继续回源检索或排除为其他模块"


def main() -> None:
    with EXTRACTION_LOG.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        suite = row["suite_guess"] or f"{row['year_root']}__未识别"
        grouped[suite].append(row)

    scopes: list[QuestionScope] = []
    for suite, items in sorted(grouped.items()):
        by_role: dict[str, list[dict[str, str]]] = defaultdict(list)
        for item in items:
            by_role[item["role"]].append(item)
        found_questions: set[str] = set()
        for item in items:
            text = read_text(item["text_path"])
            found_questions |= mentioned_questions(text)
        if not found_questions:
            # Keep a conservative default for paper/rubric files that may be image-only.
            if any(item["role"] in {"paper", "rubric", "lecture", "answer"} for item in items):
                found_questions = {f"Q{q}" for q in Q_NUMS}
        for qid in sorted(found_questions, key=lambda x: int(x[1:])):
            q = qid[1:]
            paper_ctx = ""
            for item in by_role.get("paper", []) + by_role.get("answer", []):
                paper_ctx = best_context(read_text(item["text_path"]), q)
                if paper_ctx:
                    break
            scoring_ctx = ""
            for item in by_role.get("rubric", []) + by_role.get("lecture", []):
                scoring_ctx = best_context(read_text(item["text_path"]), q)
                if scoring_ctx:
                    break
            terms = matched_terms(paper_ctx, scoring_ctx)
            status = evidence_status(by_role, q)
            likely, next_action = output_status(status, terms)
            first = items[0]
            scopes.append(
                QuestionScope(
                    suite=suite,
                    year_root=first["year_root"],
                    year=first["year"],
                    district=first["district"],
                    stage=first["stage"],
                    question=qid,
                    paper_files=[item["absolute_path"] for item in by_role.get("paper", [])],
                    rubric_files=[item["absolute_path"] for item in by_role.get("rubric", [])],
                    answer_files=[item["absolute_path"] for item in by_role.get("answer", [])],
                    lecture_files=[item["absolute_path"] for item in by_role.get("lecture", [])],
                    other_files=[item["absolute_path"] for item in by_role.get("other", [])],
                    paper_evidence=paper_ctx,
                    scoring_evidence=scoring_ctx,
                    likely_xuanbiyi=likely,
                    matched_terms="；".join(terms),
                    evidence_status=status,
                    next_action=next_action,
                )
            )

    fields = list(QuestionScope.__dataclass_fields__.keys())
    with SCOPE_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in scopes:
            data = row.__dict__.copy()
            for key, value in list(data.items()):
                if isinstance(value, list):
                    data[key] = "\n".join(value)
            writer.writerow(data)

    lines = [
        "# 选必一严格最终版主观题范围初筛",
        "",
        f"- 题目候选数：{len(scopes)}",
        "- 说明：本表是全量初筛，不等于最终入库；`细则未定位` 类题目后续继续回源检索。",
        "",
        "## 疑似选必一或需继续找细则",
        "",
        "| 套卷 | 题号 | 状态 | 匹配词 | 证据状态 |",
        "|---|---|---|---|---|",
    ]
    for row in scopes:
        if "xuanbiyi" in row.likely_xuanbiyi or row.evidence_status != "scoring_located":
            lines.append(
                f"| {row.suite} | {row.question} | {row.likely_xuanbiyi} | {row.matched_terms or '未命中'} | {row.evidence_status} |"
            )
    lines.extend(["", "## 全量题目", "", "| 套卷 | 题号 | 状态 | 证据状态 |", "|---|---|---|---|"])
    for row in scopes:
        lines.append(f"| {row.suite} | {row.question} | {row.likely_xuanbiyi} | {row.evidence_status} |")
    SCOPE_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"scope_rows={len(scopes)}")
    print(SCOPE_CSV)
    print(SCOPE_MD)


if __name__ == "__main__":
    main()
