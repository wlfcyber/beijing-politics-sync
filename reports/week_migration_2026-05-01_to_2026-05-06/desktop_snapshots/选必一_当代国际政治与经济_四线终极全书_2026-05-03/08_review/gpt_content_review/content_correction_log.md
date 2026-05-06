# Content Correction Log

| issue_id | artifact | location | severity | gpt_claim | proposed_correction | local_evidence_check_needed | local_check_result | codex_decision | patch_status | affects_student_doc | verified_closed_at |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-SB-001 | section_batch | all merged terms | must_fix_content | 多题合并后只有一个答案句 | add 总公式 plus 分题卷面句 | yes | pending | accepted_as_student_refactor_task | open | yes |  |
| GPT-SB-002 | section_batch | 时代主题 | must_fix_content | 2025海淀期中 Q21(2) source chain is incomplete in draft | add matched prompt/answer variant or remove source | yes | pending | accepted_local_check_required | open | yes |  |
| GPT-SB-003 | section_batch | 时代主题 trigger | must_fix_content | trigger is too broad | split strong and weak triggers | no | structure issue | accepted | open | yes |  |
| GPT-SB-004 | section_batch | Q17 relation items | must_fix_content | relation-type templates are mixed into general theory | split into relation-question template section | no | structure issue | accepted | open | yes |  |
| GPT-SB-005 | section_batch | high-information titles | must_fix_content | some core names are too short | restore high-information titles | yes | partly verified in fusion rules | accepted | in_progress | yes |  |
| GPT-SB-006 | section_batch | 2025海淀期中 Q16(2) | must_fix_content | IP/compliance risk is over-promoted to trade friction/international organization mechanism | split compliance/IP risk from trade friction/rule dispute | yes | pending | accepted_local_check_required | open | yes |  |
| GPT-SB-007 | section_batch | 新型国际关系 | must_fix_content | lacks China-diplomacy attribute | add main/cross bucket note | no | structure issue | accepted | open | yes |  |
| GPT-SB-008 | section_batch | 联合国三大支柱 | must_fix_content | wording may be wrong | locally verify and correct before student release | yes | pending | accepted_local_check_required | open | yes |  |
| GPT-SB-009 | section_batch | final student structure | should_fix_transfer | pure six-bucket body is not enough | convert to 按题视图 + 六桶索引 plus whole-question answers | no | structure issue | accepted | open | yes |  |
| GPT-BQ-001 | by_question_preview | 2026顺义一模 Q20 / bridge 和平与发展 | must_fix_content | bridge lists 顺义 under 和平与发展 but by-question answer omits it | include as by-question point if local evidence supports, otherwise downgrade bridge | yes | local worker Batch02 supports formal scoring PPT inclusion | accepted | patched_pending_regate | yes |  |
| GPT-BQ-002 | by_question_preview | 2025海淀期中 Q21(2) | must_fix_content | current era-background wording may flatten historical stages | stage-aware wording for 外交之变 | yes | local image8 supports world-change scoring but student wording needs narrower stage framing | accepted | patched_pending_regate | yes |  |
| GPT-BQ-003 | by_question_preview | 2025海淀期中 Q16(2) | must_fix_content | subject boundary and bucket are unstable | split enterprise / industry / government actions; main bucket 经济全球化 | yes | local fusion ATOM-B14 bucket is 经济全球化 | accepted | patched_pending_regate | yes |  |
| GPT-BQ-004 | by_question_preview | 2026西城期末 Q20 | must_fix_content | D05 concept stacking and UN wording risk | reduce answer-card concept density; tie UN role to climate-governance context | yes | local visual scoring supports D05 same-slot group and D08 UN role | accepted | patched_pending_regate | yes |  |
| GPT-BQ-005 | by_question_preview | 2025海淀二模 Q21 / bridge 新型国际关系 | must_fix_content | bridge and by-question view mismatch | add as optional expression or remove from bridge | yes | local worker Batch02 supports optional expression in 联合国需要中国 contribution line | accepted | patched_pending_regate | yes |  |
| GPT-BQ-006 | by_question_preview | 2024东城一模 Q16/Q20; 2025海淀期末 Q22 | must_fix_content | boundary/open/comprehensive questions sit peer-level with main 选必一 questions | move or label as 拓展迁移 / 可用片段 | no | structure/boundary issue | accepted | patched_pending_regate | yes |  |
| GPT-BQ-007 | by_question_preview | bridge 中国全球治理理念与价值取向 | must_fix_content | concept group is too broad for direct memorization | split main expressions and backup variants in student bridge | yes | local D05 says same-slot variants, not separate frequency points | accepted | patched_pending_regate | yes |  |
| CL-BQ-001 | by_question_preview | 2026朝阳期中 Q17 | must_fix_transfer | answer card drops 两个市场两种资源 | add phrase to answer-card sentence | yes | local Q17 scoring supports expression | accepted | patched_pending_regate | yes |  |
| CL-BQ-002 | by_question_preview | 2026通州期末 Q20 | should_fix_transfer | phrase 中国提出全球治理公共产品 is unnatural | rewrite as China contributes the initiative as an international public good | no | wording issue | accepted | patched_pending_regate | yes |  |

> Closure note, 2026-05-04 02:20 CST: the table above preserves the original live blocker states for audit history. Current release status is no-open-blocker after the local P0 patches, final Markdown targeted GPT regate, Claude targeted regate, Patcher/Governor/Confucius final regates, and the separate GPT `word_pdf` gate. Current closure records are `final_markdown_correction_log_20260504.md`, `final_markdown_targeted_regate_response_20260504.md`, and `word_pdf_correction_log_20260504.md`.

## 2026-05-03 Confucius Follow-Up

- First regate after the external by-question patch: Patcher `PASS`, Governor `PASS_WITH_GUARD`, Automation non-blocking `WARN`, Confucius `PASS_WITH_FIXES`.
- Local follow-up patch applied to student preview files for three student-transfer risks: 朝阳一模 Q20 主线/可选升华边界, 顺义一模 Q20 中国方案/人类命运共同体后置使用, and 海淀期中 Q16(2) 企业/行业组织/政府三主体动作.
- Current clean scan on both student preview files: `PASS`, no hits.
- Final delivery remains blocked pending second narrow regate and later full coverage/final artifact checks.

## 2026-05-03 Optional-Label Final Gate

- After 顺义 answer-order correction and 朝阳 optional-label targeting correction, final narrow checks returned Patcher `PASS`, Confucius `PASS`, and Governor `PASS_WITH_GUARD`.
- Governor released only internal preview / coverage expansion. Final student version, Word/PDF, FINAL_ACCEPTANCE, and coverage close remain blocked.
