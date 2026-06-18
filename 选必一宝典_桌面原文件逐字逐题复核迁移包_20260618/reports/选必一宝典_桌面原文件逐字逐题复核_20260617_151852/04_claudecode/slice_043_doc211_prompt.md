你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 211
- entry_id: Q0211
- question_ref: 2026海淀一模Q20
- question_title: 2026海淀一模Q20中国标准与全球经济治理参与
- bucket/sub_bucket: 经济全球化 / 全球经济治理与规则权益
- core_point: 参与国际标准制定，提升国际规则话语权
- blocks: 2488-2496

# Desktop Original Excerpt

```text
2488: 2. 2026海淀一模Q20中国标准与全球经济治理参与
2489: 【材料触发点】 材料显示中国不只是被动接受国际标准，而是主动向ISO、IEC提交提案、参与并牵头制定多领域国际标准；设问问中国标准走出国门的意义，必须把中国从"标准接受者"转为"规则共建者"这一角色变化讲出来。
2490: 【设问】 结合材料，运用《当代国际政治与经济》知识，谈谈中国标准走出国门的意义。
2491: 【为什么能想到】 中国不再只接受现成标准，而是主动向ISO、IEC提案、牵头制定，从守规则者变成定规则者；这一转换要用“参与国际标准制定，提升规则话语权”。
2492: 【答案落点】 我国主动向国际标准化组织贡献提案并牵头制定多领域国际标准，积极参与全球经济治理和规则制定。
2493: 【同题组】 （同主题练习提醒）
2494: · 本题适合作为同主题训练，不按固定得分层次展开。
2495: · 可写方向：围绕制度型开放、两个市场两种资源、国际标准贡献、全球治理规则制定等组织。
2496: · 易错提醒：写中国标准走出国门时，要同时说明国内开放基础和国际治理意义。
```

# Current Ledger Field Skeleton

```text
- 术语/核心采分点: current_status=STRUCTURE_NEEDS_FIX_SOURCE_PENDING; audit_note=Mechanical full-document scan: current entry structure uses bucket/core heading plus 【同题组】, but lacks independent hard-rule field for this item; source/content audit still pending.
- 完整设问: current_status=PENDING; audit_note=(pending)
- 细则位置: current_status=STRUCTURE_NEEDS_FIX_SOURCE_PENDING; audit_note=Mechanical full-document scan: current entry structure uses bucket/core heading plus 【同题组】, but lacks independent hard-rule field for this item; source/content audit still pending.
- 来源: current_status=PENDING; audit_note=(pending)
- 材料触发: current_status=PENDING; audit_note=(pending)
- 答案句: current_status=PENDING; audit_note=(pending)
- 同类项合并: current_status=PENDING; audit_note=(pending)
- 模块边界: current_status=PENDING; audit_note=(pending)
```

# Unique-Question Group Context

```json
{"unique_id": "UQ0121", "normalized_question": "2026海淀一模Q20中国标准与全球经济治理参与", "count": "1", "doc_orders": "211", "buckets": "经济全球化", "core_points": "参与国际标准制定，提升国际规则话语权", "question_titles": "2026海淀一模Q20中国标准与全球经济治理参与"}
```

# Codex Watchpoints To Verify, Not Blindly Accept

Same source family as doc208, but this title/core narrows to standards/rule voice. Verify whether block 2492 should say `规则制定` rather than broader `治理/规则` and whether this singleton UQ0121 is actually a duplicate of UQ0082. Do not invent fixed scoring layers for a paragraph rubric.

# Source / Rubric Excerpts

## SRC_EXAM_2026_HAIDIAN_YIMO_Q20.txt
```text
SOURCE_ID: SRC_EXAM_2026_HAIDIAN_YIMO_Q20
TITLE: 2026海淀一模Q20 试卷题干
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模/试卷/试卷.pdf
ORIGINAL_SHA256: 03e0412bb80579d817c36d81a80cbe3caaf6ba114b5ff7272a9ec5582696b547
ORIGINAL_SIZE_BYTES: 1739453
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04/source_inventory/extracted/2026/2026海淀一模/2026各区一模__2026海淀一模__试卷__试卷.pdf.txt

## prompt/material lines 339-355
339: 20.（8分）
340: 国际标准是全球产业界的“通用语言”。从手机充电接口的统一，到食品包装上的营养成分
341: 标注；从电梯运行的安全规范，到空气质量的监测指标，背后都离不开“标准”的支撑。它让不同
342: 国家、不同企业的产品能互通兼容，让全球资源能更高效利用。
343: 近年来，从低碳能源到人工智能，从北斗导航到传统医学，越来越多的中国标准走出国门，
344: 融入全球产业发展体系，中国与世界深度互动、共享发展。2025年，我国在国际标准的制定与推
345: 广中交出了亮眼成绩单。
346: 2025年我国在低碳能源、生
347: 2025年我国在新能源、智慧电
348: 物技术、人工智能、工业网络等前
349: 网、传统医学、脑机接口等领域，
350: 沿领域，共向ISO、IEC提交提案
351: 牵头制定发布285项ISO、IEC国
352: 505项，较2024年增长15.83%。
353: 际标准，同比增长26.67%
354: 注：ISO（国际标准化组织）和IEC（国际电工委员会）是全球最具权威性的两大国际标准化机构。
355: 结合材料，运用《当代国际政治与经济》知识，谈谈中国标准走出国门的意义。
```

## SRC_RUBRIC_2026_HAIDIAN_YIMO_Q20.txt
```text
SOURCE_ID: SRC_RUBRIC_2026_HAIDIAN_YIMO_Q20
TITLE: 2026海淀一模Q20 参考答案/细则
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模/细则/细则.pdf
ORIGINAL_SHA256: 9b5ac8fd0cfe59cb5dd47ea200078c3342a8cfc212be1cbe8a8f13044a540111
ORIGINAL_SIZE_BYTES: 2405986
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04/source_inventory/extracted/2026/2026海淀一模/2026各区一模__2026海淀一模__细则__细则.pdf.txt

## answer/rubric lines 85-89
85: 20.（8分）
86: 扩大制度型开放，增强我国产品、服务乃至产业链在全球的竞争力，推进高水平对外开放，更好利
87: 用国内国际两个市场、两种资源，推动构建新发展格局；我国在低碳能源、人工智能等领域推动贡
88: 献国际标准，促进全球范围内标准共通、技术共享，推动全球技术创新与绿色转型，同时，我国积
89: 极参与全球经济治理和规则制定，推动全球治理体制向着更加公正合理方向发展。
```


# Output Constraint

请保持严格、短而完整：总字数控制在 1200-1800 汉字；每个字段只写结论+关键行号；必须给 must-fix 和边界声明。不要展开长篇教材解释。
