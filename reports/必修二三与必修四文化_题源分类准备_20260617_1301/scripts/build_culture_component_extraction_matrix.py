#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "strong_blocker_resolved_classification_matrix.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "culture_component_extracted_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "culture_component_extraction_audit.csv"
OUT_REVIEW = RUN_DIR / "05_reports" / "culture_component_extraction_review.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "culture_component_extracted_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "culture_component_extraction_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


ROW_RESOLUTIONS: dict[tuple[str, str], dict[str, str]] = {
    ("2026_西城_二模", "2"): {
        "module": "B4_CULTURE",
        "rule_id": "CULTURE_FULL_OBJECTIVE_MILU_CULTURAL_SYMBOL",
        "matched_terms": "中华文化主体性,文化自信,中华优秀传统文化,文化基因",
    },
    ("2026_顺义_一模", "2"): {
        "module": "B4_CULTURE",
        "rule_id": "CULTURE_FULL_OBJECTIVE_BEIJING_THEATRE_INNOVATION",
        "matched_terms": "北京题材,创新文化呈现方式,建都历史,文化表达",
    },
}


ORIGINAL_REMAINDER_RESOLUTIONS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_丰台_二模", "21"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_COMPONENT_EXTRACTED_REMAINDER_PHILOSOPHY_B1",
    },
    ("2024_海淀_一模", "16"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_COMPONENT_EXTRACTED_REMAINDER_PHILOSOPHY",
    },
    ("2024_海淀_期中", "16"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_COMPONENT_EXTRACTED_REMAINDER_PHILOSOPHY",
    },
}


