# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import re
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
INV = RUN / "01_source_inventory"
OUT = RUN / "02_codex_lane"
OUT.mkdir(parents=True, exist_ok=True)

TERMS = [
    "哲学与文化", "哲学角度", "哲学知识", "哲学", "唯物辩证法", "辩证法",
    "矛盾", "主要矛盾", "次要矛盾", "主要方面", "次要方面", "两点论", "重点论", "主流", "支流",
    "联系", "整体", "部分", "系统", "发展", "量变", "质变", "辩证否定", "守正创新",
    "实践", "认识", "真理", "价值观", "价值判断", "价值选择", "人民群众",
    "社会存在", "社会意识", "改革", "规律", "意识", "物质", "主观能动性",
]
STRONG_MODULE_TERMS = ["哲学与文化", "哲学角度", "哲学知识", "唯物辩证法", "辩证法"]
PATCH_TERMS = ["主要矛盾", "次要矛盾", "主要方面", "次要方面", "两点论", "重点论", "主流", "支流"]


def read_base() -> str:
    p = INV / "accepted_base_docx_text.txt"
    return p.read_text(encoding="utf-8") if p.exists() else ""


def suite_variants(name: str) -> list[str]:
    variants = {name}
    m = re.search(r"(202[456])(.+?)(一模|二模)", name)
    if m:
        year, district, phase = m.group(1), m.group(2), m.group(3)
        for noise in ["政治", "思政", "高三", "北京"]:
            district = district.replace(noise, "")
        variants.update({year + district + phase})
    return sorted(v for v in variants if len(v) >= 3)


def base_has(base_text: str, suite: str, qno: str) -> bool:
    q_patterns = [f"第{qno}题", f"{qno}题", f"{qno}（", f"{qno}."]
    for sv in suite_variants(suite):
        for qp in q_patterns:
            if sv in base_text and qp in base_text:
                # require a loose local co-occurrence, not just both anywhere.
                for m in re.finditer(re.escape(sv), base_text):
                    window = base_text[max(0, m.start() - 120): m.end() + 160]
                    if qp in window:
                        return True
    return False


def extract_file_sections(bundle_text: str) -> list[tuple[str, str, str]]:
    parts = re.split(r"\n## FILE: ", bundle_text)
    sections = []
    for part in parts[1:]:
        first, *rest = part.splitlines()
        body = "\n".join(rest)
        status = ""
        m = re.search(r"status:\s*([^\n]+)", body)
        if m:
            status = m.group(1).strip()
        sections.append((first.strip(), status, body))
    return sections


def nearest_question(text: str, pos: int) -> str:
    left = text[max(0, pos - 2500):pos]
    patterns = [
        r"第\s*([1-9]|1[0-9]|20|21)\s*题",
        r"(?m)^\s*([1-9]|1[0-9]|20|21)[\.．、]",
        r"(?m)^\s*\(([1-9]|1[0-9]|20|21)\)",
    ]
    best = None
    best_pos = -1
    for pat in patterns:
        for m in re.finditer(pat, left):
            if m.start() > best_pos:
                best = m.group(1)
                best_pos = m.start()
    return best or "unknown"


def context(text: str, pos: int, n: int = 280) -> str:
    s = max(0, pos - n)
    e = min(len(text), pos + n)
    return re.sub(r"\s+", " ", text[s:e]).strip()


def source_kind(file_name: str) -> str:
    if any(x in file_name for x in ["细则", "评标", "阅卷", "讲评", "评分"]):
        return "rubric_or_marking"
    if any(x in file_name for x in ["答案", "参考"]):
        return "answer"
    if any(x in file_name for x in ["试卷", "试题", "教师版", "学生版", "原卷"]):
        return "paper"
    return "other"


def evidence_level(kinds: set[str], strong: bool) -> str:
    if "rubric_or_marking" in kinds and strong:
        return "rubric_explicit"
    if "rubric_or_marking" in kinds:
        return "rubric_term_hit"
    if "paper" in kinds and strong:
        return "question_explicit"
    if "answer" in kinds:
        return "answer_support_only"
    return "term_hit_needs_review"


def decision(phase: str, base: bool, level: str) -> str:
    if phase == "二模":
        return "new_2026_second_mock_candidate"
    if base:
        return "base_has_local_match_verify_quality"
    if level in {"rubric_explicit", "question_explicit", "rubric_term_hit"}:
        return "possible_omission_needs_source_review"
    return "weak_hit_review_or_exclude"


