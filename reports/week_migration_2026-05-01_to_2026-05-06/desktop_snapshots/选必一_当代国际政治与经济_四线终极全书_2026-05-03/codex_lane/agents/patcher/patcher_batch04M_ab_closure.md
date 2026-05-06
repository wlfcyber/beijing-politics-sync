# Batch04M A/B Closure Patcher Review

time: 2026-05-04
role: Codex A Patcher
student_doc_touched: no
docx_pdf_final_touched: no
fusion_touched: no

verdict: PASS_WITH_FIXES

## Read Scope

- `06_conflicts/batch04M_claudecode_conflict_resolution.md`
- `claudecode_lane/batch04M_conflicts_for_codex.md`
- `claudecode_lane/batch04M_missing_blockers.md`
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`
- `fusion/six_bucket_core_clusters_20260504.csv`
- `07_student_doc/选必一_完整学生讲义_融合稿_20260504.md`

## Closure Checks

### 1. 2024石景山 / 2024顺义 reference-only: closed

`fusion/scoring_atom_table_batch04M_remaining_prelim.csv` has downgraded:

- `M-SJS24YM-01..03` to `P1_reference_answer_only` / `reference_only`
- `M-SY24EM-01..03` to `P1_reference_answer_only` / `reference_only`

`fusion/six_bucket_core_clusters_20260504.csv` no longer lists `2024石景山一模` or `2024顺义二模` as source questions in the main clusters. The student fusion draft only mentions them in the final caution block: "只作边界表达参考，不进入本讲义主频." This satisfies the A/B ruling that ordinary reference answers cannot become scoring terms.

### 2. 2025丰台一模 Q20: mostly closed

Codex A has applied ClaudeCode B's ruling:

- `M-FT25YM-01..04` are now `模块边界` / `boundary_only`, not Xuanbiyi main cores.
- `M-FT25YM-FALLBACK` is the only positive Xuanbiyi retained expression: domestic-international circulation and two markets/two resources as a guarded fallback.
- `M-FT25YM-NEG` preserves the hard negative rule that piling `新型国际关系 / 人类命运共同体 / 泛泛推动经济全球化发展` does not score for this question.

Student draft only includes 2025丰台一模 under the `两个市场两种资源` cluster as fallback and restates the exclusion in the final caution block. This is acceptable, but the fallback paragraph still contains backstage scoring wording that must be scrubbed before final delivery.

### 3. 2026丰台期末 Q20: closed

A/B closure agrees `BLOCKED_PROMPT_ONLY`: the LAC "五大工程" prompt exists, but no current Q20 scoring rubric was found. No fusion atom is promoted, and the student draft only says it currently has only the prompt and does not enter the main framework.

Do not promote the placeholder terms (`全球发展倡议 / 全球安全倡议 / 全球文明倡议 / 新型国际关系 / 中拉命运共同体` etc.) unless a current formal rubric is found.

## Same-Core / Term-Shape Review

### Pass points

- The full globalization-direction core keeps `开放、包容、普惠、平衡、共赢`; shorter variants such as `开放包容普惠`, `普惠包容`, and `更加包容、更可持续` are not used to rename the master core.
- `共商共建共享` is generally displayed as `共商共建共享的全球治理观`, not as a domestic-governance phrase.
- `相互尊重、公平正义、合作共赢的新型国际关系` remains the full core; bare `新型国际关系` appears as weaker/variant expression.
- UN family keeps separate rows for `《联合国宪章》宗旨和原则`, `以联合国为核心的国际体系`, and `维护联合国在国际事务中的核心作用`.

### Required merge cleanup

`fusion/six_bucket_core_clusters_20260504.csv` still has over-broad expression accumulation inside some clusters:

- `共商共建共享的全球治理观` cluster includes `人类命运共同体`, `正确义利观`, `真正的多边主义`, `全人类共同价值` and similar items. These can be cross-references or same-question neighboring expressions, but not synonyms of the core.
- `推动建设相互尊重、公平正义、合作共赢的新型国际关系` cluster similarly absorbs `正确义利观`, `构建人类命运共同体`, `全人类共同价值`, and `中国智慧、中国方案`.
- `维护国家利益并兼顾他国合理关切，坚持正确义利观` cluster includes a long UN/HMC expression from 房山 Q18(2); this should be split or marked as cross-bucket expression, not used as proof that UN/HMC equals国家利益/义利观.

Minimum fix: keep these as `crossref_expression` or remove them from the core expression line in the student-facing cluster, so the student sees one scoring core and not a bag of adjacent terms.

## Student Draft Pollution Review

The student draft is not clean enough for FINAL/DOCX/PDF:

- `出现X题` frequency labels remain throughout the six-bucket overview and headings.
- `得分位置` appears heavily as a student-visible field.
- Backstage/evidence words remain, including `评分细则`, `讲评材料`, `内嵌图片image8`, `答案提示`, `评分标准说明`, `参考示例`.
- Exact `材料中` was not found, but `材料触发` is still used as a formal field. This may be acceptable for a teaching draft, but the final student version should convert it into natural "看到什么就写什么" language if required.
- The word `路径` appears in normal content and in scoring descriptions. Keep only real answer-language uses such as "发展路径"; remove uses that mean rubric path/evidence path.

This is a student-generation cleanup issue, not an A/B evidence blocker.

## Required Fixes Before Final Delivery

1. Scrub the student draft of frequency counts and audit fields: `出现X题`, `得分位置`, `评分细则`, `讲评材料`, `内嵌图片image8`, `答案提示`, `参考示例`, and similar provenance language.
2. Keep 2024石景山一模 Q19(2) and 2024顺义二模 Q19(2) out of main clusters and out of normal student examples; boundary note only is acceptable.
3. Keep 2025丰台一模 Q20 as fallback-only plus hard negative rule; do not reintroduce its four practical-measure rows as Xuanbiyi main cores.
4. Keep 2026丰台期末 Q20 blocked until a current formal scoring source is found.
5. Split or re-label over-broad expression accumulation where HMC, 正确义利观, 真正多边主义, 新型国际关系, 中国方案, and UN-family terms are adjacent but not same-core synonyms.

## Final Gate

`PASS_WITH_FIXES`: A/B closure is acceptable at the evidence/fusion-status level. The regenerated student fusion draft must be scrubbed and cluster expression lines tightened before it can become FINAL/DOCX/PDF.

