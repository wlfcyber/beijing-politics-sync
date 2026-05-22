根据 2026-05-19 的 Guarded v2 进度包与我对 zip 内 CSV、MD 文件的交叉核验，结论是：**当前 65 题 corpus 与 guarded v2 可以作为事实基线继续工作，但不能宣称 final full closure。** 主要问题集中在成稿层与少量 atom 分类层，尤其是把学生问题、教学建议、其他题答案混入逐题满分句的现象。

# ACCEPTABLE_PROGRESS

1. **65 题 factual baseline 可接受。**
   我核验到 `merged_subjective_law_questions.csv` 为 65 行，`formal 61`、`reference_only 4`、`missing 0`。`merged_rubric_atoms_subjective.csv` 为 370 行，与进度包所称 CC0143 scoring-only patch 后口径一致。

2. **guarded v2 可作为当前工作基线。**
   `framework_v1_2_question_by_question_test_20260519.csv` 与 `question_by_question_framework_runs.csv` 均显示 `PASS 46`、`PARTIAL 19`、`FAIL 0`。`baodian_label` 分布也能对上：`core_full_score_supported 44`、`boundary_non_core 2`、`formal_open_container_partial 14`、`reference_only_demo 4`、`open_container_only 1`。

3. **44 core + 2 boundary + 19 partial policy 证据安全。**
   条件是必须继续保留两层结构：44 个 core row 可作为核心满分支持，2 个 boundary row 只能算边界 gate pass，19 个 PARTIAL 不能升级为核心模板。

4. **CODE_COWORK_008 当前裁剪版可保留。**
   当前 codebook 已把 `CC0143` 从知识产权/不正当竞争链中排除，并把 `RECOVER_2026_西城_二模_18_2` 留作 open container。这个处理符合前轮审议意见。

5. **reference_only 没有被 codebook 核心节点吸收。**
   当前 8 条 codebook 的 supporting question 均为 formal，没有 reference_only 被拿来支撑核心 code。这个底线是守住的。

# BLOCKERS_BEFORE_FINAL_CLAIM

1. **不能宣称 65 题全部核心满分闭环。**
   当前只能说：44 个 core row 有核心满分支持，2 个 boundary row 被正确挡出，19 个 row 仅作 partial/open/reference 展示。

2. **DOCX visual QA 仍是 blocker。**
   `DOCX_QA_GUARDED_V2.md` 显示 DOCX 结构有效，Quick Look 首页通过，但 full Word/PDF page-by-page visual QA 未闭合。最终交付前必须补做整篇渲染检查。

3. **逐题示范存在内容污染。**
   `CC0150` 混入第 21 题《当代国际政治与经济》答案，`CC0251` 混入学生问题、建议、复练试题，`CC0245` 混入教学建议，`CC0077`、`CC0084` 混入学生问题段。这些不能留在满分句或完整答案中。

4. **部分 teaching/problem atom 仍在 support 字段。**
   `R_CC0077_2025_东城_一模_19_07`、`R_CC0084_2025_东城_二模_19_07`、`R_CC0244_2026_东城_期末_18_08`、`R_CC0245_2026_东城_期末_18_2_02`、`R_CC0245_2026_东城_期末_18_2_04` 应从 supporting_rubric_atom_ids 中移出，最多作为 risk evidence 或 common failure path。

5. **CODE_COWORK_007 在 framework 层仍过宽。**
   codebook reason 已写明需要拆成 issue-spotting/compliance 与 procedure-remedy/entity-request subpatterns，但 framework v2 仍合并为 `程序维权三层`。这会误导 `CC0092`、`CC0277` 这类法律边界识别题，也会误导调解题和公益诉讼题。

6. **CC0143 metadata 需对齐。**
   `question_by_question_test` 中 `CC0143` 的 `expansion_status` 仍是 `NO_EXPANSION_SUPPORT_YET`，但 codebook 与 baodian 已按 after atom patch 作为 core。需要改成 `CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH` 或等价标签。

7. **宝典里的标题和栏目名会放大误读风险。**
   `第一部分：最终主观题框架`、`高频满分句库`、partial/reference/boundary 行中的 `满分句` 栏目，需要加 guarded 限定或改名。尤其 open/reference/boundary 行不能出现让学生误以为可迁移满分模板的标题。

# ROW_LEVEL_PATCH_TABLE

