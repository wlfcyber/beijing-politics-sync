你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 203
- entry_id: Q0203
- question_ref: 2024石景山一模Q19
- question_title: 2024石景山一模Q19(2)
- bucket/sub_bucket: 经济全球化 / 国际分工、企业出海与国际竞争新优势
- core_point: 发挥比较优势并打造国际竞争新优势
- blocks: 2395-2402

# Desktop Original Excerpt

```text
2395: 1. 2024石景山一模Q19(2)
2396: 【材料触发点】 设问问企业从出口到海外建厂的原因，匈牙利交通枢纽和工业基础不是单纯背景，而是企业利用当地比较优势、降低成本并形成国际竞争新优势的依据。
2397: 【设问】 结合材料，运用《当代国际政治与经济》知识，分析中国新能源汽车企业从“走出去”到“扎下根”的原因。（8分）
2398: 【为什么能想到】 材料从"出口"升级到"海外建厂"，并写明匈牙利"交通枢纽""工业基础"——这不是国别背景介绍，而是企业选址的比较优势依据。要分析"从走出去到扎下根"的原因，重点在"扎下根"——必须解释为何海外建厂比出口更有竞争力，而不是泛泛谈企业国际化。先把匈牙利交通枢纽和工业基础作为东道国比较优势点出，再用利用比较优势、优化资源配置、降低成本接续，最终指向打造国际竞争新优势。
2399: 【答案落点】 中国新能源汽车企业利用匈牙利交通枢纽和工业基础等比较优势，优化资源配置、降低生产贸易成本，从而在海外生产和服务网络中打造国际竞争新优势。
2400: 【同题组】 （同主题练习提醒）
2401: · 本题适合作为同主题训练，不按固定得分层次展开。
2402: · 可写方向：顺应经济全球化趋势，利用比较优势优化资源配置，降低生产贸易成本，打造国际竞争新优势，并通过技术交流与资源共享实现合作共赢。
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
{"unique_id": "UQ0063", "normalized_question": "2024石景山一模Q19(2)", "count": "3", "doc_orders": "104;203;531", "buckets": "中国;经济全球化", "core_points": "促进技术共享和民生改善，为全球可持续发展贡献力量;发挥比较优势并打造国际竞争新优势;顺应经济全球化趋势，主动融入并推动深化", "question_titles": "2024石景山一模Q19(2) || 2024石景山一模Q19(2) || 2024石景山一模Q19(2)"}
```

# Prior Same-Source Context

Prior same-source context: doc182 was NEEDS_FIX only because it imported coffee/supply-chain facts absent from the 石景山新能源车材料; it also confirmed the PPTX answer source has no detailed point-by-point scoring layer. This doc203 uses the actual Hungary transport/industrial-foundation comparative-advantage trigger, so verify independently.

# Codex Watchpoints To Verify, Not Blindly Accept

- Source/rubric lines 164/543 exactly contain 利用当地比较优势，优化资源配置，降低生产贸易成本，打造国际竞争新优势.
- The evidence is an answer-chain/PPTX excerpt, not a granular official scoring breakdown; judge whether this is PASS with source-limited note or LOW_EVIDENCE for 细则位置.
- Desktop block 2401 says not to use fixed scoring layers; verify this accurately reflects source limits instead of hiding missing rubric.
- UQ0063 remains book-level pending; source also has doc104/doc531 variants.

# Source / Rubric Excerpts

## SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2.txt
```text
SOURCE_ID: SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2
TITLE: 2024石景山一模Q19(2) 试卷与参考答案摘要
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2024模拟题/石景山一模/试卷/试卷.docx
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_021/SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2.txt
TEXT_EXTRACT_SOURCE: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/2cc62698b97c__2024届各区一模试题分类汇编选必1.txt

## selected source lines 161-164
161: 2.（石景山一模19（2））
162: 新能源汽车已成为全球汽车产业转型发展的主要方向，也是促进世界经济持续增长的重要引擎。2023 年，我国全年汽车整车出口 491 万辆，同比增长 57.9%，首次跃居全球第一。其中，新能源汽车出口 120.3 万辆，同比增长 77.6%。出海大势之下，中国新能源汽车不但“走了出去”，也在悄悄“扎下根来”。以某企业为例，在继泰国等多国设厂后，计划采用全球先进的工艺设备和高度自动化的生产流程，在匈牙利建设全球领先的新能源汽车整车制造基地。匈牙利是欧洲重要的交通枢纽，拥有雄厚的工业基础，为该企业在当地建设工厂提供了良好的契机。生产基地的建设将创造数千个就业岗位，积极带动当地经济发展，推动中匈之间的技术交流，并借助该企业自身全产业链的优势帮助当地构建绿色“生态圈”。 
163: （2）结合材料，运用《当代国际政治与经济》知识，分析中国新能源汽车企业从“走出去”到“扎下根”的原因。（8 分） 
164: 参考答案：新能源车企顺应经济全球化趋势，依靠技术创新引领，生产优质产品，满足国际市场需求；利用当地比较优势，优化资源配置，降低生产贸易成本，打造国际竞争新优势；通过技术交流与资源共享，带动当地经济、社会发展，创设良好的生产贸易环境，实现合作共赢。
```
## SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2.txt
```text
SOURCE_ID: SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2
TITLE: 2024石景山一模Q19(2) 细则/答案（slice037 corrected excerpt）
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2024模拟题/石景山一模/细则/细则.pptx
TEXT_EXTRACT_PATH: reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_037/SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2.txt
TEXT_EXTRACT_SOURCE: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/f887d1b620c6__细则.txt

## selected source lines 539-544 (Python splitlines numbering; includes Slide 46 answer)
539: ===== SLIDE 45 =====
540: 我国新时代对外开放的措施
541: 
542: ===== SLIDE 46 =====
543: （2）（8分）新能源车企顺应经济全球化趋势，依靠技术创新引领，生产优质产品，满足国际市场需求；利用当地比较优势，优化资源配置，降低生产贸易成本，打造国际竞争新优势；通过技术交流与资源共享，带动当地经济、社会发展，创设良好的生产贸易环境，实现合作共赢。
544: （3）（4分）可从分析与综合的方法、辩证否定观等角度作答。如从其他角度回答，符合题意，亦可酌情给分。
```
