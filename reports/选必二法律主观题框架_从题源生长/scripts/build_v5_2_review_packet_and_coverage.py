#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import os
import shutil
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now().strftime("%Y%m%d")
STAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


REFERENCE_ONLY = {"CC0040_2024_海淀_一模_19", "CC0162_2025_海淀_一模_18", "CC0311_2026_海淀_二模_18_2", "CC0353_2026_西城_期末_17"}
LOW_FREQ = {"CC0011_2024_丰台_二模_17", "CC0254_2026_丰台_二模_18", "CC0332_2026_石景山_二模_19", "CC0340_2026_西城_一模_17", "RECOVER_2024_东城_一模_19"}
BOUNDARY_OPEN = {"CC0276_2026_房山_二模_17", "RECOVER_2026_西城_二模_18_3", "CC0380_2026_顺义_二模_18_2", "RECOVER_2026_西城_二模_18_2"}
FORCE_SOURCE_CHECK = {"CC0251_2026_丰台_一模_20", "CC0283_2026_朝阳_一模_18"}
CORE_REVIEW_DOWNGRADE = {
    "CC0137_2025_昌平_二模_20",
    "CC0119_2025_丰台_期末_19",
    "CC0289_2026_朝阳_二模_18",
    "CC0061_2024_西城_一模_18",
}
LOGIC_BOUNDARY = {"CC0364_2026_通州_期末_19_1"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def clean(s: str | None) -> str:
    return " ".join((s or "").replace("\n", " ").split())


def latest(pattern: str) -> Path:
    matches = sorted(ROOT.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    if not matches:
        raise FileNotFoundError(pattern)
    return matches[0]


questions = read_csv(ROOT / "04_merge_audit/merged_subjective_law_questions.csv")
pressure = {r["question_id"]: r for r in read_csv(ROOT / "10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv")}
STRICT_RUNS = latest(f"12_final_baodian/question_by_question_framework_runs_v5_2_*strict_core_{TODAY}.csv")
STRICT_MD = latest(f"12_final_baodian/选必二法律主观题满分宝典_v5_2_*严格核心扩展_{TODAY}.md")
STRICT_SENTENCE_BANK = latest(f"12_final_baodian/full_score_sentence_bank_v5_2_*strict_core_{TODAY}.csv")
strict_rows = {r["question_id"]: r for r in read_csv(STRICT_RUNS)}
source_queue = {r["question_id"]: r for r in read_csv(ROOT / "10_framework_validation/v5_ask_text_source_check_queue_20260521.csv")}


def category(qid: str, q: dict[str, str]) -> tuple[str, str]:
    if qid in REFERENCE_ONLY or q.get("evidence_level") == "reference_only":
        return "reference_only_locked", "普通参考答案/教师答案，不支撑核心"
    if qid in BOUNDARY_OPEN:
        return "boundary_open_container", "综合/宏观治理/边界题，只进开放容器"
    if qid in FORCE_SOURCE_CHECK:
        return "source_check_pending", "被 V5.2 强制要求回源清洗"
    if qid in CORE_REVIEW_DOWNGRADE:
        return "source_check_pending", "Claude Opus V5.2 复核要求移出核心并回源：材料/答案/细则或生成答案存在错位/元信息污染风险"
    if qid in strict_rows:
        return "strict_core", "formal core sample generated in V5.2 after Claude V5.2 downgrades"
    if qid in source_queue:
        return "source_check_pending", source_queue[qid].get("risk_type", "ask/material source check")
    if qid in LOGIC_BOUNDARY or "逻辑与思维" in (q.get("ask_text") or ""):
        return "excluded_logic_boundary", "设问指向《逻辑与思维》，不进入选必二法律核心"
    if qid in LOW_FREQ:
        return "low_frequency_container", "formal 但低频，不作为核心动作卡支撑"
    old = pressure.get(qid, {}).get("pass_status", "")
    if old:
        return "non_core_pending_review", f"old_status={old}; V5.2 未纳入核心"
    return "unclassified_pending_review", "needs manual review"


def build_coverage() -> list[dict[str, str]]:
    rows = []
    for q in questions:
        qid = q["question_id"]
        cat, reason = category(qid, q)
        core = strict_rows.get(qid, {})
        rows.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "evidence_level": q.get("evidence_level", ""),
                "v5_2_category": cat,
                "reason": reason,
                "framework_entry_nodes": core.get("framework_entry_nodes", ""),
                "old_pass_status": pressure.get(qid, {}).get("pass_status", ""),
                "ask_text": clean(q.get("ask_text")),
            }
        )
    return rows


