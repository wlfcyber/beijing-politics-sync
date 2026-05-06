# ClaudeCode → Codex 待裁决冲突清单

## C1 — 2026朝阳期中 Q17 第二层分说之二的"高质量发展/经济平稳可持续发展"

- 现场证据：`codex_lane/extracted_text/SRC_763b7470b96b_细则.txt` 明确将"经济平稳可持续发展/高质量发展/注入新动能/降本增效/提高效率/优化资源配置/经济增长（1分）"列为本题阅卷细则采分点。
- Codex 当前 entry 把它放入"经济全球化"桶。
- 用户规则与 xuanbiyi-term-protocol：必修二语汇（高质量发展、新发展理念、扩大高水平对外开放、落实开放发展理念等）不得进入选必一主表，可放跨书脚注或边界附录。
- 冲突：Codex 把必修二语汇放进了选必一"经济全球化"主桶，违反边界规则。
- ClaudeCode 处置：本 lane 已把它降为"模块边界：必修二"条目，并保留细则原文证据。
- 待 Codex 裁决：在最终学生版里是 (a) 跨书脚注、(b) 单列边界附录、(c) 接受用户硬规则把它从主表移除并仅在频次统计文件里说明。

## C2 — 2026朝阳一模 Q20 第③点中的"扩大高水平对外开放"

- 现场证据：`codex_lane/extracted_text/SRC_ebbe85a1ee6f_细则.txt` 明确"中国坚定不移扩大高水平对外开放（1分）"。
- Codex 当前 coverage 备注说"boundary term 推进高水平对外开放 excluded from main xuanbiyi term slot"。
- ClaudeCode 同意排除入主表，但需要 Codex 在边界附录或频次统计中保留细则证据，避免后续重读时再次误判。
- 待 Codex 裁决：边界条目位置（必修二脚注 vs 选必一主表外注释）。

## C3 — 2026西城期末 Q20 用户硬规则要求"正式补入"，但完整设问缺失

- 现场证据：见 `blockers/2026西城期末_Q20_missing_full_prompt.md`。试卷文件在源目录中确实不存在；评标 PPT 与参考答案都没有完整设问。
- 冲突：用户硬规则把它列为"正式补入"，但 USER_FRAMEWORK 又把"完整设问"列为必备字段；普通参考答案不能冒充细则。两条都是用户规则，需用户裁决优先级或补提原题。
- 待 Codex/用户裁决：是否接受以"评标 PPT + 参考答案"反推设问、用"用户确认设问"层级补入；或者继续 blocked 等待原题。

## C4 — 2026石景山期末 全模块排除条款的复核范围

- 现场证据：用户硬规则在 `选必一_交付要求记事本.md` 与 SKILL.md 同时声明全模块排除，理由是"没有可用评分细则"。
- ClaudeCode 复核：本次 ClaudeCode 没有发现新的评分细则来源，也未发现用户撤回排除的迹象。
- 处置：保持全模块排除。普通参考答案不可推翻该硬排除。
- 待 Codex 行动：在 COVERAGE_MATRIX 与 SOURCE_LEDGER 里把石景山期末标记为 user_excluded，避免后续 worker 再读再爬。

## C5 — 2025海淀期中 Q21(2) 用户提到另有图片表格形式细则

- 现场证据：本 lane 仅复核到 DOCX 中的参考答案文本部分；用户提及"另有图片表格形式细则"。
- Codex 当前已视觉读取嵌入图（见 `audit/visual_read_2025海淀期中_media.md`），ClaudeCode 本次未单独再读图。
- 冲突可能：若 Codex 的视觉读取与 ClaudeCode 仅基于参考答案文本起草的 entry 在术语取词上不一致，需以 Codex 视觉读取的图细则为准。
- 待 Codex 行动：在 fusion 时核对 ClaudeCode `entries/2025海淀期中_Q16_Q21.md` 的 Q21(2) 段是否需要按图细则补术语。

## C6 — Codex `2026西城一模 Q20(2)` 视为 in_scope，需 Codex 出示原题与细则原文比对

- ClaudeCode 本次未单独读取该套源 DOCX；仅在 COVERAGE_MATRIX 上看到 Codex 已 drafted 5 entries。
- 待 Codex 行动：在 fusion 前把原题/细则关键段贴在 suite_report 中以便 ClaudeCode 复核；ClaudeCode 已在本 lane coverage CSV 里把该套标记为 codex_only_drafted（待复核）。
