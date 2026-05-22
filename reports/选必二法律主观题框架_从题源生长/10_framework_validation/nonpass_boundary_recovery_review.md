# Non-PASS Boundary Recovery Review

生成时间：2026-05-19T14:28:00+08:00

目的：复核 v1 压测中 13 个 PARTIAL + 20 个 FAIL，避免把低频正式法律题误扔，也避免把非选必二/串题误收硬塞进框架。

## 统计

- EXCLUDE_NON_LAW: 11
- RECOVER_TO_CORE_OR_OPEN_FORMAL: 9
- KEEP_REFERENCE_OPEN_ONLY: 5
- SPLIT_OR_DEDUPLICATE: 4
- REEXTRACT_BEFORE_DECISION: 3
- EXCLUDE_MISMATCH_DUPLICATE: 1

## 裁决原则

- 正式法律题但未被 codebook 覆盖：恢复为开放容器正式样本，后续可进宝典弱/正式低频示范。
- reference_only：只进开放容器，不支撑核心。
- 父题/小问重复：保留小问，父题不重复计数。
- 行级串题：不直接恢复，写重抽任务。
- 非选必二：剔除。

## 逐题裁决

| question_id | 原状态 | 恢复裁决 | 是否进修订宝典 | 是否支撑核心 | 理由 |
| --- | --- | --- | --- | --- | --- |
| CC0001_2024_丰台_一模_16 | FAIL/必修三化 | EXCLUDE_MISMATCH_DUPLICATE | no | no | 剔除：题号16正文/细则为《政治与法治》四下基层；ask_text 串入 CC0002 法律题。 |
| CC0026_2024_朝阳_二模_18 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：材料含选择题/OCR串页，细则为《政治与法治》全过程人民民主。 |
| CC0040_2024_海淀_一模_19 | PARTIAL/证据不足 | KEEP_REFERENCE_OPEN_ONLY | yes | no | 保留弱示范：虚拟数字人著作权/不正当竞争，普通答案，evidence_level=reference_only。 |
| CC0045_2024_海淀_二模_19 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：遗赠扶养协议、继承/养老价值，正式材料与答案一致，属低频婚姻家庭/继承方向。 |
| CC0047_2024_海淀_二模_21 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：综合运用所学谈新质/民生目标，细则可从党、制度、经济、治理、文化等答，不是法律规则采分。 |
| CC0051_2024_海淀_期中_21_1 | FAIL/必修三化 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：婚姻法与民法典共同债务规定、良法/权利义务/时代背景，正式评标明确材料+知识。 |
| CC0061_2024_西城_一模_18 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：成年子女赡养义务、精神慰藉、督促履行义务告知书，正式细则有具体给分。 |
| CC0070_2024_顺义_二模_19 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：经济/国际/马克思主义中国化类综合题，非法律规则采分。 |
| CC0091_2025_东城_期末_19 | FAIL/必修三化 | SPLIT_OR_DEDUPLICATE | yes | no | 整题为电动自行车安家难综合题，含法律小问、利益主体、民主协商。应拆分；不能与 CC0092/CC0094 重复计数。 |
| CC0092_2025_东城_期末_19_1 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：充电柜方案涉及消防规定、共有部分用途、业主共有权/相邻权/侵权等法律问题，正式细则。 |
| CC0094_2025_东城_期末_19_3 | FAIL/必修三化 | KEEP_REFERENCE_OPEN_ONLY | yes | no | 保留弱/混合示范：法律与生活相邻关系2分 + 政治与法治民主程序2分；reference_only且混合。 |
| CC0118_2025_丰台_期末_18_2 | FAIL/必修三化 | REEXTRACT_BEFORE_DECISION | no | no | 当前行绑定的是经济题“数字经济放得活管得住”，但同 PPT 后续有尹某劳动合同裁判细则；行级错配，需重抽法律小问。 |
| CC0132_2025_房山_一模_20 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：奋斗主题综合题，细则为民族复兴/精神/发展观等。 |
| CC0162_2025_海淀_一模_18 | PARTIAL/证据不足 | KEEP_REFERENCE_OPEN_ONLY | yes | no | 保留弱示范：主题乐园年卡格式合同/诚信/解除合同，reference_only。 |
| CC0168_2025_海淀_二模_20 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：共享发展/国际组织/粮食安全等非选必二法律采分。 |
| CC0182_2025_海淀_期末_22 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：愚公精神/综合论述，民法典条文只是材料串入或干扰，不是法律主观题。 |
| CC0189_2025_石景山_一模_20 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：人民法院司法护航新质生产力，含委托合同违约、知识产权/创新保护，正式评分细则。 |
| CC0218_2025_顺义_一模_16 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：联系观点/文化双创/哪吒等哲学文化题。 |
| CC0229_2026_东城_一模_18 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：人民法院以司法之力守护向新力，专利权/植物新品种/调解与创新保护，正式材料。 |
| CC0240_2026_东城_二模_21 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：金融五篇大文章/党政府经济职能/辩证思维。 |
| CC0250_2026_丰台_一模_19 | PARTIAL/漏节点 | EXCLUDE_NON_LAW | no | no | 剔除：人类命运共同体/可持续发展，后页复练提示法律板块但本行不是法律题。 |
| CC0259_2026_丰台_期中_19 | FAIL/其他 | REEXTRACT_BEFORE_DECISION | no | no | 当前行严重串题：full 显示遗赠扶养协议，但 rubric atoms 多为经济/逻辑/全球倡议反馈；需回源重抽。 |
| CC0276_2026_房山_二模_17 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：涉外法律法规体系、涉外司法、调解仲裁诉讼衔接，正式细则。虽有必修三法治边界，但材料/细则明确法律治理路径。 |
| CC0294_2026_朝阳_二模_20_2 | FAIL/必修三化 | EXCLUDE_NON_LAW | no | no | 剔除：当代国际政治与经济/人类命运共同体，非法律主观题。 |
| CC0305_2026_海淀_一模_18 | FAIL/必修三化 | SPLIT_OR_DEDUPLICATE | yes | no | 整题前两问为消费/经济，第三问为隐私权、消费者知情权、虚假宣传、欺诈赔偿。应拆出 Q18(3) 法律小问。 |
| CC0311_2026_海淀_二模_18 | PARTIAL/证据不足 | KEEP_REFERENCE_OPEN_ONLY | yes | no | 保留弱示范：知识产权财产权、质押融资、作价出资、专利奖励，reference_only。 |
| CC0318_2026_海淀_期中_18_2 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：住房租赁市场合同示范文本、格式条款、诚信、合同纠纷、市场监管，正式细则。 |
| CC0332_2026_石景山_二模_19 | PARTIAL/漏节点 | RECOVER_TO_CORE_OR_OPEN_FORMAL | yes | yes | 恢复：校园欺凌惩教并行，民法典人格权/财产权、父母教育惩戒义务，正式细则。 |
| CC0353_2026_西城_期中_17 | PARTIAL/证据不足 | KEEP_REFERENCE_OPEN_ONLY | yes | no | 保留弱示范：不正当竞争+未成年人保护，reference_only。 |
| CC0358_2026_通州_一模_17 | FAIL/其他 | EXCLUDE_NON_LAW | no | no | 剔除：通州一模该行实际为《逻辑与思维》辩证思维看AI，后续文化题串页；非法律主观题。 |
| CC0363_2026_通州_期中_19 | FAIL/其他 | SPLIT_OR_DEDUPLICATE | yes | no | 整题含(1)法律相邻加装电梯、(2)逻辑推理。法律小问已由 CC0364_2026_通州_期中_19_1 PASS 承载；父题不再计数。 |
| CC0373_2026_顺义_一模_17 | FAIL/必修三化 | SPLIT_OR_DEDUPLICATE | yes | no | 行首为Q17政治题，但后续 slide 含Q18劳动就业歧视+竞业限制正式评分细则。应新建/重命名为Q18法律小问，不作为Q17。 |
| CC0380_2026_顺义_二模_18 | FAIL/必修三化 | REEXTRACT_BEFORE_DECISION | no | no | 整题含逻辑小问和开源智能体可能侵害财产权/隐私权/个人信息等法律小问，但当前 rubric_atoms 只抽到逻辑部分。需重抽Q18(2)法律细则。 |

## 下一步

1. 先生成 v2.1 修订输入包，交给 GPT-5.5 Pro 和 Claude Opus 4.7 Adaptive 对恢复裁决进行同包复核。
2. 对 `REEXTRACT_BEFORE_DECISION` 的题，交给 ClaudeCode B 或本地回源重新抽小问。
3. 在外部复核/重抽完成前，不覆盖 `framework_v2.md` 和最终宝典，只生成候选修订文件。
