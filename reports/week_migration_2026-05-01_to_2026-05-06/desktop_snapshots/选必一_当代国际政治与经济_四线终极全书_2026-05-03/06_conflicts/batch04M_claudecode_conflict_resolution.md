# Batch04M ClaudeCode A/B Conflict Resolution

time: 2026-05-04
scope: Batch04M remaining suites after ClaudeCode B independent verification
student_doc_status: fusion draft regenerated, not final

## Final Local Rulings

### 1. 2026丰台期末 Q20

ruling: BLOCKED_PROMPT_ONLY

ClaudeCode B confirmed Codex A's blocker. The LAC “五大工程” prompt exists, but the current scoring rubric for this Q20 is absent from the local deck; the following pages jump to a different 9-point comprehensive question, and the older Beijing卷四大全球倡议 rubric is only a teaching anchor. No atom is promoted. Placeholder terms such as 全球发展倡议、全球安全倡议、全球文明倡议、新型国际关系、中拉命运共同体 remain outside the main table until a current formal rubric is found.

### 2. 2024石景山一模 Q19(2) and 2024顺义二模 Q19(2)

ruling: REFERENCE_ONLY_NOT_PROMOTED

ClaudeCode B found no formal scoring standard or point/level rubric. These two questions are removed from the main student core and kept only as boundary expression awareness. This corrects the earlier guarded-candidate prelim state and follows the rule that ordinary reference answers cannot become scoring terms.

### 3. 2025丰台一模 Q20

ruling: GUARDED_FALLBACK_ONLY

ClaudeCode B identified a hard negative rule: piling 新型国际关系、人类命运共同体 or generic 推动经济全球化发展 earns no credit in this question. The four practical-measure rows are primarily 《经济与社会》 main-code measures, so they are downgraded to boundary-only. Only the macro fallback “国内国际双循环 / 两个市场两种资源联动” remains in the 选必一 guarded expression layer, and only when the main practical-measure angles are missing.

### 4. 2025昌平二模 Q21

ruling: GUARDED_ADMIT

The prompt does not explicitly name the book, but the scoring material contains clear 选必一 economic-globalization terms such as 两个市场两种资源、全球经济治理话语权、开放包容全球经济格局. These enter only as guarded expression accumulation; dual-coded economy-and-society measures remain boundary.

### 5. 术语保形

ruling: ACCEPTED

Total fusion must preserve high-information variants instead of collapsing them into vague labels:

- 经济全球化方向 keeps 开放、包容、普惠、平衡、共赢 as the full core; shorter 普惠包容/开放包容 variants stay as expression variants.
- 共商共建共享 binds to 共商共建共享的全球治理观 unless a source explicitly uses another domain.
- 新型国际关系 keeps the full 相互尊重、公平正义、合作共赢 version when the scoring position awards the full version.
- 联合国为核心的国际体系 / 国际法为基础的国际秩序 and 《联合国宪章》宗旨和原则 are same family but not interchangeable.
- 正确义利观 remains an independent term, not a loose synonym for “合作”。

## Files Updated By Codex A

- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`: downgraded reference-only rows, downgraded 2025丰台一模 primary practical-measure rows, added guarded fallback and negative-boundary atom.
- `SOURCE_LEDGER.csv`: retagged 2024石景山一模, 2024顺义二模, 2025昌平二模, and 2026丰台期末 source rows with finer evidence boundaries.
- `COVERAGE_MATRIX.csv`: marked Batch04M B line complete/pending final AB review and reflected key local rulings.
- `fusion/all_scoring_atoms_combined_20260504.csv`, `fusion/six_bucket_core_clusters_20260504.csv`, `07_student_doc/选必一_完整学生讲义_融合稿_20260504.md`: regenerated from corrected atom statuses.

## Still Required

- Wait for ClaudeCode screen to exit cleanly.
- Run Patcher and Governor AB closure review on this conflict resolution.
- Then run real Claude Opus teaching-text review and real GPT-5.5 Pro content review before final Markdown/DOCX/PDF delivery.
