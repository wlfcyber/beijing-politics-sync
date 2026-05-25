# ClaudeCode narrow recheck prompt: GPTPro scoped audit fixes

You are ClaudeCode lane B for 飞哥政治庄园-必修四 philosophy handbook. Do not act as a polite reviewer; act as an independent source/evidence auditor.

Working directory:

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Run directory:

`reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24`

Files to inspect:

- `08_external_review/gptpro_web_scoped_audit_20260524.md`
- `04_fusion_audit/gptpro_web_scoped_fixes_applied_20260524.md`
- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- `04_fusion_audit/student_patch_entries.blocked.jsonl`
- `04_fusion_audit/weak_evidence_cards_20260524.md`
- `05_delivery/docx_insert_ledger.csv`
- `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `06_governor_confucius/CURRENT_ACCEPTANCE_STATUS_20260524.md`
- `06_governor_confucius/COVERAGE_CLOSURE_MATRIX_V2.md`
- `08_external_review/batch_03_summary_and_gate.md`

Hard checks:

1. Confirm `2026房山二模 Q18(2) 辩证否定 / 守正创新` is no longer in accepted JSONL or ledger and is only in blocked with a module-boundary reason.
2. Confirm `2026西城二模 Q16 价值观的导向作用` is no longer in accepted JSONL or ledger and is only in blocked with an unsupported-high-risk-term reason.
3. Check `2026东城二模 Q16 物质决定意识`: it must not mix in 主观能动性 as a second principle.
4. Check `2026顺义二模 Q16 两点论与重点论`: it must not call this 主次矛盾.
5. Check `2026西城二模 Q16 矛盾普遍性和特殊性`: it must land on 特殊的中国生活表达 + 普遍生活追求, not generic 具体问题具体分析.
6. Check `2026房山二模 Q16 量变质变`: it must use 工匠精度/长期积累/制造能力跃升, not a planning-template tail.
7. Check `2026石景山二模 Q17(3)`: the three philosophy paths must be explicitly marked as optional paths, not cumulative scoring points.
8. Check new answer landings are not obviously thin or generic. Fail if they still rely on tails like `这说明相关主体...`, `统筹不同主体、资源和环节`, `在尊重原有基础和合理价值的同时`, or `在真实情境和具体行动中...`.
9. Check `batch_03_summary_and_gate.md` no longer mixes old counts like 26/38/41 accepted rows or PDF 227/232/234/237 pages as current state. The current state should be 36 accepted rows and 236 PDF pages.
10. Do not sign all-model final PASS unless the evidence supports it. The expected correct boundary is scoped recheck only.

Output format:

- Start with one line: `SCOPED_PASS`, `SCOPED_PASS_WITH_NOTES`, or `NOT_PASS`.
- Then a concise table with columns: `severity`, `location`, `finding`, `required_fix`.
- Use `PASS` only for checked items that passed.
- Use `REWRITE`, `DELETE`, or `NEED_EVIDENCE` for any remaining problem.
- End with a one-paragraph boundary statement explaining whether this can or cannot be called final all-model PASS.
