你是 Claude Code，正在被 Codex 监督执行“飞哥政治庄园-选必一《当代国际政治与经济》双线总控”任务。

工作目录：

`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_双线总控_2026-05-02`

最高优先级：

1. 先读本目录下 `MASTER_REQUIREMENTS.md`、`TASK_BRIEF.md`、`USER_FRAMEWORK.md`、`USER_QUESTIONS.md`、`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`PROGRESS.md`、`findings.md`。
2. 再读：
   - `/Users/wanglifei/Desktop/北京高考政治/选必一复查_2026-04-29/选必一_交付要求记事本.md`
   - `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
   - `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
   - `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`
3. 本轮只做 Phase 2：独立源目录与候选题清单审计，不要生成最终文档，不要复制旧 v12 内容。

源目录：

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`

任务：

1. 检查 Codex 已生成的 `SOURCE_LEDGER.csv` 和 `codex_lane/source_inventory_summary.md` 是否覆盖源目录中的 Word/PDF/PPT/图片类材料。
2. 按套卷识别哪些最可能含 选必一《当代国际政治与经济》主观题与评分细则。不要只按文件名，要优先搜索题面词和细则词，例如：
   - 当代国际政治与经济
   - 国际关系、国家利益、共同利益、和平与发展、世界多极化
   - 经济全球化、贸易、投资、全球治理、国际组织、联合国
   - 中国方案、中国智慧、中国担当、人类命运共同体、多边主义
3. 对特别钉死的用户纠错样本做“是否进入后续抽取优先级”的判定：
   - 2026通州期末 Q20
   - 2026朝阳期中 Q17
   - 2025海淀期中 Q16(2)
   - 2025海淀期中 Q21(2)
   - 2025海淀期末 Q22
   - 2024东城一模 Q16
   - 2024东城一模 Q20
   - 2026海淀期末
   - 2026石景山期末
4. 输出一个 Markdown 报告到：
   `claudecode_lane/phase2_source_inventory_report.md`
5. 报告必须包含：
   - 源覆盖总评；
   - 高优先级套卷/题号清单；
   - 明确排除/暂不处理清单；
   - 需要 OCR/渲染/Word/PPT 视觉读取的材料；
   - 和 Codex 后续分工建议。

硬规则：

- 旧成果只能当用户硬规则和纠错参照，不能当来源证据直接复制。
- 普通参考答案不能冒充评分细则。
- 2026石景山期末默认全模块排除，除非你发现新的用户确认评分细则；若只有“答案及评分参考”，不得纳入。
- 如果 PDF、PPT、图片或表格需要处理，必须说明具体处理办法，不许因为一个工具不可用就放弃。
- 报告写清楚你看过哪些文件、哪些还没看、为什么。

完成后不要继续 Phase 3，等 Codex 融合检查。