COMPONENTS: list[dict[str, str]] = [
    {
        "suite_id": "2024_丰台_二模",
        "parent_question": "21",
        "rule_id": "CULTURE_COMPONENT_NATIONAL_SPIRIT_STEPS_OF_CHINA",
        "matched_terms": "弘扬民族精神,理想信念,个人与国家",
        "basis": "细则拓展答案明确把“弘扬民族精神”列入认知层面；民族精神属于文化。",
        "manual_evidence": "结合材料,综合运用所学,谈谈对“你的步伐就是中国的步伐”的理解。细则拓展答案: 认知层面:价值观、理想信念、弘扬民族精神; 实践层面:担当责任、砥砺奋斗。",
    },
    {
        "suite_id": "2024_海淀_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_NATIONAL_SPIRIT_DREAM_BOAT",
        "matched_terms": "民族精神,梦舟,揽月,航天梦,诗词意象",
        "basis": "评分细则明确“可从……民族精神等角度作答”；民族精神属于文化。",
        "preferred_source_type": "rubric",
    },
    {
        "suite_id": "2024_海淀_期中",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_CULTURAL_CONFIDENCE_DREAM_BOAT_PARALLEL",
        "matched_terms": "梦舟,揽月,毛泽东诗词,航天梦,文化自信",
        "basis": "题面与 2024 海淀一模同源，属于《哲学与文化》混合题；文化命名、诗词意象和航天梦部分进入文化组件。",
    },
    {
        "suite_id": "2024_朝阳_二模",
        "parent_question": "19",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_CULTURE_MODERNIZATION",
        "matched_terms": "中华优秀传统文化,中国式现代化,深厚底蕴",
        "basis": "细则中第 19 题文化小问要求理解“中华优秀传统文化的特质赋予中国式现代化以深厚底蕴”。",
    },
    {
        "suite_id": "2024_石景山_一模",
        "parent_question": "3",
        "rule_id": "CULTURE_COMPONENT_CITY_SPIRIT",
        "matched_terms": "城市精神,爱国精神,历史文化,价值追求",
        "basis": "题面围绕北京市民精神、城市精神和历史孕育的价值追求，文化成分不能被社会意识/哲学边界吞掉。",
    },
    {
        "suite_id": "2025_东城_期末",
        "parent_question": "21",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_CULTURE_MUSEUM",
        "matched_terms": "中华优秀传统文化,博物馆,传统文化",
        "basis": "整题虽含哲学角度，但文化材料和文化采分点明确，应抽取文化组件。",
    },
    {
        "suite_id": "2025_房山_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_MUSEUM_HEAT_RUBRIC",
        "matched_terms": "优秀文化的传承,创造性转化,创新性发展,文化自信,文化功能",
        "basis": "细则明确文化 4 分、哲学 3 分；文化 4 分必须独立进入文化宝典准备账本。",
    },
    {
        "suite_id": "2025_朝阳_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_CULTURE_INHERITANCE",
        "matched_terms": "中华优秀传统文化,文化传承,中华文明",
        "basis": "题面/答案含中华优秀传统文化与文化传承，原哲学边界只能排除非文化余项，不能抹掉文化采分点。",
    },
    {
        "suite_id": "2025_门头沟_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_CULTURE_DOUBLE_CREATION",
        "matched_terms": "中华优秀传统文化,创造性转化,创新性发展,文化自信",
        "basis": "题面/细则具有传统文化双创与文化自信成分，应抽入文化组件。",
    },
    {
        "suite_id": "2025_顺义_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_CULTURE_CONFIDENCE",
        "matched_terms": "中华优秀传统文化,创造性转化,创新性发展,文化自信",
        "basis": "题面/细则具有传统文化双创与文化自信成分，应抽入文化组件。",
    },
    {
        "suite_id": "2026_延庆_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_INTANGIBLE_HERITAGE_CREATIVE_PRODUCT",
        "matched_terms": "非遗,文创,文化创新",
        "basis": "非遗和文创属于文化成分；哲学方法论余项不应吞掉文化材料。",
    },
    {
        "suite_id": "2026_延庆_一模",
        "parent_question": "4",
        "rule_id": "CULTURE_COMPONENT_CULTURE_CARRIER_DOUBLE_CREATION",
        "matched_terms": "文化载体,创造性转化",
        "basis": "客观题判断点出现文化载体和创造性转化，应抽为文化组件。",
    },
    {
        "suite_id": "2026_朝阳_一模",
        "parent_question": "3",
        "rule_id": "CULTURE_COMPONENT_SCIENCE_CULTURE_INTANGIBLE_HERITAGE",
        "matched_terms": "传统文化,文化自信,非遗,科技赋能",
        "basis": "客观题同时有文化与哲学判断点；文化自信、非遗、传统文化部分单独抽入文化组件。",
    },
    {
        "suite_id": "2026_朝阳_一模",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_CULTURE_CONFIDENCE",
        "matched_terms": "中华优秀传统文化,文化自信",
        "basis": "原判为哲学边界，但文化自信和中华优秀传统文化是明确文化采分点。",
    },
    {
        "suite_id": "2026_海淀_二模",
        "parent_question": "2",
        "rule_id": "CULTURE_COMPONENT_MUSEUM_CULTURE_SERVICE",
        "matched_terms": "博物馆,文化事业,文物",
        "basis": "客观题文化事业、博物馆和文物判断点应进入文化组件。",
    },
    {
        "suite_id": "2026_石景山_二模",
        "parent_question": "2",
        "rule_id": "CULTURE_COMPONENT_INTANGIBLE_HERITAGE_NATIONAL_SPIRIT",
        "matched_terms": "非遗,爱国主义,民族精神",
        "basis": "题面和选项明确非遗作品承载爱国主义为核心的民族精神；民族精神属于文化。",
    },
    {
        "suite_id": "2026_西城_期末",
        "parent_question": "16",
        "rule_id": "CULTURE_COMPONENT_DOCUMENTARY_CULTURAL_CONFIDENCE",
        "matched_terms": "文化自信,中华优秀传统文化,文化创新",
        "basis": "第 16 题第 (1) 问参考答案为文化自信完整采分链，需独立进入文化组件。",
    },
    {
        "suite_id": "2026_通州_一模",
        "parent_question": "18",
        "rule_id": "CULTURE_COMPONENT_LONGFU_TEMPLE_TRADITION_INNOVATION",
        "matched_terms": "中华优秀传统文化,创新性发展,非遗,历史文脉",
        "basis": "隆福寺题答案同时含哲学和文化；其中传统文化双创、非遗、历史文脉为文化组件。",
    },
    {
        "suite_id": "2026_丰台_期末",
        "parent_question": "6",
        "rule_id": "CULTURE_COMPONENT_CHINESE_KNOT_TRADITIONAL_CULTURE",
        "matched_terms": "中国结,中华优秀传统文化,精神追求",
        "basis": "raw source 已确认该选择题同时涉及中华优秀传统文化与逻辑思维；文化部分需抽离。",
        "manual_evidence": "中国结是我国传统的手工艺品，造型独特、色彩多样、内涵丰富；选项同时涉及中华优秀传统文化、精神追求、形象思维和抽象思维。",
    },
    {
        "suite_id": "2026_丰台_期末",
        "parent_question": "2",
        "rule_id": "CULTURE_COMPONENT_TRADITIONAL_VIRTUE_ELDERLY_SERVICES",
        "matched_terms": "孝亲敬老,传统美德",
        "basis": "raw source 已确认该选择题同时涉及基本公共服务、群众观点、孝亲敬老传统美德和社会治理；传统美德部分需抽离。",
        "manual_evidence": "选项同时涉及差异化基本公共服务、群众观点、孝亲敬老传统美德和社会治理方式。",
    },
]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 1200) -> str:
    return re.sub(r"\s+", " ", text or "").strip()[:limit]


