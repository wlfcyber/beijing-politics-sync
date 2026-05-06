# Codex A Governor - Shunyi Order Final Regate

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

本轮性质：顺义 Q20 答案顺序窄补丁后的最终窄门禁。只判断是否允许进入下一轮内部学生预览和 coverage 扩展；不放行 final、Word、PDF、FINAL_ACCEPTANCE、coverage close。

## 读取文件

- `08_review/confucius_followup_artifact_only_report.md`
- `08_review/confucius_followup_patch_log_20260503.md`
- `07_student_doc/by_question_view_draft_20260503.md`
- `07_student_doc/six_bucket_to_question_crosswalk_draft.md`
- `reports/督工验收状态.md`
- `codex_lane/agents/automation_checker/automation_status_shunyi_order_final.md`

## 结论

`PASS_WITH_GUARD`

允许：
- 进入下一轮内部学生预览。
- 进入 coverage 扩展、题源继续补读、矩阵继续回填和一致性复核。

继续阻断：
- `final`
- `Word`
- `PDF`
- `FINAL_ACCEPTANCE`
- `coverage close`

## 顺义 Q20 窄补丁复查

Confucius 二次报告指出的唯一剩余问题是：顺义 Q20 答题卡示范先写了中国方案，再写南南合作/经济全球化，和“先共同利益、合作共赢，再后置中国方案”的学生迁移逻辑不一致。

最新学生稿已完成窄补丁：

1. 第一段先写“国家间共同利益是国家合作的基础”，并结合科技小院回应全球南方农业生产、降本、人才培养和可持续发展需求。
2. 第二段再写“南南合作和互利共赢”，并连接合作共赢的新型国际关系、经济全球化朝更加开放、包容、普惠、平衡、共赢方向发展。
3. 第三段最后写“中国农业技术、人才培养和发展经验同当地实际结合”，帮助全球南方改善民生、增强内生动力，再写正确义利观和中国方案。
4. 慎用提醒仍保留“共同利益解释为什么能合作；正确义利观解释中国怎样合作”，且明确中国方案、人类命运共同体不能开头当万能帽子。

判定：**顺义 Q20 答题顺序风险已解除，达到内部学生预览下一轮门槛。**

## 学生污染扫描

学生预览文件：

- `07_student_doc/by_question_view_draft_20260503.md`
- `07_student_doc/six_bucket_to_question_crosswalk_draft.md`

复查结果：

- 未发现 `P0/P1/P2/P3` 等证据层级标签进入学生稿。
- 未发现 `Codex/Governor/Patcher/worker/fusion/GPT/Claude` 等后台角色或模型审稿标签进入学生稿。
- 未发现 `/Users/...`、本地路径、SOURCE/LEDGER/COVERAGE、FINAL_ACCEPTANCE 等后台路径或流程词进入学生稿。
- 未发现 `采分点`、`要落到`、`材料中`、`v7` 等学生稿禁入表达。
- 检出的“模型缺陷”“大模型”属于 AI 题目材料和学科语境，不属于后台 model 污染。

判定：**学生污染扫描通过。**

## 桥接与边界复查

- 六桶桥接表仍标明“教学预览版”，没有把本轮稿件写成终稿。
- 顺义 Q20 在桥接表中仍按共同利益、经济全球化完整五词方向、新型国际关系、正确义利观、中国方案等分桶呈现；“中国方案/人类命运共同体”仍有使用条件，不作为开头万能帽。
- 朝阳一模 Q20 的可选升华、海淀二模 Q21 的新型国际关系可选贡献侧、东城/海淀期末拓展迁移题边界仍保留。
- 督工状态仍为“运行中，不能宣布最终完成”；自动化 shunyi_order_final 为 PASS，且未发现 final/Word/PDF/coverage close 误放行语句。

判定：**可以继续内部预览和 coverage 扩展，但不能闭合。**

## 仍需保留的硬阻断

- 不得生成学生正式终稿。
- 不得生成 Word/PDF/DOCX 正式交付。
- 不得写入或宣布 `FINAL_ACCEPTANCE`。
- 不得宣布全书 coverage closed。
- 不得把普通参考答案、P1/P2、拓展迁移题、边界片段升级为 P0 高频核心。
- 不得把外部 GPT/Claude/Confucius 意见作为事实来源；它们只能作为触发本地证据复核的 advisory。

## 下一步允许与必须

允许进入：
- 下一轮内部学生预览。
- coverage 扩展与题源继续补读。
- 按题稿、六桶桥接表、scoring atom、SOURCE_LEDGER、COVERAGE_MATRIX 的一致性回填。

必须继续做：
- Confucius artifact-only 总体验收：只看学生稿本身，测试零基础学生是否会选主桶、辨可选表达、避开万能句。
- coverage 扩展：继续补齐未读套卷、未定位题源、证据等级和条目映射，不得提前 close。
- full-source 复核：继续区分正式评分细则、评标、阅卷/讲评给分口径、用户确认材料和普通参考答案。
- 最终交付前再跑 Governor 总门禁、清洁扫描、桥接一致性扫描、Confucius 学会性验收。

## Governor 最终判定

`INTERNAL_STUDENT_PREVIEW_NEXT_ROUND: PASS_WITH_GUARD`

`COVERAGE_EXPANSION: PASS_WITH_GUARD`

`FINAL_STUDENT_VERSION: BLOCK`

`WORD_PDF_DELIVERY: BLOCK`

`FINAL_ACCEPTANCE: BLOCK`

`COVERAGE_CLOSE: BLOCK`
