XBY1-GPT-DEEP-FINAL-20260504-1118

你继续作为 GPT-5.5 Pro 内容监督者，沿用本 `Opus4.6 vs 4.7` 同一个 ChatGPT Pro 对话。请先确认你看到这个唯一标记：`XBY1-GPT-DEEP-FINAL-20260504-1118`。

这是选必一《当代国际政治与经济》最终讲义补跑深度外审。上一轮 GPT 深度补跑因为浏览器错线程漂移被作废，不计 PASS。本轮不要只盖章，请用本对话已有上下文、前面 XBY1 审查记录、以及下面的最新修订摘要做最后压力测试；如果你认为上下文不足以判断，请直接输出 `verdict: NEED_ARTIFACT_UPLOAD`，不要猜。

最新本地状态摘要：

- 最终学生讲义已按“完整设问 -> 设问触发 -> 材料触发 -> 框架落点 -> 答题点自身积累 -> 答案句变体”组织。
- 覆盖 48 道主观题、177 条答题链，六桶为：时代背景、理论、经济全球化、政治多极化、中国、联合国。
- 2026 石景山期末全模块排除。
- Claude Opus 4.7 Adaptive 已在同一 Claude 选必一对话深审，给出 `PASS_AFTER_FIX`，Codex 已本地核证并修掉 D-01 至 D-10。
- 已修重点包括：经济全球化方向保留完整“开放、包容、普惠、平衡、共赢”；不再把它压成空标签；南南合作/小而美不再写孤立“和平；发展；合作”；发展与安全加入总体国家安全观、底线思维、经济安全、科技安全、AI 风险；慎用区补真实设问；2026 朝阳一模 Q20 改成七层摘要；和平与发展材料触发更具体；愚公移山题加入可用/不可用条件。
- 本地清洁检查：学生版无路径、debug、audit、模型聊天、评分标签、参考答案标签；PDF 101 页；LibreOffice `soffice` 缺失，DOCX canonical render 不能跑，但已用 QuickLook、DOCX 文本抽取、PDF 文本和 QuickLook fallback。

请检查这些 gate：

1. 同核心合并是否“既合并同类项，又保留最高信息量原词”，尤其和平与发展、经济全球化方向、新型国际关系、人类命运共同体、中国智慧中国方案、全球治理倡议。
2. 六桶落点是否有错挂，尤其政治多极化与中国责任/中国方案、联合国与一般国际组织、经济全球化与开放型世界经济。
3. 学生闭环是否能迁移：材料信号是否能推到框架落点，答案句是否像考场自然句，不是后台术语表。
4. 慎用区是否具体有效，不是泛泛提醒。
5. 是否还存在跨模块污染或参考答案冒充细则的风险。
6. Word/PDF gate 的 fallback 是否可接受；如果不可接受，请说具体还要补哪种检查。

输出格式：

`verdict: PASS | PASS_AFTER_FIX | NEEDS_FIX | NEED_ARTIFACT_UPLOAD`

然后给表格：

`issue_id | severity | location | problem | why_it_matters_for_student | proposed_correction | local_evidence_check_needed`

severity 只能用：

- `must_fix_content`
- `should_fix_transfer`
- `style_or_readability`
- `rejected_if_no_local_evidence`

如果没有 must_fix，也请列最有价值的增强项；如果你认为当前上下文不足，不要硬审，直接 `NEED_ARTIFACT_UPLOAD`。
