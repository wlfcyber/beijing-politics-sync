#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader


ROOT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync")
RUN_DIR = ROOT / "reports/philosophy_v3_reaudit_2026-04-26"
OUT_DIR = RUN_DIR / "artifacts"
FRAMEWORK_INVENTORY = OUT_DIR / "framework_entry_inventory.csv"
WRONG_OPTION_LIBRARY = RUN_DIR / "freeze/北京高考政治错肢库_持续更新版.md"
SOURCE_INVENTORY = RUN_DIR / "freeze/必修四哲学_2024-2026题源穷尽清单.md"
BUNDLE_DIR = ROOT / "data/preprocessed_corpus/gpt_suite_bundles"

DESKTOP_ROOTS = [
    Path("/Users/wanglifei/Desktop/2024模拟题"),
    Path("/Users/wanglifei/Desktop/2025模拟题"),
    Path("/Users/wanglifei/Desktop/2026模拟题"),
]

DISTRICTS = [
    "东城",
    "西城",
    "朝阳",
    "海淀",
    "丰台",
    "石景山",
    "门头沟",
    "房山",
    "通州",
    "顺义",
    "昌平",
    "延庆",
]
STAGES = ["一模", "二模", "期中", "期末"]

A_DETAIL_MARKERS = [
    "本题标准和变通",
    "评分细则",
    "评分标准",
    "阅卷细则",
    "阅卷总结",
    "阅卷报告",
    "评阅解析",
    "学生表现",
    "学生问题",
    "变通",
]
B_ANGLE_MARKERS = [
    "可从",
    "角度作答",
    "角度回答",
    "等级水平",
    "等级描述",
    "水平 4",
    "水平4",
    "水平 3",
    "水平3",
    "观点鲜明",
]
D_REFERENCE_MARKERS = [
    "参考答案",
    "答案及评分参考",
    "教师版",
]
SOURCE_HINT_MARKERS = [
    "细则",
    "阅卷",
    "评标",
    "评分",
    "讲评",
    "答案解析",
    "答案及评分参考",
    "教师版",
]


@dataclass
class BundleSection:
    bundle_path: str
    title: str
    source_path: str
    status: str
    method: str
    chars: int
    body: str
    local_path: str = ""
    local_state: str = ""
    local_chars: int = -1


def clean_cell(cell: str) -> str:
    return re.sub(r"\s+", " ", cell.replace("`", "")).strip()


def split_md_row(line: str) -> list[str]:
    return [clean_cell(part) for part in line.strip().strip("|").split("|")]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def extract_year(text: str) -> str:
    m = re.search(r"(20\d{2})", text)
    return m.group(1) if m else ""


def extract_district(text: str) -> str:
    for district in DISTRICTS:
        if district in text:
            return district
    return ""


def extract_stage(text: str) -> str:
    for stage in STAGES:
        if stage in text:
            return stage
    if "高三（上）" in text or "高三上" in text:
        return "期末"
    return ""


def extract_question(text: str) -> tuple[str, int | None]:
    patterns = [
        r"第\s*([0-9]{1,2})\s*题(?:第?（?([0-9一二三四五六七八九十]+)）?问|（([0-9一二三四五六七八九十]+)）)?",
        r"\bQ\s*([0-9]{1,2})",
        r"\bq\s*([0-9]{1,2})",
    ]
    for pattern in patterns:
        m = re.search(pattern, text)
        if not m:
            continue
        qnum = int(m.group(1))
        q = f"第{qnum}题"
        if len(m.groups()) >= 2 and m.group(2):
            q += f"第（{m.group(2)}）问"
        elif len(m.groups()) >= 3 and m.group(3):
            q += f"（{m.group(3)}）"
        return q, qnum
    return "", None


def nature_from_qnum(qnum: int | None) -> str:
    if qnum is None:
        return "unknown"
    return "choice" if qnum <= 15 else "subjective"


def bundle_index() -> list[tuple[str, Path]]:
    return [(path.name, path) for path in sorted(BUNDLE_DIR.glob("*.md"))]


