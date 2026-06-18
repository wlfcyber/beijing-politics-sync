你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 172
- entry_id: Q0172
- question_ref: 2026海淀一模Q20
- question_title: 2026海淀一模Q20中国标准走出国门撬动两个市场两种资源
- bucket/sub_bucket: 经济全球化 / 兼：国内国际两种资源两个市场
- core_point: 利用两个市场两种资源优化全球资源配置
- blocks: 2031-2039

# Desktop Original Excerpt

```text
2031: 6. 2026海淀一模Q20中国标准走出国门撬动两个市场两种资源
2032: 【材料触发点】 题面强调国际标准是全球产业界的"通用语言"，列出中国向ISO、IEC提交大量提案、在低碳能源和人工智能等领域牵头制定国际标准；标准走出国门把国内技术、产品、规则与国际市场、规则双向打通，设问问"意义"，必须从中国如何借标准联通调动跨境市场和资源切入。
2033: 【设问】 结合材料，运用《当代国际政治与经济》知识，谈谈中国标准走出国门的意义。
2034: 【为什么能想到】 题面强调"通用语言"，并给出中国向ISO、IEC提交提案、在低碳能源和人工智能等领域牵头制定标准这些具体动作，标准是规则层面的双向接入接口。问"中国标准走出国门的意义"，要把"标准"翻译为连接中国市场、技术、规则与国际市场、规则的双向通道，而不是只夸技术领先。先点明国际标准是全球产业界的通用语言、是要素跨境流动的规则接口，再写中国通过提案和牵头制定标准把国内技术、产业与国际市场对接，最后指向更好利用国内国际两个市场、两种资源、共享发展。
2035: 【答案落点】 中国标准走出国门，有利于更好利用国内国际两个市场、两种资源，推动中国与世界在技术、产业、规则上深度互动、共享发展。
2036: 【同题组】 （同主题练习提醒）
2037: · 本题适合作为同主题训练，不按固定得分层次展开。
2038: · 可写方向：围绕制度型开放、两个市场两种资源、国际标准贡献、全球治理规则制定等组织。
2039: · 易错提醒：写中国标准走出国门时，要同时说明国内开放基础和国际治理意义。
```

# Unique-Question Group Context

```text
{'unique_id': 'UQ0072', 'normalized_question': '2026海淀一模Q20中国标准走出国门撬动两个市场两种资源', 'count': '3', 'doc_orders': '161;172;200', 'buckets': '经济全球化', 'core_points': '中国扩大高水平对外开放与制度型开放;利用两个市场两种资源优化全球资源配置;加强技术创新、提高产品质量，增强竞争力', 'question_titles': '2026海淀一模Q20中国标准走出国门撬动两个市场两种资源 || 2026海淀一模Q20中国标准走出国门撬动两个市场两种资源 || 2026海淀一模Q20中国标准走出国门撬动两个市场两种资源'}
{'unique_id': 'UQ0082', 'normalized_question': '2026海淀一模Q20', 'count': '2', 'doc_orders': '208;239', 'buckets': '经济全球化', 'core_points': '促进全球范围内标准共通、技术共享，推动全球技术创新与绿色转型;积极参与全球经济治理和经贸规则完善', 'question_titles': '2026海淀一模Q20 || 2026海淀一模Q20'}
{'unique_id': 'UQ0121', 'normalized_question': '2026海淀一模Q20中国标准与全球经济治理参与', 'count': '1', 'doc_orders': '211', 'buckets': '经济全球化', 'core_points': '参与国际标准制定，提升国际规则话语权', 'question_titles': '2026海淀一模Q20中国标准与全球经济治理参与'}
{'unique_id': 'UQ0122', 'normalized_question': '2026海淀一模Q20中国标准走出国门推动治理体制公正合理', 'count': '1', 'doc_orders': '305', 'buckets': '政治多极化', 'core_points': '推动国际秩序和全球治理体系更加公正合理', 'question_titles': '2026海淀一模Q20中国标准走出国门推动治理体制公正合理'}
```

# Codex Watchpoints To Verify, Not Blindly Accept

- Rubric has three branches: opening/two markets, standards/commonality/innovation, and global governance/rules. This entry is the two-market branch; verify it does not erase the other branches and same-theme notes preserve them.
- Check whether “domestic technology/products/rules linked with international market/rules” is source-backed by the standard-as-common-language material and rubric, not an invented overreach.
- Same source appears as UQ0072/UQ0082/UQ0121/UQ0122; keep book-level hold.

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

# Required Output

Return only the复核结论 in Markdown. Do not write replacement full text.
