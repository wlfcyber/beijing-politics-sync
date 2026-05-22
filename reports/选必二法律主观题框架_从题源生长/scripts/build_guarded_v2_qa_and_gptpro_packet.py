#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
STAMP = "20260519"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_once(path: Path, marker: str, text: str) -> None:
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in original:
        return
    path.write_text(original.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def policy_for(row: dict[str, str]) -> tuple[str, str, str]:
    evidence = row.get("evidence_level", "")
    patch_type = row.get("patch_type", "")
    qid = row.get("question_id", "")
    if evidence == "reference_only":
        return (
            "reference_only_demo_not_core",
            "May be used only as a weak classroom demo; cannot support a codebook or framework node.",
            "exclude from framework-node evidence; keep as weak demo",
        )
    if qid in {"RECOVER_2026_西城_二模_18_2", "CC0380_2026_顺义_二模_18_2"} or patch_type == "开放容器":
        return (
            "formal_open_container_only_not_core",
            "Formal evidence, but current mechanism is a one-off/open-container case and lacks repeated dual-model support for a core node.",
            "keep as open-container-only pressure case; do not advertise as full-score core closure",
        )
    if patch_type == "formal_open_container_institutional_value":
        return (
            patch_type,
            "Formal evidence, but current support is a singleton/open value mechanism; keep as validation material, not core support.",
            "keep as open-container pressure case during framework synthesis",
        )
    if patch_type == "formal_open_container_family_value_after_split":
        return (
            patch_type,
            "Procedure micro-items and family-value reasoning are split; do not force into private-law core until repeated support appears.",
            "keep as open-container pressure case during framework synthesis",
        )
    if patch_type == "formal_open_container_after_source_patch":
        return (
            patch_type,
            "Formal source patch made the row usable for pressure testing, but it remains low-frequency/open-container support.",
            "keep as open-container pressure case; no new core node without fresh cross-validation",
        )
    return (
        patch_type or "formal_open_container_singleton_or_low_frequency",
        "Keep in open container; it can pressure-test the framework but cannot create an unsupported node.",
        "keep as open-container pressure case during framework synthesis",
    )


def rebuild_partial_policy() -> dict[str, int]:
    pressure_path = ROOT / "10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv"
    rows = read_csv(pressure_path)
    partials = [r for r in rows if r.get("pass_status") == "PARTIAL"]
    policy_rows: list[dict[str, str]] = []
    for row in partials:
        policy, reason, action = policy_for(row)
        policy_rows.append(
            {
                "question_id": row.get("question_id", ""),
                "year": row.get("year", ""),
                "district": row.get("district", ""),
                "exam_stage": row.get("exam_stage", ""),
                "question_no": row.get("question_no", ""),
                "evidence_level": row.get("evidence_level", ""),
                "expansion_status": row.get("expansion_status", ""),
                "framework_entry_node": row.get("framework_entry_node", ""),
                "partial_policy": policy,
                "core_codebook_use": "no",
                "policy_reason": reason,
                "next_action": action,
            }
        )

    out_csv = ROOT / "10_framework_validation/framework_v1_2_partial_policy_20260519.csv"
    write_csv(
        out_csv,
        policy_rows,
        [
            "question_id",
            "year",
            "district",
            "exam_stage",
            "question_no",
            "evidence_level",
            "expansion_status",
            "framework_entry_node",
            "partial_policy",
            "core_codebook_use",
            "policy_reason",
            "next_action",
        ],
    )

    counts = Counter(r["partial_policy"] for r in policy_rows)
    evidence_counts = Counter(r["evidence_level"] for r in policy_rows)
    out_md = ROOT / "10_framework_validation/framework_v1_2_partial_policy_20260519.md"
    lines = [
        "# Framework v1.2 PARTIAL Policy",
        "",
        "This file prevents PARTIAL rows from being mistaken for core framework evidence.",
        "",
        f"- PARTIAL rows: {len(policy_rows)}",
        f"- reference_only demos: {evidence_counts.get('reference_only', 0)}",
        f"- formal non-core/open rows: {evidence_counts.get('formal', 0)}",
        "",
        "## Counts",
        "",
    ]
    for key, value in sorted(counts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "These rows may be used to pressure-test framework_v2, but none may create a new core node unless separately supported by repeated formal evidence and a new cross-validation record.",
            "",
            "## Correction Note",
            "",
            f"The PARTIAL policy ledger now matches the pressure table and baodian sidecar: {len(policy_rows)} PARTIAL rows. Open-container rows remain non-core even when they have formal evidence.",
        ]
    )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"partial_total": len(policy_rows), **{f"partial_policy:{k}": v for k, v in counts.items()}}


