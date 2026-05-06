# Decision: After Batch04B Next Step

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex A / Decision Maker

Scope: 只裁决 Batch04B 后的下一步；不改总表、不改学生稿、不宣布最终成品。

## 裁决

允许进入 `Batch04C 东城扩展`，但只进入 `source triage -> worker evidence candidate -> Patcher/Governor narrow gate`，不得直接写主融合总表、学生正文、Word/PDF 或 coverage closed。

理由：

1. Batch04A 海淀与 Batch04B 西城已经进入 `candidate_with_fixes / boundary rows`，当前没有必须等待的西城总阻断。
2. 海西东朝顺序已经完成海淀、西城的候选窄门，下一瓶颈自然转到东城原始源扩展。
3. 当前 Governor 只放行内部预览与 coverage expansion；所以东城可以开工，但所有新题只能先作为候选或边界行。

## 下一 60 分钟瓶颈

真正瓶颈不是继续改学生稿，也不是合并总表，而是把东城候选题逐一做 `题面-评分源-题号-模块边界` 对齐。

优先顺序：

1. `2025东城一模 Q20`
   - 优先原因：题面明确指向《当代国际政治与经济》，且已有 P0 评分源候选。
   - 劳动者先核验 `SRC_d39f12bd12f3` 与 `SRC_da5883631078` 是否能形成题号、材料、设问、给分口径闭环。
2. `2025东城二模 Q20`
   - 优先原因：题面明确为国际背景/全球挑战小论文，选必一信号强。
   - 劳动者核验 `SRC_bd8e9436f81d` 与 `SRC_e1c925184ab8` 的评分细则是否直接覆盖 Q20。
3. `2025东城期末 Q20`
   - 优先原因：当前候选文件显示有 P0/试卷组合，可能补足东城期末类样本。
   - 先做题号锚点和评分页定位；若只见参考答案，降为 `reference-only`。
4. `2026东城期末 Q20`
   - 优先原因：题面强，涉及全球治理、人类命运共同体、中国倡议。
   - 关键风险：当前评分源候选 `SRC_88c6e8f353db` 的可见锚点偏向 Q16/Q17/Q18；劳动者必须先证明评分细则直接覆盖 Q20。未证明前只能标 `needs_scoring_alignment`，不得升格。
5. `2024东城二模 Q20/Q21`
   - 优先原因：有阅卷总结/分题细则候选，但视觉或题号对齐风险更高。
   - 先核 `SRC_593d33b50bbf`、`SRC_82b0237dce42`、`SRC_322c2db4a7fe`、`SRC_144e07c6e537` 与试卷 `SRC_6a382f2c9e97`；凡空文本、截图不清、题号不稳，一律 `visual_needed`。
6. `2026东城一模 Q19(3)/Q20`
   - 只作边界候选。
   - Q19(3) 可能是高水平对外开放/经济模块混合；Q20 可能是生态综合与人类命运共同体表达。未确认模块边界前不得进入主链。

## 给各角色的任务

### Codex生产

- 开启 `Batch04C 东城扩展` 的生产队列，保持 Batch04A/B 现有 `candidate_with_fixes / boundary_only` 状态不回退。
- 只安排东城 source triage 与候选证据卡，不安排学生稿改写。
- 把劳动者首批限制在上面 1-4 项；2024东城二模和 2026东城一模作为第二波，不抢先膨胀。
- 若 Patcher/Governor 对 Batch04B 还有微修，允许并行处理；除非他们发现西城误升主链或参考答案被当细则，否则不阻塞 Batch04C。

### 劳动者

- 先做 source triage，再做条目草案。
- 每个候选题必须写清：
  - `suite`
  - `question`
  - `paper_source_id`
  - `scoring_source_id`
  - `scoring_source_type`
  - `prompt_anchor`
  - `rubric_anchor`
  - `xuanbiyi_signal`
  - `boundary_risk`
  - `recommended_action`
- 若评分源只给参考答案、答案示例、材料解释，不给评分口径，标 `reference-only`。
- 若题面属于法律、必修二经济、生态综合、哲学/文化等混模块，只写 `boundary_only`，不得硬挂选必一。

### 补丁者 / Patcher

- 第一轮只查劳动者的证据等级和边界，不要求润色。
- 必查冲突：
  - 题号是否被错配，尤其 2026东城期末 Q20。
  - `共同利益` 是否被误扩成所有国际合作万能模板。
  - `人类命运共同体/中国方案/全球治理` 是否被重复拆成多条频次膨胀项。
  - 高水平对外开放、国际竞争、市场资源配置是否越界混入必修二主链。
  - 普通参考答案是否被误写成评分细则。
- 输出建议只能是 `pass_with_fixes`、`boundary_only`、`needs_scoring_alignment`、`block`，不得写 final pass。

### Governor

- 只做 narrow gate，不做最终验收。
- 放行条件：
  - 评分源为评分细则、评标、阅卷总结或明确给分口径。
  - 题号锚点稳定，题面和评分源能互相对上。
  - 选必一模块边界清楚。
  - 同义项合并，不制造频次幻觉。
- 阻断条件：
  - 只有参考答案或旧产物，无原始评分口径。
  - 题号无法稳定对齐。
  - 明显跨模块，却被写入选必一主链。
  - 有人试图把 Batch04C 直接写进学生稿、正式 Word/PDF 或宣布完成。

### 自动化检测者

- 检查本轮没有修改学生稿、主融合总表、正式 Word/PDF。
- 检查没有重新打开或纳入 `2026石景山期末`。
- 检查 Batch04C 新增候选行均带 source id、证据等级、题号、action。
- 检查 A/B 状态没有被回退或覆盖。
- 检查所有 `reference-only / boundary_only / needs_scoring_alignment / visual_needed` 没有被误算为 coverage closed。

## 不应阻塞事项

- Batch04B 的 `PASS_WITH_GUARD` 不阻塞东城扩展。
- 个别东城套卷无选必一主观题不阻塞下一套；记录 `no_xuanbiyi_signal` 后继续。
- 2026东城期末 Q20 的评分源暂未对齐不阻塞 2025东城一模、2025东城二模、2025东城期末先做。
- 2024东城二模需要视觉核验不阻塞前四项。
- 边界行存在不阻塞 coverage expansion，但阻塞其进入主链或学生正文。

## 当前禁止

- 禁止宣布最终成品。
- 禁止改学生稿。
- 禁止改主融合总表或 coverage closed。
- 禁止用普通参考答案升级为评分细则。
- 禁止把空文本、疑似截图、旧 rerun 产物当作原始证据。
- 禁止纳入 `2026石景山期末`。
