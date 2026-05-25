# 外审摘要

- final_docx: 哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx
- final_pdf: 哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf
- accepted_insertions: 36
- blocked_or_skipped: 76

## Accepted By Node
- 系统观念 / 系统优化: 5
- 辩证否定 / 守正创新: 4
- 价值观的导向作用: 4
- 实践是认识的基础: 3
- 矛盾的特殊性 / 具体问题具体分析: 3
- 矛盾就是对立统一: 3
- 量变与质变 / 适度原则: 2
- 尊重客观规律与发挥主观能动性相结合: 2
- 联系的普遍性 / 联系的观点（总）: 2
- 实践与认识（总）: 2
- 物质决定意识: 1
- 发展的观点 / 发展的普遍性: 1
- 主要矛盾和次要矛盾: 1
- 矛盾的普遍性和特殊性: 1
- 人民群众: 1
- 两点论与重点论: 1

## Accepted By Source
- 2026东城二模: 6
- 2026朝阳二模: 6
- 2026丰台二模: 5
- 2026顺义二模: 5
- 2026房山二模: 3
- 2026石景山二模: 3
- 2025海淀一模: 2
- 2026通州一模: 2
- 2026海淀二模: 2
- 2026西城二模: 2

## Blocked By Reason
- already_in_base_exact_source: 44
- weak_evidence: 10
- question_prompt_not_verified: 9
- culture_boundary: 8
- module_boundary: 3
- module_boundary_xuanbisan_logic_thinking: 1
- unsupported_high_risk_term: 1

---

# Current Acceptance Status

# CURRENT_ACCEPTANCE_STATUS_20260524

This file is the current audit entrypoint for the 2026-05-24 philosophy handbook repair run. It supersedes older status blocks that mention 26/38/41 inserted rows, 227/232/234/237 rendered pages, or "GPTPro web pending".

## Current Verdict

Status: `LOCAL_AND_EXTERNAL_CLAUDE_SCOPED_PASS__GPTPRO_WEB_SCOPED_AUDIT_FIXES_APPLIED__FULL_GPTPRO_ARTIFACT_PASS_NOT_CLAIMED`

This is still not a strict final all-model PASS. GPTPro web completed a scoped audit on the pasted review payload, found DELETE/REWRITE/NEED_EVIDENCE items, and Codex has applied the source-verified fixes. A full artifact PASS would require sending the rebuilt complete DOCX/PDF plus current raw evidence package back through the requested external web review gate.

## Counts

| item | current count |
|---|---:|
| accepted student insertions | 36 |
| DOCX insertion ledger rows | 36 |
| rendered PDF pages | 236 |
| coverage matrix suites | 35 |
| open evidence/prompt gates | 0 |
| Desktop source suites detected across 2024-2026 first/second mocks | 47 |
| source suites missing from final DOCX | 0 |

## GPTPro Scoped Audit Fixes

Evidence files:

- `08_external_review/gptpro_web_scoped_audit_20260524.md`
- `04_fusion_audit/gptpro_web_scoped_fixes_applied_20260524.md`
- `04_fusion_audit/weak_evidence_cards_20260524.md`

Applied fixes:

- Removed `2026房山二模 Q18(2) 辩证否定 / 守正创新` from the 必修四正文 because the prompt explicitly points to 《逻辑与思维》.
- Removed `2026西城二模 Q16 价值观的导向作用` from the 必修四正文 because the local scoring source lists `矛盾的普遍性和特殊性、实践、中华优秀传统文化`, not `价值观/价值观导向`.
- Rewrote `2026东城二模 Q16 物质决定意识` so it only covers 一切从实际出发 and does not mix in 主观能动性.
- Rewrote `2026顺义二模 Q16 两点论与重点论` so it no longer mislabels the material as 主次矛盾.
- Rewrote `2026西城二模 Q16 矛盾普遍性和特殊性` around "特殊的中国日常表达承载普遍生活追求".
- Rewrote `2026房山二模 Q16 量变质变` around工匠精度、长期积累、制造能力跃升.
- Marked `2026石景山二模 Q17(3)` as optional philosophy paths, not cumulative scoring points.
- Rewrote all current accepted insertions with material-specific answer landings instead of generic template tails.

