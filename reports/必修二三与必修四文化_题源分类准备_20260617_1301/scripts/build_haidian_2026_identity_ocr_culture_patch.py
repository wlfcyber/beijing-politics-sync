#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import shutil
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "00_control" / "FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "haidian_2026_identity_ocr_culture_patched_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "HAIDIAN_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "haidian_2026_identity_ocr_culture_patch_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "haidian_2026_identity_ocr_culture_patch_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "haidian_2026_identity_ocr_culture_patch_report.md"

SOURCE_INVENTORY = RUN_DIR / "01_source_inventory" / "source_inventory.csv"
SOURCE_LEDGER = RUN_DIR / "00_control" / "SOURCE_LEDGER.csv"
CACHE_MANIFEST = RUN_DIR / "02_text_cache" / "cache_manifest.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
TEXT_DIR = RUN_DIR / "02_text_cache" / "texts"

OLD_SUITE = "2026_海淀_期末"
MIDTERM_SUITE = "2026_海淀_期中"
FINAL_SUITE = "2026_海淀_期末"

MIDTERM_NEEDLE = "/2026海淀期中/"
FINAL_NEEDLE = "/2026海淀期末/"
FINAL_PAPER = "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期末/试卷/试卷.pdf"
FINAL_RUBRIC = "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期末/细则/细则.pdf"
FINAL_OCR = RUN_DIR / "02_text_cache" / "ocr_cache" / "2026_海淀_期末_试卷" / "试卷.ocr.txt"
FINAL_TEXT = RUN_DIR / "02_text_cache" / "texts" / "ac3124113aec7062.txt"
FINAL_TEXT_BACKUP = RUN_DIR / "02_text_cache" / "texts" / "ac3124113aec7062.pre_haidian_2026_partial_backup.txt"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


def load_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 1400) -> str:
    return re.sub(r"\s+", " ", text or "").strip()[:limit]


def split_evidence_source(value: str, keep_needle: str) -> str:
    parts = [part.strip() for part in (value or "").split("|")]
    kept = [part for part in parts if keep_needle in part or not (MIDTERM_NEEDLE in part or FINAL_NEEDLE in part)]
    return " | ".join(dict.fromkeys(part for part in kept if part))


def patch_suite_rows(path: Path, *, write_back: bool) -> tuple[int, int]:
    rows, fields = load_csv(path)
    changed = 0
    final_changed = 0
    for row in rows:
        file_path = row.get("file_path", "")
        if row.get("suite_id") == OLD_SUITE and MIDTERM_NEEDLE in file_path:
            row["suite_id"] = MIDTERM_SUITE
            row["stage"] = "期中"
            changed += 1
        elif row.get("suite_id") == OLD_SUITE and FINAL_NEEDLE in file_path:
            row["suite_id"] = FINAL_SUITE
            row["stage"] = "期末"
            final_changed += 1
    if write_back:
        write_csv(path, rows, fields)
    return changed, final_changed


