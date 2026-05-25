# Opus 4.7 ClaudeCode Recheck Prompt - Batch19 2024朝阳期中

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write the forbidden strict-final acceptance status.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. Verify this batch as a production lane, not as a passive reviewer.
- GPTPro web / external Claude Opus review remains `real_call_pending` unless actually completed elsewhere.
- Q17 has a formal scoring-rule line only for an open `哲学2分` add-on. Do not inflate it into point-by-point detailed scoring-rule evidence.

## Base Folder

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

## Files To Inspect

Batch19 artifacts:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch19_2024_chaoyang_midterm_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH19_2024_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH19_2024_CHAOYANG_MIDTERM_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\GOVERNOR_RECOVERY_REPORT_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch19_word\render_manifest.json`
- current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\`

Primary source packet:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\2024各区模拟题__2024各区期中__2024朝阳期中.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\0a50f76fd1e1c50f_202411朝阳高三政治_期中1试题.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\92a268ce852f6944_2024.11期中政治朝阳评标2.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\25b6e8c2207d9d9e_2024朝阳期中细则.md`

## Expected Batch19 Decisions To Verify

1. The RTF answer table is `1B 2D 3D 4C 5A 6C 7B 8D 9B 10D 11C 12C 13C 14A 15B`.
2. Choice entries use only objective-answer evidence plus question text, never subjective scoring-rule evidence:
   - Q1 existing DOCX registration -> `实现人生价值`.
   - Q3 inserted -> `主观能动性 / 意识的能动作用`.
   - Q4 inserted twice -> `系统观念 / 系统优化` and `辩证否定 / 守正创新`.
   - Q5 inserted -> `认识发展原理`.
   - Q10 inserted -> `量变与质变 / 适度原则`.
3. Q16 is registered existing DOCX coverage under four historical-materialism nodes: `社会存在与社会意识`, `社会发展的两大基本规律和基本矛盾`, `改革 / 改革的实质`, `人民群众`; this is supported by formal scoring-rule text.
4. Q17 is registered existing DOCX coverage under five open philosophy add-on nodes: `尊重客观规律与发挥主观能动性相结合`, `辩证否定 / 守正创新`, `矛盾就是对立统一`, `矛盾的特殊性 / 具体问题具体分析`, `价值判断与价值选择`; its evidence is formal rubric support for open philosophy angles only, not point-by-point detailed scoring rules.
5. Q2/Q6 remain culture or non-philosophy boundaries. Q7-Q9/Q11/Q18/Q19 remain Logic and Thinking boundaries. Q12-Q15/Q20 remain economy/international-politics boundaries.
6. Matrix has 28 `2024朝阳期中` rows and 0 open-ish rows, with Q1-Q20 all dispositioned.
7. Ledger and accepted JSONL each gained 15 governed records for this suite.
8. Render manifest should show Word COM PDF export, 250 pages rendered, blank-like body pages `[]`, DOCX/PDF label counts `2316/2316`, and all 15 suite headings located on pages `28,32,82,101,107,114,120,136,192,199,203,205,212,236,249`.
9. Global raw-suite audit should now show remaining midterm/final gap reduced from 17 to 16 suites. This is not final whole-project acceptance.

## Required Output

Write a concise Markdown result with:

- `model_gate`: pass only if you can prove Opus 4.7 max effort/adaptive thinking from runtime evidence; otherwise `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `content_result`: pass / pass_with_notes / fail.
- `sonnet_haiku_used`: must be `no` for qualified evidence.
- `answer_key_check`: whether the key and source are real and sufficient for objective-choice placement only.
- `matrix_check`: whether all Q1-Q20 dispositions and evidence boundaries are coherent.
- `docx_check`: whether current DOCX contains exactly 15 governed `2024朝阳期中` headings with the expected question distribution.
- `render_check`: whether Batch19 render evidence is coherent and new pages render cleanly.
- `global_scope_check`: confirm remaining source-scope gap is still open at 16 suites.
- `required_fixes`: concrete fixes if any.
