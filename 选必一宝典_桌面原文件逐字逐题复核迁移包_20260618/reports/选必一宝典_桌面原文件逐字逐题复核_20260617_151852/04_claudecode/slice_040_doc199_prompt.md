你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 199
- entry_id: Q0199
- question_ref: 2025西城一模Q18
- question_title: 2025西城一模Q18
- bucket/sub_bucket: 经济全球化 / 国际分工、企业出海与国际竞争新优势
- core_point: 加强技术创新、提高产品质量，增强竞争力
- blocks: 2350-2359

# Desktop Original Excerpt

```text
2350: 5. 2025西城一模Q18
2351: 【材料触发点】 设问问地区如何利用国内外资源"开拓海外市场""提升国际循环质量"。要回答从国内市场延伸到国际市场的对外开放结构，必须用"两个市场两种资源/国际国内双循环"把国内端、国际端接成一条循环——只讲产业内部升级不能回答"国际循环质量提升"。
2352: 【设问】 从“两条鱼循环”看增长新空间。产自中国的鳗鱼“游”向世界，挪威三文鱼“飞”来中国，增长新空间在不断拓展。结合材料，运用《经济与社会》所学，谈谈中国经济增长新空间是如何拓展的。
2353: 【为什么能想到】 材料讲川鳗经32道工序、从天然捕捞转向养殖近地加工成全球最大出口国，靠工艺品质打出竞争力，正是“加强技术创新、提高产品质量，增强竞争力”。
2354: 【答案落点】 特色产业链利用本地资源优势，注重技术创新与质量品质，不断提高竞争力，成功开拓海外市场。
2355: 【同题组】 （按原题答题层次）
2356: · 答题层次：本题7分，按产业优势/内生动力、物质条件、市场三层组织
2357: · 第一层：产业优势/内生动力（3分）：生态优势转换为发展优势/生态效益与经济效益相统一/绿色环保/实现生态价值；特色资源禀赋/比较优势/特色产业/技术创新/质量品质；竞争力提高/供给能力提升
2358: · 第二层：物质条件（2分）：便捷交通设施/基础设施/高水平物流体系；内外联通/贸易便利化/降成本/提效率
2359: · 第三层：市场（2分）：国内国际两个市场两种资源联动/拓宽市场/市场需求旺盛/市场广阔/对外开放质量和水平提升；互利共赢/循环质量和水平提升/双循环相互促进
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
{"unique_id": "UQ0038", "normalized_question": "2025西城一模Q18", "count": "6", "doc_orders": "89;147;179;183;199;271", "buckets": "政治多极化;经济全球化", "core_points": "内外联通畅通国内国际双循环，提升国际循环质量;利用两个市场两种资源优化全球资源配置;加强技术创新、提高产品质量，增强竞争力;在平等互利基础上开展合作，实现互利共赢;推进贸易和投资自由化便利化;提高开放型经济水平", "question_titles": "2025西城一模Q18 || 2025西城一模Q18 || 2025西城一模Q18 || 2025西城一模Q18 || 2025西城一模Q18 || 2025西城一模Q18"}
```

# Prior Same-Source Context

Prior same-source context: doc179/doc183 were NEEDS_FIX because they described answer/rubric terms as the question wording. This doc199 focuses on technology/quality/competition but must preserve the actual 《经济与社会》 prompt.

# Codex Watchpoints To Verify, Not Blindly Accept

- Source prompt lines 221-234 ask how China economic growth space is expanded; they do not literally ask “international cycle quality”.
- Rubric lines 67-70 support特色资源/技术创新/质量品质/竞争力 as industry-advantage layer.
- Because source prompt is 《经济与社会》, verify cross-module boundary: this is a source-backed overlap used in 选必一 review, not a pure 选必一 prompt.
- UQ0038 remains book-level pending.

# Source / Rubric Excerpts