## Current Verification

Rebuilt deliverables:

- `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`

Checks completed after rebuild:

- `student_patch_entries.accepted.jsonl`: 36 rows.
- `docx_insert_ledger.csv`: 36 rows.
- `COVERAGE_CLOSURE_MATRIX_V2`: 35/35 suites `COVERED_OR_PATCHED`; no open evidence/prompt gates.
- The rebuilt accepted JSONL and ledger contain 0 rows for `2026房山二模 Q18(2)` and 0 rows for `2026西城二模 Q16 价值观的导向作用`.
- Rebuilt DOCX text contains 0 hits for `NEED_EVIDENCE`, `source_lane`, `2026房山二模 第18(2)题`, `这说明相关主体`, `统筹不同主体、资源和环节`, and `在尊重原有基础和合理价值的同时`.
- Word/PDF export succeeded; rendered page count is 236. Visual QA sampled cover/contact sheet, inserted high-risk pages, and final page with no obvious clipping or layout break.

## Dual-Lane And Review Evidence

Codex lane:

- `02_codex_lane/agents/codex_a_independent_coverage_rerun_20260524.md`
- `04_fusion_audit/gptpro_web_scoped_fixes_applied_20260524.md`

ClaudeCode lane:

- `03_claudecode_lane/claudecode_b_full_coverage_rerun_20260524.md`
- `03_claudecode_lane/claudecode_after_fix_recheck_20260524.md`
- `03_claudecode_lane/claudecode_verify_haidian_choice_addendum_20260524.md`
- `03_claudecode_lane/claudecode_verify_gptpro_web_fixes_20260524.md`
- `03_claudecode_lane/claudecode_verify_batch03_cleanup_20260524.md`

Latest ClaudeCode narrow recheck:

- First recheck returned `SCOPED_PASS_WITH_NOTES`: all content fixes passed, but `batch_03_summary_and_gate.md` still contained stale current-state count assertions.
- After cleaning `batch_03`, follow-up recheck returned `SCOPED_PASS`: active state is 36 accepted rows, 36 ledger rows, 236 PDF pages; old counts are no longer presented as current state; full artifact PASS is still not claimed.

External Claude:

- `08_external_review/claude_external_review_final_delta_20260524.md`

GPTPro web:

- `08_external_review/gptpro_web_scoped_audit_20260524.md`

Next required gate:

- If strict final all-model PASS is required, send the rebuilt complete DOCX/PDF and refreshed package through GPTPro web again.

## Boundary

The local suite-level closure matrix now shows no open evidence gates, but this file deliberately does not claim "全书最终 PASS". The current honest state is: source-verified GPTPro scoped fixes are applied, local rebuild/verification passed, and the next audit gate is ClaudeCode recheck of those fixes plus optional full-artifact GPTPro web review.


---

# GPTPro Web Scoped Audit

The full GPTPro scoped audit is attached separately as `gptpro_web_scoped_audit_20260524.md`. Its DELETE/REWRITE/NEED_EVIDENCE findings have been routed through local source verification and applied in `gptpro_web_scoped_fixes_applied_20260524.md`. This summary file intentionally does not inline the old GPTPro report table, because that table quotes superseded historical counts.


---

# GPTPro Fixes Applied

# GPTPro web scoped audit fixes applied 2026-05-24

Status: `SCOPED_FIX_APPLIED_NOT_FINAL_PASS`.

- accepted backup: `student_patch_entries.accepted.backup_before_gptpro_web_scoped_fixes_20260524_215523.jsonl`
- blocked backup: `student_patch_entries.blocked.backup_before_gptpro_web_scoped_fixes_20260524_215523.jsonl`
- accepted rows before: 36
- accepted rows after: 36
- moved/deleted from student正文 in this run: 0
- moved/deleted from student正文 cumulative current state: 2
- rewritten student rows: 36

## Deleted From Student Body

