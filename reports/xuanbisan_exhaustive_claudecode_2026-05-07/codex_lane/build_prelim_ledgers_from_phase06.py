# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


DESKTOP = Path(r"C:\Users\Administrator\Desktop")
RUN_DIR = DESKTOP / "飞哥的政治庄园" / "reports" / "选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07"
CODEX_DIR = RUN_DIR / "codex_lane"
SYNC_BASE = (
    DESKTOP
    / "02_代码项目与工具"
    / "mac-thread-restore"
    / "beijing-politics-sync-visible"
    / "reports"
    / "week_migration_2026-05-01_to_2026-05-06"
    / "desktop_snapshots"
    / "选必三逻辑与思维_四线从0重跑_2026-05-04"
)
COVERAGE = SYNC_BASE / "05_coverage"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def infer_hat(method: str) -> str:
    for hat in ["科学思维", "辩证思维", "创新思维", "超前思维"]:
        if hat in method:
            return hat
    if any(x in method for x in ["发散", "聚合", "逆向", "联想", "迁移", "想象"]):
        return "创新思维"
    if any(x in method for x in ["动态", "整体", "分析", "综合", "质量互变", "辩证否定"]):
        return "辩证思维"
    return ""


def evidence_from_status(status: str) -> str:
    if "L3" in status:
        return "source_confirmed_archive_needs_current_recheck"
    if "L4" in status:
        return "locked_archive_needs_current_recheck"
    return "review_only_needs_current_recheck"


def main() -> None:
    thinking = read_csv(COVERAGE / "phase06_thinking_framework_fusion.csv")
    reasoning = read_csv(COVERAGE / "phase06_reasoning_typology_fusion.csv")
    canonical = read_csv(CODEX_DIR / "CODEX_EXHAUSTIVE_CANONICAL_DECISION_MATRIX.csv")
    decision_by_qid = {r.get("question_id", ""): r for r in canonical}

    main_rows: list[dict[str, str]] = []
    choice_rows: list[dict[str, str]] = []
    reasoning_rows: list[dict[str, str]] = []
    framework: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

    for r in thinking:
        qid = r.get("question_id", "")
        d = decision_by_qid.get(qid, {})
        qtype = d.get("question_type", "")
        decision = d.get("current_exhaustive_conclusion", "")
        method = r.get("可写思维/方法", "")
        node = r.get("framework_node", "") or method
        if decision:
            framework[node][decision].add(qid)
        if decision != "入正文":
            continue
        if qtype == "主观题":
            main_rows.append({
                "question_id": qid,
                "来源": r.get("来源例题", ""),
                "完整设问": "needs_current_source_split",
                "材料动作": r.get("材料信号", ""),
                "总帽子": infer_hat(method),
                "小方法": method,
                "触发逻辑": r.get("答题动作", ""),
                "答案句": r.get("答案落点", ""),
                "证据等级": evidence_from_status(r.get("status", "")),
                "框架落点": node,
                "题型标签": r.get("易错陷阱", ""),
                "当前判定": decision,
            })
        elif qtype == "选择题":
            choice_rows.append({
                "question_id": qid,
                "题干信号": r.get("材料信号", ""),
                "完整选项或选项单位": "needs_current_full_options_recheck",
                "答案源": r.get("来源例题", ""),
                "正确项理由": r.get("答题动作", ""),
                "诱人错项": r.get("易错陷阱", ""),
                "陷阱类型": method,
                "是否可入学生稿": "prelim_yes_needs_options_audit",
                "当前判定": decision,
            })

    for r in reasoning:
        qid = r.get("question_id", "")
        d = decision_by_qid.get(qid, {})
        qtype = d.get("question_type", "")
        decision = d.get("current_exhaustive_conclusion", "")
        node = r.get("logical_form", "") or r.get("primary_reasoning_type", "")
        if decision:
            framework[node][decision].add(qid)
        if decision != "入正文":
            continue
        reasoning_rows.append({
            "question_id": qid,
            "question_type": qtype,
            "primary_reasoning_type": r.get("primary_reasoning_type", ""),
            "secondary_reasoning_type": r.get("secondary_reasoning_type", ""),
            "logical_form": r.get("logical_form", ""),
            "rule_slogan": r.get("rule_slogan", ""),
            "valid_or_invalid_pattern": r.get("valid_or_invalid_pattern", ""),
            "trap": r.get("common_trap", ""),
            "answer_action": r.get("answer_action", ""),
            "same_type_question_ids": r.get("same_type_question_ids", ""),
            "evidence_level": evidence_from_status(r.get("status", "")),
            "current_decision": decision,
        })
        if qtype == "选择题":
            choice_rows.append({
                "question_id": qid,
                "题干信号": r.get("valid_or_invalid_pattern", ""),
                "完整选项或选项单位": "needs_current_full_options_recheck",
                "答案源": "phase06_reasoning_typology_fusion",
                "正确项理由": r.get("answer_action", ""),
                "诱人错项": r.get("common_trap", ""),
                "陷阱类型": r.get("logical_form", ""),
                "是否可入学生稿": "prelim_yes_needs_options_audit",
                "当前判定": decision,
            })

    framework_rows = []
    for node, buckets in sorted(framework.items()):
        framework_rows.append({
            "framework_node": node,
            "入正文": ";".join(sorted(buckets.get("入正文", set()))),
            "同类索引": ";".join(sorted(buckets.get("同类索引", set()))),
            "blocked": ";".join(sorted(buckets.get("blocked", set()))),
            "excluded": ";".join(sorted(buckets.get("excluded", set()))),
        })

    write_csv(CODEX_DIR / "CODEX_MAIN_THINKING_LEDGER_PRELIM.csv", main_rows, [
        "question_id", "来源", "完整设问", "材料动作", "总帽子", "小方法", "触发逻辑",
        "答案句", "证据等级", "框架落点", "题型标签", "当前判定",
    ])
    write_csv(CODEX_DIR / "CODEX_CHOICE_TRAP_LEDGER_PRELIM.csv", choice_rows, [
        "question_id", "题干信号", "完整选项或选项单位", "答案源", "正确项理由",
        "诱人错项", "陷阱类型", "是否可入学生稿", "当前判定",
    ])
    write_csv(CODEX_DIR / "CODEX_REASONING_LEDGER_PRELIM.csv", reasoning_rows, [
        "question_id", "question_type", "primary_reasoning_type", "secondary_reasoning_type",
        "logical_form", "rule_slogan", "valid_or_invalid_pattern", "trap", "answer_action",
        "same_type_question_ids", "evidence_level", "current_decision",
    ])
    write_csv(CODEX_DIR / "CODEX_FRAMEWORK_NODE_MATRIX_PRELIM.csv", framework_rows, [
        "framework_node", "入正文", "同类索引", "blocked", "excluded",
    ])

    summary = {
        "main_thinking_prelim_rows": len(main_rows),
        "choice_trap_prelim_rows": len(choice_rows),
        "reasoning_prelim_rows": len(reasoning_rows),
        "framework_node_rows": len(framework_rows),
        "choice_duplicate_question_rows_possible": dict(Counter(r["question_id"] for r in choice_rows)),
    }
    (CODEX_DIR / "CODEX_PRELIM_LEDGER_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
