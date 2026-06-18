你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 217
- entry_id: Q0217
- question_ref: 2026西城一模Q20
- question_title: 2026西城一模Q20(2)
- bucket/sub_bucket: 经济全球化 / 全球经济治理与规则权益
- core_point: 坚持多边贸易、多边主义与全球经济治理体系改革
- blocks: 2555-2565

# Desktop Original Excerpt

```text
2555: 1. 2026西城一模Q20(2)
2556: 【材料触发点】 设问把自贸区3.0版的作用从区域发展扩展到世界经济，说明答案不能只停留在双边贸易增加，还要上升到开放合作和多边贸易体系。
2557: 【设问】 结合材料，运用《当代国际政治与经济》知识，分析中国—东盟自贸区3.0版是如何为区域发展和世界经济注入强劲动力的。
2558: 【为什么能想到】 本题可从设问的“区域发展和世界经济”想到多边贸易和全球经济治理，但不能声称材料写了具体标准联合制定或打破垄断。自贸区升级本身体现开放包容、合作共赢的区域制度安排，区域开放合作的扩大能够为多边贸易体制和全球经济治理提供积极示范。
2559: 【答案落点】 中国—东盟自贸区3.0版坚持合作共赢和开放包容，推动多边贸易和多边主义发展，推动全球经济治理体系改革，为世界经济注入强劲动力。
2560: 【同题组】 （按原题答题层次）
2561: · 答题层次：本题8分，按标准规则2分、产业链供应链3分、综合意义2分、联系材料1分组织。
2562: · 标准规则（2分）：降低制度性交易成本/提高贸易效率（1分）；促进贸易投资便利化自由化、优化营商环境、破除贸易壁垒（1分）。
2563: · 产业链供应链（3分）：维护经济安全、统筹安全与发展、形成多元稳定经贸关系（1分）；发挥比较优势、优势互补、深度加入国际分工（1分）；促进产业协同、产业结构优化升级，带动就业、收入和税收（1分）。
2564: · 综合意义（2分）：对区域，推动地区经济转型升级、增强竞争力，或提升发展中国家的代表性和发言权、打破发达国家规则制定中的垄断主导（1分）；对世界，坚持合作共赢、开放包容和共同利益，维护多边贸易和多边主义，推动全球经济治理体系改革（1分）。
2565: · 联系材料（1分）：结合中国—东盟自贸区3.0版的具体安排作说明。
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
{"unique_id": "UQ0051", "normalized_question": "2026西城一模Q20(2)", "count": "5", "doc_orders": "96;204;217;218;231", "buckets": "经济全球化", "core_points": "发挥比较优势并打造国际竞争新优势;坚持多边贸易、多边主义与全球经济治理体系改革;推进贸易和投资自由化便利化;提升发展中国家的代表性和发言权，打破规则制定垄断;统筹发展和安全，形成多元稳定的经贸关系", "question_titles": "2026西城一模Q20(2) || 2026西城一模Q20(2) || 2026西城一模Q20(2) || 2026西城一模Q20(2) || 2026西城一模Q20(2)"}
```

# Codex Watchpoints To Verify, Not Blindly Accept

Verify whether the core `坚持多边贸易、多边主义与全球经济治理体系改革` is source-backed by rubric comprehensive/world layer line 79. Watch that the material trigger should not claim the original material wrote standards/joint standard-making/monopoly-breaking.

# Source / Rubric Excerpts

## SRC_EXAM_2026_XICHENG_YIMO_Q20_2.txt
```text
148: 20．（11分）中国与东盟自贸区合作迈入新阶段。
149: 材料一             
150: （1）概括材料一反映的经济信息。（3分）
151: 
152: 
153: 
154: 
155: 材料二 中国与东盟共同签署自贸区 3.0 版升级议定书，打造更高水平自由贸易协定，既顺应双方经济转型升级的现实需求，又为地区乃至全球发展注入更多确定性。  
156: 注：关键产品通常包括两方面内容。一是该产品对国家安全和经济发展具有重要性；二是该产品存在供应风险，如较为稀缺或对他国供应高度依赖。
157: （2）结合材料，运用《当代国际政治与经济》知识，分析中国—东盟自贸区3.0版是如何为区域发展和世界经济注入强劲动力的。（8分）
```
## SRC_RUBRIC_2026_XICHENG_YIMO_Q20_2.txt
```text
63: 20（1）概括材料一反映的经济信息。（3分）
64: 【细则】
65: ●2010年以来，东盟与中国货物贸易占比持续攀升（1分）。没有“占比”不得分。
66:     ●中国是东盟第一大贸易伙伴（1分）。变通：中国在东盟的贸易伙伴中“领先”“主导”“占比最高”“首位”等。写“主要贸易伙伴”不得分。
67: ●东盟对中国的贸易依存度不断提高，区域经济一体化程度加深。（任意一句得1分）变通：东盟与中国的经贸关系日益紧密、构建更紧密的中国—东盟命运共同体等。
68: （2）分析中国-东盟自贸区3.0版式如何为区域发展和世界经济注入强劲动力。（8分）
69: 【细则】
70: ●标准规则（2分）
71: 降低制度性交易成本/提高贸易效率   1分
72: 贸易投资便利化自由化/优化营商环境/破除贸易壁垒   1分
73: ●产业链供应链（3分）
74: 经济安全/统筹安全与发展/多元稳定的经贸关系  1分
75: 发挥比较优势/机会成本/优势互补/深度加入国际分工  1分
76:     产业就业 1分（产业协同、产业结构优化升级、产业发展带动就业收入税收等）
77: ●综合（2分）
78: 对区域：地区经济转型升级，增强竞争力/提升发展中国家的代表性和发言权/打破发达国家规则制定中的垄断主导  1分
79: 对世界：坚持合作共赢/开放包容/共同利益，坚持多边贸易/多边主义、全球经济治理体系改革  1分
80: ●联系材料（1分）
```

# Output Constraint

请保持严格、短而完整：总字数控制在 1200-1800 汉字；每个字段只写结论+关键行号；必须给 must-fix 和边界声明。不要展开长篇教材解释。