- 2026房山二模 Q18(2) `辩证否定 / 守正创新`
- 2026西城二模 Q16 `价值观的导向作用`

## Main Fixes

- 删除 `2026房山二模 Q18(2) 辩证否定 / 守正创新`：题干点名《逻辑与思维》，属于选必三边界。
- 删除 `2026西城二模 Q16 价值观的导向作用`：本地回查评标原文未点名价值观，按高风险术语规则撤正文。
- 重写 `2026东城二模 Q16 物质决定意识`：只保留一切从实际出发，不再混入主观能动性。
- 重写 `2026顺义二模 Q16 两点论与重点论`：不再写“主要矛盾和次要矛盾”，落到多样与主流、社会效益优先。
- 重写 `2026西城二模 Q16 矛盾普遍性和特殊性`：从“中国式日常特殊表达”落到“跨文化普遍生活追求”。
- 重写 `2026房山二模 Q16 量变质变`：从工匠精度、长期积累、制造能力跃升解释，不再沿用规划题模板。
- 为 `2026石景山二模 Q17(3)` 三条可选哲学路径加入边界句，避免被误读为三项累计得分。
- 批量去掉新增条目的模板化尾句，改为本题可直接写进卷面的材料化答案句。

## Evidence Cards

- `weak_evidence_cards_20260524.md` 已补海淀、西城、顺义、石景山四套外审证据卡。

## Gate

本补丁只处理 GPTPro scoped audit 已指出或本地回查新发现的问题；它不等于全书外部 final PASS。


---

# Weak Evidence Cards

# 弱证据门槛回源证据卡 2026-05-24

本文件服务外审与 Governor，不进入学生版正文。它只补外审所需的“原题设问、材料关键词、评分/评标原文、对应新增条目”。

## 2026海淀二模 Q16

- 设问：从哲学角度，谈谈为什么要把读“有字之书”和读“无字之书”结合起来。
- 材料关键词：“有字之书”承载经典学说、系统知识、文明智慧；“无字之书”镌刻于广袤大地，蕴藏于社会万象。
- 评分/评标原文：`16.（8分）可从联系、实践与认识等角度作答。`
- 证据位置：`01_source_inventory/suite_source_bundles/2026海淀二模_Q16_readable_evidence.md`；同源 `2026海淀二模.md` lines 1092-1094, 1140-1141, 1162-1163。
- 对应正文条目：`联系的普遍性 / 联系的观点（总）`、`实践与认识（总）`。
- 边界：早期独立矛盾条已撤；`2026海淀二模 Q21 统筹方法 9分题`保留 future candidate，不进本轮宝典正文。

## 2026西城二模 Q16

- 设问：从哲学角度，分析中式生活方式实现全球共鸣的原因。
- 材料关键词：全球青年体验喝热水、八段锦、节气起居、和睦共居；中式日常生活方式承载健康、和谐、身心平衡等共同生活追求。
- 评分/评标原文：`16.（6分）可从矛盾的普遍性和特殊性、实践、中华优秀传统文化等角度作答。`
- 证据位置：`01_source_inventory/suite_source_bundles/2026西城二模.md` lines 131-133, 172。
- 对应正文条目：`矛盾的普遍性和特殊性`、`实践是认识的基础`。
- 边界：本地检索未见“价值观/价值观导向”作为 Q16 评分角度；原 `价值观的导向作用` 条已按高风险术语规则撤出正文。

## 2026顺义二模 Q16

- 设问对象：新大众文艺。
- 评分/评标原文：`（8分）可从实践观点、人民主体、价值观、矛盾观、中华优秀传统文化等角度作答。`
- 阅卷版关键原文：尊重多样性与弘扬主流价值：对立统一、守正创新；人民群众是文化创造的主体；价值观对认识世界和改造世界具有导向作用；矛盾具有普遍性和特殊性，要坚持两点论与重点论统一；继承传统，推陈出新。
- 证据位置：`01_source_inventory/suite_source_bundles/2026顺义二模.md` line 23。
- 对应正文条目：`人民群众`、`价值观的导向作用`、`两点论与重点论`、`实践是认识的基础`、`辩证否定 / 守正创新`。
- 边界：`两点论与重点论`条不得写成“主要矛盾和次要矛盾”；本轮已按 GPTPro 意见重写。

