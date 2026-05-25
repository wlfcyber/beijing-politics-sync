# ClaudeCode Opus 4.7 Batch10 Recheck Prompt

You are the ClaudeCode production-line reviewer for the 必修四政治庄园 recovery thread.

Required model gate:
- This run must use `claude-opus-4-7` with max effort / adaptive thinking.
- Do not treat Sonnet, Haiku, or model-unknown output as qualified evidence.
- If runtime evidence cannot prove max effort / adaptive thinking, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Ordinary reference answers cannot be promoted into scoring rules. Use official answer keys, scoring standards, marking rules, and explicit source evidence.

Workspace root:
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Recovery directory:
`reports\bixiu4_thread_recovery_opus47_2026-05-24`

Primary files to inspect:
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH10_2025_HAIDIAN_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch10_2025_haidian_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2025海淀一模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery`
- Rendered pages under `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch10_word`

Review tasks:
1. Verify Q1-Q22 for `2025海淀一模` against the source bundle and official answer/scoring reference, not against Codex summaries alone.
2. Confirm new insertions:
   - Q2 -> `尊重客观规律与发挥主观能动性相结合`, using official answer D and correct item ④: “主动作为与敬畏自然相统一”. Correct item ③ is culture-line and must not be used as this philosophy-node proof.
   - Q5 -> `矛盾就是对立统一`, using official answer C and correct item ④: “运用矛盾运动的观点，以动态的方式思考生态产品价值”. Item ② is a condition-relation judgment and must not be used as this philosophy-node proof.
3. Confirm existing coverage / recitation:
   - Q16 is already covered under contradiction analysis / practice-recognition / value nodes. Its official scoring standard is only angle-level support: “可从矛盾分析法、实践与认识的关系、价值观等角度作答.” Do not upgrade this to point-by-point detailed rubric.
   - Q22 is already covered under `系统观念 / 系统优化` and `主要矛盾和次要矛盾`. Formal scoring requires “系统观念” and source text explicitly includes 全局和局部、主要矛盾和次要矛盾、特殊和一般.
   - Rows that had Q21 but actually refer to Q22 were corrected to Q22. Real Q21 is a logic + international trade boundary row.
4. Confirm excluded or boundary rows are source-defensible:
   - Q1, Q3, Q4, Q6-Q15, Q17-Q21, and Qunknown.
   - Confirm added rows Q10, Q11, Q13, and Q21 are reasonable boundary closures.
5. Confirm `2025海淀一模` has zero exact-source rows still needing placement/fusion adjudication in the matrix.
6. Confirm current render gate:
   - PDF page count is 239.
   - `page-*.png` count is 239.
   - No blank rendered body pages.
   - Full-document label count is DOCX/PDF `2200 / 2200`.
   - New Q2 is visible in the PDF around page 37.
   - New Q5 is visible in the PDF around page 125.

Write your result to:
`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH10_2025_HAIDIAN_YIMO_RECHECK_RESULT.md`

Required result format:
- `Decision: pass_with_model_gate_blocked`, `pass`, or `fail`.
- `Model evidence:` include runtime evidence you can inspect. If max effort / adaptive thinking is not machine-confirmable, state `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `Source findings:` row-level findings, especially Q2, Q5, Q16, Q22, corrected Q21/Q22 rows, and excluded Q17-Q21.
- `Required corrections:` list exact files/rows if any correction is needed.
- `Residual blockers:` include GPTPro/Claude external full-artifact review as `real_call_pending` if not completed.
