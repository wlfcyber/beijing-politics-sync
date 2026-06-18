你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 182
- entry_id: Q0182
- question_ref: 2024石景山一模Q19
- question_title: 2024石景山一模Q19(2)新能源车企"扎下根"
- bucket/sub_bucket: 经济全球化 / 兼：国内国际两种资源两个市场
- core_point: 利用两个市场两种资源优化全球资源配置
- blocks: 2138-2145

# Desktop Original Excerpt

```text
2138: 16. 2024石景山一模Q19(2)新能源车企"扎下根"
2139: 【材料触发点】 企业在匈牙利建厂，既依托国内新能源汽车技术、产业链和产品优势，又利用匈牙利欧洲交通枢纽、工业基础等条件，体现国内国际资源和市场的联动。
2140: 【设问】 结合材料，运用《当代国际政治与经济》知识，分析中国新能源汽车企业从“走出去”到“扎下根”的原因。（8分）
2141: 【为什么能想到】 出海要提前建供应链、各地原材料成本却难降，这是要素在国内国际间重新摆布的难题，一国资源解不开，故须利用两个市场两种资源优化全球资源配置。
2142: 【答案落点】 中国新能源汽车企业把国内技术、产业链和产品优势同匈牙利欧洲交通枢纽、工业基础等条件结合起来，利用两个市场两种资源优化全球资源配置，降低生产贸易成本，夯实海外长期发展根基。
2143: 【同题组】 （同主题练习提醒）
2144: · 本题适合作为同主题训练，不按固定得分层次展开。
2145: · 可写方向：顺应经济全球化趋势，利用比较优势优化资源配置，降低生产贸易成本，打造国际竞争新优势，并通过技术交流与资源共享实现合作共赢。
```

# Unique-Question Group Context

```text
{"unique_id": "UQ0090", "normalized_question": "2024石景山一模Q19(2)新能源车企\"扎下根\"", "count": "1", "doc_orders": "182", "buckets": "经济全球化", "core_points": "利用两个市场两种资源优化全球资源配置", "question_titles": "2024石景山一模Q19(2)新能源车企\"扎下根\""}
```

# Codex Watchpoints To Verify, Not Blindly Accept

- Block 2141 may be copied from the coffee-enterprise source: “提前建供应链/原材料成本难降” does not appear in the NEV/Hungary material. Verify as a possible hard 材料触发/为什么能想到 error.
- The valid source answer supports comparative advantage, optimized resource allocation, lower production/trade costs, international competition advantage, technology exchange/resource sharing, and cooperation win-win.
- Use the corrected PPTX rubric excerpt in slice037; if you still see no formal scoring breakdown, mark only the scoring-detail level as source-limited, not the whole answer.

# Source / Rubric Excerpts

## SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2.txt
```text
1: SOURCE_ID: SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2
2: TITLE: 2024石景山一模Q19(2) 试卷与参考答案摘要
3: ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2024模拟题/石景山一模/试卷/试卷.docx
4: TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_021/SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2.txt
5: TEXT_EXTRACT_SOURCE: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/2cc62698b97c__2024届各区一模试题分类汇编选必1.txt
6: 
7: ## selected source lines 161-164
8: 161: 2.（石景山一模19（2））
9: 162: 新能源汽车已成为全球汽车产业转型发展的主要方向，也是促进世界经济持续增长的重要引擎。2023 年，我国全年汽车整车出口 491 万辆，同比增长 57.9%，首次跃居全球第一。其中，新能源汽车出口 120.3 万辆，同比增长 77.6%。出海大势之下，中国新能源汽车不但“走了出去”，也在悄悄“扎下根来”。以某企业为例，在继泰国等多国设厂后，计划采用全球先进的工艺设备和高度自动化的生产流程，在匈牙利建设全球领先的新能源汽车整车制造基地。匈牙利是欧洲重要的交通枢纽，拥有雄厚的工业基础，为该企业在当地建设工厂提供了良好的契机。生产基地的建设将创造数千个就业岗位，积极带动当地经济发展，推动中匈之间的技术交流，并借助该企业自身全产业链的优势帮助当地构建绿色“生态圈”。 
10: 163: （2）结合材料，运用《当代国际政治与经济》知识，分析中国新能源汽车企业从“走出去”到“扎下根”的原因。（8 分） 
11: 164: 参考答案：新能源车企顺应经济全球化趋势，依靠技术创新引领，生产优质产品，满足国际市场需求；利用当地比较优势，优化资源配置，降低生产贸易成本，打造国际竞争新优势；通过技术交流与资源共享，带动当地经济、社会发展，创设良好的生产贸易环境，实现合作共赢。
```
## SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2.txt
```text
1: SOURCE_ID: SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2
2: TITLE: 2024石景山一模Q19(2) 细则/答案（slice037 corrected excerpt）
3: ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2024模拟题/石景山一模/细则/细则.pptx
4: TEXT_EXTRACT_PATH: reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_037/SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2.txt
5: TEXT_EXTRACT_SOURCE: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/f887d1b620c6__细则.txt
6: 
7: ## selected source lines 539-544 (Python splitlines numbering; includes Slide 46 answer)
8: 539: ===== SLIDE 45 =====
9: 540: 我国新时代对外开放的措施
10: 541: 
11: 542: ===== SLIDE 46 =====
12: 543: （2）（8分）新能源车企顺应经济全球化趋势，依靠技术创新引领，生产优质产品，满足国际市场需求；利用当地比较优势，优化资源配置，降低生产贸易成本，打造国际竞争新优势；通过技术交流与资源共享，带动当地经济、社会发展，创设良好的生产贸易环境，实现合作共赢。
13: 544: （3）（4分）可从分析与综合的方法、辩证否定观等角度作答。如从其他角度回答，符合题意，亦可酌情给分。
```