## 2026石景山二模 Q17(3)

- 设问对象：概括“良法”和“善治”的关联并结合材料分析。
- 材料关键词：养老立法把实践经验固化为地方性法规；“良法”只是起点，“善治”才是目标；养老服务最终落实到治理效能。
- 评分/评标原文：`（3）正确使用1个哲学观点概括二者关系，可得1分；运用1个哲学观点进行正确分析，可得2-4分；能够在分析中，结合必修3相关内容做综合表达，可得5-6分。可从联系、矛盾、实践与认识关系等角度回答。（7分）`
- 证据位置：`01_source_inventory/suite_source_bundles/2026石景山二模.md` lines 145-148；`99_logs/weak_gate_sources/石景山区高三政治第二次模拟考试答案评分细则(1).txt`。
- 对应正文条目：`联系的普遍性 / 联系的观点（总）`、`矛盾就是对立统一`、`实践与认识（总）`。
- 边界：这三条是任选哲学路径，不是三项累计采分点；本轮已在 why/boundary 中显式加边界句。


---

# COVERAGE_CLOSURE_MATRIX_V2

This is a suite-level closure matrix for the 35 source suites in this run. It is a governor aid, not a final PASS.

External-review packet note: direct source bundles are attached for the touched or weak-evidence suites in this repair batch; other suites rely on the accepted base baodian coverage and the lane closure records, not on a full re-upload of all 35 source bundles.

## Status Counts

- COVERED_OR_PATCHED: 35

## Open Evidence Or Prompt Gates

- none

## Reading Rule

- `COVERED_OR_PATCHED`: suite appears in final DOCX or has accepted/base-covered evidence.
- `BOUNDARY_EXCLUDED`: only module/culture boundary items remain.
- `OPEN_EVIDENCE_OR_PROMPT_GATE`: unrepaired weak evidence or missing prompt remains; do not sign final PASS.
- `NO_FINAL_ARTIFACT_EVIDENCE`: no final artifact evidence was found at suite level.


---

﻿# Full Source vs DOCX Coverage Audit 2026-05-24

Final DOCX: C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx

## Summary

| item | count |
|---|---:|
| raw source suites detected from Desktop 2024-2026 first/second mock folders | 47 |
| suites present in final DOCX and current closure matrix | 35 |
| suites present in final DOCX and inherited-base row-level rechecked | 12 |
| suites missing from final DOCX | 0 |

## Inherited Row-Level Sync

- Synced after inherited second-mock row-level recheck: 12 suite rows updated from `not reopened` to `row-level rechecked scoped pass`.
- Detailed evidence: `INHERITED_2024_2025_SECOND_MOCK_ROW_EXTRACT_20260524.csv`, `haidian_2025_second_mock_evidence_closeout_20260524.md`, and ClaudeCode recheck outputs.

## Boundary

- This audit proves suite-name coverage in the final DOCX against the current Desktop source folders.
- The 12 inherited 2024/2025 second-mock suites were later row-level extracted and rechecked: 135 rows, 0 thin material/why/answer fields after patching, with ClaudeCode scoped PASS and the Haidian Q10/Q11 choice-only boundary preserved.
- The 2024-2026 first-mock plus 2026 second-mock delta closure is still governed by `COVERAGE_CLOSURE_MATRIX_V2.csv`.

## Suites

