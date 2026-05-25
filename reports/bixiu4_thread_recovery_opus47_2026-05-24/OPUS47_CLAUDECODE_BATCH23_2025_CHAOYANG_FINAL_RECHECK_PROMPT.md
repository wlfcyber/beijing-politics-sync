# ClaudeCode Opus 4.7 Recheck Prompt - Batch23 2025 Chaoyang Final

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread. You are not a casual reviewer. Recheck the Codex Batch23 work from source evidence and current artifacts.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write or claim final acceptance for the whole project.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. Verify this batch as a production lane.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending` unless actually completed elsewhere.
- If adaptive/max-effort proof cannot be confirmed, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## Files To Inspect

- `BATCH23_2025_CHAOYANG_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH23_2025_CHAOYANG_FINAL_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md`
- `FORMAT_RENDER_QA_20260524.md`
- `word_render_qa_20260525_batch23_word/render_manifest.json`
- `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- Current DOCX/PDF under `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`
- Source caches:
  - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\195324f05d7e2fea_朝阳高三期末2025.md`
  - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\ec82917288aa8774_2025北京朝阳高三_上_期末政治_教师版.md`
  - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\953eaee3f98d8598_2025朝阳期末细则.md`

## Source Facts To Verify

1. Batch23 suite is `2025朝阳期末`.
2. Teacher-version objective answer key is `1C 2D 3B 4C 5D 6A 7A 8B 9A 10D 11A 12C 13B 14D 15A`.
3. Formal rubric PDF cache has no reliable text layer and is `rendered-ocr-needed`; it should not be used as independent text evidence unless visually/OCR checked.
4. PPT scoring source is the usable detailed scoring source for this batch. It contains scoring rules and answer-variation notes, not merely ordinary reference answers.
5. Q2 is objective-choice evidence only: answer D supports `联系的普遍性 / 联系的观点（总）`; not a subjective scoring rubric.
6. Q9 is objective-choice evidence only: answer A supports `系统观念 / 系统优化`; not a subjective scoring rubric.
7. Q16 prompt is cultural dialogue. PPT rubric supports philosophy nodes:
   - `实际/一切从实际出发`;
   - `规律/尊重客观规律/主观能动性`;
   - `联系`;
   - `发展/辩证否定`;
   - `矛盾普遍性与特殊性`;
   - `正确价值判断价值选择/正确价值观`;
   - `人民群众主体地位/群众观点群众路线`.
8. Q16 culture scoring points remain boundary rows, not philosophy-body insertions.
9. Q22 prompt is 马克思主义中国化时代化. PPT rubric supports philosophy nodes:
   - `一切从实际出发/实事求是`;
   - `系统观念`;
   - `守正创新`;
   - `发展的观点`;
   - `问题导向/具体问题具体分析`;
   - `实践观点/理论与实践相结合`;
   - `实践基础上的理论创新`;
   - `以新的理论指导新的实践`;
   - `人民至上/人民立场`.
10. Q22 non-philosophy comprehensive points such as党的领导、两个结合等 remain boundary rows unless already philosophy-scored.
11. Q7's “辩证思维” stays in logic/thinking boundary; it must not be converted into 必修四辩证否定.

## Expected Batch23 Artifact State

1. Matrix should have exactly `41` Batch23 rows:
   - `21` body rows;
   - `20` boundary rows.
2. Current DOCX should have exactly `21` governed `2025朝阳期末` headings:
   - Q2 under `联系的普遍性 / 联系的观点（总）`;
   - Q9 under `系统观念 / 系统优化`;
   - Q16 under: `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, `主观能动性 / 意识的能动作用`, `尊重客观规律与发挥主观能动性相结合`, `规律的客观性`, `联系的普遍性 / 联系的观点（总）`, `发展的观点 / 发展的普遍性`, `辩证否定 / 守正创新`, `矛盾的普遍性和特殊性`, `人民群众`, `价值判断与价值选择`;
   - Q22 under: `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, `系统观念 / 系统优化`, `发展的观点 / 发展的普遍性`, `辩证否定 / 守正创新`, `矛盾的特殊性 / 具体问题具体分析`, `实践与认识（总）`, `实践是认识的基础`, `认识对实践的反作用`, `人民群众`.
3. Ledger and accepted JSONL should each have `21` governed records for this suite.
4. Render evidence should be coherent:
   - `254/254` PDF pages/rendered PNGs;
   - labels `2375/2375`;
   - visible suite headings `21/21`;
   - page 2 is the only blank-like page and is the known foreword/divider page.
5. Global raw midterm/final gap should now be `12` suites.

## Checks Required

1. Verify matrix rows, body/boundary counts, and source/artifact evidence labels.
2. Verify Q2 and Q9 are bounded as objective answer-key evidence, not scoring rubrics.
3. Verify Q16 and Q22 entries are supported by the PPT scoring source and no principle is invented beyond rubric/teacher source.
4. Verify culture, politics, economics, law, logic, and international-politics points are boundary rows where appropriate.
5. Verify DOCX/ledger/accepted/render counts agree.
6. Identify any required corrections before Batch23 can be treated as locally closed.

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
