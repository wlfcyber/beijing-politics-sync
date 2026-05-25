# Claude External Review Result V1

Status: `EXTERNAL_REVIEW_DONE_NOT_PASS`

Reviewer lane: independent Claude external review V1, distinct from ClaudeCode B 线生产和 Claude V0 外审。本文件是本审唯一权威产物。

Scope: TASK_BRIEF / PROGRESS / 06_claude_review/V0 / 04_fusion 全部六件 / 03_claudecode_lane 三件 / 01_source_inventory/QUESTION_COVERAGE_MATRIX / 02_codex_lane 三件（FAMILY_SOURCE_PACKETS_Q0006_Q0012、B_ADDITIONS_BACKCHECK_Q0018_Q0026、四张 ledger CSV）+ A_LINE_STATUS + 06_claude_review/EXTERNAL_REVIEW_STATUS。专项回查：Q0011 错路由是否真正删除、四块/五元素索引是否落到正文、PROMOTION_GATE 是否阻断 V0 既有失效模式。

## Verdict

**NOT_READY_FOR_FINAL — V1_DRAFT_PARTIALLY_REPAIRED_REQUIRES_BODY_REWRITE_AND_REAL_EXTERNAL_REVIEW_BEFORE_V2.**

V1 在四个结构动作上的确推进了：(a) Q0011 路由从“科学思维单角度”改成“科学思维总帽下三模块复合 2/3/2”，错路由 header 已物理删除，只留作反例警告；(b) PROMOTION_GATE/LOG/HOLD/BLOCKER_RECONCILIATION 四件套建立，账目对账更明确；(c) Q0018-Q0026 已分配 Q-ID 并 source-locked 至 `A-formal`；(d) 思维册顶部 V1 四块触发索引、推理册顶部 V1 形式化索引、选择题选项原文（Q0004/Q0012/Q0015/Q0016/Q0017/Q0024）已实质回填。

但 V1 仍有三类未释放的硬伤：

1. **F1 修补不完整。** 错路由 header 已删，新路由 framework_node 已写齐，BLK-001 也按 `closed_by_correction` 落账。但 V0 F1 的 (b) 项 "Q0011 在思维宝典三个节点（科学思维 / 创新思维 / 辩证思维）互相 cross-ref" 未落实——`THINKING_BAODIAN_REVIEW_DRAFT.md` 中 Q0011 只挂在 §一.2，§二（辩证思维）和 §三（创新思维）的目录里完全找不到 "另见 Q0011" 之类指针。学生从辩证或创新章节进入时，看不到 Q0011 这个 7 分复合题。同时 Q0011 V1 四块表的"易错边界"只写 "上限就是科学思维角度 2 分"，是给老师/审稿人看的扣分口径，不是给学生看的"写哪种话术会丢分"。
2. **V1 索引表加在顶部，但章节正文未跟上四块/五元素纪律。** F2/F4 V0 缺口名义"阶段性清掉"，但只是把每行 4 / 5 块塞进了顶部表格；章节 prose 仍是触发口诀+答题模板二段式，"为什么能从该材料想到这个方法"这一教学桥段在两本宝典正文里 0 次出现（grep `为什么` 命中均为元描述、无教学性问句）。学生只读章节、不读顶部表的话，跟 V0 体验差别有限。
3. **真实外审尚未做。** PROMOTION_GATE Check 7 明确要求 GPT Pro / Claude 外审"必须是真实外审输出，不得 Codex/ClaudeCode 自评"。`EXTERNAL_REVIEW_STATUS.md` 自承 "V1 外审包尚未提交"。然而 `PROMOTION_LOG.md` 已把 Q0011 标 `promote_to_v1_candidate_after_f1_fix`，把 Q0018-Q0026 标 `source_locked_hold_for_v1_review`——这两个状态名带 V1，会被后续阶段误读为 "已通过 V1 门"。门控自身被绕过了一步。

此外，覆盖压力没有变化：26 条 source-locked vs 估计 60+ 题，BLK-002/005/006/007/008/009/010 全 open；选言推理、北京高考 19(2) 仍无 source-lock。

未达可发布门槛。下一步只能进入 V2 重写 + 真实 V1 外审，不得对外宣称已完成 / 已审完 / 已通过。

## Findings Table

