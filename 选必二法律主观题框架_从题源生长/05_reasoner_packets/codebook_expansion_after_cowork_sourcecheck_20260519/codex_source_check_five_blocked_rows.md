# Codex Source Check: Five Cowork-Blocked Rows

- generated_at: 2026-05-19T18:53:31+08:00
- scope: Cowork 点名不得直接 promote 的 5 道题
- conclusion: 5 道都不是 missing；但 4 道需要 atom/小问结构修正，1 道需要替换错误来源段。
## Overall Decision

不得把 Cowork 建议直接升代码本。先按本报告的 split/replacement plan 进入扩码输入包，由 GPT-5.5 Pro 与 Claude Opus 用同一包交叉验证。CC0254 当前 R01-R08 明确不再作为 scoring atom 使用；它们只是学生问题/教学建议。
## Row Decisions

### CC0011_2024_丰台_二模_17
- verdict: `CONFIRM_FORMAL_BUT_SPLIT_REQUIRED`
- evidence_level_after_check: `formal`
- source: F0270 extracted_text lines 11-16; F0047 same content
- action: Replace current single 8-point atom with four formal scoring atoms; keep question in corpus; do not promote as new standalone code without cross-model support.
- corrected_atomization: 1分: 绿色原则为生态环境保护提供基本遵循; 2分: 知识产权保护鼓励技术创新并为环保提供技术支撑; 1分: 污染破坏环境应承担侵权责任; 4分: 民法典确定权利义务,保护合法权益/惩罚违法行为,平衡个人利益和公共利益,预防损害并维护良好生态环境。
- promotion_decision: `ALLOW_AS_EXPANSION_EVIDENCE_AFTER_SPLIT; not standalone core code`
- reason: Formal scoring-standard wording exists with point values, but current merged_rubric atom collapses all 8 points into one atom, so model expansion must see the split plan.

### CC0019_2024_朝阳_一模_19
- verdict: `CONFIRM_FORMAL_AND_SPLIT_REQUIRED`
- evidence_level_after_check: `formal`
- source: F0015 lines 249-265 for question; F0013 lines 333-349 for scoring rubric; F0014 lines 20-23 for answer text
- action: Replace current single 7-point atom with six scoring atoms using slide 43 rubric; keep as formal evidence for revising basic-principle code branch.
- corrected_atomization: 1分: 市场经济本质上是法治经济/诚信原则入民法典/核心价值观或法德结合; 1分: 合同当事人诚信/全面履行义务; 1分: 规范民事主体行为并维护合法权利; 1分: 司法依诚信原则定分止争、维护公平正义和市场秩序; 1分: 经营者依法诚信经营; 2分: 保护消费者权益、平衡经营者消费者关系、扩大市场/激发活力/社会福祉等任选。
- promotion_decision: `ALLOW_AS_EXPANSION_EVIDENCE_AFTER_SPLIT; supports revision of CODE_COWORK_002`
- reason: The dedicated PPT gives explicit point allocation; previous atom used only answer paragraph and lost the 1+6 scoring structure.

### CC0061_2024_西城_一模_18
- verdict: `CONFIRM_FORMAL_BUT_QUESTION_SPLIT_OR_TRIM_REQUIRED`
- evidence_level_after_check: `formal`
- source: F0061 lines 101-109 for question and asks; F0278 lines 25-42 for scoring and adjustments; F0279 lines 12-20 for answer
- action: Do not treat current row as one unified mechanism. Either split into 18(1), 18(2), 18(3), or for framework expansion use only 18(3) with its 6-point rubric; quarantine 18(1)(2) as procedure micro-items unless separately modeled.
- corrected_atomization: 18(1) 1分: 回避制度适用情形，材料示例可写书记员与当事人/代理人存在可能影响公正关系; 18(2) 1分: “辩护人”应改为“诉讼代理人”; 18(3) 6分: 成年子女赡养义务1 + 经济/生活/精神慰藉等五选二2 + 三个儿子应履行精神慰藉义务/告知书保护权益引导孝老敬亲1 + 传统美德/核心价值观/法律促进道德建设等多选2。
- promotion_decision: `DEFER_UNTIL_SPLIT; 18(3) may support family-duty/value-convergence branch after split`
- reason: Current ask_text only records 18(3), but rubric atoms include 18(1)(2); using the current row directly would contaminate codebook evidence.

### CC0254_2026_丰台_二模_18
- verdict: `CONFIRM_FORMAL_BUT_CURRENT_ATOMS_WRONG_SOURCE_SEGMENT`
- evidence_level_after_check: `formal`
- source: F0187 lines 148-170 for answer and scoring table; lines 181-190 are student problems/suggestions and must not be treated as scoring atoms
- action: Remove/ignore current R01-R08 for scoring support; replace with eight formal scoring atoms from slides 29-30 before any codebook promotion.
- corrected_atomization: 1分: 法治与德治相结合; 1分: 依据民法典定分止争; 1分: 饲养动物侵权适用无过错责任; 1分: 依法维护张某合法财产权益; 1分: 引入生态环境法典核心原则/损害担责并将矛盾化解与生态修复同步; 1分: 结合双方实际提出分期赔偿+行为约束+生态修复方案; 1分: 促成互谅互让/传递司法温暖; 1分: 弘扬社会主义核心价值观。
- promotion_decision: `ALLOW_AS_EXPANSION_EVIDENCE_ONLY_AFTER_ATOM_REPLACEMENT; likely supports law-duty plus mediation/value branch`
- reason: The formal scoring table is present, but canonical atoms were extracted from later student-error slides. This is a hard atom-source mismatch, not a missing-rubric problem.

### RECOVER_2026_房山_一模_17_1
- verdict: `CONFIRM_FORMAL_BUT_ALTERNATIVE_DIMENSIONS_MUST_NOT_BE_CUMULATED`
- evidence_level_after_check: `formal`
- source: F0371 lines 22-29; F0160 lines 22-29
- action: Keep as formal 3-point subquestion, but rewrite atom plan so the 2-point explanation is one alternative dimension selected from 主体/内容/客体, not cumulative 4-6 points.
- corrected_atomization: 1分: AI幻觉造成的损失不由A公司买单; 2分: 民事法律关系主体/内容/客体任一维度解释清楚即可得2分：主体维度含自然人法人非法人组织+AI不具主体资格/承诺无效；内容维度含权利义务+A公司履行提示义务/无过错；客体维度含权利义务指向对象+梁某权益未受实际损害。
- promotion_decision: `ALLOW_AS_SINGLE_FORMAL_TRANSFER_EVIDENCE; not enough for standalone new core code`
- reason: The source is a real scoring rubric, but current atoms make alternative explanations look like separate additive rewards. Codebook expansion must preserve the 1+2 structure.

## Corrected Atom Plan

See `codex_source_check_corrected_rubric_atom_plan.csv`. This is a source-check patch plan for model expansion and later canonical integration; it does not by itself promote any new codebook node.
