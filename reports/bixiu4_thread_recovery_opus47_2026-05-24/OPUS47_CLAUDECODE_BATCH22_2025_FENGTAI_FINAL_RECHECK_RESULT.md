# ClaudeCode Batch22 Recheck Result - 2025 Fengtai Final

Parsed from raw stream:

- `OPUS47_CLAUDECODE_BATCH22_2025_FENGTAI_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl`
- `OPUS47_CLAUDECODE_BATCH22_2025_FENGTAI_FINAL_RUNTIME_EVIDENCE.json`

## Result

- `content_result`: `pass_with_notes`
- `local_policy_result`: `pass_with_model_gate_blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `required_fixes`: see ClaudeCode final response below.

## Evidence Checked

- Matrix target: Batch22 should have `35` rows, `16` body rows, `19` boundary rows.
- Body target: `16` governed DOCX entries for Q4, Q7, Q16, and Q17.
- Render target: `252/252` pages/images, labels `2339/2339`, visible suite headings `16/16`.
- Ledger target: `16` governed records in both `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Global scope target: remaining raw midterm/final source gap `13` suites.

## Model Evidence Boundary

- Runtime observed models: `claude-api, claude-opus-4-7`.
- Command lane used `--model claude-opus-4-7 --effort max`.
- Stream thinking block/signature seen: `true`.
- Debug model mentions: `claude-haiku-4-5-20251001, claude-opus-4-7`.
- Sonnet/Haiku/model-unknown output is not counted as qualified evidence.
- Machine-readable adaptive/max-effort proof is still insufficient, so the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## ClaudeCode Final Response

I'll start by inspecting the Batch22 artifacts and source files in parallel to verify the recheck claims.Let me find the canonical matrix CSV and other key Batch22 artifacts.Let me read the key Batch22 artifacts in parallel.Now I'll check the matrix CSV, ledger, and accepted JSONL to verify counts.Now let me check the matrix rows breakdown (body vs boundary), then verify Q4/Q7/Q16/Q17 placements.Let me verify the source rubric supports the Q16 nodes and the Q17 boundary.All checks completed. Let me finalize the result.# ClaudeCode Opus 4.7 Recheck Result - Batch22 2025 丰台期末

- **content_result**: `pass_with_notes`
- **local_policy_result**: `pass_with_model_gate_blocked`
- **model_gate**: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` — runtime self-reports `claude-opus-4-7`, but adaptive/max-effort/thinking configuration cannot be verified from this lane and must not be self-certified.
- **sonnet_haiku_used**: `no` — this recheck was produced by the Opus 4.7 lane; no Sonnet/Haiku/model-unknown output was counted as qualified evidence.

## matrix_check

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` contains exactly **35** rows tagged `2025丰台期末`.
- Breakdown matches spec: **16 body rows** (Q4×1, Q7×1, Q16×13, Q17×1) + **19 boundary rows** (Q1, Q2, Q3, Q5, Q6, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q18(1), Q18(2), Q18(3), Q19, Q20, Q21).
- Q4 evidence label = `教师版客观答案/解析+题面正确项；非主观评分细则` — bounded as objective-choice only, not upgraded to scoring rubric. ✅
- Q7 evidence label = same objective-only bound; disposition = `REGISTERED_EXISTING_DOCX_BATCH22_FENGTAI_FINAL` — registered, not duplicated. ✅
- Q16 13 nodes all carry label `正式PPT评分细则+教师版题面/解析+当前DOCX正文`; cross-checked against formal rubric lines 205-210, 255-263, and the formal Q16 summary line "从实践、一切从实际出发、联系观、发展观、矛盾观等角度作答" (line 260). Every node maps to a rubric keyword (实践→实践与认识/实践是认识的基础; 实际→一切从实际出发; 规律→规律的客观性; 主观能动性→主观能动性/意识的能动作用; 质量互变→量变与质变; 系统优化→系统观念/系统优化; 整体部分→整体与部分; 矛盾→矛盾的特殊性/具体问题具体分析; 发展→发展的观点; 认识对实践的反作用→same; 正确的价值观→价值观的导向作用; 联系观→联系的普遍性). No principle invented beyond rubric/teacher source. ✅
- Q17 row uses only `人民群众`; `全过程人民民主` (line 50/56 of the rubric) is **not** imported into philosophy nodes. ✅