| suite | final_docx_mentions | current_closure_status | coverage_bucket | source_example |
|---|---:|---|---|---|
| 2024朝阳二模 | 12 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2024各区二模\2024朝阳二模\其他材料\004202405朝阳高三政治质量检测二参考答案（以PDF为准）.docx |
| 2024朝阳一模 | 5 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2024各区一模\2024朝阳一模\其他材料\202404朝阳高三政治一模试卷讲评.pptx |
| 2024东城二模 | 13 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2024各区二模\2024东城二模\其他材料\002北京市东城区2023-2024学年度第二学期高三综合练习（二）思想政治答案.pdf |
| 2024东城一模 | 8 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2024各区一模\2024东城一模\其他材料\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治答案(1).pdf |
| 2024丰台二模 | 5 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2024各区二模\2024丰台二模\细则\2024丰台二模细则.docx |
| 2024丰台一模 | 6 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2024各区一模\2024丰台一模\细则\2024丰台一模细则.docx |
| 2024海淀二模 | 9 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2024各区二模\2024海淀二模\其他材料\高三二模：政治答案(2).docx |
| 2024海淀一模 | 10 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2024各区一模\2024海淀一模\其他材料\一模政治-答案.docx |
| 2024石景山一模 | 4 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2024各区一模\2024石景山一模\其他材料\2024年石景山一模.pptx |
| 2024顺义二模 | 10 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2024各区二模\2024顺义思政二模\细则\2024顺义思政二模细则.docx |
| 2024西城二模 | 10 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2024各区二模\2024西城二模\其他材料\~$模拟测试思想政治试卷.docx |
| 2024西城一模 | 11 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2024各区一模\2024西城一模\其他材料\2024.4高三统一测试思想政治答案.docx |
| 2025昌平二模 | 10 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2025各区二模\2025昌平二模\细则\2025昌平二模细则.pptx |
| 2025朝阳二模 | 19 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2025各区二模\2025朝阳二模\其他材料\扫描全能王 2025-05-13 21.42.pdf |
| 2025朝阳一模 | 7 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025朝阳一模\其他材料\20250329高3阅卷总结17 1题 具身智能 任会波组 阐释论证.doc |
| 2025东城二模 | 13 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2025各区二模\2025东城二模\细则\2025东城二模细则.pdf |
| 2025东城一模 | 11 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025东城一模\细则\2025东城一模细则.pdf |
| 2025房山一模 | 9 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025房山一模\细则\2025房山一模细则.pdf |
| 2025丰台二模 | 11 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2025各区二模\2025丰台二模\细则\2025丰台二模细则\2025丰台二模评标细则\16.(1).doc |
| 2025丰台一模 | 10 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025丰台一模\细则\2025丰台一模细则.docx |
| 2025海淀二模 | 8 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2025各区二模\2025海淀二模\其他材料\2025届二模考试讲评0510.pdf |
| 2025海淀一模 | 10 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025海淀一模\其他材料\EDU_1500334100000021014_61af1789-0742-472d-86cd-e6cb420b0ecb.pdf |
| 2025门头沟一模 | 10 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025门头沟一模\细则\2025门头沟一模细则.doc |
| 2025石景山一模 | 7 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025石景山一模\细则\2025石景山一模细则.doc |
| 2025顺义一模 | 9 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025顺义一模\细则\2025顺义一模细则.docx |
| 2025西城二模 | 13 | INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS | DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx |
| 2025西城一模 | 11 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025西城一模\细则\2025西城一模细则.docx |
| 2025延庆一模 | 9 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2025各区一模\2025延庆一模\细则\2025延庆一模细则.docx |
| 2026朝阳二模 | 6 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026朝阳二模\细则\202605朝阳高三政治二模阅卷细则(1).docx |
| 2026朝阳一模 | 9 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026朝阳一模\2026北京朝阳高三一模政治（教师版）.pdf |
| 2026东城二模 | 6 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026东城二模\细则\16.pdf |
| 2026东城一模 | 12 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026东城一模\2026东城一模 原卷扫描版.pdf |
| 2026房山二模 | 4 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026房山二模\细则\26房山评标(2).docx |
| 2026房山一模 | 9 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026房山一模\2026北京房山高三一模政治.pdf |
| 2026丰台二模 | 5 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026丰台二模\细则\2026丰台区二模主观题阅卷细则(1).pptx |
| 2026丰台一模 | 11 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026丰台一模\26 丰台一模政治(1).pptx |
| 2026海淀二模 | 2 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026海淀二模\细则\26海淀高三政治二模讲评.pdf |
| 2026海淀一模 | 6 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026海淀一模\2026海淀一模 试卷扫描版_去水印.pdf |
| 2026门头沟一模 | 9 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026门头沟一模\门头沟区高三政治一模试卷.pdf |
| 2026石景山二模 | 3 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026石景山二模\细则\石景山区高三政治第二次模拟考试答案评分细则(1).doc |
| 2026石景山一模 | 8 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026石景山一模\2026北京石景山高三一模政治（教师版）.pdf |
| 2026顺义二模 | 5 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026顺义二模\26顺义二模(1).pdf |
| 2026顺义一模 | 11 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026顺义一模\2026年顺义一模  细则.pptx |
| 2026通州一模 | 2 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026通州一模\2026北京通州高三一模政治.pdf |
| 2026西城二模 | 3 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区二模\2026西城二模\细则\西城二模评标.pdf |
| 2026西城一模 | 12 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026西城一模\2026北京西城高三一模政治.pdf |
| 2026延庆一模 | 12 | COVERED_OR_PATCHED | DELTA_OR_FIRST_MOCK_MATRIX_CLOSED | 2026各区一模\2026延庆一模\2026北京延庆高三一模政治（教师版）.pdf |