def patch_cache_manifest() -> tuple[int, int, int]:
    rows, fields = load_csv(CACHE_MANIFEST)
    midterm_changed = 0
    final_changed = 0
    text_repaired = 0
    for row in rows:
        file_path = row.get("file_path", "")
        if row.get("suite_id") == OLD_SUITE and MIDTERM_NEEDLE in file_path:
            row["suite_id"] = MIDTERM_SUITE
            row["stage"] = "期中"
            midterm_changed += 1
        elif row.get("suite_id") == OLD_SUITE and FINAL_NEEDLE in file_path:
            row["suite_id"] = FINAL_SUITE
            row["stage"] = "期末"
            final_changed += 1
            if file_path == FINAL_PAPER and FINAL_OCR.exists():
                if FINAL_TEXT.exists() and not FINAL_TEXT_BACKUP.exists():
                    shutil.copy2(FINAL_TEXT, FINAL_TEXT_BACKUP)
                shutil.copy2(FINAL_OCR, FINAL_TEXT)
                row["extraction_status"] = "raw-extracted"
                row["run_text_path"] = str(FINAL_TEXT)
                row["source_text_path"] = str(FINAL_OCR)
                row["char_count"] = str(FINAL_TEXT.stat().st_size)
                old_error = row.get("error", "")
                note = "repaired_full_ocr_for_haidian_2026_final_identity_patch"
                row["error"] = note if not old_error else f"{old_error}; {note}"
                text_repaired += 1
    seen_sha = {row.get("sha256", "") for row in rows}
    source_rows, _ = load_csv(SOURCE_INVENTORY)
    for source in source_rows:
        if source.get("suite_id") != FINAL_SUITE or source.get("status") == "duplicate-or-drift":
            continue
        if source.get("sha256", "") in seen_sha:
            continue
        if source.get("source_type") == "paper":
            run_text = FINAL_TEXT
            source_text = FINAL_OCR
            extraction_status = "raw-extracted"
            cache_hit = "no"
            error = "added_missing_cache_manifest_row; repaired_full_ocr_for_haidian_2026_final_identity_patch"
        elif source.get("source_type") == "rubric":
            run_text = TEXT_DIR / f"{source['sha256'][:16]}.txt"
            source_text = Path(source["file_path"])
            extraction_status = "raw-extracted" if run_text.exists() else "empty-or-unsupported"
            cache_hit = "no"
            error = "added_missing_cache_manifest_row_for_haidian_2026_final_rubric"
        else:
            continue
        rows.append(
            {
                "suite_id": source["suite_id"],
                "year": source["year"],
                "district": source["district"],
                "stage": source["stage"],
                "source_type": source["source_type"],
                "file_path": source["file_path"],
                "sha256": source["sha256"],
                "cache_hit": cache_hit,
                "extraction_status": extraction_status,
                "char_count": str(run_text.stat().st_size) if run_text.exists() else "0",
                "run_text_path": str(run_text) if run_text.exists() else "",
                "source_text_path": str(source_text),
                "error": error,
            }
        )
        seen_sha.add(source["sha256"])
        final_changed += 1
    write_csv(CACHE_MANIFEST, rows, fields)
    return midterm_changed, final_changed, text_repaired


def status_for(module: str) -> str:
    return "included" if module in TARGET_MODULES else "module-boundary-excluded"


def qtype_for(question: str) -> str:
    stem = question.split("#", 1)[0].split("(", 1)[0]
    return "objective" if stem.isdigit() and int(stem) <= 15 else "subjective"


def base_row(fields: list[str], *, suite_id: str, question: str, module: str, granularity: str = "question", parent: str = "") -> dict[str, str]:
    row = {field: "" for field in fields}
    row.update(
        {
            "suite_id": suite_id,
            "year": "2026",
            "district": "海淀",
            "stage": "期中" if suite_id == MIDTERM_SUITE else "期末",
            "question": question,
            "parent_question": parent,
            "row_granularity": granularity,
            "book_module": module,
            "question_type": qtype_for(parent or question),
            "evidence_source": str(FINAL_OCR) if suite_id == FINAL_SUITE else "",
            "source_types": "paper_ocr|rubric|answer_key" if suite_id == FINAL_SUITE else "",
            "status": status_for(module),
            "artifact_location": str(OUT_AUDIT.relative_to(RUN_DIR)),
            "next_action": "future_baodian_intake" if module in TARGET_MODULES else "exclude_from_three_target_lines",
            "integration_status": "haidian_2026_identity_ocr_culture_patch",
        }
    )
    return row


