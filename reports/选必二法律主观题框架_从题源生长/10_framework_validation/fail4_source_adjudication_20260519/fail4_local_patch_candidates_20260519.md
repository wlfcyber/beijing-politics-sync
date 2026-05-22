# FAIL4 Local Patch Candidates

This file is a local candidate patch sheet only. It does not promote any code into framework_v2. Core promotion still requires Cowork/GPT dual confirmation.

## Summary

| question_id | local_patch_decision | proposed_label | gate | core_use_now |
|---|---|---|---|---|
| `CC0143_2025_朝阳_一模_19` | candidate_add_or_revise_core_code | 消费合同欺诈与惩罚性赔偿 | pending_cowork_or_dual_model_confirmation | no |
| `CC0276_2026_房山_二模_17` | boundary_non_core_keep_audit | 涉外法治建设边界样本 | boundary_quarantine | no |
| `RECOVER_2026_西城_二模_18_2` | open_container_pending_dual_model | AI责任边界与产业发展开放容器 | pending_cowork_or_dual_model_confirmation | no |
| `RECOVER_2026_西城_二模_18_3` | exclude_from_xuanbier_core | 数字治理法治化非核心样本 | exclude_from_core | no |

## Details

### CC0143_2025_朝阳_一模_19

- proposed_code_id: `LOCAL_CANDIDATE_CC0143_CONSUMER_CONTRACT_FRAUD`
- proposed_label: 消费合同欺诈与惩罚性赔偿
- supporting_rubric_atom_ids: `R_CC0143_2025_朝阳_一模_19_07|R_CC0143_2025_朝阳_一模_19_08|R_CC0143_2025_朝阳_一模_19_09|R_CC0143_2025_朝阳_一模_19_10|R_CC0143_2025_朝阳_一模_19_16|R_CC0143_2025_朝阳_一模_19_17|R_CC0143_2025_朝阳_一模_19_22|R_CC0143_2025_朝阳_一模_19_23`
- supporting_material_atom_ids: `M_CC0143_2025_朝阳_一模_19_03|M_CC0143_2025_朝阳_一模_19_05|M_CC0143_2025_朝阳_一模_19_06|M_CC0143_2025_朝阳_一模_19_07|M_CC0143_2025_朝阳_一模_19_08`
- minimum_judgment: 先判断这是网络平台销售服务中的消费合同纠纷，并且设问要求解释法院支持两个诉讼请求的理由：退还票款与三倍赔偿。
- material_trigger: 平台代销机票；实付价与官网总价不一致；擅自搭售10元外卖红包；消费者无法清楚知悉费用细节且无法拒绝；消费者起诉请求退还票款并三倍赔偿；题面给出消费者权益保护法第55条。
- rubric_reward_pattern: 合同成立/要约承诺1分；搭售事实三条件写全1分；欺诈导致违背真实意思订立合同1分；合同无效或可撤销1分；写准消费者权益保护法1分；欺诈或侵犯知情权/公平交易权/自主选择权1分；价值收束2分。
- full_score_sentence_pattern: 王某通过A公司平台购买机票并出票，双方合同成立；但A公司擅自搭售10元外卖红包，王某不能清楚知悉费用细节且无法拒绝支付，构成欺诈，使王某违背真实意思订立合同，合同无效或可撤销。依据消费者权益保护法，经营者提供服务有欺诈行为，应按消费者要求增加赔偿，故法院支持退还票款及三倍赔偿，并有利于维护消费者合法权益、规范网络消费秩序。
- risk_warning: 不能写成隐私权、消费者同意权、反不正当竞争或单纯违约责任；不能漏掉两个诉讼请求；消费者权益保护法名称不能写错；搭售事实三条件必须写全。
- gate: pending_cowork_or_dual_model_confirmation

### CC0276_2026_房山_二模_17

