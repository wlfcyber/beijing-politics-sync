请以 Claude Opus 4.7 Adaptive Thinking 的最终门禁身份审核这份选必一终稿。

请读取我上传的：

1. `FINAL_EXTERNAL_REVIEW_PACKET_20260525.md`
2. `xuanbiyi_final_handbook_20260525_patched.md`
3. `FULL_SOURCE_XUANBIYI_COVERAGE_RECRAWL_SUMMARY_20260525.md`
4. `CLAUDECODE_FULL_SOURCE_RECRAWL_REVIEW_20260525.md`
5. `GPTPRO_FINAL_REVIEW_RESULT_20260525.md`
6. `GPTPRO_REQUIRED_PATCH_APPLIED_20260525.md`
7. `GPTPRO_PATCH_CONFIRM_RESULT_20260525.md`
8. `render_qa_summary_20260525_patched.md`

背景说明：

- GPT Pro 第一轮终审给出 `REJECT_NEEDS_PATCH`，指出 13 个主链经济全球化题例缺 `【同题组】`，以及 `2024东城一模Q16` 附录边界 H3 污染五段结构账。
- 我已按清单补齐 13 个非空 `【同题组】`，并把 `2024东城一模Q16` 改成非 H3 边界题。
- 补丁后机器 QA 显示：H3 总数 369；逐 H3 五段字段缺失 0；PDF 202 页全部渲染；可疑空白页 0。
- GPT Pro 补丁复验已经给出 `FINAL_VERDICT: ACCEPT`，确认上一轮硬伤关闭，并允许进入 Claude Opus 4.7 最终复审。

请你不要泛泛表扬，也不要重新发散成大规模新项目。请只做最终交付门禁：

1. 全源覆盖是否仍有硬缺口。
2. 是否仍有两个独立考题被合并为一个题例。
3. 理论、经济全球化、政治多极化、中国、联合国的归桶是否仍有会误导学生的硬错误。
4. 经济全球化桶是否仍把不可替代表述粗暴合并。
5. 对零基础学生，是否能通过“什么时候写、设问、为什么能想到、卷面句、同题组”完成迁移。
6. GPT Pro 指出的两项必改项是否确实关闭。

请输出：

- `FINAL_VERDICT`：只能写 `ACCEPT` / `ACCEPT_WITH_NON_BLOCKING_NOTES` / `REJECT_NEEDS_PATCH`
- `GPT补丁关闭情况`
- `是否还有必须修改项`
- `是否可登记为与必修四哲学宝典同等含金量的选必一学生版终稿`
- `最终可登记口径`

如果还有硬伤，必须列出具体位置；如果没有硬伤，请明确允许最终落盘、生成交付报告并推送 GitHub。
