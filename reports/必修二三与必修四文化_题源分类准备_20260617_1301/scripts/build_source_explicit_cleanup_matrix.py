#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "remaining_strong_cleanup_classification_matrix.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
SUBQUESTION_MATRIX = RUN_DIR / "04_module_classification" / "subquestion_split_matrix.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "source_explicit_cleanup_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "source_explicit_cleanup_audit.csv"
OUT_COMPONENT_AUDIT = RUN_DIR / "05_reports" / "source_explicit_target_component_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "source_explicit_cleanup_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "source_explicit_cleanup_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


ROW_RESOLUTIONS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_东城_二模", "3"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_B4P_MAQUE_PHILOSOPHY_CHOICE",
        "matched_terms": "解剖麻雀,矛盾普遍性,个性共性,系统观念",
    },
    ("2025_朝阳_二模", "18"): {
        "module": "B2_ECONOMICS",
        "rule_id": "SOURCE_EXPLICIT_B2_SOCIAL_SECURITY_PROMPT",
        "matched_terms": "运用《经济与社会》知识,社会保障,医保,个人养老金,劳动者社保",
    },
    ("2025_朝阳_二模", "21"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_XB1_NEIGHBORHOOD_DIPLOMACY_PROMPT",
        "matched_terms": "运用《当代国际政治与经济》知识,周边工作,周边命运共同体,元首外交",
    },
    ("2025_朝阳_期末", "17"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_PEOPLE_DEMOCRACY_PROMPT",
        "matched_terms": "运用《政治与法治》知识,人民民主,基层立法联系点,政协,基层群众自治",
    },
    ("2026_东城_期末", "19"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_REFORM_AND_RULE_OF_LAW_PROMPT",
        "matched_terms": "运用《政治与法治》知识,法治中国建设,改革与法治,法治政府,法治社会",
    },
    ("2026_丰台_期末", "19"): {
        "module": "B2_ECONOMICS",
        "rule_id": "SOURCE_EXPLICIT_B2_AI_DEVELOPMENT_PROMPT",
        "matched_terms": "运用《经济与社会》知识,人工智能,完整产业体系,超大规模市场,高质量发展",
    },
    ("2026_海淀_期末", "18"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_PEOPLE_CITY_GOVERNANCE_PROMPT",
        "matched_terms": "运用《政治与法治》知识,人民城市,党建引领,人大代表,政府治理",
    },
    ("2026_海淀_期末", "19"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_TWO_COMMITTEES_LAW_PROMPT",
        "matched_terms": "运用《政治与法治》知识,村民委员会组织法,居民委员会组织法,基层群众自治",
    },
    ("2026_海淀_期末", "20"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_RED_RESOURCE_PROCURATORATE_PROMPT",
        "matched_terms": "运用《政治与法治》知识,检察公益诉讼,行政机关依法履职,文物保护",
    },
    ("2026_西城_期末", "18"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_PROCURATORATE_PUBLIC_INTEREST_PROMPT",
        "matched_terms": "运用《政治与法治》知识,检察公益诉讼,人大代表,政协委员,全过程人民民主",
    },
}


PARENT_REMAINDERS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_海淀_二模", "18"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB1_DEMOCRACY_FORUM",
    },
    ("2025_东城_期末", "19(3)"): {
        "module": "XB2_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB2_NEIGHBOR_RELATION",
    },
    ("2025_丰台_一模", "20"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB1_TWO_ZONES_OPENING",
    },
    ("2025_石景山_一模", "17"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB1_BEIJING_DECLARATIONS",
    },
    ("2026_房山_一模", "18"): {
        "module": "XB3_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB3_ECOLOGICAL_GOVERNANCE",
    },
    ("2026_朝阳_一模", "17"): {
        "module": "XB3_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB3_MUSEUM_CREATIVE_DESIGN",
    },
    ("2026_海淀_一模", "18"): {
        "module": "XB2_EXCLUDED",
        "rule_id": "SOURCE_EXPLICIT_PARENT_REMAINDER_XB2_CONSUMER_RIGHTS",
    },
}