- proposed_code_id: `BOUNDARY_CC0276_FOREIGN_RELATED_RULE_OF_LAW`
- proposed_label: 涉外法治建设边界样本
- supporting_rubric_atom_ids: `R_CC0276_2026_房山_二模_17_01`
- supporting_material_atom_ids: `M_CC0276_2026_房山_二模_17_01|M_CC0276_2026_房山_二模_17_02|M_CC0276_2026_房山_二模_17_03|M_CC0276_2026_房山_二模_17_04|M_CC0276_2026_房山_二模_17_05`
- minimum_judgment: 先判断设问是涉外法治建设如何加强，不是私人法律关系中权利义务责任的判定。
- material_trigger: 外商投资法及实施条例；涉外司法实践；活扣押；调解、仲裁、诉讼一站式平台；涉外海事纠纷多元化解。
- rubric_reward_pattern: 涉外法律法规体系/加强涉外立法；创新司法实践/公正司法；多元纠纷解决平台；创新诉讼调解/多元主体参与；大国责任和涉外法治建设。
- full_score_sentence_pattern: 不作为选必二法律生活核心满分句模板，只保留边界审计。
- risk_warning: 若进入核心框架，容易把选必二框架拉向必修三法治建设和国家治理表达。
- gate: boundary_quarantine

### RECOVER_2026_西城_二模_18_2

- proposed_code_id: `OPEN_RECOVER_2026_XICHENG_AI_RESPONSIBILITY_BOUNDARY`
- proposed_label: AI责任边界与产业发展开放容器
- supporting_rubric_atom_ids: `RECOVER_2026_西城_二模_18_2_R01|RECOVER_2026_西城_二模_18_2_R02|RECOVER_2026_西城_二模_18_2_R03`
- supporting_material_atom_ids: `RECOVER_2026_西城_二模_18_2_M01|RECOVER_2026_西城_二模_18_2_M02|RECOVER_2026_西城_二模_18_2_M03`
- minimum_judgment: 先判断题目问的是AI权责边界认定对产业发展的影响，不是让学生完整判侵权责任成立与否。
- material_trigger: AI生成虚假信息；平台显著提示仅供参考；用户未证明实际损失；最高法典型案例明确责任边界。
- rubric_reward_pattern: 明确责任边界、稳定法律预期、释放创新活力；统一裁判标准、规范行业行为；权利义务相统一、平衡用户权益与技术创新。
- full_score_sentence_pattern: 该判决明确生成式AI服务中的责任边界，避免过度追责，为企业提供稳定法律预期，释放创新活力；同时统一裁判标准、规范行业行为，并坚持权利义务相统一，平衡用户权益保障与技术创新需求。
- risk_warning: 价值和产业发展表达很强，不能单独支撑核心节点；若进入核心，必须收束为责任边界/权利义务而不是泛泛营商环境。
- gate: pending_cowork_or_dual_model_confirmation

### RECOVER_2026_西城_二模_18_3

- proposed_code_id: `EXCLUDE_RECOVER_2026_XICHENG_DIGITAL_GOVERNANCE`
- proposed_label: 数字治理法治化非核心样本
- supporting_rubric_atom_ids: `RECOVER_2026_西城_二模_18_3_R01|RECOVER_2026_西城_二模_18_3_R02|RECOVER_2026_西城_二模_18_3_R03`
- supporting_material_atom_ids: `RECOVER_2026_西城_二模_18_3_M01|RECOVER_2026_西城_二模_18_3_M02|RECOVER_2026_西城_二模_18_3_M03`
- minimum_judgment: 先判断设问落点是典型案例对国家治理能力现代化的意义，不是选必二法律生活中具体权利义务责任的生成。
- material_trigger: 最高法发布典型案例；数字治理规则；法律实施机制；司法公正；依法行政；国家治理能力现代化。
- rubric_reward_pattern: 完善数字治理规则、健全法律实施机制、治理法治化；示范指引和警示教育；规范权力运行、司法公正、依法行政；公众依法行使权利履行义务；公共利益与治理能力。
- full_score_sentence_pattern: 不进入选必二核心满分句库。
- risk_warning: 这是强必修三/综合法治治理题。纳入核心会导致框架必修三化。
- gate: exclude_from_core
