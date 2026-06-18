#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "culture_component_extracted_classification_matrix.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
SUBQUESTION_MATRIX = RUN_DIR / "04_module_classification" / "subquestion_split_matrix.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "remaining_strong_cleanup_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "remaining_strong_cleanup_audit.csv"
OUT_COMPONENT_AUDIT = RUN_DIR / "05_reports" / "remaining_target_component_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "remaining_strong_cleanup_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "remaining_strong_cleanup_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


ROW_RESOLUTIONS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_丰台_二模", "2"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "REMAINING_B3_PARTY_INNOVATION_THEORY_YOUTH_PREACHING",
        "matched_terms": "青年党员,党的创新理论,信仰者,传播者",
    },
    ("2024_石景山_一模", "18(2)"): {
        "module": "XB2_EXCLUDED",
        "rule_id": "REMAINING_XB2_PROPERTY_SERVICE_DISPUTE_MEDIATION",
        "matched_terms": "法官,物业服务合同,违约责任,调解协议,司法确认",
    },
    ("2024_西城_二模", "9"): {
        "module": "B4_CULTURE",
        "rule_id": "REMAINING_B4C_MAINSTREAM_MEDIA_CONTENT_INNOVATION",
        "matched_terms": "主流媒体,智慧+产品,内容创新,价值引领",
    },
    ("2025_东城_一模", "3"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "REMAINING_XB1_ONE_COUNTRY_TWO_SYSTEMS_MACAU",
        "matched_terms": "澳门,一国两制,爱国者治澳,国家发展大局",
    },
    ("2025_昌平_二模", "7"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "REMAINING_B3_GRAIN_SECURITY_LAW_GOVERNMENT",
        "matched_terms": "粮食安全保障法,政府部门,法治体系,立法机关,协同治理",
    },
    ("2025_海淀_期末", "16(1)"): {
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_COFFEE_MARKET_PROSPECT_EXPLICIT_PROMPT",
        "matched_terms": "运用《经济与社会》知识,市场前景,消费偏好,产品创新",
    },
    ("2026_东城_二模", "13"): {
        "module": "XB3_EXCLUDED",
        "rule_id": "REMAINING_XB3_JELLYFISH_CONCEPT_REASONING",
        "matched_terms": "具有所有特征,一定正确,推理",
    },
    ("2026_延庆_一模", "2"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "REMAINING_B4P_AI_LABOR_CONSCIOUSNESS_PRACTICE",
        "matched_terms": "人工智能,劳动主体,意识能动作用,劳动分工",
    },
    ("2026_海淀_期末", "12"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "REMAINING_XB1_GREEN_SILK_ROAD_GLOBAL_GOVERNANCE",
        "matched_terms": "绿色丝绸之路,全球生态治理,国际共识",
    },
    ("2026_通州_期末", "3"): {
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_ENTERPRISE_MARKET_DEMAND_PRODUCT_QUALITY",
        "matched_terms": "企业发展,市场需求,适销对路,海外市场竞争力",
    },
}


PARENT_REMAINDERS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_东城_二模", "17"): {
        "module": "XB3_EXCLUDED",
        "rule_id": "REMAINING_COMPONENT_EXTRACTED_PARENT_REMAINDER_XB3",
    },
    ("2024_顺义_二模", "17"): {
        "module": "XB2_EXCLUDED",
        "rule_id": "REMAINING_COMPONENT_EXTRACTED_PARENT_REMAINDER_XB2",
    },
    ("2025_东城_二模", "3"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "REMAINING_COMPONENT_EXTRACTED_PARENT_REMAINDER_B4P",
    },
}