def find_bundle(year: str, district: str, stage: str, bundles: list[tuple[str, Path]]) -> tuple[str, str]:
    if not year or not district:
        return "", "missing-year-or-district"
    exact_suite = f"{year}{district}{stage}" if stage else ""
    if exact_suite:
        exact_candidates = []
        for name, path in bundles:
            suite_label = name.rsplit("__", 1)[-1]
            if exact_suite in suite_label:
                exact_candidates.append(path)
        if exact_candidates:
            if len(exact_candidates) > 1:
                return str(exact_candidates[0].relative_to(ROOT)), f"multiple:{len(exact_candidates)}"
            return str(exact_candidates[0].relative_to(ROOT)), "found"
    candidates: list[Path] = []
    for name, path in bundles:
        if year in name and district in name and (not stage or stage in name):
            candidates.append(path)
    if not candidates:
        for name, path in bundles:
            if year in name and district in name:
                candidates.append(path)
    if not candidates:
        return "", "not-found"
    if len(candidates) > 1:
        return str(candidates[0].relative_to(ROOT)), f"multiple:{len(candidates)}"
    return str(candidates[0].relative_to(ROOT)), "found"


def source_terms(source: str) -> list[str]:
    terms = []
    for marker in SOURCE_HINT_MARKERS:
        if marker in source:
            terms.append(marker)
    m = re.search(r"（([^）]+)）", source)
    if m:
        for token in re.split(r"[ +/、，,；;]+", m.group(1)):
            token = token.strip()
            if len(token) >= 2:
                terms.append(token)
    return terms


def trigger_terms(trigger: str) -> list[str]:
    terms = []
    for term in re.split(r"[/；;、，, ]+", trigger):
        term = clean_cell(term)
        if len(term) >= 2 and term not in {"观点", "角度", "方法", "哲学", "文化", "正确项"}:
            terms.append(term)
    return terms[:16]


def local_file_index() -> list[Path]:
    files: list[Path] = []
    for root in DESKTOP_ROOTS:
        if root.exists():
            files.extend(path for path in root.rglob("*") if path.is_file())
    return files


LOCAL_FILES = local_file_index()


def source_path_tokens(source_path: str) -> tuple[str, str, str, str, str]:
    year = extract_year(source_path)
    district = extract_district(source_path)
    stage = extract_stage(source_path)
    category = ""
    for token in ["细则", "试卷", "其他材料", "答案", "补充材料"]:
        if token in source_path:
            category = token
            break
    suffix = Path(source_path.replace("\\", "/")).suffix.lower()
    return year, district, stage, category, suffix


def find_local_source(source_path: str) -> str:
    if not source_path:
        return ""
    year, district, stage, category, suffix = source_path_tokens(source_path)
    if not year or not district or not suffix:
        return ""
    candidates = []
    for path in LOCAL_FILES:
        text = str(path)
        if suffix and path.suffix.lower() != suffix:
            continue
        if year not in text or district not in text:
            continue
        if stage and stage not in text:
            continue
        if category and category not in text:
            continue
        candidates.append(path)
    if len(candidates) == 1:
        return str(candidates[0])
    if candidates:
        candidates.sort(key=lambda p: (len(str(p)), str(p)))
        return str(candidates[0])
    return ""


def pdf_text_chars(path: str) -> int:
    try:
        reader = PdfReader(path)
        return sum(len(page.extract_text() or "") for page in reader.pages)
    except Exception:
        return -1


def parse_bundle_sections(bundle_path: str) -> list[BundleSection]:
    if not bundle_path:
        return []
    path = ROOT / bundle_path
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    matches = list(re.finditer(r"^## (.+)$", text, flags=re.M))
    sections: list[BundleSection] = []
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        raw = text[start:end].strip()
        meta_block, _, body = raw.partition("\n\n")
        meta: dict[str, str] = {}
        for line in meta_block.splitlines():
            m = re.match(r"- ([a-z_]+): `?(.*?)`?$", line.strip())
            if m:
                meta[m.group(1)] = m.group(2).strip("`")
        chars = 0
        try:
            chars = int(meta.get("chars", "0") or "0")
        except ValueError:
            chars = 0
        source_path = meta.get("source_path", "")
        local_path = find_local_source(source_path)
        local_chars = -1
        local_state = ""
        if local_path:
            if local_path.lower().endswith(".pdf"):
                local_chars = pdf_text_chars(local_path)
                if local_chars == 0:
                    local_state = "raw-present-scan-no-text"
                elif local_chars > 0:
                    local_state = "raw-present-text-layer"
                else:
                    local_state = "raw-present-read-error"
            else:
                local_state = "raw-present-non-pdf"
        sections.append(
            BundleSection(
                bundle_path=bundle_path,
                title=title,
                source_path=source_path,
                status=meta.get("status", ""),
                method=meta.get("method", ""),
                chars=chars,
                body=body,
                local_path=local_path,
                local_state=local_state,
                local_chars=local_chars,
            )
        )
    return sections