## SRC_EXAM_2025_XICHENG_YIMO_Q18.txt
```text
SOURCE_ID: SRC_EXAM_2025_XICHENG_YIMO_Q18
COPIED_FROM: /Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_036/SRC_EXAM_2025_XICHENG_YIMO_Q18.txt
SELECTED_RANGES: 221-234;342-345

## selected source lines 221-234
221: 18．（7分）从“两条鱼循环”看增长新空间。
222: 产自中国的鳗鱼“游”向世界，挪威三文鱼“飞”来中国，增长新空间在不断拓展。结合材料，运用
223: 第一条鱼是“川字号”鳗鱼。鳗 第二条鱼是挪威三文鱼。春节期
224: 鱼被称为 “世界上最干净的鱼”。得 间，不少人买到了产地直采的挪威三
225: 益于长江上游牢固的生态屏障，四川 文鱼。经由冷链运营的欧洲生鲜定班
226: 在长江边建鳗鱼养殖基地，在成都建 包机航线，挪威三文鱼“飞行”约
227: 起加工企业。鳗鱼经 32 道工序出炉 8000公里，直达湖北鄂州，全程约11.5
228: 后，搭载中欧班列等，流向世界各地 小时。三文鱼再经国内的空中、地面
229: 餐桌。如今，“川鳗”年产量达 1300 冷链网络，被快速分拨到各地。数据
230: 余吨，年加工量 800 余吨，九成以上 显示，2024 年，挪威对华海产品出口
231: 远销海外。从依赖天然捕捞，到淡水 量达18.2万吨，同比增长14%。中国已
232: 养殖、近地加工，中国已是全球最大 跃升为挪威海产出口的亚洲第一大市
233: 的鳗鱼养殖和出口国。 场和全球范围内增长最快的市场。
234: 《经济与社会》所学，谈谈中国经济增长新空间是如何拓展的。

## selected source lines 342-345
342: 18．（7分）环境保护给产业发展带来新机遇，推动生态价值实现，促进生态优势转换为发展优势。地区利
343: 用资源优势，注重技术和品质，探索打造特色产业链，不断提高竞争力，成功开拓海外市场。便捷的
344: 交通基础设施、高水平的物流体系，内外联通，畅通了国际国内双循环，产品等得以高效率地流通，
345: 与其他国家合作共赢。我国经济发展的内生动力和可靠性不断增强，国际循环质量和水平不断提升。
```
## SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt
```text
SOURCE_ID: SRC_RUBRIC_2025_XICHENG_YIMO_Q18
COPIED_FROM: /Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/05_source_backcheck/slice_036/SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt
SELECTED_RANGES: 65-78

## selected source lines 65-78
65: 18．（7分）环境保护给产业发展带来新机遇，推动生态价值实现，促进生态优势转换为发展优势。地区利用资源优势，注重技术和品质，探索打造特色产业链，不断提高竞争力，成功开拓海外市场。便捷的交通基础设施、高水平的物流体系，内外联通，畅通了国际国内双循环，产品等得以高效率地流通，与其他国家合作共赢。我国经济发展的内生动力和可靠性不断增强，国际循环质量和水平不断提升。
66: 【细则】
67: 产业优势（内生动力）-3分
68: 生态优势转换为发展优势/生态效益与经济效益相统一 / 绿色环保/实现生态价值    1分
69: 特色资源禀赋（本地资源优势）/比较优势/特色产业/技术创新/质量品质    1分
70: ——竞争力提高/ 供给能力提升     1分
71: 物质条件-2分
72: 便捷的交通设施/基础设施/高水平物流体系/  1分  
73: ——内外联通/贸易便利化/降成本/提效率  1分  
74: 市场-2分   国内国际两个市场两种资源联动（拓宽市场/市场需求旺盛/市场广阔）/ 对外开放质量和水平提升   1分
75: ——互利共赢/循环质量和水平提升/ 双循环相互促进  1分
76: 以下答案不给分：
77: 顺应全球化趋势（无具体分析）/“引进来”和“走出去”相结合/引进外资
78: 供给侧结构性改革/产业结构优化升级/消费结构优化升级/增收入/促就业/
```
