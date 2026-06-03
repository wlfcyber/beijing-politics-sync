# Framework v2 Boundary Recovery Delta After GPT Review
- generated_at: 2026-05-19T14:30:00+08:00
- source: local source recovery + real GPT-5.5 Pro boundary review saved at `10_framework_validation/gpt55pro_boundary_recovery_review.md`.
- status: supersedes `framework_v2_boundary_recovery_delta.csv` for count policy.

## Revised Counts
- Original v1 strict PASS: 37.
- Formal recovered existing units accepted now: 8.
- Formal split recovered core units accepted now: 2.
- Strict closed core before CC0229 atom patch: 47 = 37 + 8 recovered existing + 2 split recovered.
- Strict closed core after CC0229 atom patch: 48.
- Open/reference/formal-boundary container accepted now: 5.
- Core + open before CC0229 atom patch: 52.
- Core + open after CC0229 atom patch: 53.
- Pending tracked law/mixed units not counted in closure: CC0094_LAW_PENDING, CC0259_LAW, CC0118_LAW, plus split-parent housekeeping rows.
- Excluded non-law/mismatch rows: 12.

## GPT Corrections Applied
1. `CC0094_2025_东城_期末_19_3` changed from `keep_reference_open` to `split_or_deduplicate`; whole row cannot be a weak-open law example because current rubric atoms are wrong and the small question is law+politics mixed.
2. `CC0229_2026_东城_一模_18` is conditionally recoverable, but cannot support core code or final handbook closure until correct rubric atoms are patched from F0153/F0146.
3. `CC0250_2026_丰台_一模_19` must be removed from framework_v2 open-container examples and the handbook body.
4. `CC0051_2024_海淀_期中_21_1` moves from boundary review into formal low-frequency law sample.

## Buckets

### Recover Existing Formal Low/Core Units
- `CC0045_2024_海淀_二模_19` -> `recover_formal_low_frequency` / `core_recovered`: 恢复为低频正式法律样本：遗赠扶养协议、继承、养老价值。GPT 明确不建议自动扩主干核心。
- `CC0051_2024_海淀_期中_21_1` -> `recover_formal_low_frequency` / `core_recovered`: 恢复为低频正式法律样本：婚姻法、民法典共同债务、良法评析，注意必修三化风险。
- `CC0061_2024_西城_一模_18` -> `recover_formal_low_frequency` / `core_recovered`: 恢复为低频正式法律样本：成年子女赡养义务、精神慰藉、督促履行义务告知书。
- `CC0092_2025_东城_期末_19_1` -> `recover_core_existing_unit` / `core_recovered`: 恢复并可支撑既有核心：充电柜方案、消防规定、共有部分用途、业主共有权/相邻权/侵权。
- `CC0189_2025_石景山_一模_20` -> `recover_core_existing_unit` / `core_recovered`: 恢复并可支撑既有核心：委托合同违约、反不正当竞争、创新保护。
- `CC0276_2026_房山_二模_17` -> `recover_formal_low_frequency` / `core_recovered`: 恢复为低频正式样本：涉外法律法规体系、调解仲裁诉讼衔接；注意必修三边界。
- `CC0318_2026_海淀_期中_18_2` -> `recover_core_existing_unit` / `core_recovered`: 恢复并可支撑既有核心：住房租赁示范合同、格式条款、诚信、合同纠纷、市场监管。
- `CC0332_2026_石景山_二模_19` -> `recover_formal_low_frequency` / `core_recovered`: 恢复为低频正式样本：校园欺凌、人格权/财产权、父母教育惩戒义务，不扩主干。
- `CC0229_2026_东城_一模_18` -> `conditional_recover_atom_patch_required` / `core_recovered_after_atom_fix`: 条件恢复：题源法律方向成立，专利/植物新品种/恶意诉讼/调解明确；但当前 rubric_atom 串题，修复前不能支撑核心或入最终宝典满分闭环。

### Recover Split Formal Core Units
- `CC0305_2026_海淀_一模_18_3` -> `split_recovered_core` / `core_recovered_split`: 拆分恢复：Q18(3) 是隐私权、消费者知情权、虚假宣传、欺诈赔偿 formal 法律小问。
- `CC0373_2026_顺义_一模_18` -> `split_recovered_core` / `core_recovered_split`: 拆分恢复：Q18 劳动就业歧视与竞业限制有 formal 细则，应单独入库。

### Open / Weak Container Units
- `CC0040_2024_海淀_一模_19` -> `keep_reference_open` / `open_reference_or_weak`: 弱示范：虚拟数字人、著作权、不正当竞争方向明确，但只有 reference_only，不支撑核心。
- `CC0162_2025_海淀_一模_18` -> `keep_reference_open` / `open_reference_or_weak`: 弱示范：主题乐园年卡、格式合同、诚信、解除合同；reference_only，不作满分闭环。
- `CC0311_2026_海淀_二模_18` -> `keep_reference_open` / `open_reference_or_weak`: 弱示范：知识产权财产权、质押融资、作价出资、专利奖励；reference_only，不支撑核心。
- `CC0353_2026_西城_期中_17` -> `keep_reference_open` / `open_reference_or_weak`: 弱示范：不正当竞争与未成年人保护方向明确，但 reference_only。
- `CC0380_2026_顺义_二模_18_2` -> `split_recovered_open_formal` / `open_formal_split`: 拆分为开放容器：有 formal 法律给分口径，但同时允许必修三角度，不单独支撑核心。

