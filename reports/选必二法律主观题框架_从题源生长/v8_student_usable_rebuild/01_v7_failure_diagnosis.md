# v8 STEP 01｜v7.1 / boundary-patched 学生可用性失败诊断

- generated_at: 2026-05-21T17:21:24
- verdict: `FAIL_TO_REBUILD`
- rule: 本诊断只做诊断，不改正文，不生成总框架。

## 0. 语料口径确认

- boundary-patched questions: 53
- material atoms: 535
- ask atoms: 53
- rubric atoms: 319
- coverage: 37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE
- pending not in closed body: CC0094_2025_东城_期末_19_3; CC0259_2026_丰台_期中_19; CC0118_2025_丰台_期末_18_2
- excluded: CC0250_2026_丰台_一模_19
- CC0229 bad words scan: 当前指定正文文件未发现“逃逸粒子 / 创新资源集聚 / 空间布局精准 / 全链条产业生态”。

## 1. 总判定

v7.1 / 当前 boundary-patched 成品不能作为学生可用最终版。它更像“guarded 工程验收包 + 证据侧栏 + 答案汇编”，不是学生考场框架。最大问题不是排版，而是学生动作缺失：学生看完后仍不稳定知道“第一眼看什么、先判断什么、材料如何转法律语言、哪一句能贴细则”。

### 状态统计

| layer | PASS | PARTIAL | FAIL |
|---|---:|---:|---:|
| A_framework | 0 | 5 | 4 |
| B_question_run | 0 | 30 | 23 |
| C_sentence_bank | 0 | 2 | 1 |
| D_evidence_boundary | 5 | 0 | 1 |
| E_student_usability | 0 | 5 | 2 |

## 2. A 框架层诊断

| 检查项 | 结论 | 关键证据 | v8 修复方向 |
|---|---|---|---|
| 是否只是法律知识/工程分类 | FAIL | 正文标题和首屏仍是 guarded v2 / Framework v2 / Status / Validation Position，学生首先看到的是工程验收语言而不是考场动作。（12_final_baodian/选必二法律主观题满分宝典.md:1-31） | v8 首章必须改为学生场景：看到设问先交什么成品、看到材料先圈什么事实、第一句怎么写。 |
| 是否有清晰考场入口 | PARTIAL | One-Minute Student Version 有“先挡边界/看设问/判关系”，但没有把具体设问触发词映射为第一步动作，且仍混入低频/开放容器表述。（12_final_baodian/选必二法律主观题满分宝典.md:22-30） | 重写为“看见/先判/再转/这样写/别这样写”短框架，不放证据和工程状态。 |
| 学生是否知道第一步看什么 | PARTIAL | 当前写了“再看设问”，但节点顺序从边界和六类候选展开，学生遇到合同/侵权/表格/价值题时仍不知道第一句先表态、先分主体还是先填表格。（12_final_baodian/选必二法律主观题满分宝典.md:22-31） | 以“设问交付物”为第一层：表态判断、裁判理由、表格补全、维权路径、意义价值、开放边界。 |
| 节点是否有看到什么—判断什么—写什么—别写什么 | FAIL | 节点正文有学生启动/教师解释/证据/风险，但不是统一的考场动作格式；学生无法一眼复制运行。（12_final_baodian/选必二法律主观题满分宝典.md:31-180） | 每个节点必须固定五栏：看见、先判、再转、这样写、别这样写。 |
| 节点名称是否学生能记住 | PARTIAL | “表格一格一答”较可用，但“私法案例四链”“裁判锚句起手”“意义收束三层”仍像教研术语，不够像考场动作。（12_final_baodian/full_score_sentence_bank.csv:2-13） | 节点名改成学生动作短句，如“先表态”“一格一句”“先分谁告谁”“价值从规则长出来”。 |
| 节点是否太抽象/太细碎 | PARTIAL | 12 个句库节点里既有边界 gate、open container，又有责任链/公益诉讼等，学生层没有压成极短主干。（12_final_baodian/full_score_sentence_bank.csv:1-13） | 学生层压到 5-7 个动作；教师层再保留证据节点。 |
| 节点是否能生成答案句 | PARTIAL | 节点有 sentence_template，但多数是泛模板；不能直接告诉学生材料中哪类事实替换到哪一格。（12_final_baodian/full_score_sentence_bank.csv:3-12） | 满分句库改成“材料信号 -> 法律语言 -> 关键词 -> 推荐考场句”。 |
| 当前口径是否符合 53 题闭合基准 | FAIL | 当前宝典首页和验证摘要仍写 65 questions / 61 formal / 4 reference_only；用户本轮要求唯一闭合语料为 53 boundary-patched corpus。（12_final_baodian/选必二法律主观题满分宝典.md:11-14,3114-3144） | v8 全部正文改为 53 题口径：37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE，65 只能放历史说明或不用。 |
| v7.1 zip 是否可直接作为 v8 基底 | FAIL | v7.1 候选稿基于“65 道法律题”并有 source-card repair 队列，和本轮指定 53 题闭合语料不一致；只能作为失败样本和方法参考。（05_reasoner_packets/v7_1_core_artifacts_for_user_gpt_20260521/01_CURRENT_V7_1_CANDIDATE_BAODIAN.md:1-25） | v8 只能回到 boundary_patched_20260519 53 题重建；v7.1 的八门等说法需重新用 53 题验证。 |

