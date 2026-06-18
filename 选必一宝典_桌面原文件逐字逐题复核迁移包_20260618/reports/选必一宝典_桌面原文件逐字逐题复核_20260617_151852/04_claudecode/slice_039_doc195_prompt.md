你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 195
- entry_id: Q0195
- question_ref: 2025西城期末Q20
- question_title: 2025西城期末Q20(2)
- bucket/sub_bucket: 经济全球化 / 国际分工、企业出海与国际竞争新优势
- core_point: 加强技术创新、提高产品质量，增强竞争力
- blocks: 2304-2316

# Desktop Original Excerpt

```text
2304: 1. 2025西城期末Q20(2)
2305: 【材料触发点】 读图显示中国电动载人汽车出口竞争力提升，但面对欧盟反补贴税形成的外部贸易壁垒，企业需要通过技术和质量优势增强国际竞争力。
2306: 【设问】 欧盟是中国整车出口的第一大市场，也是中国电动汽车出口的主要目的地。2024年10月，欧盟决定对从中国进口的纯电动汽车征收为期五年的高额反补贴税。中国汽车企业该如何应对？（6分）
2307: 【为什么能想到】 读图显示中国电动载人汽车出口竞争力提升，但面对反补贴税这种外部贸易壁垒，单靠规则维权不够，必须有产品本身的过硬支撑。问"企业该如何应对"——本条要切入"产品和质量"维度，把企业内功增强作为应对外部壁垒的基础。把出口竞争力数据作为继续加强技术创新和提高产品质量的依据，再写增强国际竞争力，最后指向以产品优势应对反补贴税等贸易壁垒。
2308: 【答案落点】 中国汽车企业应加强技术创新、提高产品质量，增强国际竞争力，以更强产品优势应对欧盟反补贴税等外部贸易壁垒。
2309: 【同题组】 （按原题答题层次）
2310: · 答题层次：本小题6分，答出3条并有具体说明即可满分；每条2分，观点1分、阐述1分。
2311: · 利用规则维权：充分运用国际规则，利用国际组织赋予的权利，对话磋商，积极维护自身权益。
2312: · 提升竞争力或竞争新优势：加强技术创新、提高产品质量，降低成本、提高要素资源利用率，调整产品结构，面向市场满足需求等。
2313: · 打破单一市场：实施出口市场多元化战略，减少对单一市场的依赖；也可写深耕国内市场、挖掘国内市场需求。
2314: · 对外直接投资：积极“走出去”，到其他国家投资设厂，开展多种合作，克服贸易壁垒。
2315: · 其他合理方向：整车出口变为零部件出口、培育出口新优势等，可作为同类补充。
2316: · 答题提醒：只罗列若干合理方向但没有阐述，整体最多按3分+1分处理；只写利用好国内国际两个市场、没有具体解释和分析，只给1分。
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
{"unique_id": "UQ0067", "normalized_question": "2025西城期末Q20(2)", "count": "3", "doc_orders": "195;202;214", "buckets": "经济全球化", "core_points": "充分运用国际规则，利用国际组织赋予的权利，对话磋商，积极维护自身权益;加强技术创新、提高产品质量，增强竞争力;实施出口市场多元化战略，减少对单一市场的依赖", "question_titles": "2025西城期末Q20(2) || 2025西城期末Q20(2) || 2025西城期末Q20(2)"}
```

# Prior Same-Source Context

No prior reviewed member in UQ0067 yet in this run. Important: this is 2025西城期末Q20(2), not 2026西城期末Q20.

# Codex Watchpoints To Verify, Not Blindly Accept

- Source prompt lines 311-317 and answer/rubric lines 167-190 identify 2025西城期末Q20(2).
- Current core is the competition/quality/technology angle; rubric lines 182-183 explicitly support it.
- Same-group notes should preserve the 3-of-4 scoring frame: rules-rights, competition, market diversification, going out; line 186 says two markets/resources without explanation only gets 1分.
- UQ0067 remains book-level pending across doc_orders 195/202/214.