FINAL_ROWS = [
    ("1", "B4_PHILOSOPHY_EXCLUDED", "HAIDIAN_2026_FINAL_Q1_B4P_GNOMON_TIME", "答案B,圭表,测量智慧,社会实践", "正确项①④分别指向古代测量智慧与社会实践/历史条件，主知识落点为哲学与实践，不单列文化组件。"),
    ("2", "B4_PHILOSOPHY_EXCLUDED", "HAIDIAN_2026_FINAL_Q2_PARENT_AFTER_B3", "答案A,全面观点,为人民服务政治本色", "正确项①为全面观点，③为党员干部政治本色；B3 目标点另抽组件，父题余项按哲学边界关闭。"),
    ("3", "B4_PHILOSOPHY_EXCLUDED", "HAIDIAN_2026_FINAL_Q3_AI_TOOL_RECOGNITION", "答案A,研究工具,表演规律认识", "正确项强调人工智能作为研究工具深化认识，归入哲学/认识论边界。"),
    ("4", "B2_ECONOMICS", "HAIDIAN_2026_FINAL_Q4_HUMANISTIC_ECONOMICS", "答案C,人民福祉,文化繁荣与经济发展", "新时代人文经济学正确项含以人民福祉为出发点、文化繁荣与经济发展统一；主链抽入 B2，文化点另抽组件。"),
    ("5", "B4_CULTURE", "HAIDIAN_2026_FINAL_Q5_CULTURE_FAIR", "答案D,文化交流互鉴,中华文明传播力影响力,文化自信", "文化产业博览交易会正确项③④明确文化交流互鉴、中华文明传播和文化自信，整题进入 B4_CULTURE。"),
    ("6", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q6_TRADE_SECRET", "答案C,商业秘密,侵权责任", "商业秘密侵权题，属于《法律与生活》。"),
    ("7", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q7_TORT_TRAFFIC", "答案D,注意义务,赔礼道歉,赔偿损失", "交通侵权责任题，属于《法律与生活》。"),
    ("8", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q8_MARRIAGE_REGISTRATION", "答案A,婚姻登记条例,个人信息", "婚姻登记条例与婚姻家庭服务题，属于《法律与生活》。"),
    ("9", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q9_LABOR_RELATION", "答案D,劳动合同,劳动争议", "劳动关系与劳动争议题，属于《法律与生活》。"),
    ("10", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q10_RETURN_POLICY", "答案B,诚信原则,消费者权益", "消费者权益与市场规则题，属于《法律与生活》。"),
    ("11", "XB3_EXCLUDED", "HAIDIAN_2026_FINAL_Q11_LOGIC_ATTENTION", "答案B,谓项周延,类比推理", "概念、判断、推理题，属于《逻辑与思维》。"),
    ("12", "XB3_EXCLUDED", "HAIDIAN_2026_FINAL_Q12_SYLLOGISM", "答案C,三段论", "三段论推理题，属于《逻辑与思维》。"),
    ("13", "XB3_EXCLUDED", "HAIDIAN_2026_FINAL_Q13_INDUCTION_METHOD", "答案C,求异法,调查对象", "归纳推理与探究方案题，属于《逻辑与思维》。"),
    ("14", "XB3_EXCLUDED", "HAIDIAN_2026_FINAL_Q14_RESEARCH_CONCLUSION", "答案B,研究结论条件性", "科学思维/归纳结论可靠性题，属于《逻辑与思维》。"),
    ("15", "XB3_EXCLUDED", "HAIDIAN_2026_FINAL_Q15_TRAVEL_PLATFORM", "答案D,公共服务供给,综合思维", "统一旅游预约平台正确项含公共服务与综合思维，XB3 余项为主；B3 不单列，避免把公共服务背景强行当采分点。"),
    ("16", "B4_PHILOSOPHY_EXCLUDED", "HAIDIAN_2026_FINAL_Q16_DIGITAL_NATIVES", "矛盾观点,意识能动作用,实践观点", "设问明确从哲学角度作答，细则为哲学知识，非文化目标线。"),
    ("17", "B4_PHILOSOPHY_EXCLUDED", "HAIDIAN_2026_FINAL_Q17_PARENT_AFTER_CULTURE", "联系观点,价值观,红色文化,民族精神", "第17题《哲学与文化》混合；红色文化、民族精神和中国特色社会主义文化另抽 B4_CULTURE 组件，父题余项按哲学边界关闭。"),
    ("18", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q18_PARENT_XB2_AFTER_COMPONENTS", "法律与生活,住房租赁条例,社会主义核心价值观,政府依法履职", "第18题主体为合同/行政法规法治题；B3 与文化价值点另抽组件，父题余项按法律边界关闭。"),
    ("19", "XB2_EXCLUDED", "HAIDIAN_2026_FINAL_Q19_PARENT_XB2_AFTER_CULTURE", "反不正当竞争法,社会主义核心价值观", "第19题主体为不正当竞争与侵权责任；社会主义核心价值观另抽文化组件，父题余项按法律边界关闭。"),
    ("20", "XB3_EXCLUDED", "HAIDIAN_2026_FINAL_Q20_LOGIC_AND_ADVANCE", "充分条件假言推理,超前思维", "第20题为逻辑推理与超前思维，属于《逻辑与思维》。"),
    ("21", "B4_PHILOSOPHY_EXCLUDED", "HAIDIAN_2026_FINAL_Q21_PARENT_AFTER_B3", "党的领导,以人民为中心,矛盾观点,制度优势", "第21题为综合论述；党的领导和以人民为中心另抽 B3 组件，父题余项按哲学/综合边界关闭。"),
]

FINAL_COMPONENTS = [
    ("2#B3_COMPONENT", "2", "target_component", "B3_POLITICS_RULE_OF_LAW", "HAIDIAN_2026_FINAL_Q2_B3_COMPONENT_PARTY_CADRE", "党员干部,为人民服务,政治本色", "第2题答案A的正确项③明确党员干部坚守为人民服务政治本色，抽入 B3。"),
    ("4#B4_CULTURE_COMPONENT", "4", "culture_component", "B4_CULTURE", "HAIDIAN_2026_FINAL_Q4_B4C_COMPONENT_CULTURE_ECONOMY", "文化繁荣,文化与经济融合,中国式现代化", "第4题正确项③明确文化繁荣与经济发展统一，抽入文化组件。"),
    ("17#B4_CULTURE_COMPONENT", "17", "culture_component", "B4_CULTURE", "HAIDIAN_2026_FINAL_Q17_B4C_COMPONENT_RED_CULTURE", "红色文化,民族精神,发展中国特色社会主义文化,延安精神", "题面写红色文化圈粉年轻人，细则明列弘扬民族精神、发展中国特色社会主义文化；民族精神按文化入账。"),
    ("18#B3_COMPONENT", "18", "target_component", "B3_POLITICS_RULE_OF_LAW", "HAIDIAN_2026_FINAL_Q18_B3_COMPONENT_GOVERNMENT_RULE_OF_LAW", "政府法定职责,依法履职,严格执法,良法善治", "第18(2)问细则明确政府依法履职、严格执法、良法善治，抽入 B3。"),
    ("18#B4_CULTURE_COMPONENT", "18", "culture_component", "B4_CULTURE", "HAIDIAN_2026_FINAL_Q18_B4C_COMPONENT_CORE_VALUES", "社会主义核心价值观,诚信", "第18(2)问细则写到弘扬诚信的社会主义价值观；社会主义核心价值观属于文化成分。"),
    ("19#B4_CULTURE_COMPONENT", "19", "culture_component", "B4_CULTURE", "HAIDIAN_2026_FINAL_Q19_B4C_COMPONENT_CORE_VALUES", "社会主义核心价值观", "第19题细则把不符合社会主义核心价值观作为评价点，抽入文化组件。"),
    ("21#B3_COMPONENT", "21", "target_component", "B3_POLITICS_RULE_OF_LAW", "HAIDIAN_2026_FINAL_Q21_B3_COMPONENT_PARTY_PEOPLE", "党的领导,以人民为中心", "第21题细则明列党的领导、以人民为中心，抽入 B3 组件。"),
]


def add_final_row(out_rows: list[dict[str, str]], audit_rows: list[dict[str, str]], fields: list[str], item: tuple[str, str, str, str, str]) -> None:
    question, module, rule_id, terms, basis = item
    row = base_row(fields, suite_id=FINAL_SUITE, question=question, module=module)
    row["decision_reason"] = json.dumps(
        {"rule_id": rule_id, "matched_terms": terms, "basis": basis, "source": str(OUT_AUDIT.relative_to(RUN_DIR))},
        ensure_ascii=False,
    )
    out_rows.append(row)
    audit_rows.append(
        {
            "operation": "rebuild_2026_haidian_final_row",
            "suite_id": FINAL_SUITE,
            "question": question,
            "parent_question": "",
            "row_granularity": "question",
            "book_module": module,
            "status": row["status"],
            "rule_id": rule_id,
            "matched_terms": terms,
            "basis": basis,
            "evidence_source": str(FINAL_OCR),
            "source_types": row["source_types"],
        }
    )


def add_component(out_rows: list[dict[str, str]], audit_rows: list[dict[str, str]], fields: list[str], item: tuple[str, str, str, str, str, str, str]) -> None:
    question, parent, granularity, module, rule_id, terms, basis = item
    row = base_row(fields, suite_id=FINAL_SUITE, question=question, parent=parent, granularity=granularity, module=module)
    row["next_action"] = "future_baodian_intake_target_component" if module != "B4_CULTURE" else "future_baodian_intake_culture_component"
    row["decision_reason"] = json.dumps(
        {
            "rule_id": rule_id,
            "matched_terms": terms,
            "basis": basis,
            "source": str(OUT_AUDIT.relative_to(RUN_DIR)),
            "user_rule": "题目和细则中的文化部分必须抽离；民族精神、社会主义核心价值观属于文化。",
        },
        ensure_ascii=False,
    )
    out_rows.append(row)
    audit_rows.append(
        {
            "operation": "add_2026_haidian_final_component",
            "suite_id": FINAL_SUITE,
            "question": question,
            "parent_question": parent,
            "row_granularity": granularity,
            "book_module": module,
            "status": "included",
            "rule_id": rule_id,
            "matched_terms": terms,
            "basis": basis,
            "evidence_source": str(FINAL_OCR),
            "source_types": row["source_types"],
        }
    )


def main() -> int:
    if not FINAL_OCR.exists():
        raise SystemExit(f"missing OCR file: {FINAL_OCR}")

    if FINAL_TEXT.exists() and FINAL_TEXT.stat().st_size < FINAL_OCR.stat().st_size:
        if not FINAL_TEXT_BACKUP.exists():
            shutil.copy2(FINAL_TEXT, FINAL_TEXT_BACKUP)
        shutil.copy2(FINAL_OCR, FINAL_TEXT)

    source_mid, source_final = patch_suite_rows(SOURCE_INVENTORY, write_back=True)
    ledger_mid, ledger_final = patch_suite_rows(SOURCE_LEDGER, write_back=True)
    cand_mid, cand_final = patch_suite_rows(QUESTION_CANDIDATES, write_back=True)
    cache_mid, cache_final, cache_text_repaired = patch_cache_manifest()

    rows, fields = load_csv(IN_MATRIX)
    contaminated = [row for row in rows if row.get("suite_id") == OLD_SUITE]
    out_rows = [row for row in rows if row.get("suite_id") != OLD_SUITE]
    audit_rows: list[dict[str, str]] = []

    for old in contaminated:
        clone = dict(old)
        clone["suite_id"] = MIDTERM_SUITE
        clone["stage"] = "期中"
        clone["evidence_source"] = split_evidence_source(old.get("evidence_source", ""), MIDTERM_NEEDLE)
        clone["integration_status"] = "haidian_2026_identity_ocr_culture_patch_midterm_split"
        reason = {
            "rule_id": "HAIDIAN_2026_MIDTERM_SPLIT_FROM_CONTAMINATED_SUITE",
            "basis": "原 2026_海淀_期末 行混入海淀期中文件；本补丁将期中文件行拆回 2026_海淀_期中，保留原目标/边界判定作为期中接手账本。",
            "prior_suite_id": OLD_SUITE,
            "prior_decision_reason": old.get("decision_reason", ""),
        }
        clone["decision_reason"] = json.dumps(reason, ensure_ascii=False)
        out_rows.append(clone)
        audit_rows.append(
            {
                "operation": "split_midterm_row_from_contaminated_suite",
                "suite_id": MIDTERM_SUITE,
                "question": clone.get("question", ""),
                "parent_question": clone.get("parent_question", ""),
                "row_granularity": clone.get("row_granularity", ""),
                "book_module": clone.get("book_module", ""),
                "status": clone.get("status", ""),
                "rule_id": "HAIDIAN_2026_MIDTERM_SPLIT_FROM_CONTAMINATED_SUITE",
                "matched_terms": "",
                "basis": "海淀期中源文件从错误的 2026_海淀_期末 suite_id 拆回 2026_海淀_期中。",
                "evidence_source": clone.get("evidence_source", ""),
                "source_types": clone.get("source_types", ""),
            }
        )

    for item in FINAL_ROWS:
        add_final_row(out_rows, audit_rows, fields, item)
    for item in FINAL_COMPONENTS:
        add_component(out_rows, audit_rows, fields, item)

    dupes = [key for key, count in Counter((row["suite_id"], row["question"]) for row in out_rows).items() if count > 1]
    if dupes:
        raise SystemExit(f"duplicate keys after patch: {dupes[:20]}")

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(RUN_DIR / "00_control" / "COVERAGE_MATRIX.csv", out_rows, fields)
    write_csv(RUN_DIR / "04_module_classification" / "module_classification_matrix.csv", out_rows, fields)

    audit_fields = [
        "operation",
        "suite_id",
        "question",
        "parent_question",
        "row_granularity",
        "book_module",
        "status",
        "rule_id",
        "matched_terms",
        "basis",
        "evidence_source",
        "source_types",
    ]
    write_csv(OUT_AUDIT, audit_rows, audit_fields)
    write_csv(OUT_BLOCKED, [row for row in out_rows if row.get("status") == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    suite_counts = Counter(row["suite_id"] for row in out_rows if row["suite_id"] in {MIDTERM_SUITE, FINAL_SUITE})

    report = f"""# 2026 海淀期中/期末身份与 OCR 文化补丁报告

## Scope

- removed contaminated `2026_海淀_期末` live rows: {len(contaminated)}
- rebuilt `2026_海淀_期中` rows: {suite_counts[MIDTERM_SUITE]}
- rebuilt `2026_海淀_期末` rows: {suite_counts[FINAL_SUITE]}
- added 2026 海淀期末 culture/target components: {len(FINAL_COMPONENTS)}
- full OCR text for 2026 海淀期末 paper: `{FINAL_OCR.relative_to(RUN_DIR)}`
- canonical text overwritten from partial cache: {cache_text_repaired}

## Source Identity Repairs

- `source_inventory.csv` midterm/final rows changed: {source_mid}/{source_final}
- `SOURCE_LEDGER.csv` midterm/final rows changed: {ledger_mid}/{ledger_final}
- `question_candidates.csv` midterm/final rows changed: {cand_mid}/{cand_final}
- `cache_manifest.csv` midterm/final rows changed: {cache_mid}/{cache_final}

## Matrix Counts

- rows: {len(out_rows)}
- status counts: {dict(status_counts)}
- included module counts: {dict(included_counts)}
- row granularity counts: {dict(granularity_counts)}
- blocked rows: {status_counts.get('blocked', 0)}
- duplicate `(suite_id, question)` keys: 0

## User Rule Applied

- 海淀期末第 17 题题面与细则中的红色文化、民族精神、发展中国特色社会主义文化抽为 B4_CULTURE 组件。
- 海淀期末第 18、19 题细则中的社会主义核心价值观/诚信价值点抽为 B4_CULTURE 组件。
- 父题的法律、哲学、选必三等余项保留边界排除，不用组件行冒充整题归属。

## Deliverables

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
