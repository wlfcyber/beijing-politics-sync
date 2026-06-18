#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "raw_source_inspection_repaired_classification_matrix.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "strong_blocker_resolved_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "strong_blocker_resolution_audit.csv"
OUT_REVIEW = RUN_DIR / "05_reports" / "strong_blocker_resolution_review.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "strong_blocker_resolved_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "strong_blocker_resolution_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


# Only rows with clear paper/OCR source signals are resolved here. Mixed rows,
# weak keyword rows, and manual-subquestion-split rows remain blocked.
RESOLUTIONS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_东城_一模", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_GLOBAL_ENV_GOVERNANCE", "matched_terms": "COP15,全球生物多样性框架,全球生态治理,多极化"},
    ("2024_东城_二模", "13"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_URBANIZATION_PUBLIC_SERVICE", "matched_terms": "城镇化,农业劳动生产率,城乡融合,基本公共服务制度"},
    ("2024_东城_二模", "9"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_NECESSARY_CONDITION", "matched_terms": "只有,必然成立,充分必要判断"},
    ("2024_丰台_二模", "9"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONDITIONAL_JUDGMENT", "matched_terms": "判断正确,如果,除非,条件判断"},
    ("2024_海淀_一模", "12"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_ENTERPRISE_MARKET_SUBJECT", "matched_terms": "铁路企业,旅客需求,市场主体,供求矛盾"},
    ("2024_海淀_期中", "12"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_ENTERPRISE_MARKET_SUBJECT", "matched_terms": "铁路企业,旅客需求,市场主体,供求矛盾"},
    ("2024_石景山_一模", "1"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_PARTY_ARMY_LEADERSHIP", "matched_terms": "党指挥枪,党的绝对领导,人民军队,思想政治工作"},
    ("2024_石景山_一模", "2"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4PRACTICE_TECH_PRODUCTIVITY", "matched_terms": "农业生产实践,生产工具,生产力,规律"},
    ("2024_西城_一模", "12"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_AFFIRMATION_NEGATION", "matched_terms": "肯定,否定,联系"},
    ("2024_西城_一模", "3"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_PARTY_CADRES_VALUE_PURSUIT", "matched_terms": "党员干部,价值追求,奋斗姿态"},
    ("2025_东城_二模", "14"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_PREDICTION_LOGIC", "matched_terms": "如果,只有一人预测错误,推断"},
    ("2025_丰台_二模", "7"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_AGRICULTURAL_INNOVATION", "matched_terms": "经营方式,新品,增收致富,现代农业"},
    ("2025_朝阳_一模", "12"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_FOREST_ECONOMY_MARKET", "matched_terms": "林下经济,市场,经济价值,社会价值"},
    ("2025_朝阳_一模", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_FOREIGN_TRADE", "matched_terms": "贸易顺差,货物进出口,服务贸易,对外贸易"},
    ("2025_朝阳_二模", "13"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_SOCIAL_CREDIT_MARKET", "matched_terms": "社会信用体系,市场主体,市场调节,企业融资"},
    ("2025_朝阳_二模", "5"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONCEPT_RELATIONS", "matched_terms": "种属关系,全异关系,交叉关系,循环定义"},
    ("2025_朝阳_二模", "6"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONDITIONAL_REASONING", "matched_terms": "判断,如果,要么,推断"},
    ("2025_朝阳_二模", "9"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_DEMOCRACY_PUBLIC_PARTICIPATION", "matched_terms": "中国式民主,人民意愿,民声促民生,民主参与"},
    ("2025_海淀_一模", "11"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_ENTREPRENEURSHIP_BUSINESS_FORM", "matched_terms": "合伙企业,有限责任公司,营利法人,营业执照"},
    ("2025_海淀_一模", "5"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_DEFINITION_CONDITIONAL", "matched_terms": "定义,外延,除非,要么"},
    ("2025_海淀_二模", "18"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_TRADEMARK_MOCK_COURT", "matched_terms": "商标法,申请商标注册,抢先注册"},
    ("2025_海淀_二模", "6"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_CUSTODY_RIGHTS", "matched_terms": "监护权,法院裁定,未成年子女"},
    ("2025_石景山_一模", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_BELT_AND_ROAD_AID", "matched_terms": "对外合作,一带一路,援外品牌,互利共赢"},
    ("2025_西城_二模", "11"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_PUBLIC_PLACE_SAFETY", "matched_terms": "安全保障义务,法定义务,无过错责任"},
    ("2025_西城_二模", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_DATA_SOVEREIGNTY", "matched_terms": "数据主权,属地管辖权,国际规则,数据治理"},
    ("2025_西城_二模", "2"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_THEORY_PRACTICE_VIEW", "matched_terms": "认识,理论,事务主义,客观过程"},
    ("2025_西城_二模", "6"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONCEPT_RELATION", "matched_terms": "洛阳红,牡丹,逻辑关系"},
    ("2025_西城_期末", "10"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_PARTY_LEADERSHIP_DISCIPLINE", "matched_terms": "中共中央政治局,党风廉政建设,民主集中制,党的领导"},
    ("2025_西城_期末", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_EXPORT_STRUCTURE", "matched_terms": "商品出口份额,出口结构,价值链"},
    ("2025_西城_期末", "2"): {"module": "B4_CULTURE", "rule_id": "STRONG_BLOCKER_B4C_REVOLUTIONARY_CULTURE_ROUTE", "matched_terms": "红色历史遗存,李大钊旧居,伟大建党精神"},
    ("2025_西城_期末", "8"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_WATER_RIGHT_MARKET", "matched_terms": "用水权,市场化交易,资源优化配置"},
    ("2025_顺义_一模", "14"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_NATIONAL_SECURITY", "matched_terms": "国家安全,平安中国,新安全格局"},
    ("2025_顺义_一模", "2"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_COMMUNITY_GOVERNANCE", "matched_terms": "社区微花园,居民参与,社区治理,民生"},
    ("2026_东城_一模", "7"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONDITIONAL_EXPERIMENTS", "matched_terms": "除非,或者,如果,一定为真"},
    ("2026_东城_期末", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_GLOBAL_AI_GOVERNANCE", "matched_terms": "全球智能治理,国际治理框架,全球智能鸿沟"},
    ("2026_东城_期末", "4"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_LIFE_ORIGIN_SCIENCE", "matched_terms": "认识规律,自在联系,物质运动,基础科学"},
    ("2026_东城_期末", "7"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_PREDICTION_TRUTH_TABLE", "matched_terms": "如果,仅有一个符合事实,不可能为真"},
    ("2026_丰台_一模", "2"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_PEOPLE_ASSESSOR", "matched_terms": "人民陪审员,司法领域,审判民主化"},
    ("2026_丰台_二模", "6"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_LITERARY_IMAGE_THINKING", "matched_terms": "意象,主观与客观,思维能动性"},
    ("2026_丰台_二模", "9"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_TRUTH_LIAR_LOGIC", "matched_terms": "只有一人说假话,必然为真,推断"},
    ("2026_延庆_一模", "7"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_AIGC_CONCEPT_RELATION", "matched_terms": "交叉关系,反对关系,逻辑思维规则"},
    ("2026_房山_一模", "7"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONCEPT_DIVISION_CONTRADICTION_LAW", "matched_terms": "划分,概念,矛盾关系,矛盾律"},
    ("2026_朝阳_一模", "12"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_INTELLIGENT_ECONOMY_PATH", "matched_terms": "智能经济,数据要素,产业智能化,资源要素"},
    ("2026_朝阳_期末", "11"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_SYLLOGISM_PREMISE", "matched_terms": "小前提,结论,大前提"},
    ("2026_海淀_一模", "12"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_AI_PRODUCTIVITY_TOOL", "matched_terms": "人工智能工具,新生产工具,产品,资源配置"},
    ("2026_海淀_一模", "13"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_GREEN_ENERGY_STRUCTURE", "matched_terms": "能源结构,可再生能源,绿色低碳发展"},
    ("2026_海淀_二模", "14"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_FOREIGN_TRADE_VALUE_CHAIN", "matched_terms": "外贸进出口,全球贸易价值链,外贸市场"},
    ("2026_海淀_期末", "7"): {"module": "B3_POLITICS_RULE_OF_LAW", "rule_id": "STRONG_BLOCKER_B3_PARTY_STYLE_GOVERNANCE", "matched_terms": "中国共产党,延安作风,全面从严治党"},
    ("2026_石景山_一模", "3"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_AI_CONSCIOUSNESS", "matched_terms": "意识,主观能动性,直接现实性"},
    ("2026_石景山_一模", "4"): {"module": "B4_CULTURE", "rule_id": "STRONG_BLOCKER_B4C_TANG_POETRY_CITY_CULTURE", "matched_terms": "唐诗之都,文化品牌,城市文明风尚"},
    ("2026_石景山_一模", "6"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_EMBODIED_INTELLIGENCE_CONDITION", "matched_terms": "如果,除非,推断必然正确"},
    ("2026_石景山_二模", "3"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_DIALECTICS_BROAD_FINE", "matched_terms": "辩证法,中国式现代化,过犹不及,度"},
    ("2026_西城_一模", "10"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_ELEVATOR_PROPERTY_RIGHTS", "matched_terms": "业主,加装电梯,采光损失,公平合理"},
    ("2026_西城_一模", "15"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_WTO_REFORM", "matched_terms": "世贸组织,世界经济,全球经济治理"},
    ("2026_西城_一模", "6"): {"module": "B4_PHILOSOPHY_EXCLUDED", "rule_id": "STRONG_BLOCKER_B4P_TECH_SCENARIO_DIALECTICS", "matched_terms": "关键部分,新旧事物,共性个性,联系形式"},
    ("2026_西城_二模", "11"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_MARITAL_PROPERTY_COMPANY", "matched_terms": "夫妻共同财产,抵押,公司股东,破产责任"},
    ("2026_西城_二模", "15"): {"module": "XB1_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB1_G20_GLOBAL_ECONOMIC_GOVERNANCE", "matched_terms": "二十国集团,全球经济治理,国际经济合作"},
    ("2026_西城_二模", "5"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_CONDITIONAL_PREMISE", "matched_terms": "只有,必然推出,前提"},
    ("2026_西城_期末", "1"): {"module": "B4_CULTURE", "rule_id": "STRONG_BLOCKER_B4C_NATIONAL_SPIRIT_BELIEF", "matched_terms": "必胜信念,革命实践,民族复兴,精神动力"},
    ("2026_西城_期末", "12"): {"module": "B2_ECONOMICS", "rule_id": "STRONG_BLOCKER_B2_RAILWAY_PRICING_RESOURCE_ALLOCATION", "matched_terms": "票价优惠,差别定价,资源优化配置"},
    ("2026_西城_期末", "6"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_ACCESSIBLE_WORKS_COPYRIGHT", "matched_terms": "著作权,法定许可,个人信息"},
    ("2026_通州_期末", "10"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_LOGICAL_THINKING_LAW", "matched_terms": "逻辑思维,法学研究,分析正确"},
    ("2026_门头沟_一模", "10"): {"module": "XB2_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB2_FAMILY_SUPPORT_RELATION", "matched_terms": "扶养关系,子女,成年兄长,未成年妹妹"},
    ("2026_顺义_二模", "5"): {"module": "XB3_EXCLUDED", "rule_id": "STRONG_BLOCKER_XB3_DISJUNCTIVE_JUDGMENT", "matched_terms": "相容选言判断,如果,必然推出"},
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 1000) -> str:
    return re.sub(r"\s+", " ", text or "").strip()[:limit]


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    candidates = load_csv(QUESTION_CANDIDATES)
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in candidates:
        by_key[(row["suite_id"], row["question"])].append(row)

    matrix_keys = {(row["suite_id"], row["question"]) for row in rows}
    missing = sorted(set(RESOLUTIONS) - matrix_keys)
    if missing:
        raise SystemExit(f"resolution keys missing from matrix: {missing}")

    resolved_keys: set[tuple[str, str]] = set()
    audit_rows: list[dict[str, str]] = []
    review_rows: list[dict[str, str]] = []
    out_rows: list[dict[str, str]] = []

    for row in rows:
        key = (row["suite_id"], row["question"])
        resolution = RESOLUTIONS.get(key)
        if not resolution:
            out_rows.append(row)
            continue
        if row["status"] != "blocked":
            raise SystemExit(f"refusing to rewrite non-blocked row {key}: {row['status']}")
        resolved_keys.add(key)
        module = resolution["module"]
        status = "included" if module in TARGET_MODULES else "module-boundary-excluded"
        source_rows = by_key.get(key, [])
        preferred = [r for r in source_rows if r["source_type"] in {"paper", "ocr-cache"}]
        evidence_row = (preferred or source_rows or [{}])[0]
        evidence_text = compact(evidence_row.get("snippet", ""), 1200)
        new = dict(row)
        new.update(
            {
                "book_module": module,
                "status": status,
                "artifact_location": "05_reports/strong_blocker_resolution_audit.csv",
                "decision_reason": json.dumps(
                    {
                        "rule_id": resolution["rule_id"],
                        "matched_terms": resolution["matched_terms"],
                        "source": "strong_blocker_resolution_review.csv",
                        "evidence_source_type": evidence_row.get("source_type", ""),
                        "prior_status": "blocked",
                        "prior_next_action": row.get("next_action", ""),
                    },
                    ensure_ascii=False,
                ),
                "next_action": "future_baodian_intake" if status == "included" else "exclude_from_three_target_lines",
                "integration_status": "strong_blocker_resolution",
            }
        )
        out_rows.append(new)
        audit_rows.append(
            {
                "suite_id": key[0],
                "question": key[1],
                "prior_book_module": row["book_module"],
                "new_book_module": module,
                "new_status": status,
                "question_type": row["question_type"],
                "row_granularity": row["row_granularity"],
                "rule_id": resolution["rule_id"],
                "matched_terms": resolution["matched_terms"],
                "evidence_source_type": evidence_row.get("source_type", ""),
                "evidence_source": evidence_row.get("run_text_path", row.get("evidence_source", "")),
                "evidence_text": evidence_text,
            }
        )

    for row in rows:
        if row["status"] != "blocked":
            continue
        key = (row["suite_id"], row["question"])
        resolution = RESOLUTIONS.get(key)
        source_rows = by_key.get(key, [])
        preferred = [r for r in source_rows if r["source_type"] in {"paper", "ocr-cache"}]
        evidence_row = (preferred or source_rows or [{}])[0]
        review_rows.append(
            {
                "suite_id": key[0],
                "question": key[1],
                "prior_next_action": row["next_action"],
                "review_result": "resolved_by_strong_source_signal" if resolution else "kept_blocked",
                "new_book_module": resolution["module"] if resolution else "",
                "rule_id": resolution["rule_id"] if resolution else "",
                "evidence_text": compact(evidence_row.get("snippet", ""), 800),
            }
        )

    if resolved_keys != set(RESOLUTIONS):
        raise SystemExit(f"not all resolutions applied: {sorted(set(RESOLUTIONS) - resolved_keys)}")

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(OUT_AUDIT, audit_rows, [
        "suite_id", "question", "prior_book_module", "new_book_module", "new_status",
        "question_type", "row_granularity", "rule_id", "matched_terms",
        "evidence_source_type", "evidence_source", "evidence_text",
    ])
    write_csv(OUT_REVIEW, review_rows, [
        "suite_id", "question", "prior_next_action", "review_result",
        "new_book_module", "rule_id", "evidence_text",
    ])
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    resolved_counts = Counter(row["new_book_module"] for row in audit_rows)
    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})
    remaining_blocked = sum(1 for row in out_rows if row["status"] == "blocked")

    report = f"""# Strong Blocker Resolution Report

Generated from `{IN_MATRIX.name}`.

## Scope

- Input blocked rows: {sum(1 for row in rows if row["status"] == "blocked")}
- Strong-source rows resolved: {len(audit_rows)}
- Rows kept blocked: {remaining_blocked}

## Matrix Counts

- Rows: {len(out_rows)}
- Status counts: {dict(status_counts)}
- Included module counts: {dict(included_counts)}
- Resolved module counts: {dict(resolved_counts)}
- Duplicate `(suite_id, question)` keys: {duplicate_keys}

## Rule Boundary

This pass only resolves rows with direct paper/OCR source signals. It does not resolve manual-subquestion-split rows, answer-key-dependent mixed choice rows, or weak keyword rows.

## Deliverables

- `{OUT_REVIEW.relative_to(RUN_DIR)}`
- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
