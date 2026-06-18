你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 196
- entry_id: Q0196
- question_ref: 2026房山一模Q19
- question_title: 2026房山一模Q19海南"一线放开"自由便利
- bucket/sub_bucket: 经济全球化 / 国际分工、企业出海与国际竞争新优势
- core_point: 加强技术创新、提高产品质量，增强竞争力
- blocks: 2317-2327

# Desktop Original Excerpt

```text
2317: 2. 2026房山一模Q19海南"一线放开"自由便利
2318: 【材料触发点】 题目分析海南自贸港封关如何助力国际循环，题干中"一线放开"对应进出岛跨境自由便利措施，需要从消费角度把降低通关成本、提高通关效率、推动货物和服务贸易升级写出来，对接贸易投资自由化便利化与要素自由流动。
2319: 【设问】 结合材料，运用《当代国际政治与经济》知识，分析海南自贸港封关是如何助力国际循环的。
2320: 【为什么能想到】 材料里一台41万元的3D打印机省税约6万，企业把省下的钱投入核心技术攻坚，关税红利转成研发，正是“加强技术创新、提高产品质量，增强竞争力”。
2321: 【答案落点】 海南自贸港封关使企业节约关税投入核心技术攻坚，加强技术创新、提升企业竞争力，推动产业升级，使中国市场成为全球产业链供应链稳定器。
2322: 【同题组】 （按原题答题层次）
2323: · 答题层次：本题8分，按消费/市场、生产/产业、投资/营商、中国方案四层组织；前三类开放链条合计按材料表现取分，不要超过6分，中国方案层另按2分处理。
2324: · 消费/市场层（2分）：发挥超大规模市场优势；降低成本、提高效率，促进货物和服务贸易升级、要素自由流动、资源优化配置、贸易投资自由化便利化。
2325: · 生产/产业层（2分）：将关税节约投入技术研发，提升企业竞争力，推动产业升级或优化产业结构，融入全球产业分工和合作。
2326: · 投资/营商层（2分）：优化营商环境，吸引外商投资，推动高水平引进来。
2327: · 中国方案/制度型开放层（2分）：制度型开放1分；为助力国际循环提供中国方案，或以国内大循环吸引全球资源要素、增强国内国际两个市场两种资源联动效应1分。
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
{"unique_id": "UQ0049", "normalized_question": "2026房山一模Q19海南\"一线放开\"自由便利", "count": "5", "doc_orders": "80;130;184;196;431", "buckets": "中国;经济全球化", "core_points": "内外联通畅通国内国际双循环，提升国际循环质量;加强技术创新、提高产品质量，增强竞争力;推动建设开放型世界经济，深化国际分工与合作;推进贸易和投资自由化便利化;贡献中国智慧、中国方案、中国力量", "question_titles": "2026房山一模Q19海南\"一线放开\"自由便利 || 2026房山一模Q19海南\"一线放开\"自由便利 || 2026房山一模Q19海南\"一线放开\"自由便利 || 2026房山一模Q19海南\"一线放开\"自由便利 || 2026房山一模Q19海南\"一线放开\"自由便利"}
```

# Prior Same-Source Context

Prior same-source context: doc184 was NEEDS_FIX because it conflated 一线放开 with 二线口岸/进出岛. doc169 passed a China-solution/two-market layer. This doc196 focuses on technology R&D/competition layer, but its trigger mentions 一线放开 and consumption/free-convenience wording; judge exact blocks independently.

# Codex Watchpoints To Verify, Not Blindly Accept

- Rubric line 62 supports the production layer: 技术研发 -> 提升企业竞争力 -> 产业升级/优化产业结构 -> 融入全球产业分工和合作.
- Source material lines 311-316 support 3D-printer tax saving invested into core technology attack; this is the strongest trigger for this core point.
- Check whether block 2318 wrongly says 一线放开 corresponds to 进出岛/consumer layer, which would repeat doc184 one-line/two-line confusion or drift away from the technology layer.
- UQ0049 remains book-level pending.

# Source / Rubric Excerpts

## SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt
```text
SOURCE_ID: SRC_EXAM_2026_FANGSHAN_YIMO_Q19
COPIED_FROM: /Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_037/SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt
SELECTED_RANGES: 300-342

## selected source lines 300-342
300: 19.（8分）
301: 潮起海之南，春动自贸港。1978年12月18日，党的十一届三中全会拉开改革开放
302: 大幕；47年后的同一天，2025年12月18日，海南自由贸易港全岛封关正式启动，完成
303: 高水平对外开放的“关键一跃”，有力促进了国际循环。
304: 内容
305: 封关满月的效果
306: 对不涉证、不涉检的“零关税”、保税货物，进口
307: 依托8个“一
308: 报关项目从105项精简至33项，通关时间压缩超80%。
309: “一线”
310: 线口岸”实施自由
311: “零关税”商品增至6600多种。一台货值41万元
312: 放开
313: 便利措施，面向国
314: 的高性能3D打印机可以节省税款约6万元，企业将
315: 际开放。
316: 诸如此类的资金全部投入核心技术攻坚。
317: 将“零关税”、
318: 经“二线口岸”进出岛旅客近600万人次，进出
319: 加工增值免关税
320: 岛车辆累计近46万辆次。
321: “二线”
322: 等3类海关监管货
323: 某企业构建起“东南亚原料进口一海南加工增值
324: 管住
325: 物与普通货物分
326: 一全国市场投放”产业链，凭借加工增值超30%的优
327: 类监管、精准查
328: 势，经“二线口岸”进入内地市场免征进口关税，封关
329: 验。
330: 首月，内销货值约1500万元。
331: 家门口的全球购，离岛免税销售额同比增长
332: 在海南自贸
333: 46.8%；国内外品牌首店竞相落户；演唱会与顶级体育
334: 岛内
335: 港内，各类要素可
336: 赛事轮番登场。
337: 自由
338: 以相对自由流通。
339: 推行“极简审批”、“一码通办”，新增经营主体2.68
340: 万户，新增外资企业同比增长13%。
341: 结合材料，运用《当代国际政治与经济》知识，分析海南自贸港封关是如何助力国际
342: 循环的。
```
## SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt
```text
SOURCE_ID: SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19
COPIED_FROM: /Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_037/SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt
SELECTED_RANGES: 58-65

## selected source lines 58-65
58: 19.答案示例（8分）
59: 海南自贸港通过制度型开放发挥我国超大规模市场优势，以国内大循环吸引全球资源要素，增强国内国际两个市场两种资源联动效应，助力国际循环。降低跨境贸易成本，促进商品、服务与生产要素跨境流动，推动货物贸易优化升级；依托监管模式创新，企业节约关税投入核心技术攻坚，形成产业升级良性循环，深度融入全球产业分工和合作，使中国市场成为全球产业链供应链的稳定器；持续优化营商环境，坚持高水平引进来，吸引外商投资；我国以自贸港开放实践助力普惠包容的经济全球化，为畅通国际循环贡献中国方案。
60: 19  细则调整
61: ♣2分 消费：发挥超大规模市场优势1——降低成本提高效率，货物、服务贸易升级/要素自由流动/优化资源配置/贸易投资自由化便利化2
62: ♣2分 生产：技术研发——提升企业竞争力——产业升级/优化产业结构——融入全球产业分工和合作3
63: ♣2分 投资：优化营商环境4——吸引外商投资/引进来5
64: ♣2分 中国方案：制度型开放（1分）——提供助力国际循环中国方案/以国内大循环吸引全球资源要素/增强国内国际两个市场两种资源联动效应（1分）
65: 说明：表示1-5，每个2分，总分不超过6分。
```
