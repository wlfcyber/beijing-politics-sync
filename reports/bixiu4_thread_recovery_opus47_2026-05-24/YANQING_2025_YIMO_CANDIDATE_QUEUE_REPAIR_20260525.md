# 2025延庆一模候选队列修复记录

- Status: `YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIRED`.
- Current DOCX: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`.
- DOCX backup before removal: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24_backup_before_2025_yanqing_q18_xuanbisan_removal_20260525_140931.docx`.
- Matrix backup before rewrite: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_2025_yanqing_yimo_candidate_repair_20260525_140935.csv`.
- Source bundle: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\2025各区模拟题__2025各区一模__2025延庆一模.md`.

## DOCX 正文边界修复

- Q18 headings before repair: `2`.
- Q18 removed paragraph count: `12`.
- Q18 headings after repair: `0`.
- Adjudication: Q18 is excluded because the question explicitly asks for 《逻辑与思维》/辩证思维; it is an 选必三 boundary item, not a 必修四 philosophy/culture body item.
- Q21 current context record: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\CURRENT_DOCX_2025_YANQING_Q21_CONTEXT_20260525.md`.

## Matrix 修复范围

- Rows changed: `30`.
- Q1-Q15: closed as choice-question answer-key/term-hit boundary, non-body.
- Q16: retained as current-DOCX coverage supported by formal Q16 scoring rules, with no duplicate insertion.
- Q17: excluded as politics/law-making module boundary.
- Q18: excluded and removed from current DOCX as 选必三 boundary.
- Q19: excluded as law/dispute module boundary.
- Q20: excluded as economics/international module boundary.
- Q21: retained only for Bixiu4-relevant scoring points: 人民群众、社会主义核心价值观、民族精神/文化自信.
- SUITE_LEVEL rows: downgraded to index-only after row-level review.

## Remaining Boundaries

- This is a local source-and-DOCX repair, not an external-model acceptance.
- GPTPro web external review remains `real_call_pending`.
- Claude Opus web/app external review remains `real_call_pending`; direct `https://claude.ai` auto-login path is the required retry route.
- ClaudeCode post-repair evidence remains subject to `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until model confirmation is clean.
- No GitHub push was attempted; final upload is deferred under ORDER_063 after all active Beijing politics lines reach terminal state.

## False Pending Wording Cleanup

- Cleaned Q16/Qunknown note wording rows: `8`.
- Remaining Yanqing open-risk wording after cleanup: `0` by this local wording check.
