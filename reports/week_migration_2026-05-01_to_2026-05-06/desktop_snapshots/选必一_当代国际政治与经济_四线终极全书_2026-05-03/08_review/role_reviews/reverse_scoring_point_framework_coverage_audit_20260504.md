# 反向覆盖审计：细则踩分点 -> 六桶框架 / 学生稿

time: 2026-05-04 12:45 CST
status: PASS_FOR_XUANBIYI_SCORING_POINTS

## Audit Method

- 母表：`fusion/all_scoring_atoms_combined_20260504.csv`.
- 展开口径：按 `source_question` 拆分，一个 atom 若服务两个题源，按两个题源锚点核对。
- 核对对象：最终闭环版学生稿、教师核查索引、核心点频次统计。
- 判断规则：选必一主线 scoring/candidate 点必须进学生稿主线；混合模块、reference-only、boundary-only、wrong-book 点可以只进慎用区或教师审计表，不强行进学生主框架。

## Counts

- Fusion atom rows: 211.
- Expanded atom-question links: 217.
- Main-framework expected links: 193.
- Side/audit expected links: 24.
- Teacher-index missing links: 0.
- Main-framework student-doc missing links: 0.
- Frequency-table source-question mismatches after sync patch: 0.

## Verdict

PASS. All current 选必一 promoted scoring/candidate atom-question links are represented in the final six-bucket framework and student-facing document. Teacher index coverage is complete. Frequency source lists are synchronized with post-GPT/Claude v2 framework placement.

## Deliberately Not Promoted To Student Mainline

- `BOUNDARY-B01` / 2026朝阳期中 Q17: `excluded_boundary_subpoint`. Reason: prevents_false_missing_subpoint_without_promoting_cross_module_terms. This row has no answer sentence and records a cross-module/non-Xuanbiyi boundary, so it stays in teacher audit rather than student mainline.

## New / Unfamiliar 2026-Style Points Confirmed In Framework

- 2026西城期末 Q20: 全球气候治理、NDC、《巴黎协定》 -> 中国作为负责任大国积极参与全球气候治理；在联合国和《巴黎协定》框架下维护多边气候治理机制.
- 2026朝阳期中 Q17: 人工智能发展关系题 -> 处理好自力更生和对外开放、发展和安全、中国发展和世界发展的关系；核心技术自主可控.
- 2026朝阳一模 Q20: 全球发展稳定性和正能量 -> 南南合作、小而美项目、经济全球化五词、新型国际关系、中国智慧中国方案.
- 2026东城期末 Q20: 四大全球倡议 -> 四大倡议分路径服务推动构建人类命运共同体.
- 2026房山一模 Q19 / 2026门头沟一模 Q20: 海南自贸港与国际循环 -> 制度型开放、两个市场两种资源、贸易投资便利化、开放型世界经济.
- 2026石景山一模 Q20: 共同/开放/包容亚太合作等级题 -> 共商共建共享、维护共同利益、经济全球化包容可持续、和平发展合作共赢，guarded 处理.

## Status Breakdown

- `boundary_only`: 9
- `candidate_p2_guard`: 4
- `candidate_with_boundary_guard`: 4
- `candidate_with_fixes`: 162
- `candidate_with_fixes_boundary_guard`: 3
- `candidate_with_guard`: 18
- `excluded_boundary_subpoint`: 1
- `reference_only`: 9
- `result_expression_only`: 1

## Machine-Readable Detail

- `08_review/role_reviews/reverse_scoring_point_framework_coverage_audit_20260504.csv`

