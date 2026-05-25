# ClaudeCode Opus 4.7 Recheck Prompt - Batch22 2025 Fengtai Final

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread. You are not a casual reviewer. Recheck the Codex Batch22 work from source evidence and current artifacts.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write or claim final acceptance for the whole project.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. Verify this batch as a production lane.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending` unless actually completed elsewhere.
- If adaptive/max-effort proof cannot be confirmed, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## Files To Inspect

- `BATCH22_2025_FENGTAI_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH22_2025_FENGTAI_FINAL_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md`
- `FORMAT_RENDER_QA_20260524.md`
- `word_render_qa_20260525_batch22_word/render_manifest.json`
- `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- Current DOCX/PDF under `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`
- Source caches:
  - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\360d57a4b250de81_2025丰台期末细则.md`
  - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\89765092a6f26242_2025北京丰台高三_上_期末政治_教师版.md`

## Source Facts To Verify

1. Batch22 suite is `2025丰台期末`.
2. Teacher-version objective answer key is `1B 2D 3B 4A 5A 6A 7C 8D 9D 10B 11D 12B 13C 14C 15A`.
3. Q4 is objective-choice evidence only: answer A, correct items ①③ support `实现人生价值`; this is not a subjective scoring rubric.
4. Q7 is objective-choice evidence only: answer C supports `一切从实际出发 / 实事求是`; Batch22 should register the inherited DOCX entry, not duplicate it.
5. Q16 prompt is 胸中有“数”. Formal PPT rubric supports multiple philosophy nodes:
   - practice / actual conditions /规律 /主观能动性 from `数从哪里来`;
   - 质量互变规律 /系统优化 /整体部分 /矛盾 /发展 from `数当如何定`;
   - 认识对实践的反作用 /意识能动作用 /正确价值观 /系统优化 /整体部分 /发展 from `数为何所用`;
   - the formal line says Q16 may use 实践、一切从实际出发、联系观、发展观、矛盾观.
6. Q17 formal PPT rubric supports only the 必修四 historical-materialism point `人民群众是历史的创造者 / 群众观点`; `全过程人民民主` remains a political point and must not be imported into philosophy nodes.
7. Q1, Q2, Q3, Q5, Q6, Q8-Q15, Q18(1), Q18(2), Q18(3), Q19, Q20, and Q21 should be explicit boundary rows, not philosophy-body insertions.

## Expected Batch22 Artifact State

1. Matrix should have exactly `35` Batch22 rows:
   - `16` body rows;
   - `19` boundary rows.
2. Current DOCX should have exactly `16` governed `2025丰台期末` headings:
   - Q4 under `实现人生价值`;
   - Q7 under `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`;
   - Q16 under: `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, `主观能动性 / 意识的能动作用`, `价值观的导向作用`, `发展的观点 / 发展的普遍性`, `实践与认识（总）`, `实践是认识的基础`, `整体与部分`, `矛盾的特殊性 / 具体问题具体分析`, `系统观念 / 系统优化`, `联系的普遍性 / 联系的观点（总）`, `规律的客观性`, `认识对实践的反作用`, `量变与质变 / 适度原则`;
   - Q17 under `人民群众`.
3. Ledger and accepted JSONL should each have `16` governed records for this suite.
4. Render evidence should be coherent:
   - `252/252` PDF pages/rendered PNGs;
   - labels `2339/2339`;
   - visible suite headings `16/16`;
   - hit pages `11, 14, 23, 42, 48, 69, 83, 95, 98, 137, 165, 179, 188, 214, 231, 251`;
   - page 2 is the only blank-like page and is the known foreword/divider page.
5. Global raw midterm/final gap should now be `13` suites.

## Checks Required

1. Verify matrix rows, body/boundary counts, and source/artifact evidence labels.
2. Verify Q4 and Q7 are bounded as objective answer-key evidence, not scoring rubrics.
3. Verify Q16 entries are supported by the formal PPT rubric and no principle is invented beyond rubric/teacher source.
4. Verify Q17 imports only the people/history point and keeps political-democracy points out of philosophy nodes.
5. Verify DOCX/ledger/accepted/render counts agree.
6. Identify any required corrections before Batch22 can be treated as locally closed.

## Required Output

Return a concise Markdown result with:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `local_policy_result`: use `pass_with_model_gate_blocked` if content passes but adaptive/max-effort proof remains insufficient
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless fully proven
- `sonnet_haiku_used`: whether any Sonnet/Haiku/model-unknown output is counted as qualified evidence
- `matrix_check`
- `docx_check`
- `render_check`
- `global_scope_check`
- `required_fixes`
- `remaining_project_blockers`
