# FAIL4 Source Adjudication

These are local source decisions after the v1.1 sentence-level pressure test. They are not final framework promotions.

## Summary

| question_id | local_decision | proposed_bucket | core_use_now |
|---|---|---|---|
| `CC0143_2025_朝阳_一模_19` | candidate_core_pending_dual_model | consumer_contract_fraud_and_punitive_compensation | no |
| `CC0276_2026_房山_二模_17` | boundary_non_core_keep_audit | foreign_related_rule_of_law_governance_boundary | no |
| `RECOVER_2026_西城_二模_18_2` | open_container_pending_dual_model | ai_responsibility_boundary_industry_development | no |
| `RECOVER_2026_西城_二模_18_3` | exclude_from_xuanbier_core | digital_governance_rule_of_law_boundary | no |

## Per-Question Decisions

### CC0143_2025_朝阳_一模_19

- evidence_level: formal
- module_boundary_risk: 选必二
- ask: 结合材料，运用《法律与生活》知识，说明人民法院支持王某的诉讼请求的理由。
- local_decision: candidate_core_pending_dual_model
- proposed_bucket: consumer_contract_fraud_and_punitive_compensation
- reason: formal marking_report gives detailed scoring: contract formation, hidden bundled fee facts, fraud/true intention, revocable or invalid contract, Consumers' Rights and Interests Protection Law, threefold compensation, consumer/platform-order value. This is not IP/unfair-competition, but it is a strong selected-compulsory-2 consumer/contract case. It should not remain FAIL; it should be sent to GPT/Claude for a targeted codebook supplement or merged into CODE_COWORK_004/007.
- next_action: send targeted adjudication to GPT-5.5 Pro and Claude Opus/Cowork; do not promote locally before dual-model agreement because current expansion round did not place it.

### CC0276_2026_房山_二模_17

- evidence_level: formal
- module_boundary_risk: 选必二
- ask: 中国走向世界，以负责任大国参与国际事务，必须善于运用法治。结合材料，运用法治知识，谈谈中国是如何加强涉外法治建设的。
- local_decision: boundary_non_core_keep_audit
- proposed_bucket: foreign_related_rule_of_law_governance_boundary
- reason: formal scoring rewards涉外法律法规体系、涉外司法实践、公正司法、多元纠纷解决平台、涉外海事纠纷化解、大国责任. The answer mechanism is law-governance/涉外法治建设, not private-law rights-duty-rule conversion. It risks必修三化 if used as selected-compulsory-2 core.
- next_action: keep in boundary/open audit, not in core framework; if user wants broad法治题 appendix, list separately.

### RECOVER_2026_西城_二模_18_2

- evidence_level: formal
- module_boundary_risk: 综合
- ask: 结合该案判决对生成式AI权责边界的认定，分析其对促进AI产业发展的影响。（6分）
- local_decision: open_container_pending_dual_model
- proposed_bucket: ai_responsibility_boundary_industry_development
- reason: formal rubric has legal signals: responsibility boundary, legal expectation, rights-obligations balance, user rights and innovation balance. But scoring is mainly industry-development impact and法治营商环境. It can be an AI responsibility-boundary open container, not yet a core node.
- next_action: send with CC0143 in targeted adjudication; ask models whether it should revise CODE_COWORK_002 or remain open container.

### RECOVER_2026_西城_二模_18_3

- evidence_level: formal
- module_boundary_risk: 综合
- ask: 结合材料二，从法治的角度，阐释最高人民法院发布典型案例对推进国家治理能力现代化的意义。（6分）
- local_decision: exclude_from_xuanbier_core
- proposed_bucket: digital_governance_rule_of_law_boundary
- reason: formal rubric rewards数字治理规则、法律实施机制、治理法治化、示范指引、依法行政、国家治理能力现代化. This is overwhelmingly法治治理/必修三综合, not a selected-compulsory-2 legal-life scoring mechanism.
- next_action: quarantine as boundary/non-core; do not send as core framework evidence unless user widens scope to综合法治.

## Gate

`CC0143` and `RECOVER_2026_西城_二模_18_2` need targeted dual-model adjudication before any codebook/core change. `CC0276` and `RECOVER_2026_西城_二模_18_3` should remain boundary/non-core unless the user widens the project scope.
