# ClaudeCode Visible Review Prompt: Phase12 Batch01

Use a real visible ClaudeCode/Claude window only if available; otherwise keep this as pending.

Task: audit Phase12 Batch01 repair readiness. Do not generate Word/PDF/final.

Read:
- `05_coverage/phase12_next_repair_batch01.csv`
- `05_coverage/phase12_74row_expansion_decision_matrix.csv`
- `00_飞哥选必三逻辑与思维硬性要求记事本.md`

For each row, verify whether the source locator and answer locator are enough for正文 expansion. For reasoning rows, identify logical form, valid/invalid rule, student rule口诀, and wrong-option trap. Output a CSV and MD report under `claudecode_lane/phase12_batch01_visible_review/`.

Hard rule: no guessing answers, no Word/PDF/final, no calling the 29-row packet final.