## 3. B 逐题运行层诊断

- 逐题行数：53
- 设问触发缺失/需回源：23 行
- 最小必要判断为同一句泛话：53 行
- 满分句/完整答案疑似答案或细则摘抄：24 行
- OPEN_OR_REFERENCE：5 行，只能参考运行，不能支撑核心节点

### 逐题严格格式结论

| question_id | pass_status | strict_v8_status | 主要问题 |
|---|---|---|---|
| CC0002_2024_丰台_一模_17 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0011_2024_丰台_二模_17 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0019_2024_朝阳_一模_19 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0025_2024_朝阳_二模_17 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0040_2024_海淀_一模_19 | OPEN_OR_REFERENCE | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path；open_or_ |
| CC0045_2024_海淀_二模_19 | PASS_RECOVERED | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0051_2024_海淀_期中_21_1 | PASS_RECOVERED | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0054_2024_石景山_一模_17 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0061_2024_西城_一模_18 | PASS_RECOVERED | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0063_2024_西城_二模_16 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0077_2025_东城_一模_19 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0084_2025_东城_二模_19 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0092_2025_东城_期末_19_1 | PASS_RECOVERED | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0103_2025_丰台_一模_19 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0119_2025_丰台_期末_19 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0125_2025_延庆_一模_19 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0131_2025_房山_一模_19 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0137_2025_昌平_二模_20 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0143_2025_朝阳_一模_19 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0150_2025_朝阳_二模_20 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0157_2025_朝阳_期末_20 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0162_2025_海淀_一模_18 | OPEN_OR_REFERENCE | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path；open_or_ |
| CC0180_2025_海淀_期末_20 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0181_2025_海淀_期末_21 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0189_2025_石景山_一模_20 | PASS_RECOVERED | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0195_2025_西城_一模_20 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0200_2025_西城_二模_18 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0206_2025_西城_期末_19 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0213_2025_门头沟_一模_20 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0214_2025_门头沟_一模_20_2 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0223_2025_顺义_一模_19 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0229_2026_东城_一模_18 | PASS_RECOVERED | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0238_2026_东城_二模_19 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0244_2026_东城_期中_18 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0245_2026_东城_期中_18_2 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0251_2026_丰台_一模_20 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0254_2026_丰台_二模_18 | PASS | PARTIAL | generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one_by_one；no_real_wrong_path |
| CC0276_2026_房山_二模_17 | PASS_RECOVERED | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0277_2026_房山_二模_18 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0283_2026_朝阳_一模_18 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0289_2026_朝阳_二模_18 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0311_2026_海淀_二模_18 | OPEN_OR_REFERENCE | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0317_2026_海淀_期中_18 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0318_2026_海淀_期中_18_2 | PASS_RECOVERED | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0319_2026_海淀_期中_19 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0325_2026_石景山_一模_18 | PASS | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_st |
| CC0332_2026_石景山_二模_19 | PASS_RECOVERED | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0340_2026_西城_一模_17 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0353_2026_西城_期中_17 | OPEN_OR_REFERENCE | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0364_2026_通州_期中_19_1 | PASS | PARTIAL | generic_minimum_judgment；answer_or_rubric_dump_not_transfer_sentence；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_expl |
| CC0305_2026_海淀_一模_18_3 | PASS_RECOVERED | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0373_2026_顺义_一模_18 | PASS_RECOVERED | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |
| CC0380_2026_顺义_二模_18_2 | OPEN_OR_REFERENCE | FAIL | ask_trigger_missing_or_unrecovered；generic_minimum_judgment；raw_material_pipe_not_layered_for_student；rubric_ids_exist_but_not_explained_one |

## 4. C 满分句库层诊断

- **FAIL｜是否只是摘答案/节点模板**：现有句库只有 12 行节点模板，不是逐条可背可替换的满分句；字段是 node_class/supporting ids/usage_condition，不是材料信号/设问类型/必写关键词/禁止场景。 修复：重写为每条句子一行：适用材料信号、适用设问类型、句式模板、关键词、必须带入材料、禁止乱用、推荐考场版本。 位置：12_final_baodian/full_score_sentence_bank.csv:1-13。
- **PARTIAL｜是否有使用条件和材料触发**：有 usage_condition 和 do_not_use_when，但多为工程化长句，含 GPT/Claude 风险说明，不适合学生背诵。 修复：学生句库只保留短触发和短禁用；模型审稿语移入教师证据版。 位置：12_final_baodian/full_score_sentence_bank.csv:3-12。
- **PARTIAL｜是否有空泛价值套话/法考化风险**：风险有记录，但句库本身仍有“意义收束三层”等容易诱导套话；私法案例四链又容易诱导法考构成要件。 修复：每条句子强制绑定“本案材料事实”，并给“空写版本/推荐版本”对照。 位置：12_final_baodian/full_score_sentence_bank.csv:6,12。