COMPONENTS: list[dict[str, str]] = [
    {
        "suite_id": "2024_东城_二模",
        "parent_question": "17",
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_COMPONENT_SALINE_LAND_ECONOMY",
        "matched_terms": "运用《经济与社会》知识,土地资源优化配置,企业参与规模化经营,特色农业,旅游业",
        "basis": "第 17 题(1)明确限定《经济与社会》；第 17 题(2)为推理，作为非目标余项处理。",
    },
    {
        "suite_id": "2024_顺义_二模",
        "parent_question": "17",
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_COMPONENT_PROPERTY_SYSTEM_ECONOMIC_DEVELOPMENT",
        "matched_terms": "财产制度,经济社会发展,市场主体预期,创新创业动力,高质量发展",
        "basis": "题目虽有财产权法律基础，但细则落到市场主体预期、创新创业动力和经济高质量发展，抽入 B2 组件。",
    },
    {
        "suite_id": "2024_顺义_二模",
        "parent_question": "19(1)",
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_COMPONENT_NEW_QUALITY_PRODUCTIVE_FORCES_SYSTEM",
        "matched_terms": "社会主义基本经济制度,传统生产力,新质生产力,生产要素,市场经济体制",
        "basis": "父题原卷第 19 题(1)明确要求从社会主义基本经济制度角度说明新质生产力跃升。",
    },
    {
        "suite_id": "2025_东城_二模",
        "parent_question": "3",
        "module": "B4_CULTURE",
        "rule_id": "REMAINING_B4C_COMPONENT_ART_WITH_ERA_AND_PEOPLE",
        "matched_terms": "优秀艺术作品,时代同频,为人民发声,艺术创作",
        "basis": "客观题同时含实践认识与艺术文化判断点；文化判断点单独抽入 B4_CULTURE。",
    },
    {
        "suite_id": "2025_延庆_一模",
        "parent_question": "8",
        "module": "B4_CULTURE",
        "rule_id": "REMAINING_B4C_COMPONENT_LONG_MARCH_SPIRIT",
        "matched_terms": "长征精神,革命理想,伟大斗争",
        "basis": "长征精神/革命精神属于文化成分；哲学或中特余项不吞掉文化组件。",
    },
    {
        "suite_id": "2025_西城_二模",
        "parent_question": "3",
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_COMPONENT_GREEN_DEVELOPMENT_HIGH_QUALITY",
        "matched_terms": "高质量发展,绿色动能,全民义务植树尽责形式",
        "basis": "客观题含生态实践哲学项，但高质量发展和绿色发展动能为 B2 经济组件。",
    },
    {
        "suite_id": "2025_西城_二模",
        "parent_question": "5",
        "module": "B2_ECONOMICS",
        "rule_id": "REMAINING_B2_COMPONENT_NEW_FARMERS_RURAL_REVITALIZATION",
        "matched_terms": "新农人,农创客,家庭农场,优质农产品,研学课程,乡村全面振兴",
        "basis": "客观题含人生价值判断，但乡村振兴和返乡创业经济成分明确，抽入 B2 组件。",
    },
    {
        "suite_id": "2025_东城_期末",
        "parent_question": "19(3)",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "REMAINING_B3_COMPONENT_COMMUNITY_CONSENSUS_AUTONOMY",
        "matched_terms": "居民会议,居委会,民主协商,民主决策,达成共识",
        "basis": "第 19(3) 参考答案同时含法律相邻关系和基层群众自治；其中协商民主/基层自治部分抽入 B3。",
    },
    {
        "suite_id": "2026_东城_一模",
        "parent_question": "9",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "REMAINING_B3_COMPONENT_HEALTH_SCHOOL_GOVERNANCE",
        "matched_terms": "教育部,制度文件,学校依法履行管理职责,健康学校建设",
        "basis": "客观题含健康理念和学校治理，选项中的依法履责/制度治理部分抽入 B3。",
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


def best_evidence(
    candidates: dict[tuple[str, str], list[dict[str, str]]],
    subquestions: dict[tuple[str, str], dict[str, str]],
    suite_id: str,
    question: str,
    terms_csv: str,
) -> tuple[str, str, str]:
    terms = [term.strip("《》 ") for term in terms_csv.split(",") if term.strip()]
    rows = candidates.get((suite_id, question), [])
    scored: list[tuple[int, dict[str, str]]] = []
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
    if not scored:
        subquestion = subquestions.get((suite_id, question))
        if subquestion:
            return (
                subquestion.get("source_type", ""),
                subquestion.get("source_path", ""),
                compact(subquestion.get("part_text") or subquestion.get("classification_text", ""), 1200),
            )
        if "(" in question:
            parent_question = question.split("(", 1)[0]
            return best_evidence(candidates, subquestions, suite_id, parent_question, terms_csv)
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
    subquestions_raw = load_csv(SUBQUESTION_MATRIX) if SUBQUESTION_MATRIX.exists() else []
    subquestions = {(row["suite_id"], row["subquestion"]): row for row in subquestions_raw}

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
            row = dict(row)
            row.update(
                {
                    "book_module": module,
                    "status": status,
                    "artifact_location": "05_reports/remaining_strong_cleanup_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": resolution["rule_id"],
                            "matched_terms": resolution["matched_terms"],
                            "source": "remaining_strong_cleanup_audit.csv",
                            "prior_book_module": original["book_module"],
                            "prior_status": original["status"],
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": "future_baodian_intake" if status == "included" else "exclude_from_three_target_lines",
                    "integration_status": "remaining_strong_cleanup",
                }
            )
            evidence_type, evidence_source, evidence_text = best_evidence(
                candidates, subquestions, key[0], key[1], resolution["matched_terms"]
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
                    "artifact_location": "05_reports/remaining_target_component_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": remainder["rule_id"],
                            "source": "remaining_target_component_audit.csv",
                            "prior_book_module": original["book_module"],
                            "prior_status": original["status"],
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": "target_component_extracted_remainder_excluded",
                    "integration_status": "remaining_component_parent_remainder_closed",
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
        module = component["module"]
        suffix = module.replace("_ECONOMICS", "").replace("_POLITICS_RULE_OF_LAW", "").replace("_CULTURE", "")
        component_question = f"{component['parent_question']}#{suffix}_COMPONENT"
        key = (component["suite_id"], component_question)
        if key in existing_keys:
            raise SystemExit(f"component already exists: {key}")
        evidence_type, evidence_source, evidence_text = best_evidence(
            candidates, subquestions, component["suite_id"], component["parent_question"].split("(")[0], component["matched_terms"]
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
                "book_module": module,
                "question_type": parent["question_type"],
                "evidence_source": evidence_source or parent.get("evidence_source", ""),
                "source_types": parent.get("source_types", ""),
                "status": "included",
                "artifact_location": "05_reports/remaining_target_component_audit.csv",
                "decision_reason": json.dumps(
                    {
                        "rule_id": component["rule_id"],
                        "matched_terms": component["matched_terms"],
                        "basis": component["basis"],
                        "source": "remaining_target_component_audit.csv",
                        "parent_prior_book_module": parent["book_module"],
                        "parent_prior_status": parent["status"],
                    },
                    ensure_ascii=False,
                ),
                "next_action": "future_baodian_intake_target_component",
                "integration_status": "remaining_target_component_extraction",
            }
        )
        out_rows.append(new)
        existing_keys.add(key)
        component_audit_rows.append(
            {
                "suite_id": component["suite_id"],
                "parent_question": component["parent_question"],
                "component_question": component_question,
                "new_book_module": module,
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
    write_csv(OUT_AUDIT, audit_rows, [
        "suite_id", "question", "operation", "prior_book_module", "prior_status",
        "new_book_module", "new_status", "rule_id", "matched_terms",
        "evidence_source_type", "evidence_source", "evidence_text",
    ])
    write_csv(OUT_COMPONENT_AUDIT, component_audit_rows, [
        "suite_id", "parent_question", "component_question", "new_book_module",
        "question_type", "parent_prior_status", "parent_prior_book_module",
        "rule_id", "matched_terms", "basis", "evidence_source_type",
        "evidence_source", "evidence_text",
    ])
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})
    remaining_blocked = sum(1 for row in out_rows if row["status"] == "blocked")

    report = f"""# Remaining Strong Cleanup Report

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

This pass only handles rows whose module direction is explicit in the source prompt, options, or answer context. Multi-module rows that still require answer keys, small-question splitting, or uncertain module weights remain blocked.

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
