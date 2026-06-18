你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 224
- entry_id: Q0224
- question_ref: 2024丰台一模Q20
- question_title: 2024丰台一模Q20
- bucket/sub_bucket: 经济全球化 / 产业链供应链与开放安全
- core_point: 维护全球产业链供应链稳定畅通
- blocks: 2639-2648

# Desktop Original Excerpt

```text
2639: 6. 2024丰台一模Q20
2640: 【材料触发点】 数字化技术、绿色低碳技术对应供应链成本高、信息不对称、环节不透明、流程不标准、管理不高效和发展不环保等问题，技术赋能是供应链高质量发展的机制。
2641: 【设问】 结合材料，运用《当代国际政治与经济》知识，说明我国的实践是如何推动供应链成为国际合作“共赢链”的。
2642: 【为什么能想到】 数字化技术、绿色低碳技术对应供应链成本高、信息不对称、环节不透明、流程不标准等痛点。技术赋能能降低成本、提高效率、改善绿色水平，因此指向供应链稳定畅通和高质量发展。
2643: 【答案落点】 中国支持企业运用数字化技术、绿色低碳技术降低供应链成本、提高运行效率，推动全球供应链高质量发展。
2644: 【同题组】 （按原题得分方式）
2645: · 答题层次：本题7分，按“知识+材料”的论述质量展开；只写纯知识或只描述材料，属于低档。
2646: · 分档方式：围绕下列四个方面展开，任选三方面且论述到位可达6-7分，任选二方面为4-5分，任选一方面为2-3分；没有论述或论述严重偏差为0-1分。
2647: · 答题提醒：即使写到三个方面，如果内容不贴切，或只是照搬材料、没有说明与国际合作“共赢链”的关系，也要降档。
2648: · 四个方面：建立和完善基础设施，推动产品、服务和生产要素在全球流动；加快供应链金融创新，缓解供应链发展中的资金短缺；打造国际经济合作交流平台，推进贸易投资自由化便利化；运用先进技术降低成本、提高效率，畅通全球产业链供应链，增强经济全球化活力，推动各国合作共赢。
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
{"unique_id": "UQ0061", "normalized_question": "2024丰台一模Q20", "count": "3", "doc_orders": "90;224;230", "buckets": "经济全球化", "core_points": "以产业链供应链合作推动互利共赢;推进贸易和投资自由化便利化;维护全球产业链供应链稳定畅通", "question_titles": "2024丰台一模Q20 || 2024丰台一模Q20 || 2024丰台一模Q20"}
```

# Codex Watchpoints To Verify, Not Blindly Accept

Verify the advanced-technology/digital-green supply-chain branch against 2024丰台一模 source; watch if it overstates fixed scoring where rubric is level-based rather than point-by-point fixed rubric.

# Source / Rubric Excerpts

## SRC_EXAM_2024_FENGTAI_YIMO_Q20.txt
```text
242: 20.(7 分)让供应链成为国际合作的“共赢链”。 
243: ➢ 中国已建成全球最大的高速铁路网、高速公路网、世界级港口群。 
244: ➢ 中国发起设立国际金融机构及投资基金，加快供应链金融创新发展，助推全球供应链向广大发展中国
245: 家延伸。 
246: ➢ 首届中国国际供应链促进博览会共有515 家中外企业和机构参展，共签署合作协议、意象协议200 多
247: 项，涉及金额1500 多亿元人民币。 
248: ➢ 中国大力推动和支持企业运用数字化技术、绿色低碳技术，有效解决全球供应链中的成本高、信息不
249: 对称、环节不透明、流程不标准、管理不高效、发展不环保等痛点问题。 
250: 中国近年来在国际经济贸易与合作方面的实践，彰显了持续推动高水平对外开放的决心与信心，为促进全
251: 球供应链开放合作贡献了中国力量。 
252: 结合材料，运用《当代国际政治与经济》知识，说明我国的实践是如何推动供应链成为国际合作“共赢
253: 链”的。 

370: 20.(7 分)我国通过建立和完善基础设施，推动产品、服务和生产要素在全球的流动，提高资源配 
371: 置效率；通过加快供应链金融创新，缓解供应链发展中资金短缺问题；通过打造国际经济合作交流 平
372: 台，推进贸易投资自由化便利化；通过运用先进技术降低成本、提高效率，推动全球供应链高质 
373: 量发展；通过畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢。
```
## SRC_RUBRIC_2024_FENGTAI_YIMO_Q20.txt
```text
110: 	•	结合材料，运用《当代国际政治与经济》只是，说明我国的实践是如何推动供应链成为国际合作“共赢链”的。
111: 参考答案：
112: 我国通过建立和完善基础设施，推动产品、服务和生产要素在全球的流动，提高资源配置效率；通过加快供应链金融创新，缓解供应链发展中资金短缺问题；通过打造国际经济合作交流平台，推进贸易投资自由化便利化；通过运用先进技术降低成本、提高效率，推动全球供应链高质量发展；通过畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢。
113: 评分标准说明：
114: 一类：以纯论述知识为主，或者纯描述材料，0-3分。
115: 二类：知识+材料的精准论述或浅层论述，对答案所提示的四个方面，任选其三，为6-7分；任选其二，4-5分；任选其一，2-3；无论述或论述严重偏差0-1分；
116: 注：若虽然论述了三个层面，但不贴切或照抄材料，降一档给分。
```

# Output Constraint

请保持严格、短而完整：总字数控制在 1200-1800 汉字；每个字段只写结论+关键行号；必须给 must-fix 和边界声明。不要展开长篇教材解释。
