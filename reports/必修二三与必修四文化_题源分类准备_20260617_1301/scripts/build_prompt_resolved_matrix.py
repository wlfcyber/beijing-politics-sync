#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "subquestion_integrated_classification_matrix.csv"
CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
SUB_SPLIT = RUN_DIR / "04_module_classification" / "subquestion_split_matrix.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "prompt_resolved_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "PROMPT_RESOLVED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "prompt_resolution_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "prompt_resolved_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "prompt_resolved_matrix_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}
SOURCE_RANK = {"paper": 0, "ocr-cache": 1, "reference-answer": 2}
CHOICE_RE = re.compile(r"\s[A-D][.．、]")
PAGE_MARK_RE = re.compile(r"=====|第\s*\d+\s*页|高三")


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def build_candidate_map() -> dict[tuple[str, str], dict[str, str]]:
    best: dict[tuple[str, str], tuple[int, dict[str, str]]] = {}
    for row in load_csv(CANDIDATES):
        key = (row["suite_id"], row["question"])
        rank = SOURCE_RANK.get(row["source_type"], 9)
        old = best.get(key)
        if old is None or rank < old[0]:
            best[key] = (rank, row)
    return {key: value for key, (_, value) in best.items()}


def build_subquestion_prompt_map() -> dict[tuple[str, str], str]:
    result: dict[tuple[str, str], str] = {}
    if not SUB_SPLIT.exists():
        return result
    for row in load_csv(SUB_SPLIT):
        result[(row["suite_id"], row["subquestion"])] = row.get("classification_text") or row.get("part_text", "")
    return result


def prompt_for(row: dict[str, str], candidates: dict[tuple[str, str], dict[str, str]], sub_prompts: dict[tuple[str, str], str]) -> tuple[str, str]:
    sub_prompt = sub_prompts.get((row["suite_id"], row["question"]))
    if sub_prompt:
        return compact(sub_prompt, 1200), "subquestion_split_matrix"
    parent = row.get("parent_question") or row["question"]
    cand = candidates.get((row["suite_id"], parent), {})
    snippet = cand.get("snippet", "")
    if row.get("row_granularity") == "subquestion" and row.get("question") in snippet:
        idx = snippet.find(row["question"])
        snippet = snippet[idx:]
    match = CHOICE_RE.search(snippet)
    page_match = PAGE_MARK_RE.search(snippet)
    cut = len(snippet)
    if match and row.get("question_type") == "objective":
        cut = min(cut, match.start() + 260)
    if page_match and page_match.start() > 80:
        cut = min(cut, page_match.start())
    return compact(snippet[:cut], 1200), cand.get("source_type", "")


def contains_any(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if term in text]