def write_docx_qa() -> None:
    docx = ROOT / "12_final_baodian/选必二法律主观题满分宝典.docx"
    ql_png = ROOT / "12_final_baodian/docx_quicklook_guarded_v2/选必二法律主观题满分宝典.docx.png"
    qa = ROOT / "12_final_baodian/DOCX_QA_GUARDED_V2.md"
    text = f"""# DOCX QA - Guarded v2

Generated: 2026-05-19 Asia/Shanghai

## Target

- DOCX: `{docx}`
- Markdown source: `{ROOT / '12_final_baodian/选必二法律主观题满分宝典.md'}`

## Structural Check

- DOCX zip container: PASS
- `word/document.xml`: present
- text characters in document XML: 95821
- paragraph count in document XML: 1730
- table count in document XML: 0

## Visual/Renderer Check

- LibreOffice `soffice`: unavailable on this Mac, so the standard `render_docx.py` full-page PNG gate cannot run.
- Microsoft Word 16.109 is installed, but AppleScript open/save/export did not successfully produce a Word-saved DOCX/PDF in this pass. The attempted export ended in an AppleEvent timeout/open-object failure, and no guarded-v2 Word-saved PDF was created.
- Quick Look thumbnail fallback: PASS for first-page preview only.
- Quick Look PNG: `{ql_png}`

## QA Decision

The current DOCX is structurally valid and the first page renders cleanly through Quick Look. Full Word/PDF page-by-page visual QA remains **not closed** for guarded v2. Do not claim Word/PDF acceptance until Word or another full renderer produces a complete PDF/PNG set.
"""
    qa.write_text(text, encoding="utf-8")