```tsv
question_id	current_label	decision	required_patch	evidence_needed	severity
CC0077_2025_东城_一模_19	core_full_score_supported	keep_core_after_trim	逐题满分句只保留R_CC0077_2025_东城_一模_19_02到R_CC0077_2025_东城_一模_19_04的 scoring 内容；R05到R12移动到易错路径或risk evidence，不能进入满分句	无需新回源；用现有formal scoring atoms，重新生成该题输出	HIGH
CC0084_2025_东城_二模_19	core_full_score_supported	keep_core_after_trim	逐题满分句只保留R_CC0084_2025_东城_二模_19_02到R_CC0084_2025_东城_二模_19_05的 scoring 内容；R06到R11移动到易错路径或risk evidence	无需新回源；用现有formal scoring atoms，重新生成该题输出	HIGH
CC0150_2025_朝阳_二模_20	core_full_score_supported	keep_core_after_trim	从rubric_atom_ids_matched、full_score_sentence_generated、complete_answer_generated中删除R_CC0150_2025_朝阳_二模_20_12到R24及全部当代国际政治与经济内容；只保留第20题法律与生活部分	无需新回源；本地trim即可；如保留20(2)，限R10到R11的拆除设备、清除信息	HIGH
CC0245_2026_东城_期末_18_2	core_full_score_supported	keep_core_after_atom_split	将R_CC0245_2026_东城_期末_18_2_01拆成维权途径、证据准备、权利义务与合理诉求三个 scoring patch atoms；R02到R04仅作易错提醒，不能作为supporting_rubric_atom_ids或满分句	需要本地atom split，不需外部新证据	HIGH
CC0251_2026_丰台_一模_20	core_full_score_supported	keep_core_after_trim_or_split	只使用R_CC0251_2026_丰台_一模_20_01作为该题scoring依据，或把R01拆成锚句、规则、事实、意义四个patch atoms；R02到R16从满分句和complete answer移出	需要本地atom split；不得使用学生问题、建议、复练试题作scoring	HIGH
CC0143_2025_朝阳_一模_19	core_full_score_supported	metadata_patch	将framework_v1_2_question_by_question_test中的expansion_status由NO_EXPANSION_SUPPORT_YET改为CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH；继续禁止R11到R25进入core support	无需新证据；使用PATCH_CC0143_CONTRACT_CHAIN_R01、PATCH_CC0143_CONSUMER_TRIPLE_COMP_R02及scoring R02到R10	MEDIUM
CC0092_2025_东城_期末_19_1	core_full_score_supported	remap_to_007A	该题是法律问题识别，不应使用协商未果、程序路径、实体请求作为minimum judgment；改挂CODE_COWORK_007A法律边界识别与合规措施	无需新回源；基于R_CC0092_2025_东城_期末_19_1_01	MEDIUM
CC0277_2026_房山_二模_18	core_full_score_supported	remap_to_007A	该题是AI场景法律边界和应对措施，不应按程序维权三层启动；改挂CODE_COWORK_007A法律边界识别与合规措施	无需新回源；基于R_CC0277_2026_房山_二模_18_04到R06及相关风险识别atoms	MEDIUM
CC0125_2025_延庆_一模_19	core_full_score_supported	remap_to_007C	该题是调解方案和理由，不应只用程序救济模板；改挂CODE_COWORK_007C调解方案与合同诚信理由	无需新回源；基于R_CC0125_2025_延庆_一模_19_M17_01到M17_05	MEDIUM
RECOVER_2024_东城_二模_19_1	core_full_score_supported	remap_to_007B	该题是起诉状任务，应单列诉讼请求、事实、法律依据三个动作，不能只写程序路径加实体请求	无需新回源；基于RECOVER_2024_东城_二模_19_1_R01到R03	MEDIUM
RECOVER_2026_门头沟_一模_18_1	core_full_score_supported	remap_to_007D	该题是公益诉讼、多元解纷和司法确认，不宜被普通私权维权模板覆盖；改挂公益诉讼与司法确认子型	无需新回源；基于RECOVER_2026_门头沟_一模_18_1_R01到R03	MEDIUM
RECOVER_2026_西城_二模_18_2	open_container_only	stronger_warning	保留open_container_only；逐题示范中的满分句改为开放容器题内参考句，明确不得迁移为AI产业核心模板	无需新证据；等待重复formal同型题	MEDIUM
CC0276_2026_房山_二模_17	boundary_non_core	pass_subtype_patch	PASS必须标成boundary_gate_pass，不能与core PASS混读；逐题示范继续不生成选必二核心满分句	无需新证据；保持边界附录	MEDIUM
RECOVER_2026_西城_二模_18_3	boundary_non_core	pass_subtype_patch	PASS必须标成boundary_gate_pass；国家治理能力现代化题继续禁止进入CODE_COWORK_002意义节点	无需新证据；保持边界附录	MEDIUM
CC0040_2024_海淀_一模_19	reference_only_demo	stronger_warning	逐题示范中的满分句改为reference_only参考答案句；不得进入CODE_COWORK_008或任何核心节点	若要升级，必须补formal细则	MEDIUM
CC0162_2025_海淀_一模_18	reference_only_demo	stronger_warning	逐题示范中的满分句改为reference_only参考答案句；不得作为格式合同或知识产权融资核心支持	若要升级，必须补formal细则	MEDIUM
CC0311_2026_海淀_二模_18_2	reference_only_demo	stronger_warning	逐题示范中的满分句改为reference_only参考答案句；不得作为数字人或AI题核心支持	若要升级，必须补formal细则	MEDIUM
CC0353_2026_西城_期末_17	reference_only_demo	stronger_warning	逐题示范中的满分句改为reference_only参考答案句；不得作为青少年模式或未成年人保护核心支持	若要升级，必须补formal细则	MEDIUM
```

