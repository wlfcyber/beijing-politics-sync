# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


DESKTOP = Path(r"C:\Users\Administrator\Desktop")
RUN_DIR = DESKTOP / "飞哥的政治庄园" / "reports" / "选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07"
CODEX_DIR = RUN_DIR / "codex_lane"
CORPUS = DESKTOP / "beijing_politics_research" / "data" / "preprocessed_corpus"
SYNC = DESKTOP / "02_代码项目与工具" / "mac-thread-restore" / "beijing-politics-sync-visible"
CONTROL_BASE = SYNC / "reports" / "week_migration_2026-05-01_to_2026-05-06" / "desktop_snapshots" / "选必三逻辑与思维_四线从0重跑_2026-05-04"

SOURCE_ROOTS = [
    DESKTOP / "2024各区模拟题",
    DESKTOP / "2025各区模拟题",
    DESKTOP / "2026各区模拟题",
]

TERMS = [
    "逻辑与思维", "科学思维", "辩证思维", "创新思维", "超前思维",
    "分析与综合", "发散", "聚合", "逆向", "联想", "迁移", "想象",
    "思维抽象", "思维具体", "感性具体", "系统观念", "形式逻辑", "推理",
    "三段论", "假言推理", "必要条件", "充分条件", "选言", "联言",
]

DISTRICTS = ["海淀", "西城", "东城", "朝阳", "丰台", "顺义", "通州", "石景山", "门头沟", "房山", "昌平", "延庆", "平谷", "密云", "怀柔", "大兴"]
STAGES = ["期中", "期末", "一模", "二模", "三模", "零模", "统测", "练习"]


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def infer_year(text: str) -> str:
    m = re.search(r"20(24|25|26)", text)
    if m:
        return "20" + m.group(1)
    return ""


def first_hit(text: str, choices: list[str]) -> str:
    for c in choices:
        if c in text:
            return c
    return ""


def source_kind(path: Path) -> str:
    s = str(path)
    if "试卷" in s or "原卷" in s or "教师版" in s:
        return "paper_or_teacher"
    if "细则" in s or "评标" in s or "阅卷" in s or "评分" in s:
        return "rubric_or_marking"
    if "答案" in s or "参考" in s:
        return "answer"
    if "讲评" in s or "总结" in s:
        return "explain_or_review"
    if "分类" in s or "汇编" in s:
        return "classification_compilation"
    return "other"


def build_file_inventory() -> list[dict]:
    rows = []
    for root in SOURCE_ROOTS:
        if not root.exists():
            rows.append({
                "source_root": str(root),
                "source_path": "",
                "exists": "no",
                "suffix": "",
                "year": "",
                "district": "",
                "stage": "",
                "kind": "",
                "size": "",
                "mtime": "",
            })
            continue
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if p.name.startswith("~$"):
                continue
            text = str(p)
            rows.append({
                "source_root": str(root),
                "source_path": str(p),
                "exists": "yes",
                "suffix": p.suffix.lower(),
                "year": infer_year(text),
                "district": first_hit(text, DISTRICTS),
                "stage": first_hit(text, STAGES),
                "kind": source_kind(p),
                "size": p.stat().st_size,
                "mtime": p.stat().st_mtime,
            })
    return rows