def build_gptpro_packet() -> Path:
    packet_dir = ROOT / "05_reasoner_packets/gpt55pro_guarded_v2_review_20260519"
    files_dir = packet_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=True)

    key_files = [
        "04_merge_audit/merged_subjective_law_questions.csv",
        "04_merge_audit/merged_material_atoms_subjective.csv",
        "04_merge_audit/merged_ask_atoms_subjective.csv",
        "04_merge_audit/merged_rubric_atoms_subjective.csv",
        "08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.csv",
        "08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.md",
        "08_codebook/codebook_v1_2_after_fail4_cowork_source_evidence_map_20260519.csv",
        "08_codebook/codebook_v1_2_after_fail4_cowork_risks_20260519.md",
        "09_candidate_frameworks/framework_v1_2_guarded.md",
        "09_candidate_frameworks/framework_v1_2_evidence_map.csv",
        "10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv",
        "10_framework_validation/framework_v1_2_pass_report_20260519.md",
        "10_framework_validation/framework_v1_2_partial_policy_20260519.csv",
        "10_framework_validation/framework_v1_2_partial_policy_20260519.md",
        "11_final_framework/framework_v2.md",
        "11_final_framework/framework_v2_evidence_map.csv",
        "11_final_framework/framework_v2_student_one_page.md",
        "11_final_framework/framework_v2_teacher_guide.md",
        "11_final_framework/framework_v2_validation_summary.md",
        "12_final_baodian/选必二法律主观题满分宝典.md",
        "12_final_baodian/question_by_question_framework_runs.csv",
        "12_final_baodian/full_score_sentence_bank.csv",
        "12_final_baodian/material_trigger_bank.csv",
        "12_final_baodian/common_failure_paths.md",
        "12_final_baodian/DOCX_QA_GUARDED_V2.md",
        "10_framework_validation/fail4_source_adjudication_20260519/claude_cowork_output/fail4_targeted_adjudication_claude_cowork_20260519.md",
        "10_framework_validation/fail4_source_adjudication_20260519/fail4_external_cross_check_20260519.md",
    ]

    copied: list[str] = []
    missing: list[str] = []
    for rel in key_files:
        src = ROOT / rel
        if src.exists():
            dst = files_dir / rel.replace("/", "__")
            shutil.copy2(src, dst)
            copied.append(rel)
        else:
            missing.append(rel)

    questions = read_csv(ROOT / "04_merge_audit/merged_subjective_law_questions.csv")
    runs = read_csv(ROOT / "12_final_baodian/question_by_question_framework_runs.csv")
    q_counts = Counter(r.get("evidence_level", "") for r in questions)
    pass_counts = Counter(r.get("pass_status", "") for r in runs)
    label_counts = Counter(r.get("baodian_label", "") for r in runs)
    core_supported = label_counts.get("core_full_score_supported", 0)
    boundary_supported = label_counts.get("boundary_non_core", 0)
    partial_total = pass_counts.get("PARTIAL", 0)

    prompt = f"""# REPORT TO GPT-5.5 PRO - Guarded v2 Progress Review

You are GPT-5.5 Pro in the `选必二《法律与生活》主观题框架从题源生长工程`.

This is a progress/review packet, not a request to invent a new framework from memory. Please review only the attached/current evidence artifacts and tell Codex what is acceptable, what must be patched, and what must remain non-core.

## Current Verified Progress

- Current canonical corpus: {len(questions)} subjective-law question rows.
- Evidence levels: formal {q_counts.get('formal', 0)}, reference_only {q_counts.get('reference_only', 0)}, missing {q_counts.get('missing', 0)}.
- Current rubric atoms: 370 after CC0143 scoring-only patch.
- Guarded v1.2 pressure result: PASS {pass_counts.get('PASS', 0)}, PARTIAL {pass_counts.get('PARTIAL', 0)}, FAIL {pass_counts.get('FAIL', 0)}.
- PASS interpretation: {core_supported} core full-score supported rows + {boundary_supported} boundary-gate pass rows. Boundary-gate pass is not a selected-compulsory-2 full-score template.
- PARTIAL interpretation: {partial_total} non-core rows = formal/open or reference-only demos; they cannot support new framework core nodes without repeated formal evidence and cross-validation.
- Current baodian labels: {dict(label_counts)}.
- DOCX status: structurally valid and first-page Quick Look preview passes, but full Word/PDF page-by-page visual QA is not closed for guarded v2.

## What Changed Since Earlier Versions

1. The earlier 35-question and later 53/56/66-row packages are superseded.
2. ClaudeCode VS Code audit and Claude Cowork checks forced a 65-question canonical corpus: 61 formal, 4 reference_only, 0 missing.
3. CC0143 was patched into the consumer-contract/fraud-compensation code with scoring-only atoms. Teaching-reflection-only atoms were demoted as non-core support.
4. CC0276 and `RECOVER_2026_西城_二模_18_3` are boundary exclusions, not core 选必二 framework evidence.
5. `RECOVER_2026_西城_二模_18_2` and `CC0380_2026_顺义_二模_18_2` are open-container-only, not core templates.
6. `framework_v2` is a guarded teaching framework: teachable core path exists, but the handbook must preserve core/open/reference/boundary labels and cannot advertise all 65 as full-score core closure.

## Attached Inputs

The packet directory contains copied current artifacts under `files/`, including:

{chr(10).join('- ' + item for item in copied)}

Missing expected artifacts:

{chr(10).join('- ' + item for item in missing) if missing else '- none'}

## Review Tasks

Please output a structured review with these sections:

1. `ACCEPTABLE_PROGRESS`
   - State whether the 65-question corpus and guarded v2 can be treated as the current factual baseline.
   - State whether the {core_supported} core + {boundary_supported} boundary + {partial_total} partial policy is evidence-safe.

2. `BLOCKERS_BEFORE_FINAL_CLAIM`
   - List anything that prevents Codex from claiming final full closure.
   - Include DOCX visual QA if you agree it remains a blocker.

3. `ROW_LEVEL_PATCH_TABLE`
   - TSV columns: `question_id`, `current_label`, `decision`, `required_patch`, `evidence_needed`, `severity`.
   - Only include rows that need change, source check, promotion, demotion, or stronger warning.

4. `FRAMEWORK_PATCH_TABLE`
   - TSV columns: `node_id_or_file`, `issue`, `required_patch`, `why`, `severity`.

5. `BAODIAN_PATCH_TABLE`
   - TSV columns: `section_or_file`, `issue`, `required_patch`, `why`, `severity`.

6. `CAN_CONTINUE_TO_NEXT_STEP`
   - Choose one: `YES_WITH_GUARDS`, `NO_BLOCKED`, or `ONLY_LOCAL_POLISH`.
   - Explain exactly what Codex should do next.

## Hard Rules

- Do not promote reference_only evidence into formal support.
- Do not turn open-container rows into core nodes without repeated formal support and explicit question/rubric/material IDs.
- Do not法考化, do not必修三化, do not make a textbook-directory framework.
- If a claim lacks question_id and rubric_atom_id support, mark it `reject_or_pending`.
- Keep the two-layer structure: high-frequency core trunk + open/boundary/reference containers.
"""

    handoff = ROOT / "handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md"
    handoff.write_text(prompt, encoding="utf-8")
    (packet_dir / "CURRENT_PROGRESS_FOR_GPT55PRO.md").write_text(prompt, encoding="utf-8")

    readme = f"""# GPT-5.5 Pro Guarded v2 Review Packet

Generated: 2026-05-19 Asia/Shanghai

- Prompt: `{handoff}`
- Copied artifact count: {len(copied)}
- Missing artifact count: {len(missing)}
- Corpus: {len(questions)} questions; formal {q_counts.get('formal', 0)}; reference_only {q_counts.get('reference_only', 0)}; missing {q_counts.get('missing', 0)}
- Pressure: PASS {pass_counts.get('PASS', 0)}; PARTIAL {pass_counts.get('PARTIAL', 0)}; FAIL {pass_counts.get('FAIL', 0)}
- Labels: {dict(label_counts)}

Status: prepared for real GPT-5.5 Pro visible review. If not submitted through the web/app, treat as `real_call_pending`.
"""
    (packet_dir / "README.md").write_text(readme, encoding="utf-8")

    zip_path = ROOT / "05_reasoner_packets/gpt55pro_guarded_v2_review_20260519.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in packet_dir.rglob("*"):
            z.write(path, path.relative_to(packet_dir.parent))

    status = ROOT / "tool_outputs/gpt55pro_guarded_v2_review_call_status_20260519.md"
    status.write_text(
        """# GPT-5.5 Pro Guarded v2 Review Call Status

Status: prepared_not_submitted

- Prompt saved to `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md`.
- Packet saved to `05_reasoner_packets/gpt55pro_guarded_v2_review_20260519.zip`.
- Real GPT-5.5 Pro web/app submission is still pending.
- No local Codex simulation should be treated as the GPT-5.5 Pro review.
""",
        encoding="utf-8",
    )
    return zip_path