def parse_score(reason: str, key: str) -> int:
    try:
        value = json.loads(reason).get(key, 0)
        return int(value or 0)
    except Exception:
        return 0


def best_evidence(
    candidates: dict[tuple[str, str], list[dict[str, str]]],
    component: dict[str, str],
) -> tuple[str, str, str]:
    if component.get("manual_evidence"):
        return "manual_verified_note", "", compact(component["manual_evidence"], 1200)

    key = (component["suite_id"], component["parent_question"])
    rows = candidates.get(key, [])
    terms = [term.strip() for term in component["matched_terms"].split(",") if term.strip()]
    preferred_types = {"rubric", "reference-answer", "paper", "ocr-cache"}
    scored: list[tuple[int, dict[str, str]]] = []
    for row in rows:
        if row.get("source_type") not in preferred_types:
            continue
        text = row.get("snippet", "")
        score = sum(1 for term in terms if term and term in text)
        if component.get("preferred_source_type") == row.get("source_type"):
            score += 5
        if row.get("source_type") in {"rubric", "reference-answer"}:
            score += 2
        elif row.get("source_type") in {"paper", "ocr-cache"}:
            score += 1
        scored.append((score, row))
    if not scored:
        return "", "", ""
    scored.sort(key=lambda item: item[0], reverse=True)
    row = scored[0][1]
    return row.get("source_type", ""), row.get("run_text_path", ""), compact(row.get("snippet", ""), 1200)


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    candidates_raw = load_csv(QUESTION_CANDIDATES)
    candidates: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in candidates_raw:
        candidates[(row["suite_id"], row["question"])].append(row)

    row_by_key = {(row["suite_id"], row["question"]): row for row in rows}
    missing = []
    for key in set(ROW_RESOLUTIONS) | set(ORIGINAL_REMAINDER_RESOLUTIONS):
        if key not in row_by_key:
            missing.append(key)
    for component in COMPONENTS:
        key = (component["suite_id"], component["parent_question"])
        if key not in row_by_key:
            missing.append(key)
    if missing:
        raise SystemExit(f"missing parent rows: {sorted(missing)}")

    out_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    review_rows: list[dict[str, str]] = []
    row_resolution_audit: list[dict[str, str]] = []

    component_parent_keys = {(item["suite_id"], item["parent_question"]) for item in COMPONENTS}

    for row in rows:
        key = (row["suite_id"], row["question"])
        original = dict(row)
        resolution = ROW_RESOLUTIONS.get(key)
        remainder = ORIGINAL_REMAINDER_RESOLUTIONS.get(key)
        if resolution:
            if row["status"] == "reference-only":
                raise SystemExit(f"refusing to rewrite reference-only row {key}")
            module = resolution["module"]
            status = "included" if module in TARGET_MODULES else "module-boundary-excluded"
            row = dict(row)
            row.update(
                {
                    "book_module": module,
                    "status": status,
                    "artifact_location": "05_reports/culture_component_extraction_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": resolution["rule_id"],
                            "matched_terms": resolution["matched_terms"],
                            "source": "culture_component_extraction_review.csv",
                            "prior_book_module": original["book_module"],
                            "prior_status": original["status"],
                            "user_rule": "民族精神及明确文化判断点属于文化；哲学文化混合题需抽离文化部分。",
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": "future_baodian_intake",
                    "integration_status": "culture_component_row_resolution",
                }
            )
            row_resolution_audit.append(
                {
                    "suite_id": key[0],
                    "question": key[1],
                    "operation": "resolve_original_row",
                    "prior_book_module": original["book_module"],
                    "prior_status": original["status"],
                    "new_book_module": module,
                    "new_status": status,
                    "rule_id": resolution["rule_id"],
                    "matched_terms": resolution["matched_terms"],
                    "basis": "objective row is culture-dominant after applying user rule",
                }
            )
        elif remainder:
            if row["status"] != "blocked":
                # Already-excluded rows can stay as they are; only blocked parents
                # need their non-culture remainder closed after component extraction.
                pass
            else:
                module = remainder["module"]
                row = dict(row)
                row.update(
                    {
                        "book_module": module,
                        "status": "module-boundary-excluded",
                        "artifact_location": "05_reports/culture_component_extraction_audit.csv",
                        "decision_reason": json.dumps(
                            {
                                "rule_id": remainder["rule_id"],
                                "source": "culture_component_extraction_review.csv",
                                "prior_book_module": original["book_module"],
                                "prior_status": original["status"],
                                "user_rule": "文化采分点已抽离；原父题余项按非文化边界保留。",
                            },
                            ensure_ascii=False,
                        ),
                        "next_action": "culture_component_extracted_remainder_excluded",
                        "integration_status": "culture_component_parent_remainder_closed",
                    }
                )
                row_resolution_audit.append(
                    {
                        "suite_id": key[0],
                        "question": key[1],
                        "operation": "close_parent_remainder",
                        "prior_book_module": original["book_module"],
                        "prior_status": original["status"],
                        "new_book_module": module,
                        "new_status": "module-boundary-excluded",
                        "rule_id": remainder["rule_id"],
                        "matched_terms": "",
                        "basis": "culture component extracted; parent remainder is non-culture",
                    }
                )
        out_rows.append(row)

        if key in component_parent_keys:
            review_rows.append(
                {
                    "suite_id": key[0],
                    "parent_question": key[1],
                    "prior_status": original["status"],
                    "prior_book_module": original["book_module"],
                    "target_score": str(parse_score(original["decision_reason"], "target_score")),
                    "boundary_score": str(parse_score(original["decision_reason"], "boundary_score")),
                    "review_result": "culture_component_added",
                }
            )

    existing_keys = {(row["suite_id"], row["question"]) for row in out_rows}
    for component in COMPONENTS:
        parent_key = (component["suite_id"], component["parent_question"])
        parent = row_by_key[parent_key]
        component_question = f"{component['parent_question']}#B4_CULTURE_COMPONENT"
        key = (component["suite_id"], component_question)
        if key in existing_keys:
            raise SystemExit(f"component key already exists: {key}")
        evidence_source_type, evidence_source, evidence_text = best_evidence(candidates, component)
        new = {field: "" for field in fields}
        new.update(
            {
                "suite_id": parent["suite_id"],
                "year": parent["year"],
                "district": parent["district"],
                "stage": parent["stage"],
                "question": component_question,
                "parent_question": component["parent_question"],
                "row_granularity": "culture_component",
                "book_module": "B4_CULTURE",
                "question_type": parent["question_type"],
                "evidence_source": evidence_source or parent.get("evidence_source", ""),
                "source_types": parent.get("source_types", ""),
                "status": "included",
                "artifact_location": "05_reports/culture_component_extraction_audit.csv",
                "decision_reason": json.dumps(
                    {
                        "rule_id": component["rule_id"],
                        "matched_terms": component["matched_terms"],
                        "basis": component["basis"],
                        "source": "culture_component_extraction_review.csv",
                        "parent_prior_book_module": parent["book_module"],
                        "parent_prior_status": parent["status"],
                        "user_rule": "哲学文化混合题需抽离文化采分点；民族精神属于文化。",
                    },
                    ensure_ascii=False,
                ),
                "next_action": "future_baodian_intake_culture_component",
                "integration_status": "culture_component_extraction",
            }
        )
        out_rows.append(new)
        existing_keys.add(key)
        audit_rows.append(
            {
                "suite_id": component["suite_id"],
                "parent_question": component["parent_question"],
                "component_question": component_question,
                "question_type": parent["question_type"],
                "parent_prior_status": parent["status"],
                "parent_prior_book_module": parent["book_module"],
                "rule_id": component["rule_id"],
                "matched_terms": component["matched_terms"],
                "basis": component["basis"],
                "evidence_source_type": evidence_source_type,
                "evidence_source": evidence_source,
                "evidence_text": evidence_text,
            }
        )

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(OUT_AUDIT, audit_rows, [
        "suite_id", "parent_question", "component_question", "question_type",
        "parent_prior_status", "parent_prior_book_module", "rule_id", "matched_terms",
        "basis", "evidence_source_type", "evidence_source", "evidence_text",
    ])
    write_csv(OUT_REVIEW, review_rows, [
        "suite_id", "parent_question", "prior_status", "prior_book_module",
        "target_score", "boundary_score", "review_result",
    ])
    write_csv(RUN_DIR / "05_reports" / "culture_component_row_resolution_audit.csv", row_resolution_audit, [
        "suite_id", "question", "operation", "prior_book_module", "prior_status",
        "new_book_module", "new_status", "rule_id", "matched_terms", "basis",
    ])
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    row_granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})
    remaining_blocked = sum(1 for row in out_rows if row["status"] == "blocked")
    component_count = sum(1 for row in out_rows if row["row_granularity"] == "culture_component")

    report = f"""# Culture Component Extraction Report

Generated from `{IN_MATRIX.name}`.

## Scope

- User rule applied: 哲学文化混合题需要抽离题面和细则中的文化部分；民族精神属于文化。
- Culture component rows added: {len(audit_rows)}
- Original rows resolved or remainder-closed: {len(row_resolution_audit)}
- Remaining blocked rows: {remaining_blocked}

## Matrix Counts

- Rows: {len(out_rows)}
- Status counts: {dict(status_counts)}
- Included module counts: {dict(included_counts)}
- Row granularity counts: {dict(row_granularity_counts)}
- Culture component rows: {component_count}
- Duplicate `(suite_id, question)` keys: {duplicate_keys}

## Rule Boundary

This pass does not treat every cultural word in a material as a B4_CULTURE answer point. It only adds a component when the question, answer, rubric, or manually verified source signal shows a culture judgment or scoring angle. Cross-book legal, logic, or international rows remain excluded unless a culture component is explicitly extracted and recorded.

## Deliverables

- `{OUT_REVIEW.relative_to(RUN_DIR)}`
- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `05_reports/culture_component_row_resolution_audit.csv`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
