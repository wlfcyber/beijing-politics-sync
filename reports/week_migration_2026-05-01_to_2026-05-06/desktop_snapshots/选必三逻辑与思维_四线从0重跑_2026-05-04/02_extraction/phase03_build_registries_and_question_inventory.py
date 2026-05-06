#!/usr/bin/env python3
"""Build Phase 03 source/suite registries and first question inventory.

The outputs are official Phase 03 scan artifacts, but all classifications remain
provisional until source pairing, visual fallback, and A/B diff close.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


RUN_DIR = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
MANIFEST = RUN_DIR / "02_extraction/priority_queue_sources/priority_queue_extraction_manifest.csv"
SOURCE_LEDGER = RUN_DIR / "SOURCE_LEDGER.csv"
CANDIDATE_MATRIX = RUN_DIR / "05_coverage/question_coverage_matrix_phase03_candidates.csv"
REASONING_CANDIDATES = RUN_DIR / "05_coverage/reasoning_typology_candidates_phase03.csv"
VISUAL_SEEDS = RUN_DIR / "02_extraction/phase03_visual_recovery_seeds.csv"

OUT_SOURCE_CSV = RUN_DIR / "01_source_inventory/phase03_raw_source_registry.csv"
OUT_SOURCE_MD = RUN_DIR / "01_source_inventory/phase03_raw_source_registry.md"
OUT_LOCATOR_MD = RUN_DIR / "01_source_inventory/phase03_locator_only_removed_or_isolated.md"
OUT_METHODS_MD = RUN_DIR / "01_source_inventory/phase03_source_reading_methods.md"
OUT_FAILURES_MD = RUN_DIR / "01_source_inventory/phase03_source_failures_and_fallbacks.md"

OUT_SUITE_CSV = RUN_DIR / "04_suite_reports/phase03_suite_registry.csv"
OUT_SUITE_MD = RUN_DIR / "04_suite_reports/phase03_suite_registry.md"
OUT_DUP_CSV = RUN_DIR / "04_suite_reports/phase03_suite_duplicate_map.csv"
OUT_MISSING_MD = RUN_DIR / "05_coverage/phase03_missing_expected_sources.md"
OUT_2026_2_MD = RUN_DIR / "05_coverage/phase03_2026_二模_missing_or_blocked.md"

OUT_Q_CSV = RUN_DIR / "05_coverage/phase03_question_coverage_matrix.csv"
OUT_Q_MD = RUN_DIR / "05_coverage/phase03_question_coverage_matrix.md"
OUT_THINK_CSV = RUN_DIR / "05_coverage/phase03_thinking_signal_chain_matrix.csv"
OUT_THINK_MD = RUN_DIR / "05_coverage/phase03_thinking_signal_chain_matrix.md"
OUT_REASON_CSV = RUN_DIR / "05_coverage/phase03_reasoning_question_attachment_matrix.csv"
OUT_REASON_TREE = RUN_DIR / "05_coverage/phase03_reasoning_typology_tree.md"
OUT_BLOCKED_CSV = RUN_DIR / "05_coverage/phase03_blocked_questions.csv"
OUT_VISUAL_BLOCKERS = RUN_DIR / "05_coverage/phase03_visual_fallback_blockers.md"
OUT_REPORT = RUN_DIR / "04_suite_reports/codex_suite_reports/phase03_registry_and_question_inventory_report.md"


THINKING_TERMS = [
    "科学思维", "辩证思维", "创新思维", "超前思维", "联想思维", "发散思维", "聚合思维", "逆向思维",
    "分析与综合", "质量互变", "辩证否定", "整体性", "动态性", "思维抽象", "思维具体", "感性具体",
    "迁移", "想象", "系统思维", "系统观念", "客观性", "预见性", "可检验性",
]
REASONING_TERMS = [
    "形式逻辑", "三段论", "假言", "选言", "联言", "充分条件", "必要条件", "充分必要条件",
    "周延", "换质", "换位", "矛盾律", "排中律", "同一律", "概念", "判断", "推理", "归纳", "类比",
    "演绎推理", "保真", "前提", "结论", "中项", "大项", "小项",
]
BOUNDARY_BOOKS = ["哲学与文化", "当代国际政治与经济", "法律与生活", "政治与法治", "经济与社会"]

TYPOLOGY_RULES = [
    ("三段论", ["三段论", "中项", "大项", "小项"]),
    ("假言推理", ["假言", "充分条件", "必要条件", "充分必要条件", "肯定前件", "否定后件", "肯前", "肯后", "否前", "否后"]),
    ("选言推理", ["选言", "相容选言", "不相容选言"]),
    ("联言推理", ["联言"]),
    ("归纳推理与因果探求", ["归纳", "求同法", "求异法", "共变法", "剩余法", "因果"]),
    ("类比推理", ["类比"]),
    ("周延判断", ["周延", "主项", "谓项"]),
    ("换质换位", ["换质", "换位"]),
    ("逻辑三律与概念规则", ["矛盾律", "排中律", "同一律", "定义", "划分"]),
]


def norm(text: str) -> str:
    return unicodedata.normalize("NFKC", text).replace("\u3000", " ")


def suite_key(path_text: str) -> str:
    candidates = re.findall(r"20\d{2}[\u4e00-\u9fa5]{2,4}(?:一模|二模|期中|期末)", path_text)
    if candidates:
        return re.sub(r"^(20\d{2})年", r"\1", candidates[-1])
    if "西城一模" in path_text:
        return "2024西城一模"
    if "海淀二模" in path_text:
        return "2024海淀二模"
    return "UNKNOWN_SUITE"


def suite_id(suite: str) -> str:
    return "S-" + suite


def source_role(path_text: str, source_id: str) -> str:
    joined = f"{path_text} {source_id}"
    if "评标" in joined or "讲评" in joined or "其他材料" in joined:
        return "support_or_lecture"
    if "试卷" in joined or "教师版" in joined or "原卷" in joined:
        return "paper"
    if "细则" in joined or "答案" in joined or "评分" in joined:
        return "rubric_or_answer"
    return "unknown"


def visual_risk(suffix: str, method: str, char_count: str, role: str) -> str:
    try:
        chars = int(char_count or 0)
    except ValueError:
        chars = 0
    risks = []
    if suffix.lower() in {".pptx", ".pdf"}:
        risks.append("visual_source")
    if suffix.lower() == ".pdf" and chars < 1000:
        risks.append("thin_text_pdf")
    if role == "support_or_lecture":
        risks.append("support_boundary")
    if "render" in method:
        risks.append("render_available")
    return ";".join(risks) if risks else "low"


def hit_terms(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if term in text]


def typology_for(text: str) -> str:
    hits = []
    for label, keys in TYPOLOGY_RULES:
        if any(key in text for key in keys):
            hits.append(label)
    return ";".join(hits) if hits else "其他复合推理"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def question_starts(lines: list[str]) -> list[tuple[int, str]]:
    starts = []
    for idx, line in enumerate(lines):
        s = line.strip()
        if re.match(r"^\d{1,2}\s*[.、．􀆰]\s*", s):
            q = re.match(r"^(\d{1,2})", s).group(1)
            if int(q) == 0:
                continue
            starts.append((idx, q))
    dedup = []
    last_q = None
    for idx, q in starts:
        if q == last_q and dedup and idx - dedup[-1][0] < 5:
            continue
        dedup.append((idx, q))
        last_q = q
    return dedup


def split_questions(text: str) -> list[dict[str, str]]:
    lines = norm(text).splitlines()
    starts = question_starts(lines)
    blocks = []
    for pos, (start, qno) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        block = "\n".join(lines[start:end]).strip()
        if len(block) < 15:
            continue
        opt_count = len(re.findall(r"(?:^|\n)\s*[ABCD][.、．]\s*", block))
        subqs = re.findall(r"[（(]([1-9])[\)）]", block)
        subqs = sorted(set(subqs), key=lambda x: int(x))
        if int(qno) >= 16 and subqs:
            for sub in subqs:
                blocks.append({"qno": qno, "subq": sub, "block": block, "option_count": str(opt_count)})
        else:
            blocks.append({"qno": qno, "subq": "", "block": block, "option_count": str(opt_count)})
    return blocks


def stem_excerpt(block: str) -> str:
    block = re.sub(r"\s+", " ", block)
    return block[:380]


def section_guess(block: str) -> str:
    t_hits = hit_terms(block, THINKING_TERMS)
    r_hits = hit_terms(block, REASONING_TERMS)
    if t_hits and r_hits:
        return "交叉"
    if t_hits:
        return "思维"
    if r_hits:
        return "推理"
    if any(book in block for book in BOUNDARY_BOOKS):
        return "边界"
    return "待判"


def answer_status_for(qno: str, suite: str, nonpaper_sources: list[dict[str, str]]) -> tuple[str, str]:
    ids = []
    for src in nonpaper_sources:
        txt_path = Path(src["text_path"])
        if not txt_path.exists():
            continue
        txt = norm(txt_path.read_text(encoding="utf-8", errors="ignore"))
        if re.search(rf"(?<!\d){re.escape(qno)}(?:[.、．\s(（]|题)", txt):
            ids.append(src["source_id"])
    return ("yes_candidate" if ids else "missing_or_not_yet_paired", ";".join(ids))


def main() -> None:
    manifest_rows = read_csv(MANIFEST)
    candidate_rows = read_csv(CANDIDATE_MATRIX)
    reasoning_candidate_rows = read_csv(REASONING_CANDIDATES)
    visual_seed_rows = read_csv(VISUAL_SEEDS)

    source_rows = []
    suite_sources: dict[str, list[dict[str, str]]] = defaultdict(list)
    for item in manifest_rows:
        role = source_role(item["path"], item["source_id"])
        suite = suite_key(item["path"])
        visual = visual_risk(item["suffix"], item["method"], item["char_count"], role)
        row = {
            "source_id": item["source_id"],
            "suite_id": suite_id(suite),
            "suite": suite,
            "source_role": role,
            "path": item["path"],
            "suffix": item["suffix"],
            "exists": item["exists"],
            "status": item["status"],
            "reading_method": item["method"],
            "char_count": item["char_count"],
            "hit_count": item["hit_count"],
            "text_path": item["text_path"],
            "render_dir": item["render_dir"],
            "visual_risk": visual,
            "evidence_use": "raw_exam_source" if role in {"paper", "rubric_or_answer"} else "support_or_locator_after_pairing",
            "notes": "phase03 clean raw-source registry",
        }
        source_rows.append(row)
        suite_sources[suite].append(row)

    write_csv(OUT_SOURCE_CSV, source_rows, [
        "source_id", "suite_id", "suite", "source_role", "path", "suffix", "exists", "status",
        "reading_method", "char_count", "hit_count", "text_path", "render_dir", "visual_risk", "evidence_use", "notes",
    ])

    with OUT_SOURCE_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Raw Source Registry\n\n")
        f.write("This registry is built from extracted raw priority sources only. Old-draft locator rows are isolated elsewhere.\n\n")
        for suite in sorted(suite_sources):
            f.write(f"## {suite}\n\n")
            for src in sorted(suite_sources[suite], key=lambda r: r["source_id"]):
                f.write(f"- `{src['source_id']}` | {src['source_role']} | {src['suffix']} | {src['reading_method']} | visual={src['visual_risk']} | {src['path']}\n")
            f.write("\n")

    locator_rows = []
    for row in read_csv(SOURCE_LEDGER):
        notes = row.get("notes", "")
        status = row.get("status", "")
        if "old_artifact_locator_only" in notes or "not_evidence" in notes or row.get("source_type") == "other":
            locator_rows.append(row)
    with OUT_LOCATOR_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Locator-Only Isolation\n\n")
        f.write("The rows below are not raw evidence for Phase 03. They may help find failures or old contamination only.\n\n")
        f.write(f"- isolated rows: {len(locator_rows)}\n\n")
        for row in locator_rows[:160]:
            f.write(f"- `{row.get('source_id','')}` | {row.get('notes','')} | {row.get('path','')}\n")

    methods = defaultdict(int)
    failures = []
    for row in source_rows:
        methods[row["reading_method"]] += 1
        if row["status"] != "extracted":
            failures.append(row)
    with OUT_METHODS_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Source Reading Methods\n\n")
        for method, count in sorted(methods.items()):
            f.write(f"- {method}: {count}\n")
        f.write("\n## Visual-Risk Reading Notes\n\n")
        for row in source_rows:
            if row["visual_risk"] != "low":
                f.write(f"- `{row['source_id']}` | {row['suite']} | {row['visual_risk']} | {row['path']}\n")
    with OUT_FAILURES_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Source Failures And Fallbacks\n\n")
        if not failures:
            f.write("- No extraction failures in the 56-source priority queue.\n")
        else:
            for row in failures:
                f.write(f"- `{row['source_id']}` | {row['status']} | {row['path']}\n")

    suite_rows = []
    question_rows = []
    thinking_rows = []
    reasoning_rows = []
    blocked_rows = []
    duplicate_rows = []

    candidate_by_suite_q = defaultdict(list)
    for row in candidate_rows:
        candidate_by_suite_q[(row.get("suite", ""), row.get("question_no_guess", ""))].append(row)
    reasoning_by_suite_q = defaultdict(list)
    for row in reasoning_candidate_rows:
        reasoning_by_suite_q[(row.get("suite", ""), row.get("question_no_guess", ""))].append(row)
    visual_seed_by_suite = defaultdict(list)
    for row in visual_seed_rows:
        visual_seed_by_suite[row.get("suite", "")].append(row)

    visual_blockers = []

    for suite in sorted(suite_sources):
        srcs = suite_sources[suite]
        papers = [s for s in srcs if s["source_role"] == "paper"]
        nonpapers = [s for s in srcs if s["source_role"] != "paper"]
        q_count = 0
        visual_seed_count = 0
        visual_level = "medium" if any(s["visual_risk"] != "low" for s in srcs) else "low"
        for paper in papers:
            txt_path = Path(paper["text_path"])
            if not txt_path.exists():
                continue
            q_blocks = split_questions(txt_path.read_text(encoding="utf-8", errors="ignore"))
            q_count += len(q_blocks)
            for q in q_blocks:
                qno = q["qno"]
                sub = q["subq"]
                qid = f"Q-{suite}-{qno}" + (f"-{sub}" if sub else "")
                block = q["block"]
                scope = section_guess(block)
                cands = candidate_by_suite_q.get((suite, qno), [])
                rcands = reasoning_by_suite_q.get((suite, qno), [])
                hit_terms = ";".join(sorted(set(";".join(c.get("hit_terms", "") for c in cands).split(";")) - {""}))
                typology = ";".join(sorted(set(r.get("typology_guess", "") for r in rcands if r.get("typology_guess"))))
                answer_status, paired_sources = answer_status_for(qno, suite, nonpapers)
                option_count = int(q["option_count"] or 0)
                qtype = "选择题" if int(qno) <= 15 else "主观题"
                if option_count and option_count < 4 and qtype == "选择题":
                    opt_status = "incomplete_options_needs_visual"
                elif option_count >= 4:
                    opt_status = "complete_options_candidate"
                else:
                    opt_status = "not_option_question_or_needs_visual"
                visual_need = "yes" if "visual_source" in paper["visual_risk"] or opt_status == "incomplete_options_needs_visual" else "no_or_later"
                blocked_status = "pending_pairing"
                blocked_reason = ""
                if answer_status.startswith("missing") and scope in {"思维", "推理", "交叉"}:
                    blocked_status = "blocked_until_answer_or_rubric_pairing"
                    blocked_reason = "logic/thinking candidate without paired answer/rubric yet"
                if opt_status == "incomplete_options_needs_visual":
                    blocked_status = "blocked_until_options_visual_check"
                    blocked_reason = "choice options not fully detected in text"
                row = {
                    "question_id": qid,
                    "suite_id": suite_id(suite),
                    "source_id": paper["source_id"],
                    "stable_locator": f"{paper['source_id']}::Q{qno}{'('+sub+')' if sub else ''}",
                    "原始题号": f"{qno}{'('+sub+')' if sub else ''}",
                    "题型": qtype,
                    "部分归属": scope,
                    "是否完整题干": "text_candidate_needs_review",
                    "是否完整选项": opt_status,
                    "是否有答案": answer_status,
                    "是否有评分细则": "yes_candidate" if paired_sources else "missing_or_not_yet_paired",
                    "是否有讲评": "yes_candidate" if any("support" in s["source_role"] for s in nonpapers) else "not_found_yet",
                    "是否需要视觉核读": visual_need,
                    "是否已视觉核读": "no",
                    "知识节点": hit_terms,
                    "题型节点": typology,
                    "材料信号": "",
                    "设问动作": "",
                    "答案落点状态": "not_extracted_yet",
                    "推理规则状态": "not_extracted_yet",
                    "blocked_status": blocked_status,
                    "blocked_reason": blocked_reason,
                    "lane_A_classification": "initial_inventory_only",
                    "lane_B_classification": "pending_claudecode_phase03",
                    "A_B_conflict_status": "pending",
                    "final_classification": "pending",
                    "excerpt": stem_excerpt(block),
                    "paired_nonpaper_source_ids": paired_sources,
                }
                question_rows.append(row)
                if blocked_status.startswith("blocked"):
                    blocked_rows.append({
                        "question_id": qid,
                        "suite_id": suite_id(suite),
                        "source_id": paper["source_id"],
                        "blocked_status": blocked_status,
                        "blocked_reason": blocked_reason,
                        "next_action": "return to raw source/visual/rubric before promotion",
                    })
                if scope in {"思维", "交叉"}:
                    thinking_rows.append({
                        "question_id": qid,
                        "suite_id": suite_id(suite),
                        "stable_locator": row["stable_locator"],
                        "思维知识节点": hit_terms,
                        "材料信号": "",
                        "可写思维或方法": "",
                        "答题动作": "",
                        "设问类型": qtype,
                        "为什么能想到": "",
                        "答案落点": "",
                        "来源例题": suite + " " + row["原始题号"],
                        "同类题": "",
                        "易错点": "",
                        "是否可入学生稿": "no_pending_source_pairing",
                    })
                if scope in {"推理", "交叉"} or typology:
                    reasoning_rows.append({
                        "question_id": qid,
                        "suite_id": suite_id(suite),
                        "stable_locator": row["stable_locator"],
                        "原始题号": row["原始题号"],
                        "primary_reasoning_type": typology.split(";")[0] if typology else typology_for(block),
                        "secondary_reasoning_type": ";".join(typology.split(";")[1:]) if ";" in typology else "",
                        "logical_form": "",
                        "rule_slogan": "",
                        "valid_pattern": "",
                        "invalid_pattern_or_trap": "",
                        "same_type_question_ids": "",
                        "answer_key": "",
                        "explanation_status": "not_extracted_yet",
                        "blocked_status": blocked_status,
                    })

        existing_qids = {r["question_id"] for r in question_rows if r["suite_id"] == suite_id(suite)}
        for seed in visual_seed_by_suite.get(suite, []):
            qid = seed.get("question_id") or f"Q-{suite}-{seed.get('原始题号', 'VISUAL')}"
            if qid in existing_qids:
                continue
            visual_seed_count += 1
            paper_source_id = seed.get("paper_source_id") or (papers[0]["source_id"] if papers else "")
            paired_sources = seed.get("paired_nonpaper_source_ids", "")
            scope = seed.get("部分归属", "待判")
            qtype = seed.get("题型", "主观题")
            blocked_status = seed.get("blocked_status", "locked_pending_laneB_visual_confirmation")
            blocked_reason = seed.get("blocked_reason", "visual recovered seed needs lane B confirmation before promotion")
            row = {
                "question_id": qid,
                "suite_id": suite_id(suite),
                "source_id": paper_source_id,
                "stable_locator": seed.get("stable_locator", f"{paper_source_id}::visual_seed"),
                "原始题号": seed.get("原始题号", ""),
                "题型": qtype,
                "部分归属": scope,
                "是否完整题干": seed.get("是否完整题干", "visual_recovered_needs_review"),
                "是否完整选项": seed.get("是否完整选项", "not_option_question_or_needs_visual"),
                "是否有答案": seed.get("是否有答案", "yes_candidate" if paired_sources else "missing_or_not_yet_paired"),
                "是否有评分细则": seed.get("是否有评分细则", "yes_candidate" if paired_sources else "missing_or_not_yet_paired"),
                "是否有讲评": seed.get("是否有讲评", "not_found_yet"),
                "是否需要视觉核读": "yes",
                "是否已视觉核读": seed.get("是否已视觉核读", "codex_visual_seed_only"),
                "知识节点": seed.get("知识节点", ""),
                "题型节点": seed.get("题型节点", ""),
                "材料信号": seed.get("材料信号", ""),
                "设问动作": seed.get("设问动作", ""),
                "答案落点状态": seed.get("答案落点状态", "not_extracted_yet"),
                "推理规则状态": seed.get("推理规则状态", "not_extracted_yet"),
                "blocked_status": blocked_status,
                "blocked_reason": blocked_reason,
                "lane_A_classification": "visual_recovery_seed_initial_only",
                "lane_B_classification": "pending_claudecode_phase03",
                "A_B_conflict_status": "pending",
                "final_classification": "pending",
                "excerpt": seed.get("excerpt", ""),
                "paired_nonpaper_source_ids": paired_sources,
            }
            question_rows.append(row)
            if blocked_status not in {"ok", "ready_for_fusion"}:
                blocked_rows.append({
                    "question_id": qid,
                    "suite_id": suite_id(suite),
                    "source_id": paper_source_id,
                    "blocked_status": blocked_status,
                    "blocked_reason": blocked_reason,
                    "next_action": seed.get("next_action", "lane B visual confirmation and source pairing before promotion"),
                })
            visual_blockers.append({
                "suite": suite,
                "question_id": qid,
                "source_id": paper_source_id,
                "render_locator": seed.get("render_locator", ""),
                "reason": blocked_reason,
                "next_action": seed.get("next_action", "lane B visual confirmation"),
            })
            if scope in {"思维", "交叉"}:
                thinking_rows.append({
                    "question_id": qid,
                    "suite_id": suite_id(suite),
                    "stable_locator": row["stable_locator"],
                    "思维知识节点": row["知识节点"],
                    "材料信号": row["材料信号"],
                    "可写思维或方法": seed.get("可写思维或方法", ""),
                    "答题动作": row["设问动作"],
                    "设问类型": qtype,
                    "为什么能想到": seed.get("为什么能想到", ""),
                    "答案落点": seed.get("答案落点", ""),
                    "来源例题": suite + " " + row["原始题号"],
                    "同类题": "",
                    "易错点": seed.get("易错点", ""),
                    "是否可入学生稿": seed.get("是否可入学生稿", "no_pending_laneB_visual_confirmation"),
                })
            if scope in {"推理", "交叉"} or row["题型节点"]:
                reasoning_rows.append({
                    "question_id": qid,
                    "suite_id": suite_id(suite),
                    "stable_locator": row["stable_locator"],
                    "原始题号": row["原始题号"],
                    "primary_reasoning_type": (row["题型节点"].split(";")[0] if row["题型节点"] else seed.get("primary_reasoning_type", "")),
                    "secondary_reasoning_type": ";".join(row["题型节点"].split(";")[1:]) if ";" in row["题型节点"] else seed.get("secondary_reasoning_type", ""),
                    "logical_form": seed.get("logical_form", ""),
                    "rule_slogan": seed.get("rule_slogan", ""),
                    "valid_pattern": seed.get("valid_pattern", ""),
                    "invalid_pattern_or_trap": seed.get("invalid_pattern_or_trap", ""),
                    "same_type_question_ids": "",
                    "answer_key": seed.get("answer_key", ""),
                    "explanation_status": seed.get("explanation_status", "visual_seed_needs_laneB_confirmation"),
                    "blocked_status": blocked_status,
                })

        if papers and q_count == 0:
            visual_level = "high"
            for paper in papers:
                qid = f"Q-{suite}-UNPARSED-PAPER"
                if qid not in {r["question_id"] for r in question_rows}:
                    question_rows.append({
                        "question_id": qid,
                        "suite_id": suite_id(suite),
                        "source_id": paper["source_id"],
                        "stable_locator": f"{paper['source_id']}::paper_text_blank_all_render_pages",
                        "原始题号": "UNPARSED",
                        "题型": "suite_visual_blocker",
                        "部分归属": "missing",
                        "是否完整题干": "no_paper_text_blank",
                        "是否完整选项": "not_detected_paper_text_blank",
                        "是否有答案": "unknown_until_visual_inventory",
                        "是否有评分细则": "unknown_until_visual_inventory",
                        "是否有讲评": "unknown_until_visual_inventory",
                        "是否需要视觉核读": "yes",
                        "是否已视觉核读": "no_full_suite_visual_inventory",
                        "知识节点": "",
                        "题型节点": "",
                        "材料信号": "",
                        "设问动作": "",
                        "答案落点状态": "blocked_by_blank_paper_text",
                        "推理规则状态": "blocked_by_blank_paper_text",
                        "blocked_status": "blocked_until_full_paper_visual_or_ocr_question_inventory",
                        "blocked_reason": "paper PDF text layer is blank/thin; full question list must be recovered from rendered pages before coverage PASS",
                        "lane_A_classification": "suite_level_blank_paper_blocker",
                        "lane_B_classification": "pending_claudecode_phase03",
                        "A_B_conflict_status": "pending",
                        "final_classification": "pending",
                        "excerpt": "",
                        "paired_nonpaper_source_ids": ";".join(s["source_id"] for s in nonpapers),
                    })
                blocked_rows.append({
                    "question_id": qid,
                    "suite_id": suite_id(suite),
                    "source_id": paper["source_id"],
                    "blocked_status": "blocked_until_full_paper_visual_or_ocr_question_inventory",
                    "blocked_reason": "paper PDF text layer is blank/thin; full question list must be recovered from rendered pages before coverage PASS",
                    "next_action": "OCR or visually inspect every rendered page and replace suite-level blocker with question-level rows",
                })
                visual_blockers.append({
                    "suite": suite,
                    "question_id": qid,
                    "source_id": paper["source_id"],
                    "render_locator": paper["render_dir"],
                    "reason": "paper text blank/thin; question inventory cannot rely on text extraction",
                    "next_action": "OCR or visually inspect every rendered page; do not treat suite as empty",
                })

        suite_rows.append({
            "suite_id": suite_id(suite),
            "suite": suite,
            "source_ids": ";".join(s["source_id"] for s in srcs),
            "地区": re.sub(r"^20\d{2}", "", suite).replace("一模", "").replace("二模", "").replace("期中", "").replace("期末", ""),
            "年份": re.match(r"20\d{2}", suite).group(0) if re.match(r"20\d{2}", suite) else "",
            "考试阶段": suite[-2:],
            "题目范围": "paper_text_blank_visual_seed_partial" if papers and q_count == 0 and visual_seed_count else ("paper_text_blank_visual_inventory_required" if papers and q_count == 0 else ("paper_questions_detected" if papers else "no_paper")),
            "是否含思维部分": "yes_candidate" if any(r["部分归属"] in {"思维", "交叉"} and r["suite_id"] == suite_id(suite) for r in question_rows) else "not_detected_yet",
            "是否含推理部分": "yes_candidate" if any(r["部分归属"] in {"推理", "交叉"} and r["suite_id"] == suite_id(suite) for r in question_rows) else "not_detected_yet",
            "题目页范围": "from_paper_text_or_render",
            "答案页范围": "from_nonpaper_pairing",
            "评分细则页范围": "from_nonpaper_pairing",
            "讲评页范围": "from_support_sources",
            "题量检测值": str(q_count + visual_seed_count),
            "题量确认值": "partial_visual_seed_only_paper_text_blank" if papers and q_count == 0 and visual_seed_count else ("blocked_paper_text_blank" if papers and q_count == 0 else "pending_manual_or_laneB_check"),
            "视觉风险等级": visual_level,
            "是否进入全量扫描": "yes",
        })

    # Same suite can appear as separate display labels, e.g. lecture text title variants.
    seen_norm = defaultdict(list)
    for suite in sorted(suite_sources):
        key = re.sub(r"^20\d{2}年", "", suite)
        seen_norm[key].append(suite)
    for key, labels in seen_norm.items():
        if len(labels) > 1:
            duplicate_rows.append({"duplicate_key": key, "suite_labels": ";".join(labels), "action": "manual canonicalization before final PASS"})

    write_csv(OUT_SUITE_CSV, suite_rows, [
        "suite_id", "suite", "source_ids", "地区", "年份", "考试阶段", "题目范围", "是否含思维部分", "是否含推理部分",
        "题目页范围", "答案页范围", "评分细则页范围", "讲评页范围", "题量检测值", "题量确认值", "视觉风险等级", "是否进入全量扫描",
    ])
    write_csv(OUT_DUP_CSV, duplicate_rows, ["duplicate_key", "suite_labels", "action"])
    write_csv(OUT_Q_CSV, question_rows, list(question_rows[0].keys()) if question_rows else [])
    write_csv(OUT_THINK_CSV, thinking_rows, list(thinking_rows[0].keys()) if thinking_rows else [
        "question_id", "suite_id", "stable_locator", "思维知识节点", "材料信号", "可写思维或方法", "答题动作", "设问类型",
        "为什么能想到", "答案落点", "来源例题", "同类题", "易错点", "是否可入学生稿",
    ])
    write_csv(OUT_REASON_CSV, reasoning_rows, list(reasoning_rows[0].keys()) if reasoning_rows else [
        "question_id", "suite_id", "stable_locator", "原始题号", "primary_reasoning_type", "secondary_reasoning_type",
        "logical_form", "rule_slogan", "valid_pattern", "invalid_pattern_or_trap", "same_type_question_ids", "answer_key",
        "explanation_status", "blocked_status",
    ])
    write_csv(OUT_BLOCKED_CSV, blocked_rows, ["question_id", "suite_id", "source_id", "blocked_status", "blocked_reason", "next_action"])

    with OUT_VISUAL_BLOCKERS.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Visual Fallback Blockers\n\n")
        f.write("These rows are hard blockers for coverage PASS. They are source-control artifacts, not student-facing content.\n\n")
        if not visual_blockers:
            f.write("- No visual blockers recorded by the official Phase 03 inventory script.\n")
        for row in visual_blockers:
            f.write(f"- `{row['suite']}` | `{row['question_id']}` | `{row['source_id']}` | {row['reason']} | render={row['render_locator']} | next={row['next_action']}\n")

    with OUT_SUITE_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Suite Registry\n\n")
        for row in suite_rows:
            f.write(f"- `{row['suite_id']}` | sources={len(row['source_ids'].split(';'))} | questions={row['题量检测值']} | thinking={row['是否含思维部分']} | reasoning={row['是否含推理部分']} | visual={row['视觉风险等级']}\n")

    with OUT_MISSING_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Missing Expected Sources\n\n")
        missing = [r for r in suite_rows if "no_paper" in r["题目范围"]]
        if not missing:
            f.write("- No no-paper suite in the extracted 56-source priority queue.\n")
        for row in missing:
            f.write(f"- `{row['suite_id']}` | missing paper source in priority queue\n")

    with OUT_2026_2_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 2026 二模 Missing Or Blocked\n\n")
        f.write("- Current scan boundary: 56 extracted priority sources plus current run source inventory.\n")
        f.write("- This run did not find a confirmed 2026 二模 source inside the extracted priority queue.\n")
        f.write("- Status: `missing_or_blocked_until_new_source_appears`.\n")
        f.write("- Do not state that 2026 二模 objectively does not exist; only state the current source-root scan result.\n")

    with OUT_Q_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Question Coverage Matrix Summary\n\n")
        f.write(f"- question/sub-question rows: {len(question_rows)}\n")
        f.write(f"- thinking/交叉 rows: {len(thinking_rows)}\n")
        f.write(f"- reasoning/交叉 rows: {len(reasoning_rows)}\n")
        f.write(f"- blocked rows: {len(blocked_rows)}\n\n")
        for row in question_rows[:120]:
            f.write(f"- `{row['question_id']}` | {row['部分归属']} | {row['题型']} | {row['是否完整选项']} | {row['blocked_status']}\n")

    with OUT_THINK_MD.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Thinking Signal Chain Matrix\n\n")
        f.write("Initial inventory only. Blank material-signal and answer-action fields are intentional blockers for the next extraction pass.\n\n")
        for row in thinking_rows[:120]:
            f.write(f"- `{row['question_id']}` | {row['思维知识节点']} | {row['是否可入学生稿']}\n")

    by_type = defaultdict(list)
    for row in reasoning_rows:
        by_type[row["primary_reasoning_type"]].append(row["question_id"])
    with OUT_REASON_TREE.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Reasoning Typology Tree\n\n")
        f.write("Observed provisional tree from raw paper/rubric hits. Every node must be source-verified before student use.\n\n")
        for typ, qids in sorted(by_type.items()):
            f.write(f"## {typ}\n\n")
            f.write("本题型全部题目清单：\n\n")
            for qid in sorted(set(qids)):
                f.write(f"- `{qid}`\n")
            f.write("\n")

    with OUT_REPORT.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Registry And Question Inventory Report\n\n")
        f.write("Status: initial lane A inventory. It authorizes no student-facing text.\n\n")
        f.write(f"- raw sources: {len(source_rows)}\n")
        f.write(f"- suites: {len(suite_rows)}\n")
        f.write(f"- question/sub-question rows: {len(question_rows)}\n")
        f.write(f"- thinking matrix rows: {len(thinking_rows)}\n")
        f.write(f"- reasoning attachment rows: {len(reasoning_rows)}\n")
        f.write(f"- blocked rows: {len(blocked_rows)}\n")
        f.write(f"- visual blocker rows: {len(visual_blockers)}\n")
        f.write(f"- visual recovery seed rows used: {len(visual_seed_rows)}\n")
        f.write(f"- locator-only rows isolated: {len(locator_rows)}\n\n")
        f.write("Next: fill material signal, answer action, logical form, rule slogan, traps, and paired rubric/answer locators; then run ClaudeCode lane B full scan and A/B diff.\n")


if __name__ == "__main__":
    main()