COMPONENTS: list[dict[str, str]] = [
    {
        "suite_id": "2024_海淀_二模",
        "parent_question": "18",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_COMPONENT_CHINESE_DEMOCRACY_PRACTICE",
        "matched_terms": "运用《政治与法治》知识,中国民主独特实践,人大代表,政协委员,全过程人民民主",
        "basis": "第18题(2)明确限定《政治与法治》；第18题(1)为《当代国际政治与经济》余项。",
    },
    {
        "suite_id": "2025_丰台_一模",
        "parent_question": "20",
        "module": "B2_ECONOMICS",
        "rule_id": "SOURCE_EXPLICIT_B2_COMPONENT_TWO_ZONES_OPEN_ECONOMY",
        "matched_terms": "运用《经济与社会》《当代国际政治与经济》知识,两区建设,开放型经济,营商环境",
        "basis": "设问同时限定《经济与社会》和《当代国际政治与经济》；其中开放型经济的经济制度、营商环境和高质量发展部分抽入 B2。",
    },
    {
        "suite_id": "2025_石景山_一模",
        "parent_question": "17",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_COMPONENT_COMPLAINT_HANDLING_GOVERNANCE",
        "matched_terms": "运用《政治与法治》知识,接诉即办,党建引领,人大常委会,全过程人民民主",
        "basis": "第17题材料一明确要求用《政治与法治》说明接诉即办改革；材料二为《当代国际政治与经济》余项。",
    },
    {
        "suite_id": "2026_房山_一模",
        "parent_question": "18",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_COMPONENT_ECOLOGICAL_CODE_LEGISLATION",
        "matched_terms": "运用《政治与法治》知识,生态环境法典,科学立法,全国人大,人民检察院",
        "basis": "第18题(2)明确限定《政治与法治》；第18题(1)为辩证思维方法余项。",
    },
    {
        "suite_id": "2026_朝阳_一模",
        "parent_question": "17",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "SOURCE_EXPLICIT_B3_COMPONENT_MUSEUM_CITY_GOVERNANCE",
        "matched_terms": "运用《政治与法治》知识,博物馆事业,政府,公共文化服务,多元共治",
        "basis": "第17题(2)明确限定《政治与法治》；第17题(1)为《逻辑与思维》余项。",
    },
    {
        "suite_id": "2026_海淀_一模",
        "parent_question": "18",
        "module": "B2_ECONOMICS",
        "rule_id": "SOURCE_EXPLICIT_B2_COMPONENT_SERVICE_CONSUMPTION",
        "matched_terms": "运用《经济与社会》知识,服务消费,经济高质量发展,扩大内需,产业结构优化",
        "basis": "第18题(2)明确限定《经济与社会》；第18题(3)为《法律与生活》余项。",
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


def score_rows(rows: list[dict[str, str]], terms_csv: str) -> list[tuple[int, dict[str, str]]]:
    terms = [term.strip("《》 ") for term in terms_csv.split(",") if term.strip()]
    scored = []
    for row in rows:
        if row.get("source_type") not in {"paper", "ocr-cache", "rubric", "reference-answer"}:
            continue
        text = row.get("snippet", "")
        score = sum(1 for term in terms if term and term in text)
        if row.get("source_type") in {"paper", "ocr-cache"}:
            score += 2
        else:
            score += 1
        scored.append((score, row))
    return scored


def best_evidence(
    candidates: dict[tuple[str, str], list[dict[str, str]]],
    subquestions: dict[tuple[str, str], dict[str, str]],
    suite_id: str,
    question: str,
    terms_csv: str,
) -> tuple[str, str, str]:
    scored = score_rows(candidates.get((suite_id, question), []), terms_csv)
    if scored:
        scored.sort(key=lambda item: item[0], reverse=True)
        row = scored[0][1]
        return row.get("source_type", ""), row.get("run_text_path", ""), compact(row.get("snippet", ""))
    subquestion = subquestions.get((suite_id, question))
    if subquestion:
        return (
            subquestion.get("source_type", ""),
            subquestion.get("source_path", ""),
            compact(subquestion.get("part_text") or subquestion.get("classification_text", "")),
        )
    if "(" in question:
        return best_evidence(candidates, subquestions, suite_id, question.split("(", 1)[0], terms_csv)
    return "", "", ""


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    candidates_raw = load_csv(QUESTION_CANDIDATES)
    candidates: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in candidates_raw:
        candidates[(row["suite_id"], row["question"])].append(row)
    subquestions = {
        row["suite_id"] + "\0" + row["subquestion"]: row
        for row in (load_csv(SUBQUESTION_MATRIX) if SUBQUESTION_MATRIX.exists() else [])
    }
    subquestion_map = {(key.split("\0", 1)[0], key.split("\0", 1)[1]): value for key, value in subquestions.items()}

    row_by_key = {(row["suite_id"], row["question"]): row for row in rows}
    missing = []
    for key in set(ROW_RESOLUTIONS) | set(PARENT_REMAINDERS):
        if key not in row_by_key:
            missing.append(key)
    for component in COMPONENTS:
        key = (component["suite_id"], component["parent_question"])
        if key not in row_by_key:
            missing.append(key)
    if missing:
        raise SystemExit(f"missing rows: {sorted(missing)}")

    out_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    component_audit_rows: list[dict[str, str]] = []

    for row in rows:
        key = (row["suite_id"], row["question"])
        original = dict(row)
        if key in ROW_RESOLUTIONS:
            resolution = ROW_RESOLUTIONS[key]
            if row["status"] == "reference-only":
                raise SystemExit(f"refusing reference-only rewrite: {key}")
            module = resolution["module"]
            status = "included" if module in TARGET_MODULES else "module-boundary-excluded"
            evidence_type, evidence_source, evidence_text = best_evidence(
                candidates, subquestion_map, key[0], key[1], resolution["matched_terms"]
            )
            row = dict(row)
            row.update(
                {
                    "book_module": module,
                    "status": status,
                    "artifact_location": "05_reports/source_explicit_cleanup_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": resolution["rule_id"],
                            "matched_terms": resolution["matched_terms"],
                            "source": "source_explicit_cleanup_audit.csv",
                            "prior_book_module": original["book_module"],
                            "prior_status": original["status"],
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": "future_baodian_intake" if status == "included" else "exclude_from_three_target_lines",
                    "integration_status": "source_explicit_cleanup",
                }
            )
            audit_rows.append(
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
                    "evidence_source_type": evidence_type,
                    "evidence_source": evidence_source,
                    "evidence_text": evidence_text,
                }
            )
        elif key in PARENT_REMAINDERS and row["status"] == "blocked":
            remainder = PARENT_REMAINDERS[key]
            row = dict(row)
            row.update(
                {
                    "book_module": remainder["module"],
                    "status": "module-boundary-excluded",
                    "artifact_location": "05_reports/source_explicit_target_component_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": remainder["rule_id"],
                            "source": "source_explicit_target_component_audit.csv",
                            "prior_book_module": original["book_module"],
                            "prior_status": original["status"],
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": "target_component_extracted_remainder_excluded",
                    "integration_status": "source_explicit_parent_remainder_closed",
                }
            )
            audit_rows.append(
                {
                    "suite_id": key[0],
                    "question": key[1],
                    "operation": "close_parent_remainder",
                    "prior_book_module": original["book_module"],
                    "prior_status": original["status"],
                    "new_book_module": remainder["module"],
                    "new_status": "module-boundary-excluded",
                    "rule_id": remainder["rule_id"],
                    "matched_terms": "",
                    "evidence_source_type": "",
                    "evidence_source": "",
                    "evidence_text": "",
                }
            )
        out_rows.append(row)

    existing_keys = {(row["suite_id"], row["question"]) for row in out_rows}
    for component in COMPONENTS:
        parent = row_by_key[(component["suite_id"], component["parent_question"])]
        suffix = component["module"].replace("_ECONOMICS", "").replace("_POLITICS_RULE_OF_LAW", "").replace("_CULTURE", "")
        component_question = f"{component['parent_question']}#{suffix}_COMPONENT"
        key = (component["suite_id"], component_question)
        if key in existing_keys:
            raise SystemExit(f"component already exists: {key}")
        evidence_type, evidence_source, evidence_text = best_evidence(
            candidates, subquestion_map, component["suite_id"], component["parent_question"].split("(")[0], component["matched_terms"]
        )
        new = {field: "" for field in fields}
        new.update(
            {
                "suite_id": parent["suite_id"],
                "year": parent["year"],
                "district": parent["district"],
                "stage": parent["stage"],
                "question": component_question,
                "parent_question": component["parent_question"],
                "row_granularity": "target_component",
                "book_module": component["module"],
                "question_type": parent["question_type"],
                "evidence_source": evidence_source or parent.get("evidence_source", ""),
                "source_types": parent.get("source_types", ""),
                "status": "included",
                "artifact_location": "05_reports/source_explicit_target_component_audit.csv",
                "decision_reason": json.dumps(
                    {
                        "rule_id": component["rule_id"],
                        "matched_terms": component["matched_terms"],
                        "basis": component["basis"],
                        "source": "source_explicit_target_component_audit.csv",
                        "parent_prior_book_module": parent["book_module"],
                        "parent_prior_status": parent["status"],
                    },
                    ensure_ascii=False,
                ),
                "next_action": "future_baodian_intake_target_component",
                "integration_status": "source_explicit_target_component_extraction",
            }
        )
        out_rows.append(new)
        existing_keys.add(key)
        component_audit_rows.append(
            {
                "suite_id": component["suite_id"],
                "parent_question": component["parent_question"],
                "component_question": component_question,
                "new_book_module": component["module"],
                "question_type": parent["question_type"],
                "parent_prior_status": parent["status"],
                "parent_prior_book_module": parent["book_module"],
                "rule_id": component["rule_id"],
                "matched_terms": component["matched_terms"],
                "basis": component["basis"],
                "evidence_source_type": evidence_type,
                "evidence_source": evidence_source,
                "evidence_text": evidence_text,
            }
        )

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(
        OUT_AUDIT,
        audit_rows,
        [
            "suite_id",
            "question",
            "operation",
            "prior_book_module",
            "prior_status",
            "new_book_module",
            "new_status",
            "rule_id",
            "matched_terms",
            "evidence_source_type",
            "evidence_source",
            "evidence_text",
        ],
    )
    write_csv(
        OUT_COMPONENT_AUDIT,
        component_audit_rows,
        [
            "suite_id",
            "parent_question",
            "component_question",
            "new_book_module",
            "question_type",
            "parent_prior_status",
            "parent_prior_book_module",
            "rule_id",
            "matched_terms",
            "basis",
            "evidence_source_type",
            "evidence_source",
            "evidence_text",
        ],
    )
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})
    remaining_blocked = sum(1 for row in out_rows if row["status"] == "blocked")

    report = f"""# Source Explicit Cleanup Report

Generated from `{IN_MATRIX.name}`.

## Scope

- Original blocked rows resolved or excluded: {len(audit_rows)}
- Target component rows added: {len(component_audit_rows)}
- Remaining blocked rows: {remaining_blocked}

## Matrix Counts

- Rows: {len(out_rows)}
- Status counts: {dict(status_counts)}
- Included module counts: {dict(included_counts)}
- Row granularity counts: {dict(granularity_counts)}
- Duplicate `(suite_id, question)` keys: {duplicate_keys}

## Rule Boundary

This pass only handles rows whose source prompt, answer/rubric pair, or question structure explicitly names the target module or boundary module. Known suite-id collision and answer-key-dependent objective rows remain blocked.

## Deliverables

- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_COMPONENT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