RULES = [
    (
        "XB3_LOGIC_PROMPT",
        "XB3_EXCLUDED",
        "module-boundary-excluded",
        "exclude_from_three_target_lines",
        [
            "逻辑与思维",
            "科学思维",
            "三段论",
            "推理",
            "必然成立",
            "当且仅当",
            "充分条件",
            "必要条件",
            "假言判断",
            "判断类型",
            "保真条件",
            "逻辑错误",
            "求异法",
            "求同法",
            "共变法",
            "剩余法",
            "选科情况",
        ],
    ),
    (
        "XB1_INTERNATIONAL_PROMPT",
        "XB1_EXCLUDED",
        "module-boundary-excluded",
        "exclude_from_three_target_lines",
        [
            "当代国际政治与经济",
            "全球治理",
            "国际组织",
            "国际社会",
            "国际贸易",
            "国际投资",
            "进出口贸易",
            "主权国家",
            "他国主权",
            "美国总统大选",
            "多党制国家",
            "关税",
            "对外贸易",
            "贸易自由化",
            "金砖",
            "上海合作组织",
            "国家利益",
        ],
    ),
    (
        "XB2_LAW_PROMPT",
        "XB2_EXCLUDED",
        "module-boundary-excluded",
        "exclude_from_three_target_lines",
        [
            "法律与生活",
            "民法典",
            "民事法律关系",
            "侵权",
            "诉讼",
            "仲裁",
            "调解协议",
            "所有权",
            "共有部分",
            "业主共同决定",
        ],
    ),
    (
        "B1_SOCIALISM_PROMPT",
        "B1_EXCLUDED",
        "module-boundary-excluded",
        "exclude_from_three_target_lines",
        [
            "中国特色社会主义",
            "科学社会主义",
            "中国梦",
            "改革开放",
            "中华人民共和国成立",
        ],
    ),
    (
        "B4_PHILOSOPHY_PROMPT",
        "B4_PHILOSOPHY_EXCLUDED",
        "module-boundary-excluded",
        "exclude_from_three_target_lines",
        [
            "从哲学角度",
            "哲学角度",
            "哲学观点",
            "哲学却识",
            "哲理",
            "矛盾普遍性",
            "矛盾特殊性",
            "矛盾的特殊性",
            "对立统一",
            "辩证否定",
            "联系的观点",
            "整体与部分",
            "系统优化",
            "价值判断",
            "价值选择",
            "社会存在",
            "社会意识",
            "人类中心主义",
            "一切从实际出发",
        ],
    ),
    (
        "B2_EXPLICIT_ECONOMICS_PROMPT",
        "B2_ECONOMICS",
        "included",
        "future_baodian_intake",
        [
            "《经济与社会》",
            "经济与社会",
            "经济信息",
            "从经济角度",
            "经济高质量发展",
            "新质生产力",
            "基本经济制度",
            "社会保障",
            "医保",
            "养老",
            "财政补贴",
            "税收优惠",
            "市场监管",
            "市场秩序",
            "消费",
            "产业发展",
            "物流",
            "营商环境",
            "瞪羚企业",
        ],
    ),
    (
        "B3_EXPLICIT_POLITICS_PROMPT",
        "B3_POLITICS_RULE_OF_LAW",
        "included",
        "future_baodian_intake",
        [
            "《政治与法治》",
            "政治与法治",
            "政协",
            "人民政协",
            "人大代表",
            "人民代表大会",
            "基层群众自治",
            "居委会",
            "社区治理",
            "基层治理",
            "法治政府",
            "严格执法",
            "公正司法",
            "政府部门、居委会",
            "城市治理",
            "接诉即办",
        ],
    ),
    (
        "B4_CULTURE_PROMPT",
        "B4_CULTURE",
        "included",
        "future_baodian_intake",
        [
            "文化自信",
            "中华优秀传统文化",
            "优秀传统文化",
            "文化遗产",
            "文物",
            "博物馆",
            "公共文化服务",
            "文化服务",
            "文化内涵",
            "民族精神",
            "探月精神",
            "社会主义核心价值观",
            "大思政课",
            "启智润心",
            "精神文明",
        ],
    ),
]


def resolve_prompt(prompt: str) -> dict[str, str] | None:
    # Explicit mixed-book prompts remain blocked.
    if "《政治与法治》" in prompt and "《当代国际政治与经济》" in prompt:
        return None
    if "《经济与社会》" in prompt and ("《逻辑与思维》" in prompt or "《当代国际政治与经济》" in prompt):
        return None
    if "运用《法律与生活》和《政治与法治》" in prompt:
        return None

    for rule_id, module, status, next_action, terms in RULES:
        hits = contains_any(prompt, terms)
        if hits:
            if rule_id == "B4_PHILOSOPHY_PROMPT" and "实践教学基地" in prompt:
                continue
            return {
                "rule_id": rule_id,
                "book_module": module,
                "status": status,
                "next_action": next_action,
                "matched_terms": ",".join(hits[:8]),
            }
    return None


def prior_requires_subquestion_split(row: dict[str, str]) -> bool:
    if row.get("row_granularity") == "subquestion":
        return False
    try:
        reason = json.loads(row.get("decision_reason", ""))
    except json.JSONDecodeError:
        return False
    return reason.get("override") == "manual_subquestion_split_needed"


