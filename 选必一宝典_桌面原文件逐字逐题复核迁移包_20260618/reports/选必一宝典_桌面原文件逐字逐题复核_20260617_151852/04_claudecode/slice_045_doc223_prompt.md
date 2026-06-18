你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 223
- entry_id: Q0223
- question_ref: 2025海淀期中Q16
- question_title: 2025海淀期中Q16(2)
- bucket/sub_bucket: 经济全球化 / 产业链供应链与开放安全
- core_point: 维护全球产业链供应链稳定畅通
- blocks: 2629-2638

# Desktop Original Excerpt

```text
2629: 5. 2025海淀期中Q16(2)
2630: 【材料触发点】 中国咖啡企业“出海”面对海外消费差异、供应链压力、知识产权和贸易风险，单靠企业经营策略不足，还要从国际规则和治理参与角度改善外部环境。
2631: 【设问】 结合材料三，从经济角度，为中国咖啡企业“出海”提出建议。
2632: 【为什么能想到】 出海要先铺供应链这一“底层基础设施”、且成本难压，链条一断经营就停摆，故须把它做稳做畅，落到维护全球产业链供应链稳定畅通。
2633: 【答案落点】 咖啡企业应打造稳定供应链、降低生产成本，维护全球产业链供应链稳定畅通，保障"出海"经营。
2634: 【同题组】 （按原题答题层次）
2635: · 答题层次：按答案链训练，不展示固定分值层次；围绕企业经营、政府支持与资源、贸易摩擦与规则三条建议链组织。
2636: · 企业经营层：客观看待“出海”的机遇与挑战，制定正确经营战略；重视海外市场考察研究，在充分了解市场信息基础上提高自主创新能力、形成竞争优势。
2637: · 政府支持与资源层：通过税收优惠等政策鼓励、支持企业积极参与经济全球化，充分利用国际国内两种资源、两个市场，打造稳定供应链、降低生产成本。
2638: · 贸易摩擦与规则层：面对国际贸易摩擦，政府和企业共同携手，充分利用国际组织赋予的权利，积极参与全球经济治理和规则制定，为企业“出海”营造良好的国际环境。
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
{"unique_id": "UQ0030", "normalized_question": "2025海淀期中Q16(2)", "count": "7", "doc_orders": "103;180;201;205;215;216;223", "buckets": "经济全球化", "core_points": "企业和政府可利用国际组织赋予的权利，积极参与全球经济治理和规则制定，为企业\"出海\"营造良好的国际环境;利用两个市场两种资源优化全球资源配置;加强技术创新、提高产品质量，增强竞争力;参与全球经济治理和规则制定，为企业出海营造国际环境;维护全球产业链供应链稳定畅通;顺应经济全球化趋势，主动融入并推动深化", "question_titles": "2025海淀期中Q16(2) || 2025海淀期中Q16(2) || 2025海淀期中Q16(2) || 2025海淀期中Q16(2) || 2025海淀期中Q16(2) || 2025海淀期中Q16(2) || 2025海淀期中Q16(2)"}
```

# Codex Watchpoints To Verify, Not Blindly Accept

Compare with Q0215/Q0216. This is the stable-supply-chain slice from 海淀期中 Q16(2); verify whether source supports `全球产业链供应链稳定畅通` or only `打造稳定供应链，降低生产成本`.

# Source / Rubric Excerpts

## SRC_EXAM_2025_HAIDIAN_QIZHONG_Q16_2.txt
```text
184: 材料三 在国内发展的同时，中国咖啡企业也开启了“出海”试验，以性价比、产品创新和营销为主
185: 打，在东南亚、日韩和北美市场“多点开花”。
186: 中国咖啡企业“出海”之路并非一帆风顺。消费品主要依赖品牌、产品、渠道竞争。不少海外市场已
187: 经培养了成熟的咖啡文化，消费者习惯、口味等方面与国内市场存在一定差异。“出海”需要提前建设供
188: 应链等底层基础设施，各地咖啡原材料成本难降，中国咖啡企业在成本端和管理端尚不具备优势。此外，
189: 知识产权保护方面也存在风险。近日，中国 L 公司诉泰国某公司侵犯商标权案以败诉落幕，后者甚至提起
190: 反诉，向L公司索赔100亿泰铢。
191: （2）结合材料三，从经济角度，为中国咖啡企业“出海”提出建议。
```
## SRC_RUBRIC_2025_HAIDIAN_QIZHONG_Q16_2.txt
```text
4: 16．（11分）
5: （1）可从生产技术、产品质量、消费方式、市场需求等角度回答。
6: （2）咖啡企业应客观看待“出海”的机遇与挑战，制定正确的经营战略，重视对海外市场的考察研究，在充分了解市场信息的基础上，通过提高自主创新能力形成自己的竞争优势。政府可以通过税收优惠等政策鼓励、支持企业积极参与经济全球化，充分利用国际国内两种资源、两个市场，打造稳定供应链，降低生产成本。面对国际贸易中出现的贸易摩擦，我国政府和企业要共同携手，充分利用国际组织赋予的权利，积极参与全球经济治理和规则制定，为企业“出海”营造良好的国际环境。
```

# Output Constraint

请保持严格、短而完整：总字数控制在 1200-1800 汉字；每个字段只写结论+关键行号；必须给 must-fix 和边界声明。不要展开长篇教材解释。
