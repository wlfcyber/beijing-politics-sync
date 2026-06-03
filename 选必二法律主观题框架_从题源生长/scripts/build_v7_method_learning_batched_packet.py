#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the V7 method-learning-first packet for GPTPro / Claude Opus.

This packet deliberately separates:
1. prior-framework method learning,
2. current-law framework failure diagnosis,
3. batched legal evidence processing.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import textwrap
import zipfile
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
OUT = ROOT / "05_reasoner_packets" / "v7_method_learning_batched_rebuild_20260521"
PRIOR = ROOT / "05_reasoner_packets" / "prior_framework_deep_learning_20260520"
DATE = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


CORE_CATEGORY_BY_DISPLAY = {
    "1": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/entity_responsibility",
    "2": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/labor",
    "3": "BATCH_03_INNOVATION_AI_VALUE/value",
    "4": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/contract",
    "5": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/consumer",
    "6": "BATCH_03_INNOVATION_AI_VALUE/innovation_competition",
    "7": "BATCH_02_PROCEDURE_TABLE/procedure",
    "8": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/consumer",
    "9": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/entity_responsibility",
    "10": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/labor",
    "11": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/entity_responsibility",
    "12": "BATCH_03_INNOVATION_AI_VALUE/innovation_competition",
    "13": "BATCH_03_INNOVATION_AI_VALUE/value",
    "14": "BATCH_03_INNOVATION_AI_VALUE/innovation_competition",
    "15": "BATCH_03_INNOVATION_AI_VALUE/innovation_competition",
    "16": "BATCH_02_PROCEDURE_TABLE/procedure",
    "17": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/labor",
    "18": "BATCH_02_PROCEDURE_TABLE/table_completion",
    "19": "BATCH_02_PROCEDURE_TABLE/table_completion",
    "20": "BATCH_02_PROCEDURE_TABLE/procedure",
    "21": "BATCH_02_PROCEDURE_TABLE/procedure",
    "22": "BATCH_03_INNOVATION_AI_VALUE/innovation_competition",
    "23": "BATCH_02_PROCEDURE_TABLE/procedure",
    "24": "BATCH_03_INNOVATION_AI_VALUE/ai_boundary",
    "25": "BATCH_03_INNOVATION_AI_VALUE/ai_boundary",
    "26": "BATCH_02_PROCEDURE_TABLE/procedure",
    "27": "BATCH_01_HIGH_FREQ_CORE_JUDGMENT/contract",
}