## docx_check

- Ledger `docx_insert_ledger.csv`: **16** rows containing `2025丰台期末`. ✅
- Accepted JSONL `student_patch_entries.accepted.jsonl`: **16** rows containing `2025丰台期末`. ✅
- Per `render_manifest.json` `word_headings` array, the current DOCX has **16** governed `2025丰台期末` headings; placements match spec exactly:
  - Q4 → 实现人生价值 (`9.…第4题`, page 251) ✅
  - Q7 → 一切从实际出发… (`16.…第7题`, page 14) ✅
  - Q17 → 人民群众 (`17.…第17题`, page 214) ✅
  - Q16 → 13 distinct main-body entries (`7., 8., 9., 10., 11., 13., 14., 15., 15., 18., 29., 31., 32.`) covering the 13 expected philosophy nodes; two `15.…第16题` entries appear correctly under different parent nodes (`主观能动性 / 意识的能动作用` and `实践与认识（总）`), consistent with the source transcription file. ✅
- DOCX/PDF newly applied this batch via `INSERTED_DOCX_BATCH22_FENGTAI_FINAL` = 6 entries (Q4实现人生价值, Q16 规律的客观性 / 系统观念 / 发展的观点 / 认识对实践的反作用 / 价值观的导向作用), matches fusion file `Newly inserted DOCX entries: 6`. ✅

## render_check

- PDF pages / rendered PNGs: **252 / 252**. ✅
- DOCX / PDF label count: **2339 / 2339**. ✅
- DOCX / Word-layout visible suite headings: **16 / 16**. ✅
- Raw PDF exact text-extraction suite mentions: `0` (expected — Word-generated PDF doesn't preserve this Chinese string for exact-string scan, as already noted in Batch21 QA precedent).
- Hit pages: `11, 14, 23, 42, 48, 69, 83, 95, 98, 137, 165, 179, 188, 214, 231, 251` — exact match to spec. ✅
- Blank-like pages: `[2]` only — confirmed as the intended `前言`/foreword/divider page. ✅
- Programmatic render gate: `RENDER_PASS_MODEL_PENDING`. ✅

## global_scope_check

- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`: row for `2025丰台期末` shows `matrix_rows=35`, `current_docx_mentions=16`, `status=covered_by_batch22_recovery_matrix`. ✅
- Remaining midterm/final raw suites outside current coverage: **13** (4 × 2025 + 9 × 2026), matching spec. ✅
- 47-suite first/second-mock strict-audit scope is preserved as the boundary; this recheck does **not** claim whole-project final acceptance.

## required_fixes

None for content correctness. The following non-content gates remain open and must not be self-flipped from this lane:

1. Adaptive/max-effort/thinking proof for Opus 4.7 — `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
2. GPTPro web full-artifact review — `real_call_pending`.
3. External Claude Opus full-artifact review — `real_call_pending`.

## remaining_project_blockers

- **Model-effort gate**: cannot confirm `adaptive`/`max-effort`/`thinking` configuration from runtime; status remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until an authoritative configuration record is produced.
- **External reviews still pending**: GPTPro web review and external Claude Opus full-artifact review are both `real_call_pending`.
- **Raw-source scope gap**: 13 midterm/final raw suites (`2025朝阳期末/海淀期中/海淀期末/西城期末`; `2026东城/丰台/朝阳期中/朝阳/海淀期中/海淀/石景山/西城/通州期末`) remain outside the current strict 47-suite first/second-mock audit scope.
- **Whole-project final acceptance**: explicitly not claimed by this recheck (hard rule).
- **Full every-page manual typography comparison**: still open per the FORMAT_RENDER_QA log.

Batch22 may be treated as **locally closed for content and render**, while the model-effort, GPTPro, and external-Opus gates and the 13 out-of-scope raw suites continue to block whole-project final acceptance.