def main() -> None:
    coverage = build_coverage()
    write_csv(
        ROOT / f"10_framework_validation/v5_2_65_question_coverage_matrix_{TODAY}.csv",
        coverage,
        ["question_id", "year", "district", "exam_stage", "question_no", "evidence_level", "v5_2_category", "reason", "framework_entry_nodes", "old_pass_status", "ask_text"],
    )
    counts = Counter(r["v5_2_category"] for r in coverage)
    report = f"""# V5.2 65 题覆盖矩阵报告

生成时间：{STAMP}

## 分类统计

{dict(counts)}

## 裁定

V5.2 目前只有 `strict_core` 题进入逐题样章。其他题保持标签化进入后续宝典附录或待回源队列，不能偷偷包装成核心满分样章。

## 文件

- `10_framework_validation/v5_2_65_question_coverage_matrix_{TODAY}.csv`
"""
    (ROOT / f"10_framework_validation/v5_2_65_question_coverage_matrix_{TODAY}.md").write_text(report, encoding="utf-8")

    packet = ROOT / f"05_reasoner_packets/v5_2_gptpro_claude_review_packet_{TODAY}"
    if packet.exists():
        shutil.rmtree(packet)
    (packet / "00_prompt").mkdir(parents=True)
    (packet / "01_framework").mkdir()
    (packet / "02_pressure_tests").mkdir()
    (packet / "03_core_expansion").mkdir()
    (packet / "04_coverage").mkdir()
    (packet / "05_evidence_baseline").mkdir()

    prompt = f"""# Prompt for GPTPro and Claude Opus: V5.2 选必二法律主观题框架复核

你是选必二《法律与生活》主观题框架复核者。请判断 V5.2 是否已经从“能启动”进化到“学生看完能接近满分”。

请只基于本包文件，不使用外部先验框架。

## 输入重点

1. `framework_v5_2_student_one_page_20260521.md`：学生速用稿。
2. `codex_grading_report_v5_1_20260521.md` 与 `codex_grading_report_v5_2_20260521.md`：同一干净题面前后压测。
3. `{STRICT_MD.name}`：{len(strict_rows)} 道严格核心逐题运行。
4. `v5_2_65_question_coverage_matrix_20260521.csv`：65 题全覆盖标签。

## 复核问题

1. V5.2 的六张动作卡是否足够清楚、可启动、可迁移？
2. V5.2 必踩硬词句库是否解决了 V5.1 零基础压测失分点？
3. {len(strict_rows)} 道严格核心样章是否像学生能照着学的宝典，而不是审计报告？
4. 4 道从旧 35 中降级的题是否降级合理？
5. 哪些题/节点仍然会让学生看完不能满分？
6. 请给出必须修改的条目，要求具体到文件、题号、动作卡、应该改成什么。

## 输出格式

请输出：

- 总裁定：PASS / CONDITIONAL_PASS / FAIL
- 必修补问题清单
- 可保留优点
- 31 核心扩展是否可进入最终宝典正文
- 65 覆盖矩阵中哪些标签需要调整
- 给 Codex 的下一步执行指令
"""
    (packet / "00_prompt/PROMPT_FOR_GPTPRO_AND_CLAUDE_V5_2_REVIEW_20260521.md").write_text(prompt, encoding="utf-8")

    copies = [
        (ROOT / "11_final_framework/framework_v5_2_student_one_page_20260521.md", packet / "01_framework/framework_v5_2_student_one_page_20260521.md"),
        (ROOT / "11_final_framework/framework_v5_2_patch_decision_20260521.md", packet / "01_framework/framework_v5_2_patch_decision_20260521.md"),
        (ROOT / "10_framework_validation/zero_baseline_student_pressure_v5_1_20260521/codex_grading_report_v5_1_20260521.md", packet / "02_pressure_tests/codex_grading_report_v5_1_20260521.md"),
        (ROOT / "10_framework_validation/zero_baseline_student_pressure_v5_1_20260521/codex_grading_report_v5_2_20260521.md", packet / "02_pressure_tests/codex_grading_report_v5_2_20260521.md"),
        (ROOT / "10_framework_validation/zero_baseline_student_pressure_v5_1_20260521/codex_agent_zero_baseline_answers_v5_2_20260521.md", packet / "02_pressure_tests/codex_agent_zero_baseline_answers_v5_2_20260521.md"),
        (STRICT_MD, packet / "03_core_expansion/baodian_v5_2_strict_core.md"),
        (STRICT_RUNS, packet / "03_core_expansion/question_by_question_framework_runs_v5_2_strict_core.csv"),
        (STRICT_SENTENCE_BANK, packet / "03_core_expansion/full_score_sentence_bank_v5_2_strict_core.csv"),
        (ROOT / "10_framework_validation/v5_2_65_question_coverage_matrix_20260521.csv", packet / "04_coverage/v5_2_65_question_coverage_matrix_20260521.csv"),
        (ROOT / "10_framework_validation/v5_2_strict_core_expansion_report_20260521.md", packet / "04_coverage/v5_2_strict_core_expansion_report_20260521.md"),
        (ROOT / "04_merge_audit/merged_subjective_law_questions.csv", packet / "05_evidence_baseline/merged_subjective_law_questions.csv"),
        (ROOT / "04_merge_audit/merged_rubric_atoms_subjective.csv", packet / "05_evidence_baseline/merged_rubric_atoms_subjective.csv"),
    ]
    for src, dst in copies:
        shutil.copy2(src, dst)

    zip_path = packet.with_suffix(".zip")
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in packet.rglob("*"):
            if path.is_file():
                z.write(path, path.relative_to(packet.parent))

    if os.environ.get("V52_REVIEW_SKIP_CONTROL") == "1":
        print(zip_path)
        print(dict(counts))
        print("skip_control=1")
        return

    note = f"""

## STEP_82_V5_2_REVIEW_PACKET_AND_65_COVERAGE ({STAMP})

- 已生成 V5.2 65 题覆盖矩阵：`10_framework_validation/v5_2_65_question_coverage_matrix_{TODAY}.csv`。
- 已生成 GPTPro/Claude 复核包：`05_reasoner_packets/v5_2_gptpro_claude_review_packet_{TODAY}.zip`。
- 当前允许：发送真实 GPTPro/Claude 复核。
- 当前不允许：最终定稿或 DOCX/PDF 交付。
"""
    for rel in ["PROGRESS.md", "governor_board.md", "TODO.md"]:
        p = ROOT / rel
        p.write_text(p.read_text(encoding="utf-8") + note, encoding="utf-8")

    print(zip_path)
    print(dict(counts))


if __name__ == "__main__":
    main()
