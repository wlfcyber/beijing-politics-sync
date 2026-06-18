你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 222
- entry_id: Q0222
- question_ref: 2025延庆一模Q20
- question_title: 2025延庆一模Q20(2)外交部发言人回应"脱钩断链"
- bucket/sub_bucket: 经济全球化 / 产业链供应链与开放安全
- core_point: 维护全球产业链供应链稳定畅通
- blocks: 2617-2628

# Desktop Original Excerpt

```text
2617: 4. 2025延庆一模Q20(2)外交部发言人回应"脱钩断链"
2618: 【材料触发点】 材料二中个别国家鼓噪"脱钩断链"和供应链"去风险"，与近70个国家和地区企业到链博会寻找"链"通中外方案形成对照；要论证供应链合作的正当性，必须用时代主题判定"合作"才是符合潮流的方向，"脱钩"违背潮流。
2619: 【设问】 假如你是外交部发言人，请结合材料二，运用《当代国际政治与经济》知识，对上述提问做出回应。
2620: 【为什么能想到】 个别国家鼓噪脱钩断链，而各国企业来链博会寻找链通中外方案，直接指向维护全球产供链稳定畅通。
2621: 【答案落点】 维护全球产供链韧性和稳定是推动世界经济可持续发展的重要保障，“脱钩断链”损人不利己，中国愿携手各国打造“世界共赢链”。
2622: 【同题组】 （按原题答题层次）
2623: · 答题层次：本题8分，四个角度，每角度2分。
2624: · 时代主题：维护全球产供链韧性和稳定，是推动世界经济可持续发展的重要保障，符合国际社会共同利益，顺应和平与发展的时代主题。
2625: · 经济全球化方向：中国坚持高质量发展和高水平对外开放，反对“脱钩断链”，推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展。
2626: · 世界多极化：世界多极化是当今国际形势的突出特点，“脱钩断链”损人不利己；中国在追求本国利益的同时兼顾他国合理关切，推动各国深化产供链合作、共建“世界共赢链”。
2627: · 人类命运共同体：中国愿同各国携手维护全球产业链供应链稳定畅通，凝聚合作共识，共筑人类命运共同体。
2628: · 可替代提醒：国家利益、国际关系、多边主义等角度可替代作答，但与前面角度意思重复时不重复计算。
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
{"unique_id": "UQ0019", "normalized_question": "2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\"", "count": "8", "doc_orders": "4;38;65;222;330;361;379;530", "buckets": "中国;政治多极化;时代背景;理论;经济全球化", "core_points": "和平与发展仍是时代主题;国家间共同利益是国家合作的基础;展现大国责任担当;推动国际关系民主化;推动构建人类命运共同体;维护全球产业链供应链稳定畅通;维护国家利益是主权国家对外活动的出发点和落脚点;践行真正的多边主义", "question_titles": "2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\" || 2025延庆一模Q20(2)外交部发言人回应\"脱钩断链\""}
```

# Codex Watchpoints To Verify, Not Blindly Accept

Verify whether the `产供链韧性和稳定` answer sits in the time-theme/global supply-chain angle. Check whether the world multipolarity / human-community layers in 同题组 are source-backed and whether this card should keep only the supply-chain slice.

# Source / Rubric Excerpts

## SRC_EXAM_2025_YANQING_YIMO_Q20_2.txt
```text
212: 材料二 随着多元化、数字化、绿色化方面的发展机遇不断涌现，各国企业纷纷展现出加强产业链供
213: 应链合作的需求和期待。
214: 2024年11月，第二届中国国际供应链促进博览会（简称“链博会”）作为全球首个以供应链为主题
215: 的国家级展会在北京举办。面对全球化遭遇逆流、贸易保护主义抬头，地缘冲突加剧等多重挑战，近70
216: 第7页/共10页
217: --- page 8 ---
218: 个国家和地区的600余家企业和机构在相聚、相交、相融中携手寻找“链”通中外的新方案，谱写合作共
219: 赢的新篇章。他们普遍认为，从促进基础设施互联互通，到推动供应链数字化智能化，再到签署一系列自
220: 贸协定，中国一直在为全球供应链注入“润滑剂”。
221: 然而，个别国家在霸权和冷战思维作祟下，鼓噪“脱钩断链”，酝酿出加征关税、限制投资、收紧出
222: 口管制等举措，以维持本国在相关技术领域以及全球产供链中的主导地位。对此，在外交部例行记者会
223: 上，有记者提问：“很多‘链博会’参展外宾表示‘脱钩断链’损人不利己，建好‘共赢链’才是众望所
224: 归。发言人对此有何评论”？
225: （2）假如你是外交部发言人，请结合材料二，运用《当代国际政治与经济》知识，对上述提问做出回
226: 应。

292: （2） 回应要点： ① 经济全球化不可逆转，人为“脱钩断链”违背市场规律，损害全球共同利益。
293: ② 中国坚持开放合作，通过链博会、自贸协定等推动供应链互联互通，为全球注入稳定性和正能量。
294: ③ 反对保护主义，倡导各国在平等互利基础上加强合作，共同维护产业链供应链安全畅通。
```
## SRC_RUBRIC_2025_YANQING_YIMO_Q20_2.txt
```text
87: 	•	（8分）
88: 维护全球产供链韧性和稳定，是推动世界经济可持续发展的重要保障，符合国际社会的共同利益，顺应和平与发展的时代主题。（2分）中国将继续坚持高质量发展和高水平对外开放，推动经济全球化朝着开放、包容、普惠、平衡、共赢的方向发展。（2分）世界多极化是当今国际形势的突出特点，‘脱钩断链’损人不利己，作为负责任大国，中国在追求本国利益的同时兼顾他国合理关切，愿携手各国让链博会的“朋友圈”越来越大，让各国深化产供链合作的共识越来越强，将全球供应链真正打造为“世界共赢链”，共筑人类命运共同体。（4分）
89: 细则：时代主题2分；经济全球化方向2分；多极化2分；人类命运共同体2分。
90: 	•	（国家利益、国际关系、多边主义等角度可替代，不重复给分）
```

# Output Constraint

请保持严格、短而完整：总字数控制在 1200-1800 汉字；每个字段只写结论+关键行号；必须给 must-fix 和边界声明。不要展开长篇教材解释。