## 5. D 证据边界层诊断

- **PASS｜OPEN_OR_REFERENCE 是否单独支撑核心节点**：句库 core_node 支撑题中未发现 QUESTION_COVERAGE_MATRIX 标记为 OPEN_OR_REFERENCE 的题；OPEN/边界节点单列存在。 修复：v8 继续保持：OPEN_OR_REFERENCE 只放边界与参考运行，不支撑学生核心节点。 位置：QUESTION_COVERAGE_MATRIX.csv; full_score_sentence_bank.csv。
- **PASS｜pending case 是否回流**：当前指定正文/侧栏文件未检出 CC0094、CC0259、CC0118；旧备份表中有这些记录但不属于当前正文。 修复：v8 打包和宝典正文禁止读取/复制 pre_boundary 备份内容；pending 只进风险章。 位置：current core files scan。
- **PASS｜CC0250 是否回流**：当前指定正文/侧栏文件未检出已剔除 CC0250。 修复：v8 继续禁止 CC0250；只在边界说明写“已剔除”。 位置：current core files scan。
- **PASS｜CC0229 旧坏词是否回流**：当前指定文件未检出“逃逸粒子/创新资源集聚/空间布局精准/全链条产业生态”。 修复：v8 生成后再次全量扫描这些坏词。 位置：current core files scan。
- **FAIL｜证据等级是否在学生版中过度干扰**：学生正文出现 reference_only、Status、Validation Position、corpus/evidence 等工程词，混淆学生版和教师版。 修复：v8 分三层：学生版不出现证据编号/状态词；教师版保留 question_id/material_atom_id/rubric_atom_id。 位置：12_final_baodian/选必二法律主观题满分宝典.md:9-20,179-255。
- **PASS｜教师版是否保留足够证据**：当前教师/侧栏文件保留 coverage matrix、rubric ids、material atoms，可作为 v8 教师版证据源。 修复：教师版按节点重构证据，不直接复制工程报告。 位置：QUESTION_COVERAGE_MATRIX.csv; boundary_patched_20260519/*.csv。

## 6. E 学生可用性诊断

| 场景 | 结论 | 为什么 | v8 必须怎么改 |
|---|---|---|---|
| 人身权/知识产权题 | PARTIAL | 能从私法案例/知识产权节点找到大方向，但学生只看一页框架不能稳定判断先表态还是先说权利保护对象。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。增加“先判保护对象/侵害行为/责任结果”节点和 2 道金样板。 |
| 合同/侵权题 | PARTIAL | 有私法案例四链，但合同成立、违约责任、侵权责任、产品责任在学生层不够分开，易写成混账。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。用金样板拆成“合同链”和“侵权责任链”，每链给第一句。 |
| 劳动/就业题 | FAIL | 学生版没有专门告诉学生劳动题先判劳动关系/从属性/就业歧视/竞业限制，劳动题会被塞进私法案例四链。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。设劳动就业小动作：先判劳动者身份/用工关系/权利限制是否合法。 |
| 纠纷解决题 | PARTIAL | 有程序救济和调解/公益诉讼节点，但学生不知道什么时候写调解、仲裁、诉讼、司法确认。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。建立“路径题先写请求-证据-路径”并用诉讼调解金样板示范。 |
| 制度意义题 | FAIL | 意义收束目前容易变成“维护公平正义/法治中国”，缺“本案规则推出价值”的学生动作。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。价值节点改成：规则保护谁 -> 解决什么冲突 -> 形成什么秩序，禁止裸写必修三。 |
| 避免必修三化 | PARTIAL | 风险提示存在，但学生版仍出现核心价值观、公平正义等收束，缺少“先法律后价值”的硬句式。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。每条价值句必须先带具体法律规则和材料事实。 |
| 避免法考化 | PARTIAL | 风险提示存在，但“私法案例四链”容易诱导构成要件清单；缺高中版限度。 | v8 学生框架必须可独立推出答案；学生测试只看学生版，不看逐题答案。将法考式构成要件改成高中三问：谁的权利/谁的行为/承担什么后果。 |

## 7. 进入 v8 的硬门槛

1. v8 不能从“总框架”开始，必须先写 8 道金样板题。
2. 学生版和教师证据版必须彻底分层：学生版不出现证据编号、reference_only、Status、Validation Position、corpus 统计。
3. 逐题运行必须从“设问怎么进框架”开始，而不是从答案或细则摘抄开始。
4. 满分句库必须由“材料信号 + 设问类型 + 句式模板 + 必写关键词 + 禁用场景”组成。
5. OPEN_OR_REFERENCE 继续降级；pending 三题和 CC0250 不得回流；CC0229 旧坏词继续禁止。

## 8. Step Gate

STEP 01 完成。允许进入 STEP 03：调用 GPT-5.5 Pro 和 Claude Opus 做同题同问诊断与金样板建议。仍禁止写 v8 总框架，直到 8 道金样板题完成。