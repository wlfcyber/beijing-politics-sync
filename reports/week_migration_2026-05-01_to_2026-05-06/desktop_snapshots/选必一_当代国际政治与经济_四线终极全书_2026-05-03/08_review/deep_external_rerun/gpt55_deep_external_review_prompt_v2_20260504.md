XBY1-GPT-DEEP-REVIEW-V2-20260504

你继续作为 GPT-5.5 Pro 内容监督者，沿用这个同一个 ChatGPT Pro 对话。请先确认你看到唯一标记：XBY1-GPT-DEEP-REVIEW-V2-20260504。

我已经上传最新版附件：xby1_external_review_FINAL_20260504.md。这是选必一《当代国际政治与经济》最终学生讲义，已经过 Codex/ClaudeCode 本地证据线、Claude Opus 教学深审返修、Governor/Confucius/Word-PDF fallback QA。现在补跑的是你作为“首席内容监督者/压力测试者”的缺失环节，不要只盖章。

请深度审查附件本身，重点看：

1. 是否仍有同类项合并过度或合并不足；特别检查“和平与发展仍是时代主题”“推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展”“新型国际关系”“共商共建共享的全球治理观”“人类命运共同体”“中国智慧/中国方案”“联合国核心作用”等高频核心。
2. 是否有“参考答案式表述”被伪装成稳定采分核心；如只能作为表达积累、guarded、reference-only、prompt-only 的内容，不应被学生当作必背主干。
3. 是否每道题都形成完整闭环：完整设问 -> 设问触发 -> 材料触发 -> 框架落点 -> 答题点自身积累 -> 卷面答案句。
4. 是否存在一材料对应多个答题点，但讲义只收到一个点的漏收情况。
5. 是否存在材料触发太泛、学生看完仍不知道“为什么想到这个点”的地方。
6. 是否有答案句太空、太像口号、缺少材料事实或结果链。
7. 是否有跨模块污染：必修二、法律、逻辑、哲学、文化、政治与法治内容误入选必一主框架。
8. 是否仍有学生版不该出现的后台语：路径、debug、audit、模型聊天、评分细则、参考答案、证据层级、PASS、blocked 等。
9. Word/PDF gate 的 fallback 是否可接受；若不可接受，请说明还缺哪种具体检查。
10. 最后请判断这份讲义是否能让零基础学生从“看到材料”迁移到“写出卷面答案”。

输出格式请严格按下面来：

verdict: PASS / NEEDS_FIX / NEED_ARTIFACT_UPLOAD

如果是 NEED_ARTIFACT_UPLOAD，只说明缺什么附件或上下文，不要猜。

如果是 NEEDS_FIX，请列出：
- issue_id: XBY1-GPTV2-01...
- severity: must_fix_content / should_fix_transfer / style_or_readability
- location: 题号或核心点
- problem: 具体问题
- suggested_fix: 具体怎么改

如果是 PASS，也请列出 5-8 条“我实查过并认为可过”的高风险点，说明为什么不阻断。不要只写泛泛肯定。

注意：你是内容监督者，不是本地证据裁判。你可以指出风险和修改建议，但不能替 Codex 判定细则证据是否足够；所有 substantive 修改会回到本地源文件核验后再决定。