# FRAMEWORK_PATCH_TABLE

```tsv
node_id_or_file	issue	required_patch	why	severity
08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.csv CODE_COWORK_001	supporting_rubric_atom_ids含R_CC0077_2025_东城_一模_19_07和R_CC0084_2025_东城_二模_19_07，这两项是学生问题或不得分提醒	把这些ID移到risk_evidence_ids或counterexamples；core support改用R_CC0077_02到R04、R_CC0084_02到R05等正向scoring atoms	学生问题、典型错误不能当scoring support	HIGH
08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.csv CODE_COWORK_006	使用R_CC0244_2026_东城_期末_18_08支撑合同/侵权四链，但该atom主要是建议与一般逻辑提醒	将R08转为risk evidence；用R_CC0244_03和R_CC0244_05支撑合同成立有效、违约、侵权责任链	避免把教学建议当评分原子	HIGH
08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.csv CODE_COWORK_007	R_CC0245_2026_东城_期末_18_2_02和R04是教学建议或典型问题，却被纳入supporting_rubric_atom_ids	从support中移除R02到R04；把R01拆为实际scoring patch atoms；保留R02到R04为易错提醒	当前写法违反证据纪律	HIGH
FWV1_2_N06 程序维权三层	CODE_COWORK_007的四类题被合并成一个程序维权模板	拆为007A法律边界识别与合规措施、007B诉讼请求或起诉状、007C调解方案与理由、007D公益诉讼与司法确认	CC0092、CC0277、CC0125、RECOVER_2026_门头沟_一模_18_1的启动判断不同	HIGH
FWV1_2_N07 意义收束三层	CC0143是2分意义尾巴，不能证明独立三层意义题	把CC0143标为limited value-tail support；三层意义节点的主支撑仍用CC0002、CC0019、CC0054、CC0045、CC0063、CC0223等	防止把任意价值尾句都套成三层意义模板	MEDIUM
10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv	CC0143仍显示NO_EXPANSION_SUPPORT_YET	改为CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH或等价字段	状态字段与codebook、baodian_label不一致	MEDIUM
11_final_framework/framework_v2.md	文件内还嵌入Framework v1.2 pressure-test标题，容易混淆v2与v1.2	删除或降级v1.2标题，只保留guarded v2框架说明	成稿结构不够干净	LOW
11_final_framework/framework_v2_evidence_map.csv	FWV1_2_GATE和FWV1_2_OPEN出现在同一个evidence_map中，容易被误读为普通节点	增加node_class字段：core_node、boundary_gate、open_container；对应sentence bank同步标注	防止boundary/open被误作满分模板	MEDIUM
12_final_baodian/full_score_sentence_bank.csv	边界和open rows进入高频满分句库	把FWV1_2_GATE、FWV1_2_OPEN移到non_core_guardrail_sentence_bank，或保留但node_class明确为non_core	高频满分句库名称会诱导迁移	MEDIUM
04_merge_audit/merged_rubric_atoms_subjective.csv	CC0150混入第21题国际政治经济内容	将R_CC0150_12到R24从CC0150法律主观题rubric匹配链中移除或单独归档为非本工程题目	逐题答案污染	HIGH
04_merge_audit/merged_rubric_atoms_subjective.csv	CC0251混入学生问题、建议、复练试题	只保留R01为scoring基础，R02到R16改为risk或discard；必要时拆R01为patch atoms	逐题答案污染	HIGH
```