---

# Historical Worker Files Boundary

The upload packet may include older lane reports for traceability. They are superseded by `CURRENT_ACCEPTANCE_STATUS_20260524.md` and `gptpro_web_scoped_fixes_applied_20260524.md` wherever counts or kept/deleted rows differ. The current active counts are 36 accepted rows, 36 ledger rows, and 236 PDF pages.


---

# Source Evidence Index


## Source Evidence

- source_evidence/99_logs/tongzhou_paper_pages/contact.png
- source_evidence/99_logs/tongzhou_paper_pages/page_01.png
- source_evidence/99_logs/tongzhou_paper_pages/page_02.png
- source_evidence/99_logs/tongzhou_paper_pages/page_03.png
- source_evidence/99_logs/tongzhou_paper_pages/page_04.png
- source_evidence/99_logs/tongzhou_paper_pages/page_05.png
- source_evidence/99_logs/tongzhou_paper_pages/page_06.png
- source_evidence/99_logs/tongzhou_paper_pages/page_07.png
- source_evidence/99_logs/tongzhou_paper_pages/page_08.png
- source_evidence/99_logs/tongzhou_paper_pages/page_09.png
- source_evidence/99_logs/tongzhou_paper_pages/page_10.png
- source_evidence/99_logs/weak_gate_sources/26顺义二模评标.txt
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/contact.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_001.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_002.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_003.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_004.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_005.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_006.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_007.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_008.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_009.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_010.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_011.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_012.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_013.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_014.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_015.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_016.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_017.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_018.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_019.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_020.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_021.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_022.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_023.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_024.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_025.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_026.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_027.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_028.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_029.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_030.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_031.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_032.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_033.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_034.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_035.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_036.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/contact.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_001.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_002.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_003.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_004.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_005.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_006.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_007.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_008.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_009.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_010.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_011.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_012.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_013.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_014.png
- source_evidence/99_logs/weak_gate_sources/石景山区高三政治第二次模拟考试答案评分细则(1).txt
- source_evidence/second_mock_candidate_entries.csv
- source_evidence/suite_source_bundles/2025海淀一模.md
- source_evidence/suite_source_bundles/2026东城二模.md
- source_evidence/suite_source_bundles/2026丰台二模.md
- source_evidence/suite_source_bundles/2026房山二模.md
- source_evidence/suite_source_bundles/2026朝阳二模.md
- source_evidence/suite_source_bundles/2026海淀二模.md
- source_evidence/suite_source_bundles/2026海淀二模_Q16_readable_evidence.md
- source_evidence/suite_source_bundles/2026石景山二模.md
- source_evidence/suite_source_bundles/2026西城二模.md
- source_evidence/suite_source_bundles/2026通州一模.md
- source_evidence/suite_source_bundles/2026顺义二模.md