BATCH_NAMES = {
    "BATCH_01_HIGH_FREQ_CORE_JUDGMENT": "高频实体判断：合同、消费、劳动、一般责任",
    "BATCH_02_PROCEDURE_TABLE": "程序救济与表格补全：路径、证据、请求、表格格子",
    "BATCH_03_INNOVATION_AI_VALUE": "创新竞争、AI边界、价值收束",
    "BATCH_04_NON_CORE_OPEN_CONTAINER": "38道非核心与开放容器：保分、边界、reference_only",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def safe_ascii_name(name: str, fallback: str) -> str:
    stem = Path(name).stem
    suffix = Path(name).suffix
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", stem)
    stem = stem.strip("._-")
    if not stem:
        stem = fallback
    return f"{stem}{suffix}"


def md_escape(text: str) -> str:
    return (text or "").replace("\r\n", "\n").strip()


def shorten(text: str, limit: int = 1400) -> str:
    text = md_escape(text)
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n...[TRUNCATED_IN_BATCH_CARD; see full CSV in /evidence_full/]"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def make_question_card(q: dict[str, str], rubrics: list[dict[str, str]], core_row: dict[str, str] | None = None) -> str:
    bits = []
    bits.append(f"### {q['question_id']}")
    bits.append("")
    bits.append(f"- 题源：{q.get('year','')} {q.get('district','')} {q.get('exam_stage','')} 第{q.get('question_no','')}题 {q.get('sub_question_no','')}".strip())
    bits.append(f"- 证据等级：{q.get('evidence_level','')} / {q.get('evidence_type','')}")
    bits.append(f"- 模块边界：{q.get('module_boundary_risk','')}；置信度：{q.get('confidence','')}")
    if core_row:
        bits.append(f"- V6.9暂归位：{core_row.get('framework_entry_nodes','')}")
        bits.append(f"- V6.9学生第一判断：{core_row.get('student_first_judgment_v5_5','')}")
        bits.append(f"- V6.9踩分词：{core_row.get('must_have_keywords','')}")
    bits.append("")
    bits.append("**设问**")
    bits.append("")
    bits.append(shorten(q.get("ask_text", ""), 900))
    bits.append("")
    bits.append("**材料/题干压缩摘录**")
    bits.append("")
    material = q.get("material_text") or q.get("full_question_text") or ""
    bits.append(shorten(material, 1600))
    bits.append("")
    bits.append("**细则/答案原子**")
    bits.append("")
    for r in rubrics:
        bits.append(
            f"- `{r.get('rubric_atom_id','')}` [{r.get('evidence_level','')}/{r.get('evidence_type','')}; "
            f"{r.get('knowledge_material_value_type','')}] "
            f"{md_escape(r.get('rubric_or_answer_phrase',''))}"
        )
        if r.get("legal_knowledge_or_rule_if_explicit"):
            bits.append(f"  - 法律规则信号：{md_escape(r.get('legal_knowledge_or_rule_if_explicit',''))}")
        if r.get("what_judgment_student_must_make_before_writing"):
            bits.append(f"  - 写前判断：{md_escape(r.get('what_judgment_student_must_make_before_writing',''))}")
    bits.append("")
    return "\n".join(bits)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "prior_framework_learning").mkdir(parents=True)
    (OUT / "current_law_candidate").mkdir(parents=True)
    (OUT / "evidence_full").mkdir(parents=True)
    (OUT / "batches").mkdir(parents=True)
    (OUT / "rendered_prior_samples").mkdir(parents=True)

    # Core inputs.
    source_files = [
        PRIOR / "PRIOR_FRAMEWORK_DEEP_DNA_20260520.md",
        PRIOR / "LEGAL_REWRITE_SPEC_AFTER_PRIOR_STUDY_20260520.md",
        PRIOR / "MODEL_PACKET_README.md",
        ROOT / "09_candidate_frameworks" / "gptpro_current_framework_prior_learning_countermeasures_20260520.md",
        ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_9_恢复27核心完整学生使用版_20260521.md",
        ROOT / "12_final_baodian" / "DOCX_QA_V6_9_STUDENT_20260521.md",
        ROOT / "10_framework_validation" / "v6_9_core_section_integrity_audit_20260521.md",
        ROOT / "10_framework_validation" / "v6_9_student_text_hygiene_scan_20260521.md",
    ]
    for src in source_files:
        if src.exists():
            if "prior_framework_deep_learning" in str(src):
                copy_file(src, OUT / "prior_framework_learning" / src.name)
            elif src.name.startswith("gptpro_"):
                copy_file(src, OUT / "prior_framework_learning" / src.name)
            elif src.name.startswith("选必二法律主观题满分训练宝典_v6_9"):
                copy_file(src, OUT / "current_law_candidate" / "current_v6_9_student_candidate.md")
            else:
                copy_file(src, OUT / "current_law_candidate" / src.name)

    # Copy rendered prior samples, capped to files already curated.
    sample_index = []
    sample_dir = PRIOR / "rendered_samples"
    if sample_dir.exists():
        for i, png in enumerate(sorted(sample_dir.glob("*.png")), start=1):
            safe = f"prior_sample_{i:02d}.png"
            copy_file(png, OUT / "rendered_prior_samples" / safe)
            sample_index.append({
                "safe_filename": safe,
                "original_filename": png.name,
                "bytes": str(png.stat().st_size),
            })
    if sample_index:
        write_csv(OUT / "rendered_prior_samples" / "INDEX.csv", sample_index)

    prior_paths = []
    prior_source_dir = Path("/Users/wanglifei/Desktop/先前框架")
    if prior_source_dir.exists():
        for p in sorted(prior_source_dir.glob("*")):
            if p.is_file() and p.name != ".DS_Store":
                prior_paths.append(f"- `{p}` ({p.stat().st_size / 1024 / 1024:.1f} MB)")
    (OUT / "prior_framework_learning" / "ORIGINAL_PRIOR_FRAMEWORK_PATHS.md").write_text(
        "# Original Prior Framework Files\n\n"
        "The full source PDFs are large, so this packet includes curated rendered samples and extracted DNA. "
        "If the web model needs an original PDF, upload it separately from these paths.\n\n"
        + "\n".join(prior_paths)
        + "\n",
        encoding="utf-8",
    )

    full_files = [
        ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv",
        ROOT / "04_merge_audit" / "merged_material_atoms_subjective.csv",
        ROOT / "04_merge_audit" / "merged_ask_atoms_subjective.csv",
        ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv",
        ROOT / "08_codebook" / "provisional_codebook_v1_3_after_gptpro_guarded_review_20260519.csv",
        ROOT / "12_final_baodian" / "question_by_question_framework_runs_v5_9_27core65guard_20260521.csv",
        ROOT / "12_final_baodian" / "non_core_guardrails_v5_9_20260521.csv",
        ROOT / "12_final_baodian" / "full_score_sentence_bank_v5_2_27strict_core_20260521.csv",
        ROOT / "12_final_baodian" / "material_trigger_bank_v5_draft_20260521.csv",
        ROOT / "04_merge_audit" / "candidate70_to_current65_delta_summary_20260521.md",
        ROOT / "04_merge_audit" / "candidate70_to_current65_delta_ledger_20260521.csv",
    ]
    for src in full_files:
        if src.exists():
            copy_file(src, OUT / "evidence_full" / src.name)

    questions = {r["question_id"]: r for r in read_csv(ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv")}
    rubric_rows = read_csv(ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv")
    rubrics_by_q: dict[str, list[dict[str, str]]] = {}
    for r in rubric_rows:
        rubrics_by_q.setdefault(r["question_id"], []).append(r)
    core_rows = read_csv(ROOT / "12_final_baodian" / "question_by_question_framework_runs_v5_9_27core65guard_20260521.csv")
    non_core_rows = read_csv(ROOT / "12_final_baodian" / "non_core_guardrails_v5_9_20260521.csv")
    core_by_id = {r["question_id"]: r for r in core_rows}

    # Build core batch md/csv.
    batch_rows: dict[str, list[dict[str, str]]] = {k: [] for k in BATCH_NAMES}
    for row in core_rows:
        batch = CORE_CATEGORY_BY_DISPLAY[row["display_index"]].split("/")[0]
        enriched = dict(row)
        enriched["batch_id"] = batch
        enriched["batch_name"] = BATCH_NAMES[batch]
        enriched["batch_subtype"] = CORE_CATEGORY_BY_DISPLAY[row["display_index"]].split("/", 1)[1]
        batch_rows[batch].append(enriched)

    for row in non_core_rows:
        enriched = dict(row)
        enriched["batch_id"] = "BATCH_04_NON_CORE_OPEN_CONTAINER"
        enriched["batch_name"] = BATCH_NAMES["BATCH_04_NON_CORE_OPEN_CONTAINER"]
        enriched["batch_subtype"] = row.get("student_category", "")
        batch_rows["BATCH_04_NON_CORE_OPEN_CONTAINER"].append(enriched)

    manifest_rows = []
    for batch, rows in batch_rows.items():
        write_csv(OUT / "batches" / f"{batch}.csv", rows)
        parts = [f"# {batch}: {BATCH_NAMES[batch]}", ""]
        parts.append("本文件是给 GPTPro / Claude Opus 的分批证据卡。请按本批独立归纳机制，不要跳到总框架。")
        parts.append("")
        if batch != "BATCH_04_NON_CORE_OPEN_CONTAINER":
            for row in rows:
                qid = row["question_id"]
                parts.append(make_question_card(questions[qid], rubrics_by_q.get(qid, []), core_by_id.get(qid)))
        else:
            parts.append("## 非核心/开放容器清单")
            parts.append("")
            for row in rows:
                qid = row["question_id"]
                q = questions.get(qid, {})
                parts.append(f"### {qid}")
                parts.append(f"- 题源：{row.get('source_label','')}")
                parts.append(f"- 证据等级：{row.get('evidence_level','')}")
                parts.append(f"- 当前类型：{row.get('student_category','')}")
                parts.append(f"- 最小保分句1：{row.get('minimum_sentence_1','')}")
                parts.append(f"- 最小保分句2：{row.get('minimum_sentence_2','')}")
                parts.append(f"- 最小保分句3：{row.get('minimum_sentence_3','')}")
                parts.append(f"- 禁止乱写：{row.get('do_not_write','')}")
                parts.append("**设问**")
                parts.append(shorten(q.get("ask_text", ""), 800))
                parts.append("**细则/答案原子**")
                for r in rubrics_by_q.get(qid, []):
                    parts.append(f"- `{r.get('rubric_atom_id','')}` [{r.get('evidence_level','')}/{r.get('evidence_type','')}] {md_escape(r.get('rubric_or_answer_phrase',''))}")
                parts.append("")
        md_path = OUT / "batches" / f"{batch}.md"
        md_path.write_text("\n".join(parts), encoding="utf-8")
        manifest_rows.append({
            "batch_id": batch,
            "batch_name": BATCH_NAMES[batch],
            "question_count": str(len(rows)),
            "file_md": f"batches/{batch}.md",
            "file_csv": f"batches/{batch}.csv",
        })

    write_csv(OUT / "BATCH_MANIFEST.csv", manifest_rows)

    stats = {
        "created_at": DATE,
        "total_questions": len(questions),
        "core_questions": len(core_rows),
        "non_core_questions": len(non_core_rows),
        "evidence_level_counts": {},
        "rubric_atom_count": len(rubric_rows),
    }
    for q in questions.values():
        stats["evidence_level_counts"][q.get("evidence_level", "")] = stats["evidence_level_counts"].get(q.get("evidence_level", ""), 0) + 1
    (OUT / "CURRENT_LAW_CORPUS_STATS.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "CURRENT_LAW_CORPUS_STATS.md").write_text(
        textwrap.dedent(f"""\
        # Current Law Corpus Stats

        - created_at: {DATE}
        - total_subjective_law_questions: {len(questions)}
        - evidence_level: {stats['evidence_level_counts']}
        - rubric_atoms: {len(rubric_rows)}
        - current_student_candidate: V6.9, kept as failed/insufficient candidate to critique, not as final answer.
        - batching_rule: GPTPro / Claude must first learn prior-framework DNA, then process batches in order.

        ## Batch Counts

        {chr(10).join(f"- {r['batch_id']}: {r['question_count']} questions, {r['batch_name']}" for r in manifest_rows)}
        """),
        encoding="utf-8",
    )

    prompt = textwrap.dedent("""\
    # GPTPro / Claude Opus V7 Task: Learn The User's Framework Method First, Then Rebuild Xuanbier Law

    You are participating in the user's 选必二《法律与生活》主观题框架重建工程.

    ## Absolute order

    Do not immediately write a new law framework.

    Step 1: Learn the user's previous strong framework style from:
    - `prior_framework_learning/PRIOR_FRAMEWORK_DEEP_DNA_20260520.md`
    - `prior_framework_learning/LEGAL_REWRITE_SPEC_AFTER_PRIOR_STUDY_20260520.md`
    - `rendered_prior_samples/`

    Output first: `METHOD_LEARNING_NOTES`.
    You must explain what makes those frameworks usable for a smart but zero-baseline Gaokao student.

    Step 2: Read the current law candidate V6.9 in `current_law_candidate/`.
    Output: `WHY_V6_9_STILL_NOT_ENOUGH`.
    Be harsh. The user's complaint is that the current framework still does not let a student reliably answer full marks.

    Step 3: Process legal evidence by batches, in this order:
    - `batches/BATCH_01_HIGH_FREQ_CORE_JUDGMENT.md`
    - `batches/BATCH_02_PROCEDURE_TABLE.md`
    - `batches/BATCH_03_INNOVATION_AI_VALUE.md`
    - `batches/BATCH_04_NON_CORE_OPEN_CONTAINER.md`

    For each batch output:
    - `batch_mechanisms`: what scoring mechanisms really recur.
    - `student_start_moves`: what the student should do first when seeing this batch type.
    - `material_to_legal_translation`: material signal -> legal language -> scoring sentence.
    - `full_score_sentence_rules`: sentence formulas, not empty slogans.
    - `bad_framework_nodes_to_delete_or_demote`: anything pretty but not useful.
    - `evidence_ids`: question_id + rubric_atom_id, mandatory.

    Step 4: Only after all batches, create a V7 candidate framework.

    Please write your answer in Chinese. Keep all evidence ids unchanged.

    ## Required V7 output

    1. `METHOD_LEARNING_NOTES`
    2. `WHY_V6_9_STILL_NOT_ENOUGH`
    3. `BATCH_01_FINDINGS`
    4. `BATCH_02_FINDINGS`
    5. `BATCH_03_FINDINGS`
    6. `BATCH_04_FINDINGS`
    7. `V7_FRAMEWORK_PROPOSAL`
    8. `V7_STUDENT_FIRST_10_PAGES_PLAN`
    9. `QUESTION_BY_QUESTION_STRESS_TEST_PLAN`
    10. `WHAT_YOU_NEED_FROM_CODEX_NEXT`

    ## Framework constraints

    - The framework must keep `主干高频层 + 开放容器层`.
    - Every node must be traceable to question_id and rubric_atom_id.
    - Do not use textbook chapter names as the front-stage framework.
    - Do not write a law-exam style framework.
    - Do not write broad 必修三 rule-of-law slogans.
    - A smart zero-baseline high-school student must know: first sentence, material translation, legal rule, scoring endpoint.
    - If a node cannot help the student write a sentence, delete it or demote it.

    ## Output verdict

    End with one of:
    - PASS_TO_REWRITE: enough to let Codex write V7.
    - CONDITIONAL_PASS_TO_REWRITE: Codex can write V7 only if listed fixes are applied.
    - FAIL_RETHINK: the batch evidence still does not support a useful framework.
    """)
    (OUT / "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md").write_text(prompt, encoding="utf-8")
    (OUT / "VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt").write_text(
        "请读取上传压缩包中的 PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md。\n"
        "重要：先学习 prior_framework_learning 和 rendered_prior_samples 里的旧框架方法，再按 batches 顺序分批处理法律题，最后才提出 V7 框架。不要直接写总框架。\n",
        encoding="utf-8",
    )
    (OUT / "VISIBLE_PROMPT_ASCII_FALLBACK_20260521.txt").write_text(
        "Please open PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md in the attached zip. "
        "If Chinese text renders incorrectly, use the UTF-8 markdown files inside the zip. "
        "First learn the prior-framework method, then process the legal evidence batch by batch, and only then propose V7. "
        "Do not write a one-shot framework.\n",
        encoding="utf-8",
    )

    readme = textwrap.dedent(f"""\
    # V7 Method-Learning-First Batched Rebuild Packet

    created_at: {DATE}

    This packet answers the user's newest correction:

    > 让 GPT 和 Claude 先学会怎么做，把我的框架发给他们让他们学习后再创建新的。可以分批上传题。

    ## How to use

    1. Upload this zip to GPT-5.5 Pro and Claude Opus 4.7 Adaptive in separate fresh chats.
    2. Paste `VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt`.
    3. If the web UI displays garbled text, paste `VISIBLE_PROMPT_ASCII_FALLBACK_20260521.txt` and tell the model to read the UTF-8 md files inside the zip.
    4. Require the model to output all required sections in the prompt.

    ## Contents

    - `prior_framework_learning/`: extracted DNA and rewrite spec from the user's prior strong frameworks.
    - `rendered_prior_samples/`: visual samples from prior framework PDFs.
    - `current_law_candidate/`: current V6.9 candidate and QA/audit files, to criticize rather than accept.
    - `evidence_full/`: full evidence CSVs for back-reference.
    - `batches/`: four legal question batches.
    - `BATCH_MANIFEST.csv`: batch counts.
    - `CURRENT_LAW_CORPUS_STATS.md/json`: 65-question corpus stats.

    ## Status

    This is a handoff packet. It does not itself count as GPTPro or Claude Opus response.
    Until the real web/app outputs are captured, mark the external model gate as `real_call_pending`.
    """)
    (OUT / "PACKET_README.md").write_text(readme, encoding="utf-8")

    split_plan = textwrap.dedent(f"""\
    # Split Upload Plan For GPTPro / Claude Opus

    created_at: {DATE}

    Use the full zip first if the web UI accepts it:

    - `{OUT}.zip`

    If the full zip fails, upload in this order:

    1. `v7_method_learning_batched_rebuild_20260521_METHOD_PACK.zip`
       - prior framework DNA
       - rendered prior samples
       - current V6.9 candidate and failure-audit files
       - master prompt
    2. `v7_method_learning_batched_rebuild_20260521_BATCH_01.zip`
    3. `v7_method_learning_batched_rebuild_20260521_BATCH_02.zip`
    4. `v7_method_learning_batched_rebuild_20260521_BATCH_03.zip`
    5. `v7_method_learning_batched_rebuild_20260521_BATCH_04.zip`

    Important:

    - Paste `VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt` only once after the method pack or full pack.
    - Do not repeatedly press send in Claude. Upload, paste, send once, then wait.
    - If a model says it cannot see a batch, upload only the missing batch zip and ask it to continue from the last completed section.
    """)
    (OUT / "SPLIT_UPLOAD_PLAN.md").write_text(split_plan, encoding="utf-8")

    # File list included inside the zip, with ASCII filenames in paths.
    (OUT / "PACKET_FILE_LIST.json").write_text(
        json.dumps([str(p.relative_to(OUT)) for p in sorted(OUT.rglob("*")) if p.is_file()], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Compatibility handoff copies.
    handoff = ROOT / "handoff_prompts"
    handoff.mkdir(exist_ok=True)
    for name in [
        "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md",
        "VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt",
        "VISIBLE_PROMPT_ASCII_FALLBACK_20260521.txt",
    ]:
        copy_file(OUT / name, handoff / name.replace("GPTPRO_AND_CLAUDE_OPUS", "GPTPRO").replace("V7_METHOD_FIRST_REBUILD", "V7_METHOD_FIRST_REBUILD"))
        copy_file(OUT / name, handoff / name.replace("GPTPRO_AND_CLAUDE_OPUS", "CLAUDE_OPUS").replace("V7_METHOD_FIRST_REBUILD", "V7_METHOD_FIRST_REBUILD"))

    # Status notes.
    status_text = textwrap.dedent(f"""\
    # V7 external model status

    - created_at: {DATE}
    - packet: `{OUT}`
    - zip: `{OUT}.zip`
    - status: real_call_pending
    - reason: packet prepared; official GPTPro / Claude Opus web/app response not yet captured in this run.
    - UI safety note: do not repeatedly click send. Upload once, paste the short visible prompt once, then wait for natural completion.
    """)
    for model in ["gptpro", "claude_opus"]:
        (ROOT / "tool_outputs" / f"{model}_v7_method_first_batched_rebuild_status_20260521.md").write_text(status_text, encoding="utf-8")

    # Zip.
    zip_path = Path(str(OUT) + ".zip")
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(OUT.rglob("*")):
            z.write(path, path.relative_to(OUT.parent))

    def write_split_zip(suffix: str, rel_paths: list[str]) -> str:
        split_path = OUT.parent / f"v7_method_learning_batched_rebuild_20260521_{suffix}.zip"
        if split_path.exists():
            split_path.unlink()
        with zipfile.ZipFile(split_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for rel in rel_paths:
                p = OUT / rel
                if p.is_file():
                    zf.write(p, Path(OUT.name) / rel)
                elif p.is_dir():
                    for sub in sorted(p.rglob("*")):
                        if sub.is_file():
                            zf.write(sub, Path(OUT.name) / sub.relative_to(OUT))
        return str(split_path)

    split_zips = [
        write_split_zip("METHOD_PACK", [
            "PACKET_README.md",
            "SPLIT_UPLOAD_PLAN.md",
            "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md",
            "VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt",
            "VISIBLE_PROMPT_ASCII_FALLBACK_20260521.txt",
            "CURRENT_LAW_CORPUS_STATS.md",
            "BATCH_MANIFEST.csv",
            "prior_framework_learning",
            "rendered_prior_samples",
            "current_law_candidate",
        ]),
        write_split_zip("BATCH_01", [
            "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md",
            "batches/BATCH_01_HIGH_FREQ_CORE_JUDGMENT.md",
            "batches/BATCH_01_HIGH_FREQ_CORE_JUDGMENT.csv",
            "evidence_full/merged_rubric_atoms_subjective.csv",
            "evidence_full/merged_subjective_law_questions.csv",
        ]),
        write_split_zip("BATCH_02", [
            "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md",
            "batches/BATCH_02_PROCEDURE_TABLE.md",
            "batches/BATCH_02_PROCEDURE_TABLE.csv",
            "evidence_full/merged_rubric_atoms_subjective.csv",
            "evidence_full/merged_subjective_law_questions.csv",
        ]),
        write_split_zip("BATCH_03", [
            "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md",
            "batches/BATCH_03_INNOVATION_AI_VALUE.md",
            "batches/BATCH_03_INNOVATION_AI_VALUE.csv",
            "evidence_full/merged_rubric_atoms_subjective.csv",
            "evidence_full/merged_subjective_law_questions.csv",
        ]),
        write_split_zip("BATCH_04", [
            "PROMPT_FOR_GPTPRO_AND_CLAUDE_OPUS_V7_METHOD_FIRST_REBUILD_20260521.md",
            "batches/BATCH_04_NON_CORE_OPEN_CONTAINER.md",
            "batches/BATCH_04_NON_CORE_OPEN_CONTAINER.csv",
            "evidence_full/merged_rubric_atoms_subjective.csv",
            "evidence_full/merged_subjective_law_questions.csv",
        ]),
    ]

    manifest = {
        "packet_dir": str(OUT),
        "zip_path": str(zip_path),
        "zip_sha256": sha256(zip_path),
        "split_zips": split_zips,
        "files": [str(p.relative_to(OUT)) for p in sorted(OUT.rglob("*")) if p.is_file()],
        "stats": stats,
    }
    (OUT / "PACKET_BUILD_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
