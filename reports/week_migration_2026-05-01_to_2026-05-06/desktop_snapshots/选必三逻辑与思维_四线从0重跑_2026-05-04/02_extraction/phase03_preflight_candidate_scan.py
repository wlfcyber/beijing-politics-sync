#!/usr/bin/env python3
"""Phase 03 preflight candidate scan.

This script does not promote evidence or produce student-facing content. It only
builds candidate queues from already extracted priority-source text so the next
manual/source-verified pass can work suite by suite.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


RUN_DIR = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
MANIFEST = RUN_DIR / "02_extraction/priority_queue_sources/priority_queue_extraction_manifest.csv"
OUT_MATRIX = RUN_DIR / "05_coverage/question_coverage_matrix_phase03_candidates.csv"
OUT_REASONING = RUN_DIR / "05_coverage/reasoning_typology_candidates_phase03.csv"
OUT_SNIPPETS = RUN_DIR / "03_entries/phase03_candidate_snippets_internal.md"
OUT_REPORT = RUN_DIR / "04_suite_reports/codex_suite_reports/phase03_preflight_candidate_scan_report.md"
OUT_VISUAL = RUN_DIR / "02_extraction/visual_fallback_queue_phase03.md"


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

BOUNDARY_TERMS = [
    "哲学与文化", "当代国际政治与经济", "法律与生活", "政治与法治", "经济与社会",
]

TYPOLOGY_RULES = [
    ("三段论", ["三段论", "中项", "大项", "小项"]),
    ("假言推理", ["假言", "充分条件", "必要条件", "充分必要条件", "肯定前件", "否定后件", "肯前", "肯后", "否前", "否后"]),
    ("选言推理", ["选言", "相容选言", "不相容选言"]),
    ("联言推理", ["联言"]),
    ("归纳推理与因果探求", ["归纳", "求同法", "求异法", "共变法", "剩余法", "因果"]),
    ("类比推理", ["类比"]),
    ("周延判断", ["周延", "主项", "谓项"]),
    ("换质换位", ["换质", "换位"]),
    ("逻辑三律与概念规则", ["矛盾律", "排中律", "同一律", "概念", "定义", "划分"]),
]


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    return text.replace("\u3000", " ")


def source_kind(path_text: str, source_id: str) -> str:
    joined = f"{path_text} {source_id}"
    if "试卷" in joined or "教师版" in joined or "原卷" in joined:
        return "paper"
    if "细则" in joined or "答案" in joined or "评分" in joined:
        return "rubric_or_answer"
    if "评标" in joined or "讲评" in joined or "其他材料" in joined:
        return "support_or_lecture"
    return "unknown"


def suite_key(path_text: str) -> str:
    candidates = re.findall(r"20\d{2}[\u4e00-\u9fa5]{2,4}(?:一模|二模|期中|期末)", path_text)
    if candidates:
        return candidates[-1]
    if "西城一模" in path_text:
        return "2024西城一模"
    if "海淀二模" in path_text:
        return "2024海淀二模"
    return "UNKNOWN_SUITE"


def hit_terms(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if term in text]


def nearest_question_no(lines: list[str], index: int) -> str:
    for i in range(index, max(-1, index - 35), -1):
        line = lines[i].strip()
        m = re.match(r"^(?:第)?(\d{1,2})(?:[.、．]|[􀆰])", line)
        if m:
            return m.group(1)
        m = re.search(r"(\d{1,2})[.(（](?:\d+|[一二三四])[)）]", line)
        if m:
            return m.group(1)
        m = re.match(r"^\(?([一二三四五六七八九十]+)\)?[、.．]", line)
        if m:
            return m.group(1)
    return ""


def snippet(lines: list[str], index: int, radius: int = 6) -> str:
    start = max(0, index - radius)
    end = min(len(lines), index + radius + 1)
    text = "\n".join(line.strip() for line in lines[start:end] if line.strip())
    return re.sub(r"\s+", " ", text)[:520]


def evidence_guess(kind: str, module_bucket: str) -> str:
    if kind == "paper" and module_bucket == "reasoning":
        return "candidate_needs_answer_key_or_rubric"
    if kind == "paper" and module_bucket == "thinking":
        return "candidate_needs_rubric_pairing"
    if kind == "rubric_or_answer":
        return "candidate_scoring_source_needs_question_pairing"
    if kind == "support_or_lecture":
        return "candidate_support_needs_primary_pairing"
    return "candidate_needs_source_pairing"


def typology_for(context: str) -> str:
    hits = []
    for label, keys in TYPOLOGY_RULES:
        if any(key in context for key in keys):
            hits.append(label)
    return ";".join(hits) if hits else "其他复合推理"


def main() -> None:
    rows = []
    reasoning_rows = []
    snippets_by_suite = defaultdict(list)
    visual_rows = []
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for item in csv.DictReader(f):
            if item.get("status") != "extracted":
                continue
            text_path = Path(item["text_path"])
            if not text_path.exists():
                continue
            raw = norm(text_path.read_text(encoding="utf-8", errors="ignore"))
            lines = raw.splitlines()
            kind = source_kind(item["path"], item["source_id"])
            suite = suite_key(item["path"])
            source_hits = 0
            for idx, line in enumerate(lines):
                t_hits = hit_terms(line, THINKING_TERMS)
                r_hits = hit_terms(line, REASONING_TERMS)
                if not t_hits and not r_hits:
                    continue
                context = snippet(lines, idx)
                b_hits = hit_terms(context, BOUNDARY_TERMS)
                module_bucket = "mixed"
                if r_hits and not t_hits:
                    module_bucket = "reasoning"
                elif t_hits and not r_hits:
                    module_bucket = "thinking"
                qno = nearest_question_no(lines, idx)
                status = "candidate_needs_manual_pairing"
                if b_hits and "逻辑与思维" not in context:
                    status = "candidate_boundary_check_required"
                row = {
                    "suite": suite,
                    "question_no_guess": qno,
                    "module_bucket_guess": module_bucket,
                    "candidate_status": status,
                    "evidence_level_guess": evidence_guess(kind, module_bucket),
                    "source_kind": kind,
                    "source_id": item["source_id"],
                    "source_path": item["path"],
                    "hit_terms": ";".join(dict.fromkeys(t_hits + r_hits)),
                    "boundary_terms": ";".join(b_hits),
                    "snippet": context,
                    "next_action": "pair paper with rubric/answer, then classify A-formal/A-support/B-choice-signal/C-boundary/missing",
                }
                rows.append(row)
                source_hits += 1
                snippets_by_suite[suite].append(row)
                if r_hits:
                    reasoning_rows.append({
                        "suite": suite,
                        "question_no_guess": qno,
                        "typology_guess": typology_for(context),
                        "source_kind": kind,
                        "source_id": item["source_id"],
                        "hit_terms": ";".join(dict.fromkeys(r_hits)),
                        "snippet": context,
                        "next_action": "verify full stem/options or scoring rule; attach to all-question typology table only after source pairing",
                    })
            if kind != "paper" and item.get("suffix", "").lower() in {".pptx", ".pdf"} and source_hits:
                visual_rows.append((suite, item["source_id"], item["path"], "hit-bearing visual source; inspect slides/pages before final classification"))

    rows.sort(key=lambda r: (r["suite"], r["question_no_guess"], r["source_id"]))
    reasoning_rows.sort(key=lambda r: (r["typology_guess"], r["suite"], r["question_no_guess"], r["source_id"]))

    OUT_MATRIX.parent.mkdir(parents=True, exist_ok=True)
    with OUT_MATRIX.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [
            "suite", "question_no_guess", "module_bucket_guess", "candidate_status", "evidence_level_guess",
            "source_kind", "source_id", "source_path", "hit_terms", "boundary_terms", "snippet", "next_action",
        ])
        writer.writeheader()
        writer.writerows(rows)

    with OUT_REASONING.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(reasoning_rows[0].keys()) if reasoning_rows else [
            "suite", "question_no_guess", "typology_guess", "source_kind", "source_id", "hit_terms", "snippet", "next_action",
        ])
        writer.writeheader()
        writer.writerows(reasoning_rows)

    with OUT_SNIPPETS.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Candidate Snippets Internal\n\n")
        f.write("This is a preflight queue only. It is not evidence promotion and must not enter the student artifact.\n\n")
        for suite in sorted(snippets_by_suite):
            f.write(f"## {suite}\n\n")
            for row in snippets_by_suite[suite][:80]:
                f.write(f"- Q{row['question_no_guess'] or '?'} | {row['module_bucket_guess']} | {row['source_kind']} | {row['source_id']} | {row['hit_terms']}\n")
                f.write(f"  - {row['snippet']}\n")
            f.write("\n")

    by_suite = defaultdict(int)
    by_bucket = defaultdict(int)
    for row in rows:
        by_suite[row["suite"]] += 1
        by_bucket[row["module_bucket_guess"]] += 1

    with OUT_REPORT.open("w", encoding="utf-8") as f:
        f.write("# Phase 03 Preflight Candidate Scan Report\n\n")
        f.write("Status: PRE-GPT-GATE_PREFLIGHT_ONLY. This report only prepares queues; it does not authorize full Phase 03 promotion.\n\n")
        f.write(f"- candidate hit rows: {len(rows)}\n")
        f.write(f"- reasoning typology rows: {len(reasoning_rows)}\n")
        f.write(f"- suites with hits: {len(by_suite)}\n\n")
        f.write("## By Module Bucket\n\n")
        for key, count in sorted(by_bucket.items()):
            f.write(f"- {key}: {count}\n")
        f.write("\n## By Suite\n\n")
        for key, count in sorted(by_suite.items()):
            f.write(f"- {key}: {count}\n")
        f.write("\n## Gate Note\n\n")
        f.write("Next step after GPT Phase 02 advice: pair each candidate with its paper/rubric/answer source and write suite-level closure reports. Do not generate student text from this preflight table.\n")

    with OUT_VISUAL.open("a", encoding="utf-8") as f:
        f.write("\n## Phase 03 Preflight Visual Follow-up\n\n")
        for suite, sid, path, note in visual_rows:
            f.write(f"- {suite} | {sid} | {path} | {note}\n")


if __name__ == "__main__":
    main()