# BAODIAN_PATCH_TABLE

```tsv
section_or_file	issue	required_patch	why	severity
12_final_baodian/选必二法律主观题满分宝典.md 标题与第一部分	第一部分写最终主观题框架，容易被解读为final closure	改为guarded v2核心路径框架或阶段性守门框架，并保留44 core、2 boundary、19 partial声明	当前证据不能支持65题全部核心闭环	MEDIUM
12_final_baodian/选必二法律主观题满分宝典.md 第三部分	partial、reference、boundary行仍使用细则对应与满分句栏目	按label改栏目：core用满分句，formal_open_container用题内参考句，reference_only用参考答案句，boundary用边界说明	避免学生把非核心行当可迁移满分模板	HIGH
12_final_baodian/选必二法律主观题满分宝典.md CC0150逐题示范	混入第21题当代国际政治与经济答案	删除第21题全部内容，只保留第20题法律与生活评分内容	非本工程内容污染满分答案	HIGH
12_final_baodian/选必二法律主观题满分宝典.md CC0251逐题示范	混入学生问题、建议、复练试题	删除R02到R16对应内容，只保留或拆分R01 scoring答案	教学建议不能进入满分答案	HIGH
12_final_baodian/选必二法律主观题满分宝典.md CC0245逐题示范	混入继续短周期、反复训练等教学建议	删除R02到R04对应文本；改写为维权途径、证据准备、合理诉求三项	教学建议不能当作学生答案	HIGH
12_final_baodian/选必二法律主观题满分宝典.md CC0077逐题示范	满分句混入学生问题段	保留R02到R04 scoring句；学生问题移到易错路径	满分句需要只呈现得分表达	MEDIUM
12_final_baodian/选必二法律主观题满分宝典.md CC0084逐题示范	满分句混入学生表现和问题	保留R02到R05 scoring句；R06到R11移到易错路径	满分句需要只呈现得分表达	MEDIUM
12_final_baodian/选必二法律主观题满分宝典.md 高频满分句库	FWV1_2_GATE和FWV1_2_OPEN位于满分句库	移至边界与开放容器警戒库，或在标题中显式标注非核心	防止boundary/open被当成高频模板	MEDIUM
12_final_baodian/question_by_question_framework_runs.csv	部分core row的complete_answer_generated仍是细则拼贴	核心行应重新生成考场可写句；非核心行保持参考标签	当前成稿可审计，但不适合直接发学生	HIGH
12_final_baodian/DOCX_QA_GUARDED_V2.md	仅结构检查和首页Quick Look通过	必须完成整篇Word或PDF逐页视觉QA，并记录页码、溢出、乱码、标题层级、目录与分页	最终交付前的文档质量门槛未闭合	HIGH
```

# CAN_CONTINUE_TO_NEXT_STEP

**YES_WITH_GUARDS**

Codex 可以继续，但下一步应限定为 **本地证据清洗、框架守门修补、成稿视觉QA**，不能进入 final full closure 宣传。

具体执行顺序：

1. 先清洗 atom 分类：把学生问题、教学建议、典型错误、其他题答案从 scoring support 中移出。
2. 对 `CC0245`、`CC0251` 做本地 atom split；对 `CC0150` 做跨题污染 trim。
3. 重新生成 codebook evidence map，确保 core support 字段只含 scoring 或明确 patch scoring atoms。
4. 将 `CODE_COWORK_007` 在 framework 层拆成子型，再回填逐题入口。
5. 重跑 `question_by_question_framework_runs.csv`，检查所有 `full_score_sentence_generated` 不再含学生问题、复练试题、教学建议、其他模块答案。
6. 重写宝典对应行的栏目名，partial/reference/boundary 不再使用满分句标签。
7. 完成 DOCX full Word/PDF page-by-page visual QA。
8. 最终表述只能写 guarded v2 核心路径可教学，不能写 65 题全部核心满分闭环。