# Source / Rubric Excerpts

## SRC_EXAM_2025_XICHENG_QIMO_Q20_2.txt
```text
SOURCE_ID: SRC_EXAM_2025_XICHENG_QIMO_Q20_2
TITLE: 2025西城期末Q20(2) 试卷/参考答案摘录
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025西城期末/试卷/试卷.pdf
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/3b9cf3beca8e__试卷.txt

## prompt/material lines 307-317
307: ===== PAGE 7 =====
308:  
309: 第7页/共10页 
310:  
311: 20．（9 分）读图，回答问题： 
312:  
313:  
314: （1）读图1 和图2，说明全球汽车产业链出口的竞争格局所发生的变化。（3 分） 
315:  
316: （2）欧盟是中国整车出口的第一大市场，也是中国电动汽车出口的主要目的地。2024 年10 月，欧盟决定
317: 对从中国进口的纯电动汽车征收为期五年的高额反补贴税。中国汽车企业该如何应对？（6 分） 

## reference-answer lines 413-418
413: 20.（9 分） 
414: （1）其他主要经济体（德日）的市场份额有所下降，中国汽车产业出口竞争力提升， 
415: 尤其电动载人汽车具有较大优势。（3 分） 
416: （2）充分运用国际规则，利用国际组织赋予的权利，对话磋商，积极维护自身权益； 
417: 加强技术创新、提高产品质量，增强竞争力；实施出口市场多元化战略，减少对单一市场的依赖；积极地
418: “走出去”，到其他国家投资设厂，开展多种合作，克服贸易壁垒。（6 分）
```
## SRC_RUBRIC_2025_XICHENG_QIMO_Q20_2.txt
```text
SOURCE_ID: SRC_RUBRIC_2025_XICHENG_QIMO_Q20_2
TITLE: 2025西城期末Q20(2) 正式细则摘录
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025西城期末/细则/细则.pdf
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/f548fe634936__细则.txt

## Q20 scoring lines 167-190
167: 20. （9 分） 
168: （1）其他主要经济体（德日）的市场份额有所下降，中国汽车产业出口竞争力提升，尤其
169: 电动载人汽车具有较大优势。 
170: （2）充分运用国际规则，利用国际组织赋予的权利，对话磋商，积极维护自身权益；加强
171: 技术创新、提高产品质量，增强竞争力；实施出口市场多元化战略，减少对单一市场
172: 的依赖；积极地“走出去”，到其他国家投资设厂，开展多种合作，克服贸易壁垒。
173: （6 分） 
174: 解析： 
175: （1）其他主要经济体(德日)的市场份额有所下降，中国汽车产业出口竞争力提升(市场份额
176: 上升)，尤其电动载人汽车具有较大优势 
177: （2）以下角度，答出3 条，并有具体说明，即可给满分，每条2 分（观点1 分，有所阐述
178: 1 分） 
179: 角度如下: 
180: 利用规则维权角度：充分运用国际规则，利用国际组织赋予的权利，对话磋商，积极维护
181: 自身权益; 
182: 提升竞争力或竞争新优势角度：加强技术创新、提高产品质量，(降低成本、提要要素资源
183: 利用率、调整产品结构、面相市场满足需求……) 
184: 打破单一市场角度：实施出口市场多元化战略，减少对单一市场的依赖(深耕国内市场，挖
185: 掘国内市场需求)。 
186: 注意:只写利用好国内国际两个市场没有具体解释和分析只给1 分。 
187: 对外直接投资角度：积极地“走出去”，到其他国家投资设厂，开展多种合作，克服贸易壁
188: 垒。 
189: 其他角度:如整车出口变为零部件出口，培育出口新优势等酌情给分 
190: 如果罗列了若干条都合理，但没有阐述和说明，总体给3 分+1 分
```