BUNDLE_SECTION_CACHE: dict[str, list[BundleSection]] = {}


def get_sections(bundle_path: str) -> list[BundleSection]:
    if bundle_path not in BUNDLE_SECTION_CACHE:
        BUNDLE_SECTION_CACHE[bundle_path] = parse_bundle_sections(bundle_path)
    return BUNDLE_SECTION_CACHE[bundle_path]


def classify_section(section: BundleSection) -> str:
    title_body = f"{section.title}\n{section.body}"
    if (
        "rendered-ocr-needed" in section.status
        or "No reliable text layer" in section.body
        or (section.chars == 0 and section.local_state == "raw-present-scan-no-text")
    ):
        return "E_ocr_needed"
    title_has_scoring = any(marker in section.title for marker in ["细则", "阅卷", "评标", "评分", "讲评"])
    title_has_ppt = ".ppt" in section.title.lower() or "PPT" in section.title or "ppt" in section.title
    if title_has_scoring and any(marker in title_body for marker in A_DETAIL_MARKERS) and "分" in title_body:
        if title_has_ppt or ("可从" in title_body and "等级" in title_body and "本题标准和变通" not in title_body):
            return "B_angle_list"
        return "A_scoring_detail"
    if title_has_scoring or title_has_ppt:
        if any(marker in title_body for marker in B_ANGLE_MARKERS):
            return "B_angle_list"
        return "B_scoring_source_needs_content_check"
    if any(marker in title_body[:1200] for marker in D_REFERENCE_MARKERS):
        return "D_reference_answer"
    if "试卷" in section.title:
        return "C_paper_or_teacher_source"
    return "E_unclassified_source"


def grade_rank(grade: str) -> int:
    if grade.startswith("A_"):
        return 5
    if grade.startswith("B_"):
        return 4
    if grade.startswith("C_"):
        return 3
    if grade.startswith("D_"):
        return 2
    return 1


def section_trigger_hits(section: BundleSection, trigger: str) -> list[str]:
    body = section.body
    return [term for term in trigger_terms(trigger) if term and term in body]


def section_source_hint_hits(section: BundleSection, source: str) -> list[str]:
    title_body = f"{section.title}\n{section.source_path}\n{section.body[:1200]}"
    return [term for term in source_terms(source) if term and term in title_body]


def best_section_for_entry(entry: dict[str, str]) -> tuple[BundleSection | None, str, list[str], list[str]]:
    sections = get_sections(entry.get("bundle_path", ""))
    if not sections:
        return None, "E_source_not_mapped", [], []
    best: tuple[int, int, int, BundleSection, str, list[str], list[str]] | None = None
    for section in sections:
        grade = classify_section(section)
        hits = section_trigger_hits(section, entry.get("trigger", ""))
        hints = section_source_hint_hits(section, entry.get("source", ""))
        qnum = re.sub(r"\D", "", entry.get("question", ""))
        qhit = 1 if qnum and (f"{qnum}." in section.body or f"{qnum}．" in section.body or f"{qnum} " in section.body) else 0
        score = (
            grade_rank(grade),
            min(len(hits), 8),
            len(hints) + qhit,
        )
        if best is None or score > best[:3]:
            best = (*score, section, grade, hits, hints)
    assert best is not None
    _, _, _, section, grade, hits, hints = best
    return section, grade, hits, hints


def bundle_has_choice_answer_key(bundle_path: str, qnum: int | None) -> str:
    if not bundle_path or qnum is None:
        return "unknown"
    path = ROOT / bundle_path
    if not path.exists():
        return "missing-bundle"
    text = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"答案\s*[A-D]", text) and ("选择题" in text or "题号" in text):
        return "answer-key-present"
    if re.search(rf"{qnum}\s*[\.．、]\s*[A-D]", text):
        return "answer-key-present"
    if re.search(r"1\s*[\.．、]\s*[A-D].{0,80}2\s*[\.．、]\s*[A-D]", text, flags=re.S):
        return "answer-key-present"
    if "参考答案" in text and re.search(r"\b[A-D]\b", text):
        return "possible-answer-key"
    return "answer-key-not-detected"


