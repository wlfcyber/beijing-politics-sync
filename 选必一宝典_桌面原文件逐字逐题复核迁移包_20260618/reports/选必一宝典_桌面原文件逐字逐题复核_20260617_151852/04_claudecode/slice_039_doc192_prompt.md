你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 192
- entry_id: Q0192
- question_ref: 2026东城二模Q20
- question_title: 2026东城二模Q20(3)
- bucket/sub_bucket: 经济全球化 / 兼：国内国际两种资源两个市场
- core_point: 促进国内国际双循环，让世界共享中国发展机遇
- blocks: 2259-2268

# Desktop Original Excerpt

```text
2259: 1. 2026东城二模Q20(3)
2260: 【材料触发点】 中国消费市场与外商投资相互促进，使中国市场和世界市场形成更顺畅互动。
2261: 【设问】 结合材料三，运用《当代国际政治与经济》知识，分析购在中国与投资中国如何协同发力，释放我国独特的开放红利。
2262: 【为什么能想到】 消费市场与外商投资互为前提、互相放大——中国市场与世界市场不再分隔，而是在购销与投资两端形成顺畅互动。问"释放独特开放红利"，红利体现在国内市场与国际市场之间循环更顺畅，必须把双循环的结构性优势说出来。先把购在中国与投资中国互相促进作为双循环的现实表现点出；再写它促进国内国际两个循环顺畅互动；进而接到推动高水平对外开放，让世界共享中国发展机遇。
2263: 【答案落点】 购在中国和投资中国协同发力，促进国内国际双循环，推动高水平对外开放，让世界共享中国发展机遇。
2264: 【同题组】 （按原题答题层次）
2265: · 答题层次：本题7分，按“购在中国”吸引“投资中国”3分、“投资中国”推动“购在中国”3分、二者协同影响1分组织。
2266: · 第一层：“购在中国”吸引“投资中国”（3分）：激活入境消费需求、扩大入境消费规模或提升入境消费吸引力1分；发挥我国超大规模市场优势1分；消费牵引投资、吸引外商“投资中国”、推动全球要素集聚或引进来1分。
2267: · 第二层：“投资中国”推动“购在中国”（3分）：坚持制度型开放、发挥政策优势、鼓励支持非公经济发展、营造良好营商环境或促进投资自由化便利化1分；推动国内产业升级、产业结构优化、提升供给质量、供给侧结构性改革或产业创新1分；推动“购在中国”提质扩容、红利惠及全球消费者或吸引更多入境消费1分。
2268: · 第三层：二者协同发力的影响（1分）：促进国内国际双循环、推动高水平对外开放、让世界共享中国发展机遇，任意一点即可。
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
{"unique_id": "UQ0046", "normalized_question": "2026东城二模Q20(3)", "count": "5", "doc_orders": "94;162;192;193;194", "buckets": "经济全球化", "core_points": "中国扩大高水平对外开放与制度型开放;促进国内国际双循环，让世界共享中国发展机遇;发挥我国超大规模市场优势;推动全球要素向中国市场集聚;推进贸易和投资自由化便利化", "question_titles": "2026东城二模Q20(3) || 2026东城二模Q20(3) || 2026东城二模Q20(3) || 2026东城二模Q20(3) || 2026东城二模Q20(3)"}
```

# Prior Same-Source Context

Prior same-source context: doc94 was NEEDS_FIX because the prompt dropped quoted brand names and the trigger imported generic 通关/准入/协议/人员往来 language. doc162 was PASS because the row validly focused on 投资中国/制度型开放 and quote punctuation was treated as optional. This doc192 must be judged on its own exact blocks.

# Codex Watchpoints To Verify, Not Blindly Accept

- Source prompt line 127 uses “购在中国” and “投资中国” as quoted brand names and includes （7分）; desktop prompt may omit quotes and score.
- Rubric lines 17-21 and 39 support the total layer: double circulation, high-level opening, world shares China opportunity; teacher reference line 154 has the full wording.
- Rubric text extract line 39 truncates 机遇 at 机; do not treat the text-extract truncation as a source concept error when teacher answer line 154 supplies full wording.
- UQ0046 remains book-level pending across doc_orders 94/162/192/193/194.

# Source / Rubric Excerpts

## SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt
```text
SOURCE_ID: SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3
TITLE: 2026东城二模Q20(3) 试卷/教师版参考答案
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026东城二模/试卷/2026北京东城高三二模政治（教师版）.docx
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/新题增补_哲学_选必一_2026-05-18/01_source_packets/texts/2026东城二模__试卷__2026北京东城高三二模政治（教师版）.txt

## prompt/material lines 119-127
119: 20．（18分）“中国服务”“购在中国”“投资中国”……一张张名片，勾勒出生机勃勃、开放包容的中国形象。某班同学围绕这三大品牌，开展探究性学习活动。
120: 材料一
121: 材料二  多措并举促进服务消费高质量发展：设立专项基金，加大对软件和信息技术等生产性服务业支持力度，加大对住宿餐饮、文娱、教育等重点领域信贷支持；创新“旅游+”“体育+”“演艺+”等融合消费场景，开展服务消费季、中华美食荟等主题活动；强化跨部门联合监管，加强家政等领域的信用体系建设，完善服务消费领域标准。
122: （1）概括材料一反映的经济信息。（4分）
123: （2）运用《经济与社会》知识，说明材料二中的举措如何促进服务消费高质量发展。（7分）
124: 材料三  我国持续打造“购在中国”品牌，丰富国货潮品、中华老字号供给，优化入境消费服务，出台离境退税政策，推动购物、旅游、展演等业态融合。2025年，全国口岸出入境外国人8203.5万人次，同比增长26.4%。
125: 我国持续擦亮“投资中国”名片，实施《鼓励外商投资产业目录（2025年版）》，对接国际标准，扩大服务业市场准入，落实外资税收抵免政策。2026年1——2月，全国新设立外资企业同比增长14％，实际使用外资金额1614.5亿元。
126: 中国不断释放独特的开放红利，为不确定的世界注入更多的确定性。
127: （3）结合材料三，运用《当代国际政治与经济》知识，分析“购在中国”与“投资中国”如何协同发力，释放我国独特的开放红利。（7分）

## teacher reference answer lines 151-154
151: 20.(18分)
152: (1)2021—2025 年我国服务业增加值持续增长，居民人均服务性消费支出不断提高。服务业规模不断扩大为居民服务性消费增长提供支撑，居民服务性消费提高拉动服务业发展。
153: (2)降低服务供给成本，扩大优质服务供给，促进服务消费提质扩容。发展融合业态，丰富服务消费体验，激发消费活力，培育服务消费新增长点。规范服务消费市场秩序，营造良好的服务消费环境，提升服务消费意愿和信心，促进服务消费持续高质量发展。
154: (3)优化供给和服务，降低入境消费制度性成本，激活入境消费需求，依托我国超大规模市场优势，吸引外商“投资中国”，推动全球资本等要素集聚，实现互利共赢。坚持制度型开放，促进投资自由化便利化，推动产业结构优化，推动“购在中国”提质扩容，让红利惠及全球消费者。消费和投资协同发力，促进国内国际双循环，推动更高水平开放型经济的发展，为世界发展提供中国机遇。
```
## SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt
```text
SOURCE_ID: SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3
TITLE: 2026东城二模Q20(3) 专门细则
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026东城二模/细则/26年东城二模20（3）.pdf
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/新题增补_哲学_选必一_2026-05-18/01_source_packets/texts/2026东城二模__细则__26年东城二模20（3）.txt

## rubric and point layers lines 16-39
16: ===== PAGE 2/4 =====
17: （3 ）优化供给和服务，降低入境消费制度性成本，激活入境消费需求，/ 依托我国超大规模市场优势，
18: / 吸引外商“投资中国” , 推动全球资本等要素集聚，实现互利共赢。// 坚持制度型开放，促进投资自
19: 由化便利化，/ 推动产业结构优化，/ 推动“购在中国”提质扩容，让红利惠及全球消费者。// 
20: 消费和投资协同发力，促进国内国际双循环，推动更高水平开放型经济的发展，为世界发展提供中国机遇
21: 。
22: 第一层：“购在中国”吸引“投资中国”（3 分）（基本路径：激活入境消费→发挥大市场优势→牵引投资）
23: •
24: “ 购在中国”举措对消费的影响（1 分）：激活入境消费需求/ 扩大入境消费规模/ 提升入境消费吸引力
25: •
26:   释放的开放红利（1 分）：发挥我国超大规模市场优势 
27: •
28:   对“投资中国”的影响（1 分）：消费牵引投资/ 吸引外商“投资中国” / 推动全球要素集聚/ 引进来
29: 第二层：“投资中国”推动“购在中国”（3 分）（基本路径：发挥政策优势吸引外资→推动产业升级→扩大入境消
30: 费）
31: •
32: 释放开放红利吸引外资（1 分）：坚持制度型开放/ 发挥政策优势/ 鼓励支持非公经济发展/ 营造良好营商环境
33: / 促进投资自由化便利化
34: •
35: 引入外资对供给的影响（1 分）：推动国内产业升级/ 产业结构优化/ 提升供给质量/ 供给侧结构性改革/ 产业
36: 创新
37: •
38: 对“购在中国”的影响（1 分）：推动“购在中国”提质扩容/ 红利惠及全球消费者/ 吸引更多入境消费
39: 第三层：（总）二者协同发力的影响（1 分）：促进国内国际双循环/ 推动高水平对外开放/ 让世界共享中国发展机
```
