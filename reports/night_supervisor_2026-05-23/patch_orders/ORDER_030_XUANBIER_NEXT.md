# ORDER_030_XUANBIER_NEXT

状态：`MUST_PATCH_BEFORE_STRICT_FINAL`

对象：选必二《法律与生活》v13.10 后续生产/治理线程  
当前目录：`reports/选必二法律主观题框架_从题源生长/v12_2_framework_growth_restart/v13_10_final_baodian_integrated`

## 总命令

不要覆盖 v13.10 成品目录。下一步必须新建候选目录：

`reports/选必二法律主观题框架_从题源生长/v12_2_framework_growth_restart/v13_11_strict_acceptance_patch`

v13.10 只能作为只读输入。所有补丁、复核、截图、模型输出、QA、Governor 都写入 v13.11 目录或夜间总控目录。

## PATCH-030-1：真实 GPT/Claude delta 复核

建立 `MODEL_DELTA_PACKET_v13_10.md`，只列 v13.8-v13.10 相对 v13.7/v13.1 的增量：

- 一页考场卡；
- A 入口判定表；
- B1 无表头默认表；
- B3 支持/部分支持/不支持尺度；
- B7 法律问题识别/填空短语库；
- A4/A9 商业购买边界；
- 混合题排序卡；
- Confucius 8 道盲题试读结论。

分别提交到真实 GPT Pro web 与真实 Claude Opus 4.7 Adaptive web。不得用 Codex 本地模拟、CLI provisional、摘要复写冒充真实模型。

模型问题必须直问：

1. v13.8-v13.10 的学生化修复是否保持 v13 双轴框架，不破坏 Round05/Round06 已接受结构？
2. 是否足以让聪明高三学生从零上手生成可得分答案？
3. 是否存在必须修复后才能交付的结构性问题？
4. 是否允许进入严格接受，还是只能 candidate / governance gaps？

保存：

- `model_outputs/gpt_v13_10_delta_review_pro_web_raw.md`
- `model_outputs/claude_v13_10_delta_review_opus47_web_raw.md`
- 对应截图；
- 会话 URL / 模式标签 / 完成状态；
- `codex_adjudication/CODEX_V13_10_DELTA_MODEL_ADJUDICATION.md`

若任一模型要求结构性修复，不得进入最终 Governor。

## PATCH-030-2：GPT/Claude 交叉互评

把 GPT 的 delta review 原文发给 Claude，把 Claude 的 delta review 原文发给 GPT，要求互评对方是否漏掉：

- 框架可迁移性；
- 法律关系与设问动作边界；
- 学生语言是否能直接写；
- 42 题与开放容器边界；
- 是否有假闭环。

保存：

- `cross_critiques/gpt_critiques_claude_v13_10_delta.md`
- `cross_critiques/claude_critiques_gpt_v13_10_delta.md`
- `codex_adjudication/CODEX_V13_10_DELTA_CONVERGENCE.md`

没有双向交叉互评，不许写 `STRICT_FINAL_ACCEPTED`。

## PATCH-030-3：DOCX 视觉 QA 闭合

目标是关闭当前 caveat：`DOCX direct render QA not passed / not claimed`。

优先路径：

1. 用 Word COM 从 v13.10 DOCX 导出 PDF；
2. 将该 DOCX-derived PDF rasterize 成页面 PNG；
3. 检查页数、空白页、第一页/中段/末页文字可见性；
4. 写 `render_qa/DOCX_VISUAL_RENDER_QA_v13_11.md`。

如果 Word COM 导出失败，再尝试 LibreOffice/soffice；如果两条都失败，必须写：

`DOCX_VISUAL_RENDER_BLOCKED_v13_11.md`

并维持 `DELIVERED_WITH_GOVERNANCE_GAPS`，不得改写为 `STRICT_FINAL_ACCEPTED`。

## PATCH-030-4：42 题 traceability reconciliation

写 `traceability/TRACEABILITY_RECONCILIATION_v13_11.md`，逐项解释：

- 42 行是否仍唯一；
- `PASS=33`、`PASS_RECOVERED=8`、`PASS_RECOVERED_FORMAL_BUT_ASK_TEXT_PARTIAL=1` 各自含义；
- 36 行 `source_check_state=not_in_round03_source_check` 为什么可由 `covered_by_prior_locked_core` 承接；
- `CC0305_2026_海淀_一模_18_3` 的 ask text partial 是否影响可交付；
- 每行是否有 A 轴、B 轴、命题路径、评分锚点、材料触发、答案骨架、学生预警。

若发现任一 locked core 行缺评分锚点、材料触发、命题路径或答案骨架，必须停在 `CANDIDATE_DELIVERY_NEEDS_AUDIT`。

## PATCH-030-5：开放容器逐题裁决

对 `04_开放容器与不晋升题附录_v13_10.md` 中所有候选写 `open_container/OPEN_CONTAINER_DECISION_v13_11.md`。

至少覆盖：

- CC0040、CC0162、CC0311、CC0353、CC0380 参考运行题；
- CC0251、CC0276、CC0277、CC0317、CC0318、CC0319 下一版回填候选。

每题只能有三种结论：

- `PROMOTE_TO_CORE`
- `EXCLUDE_WITH_REASON`
- `DEFER_NEXT_VERSION_WITH_SOURCE_BOUNDARY`

若任何题被 `PROMOTE_TO_CORE`：

1. 新建 traceability delta；
2. 重跑 A/B 支持数；
3. 重新生成题卡；
4. 重新提交 GPT/Claude delta review；
5. 重新做 Governor。

不得把开放容器无声吞进 42 题正文。

## PATCH-030-6：学生全对检查

把 Confucius 的“能写骨架”升级为 rubric-level 检查。新建：

`student_transfer/STUDENT_RUBRIC_LEVEL_CHECK_v13_11.md`

要求：

- 至少复核第五轮 8 道盲题；
- 对照本地隐藏答案键或 traceability rubric anchors；
- 判定每题是否达到“高分/可满分骨架/只会入口但缺落点/错挂入口”；
- 明确哪些题还需要教师补充原表头、完整设问、损失证据或比例判断。

没有 rubric-level 结果，不得写“聪明高三学生能够全对”；只能写“能生成稳定答案骨架”。

## PATCH-030-7：最终 Governor

只有 PATCH-030-1 到 PATCH-030-6 全部关闭，才能写：

`governance/GOVERNOR_STRICT_FINAL_ACCEPTANCE_v13_11.md`

Governor 必须使用总控允许状态词：

- 若所有门都关闭：`STRICT_FINAL_ACCEPTED`
- 若 DOCX direct QA 仍 blocked：`DELIVERED_WITH_GOVERNANCE_GAPS`
- 若真实 GPT/Claude delta review 未完成：`BLOCKED_ADVISOR`
- 若开放容器或 42 题证据边界不清：`BLOCKED_SOURCE_BOUNDARY`
- 若还有待审候选：`CANDIDATE_DELIVERY_NEEDS_AUDIT`

最终总结不得使用 `v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat` 这类非总控状态词替代总控状态。