def review_framework_entries(entries: list[dict[str, str]]) -> list[dict[str, str]]:
    reviewed: list[dict[str, str]] = []
    for entry in entries:
        source = entry.get("source", "")
        q, qnum = extract_question(source)
        nature = entry.get("question_nature") or nature_from_qnum(qnum)
        bundle_path = entry.get("bundle_path", "")
        section, section_grade, trigger_hits, hint_hits = best_section_for_entry(entry)
        answer_key_state = bundle_has_choice_answer_key(bundle_path, qnum)

        if nature == "choice":
            if not bundle_path and "2024" in source and "门头沟" in source:
                final_status = "C_verified_by_worker_report"
                final_grade = "C"
                recommended_action = "keep-choice-source-with-worker-boundary"
                support_path = "reports/parallel_closure_2026-04-25/worker_2024_mentougou_yimo.md"
                support_note = "2024门头沟一模原套卷未在 suite bundle；worker 报告记录外部答案版 PDF、逐页读图和答案表。"
            elif bundle_path and answer_key_state in {"answer-key-present", "possible-answer-key"}:
                final_status = "C_verified_choice_source"
                final_grade = "C"
                recommended_action = "keep-choice-source"
                support_path = bundle_path
                support_note = answer_key_state
            else:
                final_status = "E_choice_key_or_stem_not_confirmed"
                final_grade = "E"
                recommended_action = "needs-choice-answer-key"
                support_path = bundle_path
                support_note = answer_key_state
        else:
            support_path = section.bundle_path if section else bundle_path
            support_note = section.title if section else "no supporting section"
            if "用户补充" in source and (not section or "用户补充" not in f"{section.title}\n{section.body}"):
                final_status = "E_user_supplement_not_in_workspace"
                final_grade = "E"
                recommended_action = "needs-user-supplement-or-downgrade"
            elif section_grade.startswith("A_"):
                if trigger_hits:
                    final_status = "A_verified_scoring_source"
                    final_grade = "A"
                    recommended_action = "keep-formal-chain"
                else:
                    final_status = "A_scoring_source_trigger_not_text_matched"
                    final_grade = "A"
                    recommended_action = "keep-source-but-chain-needs-human-check"
            elif section_grade.startswith("B_"):
                final_status = "B_angle_or_scoring_source"
                final_grade = "B"
                recommended_action = "keep-as-angle-list-or-organizer-chain"
            elif section_grade.startswith("D_"):
                final_status = "D_reference_only"
                final_grade = "D"
                recommended_action = "downgrade-reference-only"
            elif section_grade == "E_ocr_needed":
                final_status = "E_ocr_needed_or_unsynced_render"
                final_grade = "E"
                recommended_action = "needs-ocr-before-formal-use"
            else:
                final_status = "E_source_not_proven"
                final_grade = "E"
                recommended_action = "source-missing-or-delete-candidate"

        reviewed.append(
            {
                **entry,
                "qnum": str(qnum or ""),
                "final_grade": final_grade,
                "final_status": final_status,
                "recommended_action": recommended_action,
                "support_path": support_path,
                "support_note": support_note,
                "support_section_grade": section_grade,
                "support_trigger_hits": ";".join(trigger_hits),
                "support_source_hint_hits": ";".join(hint_hits),
                "choice_answer_key_state": answer_key_state,
                "local_raw_path": section.local_path if section else "",
                "local_raw_state": section.local_state if section else "",
                "local_raw_chars": str(section.local_chars) if section and section.local_chars >= 0 else "",
            }
        )
    return reviewed


def parse_wrong_option_rows() -> list[dict[str, str]]:
    lines = WRONG_OPTION_LIBRARY.read_text(encoding="utf-8").splitlines()
    rows: list[dict[str, str]] = []
    current_batch = ""
    current_evidence_note = ""
    for line_no, line in enumerate(lines, 1):
        if line.startswith("## "):
            current_batch = line.lstrip("#").strip()
            current_evidence_note = ""
        elif line.startswith("来源："):
            current_evidence_note = clean_cell(line.removeprefix("来源："))
        if not line.startswith("|"):
            continue
        cols = split_md_row(line)
        if len(cols) < 9 or cols[0] in {"所属模块", "---"}:
            continue
        source = cols[-1]
        if not re.search(r"20\d{2}", source):
            continue
        year = extract_year(source)
        district = extract_district(source)
        stage = extract_stage(source)
        question, qnum = extract_question(source)
        rows.append(
            {
                "audit_id": f"V3-WO-{len(rows)+1:04d}",
                "line": str(line_no),
                "batch": current_batch,
                "evidence_note": current_evidence_note,
                "module": cols[0],
                "wrong_statement": cols[1],
                "error_type": cols[2],
                "source": source,
                "year": year,
                "district": district,
                "stage": stage,
                "question": question,
                "qnum": str(qnum or ""),
                "question_nature": nature_from_qnum(qnum),
            }
        )
    return rows


