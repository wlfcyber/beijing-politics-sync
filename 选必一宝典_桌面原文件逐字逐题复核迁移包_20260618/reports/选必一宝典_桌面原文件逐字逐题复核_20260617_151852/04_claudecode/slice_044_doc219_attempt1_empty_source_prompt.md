你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 219
- entry_id: Q0219
- question_ref: 2026朝阳一模Q20
- question_title: 2026朝阳一模Q20
- bucket/sub_bucket: 经济全球化 / 产业链供应链与开放安全
- core_point: 维护全球产业链供应链稳定畅通
- blocks: 2585-2594

# Desktop Original Excerpt

```text
2585: 1. 2026朝阳一模Q20
2586: 【材料触发点】 中国AI眼镜、开源大模型、创新药等创新成果说明中国科技实力增强，答案要把“创新驱动—全球创新策源地—产业链供应链稳定”写成能力链条。
2587: 【设问】 结合材料，运用《当代国际政治与经济》的知识，阐述中国为什么能为全球发展注入稳定性和正能量。
2588: 【为什么能想到】 材料列出AI眼镜、开源大模型、创新药等具体创新成果，说明中国不是只表达合作意愿，而是具备稳定全球产业链供应链的科技和产业能力。问“中国为什么能”注入稳定性，要把这些创新成果转化为全球创新策源和产业链供应链韧性的支撑。
2589: 【答案落点】 当前国际竞争的实质是以经济和科技实力为基础的综合国力较量，中国坚持创新驱动发展战略，科技实力日益增强、创新势能持续迸发，成为全球创新策源地，为全球产业链供应链稳定提供坚实支撑。
2590: 【同题组】 （按原题答题层次）
2591: · 答题层次：本题8分，按必答点、共享发展经验、发展潜力三个层次组织；全题总分不超过8分，发展潜力角度最多5分。
2592: · 必答点（2分）：当前国际竞争的实质是以经济和科技实力为基础的综合国力较量1分；中国坚持创新驱动战略，科技实力日益增强，成为全球创新策源地，为全球产业链供应链稳定提供坚实支撑1分。
2593: · 共享发展经验（3分）：通过分享减贫经验、生态治理经验、职业教育经验等助力发展中国家持续发展，并展现大国责任担当、正确义利观、中国智慧或中国方案1分；改善发展中国家民生1分；推动构建人类命运共同体1分。
2594: · 发展潜力和开放合作（最多5分）：共享中国发展机遇、超大规模市场潜力、两个市场两种资源；坚定不移扩大高水平对外开放；推动贸易投资自由化便利化；推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展；推动合作共赢的新型国际关系；坚持共商共建共享；促进人才、商品、服务和生产要素全球流动；符合和平与发展时代主题。以上方向按有效表达取分，每个方向1分。
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
{"unique_id": "UQ0002", "normalized_question": "2026朝阳一模Q20", "count": "15", "doc_orders": "13;50;76;78;118;153;168;219;250;278;435;490;500;504;529", "buckets": "中国;政治多极化;时代背景;理论;经济全球化", "core_points": "与发展中国家共享发展新机遇，惠民生增福祉，实现互利共赢;中国扩大高水平对外开放与制度型开放;促进全球资源优化配置和国际贸易发展;共商共建共享的全球治理观;利用两个市场两种资源优化全球资源配置;和平与发展仍是时代主题;坚持正确义利观;展现大国责任担当;当前国际竞争的实质是以经济和科技实力为基础的综合国力较量;推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展;推进贸易和投资自由化便利化;改善发展中国家民生并助力持续发展;相互尊重、公平正义、合作共赢的新型国际关系;维护全球产业链供应链稳定畅通;贡献中国智慧、中国方案、中国力量", "question_titles": "2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20 || 2026朝阳一模Q20"}
```

# Codex Watchpoints To Verify, Not Blindly Accept

Verify that AI眼镜、开源大模型、创新药 support the innovation/global innovation source/industrial-chain stability branch and that `当前国际竞争的实质...` is a rubric必答点, not invented.

# Source / Rubric Excerpts

## SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt
```text

```
## SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt
```text

```

# Output Constraint

请保持严格、短而完整：总字数控制在 1200-1800 汉字；每个字段只写结论+关键行号；必须给 must-fix 和边界声明。不要展开长篇教材解释。