def build_suite_candidates(file_rows: list[dict]) -> list[dict]:
    suites: dict[tuple[str, str, str], dict] = {}
    for r in file_rows:
        if r.get("exists") != "yes":
            continue
        key = (r.get("year", ""), r.get("district", ""), r.get("stage", ""))
        if not all(key):
            continue
        row = suites.setdefault(key, {
            "year": key[0],
            "district": key[1],
            "stage": key[2],
            "suite": "".join(key),
            "file_count": 0,
            "paper_count": 0,
            "answer_count": 0,
            "rubric_count": 0,
            "explain_count": 0,
            "classification_count": 0,
            "all_files": [],
        })
        row["file_count"] += 1
        row["all_files"].append(r["source_path"])
        kind = r["kind"]
        if kind == "paper_or_teacher":
            row["paper_count"] += 1
        elif kind == "answer":
            row["answer_count"] += 1
        elif kind == "rubric_or_marking":
            row["rubric_count"] += 1
        elif kind == "explain_or_review":
            row["explain_count"] += 1
        elif kind == "classification_compilation":
            row["classification_count"] += 1
    out = []
    for row in suites.values():
        row["has_paper"] = "yes" if row["paper_count"] else "no"
        row["has_scoring_source"] = "yes" if row["rubric_count"] or row["explain_count"] else "no"
        row["has_answer_like"] = "yes" if row["answer_count"] or row["paper_count"] else "no"
        row["all_files"] = " | ".join(row["all_files"])
        out.append(row)
    out.sort(key=lambda x: (x["year"], DISTRICTS.index(x["district"]) if x["district"] in DISTRICTS else 99, x["stage"]))
    return out


def build_term_hits(manifest_rows: list[dict]) -> list[dict]:
    rows = []
    for m in manifest_rows:
        text_path = m.get("text_path") or ""
        p = Path(text_path)
        if not p.exists():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            rows.append({
                "source_path": m.get("source_path", ""),
                "relative_path": m.get("relative_path", ""),
                "suite_key": m.get("suite_key", ""),
                "text_path": text_path,
                "year": infer_year(m.get("source_path", "") + " " + m.get("relative_path", "")),
                "district": first_hit(m.get("source_path", "") + " " + m.get("relative_path", ""), DISTRICTS),
                "stage": first_hit(m.get("source_path", "") + " " + m.get("relative_path", ""), STAGES),
                "kind": source_kind(Path(m.get("source_path", ""))),
                "term": "",
                "hit_count": "",
                "snippet": "",
                "error": repr(exc),
            })
            continue
        for term in TERMS:
            count = text.count(term)
            if not count:
                continue
            idx = text.find(term)
            snippet = re.sub(r"\s+", " ", text[max(0, idx - 80): idx + 160]).strip()
            rows.append({
                "source_path": m.get("source_path", ""),
                "relative_path": m.get("relative_path", ""),
                "suite_key": m.get("suite_key", ""),
                "text_path": text_path,
                "year": infer_year(m.get("source_path", "") + " " + m.get("relative_path", "")),
                "district": first_hit(m.get("source_path", "") + " " + m.get("relative_path", ""), DISTRICTS),
                "stage": first_hit(m.get("source_path", "") + " " + m.get("relative_path", ""), STAGES),
                "kind": source_kind(Path(m.get("source_path", ""))),
                "term": term,
                "hit_count": count,
                "snippet": snippet,
                "error": "",
            })
    rows.sort(key=lambda x: (
        x.get("year", ""),
        x.get("district", ""),
        x.get("stage", ""),
        x.get("term", ""),
        -int(x.get("hit_count") or 0),
    ))
    return rows