def review_wrong_option_sources(rows: list[dict[str, str]], bundles: list[tuple[str, Path]]) -> list[dict[str, str]]:
    reviewed: list[dict[str, str]] = []
    for row in rows:
        bundle_path, bundle_state = find_bundle(row["year"], row["district"], row["stage"], bundles)
        qnum = int(row["qnum"]) if row["qnum"].isdigit() else None
        answer_key_state = bundle_has_choice_answer_key(bundle_path, qnum)
        evidence_note = row.get("evidence_note", "")
        if bundle_path and answer_key_state in {"answer-key-present", "possible-answer-key"}:
            status = "C_verified_choice_source"
            action = "keep-source"
            support = bundle_path
        elif "worker_" in evidence_note or "worker_" in row.get("batch", "") or "答案表" in evidence_note:
            status = "C_worker_report_source"
            action = "keep-with-worker-report-boundary"
            support = evidence_note
        elif bundle_path:
            status = "E_choice_key_not_detected"
            action = "needs-answer-key-check"
            support = bundle_path
        else:
            status = "E_source_not_mapped"
            action = "needs-source"
            support = ""
        reviewed.append(
            {
                **row,
                "bundle_path": bundle_path,
                "bundle_state": bundle_state,
                "choice_answer_key_state": answer_key_state,
                "final_status": status,
                "recommended_action": action,
                "support_path": support,
            }
        )
    return reviewed


