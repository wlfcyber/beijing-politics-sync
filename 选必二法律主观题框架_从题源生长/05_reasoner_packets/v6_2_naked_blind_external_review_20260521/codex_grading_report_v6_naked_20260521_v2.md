# V6 裸题盲测 Codex 严判报告 v2

日期：2026-05-21

## 总判

结论：`PASS_WITH_REAL_GUARDS_NOT_FINAL`。

这次测试比 V5.9 有效：样题 A-L 隐去了 question_id、年份区县、core/guard、evidence_level 等后台标签，学生仍能对 7 道 strict core 题基本写出接近细则的答案；对 source-check、reference-only、low-frequency、boundary 题也能保分。但它还不能封版，因为源卡污染、表格形态缺失和 reference-only 前台识别问题仍需要硬处理。

### 统计

- PASS: 4
- PASS_AS_LOW_FREQUENCY: 2
- PASS_AS_SOURCE_CHECK_PRACTICE: 1
- PASS_WITH_BOUNDARY_WARNING: 1
- PASS_WITH_MINOR_PATCH: 1
- PASS_WITH_SOURCE_RISK: 1
- PASS_WITH_SOURCE_SHAPE_GUARD: 1
- REFERENCE_ONLY_CONTENT_PASS: 1

### 关键发现

- A/B 易混组通过了核心压力：A 没写“优化营商环境”，B 能写不正当竞争和法治环境；但 B 还要把“法治化营商环境”写成硬词。
- C 能主动拆两问，说明 V6 的“先拆问号”有效；但 CC0244 canonical ask_text 仍需回源覆盖，不能只靠 derived patch。
- E 表格题能力通过，但裸题包未呈现真实表格列名，只能判“方法会用”，不能判“逐格满分闭合”。
- G/H 暴露 source-card 问题：学生能避开污染材料，但这不能替代 canonical 清洗和回源。
- I 说明裸题无法测试 reference_only 降级意识；证据等级必须由宝典后台/教师版显式管控。

## 逐题严判

### 样题 A｜CC0103_2025_丰台_一模_19

- 类别：strict_core；证据等级：formal。
- 判定：`PASS`；估分：near_full。
- 已踩中：技术秘密；知识产权；惩罚性赔偿；公平市场环境；鼓励创新；同类案件示范；司法公信力。
- 弱项/可能扣分：无实质缺项。。
- 风险：本题最怕误写“优化营商环境”，学生答案明确避开。。
- V6 处理：keep_v6_rule。

### 样题 B｜CC0206_2025_西城_期末_19

- 类别：strict_core；证据等级：formal。
- 判定：`PASS_WITH_MINOR_PATCH`；估分：5.5-6/6。
- 已踩中：有一定影响；混淆误认；攀附商誉；诚实信用；不正当竞争；公平竞争秩序；数字经济法治环境。
- 弱项/可能扣分：未把“法治化营商环境/营商环境”四字写得足够硬，只写了“良好的法治环境”。。
- 风险：CC0103 禁写“优化营商环境”，但 CC0206 奖励“法治化营商环境”，两题必须并排刹车。。
- V6 处理：patch_v6_cc0206_must_write_business_environment。

### 样题 C｜CC0244_2026_东城_期末_18

- 类别：strict_core；证据等级：formal。
- 判定：`PASS`；估分：near_full。
- 已踩中：两问拆分；要约承诺；合同成立有效；违约责任；侵权责任；证据准备；请求设计；协商调解诉讼路径。
- 弱项/可能扣分：生产者无过错责任没有作为主线展开，但学生没有写错为过错推定；以销售者交付安全隐患商品处理可接受。。
- 风险：canonical ask_text 曾只带第（1）问，后续必须使用 derived two-ask patch 或回源覆盖。。
- V6 处理：keep_cc0244_derived_ask_patch_and_source_review。

### 样题 D｜CC0181_2025_海淀_期末_21

- 类别：strict_core；证据等级：formal。
- 判定：`PASS`；估分：near_full。
- 已踩中：商业秘密；知识产权；竞业限制义务；高级管理/技术人员；普通劳动技能；劳动权；择业自由；利益平衡。
- 弱项/可能扣分：无实质缺项。。
- 风险：不能把所有员工都写成竞业限制对象。。
- V6 处理：keep_v6_rule。

### 样题 E｜RECOVER_2026_通州_一模_20

- 类别：strict_core；证据等级：formal。
- 判定：`PASS_WITH_SOURCE_SHAPE_GUARD`；估分：near_full_if_real_table_visible。
- 已踩中：自愿参加；安全保障义务；自身原因；无故意或重大过失；因果关系；公平原则；社区互助。
- 弱项/可能扣分：裸题包未给出真实表格列名，学生只能写“如果表格要求……”。真实考试中必须按格子列名逐格写。。
- 风险：表格题的能力通过，但测试材料形态不完整；不能据此宣称原表格逐格满分已验证。。
- V6 处理：add_v6_table_source_shape_warning。