def audit_control_base() -> tuple[list[dict], dict]:
    path = CONTROL_BASE / "05_coverage" / "phase03_question_coverage_matrix.csv"
    rows = read_csv(path)
    out = []
    counters = {
        "total": len(rows),
        "by_suite": Counter(),
        "by_part": Counter(),
        "by_final": Counter(),
        "by_block": Counter(),
    }
    for r in rows:
        part = r.get("部分归属", "")
        final = r.get("final_classification", "")
        suite = r.get("suite_id", "")
        block = r.get("blocked_status", "")
        counters["by_suite"][suite] += 1
        counters["by_part"][part] += 1
        counters["by_final"][final] += 1
        counters["by_block"][block] += 1
        hint = r.get("知识节点", "") + ";" + r.get("题型节点", "")
        if part == "思维":
            preliminary = "needs_evidence_pairing_then_body_or_choice"
        elif part == "推理":
            preliminary = "same_type_index_or_boundary"
        elif part == "交叉":
            preliminary = "split_thinking_part_from_reasoning_part"
        elif part == "边界":
            preliminary = "excluded_or_boundary_index"
        elif part == "missing":
            preliminary = "blocked"
        else:
            preliminary = "needs_module_judgment"
        out.append({
            "question_id": r.get("question_id", ""),
            "suite_id": suite,
            "stable_locator": r.get("stable_locator", ""),
            "原始题号": r.get("原始题号", ""),
            "题型": r.get("题型", ""),
            "部分归属": part,
            "知识节点": r.get("知识节点", ""),
            "题型节点": r.get("题型节点", ""),
            "是否有答案": r.get("是否有答案", ""),
            "是否有评分细则": r.get("是否有评分细则", ""),
            "是否有讲评": r.get("是否有讲评", ""),
            "blocked_status": block,
            "source_final_classification": final,
            "codex_preliminary_action": preliminary,
            "codex_reason": "control_base_audit_only",
            "excerpt": r.get("excerpt", "")[:600],
        })
    summary = {
        "path": str(path),
        "total": counters["total"],
        "by_suite": counters["by_suite"],
        "by_part": counters["by_part"],
        "by_final": counters["by_final"],
        "by_block": counters["by_block"],
    }
    return out, summary


def audit_signal_matrix() -> tuple[list[dict], dict]:
    path = CONTROL_BASE / "05_coverage" / "phase03_thinking_signal_chain_matrix.csv"
    rows = read_csv(path)
    out = []
    c = Counter()
    for r in rows:
        status = r.get("是否可入学生稿", "")
        c[status] += 1
        out.append({
            "question_id": r.get("question_id", ""),
            "suite_id": r.get("suite_id", ""),
            "stable_locator": r.get("stable_locator", ""),
            "思维知识节点": r.get("思维知识节点", ""),
            "设问类型": r.get("设问类型", ""),
            "来源例题": r.get("来源例题", ""),
            "是否可入学生稿": status,
            "codex_needed_action": "pair_source_and_extract" if "pending" in status else "review",
        })
    return out, {"path": str(path), "total": len(rows), "by_status": c}


def scan_erm(file_rows: list[dict], term_hits: list[dict]) -> dict:
    file_hits = [r for r in file_rows if "二模" in r.get("source_path", "")]
    source_2026_hits = [r for r in file_hits if r.get("year") == "2026" or "2026" in r.get("source_path", "")]
    text_2026_hits = [r for r in term_hits if r.get("year") == "2026" and "二模" in (r.get("source_path", "") + r.get("relative_path", ""))]
    return {
        "source_root_2026_erm_files": len(source_2026_hits),
        "source_root_2026_erm_paths": [r["source_path"] for r in source_2026_hits],
        "cache_2026_erm_term_hits": len(text_2026_hits),
    }