def parse_source_inventory_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line_no, line in enumerate(SOURCE_INVENTORY.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        cols = split_md_row(line)
        if len(cols) < 10 or cols[0] in {"年份", "---"}:
            continue
        year, district, stage = cols[0], cols[1], cols[2]
        rows.append(
            {
                "line": str(line_no),
                "year": year,
                "district": district,
                "stage": stage,
                "question_range": cols[3],
                "question_type": cols[4],
                "file_source": cols[5],
                "answer_key_state_old": cols[6],
                "rubric_state_old": cols[7],
                "old_closed_state": cols[8],
                "old_notes": cols[9],
            }
        )
    return rows


def review_suite_inventory(rows: list[dict[str, str]], framework_rows: list[dict[str, str]], wrong_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped_framework = defaultdict(list)
    for row in framework_rows:
        key = (row.get("year", ""), row.get("district", ""), row.get("stage", ""))
        grouped_framework[key].append(row)
    grouped_wrong = defaultdict(list)
    for row in wrong_rows:
        key = (row.get("year", ""), row.get("district", ""), row.get("stage", ""))
        grouped_wrong[key].append(row)

    reviewed: list[dict[str, str]] = []
    for row in rows:
        key = (row["year"], row["district"], row["stage"])
        f_rows = grouped_framework.get(key, [])
        w_rows = grouped_wrong.get(key, [])
        f_statuses = Counter(r.get("final_status", "") for r in f_rows)
        w_statuses = Counter(r.get("final_status", "") for r in w_rows)
        all_statuses = set(f_statuses) | set(w_statuses)
        notes = row.get("old_notes", "")
        if row["old_closed_state"] == "明确排除":
            verdict = "confirmed-excluded"
            action = "keep-exclusion"
        elif any(status.startswith("E_") for status in all_statuses):
            verdict = "old-closed-needs-boundary-or-evidence"
            action = "do-not-call-unqualified-closed"
        elif any(status.startswith("D_") for status in all_statuses) or "reference-only" in notes or "无详细" in notes:
            verdict = "closed-with-reference-boundary"
            action = "downgrade-closed-wording"
        elif any(status.startswith("B_") for status in all_statuses):
            verdict = "closed-with-angle-boundary"
            action = "keep-but-mark-B-boundary"
        elif f_rows or w_rows:
            verdict = "source-reviewed"
            action = "keep-source-reviewed"
        else:
            verdict = "not-in-v3-entry-scope"
            action = "no-framework-or-wrong-option-entry-found"
        reviewed.append(
            {
                **row,
                "framework_entry_count": str(len(f_rows)),
                "wrong_option_entry_count": str(len(w_rows)),
                "framework_statuses": ";".join(f"{k}:{v}" for k, v in sorted(f_statuses.items())),
                "wrong_option_statuses": ";".join(f"{k}:{v}" for k, v in sorted(w_statuses.items())),
                "v3_suite_verdict": verdict,
                "recommended_action": action,
            }
        )
    return reviewed


def aggregate_source_keys(framework_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped = defaultdict(list)
    for row in framework_rows:
        key = (row.get("year", ""), row.get("district", ""), row.get("stage", ""), row.get("source", ""))
        grouped[key].append(row)
    source_rows: list[dict[str, str]] = []
    for (year, district, stage, source), rows in sorted(grouped.items()):
        status_counts = Counter(row["final_status"] for row in rows)
        grade_counts = Counter(row["final_grade"] for row in rows)
        support_paths = sorted(set(row.get("support_path", "") for row in rows if row.get("support_path", "")))
        source_rows.append(
            {
                "source_key": f"{year}-{district}-{stage}-{source}",
                "year": year,
                "district": district,
                "stage": stage,
                "source": source,
                "entry_count": str(len(rows)),
                "final_grades": ";".join(f"{k}:{v}" for k, v in sorted(grade_counts.items())),
                "final_statuses": ";".join(f"{k}:{v}" for k, v in sorted(status_counts.items())),
                "support_paths": ";".join(support_paths[:4]),
                "source_review_result": "reviewed",
            }
        )
    return source_rows


def md_table(rows: Iterable[dict[str, str]], fields: list[str], limit: int | None = None) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "|" + "|".join(["---"] * len(fields)) + "|"]
    count = 0
    for row in rows:
        if limit is not None and count >= limit:
            break
        values = [str(row.get(field, "")).replace("|", "／") for field in fields]
        lines.append("| " + " | ".join(values) + " |")
        count += 1
    return lines


def write_summary(
    framework_rows: list[dict[str, str]],
    wrong_rows: list[dict[str, str]],
    source_rows: list[dict[str, str]],
    suite_rows: list[dict[str, str]],
) -> None:
    f_status = Counter(row["final_status"] for row in framework_rows)
    f_grade = Counter(row["final_grade"] for row in framework_rows)
    w_status = Counter(row["final_status"] for row in wrong_rows)
    suite_verdict = Counter(row["v3_suite_verdict"] for row in suite_rows)
    risky_framework = [
        row
        for row in framework_rows
        if row["final_grade"] in {"D", "E"} or row["final_status"] in {"B_angle_or_scoring_source", "A_scoring_source_trigger_not_text_matched"}
    ]
    risky_suites = [row for row in suite_rows if row["v3_suite_verdict"] != "source-reviewed"]

    lines = [
        "# v3 全来源复核汇总",
        "",
        "## 范围",
        "",
        f"- 框架触发条目：{len(framework_rows)}",
        f"- 框架不同来源键：{len(source_rows)}",
        f"- 错肢库来源行：{len(wrong_rows)}",
        f"- 旧题源清单套卷行：{len(suite_rows)}",
        "",
        "## 框架条目最终证据等级",
        "",
    ]
    for key in ["A", "B", "C", "D", "E"]:
        lines.append(f"- {key}: {f_grade.get(key, 0)}")
    lines.extend(["", "## 框架条目最终状态", ""])
    for key, value in sorted(f_status.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## 错肢库来源状态", ""])
    for key, value in sorted(w_status.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## 题源清单 v3 判定", ""])
    for key, value in sorted(suite_verdict.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## 需降级/补证/边界标注的框架条目前 120 条", ""])
    lines.extend(
        md_table(
            risky_framework,
            [
                "audit_id",
                "final_grade",
                "final_status",
                "recommended_action",
                "source",
                "support_path",
                "support_note",
                "support_trigger_hits",
            ],
            limit=120,
        )
    )
    lines.extend(["", "## 需改写闭环口径的题源清单行", ""])
    lines.extend(
        md_table(
            risky_suites,
            [
                "year",
                "district",
                "stage",
                "old_closed_state",
                "v3_suite_verdict",
                "recommended_action",
                "framework_statuses",
                "wrong_option_statuses",
            ],
            limit=None,
        )
    )
    lines.extend(
        [
            "",
            "## 结论口径",
            "",
            "- 本报告完成的是“来源层复核”：每条旧框架来源键、每条错肢库来源行、每个旧题源清单套卷行都已给出 v3 来源状态。",
            "- A/B/C 可作为继续修订草案的输入；D 只能作 reference-only 或方向边界；E 不得进入正式框架，必须补 OCR/补用户截图/补原件后再使用。",
            "- `全来源复核_边界与缺口清单.md` 汇总了需要降级、补证和改写闭环口径的条目；完整逐行结果见同目录 CSV。",
            "- 本报告不直接覆盖正式总框架和错肢库；下一步如要交付 v3 正文，应按本表生成 diffable draft。",
        ]
    )
    (OUT_DIR / "all_source_reaudit_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_boundary_report(
    framework_rows: list[dict[str, str]],
    wrong_rows: list[dict[str, str]],
    suite_rows: list[dict[str, str]],
) -> None:
    framework_status = Counter(row["final_status"] for row in framework_rows)
    framework_grade = Counter(row["final_grade"] for row in framework_rows)
    wrong_status = Counter(row["final_status"] for row in wrong_rows)

    framework_de = [row for row in framework_rows if row["final_grade"] in {"D", "E"}]
    framework_b = [row for row in framework_rows if row["final_status"] == "B_angle_or_scoring_source"]
    framework_a_chain = [
        row for row in framework_rows if row["final_status"] == "A_scoring_source_trigger_not_text_matched"
    ]
    wrong_e_group = defaultdict(Counter)
    for row in wrong_rows:
        if row["final_status"].startswith("E_"):
            wrong_e_group[(row["year"], row["district"], row["stage"])][row["final_status"]] += 1
    wrong_e_rows = [
        {
            "year": year,
            "district": district,
            "stage": stage,
            "status_counts": ";".join(f"{k}:{v}" for k, v in sorted(counter.items())),
            "recommended_action": "needs-answer-key-check",
        }
        for (year, district, stage), counter in sorted(wrong_e_group.items())
    ]
    suite_boundary_rows = [row for row in suite_rows if row["v3_suite_verdict"] != "source-reviewed"]

    lines = [
        "# v3 全来源复核：边界与缺口清单",
        "",
        "## 使用口径",
        "",
        "- 本清单只记录来源复核结论，不直接改写正式总框架、错肢库或题源清单。",
        "- D/E 是已复核后的证据边界，不是未处理待办；后续 v3 正文必须按本清单删除、降级或补证。",
        "- 完整逐行证据在 `all_framework_entry_source_reaudit.csv`、`wrong_option_source_reaudit.csv`、`suite_inventory_reaudit.csv`。",
        "",
        "## 总量",
        "",
    ]
    for key in ["A", "B", "C", "D", "E"]:
        lines.append(f"- 框架 {key}: {framework_grade.get(key, 0)}")
    lines.append(f"- 框架 D/E 条目合计: {len(framework_de)}")
    lines.append(f"- 框架 B 边界条目: {len(framework_b)}")
    lines.append(f"- 框架 A 但触发词未在文本中直接命中: {len(framework_a_chain)}")
    lines.append(f"- 错肢库 E 来源行: {sum(v for k, v in wrong_status.items() if k.startswith('E_'))}")
    lines.append(f"- 需改写闭环口径的题源清单行: {len(suite_boundary_rows)}")

    lines.extend(["", "## 框架 D/E 条目完整清单", ""])
    lines.extend(
        md_table(
            framework_de,
            [
                "audit_id",
                "final_grade",
                "final_status",
                "recommended_action",
                "source",
                "support_note",
                "support_path",
            ],
            limit=None,
        )
    )

    lines.extend(["", "## 框架 B 边界分组", ""])
    b_group = Counter((row["year"], row["district"], row["stage"]) for row in framework_b)
    b_rows = [
        {
            "year": year,
            "district": district,
            "stage": stage,
            "B_angle_or_scoring_source": str(count),
            "boundary": "keep-as-angle-list-or-organizer-chain",
        }
        for (year, district, stage), count in sorted(b_group.items())
    ]
    lines.extend(md_table(b_rows, ["year", "district", "stage", "B_angle_or_scoring_source", "boundary"], limit=None))

    lines.extend(["", "## 框架 A 级链条需人工复看分组", ""])
    a_group = Counter((row["year"], row["district"], row["stage"]) for row in framework_a_chain)
    a_rows = [
        {
            "year": year,
            "district": district,
            "stage": stage,
            "A_scoring_source_trigger_not_text_matched": str(count),
            "action": "keep-source-but-chain-needs-human-check",
        }
        for (year, district, stage), count in sorted(a_group.items())
    ]
    lines.extend(md_table(a_rows, ["year", "district", "stage", "A_scoring_source_trigger_not_text_matched", "action"], limit=None))

    lines.extend(["", "## 错肢库 E 来源行分组", ""])
    lines.extend(md_table(wrong_e_rows, ["year", "district", "stage", "status_counts", "recommended_action"], limit=None))

    lines.extend(["", "## 题源清单闭环口径修正", ""])
    lines.extend(
        md_table(
            suite_boundary_rows,
            [
                "year",
                "district",
                "stage",
                "old_closed_state",
                "v3_suite_verdict",
                "recommended_action",
                "framework_statuses",
                "wrong_option_statuses",
            ],
            limit=None,
        )
    )

    lines.extend(
        [
            "",
            "## Governor 结论",
            "",
            "- 全来源复核已经覆盖旧框架条目、错肢库来源行和旧题源清单行。",
            "- 仍为 E 的行不得进入正式 v3 正文；仍为 D 的行只能保留 reference-only/方向边界；B 行必须改写为角度清单或整理链。",
            "- 本清单不构成 `TASK_COMPLETE`，只能作为下一步 v3 修订草案的输入。",
        ]
    )
    (OUT_DIR / "全来源复核_边界与缺口清单.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    bundles = bundle_index()
    framework_entries = read_csv(FRAMEWORK_INVENTORY)
    framework_reviewed = review_framework_entries(framework_entries)
    source_key_rows = aggregate_source_keys(framework_reviewed)
    wrong_rows = review_wrong_option_sources(parse_wrong_option_rows(), bundles)
    suite_rows = review_suite_inventory(parse_source_inventory_rows(), framework_reviewed, wrong_rows)

    write_csv(
        OUT_DIR / "all_framework_entry_source_reaudit.csv",
        framework_reviewed,
        [
            "audit_id",
            "line",
            "entry_type",
            "section",
            "source",
            "year",
            "district",
            "stage",
            "question",
            "question_nature",
            "evidence_grade_initial",
            "final_grade",
            "final_status",
            "recommended_action",
            "support_path",
            "support_note",
            "support_section_grade",
            "support_trigger_hits",
            "support_source_hint_hits",
            "choice_answer_key_state",
            "bundle_path",
            "bundle_state",
            "local_raw_path",
            "local_raw_state",
            "local_raw_chars",
            "material",
            "trigger",
            "logic",
        ],
    )
    write_csv(
        OUT_DIR / "all_framework_source_key_reaudit.csv",
        source_key_rows,
        [
            "source_key",
            "year",
            "district",
            "stage",
            "source",
            "entry_count",
            "final_grades",
            "final_statuses",
            "support_paths",
            "source_review_result",
        ],
    )
    write_csv(
        OUT_DIR / "wrong_option_source_reaudit.csv",
        wrong_rows,
        [
            "audit_id",
            "line",
            "batch",
            "source",
            "year",
            "district",
            "stage",
            "question",
            "question_nature",
            "module",
            "wrong_statement",
            "error_type",
            "bundle_path",
            "bundle_state",
            "choice_answer_key_state",
            "final_status",
            "recommended_action",
            "support_path",
        ],
    )
    write_csv(
        OUT_DIR / "suite_inventory_reaudit.csv",
        suite_rows,
        [
            "line",
            "year",
            "district",
            "stage",
            "question_range",
            "question_type",
            "file_source",
            "answer_key_state_old",
            "rubric_state_old",
            "old_closed_state",
            "v3_suite_verdict",
            "recommended_action",
            "framework_entry_count",
            "wrong_option_entry_count",
            "framework_statuses",
            "wrong_option_statuses",
            "old_notes",
        ],
    )
    write_summary(framework_reviewed, wrong_rows, source_key_rows, suite_rows)
    write_boundary_report(framework_reviewed, wrong_rows, suite_rows)


if __name__ == "__main__":
    main()