def update_control_files(zip_path: Path) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
    marker = "STEP_51_GUARDED_V2_QA_AND_GPTPRO_PACKET"
    append_once(
        ROOT / "PROGRESS.md",
        marker,
        f"""| {marker} | completed_local | 10_framework_validation/framework_v1_2_partial_policy_20260519.md; 12_final_baodian/DOCX_QA_GUARDED_V2.md; handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md; 05_reasoner_packets/gpt55pro_guarded_v2_review_20260519.zip | Corrected PARTIAL policy to match the current pressure table, recorded guarded-v2 DOCX structural/QuickLook QA with full Word/PDF still open, and prepared GPT-5.5 Pro progress-review packet. Real GPTPro submission remains pending. |""",
    )
    append_once(
        ROOT / "governor_board.md",
        marker,
        f"""## {marker} - {timestamp}

1. 当前阶段：guarded v2 QA + GPT-5.5 Pro 进度审查包准备。
2. 已完成文件：`10_framework_validation/framework_v1_2_partial_policy_20260519.md/.csv`; `12_final_baodian/DOCX_QA_GUARDED_V2.md`; `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md`; `{zip_path}`。
3. 证据数量：65 question rows; 482 material atoms; 65 ask atoms; 370 rubric atoms.
4. formal/reference_only/missing：61 / 4 / 0.
5. 争议题数量：non-core PARTIAL rows follow `framework_v1_2_partial_policy_20260519.csv`; 2 boundary-gate PASS rows.
6. 当前是否允许进入下一阶段：不允许无条件最终闭合；允许提交 GPT-5.5 Pro 审查。
7. 不允许原因：guarded v2 全页 Word/PDF 视觉 QA 未闭合；GPT-5.5 Pro 当前轮真实审查尚未回收。
8. 下一步任务：真实提交 GPT-5.5 Pro 审查包，回收后做行级补丁/保留/降级裁决。
9. 责任工具：Codex A + GPT-5.5 Pro。
10. 时间戳：{timestamp}。
""",
    )
    append_once(
        ROOT / "DECISIONS.md",
        "D056_GUARDED_V2_PARTIAL_POLICY_MATCHES_PRESSURE",
        """## D056_GUARDED_V2_PARTIAL_POLICY_MATCHES_PRESSURE

- Decision: `framework_v1_2_partial_policy_20260519` must match the current pressure table and baodian sidecar.
- Reason: open-container rows are non-core even when formal; this includes AI/open-boundary cases such as `RECOVER_2026_西城_二模_18_2` and `CC0380_2026_顺义_二模_18_2` when present in PARTIAL.
- Consequence: PARTIAL rows cannot support a new core node without repeated formal evidence and cross-validation.
""",
    )
    append_once(
        ROOT / "DECISIONS.md",
        "D057_GPTPRO_REVIEW_PENDING_NOT_SIMULATED",
        """## D057_GPTPRO_REVIEW_PENDING_NOT_SIMULATED

- Decision: the guarded v2 packet is prepared for GPT-5.5 Pro, but until a visible/web GPT-5.5 Pro response is captured, the phase remains `real_call_pending`.
- Reason: 选必二 framework-phase rules require real GPT/Claude model calls; local Codex notes cannot substitute for GPT-5.5 Pro.
""",
    )
    append_once(
        ROOT / "RISKS.md",
        "R037_GUARDED_V2_DOCX_VISUAL_QA_OPEN",
        """## R037_GUARDED_V2_DOCX_VISUAL_QA_OPEN

- Risk: guarded v2 DOCX is structurally valid and Quick Look can preview page 1, but full Word/PDF page-by-page visual QA is not closed because `soffice` is unavailable and Word AppleScript export failed in this pass.
- Mitigation: do not claim final Word/PDF acceptance; keep DOCX QA status explicit and retry via Word UI/manual save or another renderer before final delivery PASS.
""",
    )
    append_once(
        ROOT / "TODO.md",
        "TODO_GPTPRO_GUARDED_V2_REVIEW",
        """## TODO_GPTPRO_GUARDED_V2_REVIEW

- [ ] Submit `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md` plus `05_reasoner_packets/gpt55pro_guarded_v2_review_20260519.zip` to real GPT-5.5 Pro.
- [ ] Capture GPT-5.5 Pro output under `06_open_observations/` or `tool_outputs/`.
- [ ] Apply only evidence-supported row/file patches after GPT-5.5 Pro review.
- [ ] Retry full Word/PDF visual QA for guarded v2 before final delivery PASS.
""",
    )


def main() -> None:
    rebuild_partial_policy()
    write_docx_qa()
    zip_path = build_gptpro_packet()
    update_control_files(zip_path)
    print(f"wrote {zip_path}")


if __name__ == "__main__":
    main()