def write_progress(summary: dict) -> None:
    lines = [
        "# CODEX A 线源索引进度",
        "",
        "## 2026-05-07",
        "",
        "- 已生成本机 2024-2026 文件级题源清单。",
        "- 已生成套卷候选清单。",
        "- 已扫描预处理缓存中的选必三相关术语命中。",
        "- 已审计 528-row control base 和 73-row thinking signal matrix。",
        "",
        "## 关键计数",
        "",
        f"- source_inventory_rows: {summary['source_inventory_rows']}",
        f"- suite_candidate_rows: {summary['suite_candidate_rows']}",
        f"- corpus_manifest_rows: {summary['manifest_rows']}",
        f"- term_hit_rows: {summary['term_hit_rows']}",
        f"- control_base_rows: {summary['control_summary']['total']}",
        f"- signal_matrix_rows: {summary['signal_summary']['total']}",
        f"- source_root_2026_erm_files: {summary['erm_scan']['source_root_2026_erm_files']}",
        "",
        "## control base 分布",
        "",
        "```json",
        json.dumps({
            "by_suite": dict(summary["control_summary"]["by_suite"]),
            "by_part": dict(summary["control_summary"]["by_part"]),
            "by_final": dict(summary["control_summary"]["by_final"]),
            "by_block": dict(summary["control_summary"]["by_block"]),
        }, ensure_ascii=False, indent=2),
        "```",
        "",
        "## 下一步",
        "",
        "- 将 control base 的 528 行转为正式 `入正文 / 同类索引 / blocked / excluded` 裁决矩阵。",
        "- 对 term hit index 中 2026 一模/期末/期中与 2024-2025 二模额外源进行回源抽样。",
        "- 等 ClaudeCode B 线产出 suite_reports 和 entries 后做交叉验证。",
    ]
    (CODEX_DIR / "CODEX_A_LANE_PROGRESS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    CODEX_DIR.mkdir(parents=True, exist_ok=True)
    file_rows = build_file_inventory()
    write_csv(CODEX_DIR / "CODEX_SOURCE_ROOT_INVENTORY.csv", file_rows, [
        "source_root", "source_path", "exists", "suffix", "year", "district", "stage", "kind", "size", "mtime",
    ])

    suite_rows = build_suite_candidates(file_rows)
    write_csv(CODEX_DIR / "CODEX_SUITE_CANDIDATES.csv", suite_rows, [
        "year", "district", "stage", "suite", "file_count", "paper_count", "answer_count", "rubric_count",
        "explain_count", "classification_count", "has_paper", "has_answer_like", "has_scoring_source", "all_files",
    ])

    manifest_rows = read_csv(CORPUS / "manifest.csv")
    term_hits = build_term_hits(manifest_rows)
    write_csv(CODEX_DIR / "CODEX_TERM_HIT_INDEX.csv", term_hits, [
        "source_path", "relative_path", "suite_key", "text_path", "year", "district", "stage", "kind",
        "term", "hit_count", "snippet", "error",
    ])

    control_rows, control_summary = audit_control_base()
    write_csv(CODEX_DIR / "CODEX_CONTROL_BASE_AUDIT.csv", control_rows, [
        "question_id", "suite_id", "stable_locator", "原始题号", "题型", "部分归属", "知识节点", "题型节点",
        "是否有答案", "是否有评分细则", "是否有讲评", "blocked_status", "source_final_classification",
        "codex_preliminary_action", "codex_reason", "excerpt",
    ])

    signal_rows, signal_summary = audit_signal_matrix()
    write_csv(CODEX_DIR / "CODEX_SIGNAL_MATRIX_AUDIT.csv", signal_rows, [
        "question_id", "suite_id", "stable_locator", "思维知识节点", "设问类型", "来源例题", "是否可入学生稿", "codex_needed_action",
    ])

    erm_scan = scan_erm(file_rows, term_hits)
    (CODEX_DIR / "CODEX_2026_ERM_SCAN.json").write_text(json.dumps(erm_scan, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "source_inventory_rows": len(file_rows),
        "suite_candidate_rows": len(suite_rows),
        "manifest_rows": len(manifest_rows),
        "term_hit_rows": len(term_hits),
        "control_summary": control_summary,
        "signal_summary": signal_summary,
        "erm_scan": erm_scan,
    }
    (CODEX_DIR / "CODEX_SOURCE_INVENTORY_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, default=lambda x: dict(x)), encoding="utf-8"
    )
    write_progress(summary)
    print(json.dumps({
        "source_inventory_rows": len(file_rows),
        "suite_candidate_rows": len(suite_rows),
        "manifest_rows": len(manifest_rows),
        "term_hit_rows": len(term_hits),
        "control_base_rows": len(control_rows),
        "signal_rows": len(signal_rows),
        "source_root_2026_erm_files": erm_scan["source_root_2026_erm_files"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