def main() -> int:
    rows = load_csv(IN_MATRIX)
    candidates = build_candidate_map()
    sub_prompts = build_subquestion_prompt_map()

    out_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    for row in rows:
        new = dict(row)
        if row["status"] == "blocked":
            if prior_requires_subquestion_split(row):
                out_rows.append(new)
                continue
            prompt, prompt_source = prompt_for(row, candidates, sub_prompts)
            resolved = resolve_prompt(prompt)
            if resolved:
                old_reason = row.get("decision_reason", "")
                new["book_module"] = resolved["book_module"]
                new["status"] = resolved["status"]
                new["next_action"] = resolved["next_action"]
                new["artifact_location"] = "05_reports/prompt_resolution_audit.csv"
                new["decision_reason"] = json.dumps(
                    {
                        "override": "strict_prompt_resolution",
                        "rule_id": resolved["rule_id"],
                        "matched_terms": resolved["matched_terms"],
                        "prompt_source": prompt_source,
                        "prompt": prompt[:400],
                        "previous_decision": old_reason,
                    },
                    ensure_ascii=False,
                )
                new["integration_status"] = f"prompt_resolved_from_{row['integration_status']}"
                audit_rows.append(
                    {
                        "suite_id": row["suite_id"],
                        "question": row["question"],
                        "parent_question": row.get("parent_question", ""),
                        "old_book_module": row["book_module"],
                        "new_book_module": new["book_module"],
                        "old_status": row["status"],
                        "new_status": new["status"],
                        "rule_id": resolved["rule_id"],
                        "matched_terms": resolved["matched_terms"],
                        "prompt_source": prompt_source,
                        "prompt": prompt,
                    }
                )
        out_rows.append(new)

    blocked_rows = [row for row in out_rows if row["status"] == "blocked"]
    write_csv(OUT_MATRIX, out_rows, rows[0].keys())
    write_csv(OUT_COVERAGE, out_rows, rows[0].keys())
    write_csv(
        OUT_AUDIT,
        audit_rows,
        [
            "suite_id",
            "question",
            "parent_question",
            "old_book_module",
            "new_book_module",
            "old_status",
            "new_status",
            "rule_id",
            "matched_terms",
            "prompt_source",
            "prompt",
        ],
    )
    write_csv(OUT_BLOCKED, blocked_rows, rows[0].keys())

    status_counts = Counter(row["status"] for row in out_rows)
    module_counts = Counter(row["book_module"] for row in out_rows)
    target_counts = Counter(
        row["book_module"]
        for row in out_rows
        if row["status"] == "included" and row["book_module"] in TARGET_MODULES
    )
    rule_counts = Counter(row["rule_id"] for row in audit_rows)

    lines = [
        "# Prompt-Resolved Matrix Report",
        "",
        "- purpose: Conservative prompt-level resolution of remaining blocked rows after subquestion integration.",
        f"- input_rows: {len(rows)}",
        f"- prompt_resolved_rows: {len(audit_rows)}",
        f"- output_rows: {len(out_rows)}",
        f"- blocked_rows_after_prompt_resolution: {len(blocked_rows)}",
        f"- output_matrix: `{OUT_MATRIX}`",
        f"- output_coverage: `{OUT_COVERAGE}`",
        f"- audit_file: `{OUT_AUDIT}`",
        f"- blocked_queue: `{OUT_BLOCKED}`",
        "",
        "## Rule Counts",
        "",
    ]
    for key, value in rule_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Status Counts", ""])
    for key, value in status_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Target Included Counts", ""])
    for key, value in target_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Module Counts", ""])
    for key, value in module_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- This pass only resolves rows with strong prompt evidence. Weak single-keyword rows remain blocked.",
            "- Final closure still requires reviewing the remaining blocked queue and the question-gap review.",
        ]
    )
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(OUT_MATRIX)
    print(OUT_COVERAGE)
    print(OUT_AUDIT)
    print(OUT_BLOCKED)
    print(OUT_REPORT)
    print(f"resolved={len(audit_rows)} blocked={len(blocked_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