| # | 严重度 | 文件 / 位置 | 问题 | 必须修正 |
|---|---|---|---|---|
| F1 | **Critical** | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §二、§三 目录 + Q0011 单一挂点 §一.2 | V0 F1 修复要求 Q0011 "在三个节点互相 cross-ref"，实际只在 §一.2 出现；§二（辩证思维）和 §三（创新思维）章节里没有任何指针 "另见 Q0011 / 此题在 §一.2 已作为 7 分复合题分析"。学生从辩证或创新章节查找复合题时，依旧拿不到这道题。F1(b) 未真正闭合，BLK-001 的实际教学效果只完成一半。同时 Q0011 V1 四块表的 "易错边界" 只写 "上限就是科学思维角度 2 分"，是扣分口径，不是写作失误清单——学生不知道"写哪个话术会出问题"。 | (a) 在思维册 §二 末尾新增 "复合题指针：见 §一.2 Q0011 辩证思维 2 分模块（整体性 / 分析与综合 / 矛盾分析法）"；§三 末尾同样新增 "复合题指针：见 §一.2 Q0011 创新思维 3 分模块（三新 / 发散聚合 / 超前）"。(b) Q0011 的"易错边界"必须改写成学生写作失误清单：①只写客观性 / 预见性 / 可检验性等"科学思维三性"词→被锁 2 分；②漏写"思路新 / 方法新 / 范围对象内容更丰富 / 创造性解决问题"→丢 3 分（创新模块）；③漏写"整体性 / 分阶段实施 / 任务明确"→丢 2 分（辩证模块）；④把"整体性"误写为"系统优化"或"分析综合"以外的辩证术语→部分给分。(c) 四块表的 "卷面答案句" 现写"体现辩证思维整体性"——应同时点 "整体性 + 分析综合"两层，与 §一.2 prose 一致，避免 4 块表与正文相互不齐。 |
| F2 | **High** | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` 全册章节正文；`04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` 全册章节正文 | V0 F2/F4 仅"阶段性清掉"——四块索引和形式化索引已加到顶部表格，但章节 prose 依旧是触发口诀+答题模板二段式。grep `为什么` 命中 0 处教学性问句。Q0019 §三.2 正文 7 行；Q0023 §五.1 正文只 "触发口诀+答题策略"，无答案句；Q0018 §六.1 正文 3 句，无同类题对比；Q0025 晏子 §七 1 段，无答题模板；Q0020 在 §一.2 完全和 Q0008 并入同一形式，不展开。结果是：学生只读章节、不读顶部表，体验与 V0 接近。 | 每个章节正文严格 4 块（思维）/ 5 块（推理）化：① 材料动作（带原句关键词）② 为什么联想到这个方法（教学桥段、必须有"问号"）③ 卷面答案句（学生可逐字搬上考卷的话术）④ 易错与边界（写作失误清单，不是扣分口径）⑤（推理）同类题对比（列 Q-ID + 差别）。顶部索引表只是脚手架，body 必须独立完整、可剪贴当学案。 |
| F3 | **High** | `02_codex_lane/MAIN_THINKING_LEDGER.csv` MT0008 (Q0023) "answer_sentence" 字段；`04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` 四块表 Q0023 行 与 §五.1 | Q0023 ledger 答案句写 "改进调研活动时，可从科学思维、逻辑规则、辩证思维、创新思维中选取两类方法，做到建议具体且知识匹配"。这是 meta 指令，不是卷面答案。学生若在考场上抄这个句子，等于交白卷。四块表里的版本 "改进调研要从真实问题出发，完善选项和样本，综合运用多种方法，并先广泛收集意见再聚焦核心问题" 也偏建议清单，未点对应思维方法名。`02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` 决策段说"细则锁科学/逻辑/辩证/创新任选两个"，但 ledger 与 draft 都没演示"任选两个角度"应该怎么具体落到一段考卷答案。 | 答案句必须给"任选两个角度"的两段示范，每段 ≥ 1 句知识 + ≥ 1 句材料：例如"角度 1（科学思维客观性 / 可检验性）：改进调研方案应当从真实问题出发，[材料举例]；角度 2（逻辑规则）：提高不完全归纳推理可靠程度，需扩大样本并寻找因果联系，[材料举例]"。两段都要带 Q-ID 注释，明确这是示范不是唯一解。Ledger 的 meta 句必须删除或下放到"答题策略"字段。 |
| F4 | High | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §四.1 Q0021；`02_codex_lane/MAIN_THINKING_LEDGER.csv` MT0007；`02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` Q0021 段 | Q0021 (2026海淀期末 Q20(2)) framework_node 写 "超前思维 / 调查研究 / 矛盾分析 / 推理和想象"。但"矛盾分析方法"在选必三课程里通常归属辩证思维，不是超前思维子方法；只有当材料明确"对未来情境的不确定 / 张力 / 风险预判"触发时，才能挂到超前思维的"矛盾分析-冷热权衡"路径。draft §四.1 "答题模板" 直接写"运用矛盾分析方法处理建设运营成本与需求之间的张力"，但没解释为什么这层归在超前思维帽下、而不是辩证思维。学生若按本条思路上考场，可能漏写"超前"语词、只写"运用矛盾分析处理张力"，结果被判到辩证思维一层。 | 在 Q0021 答题模板加入"超前帽下"的明示句：例如"运用超前思维的矛盾分析方法（不同于辩证思维的矛盾分析），在前瞻性规划中先识别成本与需求的潜在张力"。同时在 §四.1 增加"易混提醒：本题的矛盾分析不能写成单纯辩证思维矛盾分析，必须挂在超前思维方法链下"。如细则不支持这种归属，应回源核验并降为可选方法之一。 |
| F5 | High | `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` §三.5 Q0026 甲；`02_codex_lane/REASONING_FORM_LEDGER.csv` RF0022；`02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` Q0026 段 | Q0026 甲（2026西城一模 Q19(3) 甲）draft 给两个判定 "可以从三段论规则说它犯四概念错误，也可以从前提不真说'个人补偿诉求是正当个人利益，与公共利益不是非此即彼关系'"。两条路径并列、未指明哪条是细则主链。学生只能写一条；若写错另一条主链，结果可能只拿一半分。细则 `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77` 应能明确主链次链，draft 未引用。 | 回源细则；明确细则主链（四概念 vs 前提不真）；将另一条写成"可选第二角度，得分上限 X"。draft 同段写"答题时不要只贴'四概念'标签，要指出公共利益外延被窄化"——这条很好，但需要和主链关系挂上。 |
| F6 | High | `04_fusion/PROMOTION_LOG.md` Q0011 行 + `04_fusion/PROMOTION_GATE.md` Check 7 | `PROMOTION_LOG.md` 把 Q0011 标 `promote_to_v1_candidate_after_f1_fix`；`PROMOTION_GATE.md` Check 7 明确 "GPT Pro 和 Claude 外审必须是真实外审输出"。Q0011 至今未经过 V1 外审（本审才是 V1 外审第一稿）。把"Critical 已修+ blocker 闭合"等同于"通过 V1 门"，跳过了 Check 7。同样问题：Q0018-Q0026 标 `source_locked_hold_for_v1_review`，名字里带 V1，会被后续阶段误读为"已通过 V1 门"。 | (a) 在 `PROMOTION_LOG.md` 增加 Check 7 列，所有行明确写 `external_review_v1_not_yet_done`；(b) Q0011 状态改为 `f1_fix_done_pending_v1_external_review`；(c) `PROMOTION_GATE.md` 增加 "Check 7 不通过时，状态名不得含 `v1_candidate` 字样"；(d) `source_locked_hold_for_v1_review` 重命名为 `source_locked_hold_pending_v1_external_review`，避免歧义。 |
| F7 | High | `04_fusion/PROMOTION_GATE.md` Check 3 / Check 4 enforcement gap | Check 3 要求思维行 "材料动作 / 联想理由 / 答案句 / 易错边界" 四要素全填。Q0011 当前 V1 四块表 "易错边界" 只一句 "上限就是科学思维角度 2 分"，技术上"非空"，但内容是扣分口径不是教学失误清单，等同 V0 F2 老问题再次发生。Check 4 要求 "可检查式子 / 同类题对比"；Q0008/Q0020 在推理册章节正文里没有 `p->q; q; therefore p` 这一符号化形式，只在顶部索引表里出现。Gate 名义满足，实质失效。 | Gate 须升级为 "字段非空 + 教学内容合规" 双判：(a) 易错边界 ≥ 2 条具体学生写作失误（不是扣分总数）；(b) 答案句必须可剪贴上考卷，不能是 meta 指令；(c) 形式化必须落到章节正文，不只索引表。建立 `04_fusion/PROMOTION_QUALITY_CHECK.md` 列各行四 / 五块的实际质量评级，门控指向该文件。 |
| F8 | High | `04_fusion/BLOCKER_RECONCILIATION.md` BLK-003 / BLK-004 状态 `source_lock_closed_promotion_hold` | 这个状态名同时把"source-lock 已闭合"和"V1 promotion hold"两件事缠在一起，门控读起来歧义：到底算 closed 还是 open？且 hold 的 required_fix 是"V1 promotion 前补 A/B/C/D 选项原文 / 形式化 + 同类对照"——但 V1 draft 里 Q0008 (BLK-004) 章节并未补出 5 元素正文（只在顶部索引表有），Q0012 (BLK-003) 也只有选项原文（√），形式化和同类对照仍在顶部索引表层。也就是说，hold 条件实际未达成，但状态名"closed"已挂出。 | 拆为两个独立状态：`source_lock_evidence_closed`（事实层面 closed）+ `v1_promotion_held_pending_template_fill`（流程层面 hold）。required_fix 必须可逐项打钩，每项验证到具体行号；当所有项都打钩，再升级到 `promotion_unhold_pending_external_review`。 |
| F9 | High | `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` §一.2 Q0008 + Q0020 合并段；§六.1 Q0018 段；§七 Q0025 晏子段 | 推理册章节正文几处与顶部"V1 形式化索引"不一致：(a) §一.2 把 Q0008 / Q0020 合并到同一形式说明，只举 Q0008 例（岩松鼠 / 红嘴蓝鹊），Q0020（海淀期末电梯加装相关）的材料触发链 0 字符——学生看不到 Q0020 的具体材料动作；(b) §六.1 Q0018 正文 3 句，缺细则原文摘录，无同类题对比（明明顶部表有 Q0025）；(c) §七 Q0025 晏子段只 1 段判定，无答题模板、无 Q0018 横向对照（顶部表点了同类）。F2 的具体表现。 | (a) §一.2 Q0020 独立成子节，给材料动作、形式化、判定、易错；(b) §六.1 加 "细则原文摘录 `gpt_sources/3a11db4bade216d1_2026朝阳一模细则.md:40-43`"+ "同类题对比：Q0018 是识别题，Q0025 楚王是评析其可靠性"；(c) §七 Q0025 晏子加答题模板"先点类比推理、再写两类对象在 X 属性相似 → 推出 Y 属性相似、最后写论证效果"。 |
| F10 | Medium | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §六.1 Q0004 / §七 Q0017 "选项原文与逐项解释" 段 | 选项原文已完整粘贴（√），逐项解释也都到位（√）。剩下一个教学风险：Q0004 §六.1 D 选项 "类比推理与系统整合" 解释只说 "材料不是由相似性推出新结论的类比推理"——但"水脉-文脉-人脉"在字面上极像类比意象，学生很可能误判。建议加一句"水脉/文脉/人脉是平行隐喻，不构成'由两类对象在若干属性相似推出其他属性'的类比推理结构"作为对比。Q0017 §七 B 选项解释 "把数据打通和结算机制建设误挂成创新思维"——但材料里"打通数据壁垒"在 2026 新方案里也确有创新含义，应明示"创新思维需要发散、逆向、联想、超前等明确思维动作，本题没有"。 | Q0004 加"水脉/文脉/人脉是平行隐喻不是类比推理"对照句；Q0017 加"为什么'打通数据壁垒'不算创新思维"——必须举出哪些思维动作词缺失（发散 / 逆向 / 联想 / 超前 全部缺）。 |
| F11 | Medium | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` § 章节标题层级 | §一 科学思维 / §二 辩证思维 / §三 创新思维 / §四 超前思维 / §五 调研改进题 / §六 思维抽象与思维具体 / §七 选择题边界——半触发半分类。TASK_BRIEF 要求 "思维类型 -> 小方法 / 触发链 -> 对应考题"。§六、§七 已经是触发标题；§一-§四 仍是思维类型标题，下一层才到触发口诀。学生从材料反查思维方法的路径不直观。 | 章节内每个二级标题改为"触发动作 -> 思维方法"形式，例如 §一.1 改为 "见'蹲点观察 / 趋势预判 / 测试迭代' -> 科学思维三性"；§二.1 改为 "见'共建共享 / 渐进推进 / 扬弃旧偏差' -> 辩证思维五角度复合"。这样和推理册的"形式化 -> 形式名"对称。 |
| F12 | Medium | `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` §五.3 Q0026 乙（反对关系）与 §五.2 Q0016（矛盾关系） | 两题逻辑结构相邻，学生最易混。draft 在 §五.2 Q0016 末尾 "排雷" 写到 "矛盾命题必有一真一假"；§五.3 Q0026 乙 写到 "反对关系不能同真但可以同假"。两条规则正确，但章节里没有横向对照表（顶部 V1 索引表已有，但章节正文没有）。学生只读正文，可能仍把 "所有 X 是 P / 所有 X 不是 P" 当矛盾关系（实际是反对关系，矛盾关系是"所有 X 是 P / 有些 X 不是 P"）。 | 在 §五.3 Q0026 乙末尾增加 "反对 vs 矛盾对照表"：反对关系（全称肯定 vs 全称否定，可同假不可同真）/ 下反对关系（特称肯定 vs 特称否定，可同真不可同假）/ 矛盾关系（全称肯定 vs 特称否定 / 全称否定 vs 特称肯定，必一真一假）。三关系并列 + Q-ID。 |
| F13 | Medium | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` 全册；`04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` 全册 | 两本宝典都缺 "如何使用本宝典" 开场页。TASK_BRIEF §产物一/二 都说要"按思维类型 / 推理形式 -> 小方法 / 触发链 -> 考题"组织，期望读者按触发反查。但当前 draft 顶端只 4 行状态声明 + 1 行抽样说明。学生 / 阅卷老师拿到 markdown 第一眼看不到使用路径，仍会按 Q-ID 顺读，等同查找表。 | 每本宝典开头加 "使用说明"：① 从材料动作进入（举例：见"蹲点观察"想到科学思维客观性 → 翻 §一.1）；② 从知识点反查（举例：复习创新思维三新 → 翻 §三）；③ 选择题陷阱专章入口；④ 易混专题专章入口（如反对 vs 矛盾）；⑤ 索引表的位置和阅读法。 |
| F14 | Medium | `04_fusion/A_B_DIFF_SNAPSHOT.md` "External Review V0 Follow-up" 部分 | 末段写 "F11 has been addressed structurally: `PROMOTION_GATE.md`...now control V1 promotion."。"addressed structurally" 措辞太软，回避了"实际门控有没有阻断 V0 既有失效模式"。本审 F6/F7 显示门控未真正阻断（PROMOTION_LOG 已挂 V1 字样的状态名、Check 3 非空但未要求质量、Check 7 未列入逐行检查）。如果后续阶段读这段 follow-up，会以为"V1 门已生效"。 | 改写为 "F11 已完成结构搭建，但 V1 外审显示门控仍存在 6 项实际未生效条款（见 V1 F6/F7/F8），需在 V2 继续硬化"。  |
| F15 | Medium | `01_source_inventory/QUESTION_COVERAGE_MATRIX.csv` 与 `03_claudecode_lane/blockers.csv` 的覆盖盲区 | matrix 26 行，全为 2024-2026 部分套卷；BLK-002（2024朝阳二模 Q7）、BLK-005（2026海淀一模 Q17(1) 完整问卷）、BLK-006/007（2026顺义/朝阳一模 Q1-Q15 选择题）、BLK-008（2025 backlog）、BLK-009（2024 backlog）、BLK-010（北京高考 19(2)）全 open。`A_B_DIFF_SNAPSHOT.md` 写 "26 source-locked rows" 但没暴露 "estimated 60+ candidates"。PROGRESS 末行状态码 `CLAUDECODE_DONE_A_LINE_26_LOCKED_CLAUDE_V0_NOTPASS_F1_FIXED_GATE_ACTIVE` 也没写出覆盖率差距。 | 在 `QUESTION_COVERAGE_MATRIX.csv` 增加 `coverage_pressure` 列或单独建 `01_source_inventory/COVERAGE_GAP.csv` 列出"尚未 source-lock 的具体套卷-题号 + 估计数量"。状态码追加 "26/估计 60+，缺口 ≥ 56%"。 |
| F16 | Low | `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` §八 "当前推理册还需扩容的节点" | §八 现在只列 "选言推理"、"2024朝阳二模 Q7 仍是 B 线旧索引占位"两项。V0 F9 要求分两栏 "已被 B 线锁定待 A 线编入" / "两线都未发现"。当前 Q0018-Q0026 已编入，§八 内容已大幅释放，但 "选言判断遗漏" 与 "规范选言推理" 的区别没说明（Q0022 已涉及选言判断遗漏，§八 又说"尚未 source-lock 规范选言推理代表题"，初读会疑惑）。 | §八 改写为分栏：(a) "已有但形式不完整"列 Q0022 选言判断遗漏，标 "需补规范选言推理（相容选言肯定否定式 / 不相容选言肯定否定式）"；(b) "两线均未发现"列剩下的 2024朝阳二模 Q7 等。每项写 "如发现，预期 Q-ID 段"。 |
| F17 | Low | `06_claude_review/EXTERNAL_REVIEW_STATUS.md` "Current Check" 段 | "已准备 `10_packets/CLAUDE_REVIEW_PACKET_V1.md`，但尚未启动新的 Claude V1 外审" 与 PROGRESS "[x] 独立 Claude 外审 V0 已真实返回" + "[ ] V1 外审包尚未真实提交" 一致，但容易被读成 "V0 已结案、V1 等启动"。本审是 V1 外审，结果应在本文件落地后立即更新 STATUS 为 `done_not_pass_v1`。 | 本文件落盘后，在 `EXTERNAL_REVIEW_STATUS.md` 增加 V1 section：runner 路径、return code、本文件路径、关键发现摘要 ≤ 5 行。 |
| F18 | Low | `04_fusion/PROMOTION_LOG.md` 列名 | 当前列：row / gate status / notes 三列。无 check 1-7 的逐项打钩，读者无法快速判断某行卡在哪一项。 | 增加 7 列 `check1_source / check2_blocker / check3_thinking_template / check4_reasoning_template / check5_choice_options / check6_ab_provenance / check7_external_review`，每行逐项写 `pass` / `fail-原因`。 |

## Gate Audit

PROMOTION_GATE 7 项检查 vs V0 既有失效模式：

| Check | 设计意图 | V0 对应失效模式 | 实际生效程度 | 漏洞 |
|---|---|---|---|---|
| 1 source packet | A-formal 或合理非 formal | V0 未单独列 | 实质生效。26 行全 A-formal。 | 无重大漏洞。 |
| 2 blocker reconciliation | blocker 闭合或转 hold | V0 F6/F7（BLK-001/003/004 open+entry imported） | 部分生效。BLK-001 已 `closed_by_correction`（√）；BLK-003/004 用了 `source_lock_closed_promotion_hold` 复合状态名（V1 F8）。BLK-002/005-013 仍 open。 | 复合状态名歧义；hold required_fix 未逐项打钩。 |
| 3 thinking template | 4 块全填 | V0 F2 | 表层生效（顶部 4 块表已填）但本审 V1 F1/F2/F7 显示：Q0011 易错边界 1 句口径；Q0019/Q0023 章节正文未跟上；teaching bridge "为什么" 字段全册 0 条。 | "非空"等于"通过"——Gate 必须升级为质量评级。 |
| 4 reasoning template | 5 块全填 | V0 F4 | 表层生效（顶部形式化索引已填）但章节正文 Q0008/Q0020 合并段、Q0018 三句段、Q0025 晏子段都缺正文 5 块。 | 同上。Gate 必须要求"索引表 + 章节正文双层达标"。 |
| 5 choice options | A/B/C/D 原文 + 逐项解释 | V0 F3 | 实质生效。Q0004/Q0012/Q0015/Q0016/Q0017/Q0024 都有原文 + 逐项解释。 | 个别逐项解释教学性偏弱（V1 F10），但格式层面达标。 |
| 6 A/B provenance | B 行需 Codex A 回源 | V0 F5 | 实质生效。`02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` 已完成。 | 无重大漏洞。 |
| 7 external review | GPT Pro / Claude 必须真实外审 | V0 F11 通用 | **未生效。** `PROMOTION_LOG` 已挂 `promote_to_v1_candidate_after_f1_fix` 等含 V1 字样的状态名，V1 外审本审才是第一稿。 | Gate 名义存在但未阻断"未经过 V1 外审即标 V1 candidate"。F6 必修。 |

总结：门控 7 项中，3 项（Check 1/5/6）实质生效；2 项（Check 3/4）表层生效但质量未管控；1 项（Check 2）部分生效但状态名歧义；1 项（Check 7）未生效。V0 的核心失效模式（source-locked 行越级进 draft）名义堵上，但实际通过四块/五元素的"非空"满足以及"V1 candidate"状态名提前挂出，重新打开了同一个口子的薄壁版。

## Highest-Priority Rewrite List

按学生使用风险倒序，V1 -> V2 必须先做：

1. **Q0011 cross-ref + 易错边界重写**（V1 F1）。F1 修复的最后两块未落地。
2. **Q0023 答案句改成可剪贴的两段示范**（V1 F3）。当前 ledger meta 句直接交考卷=零分。
3. **章节正文 4 / 5 块化**（V1 F2/F9）。顶部索引表只是脚手架，body 须独立完整。
4. **Q0026 甲 主次链明示**（V1 F5）。回源细则确认四概念 vs 前提不真的主链。
5. **Q0021 超前 vs 辩证 矛盾分析归属说明**（V1 F4）。否则学生会写错思维帽子。
6. **PROMOTION_LOG 升级为逐 Check 打钩 + 状态名去 V1 化**（V1 F6/F18）。否则后续阶段误读"V1 已通过"。
7. **Gate 升级为质量评级，建 `PROMOTION_QUALITY_CHECK.md`**（V1 F7）。Check 3/4 必须 "非空 + 教学合规" 双判。
8. **BLK-003/004 拆分为 evidence_closed + promotion_held 两状态**（V1 F8）。
9. **反对 vs 矛盾对照表加入 §五**（V1 F12）。学生最易混点。
10. **两本宝典开"如何使用本宝典"页**（V1 F13）。否则仍是查找表。
11. **§一-§四 章节二级标题改触发动作 -> 思维方法形式**（V1 F11）。
12. **§六.1 Q0004 加"水脉/文脉/人脉是平行隐喻不是类比"对照句**（V1 F10）。
13. **回填 Q0008/Q0020/Q0018/Q0025 晏子段章节正文**（V1 F9）。
14. **`A_B_DIFF_SNAPSHOT.md` follow-up 段措辞改硬**（V1 F14）。
15. **PROGRESS 状态码加覆盖率差距**（V1 F15）。
16. **真实 V1 外审捕获本文件结果，启动 GPT Pro V1 外审**（V0 BLK-013 仍 open）。

## Coverage Pressure List

按需要释放压力倒序：

1. **选言推理规范代表题**：Q0022 锁的是"选言判断遗漏"，不等于规范选言推理（相容选言肯前否后 / 不相容选言肯前否后）。推理册 §八 自报缺口；本节是高考重点。需扫 2024-2026 各区 "如果A或B则X" 题型。
2. **2024 backlog（BLK-009）**：当前只 2024朝阳一模 Q6/Q20、2024海淀二模 Q17(1)、2024.11朝阳期中 Q18，4 题。2024 各区一模/二模/期末仍未逐套卷处理。
3. **2025 backlog（BLK-008）**：当前只 2025海淀二模 Q20、2025西城二模 Q16(2)、2025顺义一模 Q7，3 题。2025 一模/期末全集未扫。
4. **2026 选择题语料（BLK-006/007）**：2026顺义/朝阳一模 Q1-Q15 未逐题分类。当前选择题 ledger 只 6 行，远不足支撑"选择题陷阱"作为独立模块。
5. **北京高考 Q19(2) 青海防沙治沙（BLK-010）**：高考真题级别，含 24 年实战，本轮未单独建 suite。需新建北京高考 suite。
6. **2024朝阳二模 Q7（BLK-002）**：三段论小项不当扩大代表题，B 线已点但 A 线未 source-lock。
7. **2026海淀一模 Q17(1) 完整问卷（BLK-005）**：逻辑错误 source-locked，问卷选项尚未回源；当前只能讲规则识别，无法讲选项陷阱。
8. **复合题节点扩容**：Q0011 类型（题干说 A 思维 / 细则收 B+C+D 思维）应至少再扫到 2-3 个同型题，否则规则 vs 反例只 1 比 0。
9. **类比 + 不完全归纳对比题**：Q0025（楚王 + 晏子）是稀缺双推理同题。同型题（一段材料含两种推理）需横向扫描扩容。
10. **真实 GPT Pro V1 外审（BLK-013）**：仍未提交。所有 draft 不能跨过 `REVIEW_DRAFT_NOT_FINAL`。
11. **评标实录 / 讲评 PPT 三角证据**：当前只 Q0002 三重；Q0011 重写版 + Q0003 / Q0014 等应补讲评层（提升教学权威性）。

## Forbidden Final Claims

下列说法在任何 user-facing 产物（宝典 MD / DOCX / PDF / README / 进度小结 / 移交消息 / 用户对话）中**均不得书写、不得显示、不得暗示**：

- 不得写 "选必三《逻辑与思维》宝典 已完成 / 终稿 / 定稿 / V1 / 最终版"。
- 不得写 "已穷尽 2024-2026 三年北京选必三考题"、"全量覆盖"、"已覆盖所有选必三题"。
- 不得写 "已经过 Claude 外审 / 通过 Claude review / Claude PASS"。本审 V1 仍显式不写 PASS（V0 / V1 累计两轮 NOT_PASS）。
- 不得写 "已经过 GPT Pro 外审 / GPT Pro 已通过"（BLK-013：未提交）。
- 不得用 "思维宝典涵盖 X 种思维方法 / 推理宝典涵盖 Y 种推理形式" 来暗示完备性。
- 不得宣称 "Q0011 / 2024海淀二模 17(1) 已完成宝典级修复"（V1 F1：cross-ref 未补、易错边界为扣分口径）。
- 不得宣称 "PROMOTION_GATE 已生效阻断 V0 既有失效模式"（V1 F6/F7/F8：Check 3/4/7 实际未完全生效）。
- 不得宣称 "BLK-003 / BLK-004 已闭合"（V1 F8：状态为复合 `source_lock_closed_promotion_hold`，且 hold 条件未逐项打钩；BLK-002/005-013 仍 open）。
- 不得写 "可作为学生练习材料 / 可直接发学生 / 可印刷下发"（V1 F2/F3：章节正文未达 4/5 块，Q0023 答案句不可剪贴）。
- 不得写 "A/B 双线已对齐 / 双线闭合 / 双线一致"（虽然 Q0018-Q0026 已 A 回源，但章节正文模板未对齐）。
- 不得写 "已交付 / delivered / ready-to-ship / 入正稿"。
- 不得给区/年份/试卷-级完成率数字。当前 26/估计 60+ 仍小，公布数字会误导。
- 不得引用本审结果反过来说 "Claude 已确认 Q0001-Q0026 教学语言无问题"。本审深度 spot-check 了 Q0011 / Q0017 / Q0019 / Q0021 / Q0023 / Q0026 等点位，但未对每条逐字回源原始试题与细则。
- 不得把 `PROMOTION_LOG` 中含 `v1_candidate` / `v1_review` 字样的状态名解读为"已通过 V1 门"。Check 7（真实外审）本审是第一稿，仍 NOT_PASS。
- 不得宣称 "F2/F3/F4 V0 缺口已清"。F3 选择题选项原文已清（√），但 F2（四块全填正文）/ F4（形式化全填正文）仅顶部索引层达标，章节正文层仍缺。`PROGRESS.md` 已正确写 "阶段性清掉但仍需逐条课堂化润色"——任何精简表述不得丢掉 "阶段性 / 仍需润色" 两个限定。
- 不得在 PROGRESS.md 状态码中把 `EXTERNAL_REVIEW_V1_DONE_NOT_PASS` 简写为 "external review v1 done"——必须保留 NOT_PASS 后缀。

下一可达状态（建议命名）：`V1_EXTERNAL_REVIEWED_REQUIRES_BODY_REWRITE_AND_REAL_GPTPRO_BEFORE_V2`。

— Claude 外审 V1（独立 lane）· 完