def main() -> int:
    base_text = read_base()
    bundles = sorted((INV / "suite_source_bundles").glob("*.md"))
    rows: dict[tuple[str, str], dict] = {}
    hit_rows = []
    for b in bundles:
        suite = b.stem
        phase = "二模" if "二模" in suite else "一模"
        year = suite[:4] if suite[:4].isdigit() else ""
        txt = b.read_text(encoding="utf-8", errors="ignore")
        for file_name, status, body in extract_file_sections(txt):
            kind = source_kind(file_name)
            for term in TERMS:
                start = 0
                while True:
                    pos = body.find(term, start)
                    if pos == -1:
                        break
                    qno = nearest_question(body, pos)
                    key = (suite, qno)
                    strong = term in STRONG_MODULE_TERMS
                    patch = term in PATCH_TERMS
                    row = rows.setdefault(key, {
                        "suite": suite,
                        "year": year,
                        "phase": phase,
                        "question_no": qno,
                        "terms": set(),
                        "source_kinds": set(),
                        "strong_module_hit": False,
                        "patch_term_hit": False,
                        "example_context": "",
                    })
                    row["terms"].add(term)
                    row["source_kinds"].add(kind)
                    row["strong_module_hit"] = row["strong_module_hit"] or strong
                    row["patch_term_hit"] = row["patch_term_hit"] or patch
                    if not row["example_context"]:
                        row["example_context"] = context(body, pos)
                    hit_rows.append({
                        "suite": suite,
                        "question_no": qno,
                        "file": file_name,
                        "source_kind": kind,
                        "term": term,
                        "context": context(body, pos),
                    })
                    start = pos + len(term)

    matrix = []
    for row in rows.values():
        kinds = set(row["source_kinds"])
        level = evidence_level(kinds, bool(row["strong_module_hit"]))
        base = base_has(base_text, row["suite"], row["question_no"]) if row["question_no"] != "unknown" else False
        matrix.append({
            "suite": row["suite"],
            "year": row["year"],
            "phase": row["phase"],
            "question_no": row["question_no"],
            "module_judgment": "philosophy_candidate" if row["strong_module_hit"] else "philosophy_term_candidate",
            "evidence_level": level,
            "base_status": "base_local_match" if base else "base_no_local_match",
            "proposed_framework_node": "TO_BE_PLACED_BY_SOURCE_REVIEW",
            "decision": decision(row["phase"], base, level),
            "terms": " | ".join(sorted(row["terms"])),
            "source_kinds": " | ".join(sorted(kinds)),
            "patch_term_hit": "yes" if row["patch_term_hit"] else "no",
            "note": row["example_context"],
        })
    matrix.sort(key=lambda r: (r["year"], r["phase"], r["suite"], int(r["question_no"]) if r["question_no"].isdigit() else 99))

    with (OUT / "codex_a_term_hits.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["suite", "question_no", "file", "source_kind", "term", "context"])
        writer.writeheader()
        writer.writerows(hit_rows)
    with (OUT / "codex_a_coverage_matrix.csv").open("w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["suite", "year", "phase", "question_no", "module_judgment", "evidence_level", "base_status", "proposed_framework_node", "decision", "terms", "source_kinds", "patch_term_hit", "note"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(matrix)

    omissions = [r for r in matrix if r["phase"] == "一模" and r["decision"] == "possible_omission_needs_source_review"]
    second = [r for r in matrix if r["phase"] == "二模"]
    patch = [r for r in matrix if r["patch_term_hit"] == "yes"]
    report = [
        "# Codex A 题号级初审报告",
        "",
        f"- candidate_question_rows: {len(matrix)}",
        f"- first_mock_possible_omissions: {len(omissions)}",
        f"- second_mock_candidates: {len(second)}",
        f"- main_minor_contradiction_patch_hits: {len(patch)}",
        "",
        "## 一模疑似遗漏或需回源复核",
    ]
    for r in omissions:
        report.append(f"- {r['suite']} 第{r['question_no']}题 | {r['evidence_level']} | {r['terms']} | {r['note'][:180]}")
    report.extend(["", "## 2026二模候选题号"])
    for r in second:
        report.append(f"- {r['suite']} 第{r['question_no']}题 | {r['evidence_level']} | {r['terms']} | {r['note'][:180]}")
    report.extend(["", "## 主次矛盾/矛盾主次方面/两点论重点论专项命中"])
    for r in patch:
        report.append(f"- {r['suite']} 第{r['question_no']}题 | {r['phase']} | {r['terms']} | base={r['base_status']}")
    (OUT / "codex_a_audit_report.md").write_text("\n".join(report), encoding="utf-8")

    with (OUT / "codex_a_second_mock_insert_candidates_from_old_and_source.csv").open("w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["suite", "question_no", "evidence_level", "terms", "source_kinds", "note"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in second:
            writer.writerow({k: r[k] for k in fieldnames})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