### 样题 F｜RECOVER_2026_房山_一模_17_1

- 类别：strict_core；证据等级：formal。
- 判定：`PASS`；估分：near_full。
- 已踩中：民事主体；AI 不具备主体资格；意思表示；承诺无效；提示义务；实际损害；因果关系。
- 弱项/可能扣分：无实质缺项。。
- 风险：不能把 AI 写成独立担责主体，也不能写成数字中国宏观题。。
- V6 处理：keep_v6_rule。

### 样题 G｜CC0223_2025_顺义_一模_19

- 类别：strict_core_source_risk；证据等级：formal。
- 判定：`PASS_WITH_SOURCE_RISK`；估分：near_full_if_current_source_accepted。
- 已踩中：权利边界；相邻纠纷；法院调解；企业名称纠纷；行政裁决；行政诉讼；多元纠纷解决；社会和谐。
- 弱项/可能扣分：相邻关系原则未逐字写出“有利生产、方便生活、团结互助、公平合理”，但材料化表达到位。。
- 风险：CC0223 曾有 material atom 污染风险；本次题面已人工清理，仍不能替代回源核验。。
- V6 处理：keep_in_core_but_mark_source_review_priority。

### 样题 H｜CC0137_2025_昌平_二模_20

- 类别：source_check_pending；证据等级：formal。
- 判定：`PASS_AS_SOURCE_CHECK_PRACTICE`；估分：content_pass_not_core_promotion。
- 已踩中：AI 绘图的人类智力投入；独创性；著作权保护；未经许可使用；抹去水印；信用卡合同；透支违约；诚信全面履行。
- 弱项/可能扣分：题面前段混入大量非法律材料，学生能避开，但 canonical source-card 仍需清理。。
- 风险：source_check_pending 不能因学生答得好就升 strict_core。。
- V6 处理：clean_source_card_before_any_promotion。

### 样题 I｜CC0040_2024_海淀_一模_19

- 类别：reference_only_locked；证据等级：reference_only。
- 判定：`REFERENCE_ONLY_CONTENT_PASS`；估分：practice_pass_not_formal_closure。
- 已踩中：虚拟数字人非主体；作品/视频权益；未经许可使用；替换标识；营销信息；不正当竞争；创新与市场秩序。
- 弱项/可能扣分：裸题本身无法让学生识别 evidence_level，因此不能测试 reference_only 降级意识。。
- 风险：本题只能作为练笔表达，不得支撑框架核心节点或 formal 满分闭环。。
- V6 处理：keep_reference_only_front_stage_warning。

### 样题 J｜CC0340_2026_西城_一模_17

- 类别：low_frequency_container；证据等级：formal。
- 判定：`PASS_AS_LOW_FREQUENCY`；估分：near_full。
- 已踩中：绿色原则；物权行使边界；业主义务；停止侵害/排除妨碍/消除危险；用益物权；生态公共利益。
- 弱项/可能扣分：无实质缺项。。
- 风险：不能把低频物权绿色题抬成高频主干。。
- V6 处理：keep_noncore_container。

### 样题 K｜RECOVER_2026_西城_二模_18_2

- 类别：boundary_open_container；证据等级：formal。
- 判定：`PASS_WITH_BOUNDARY_WARNING`；估分：near_full_for_law_layer。
- 已踩中：AI 不具备民事主体；承诺不当然有效；提示管理注意义务；实际损害；因果关系；稳定预期；用户权益与创新平衡。
- 弱项/可能扣分：如果原题同时要求其他模块，学生还需另开非法律模块段；本测试只验证法律层。。
- 风险：边界开放题不能被私法模板吃掉，也不能写成纯产业乐观。。
- V6 处理：keep_boundary_open_container。

### 样题 L｜RECOVER_2024_东城_一模_19

- 类别：low_frequency_container；证据等级：formal。
- 判定：`PASS_AS_LOW_FREQUENCY`；估分：near_full。
- 已踩中：诉讼时效；及时主张权利；稳定法律关系；拒绝给付抗辩；赡养义务；基本生活保障；保护老年人权益。
- 弱项/可能扣分：无实质缺项。。
- 风险：不能把赡养费写成普通借款，也不能机械套“过期不保护”。。
- V6 处理：keep_noncore_container。

## 必须进入 V6.1 的补丁

1. 把 CC0206 的“法治化营商环境/营商环境”从可写词升级为必须词，并继续保留 CC0103 禁写“优化营商环境”的反向刹车。
2. 在表格题规则中增加一句：裸题训练若看不到真实表格，只能练方法；真实考试必须按列名逐格作答。
3. 在 source-check 区增加前台红线：会写不等于可升核心，必须回源清洗题面和细则。
4. 在 reference-only 区增加前台红线：学生可练表达，教师不得说这题已 formal 满分闭环。
5. 把 canonical source-card 污染列入下一轮优先清洗：CC0223、CC0137、CC0244。

