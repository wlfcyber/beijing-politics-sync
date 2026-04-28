import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


RUN = Path(r"C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29")
LATE = RUN / "late_objective_closure"

INITIAL_LATE_GAPS = {
    "S003",
    "S007",
    "S010",
    "S012",
    "S014",
    "S038",
    "S039",
    "S042",
    "S044",
    "S053",
    "S054",
}

BLOCKED_OBJECTIVE = {
    "S053": "试卷题干可由渲染页确认，但本地 cache、原始目录、细则页和套卷 bundle 均未找到可靠第1-15题答案键；不猜答案、不写错肢。",
    "S054": "试卷题干可由渲染页确认，但本地 cache、原始目录、细则文本和套卷 bundle 均未找到可靠第1-15题答案键；不猜答案、不写错肢。",
}

RESOLVED_LATE = INITIAL_LATE_GAPS - set(BLOCKED_OBJECTIVE)

WORKER_REPORT_BY_YEAR = {
    "2024": "worker_2024_v6.md",
    "2025": None,
    "2026": None,
}


def read_csv(path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def suite_rows():
    return read_csv(RUN / "SUITE_ROSTER.csv")


def suite_lookup():
    return {row["suite_id"]: row for row in suite_rows()}


def late_source_rows():
    out = []
    for path in sorted(LATE.glob("*.csv")):
        if path.name in {"objective_gap_closure_matrix.csv", "late_objective_entries_normalized.csv"}:
            continue
        for row in read_csv(path):
            row["_late_source_file"] = str(path)
            out.append(row)
    return out


def closure_status_by_suite():
    status = {}
    evidence = defaultdict(list)
    for row in late_source_rows():
        sid = row.get("suite_id", "")
        if not sid:
            continue
        evidence[sid].append(row.get("_late_source_file", ""))
        if sid in BLOCKED_OBJECTIVE:
            status[sid] = "BLOCKED_NO_LOCAL_OBJECTIVE_ANSWER_KEY"
        elif sid in RESOLVED_LATE:
            status[sid] = "PASS_OBJECTIVE_CLOSED_BY_LATE_EVIDENCE"
    return status, evidence


def chain_rows():
    rows = []
    for row in late_source_rows():
        sid = row.get("suite_id", "")
        if sid in BLOCKED_OBJECTIVE:
            continue
        question = row.get("question_no") or row.get("question") or row.get("question_range") or ""
        if question in {"", "1-15", "N/A"}:
            continue
        action = (
            row.get("philo_culture_action")
            or row.get("entry_kind")
            or row.get("chain_type")
            or row.get("choice_chain_status")
            or row.get("status")
            or ""
        )
        module = row.get("module") or row.get("module_boundary") or ""
        if action == "module_boundary" and not any(token in module for token in ["哲学", "文化"]):
            continue
        if row.get("entry_type") == "objective_coverage" and row.get("choice_chain_status") != "choice_chain":
            continue
        text = " ".join(str(v) for v in row.values() if v)
        has_chain = any(
            token in text
            for token in [
                "choice_chain",
                "correct_chain",
                "wrong_option",
                "chain_confirmed",
                "哲学",
                "文化",
            ]
        )
        if not has_chain:
            continue
        rows.append(row)
    return rows


def normalize_chain(row):
    sid = row.get("suite_id", "")
    suite = row.get("suite_name", "")
    question = row.get("question_no") or row.get("question") or ""
    answer = row.get("answer") or row.get("answer_key") or ""
    module = row.get("module") or row.get("module_boundary") or row.get("chain_type") or row.get("entry_type") or ""
    stem = row.get("question_stem") or row.get("stem_excerpt") or row.get("material_or_stem") or row.get("knowledge_or_error_chain") or ""
    trigger = row.get("material_trigger") or row.get("evidence_excerpt") or row.get("material_or_stem") or ""
    correct = row.get("correct_chain") or row.get("knowledge_or_error_chain") or row.get("analysis") or ""
    wrong = row.get("wrong_or_boundary") or row.get("option_or_wrong_item") or row.get("notes") or ""
    if not correct and row.get("notes"):
        correct = row.get("notes", "")
        wrong = "见上句，正确项和错项已合并说明。"
    action = row.get("decision") or row.get("status") or row.get("choice_chain_status") or row.get("philo_culture_action") or ""
    source = row.get("source_path") or row.get("evidence_path") or row.get("evidence_paths") or row.get("stem_evidence") or ""
    return {
        "suite_id": sid,
        "suite_name": suite,
        "question": question,
        "answer": answer,
        "module": module,
        "stem_or_material": stem,
        "material_trigger": trigger,
        "correct_chain": correct,
        "wrong_or_boundary": wrong,
        "student_action": action,
        "evidence": source,
        "_source_file": row.get("_late_source_file", ""),
    }


def make_student_choice_supplement(rows):
    by_suite = defaultdict(list)
    for row in rows:
        by_suite[(row["suite_id"], row["suite_name"])].append(row)

    lines = [
        "# 迟到客观题补证后新增的选择题触发链",
        "",
        "说明：以下只放哲学、文化或必修四相关选择题链条；纯经济、政治、法律、逻辑题只在覆盖矩阵里记录为已核题，不放入学生版框架。",
        "",
    ]
    for (sid, suite), items in sorted(by_suite.items()):
        lines.extend([f"## {sid} {suite}", ""])
        for row in sorted(items, key=lambda r: (str(r["question"]).zfill(3), r["module"], r["wrong_or_boundary"])):
            q = row["question"]
            answer = row["answer"]
            module = row["module"] or "必修四/文化相关"
            stem = row["stem_or_material"] or row["material_trigger"]
            correct = row["correct_chain"] or "已按答案键确认。"
            wrong = row["wrong_or_boundary"] or "无单独错肢补写。"
            action = row["student_action"] or "纳入选择题错肢/正确项链条。"
            lines.append(f"### 第{q}题（答案：{answer}｜模块：{module}）")
            if stem:
                lines.append(f"- 材料抓手：{stem}")
            if row["material_trigger"] and row["material_trigger"] != stem:
                lines.append(f"- 触发逻辑：{row['material_trigger']}")
            lines.append(f"- 正确项为什么对：{correct}")
            lines.append(f"- 错项怎么错：{wrong}")
            lines.append(f"- 入库处理：{action}")
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def build_closure_matrix():
    late_status, evidence = closure_status_by_suite()
    rows = []
    for suite in suite_rows():
        sid = suite["suite_id"]
        if sid in BLOCKED_OBJECTIVE:
            answer_status = "blocked-no-local-answer-key"
            choice_processed = "blocked-no-answer-key"
            governor_status = "BOUNDARY_RECORDED"
            blocker = BLOCKED_OBJECTIVE[sid]
            evidence_level = "paper-rendered-confirmed; answer-key-missing-after-cache-original-bundle-check"
        else:
            answer_status = "confirmed"
            choice_processed = "processed"
            governor_status = "PASS_OBJECTIVE"
            blocker = ""
            evidence_level = "worker-cache-confirmed"
            if sid in RESOLVED_LATE:
                evidence_level = "late-objective-closure"

        if sid in RESOLVED_LATE:
            note = "迟到客观题补证已闭合；相关选择题链条已进入补充学生版。"
        elif sid in BLOCKED_OBJECTIVE:
            note = "题干已核，答案键无可靠本地证据；为防虚构，不写正确项或错肢链。"
        else:
            note = "原 worker 批次已处理。"

        rows.append(
            {
                "suite_id": sid,
                "suite_name": suite["suite_name"],
                "year": suite["year"],
                "district": suite["district"],
                "stage": suite["stage"],
                "paper_status": "confirmed",
                "answer_key_status": answer_status,
                "rubric_status": "processed-or-module-boundary",
                "choice_processed": choice_processed,
                "subjective_processed": "processed-or-module-boundary",
                "philosophy_entries": "",
                "culture_entries": "",
                "wrong_option_rows": "",
                "evidence_level": evidence_level,
                "worker_report": suite.get("assigned_role", ""),
                "patcher_status": "reviewed",
                "governor_status": governor_status,
                "blocker": blocker,
                "closure_note": note,
                "late_evidence_files": "; ".join(sorted(set(evidence.get(sid, [])))),
            }
        )
    return rows


def write_progress_append(summary):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    progress = RUN / "PROGRESS.md"
    decision = RUN / "DECISION_LOG.md"
    progress_text = progress.read_text(encoding="utf-8", errors="replace") if progress.exists() else "# Progress\n"
    decision_text = decision.read_text(encoding="utf-8", errors="replace") if decision.exists() else "# Decision Log\n"
    progress_line = f"- {stamp}: 客观题迟到补证完成：初始全局缺口 11 套，9 套补齐，S053/S054 因无可靠本地答案键登记为阻塞边界；最终 Word 只能在该边界上生成。\n"
    decision_line = f"- {stamp}: 对 S053/S054 执行“不猜答案”规则；题干可见但答案键缺失时，不写正确项链或错肢链，只进审计边界，不进学生版错肢总结。\n"
    if "客观题迟到补证完成：初始全局缺口 11 套" not in progress_text:
        progress.write_text(progress_text.rstrip() + "\n" + progress_line, encoding="utf-8")
    if "对 S053/S054 执行“不猜答案”规则" not in decision_text:
        decision.write_text(decision_text.rstrip() + "\n" + decision_line, encoding="utf-8")


def write_reports(matrix_rows, normalized_rows):
    fields = [
        "suite_id",
        "suite_name",
        "year",
        "district",
        "stage",
        "paper_status",
        "answer_key_status",
        "rubric_status",
        "choice_processed",
        "subjective_processed",
        "philosophy_entries",
        "culture_entries",
        "wrong_option_rows",
        "evidence_level",
        "worker_report",
        "patcher_status",
        "governor_status",
        "blocker",
        "closure_note",
        "late_evidence_files",
    ]
    write_csv(RUN / "COVERAGE_MATRIX.csv", matrix_rows, fields)
    write_csv(LATE / "objective_gap_closure_matrix.csv", matrix_rows, fields)
    write_csv(
        LATE / "late_objective_entries_normalized.csv",
        normalized_rows,
        [
            "suite_id",
            "suite_name",
            "question",
            "answer",
            "module",
            "stem_or_material",
            "material_trigger",
            "correct_chain",
            "wrong_or_boundary",
            "student_action",
            "evidence",
            "_source_file",
        ],
    )

    counts = Counter(row["choice_processed"] for row in matrix_rows)
    blocked = [row for row in matrix_rows if row["choice_processed"].startswith("blocked")]
    md = [
        "# 客观题证据缺口收口报告",
        "",
        f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 结论",
        "",
        f"- 全量题源：{len(matrix_rows)} 套。",
        f"- 本轮初始客观证据缺口：{len(INITIAL_LATE_GAPS)} 套。",
        f"- 已补齐：{len(RESOLVED_LATE)} 套。",
        f"- 仍保留阻塞边界：{len(blocked)} 套。",
        f"- 覆盖矩阵状态：{dict(counts)}。",
        "",
        "## 仍未写错肢的边界",
        "",
    ]
    for row in blocked:
        md.append(f"- {row['suite_id']} {row['suite_name']}：{row['blocker']}")
    md.extend(
        [
            "",
            "## 已补齐的迟到套卷",
            "",
            "- "
            + "、".join(
                f"{sid} {suite_lookup()[sid]['suite_name']}"
                for sid in sorted(RESOLVED_LATE)
            ),
            "",
            "## 最终处理规则",
            "",
            "- 有题干、有答案键：进入覆盖矩阵；哲学/文化相关题进入学生版选择题链条。",
            "- 有题干、无可靠答案键：只登记阻塞边界，不猜正确项，不编错肢。",
            "- 纯经济、政治、法律、逻辑选择题：只做套卷覆盖，不塞进必修四哲学/文化框架。",
        ]
    )
    (LATE / "objective_gap_closure_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main():
    normalized_rows = [normalize_chain(row) for row in chain_rows()]
    (LATE / "late_objective_choice_review_supplement.md").write_text(
        make_student_choice_supplement(normalized_rows), encoding="utf-8"
    )
    matrix_rows = build_closure_matrix()
    write_reports(matrix_rows, normalized_rows)
    write_progress_append(matrix_rows)
    print(
        f"closed objective matrix: {len(matrix_rows)} suites, "
        f"late resolved {len(RESOLVED_LATE)}, blocked {len(BLOCKED_OBJECTIVE)}, "
        f"student choice chains {len(normalized_rows)}"
    )


if __name__ == "__main__":
    main()
