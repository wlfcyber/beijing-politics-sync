你是 GPT-5.5 Pro，本轮只做 Phase12 student-clean candidate 的 post-patch 复审。

重要边界：

1. 不要扩题，不要要求重扫 362，不要讨论 Word 版式。
2. 只复审上一轮你给出的 `PATCH_REQUIRED_NO_WORD` 中的 must_fix / should_fix 是否已经关闭。
3. 若所有阻断已关闭，请给 verdict=`CLEAN_PASS_TO_WORD_PREP`。
4. 若仍有阻断，请给 verdict=`PATCH_REQUIRED_NO_WORD`，只列仍阻断的具体题目和修法。
5. 不要把 Word/PDF/final 直接授权成终稿；最多允许进入 Word prep 前置门。

本轮已上传 post-patch packet，里面包括：

- 修补后的学生正文：`phase12_student_clean_candidate.md`
- 修补后的推理索引：`phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md`
- 修补后的思维索引：`phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md`
- traceability matrix
- 上一轮 GPT raw/digest
- 本轮 Codex patch resolution/audit
- `2024 西城一模第11题` 官方锁定文件

请重点复审：

1. `2024 西城一模第11题`
   - 上轮你指出 B、①③、①④ 冲突。
   - 本地官方锁定是：正确答案 B，且 B=①③；选项为 A=①② / B=①③ / C=②④ / D=③④。
   - 请只检查正文是否已经内部一致，不要按上一轮条件句把它误改成 B=①④。

2. `2026 丰台一模第18题第(2)问`
   - 是否补齐材料信号、设问、为什么能想到。
   - 甲是否清楚写成必要条件假言推理；乙是否清楚写成三段论大项不当扩大。

3. `2025 东城期末第13题`
   - 推理索引是否已经改为：①③中项不周延；②大项不当扩大；④四概念。
   - 不得把②写成小项不当扩大。

4. `2024 朝阳二模第19题第(2)问`
   - 是否已经从思维方法索引的辩证思维/分析与综合正向节点移除。
   - 是否只保留在推理索引的联言判断与联言推理下。

5. `2025 海淀二模第20题`
   - 同类题索引中是否已经删除 `2024 朝阳二模第19题第(2)问`。
   - 可保留 `2024 朝阳二模第19题第(1)问`。

6. should_fix
   - `2026 丰台一模第8题` 是否补入限制换位链条，并进入充分条件假言推理的易混选择题。
   - `2026 东城期末第7题` 是否补了形式化表达和逐项代入逻辑。
   - 双索引标签是否已经学生化为 `可正用例 / 相关检索 / 易混选择题 / 边界提醒`。

请输出：

- verdict
- still_blocking
- closed_items
- optional_should_fix
- word_prep_permission: yes/no
- final_permission: no
