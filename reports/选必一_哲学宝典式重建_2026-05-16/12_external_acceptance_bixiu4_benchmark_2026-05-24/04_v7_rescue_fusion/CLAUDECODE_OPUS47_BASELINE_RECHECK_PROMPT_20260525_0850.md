# ClaudeCode Opus 4.7 Baseline Recheck Prompt (2026-05-25 08:50)

You are ClaudeCode production lane B for the user's Beijing Gaokao politics 选必一 handbook project.

This is not the Claude Desktop app final review. Do not claim to satisfy the app-side Opus Adaptive gate. Your job is to perform a fresh production-lane baseline recheck on the current locked Markdown final.

## Required Role

- Treat ClaudeCode as independent production lane B, not as a mere reviewer.
- Compare the current FINAL against the recorded ClaudeCode production evidence and the user's hard rules.
- Do not edit the final file directly in this pass.
- Give a hard verdict and a directly actionable list.

## Files To Read

Current locked final:

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/04_v7_rescue_fusion/选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md`

Current status / root-cause logs:

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/04_v7_rescue_fusion/FINAL_GATE_STATUS_AFTER_GPT_CLEANUP_20260525.md`

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/04_v7_rescue_fusion/EXTERNAL_GATE_ROOT_CAUSE_AND_RECOVERY_20260525_0845.md`

Workflow correction:

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/00_control/WORKFLOW_CORRECTION_20260524_APP_CLAUDE_AND_DUAL_PRODUCTION.md`

ClaudeCode production status:

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/00_control/CLAUDECODE_PRODUCTION_LANE_STATUS_20260524.md`

If needed, sample or consult:

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/02_gptpro_web/primary_fusion_remediation_packet_20260524/06_CLAUDECODE_PRODUCTION_BATCHES_COMBINED.md`

`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/02_gptpro_web/primary_fusion_remediation_packet_20260524/05_CODEX_PRODUCTION_BATCHES_COMBINED.md`

## User Hard Rules To Enforce

1. Cover all 2024-2026 Beijing district mock subjective questions involving 选必一.
2. Do not merge two distinct questions into one example. More examples are required so students build memory through cases.
3. Keep frequency counts in the final.
4. Six buckets: 时代背景、理论、经济全球化、政治多极化、中国、联合国.
5. “合作共赢的新型国际关系” belongs to 政治多极化 unless a specific economic/China context requires another bucket.
6. “独立自主和平外交 / 和平共处五项原则” belongs to 中国.
7. Economic globalization terms must be expression-sensitive. Do not merge terms merely because their essence is similar.
8. Student-facing final must not contain backend audit language such as 细则、评标、评分、参考答案、PASS、FAIL、GPT、Claude、Codex as student content.

## Output Format

Return:

1. `VERDICT`: choose exactly one:
   - `LOCAL_BASELINE_OK_EXTERNAL_GATES_PENDING`
   - `FAIL_MUST_PATCH_CONTENT`
   - `FAIL_WORKFLOW_CHAIN`
2. `content_counts_checked`: report core points, question headings, and any mixed-question heading candidates you found.
3. `claudecode_absorption`: whether the current final appears to have absorbed the ClaudeCode thick production lane sufficiently for a local baseline, and what evidence supports or weakens that.
4. `high_risk_findings`: list concrete findings with file locations or heading names. If none, say none.
5. `must_patch_now`: exact text-level or structural patches needed before external GPT/Claude app gates.
6. `external_gate_status`: state clearly that GPT Pro full-file final review and Claude Desktop Opus Adaptive app review remain pending unless the files prove otherwise.
7. `allowed_user_claim`: one paragraph, honest and bounded.