### Pending Split or Reextract Units
- `CC0091_2025_东城_期末_19` -> `split_or_deduplicate_parent` / `not_counted_parent_unit`: 父题含法律小问、利益主体、民主协商小问；整题不计入法律题，法律小问由拆分项承载。
- `CC0094_2025_东城_期末_19_3` -> `split_or_deduplicate` / `pending_split_not_open`: GPT 修正：不能整题 keep_reference_open。小问法律+政治混合，且当前 rubric atoms 串到新能源/欧盟/贸易保护；须拆出法律 2 分相邻关系后再决定。
- `CC0118_2025_丰台_期末_18_2` -> `reextract_needed` / `duplicate_or_reextract_pending`: 当前行绑定经济题；后续 PPT 才出现尹某劳动合同裁判反馈，可能与 CC0119 去重，需定向重抽。
- `CC0259_2026_丰台_期中_19` -> `reextract_needed` / `pending_missing_legal_rubric`: 题面显示遗赠扶养协议，但 rubric atoms 严重串入经济/逻辑/全球倡议；补到正式法律细则前不得进入归纳或满分闭环。
- `CC0305_2026_海淀_一模_18` -> `split_parent` / `not_counted_parent_unit`: 父题前两问为消费数据/经济意义；只拆 Q18(3) 法律小问，父题不计入法律题。
- `CC0363_2026_通州_期中_19` -> `split_or_deduplicate_parent` / `not_counted_parent_unit`: 父题含法律相邻加装电梯与逻辑推理；法律小问已由 CC0364 PASS 承载，父题不重复计数。
- `CC0373_2026_顺义_一模_17` -> `split_parent` / `not_counted_parent_unit`: 原行首为 Q17 政治题，后续 slide 有 Q18 劳动就业歧视/竞业限制法律细则；父题不计。
- `CC0380_2026_顺义_二模_18` -> `reextract_needed` / `not_counted_parent_unit`: 整题含逻辑与开源智能体法律小问，当前 atoms 只抽逻辑；需重抽 Q18(2)。
- `CC0259_2026_丰台_期中_19_LAW` -> `pending_reextract_missing_legal_rubric` / `pending_missing_legal_rubric`: 跟踪待补：遗赠扶养协议题面明确，但正式法律细则未匹配，暂不入框架归纳或宝典闭环。
- `CC0118_2025_丰台_期末_18_2_LAW` -> `duplicate_or_reextract_pending` / `duplicate_or_reextract_pending`: 跟踪待核：尹某劳动合同小问可能是 CC0119 学生问题页，不宜新增计数。

### Excluded Rows
- `CC0001_2024_丰台_一模_16` -> `exclude_duplicate_mismatch` / `excluded`: 剔除：Q16 正文/细则是《政治与法治》四下基层，ask_text 串入 CC0002 法律题。
- `CC0026_2024_朝阳_二模_18` -> `exclude_nonlaw` / `excluded`: 剔除：细则主干为《政治与法治》全过程人民民主，另有选择题/OCR 串页。
- `CC0047_2024_海淀_二模_21` -> `exclude_nonlaw` / `excluded`: 剔除：新质/民生综合题，采分来自党、制度、经济、治理、文化等模块。
- `CC0070_2024_顺义_二模_19` -> `exclude_nonlaw` / `excluded`: 剔除：经济/国际/马克思主义中国化综合题，非法律规则采分。
- `CC0132_2025_房山_一模_20` -> `exclude_nonlaw` / `excluded`: 剔除：奋斗主题综合论述，非法律规则采分。
- `CC0168_2025_海淀_二模_20` -> `exclude_nonlaw` / `excluded`: 剔除：共享发展/国际组织/粮食安全等非选必二法律采分。
- `CC0182_2025_海淀_期末_22` -> `exclude_nonlaw` / `excluded`: 剔除：愚公精神综合论述，法律片段为串页或干扰。
- `CC0218_2025_顺义_一模_16` -> `exclude_nonlaw` / `excluded`: 剔除：哪吒、哲学与文化、联系发展矛盾等采分，非法律题。
- `CC0240_2026_东城_二模_21` -> `exclude_nonlaw` / `excluded`: 剔除：金融五篇大文章/党和政府经济职能/辩证思维。
- `CC0250_2026_丰台_一模_19` -> `exclude_nonlaw` / `excluded`: GPT 明确要求从 v2 开放容器删除：本题为人类命运共同体/2030 议程/可持续发展，复练页法律提示不能带动恢复。
- `CC0294_2026_朝阳_二模_20_2` -> `exclude_nonlaw` / `excluded`: 剔除：当代国际政治与经济/人类命运共同体/系统思维串页，非法律主观题。
- `CC0358_2026_通州_一模_17` -> `exclude_nonlaw` / `excluded`: 剔除：实际为《逻辑与思维》辩证思维看 AI，隐私/法律治理只是材料风险词。

## Governor Effect
- Existing v2 and final handbook are now `provisional_boundary_patch_required`, not final classroom release.
- Next minimal step is atom/evidence-map patching, beginning with `CC0229`, then split records `CC0305_18_3`, `CC0373_18`, and `CC0380_18_2`.
