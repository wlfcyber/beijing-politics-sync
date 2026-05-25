# Claude External Review Result V3

Status: `EXTERNAL_REVIEW_DONE_NOT_PASS`

Reviewer lane: independent Claude external review V3, distinct from ClaudeCode B 线生产、Claude V0/V1/V2 外审。本文件是本审唯一权威产物。

Scope: 仅复审 Claude V2 NOT_PASS 之后落地的 post-V2 本地补丁，对照 V2 review 的 P0/P1 必须项。读入 `PROGRESS.md`、`06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V2.md`、`06_claude_review/EXTERNAL_REVIEW_STATUS.md`、`04_fusion/PROMOTION_QUALITY_CHECK.md`、`04_fusion/PROMOTION_LOG.md`、`01_source_inventory/COVERAGE_GAP.csv`、`04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`、`04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`、`02_codex_lane/MAIN_THINKING_LEDGER.csv`、`02_codex_lane/REASONING_FORM_LEDGER.csv`、`02_codex_lane/CHOICE_TRAP_LEDGER.csv`，并旁证 `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` 与 `03_claudecode_lane/suite_reports/2026西城一模.md`。

## Verdict

**NOT_READY_FOR_FINAL — POST_V2_PATCHES_LANDED_FOR_Q0026_Q0020_QUALITY_RATING_USAGE_ENTRY_AND_COVERAGE_GAP_PRIORITIES_BUT_PROVENANCE_AND_REAL_EXTERNAL_REVIEW_GAPS_REQUIRE_CLOSURE_BEFORE_V4.**

Post-V2 补丁在五个 V2 review 直接点名的位置都有可验证落地：

(a) Q0026 甲 V2 body §5 与 RF0022 已不再写主次链，改为 "细则没有把本题理由分成主链/次链，而是把四概念错误、前提不真、材料分析列为并列可用理由"，并给出 "前提不真 + 公共利益外延窄化造成四概念错误" 的合写卷面句、"若时间紧，至少写清个人补偿诉求与公共利益不是非此即彼" 的兜底句。这条路径在结构上比 V2 review 要求的 "硬指主链" 更尊重源事实——因为旁证文件 `B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` line 84-86 明示 rubric 73-77 是 "犯三段论四概念错误**或**前提不真"，"或" 字与 `03_claudecode_lane/suite_reports/2026西城一模.md` line 12 的 "三段论-四概念 (或前提不真)" 一致，原文不支持单一主链。

(b) Q0020 V2 body §1 已增加 "两个样本怎么落地" 段，第二自然段是 Q0020 专属的具体材料引述："只要是全民阅读设施管理单位，就应当考虑老年人阅读需求和特点，提供适老阅读内容和便利服务" + "某实体书店已经考虑老年人阅读需求、提供适老内容和便利服务" + "后件为真，不能倒推出该实体书店一定是全民阅读设施管理单位"。学生只读 §1 现在能看到 Q0020 海淀期末 Q20(1) 的真实材料动作。

(c) `PROMOTION_QUALITY_CHECK.md` Current Ratings 表已把全部 `partial-plus` 评级降回 `partial`，并在 notes 中明确 "V2 body sections exist and were partly accepted by Claude V2, but row-level promotion still awaits gap closure and GPT Pro"。Rating Rules 与 Current Ratings 自洽，未定义档已消除。Immediate Quality Gaps 段增加 "Q0026 甲, Q0020, Q0017, body usage entries, and cross-book/cross-section references were patched afterward and need re-review"。

(d) 两本 V2 body draft 头部 "如何使用本稿" 段已存在；思维册给三条入口路径（材料动作 / 知识点反查 / 选择题入口），推理册给三条入口路径（按形式找题 / 每形式至少读两个样本 / 翻译式子再写答句）。Q0011 cross-ref 在 §6 Q0001、§7 Q0002、§8 Q0003 末尾各加 "另见 §1 Q0011" 一句；Q0023 思维段末加 "推理形式和提高可靠性的写法要回看推理册 §2 Q0018/Q0025"，推理册 §2 末加 "调研改进题里要回看思维册 §3 Q0023"，跨册双向 cross-ref 闭合。Q0017 卷面答案句已改为 "材料给出的是系统化、数字化的资源整合动作，没有发散、逆向、联想、超前等明确创新思维动作；因此不能判为'体现创新思维'，正确判断应落在'整合医保与商保资源，形成一站式清分结算新机制'"——排除路径与正确答案双段并列，V2-F11 闭合。

(e) `COVERAGE_GAP.csv` 已增加 `priority` / `owner` / `milestone` 三列，10 项均填值；P0 两项（GAP008 规范选言推理代表题、GAP010 GPT Pro 外审）、P1 四项（GAP001 2024朝阳二模 Q7、GAP002 2026海淀一模 Q17(1) 完整问卷、GAP007 北京高考 Q19(2)、GAP009 复合题同型扩容）、P2 四项（GAP003/GAP004 2026 选择题语料、GAP005/GAP006 2024-2025 backlog）。next_action 列与 owner 列对齐，下一步工作可执行。

但本审仍判 NOT_PASS，原因有三类未释放硬伤：

1. **Q0026 "材料分析" 作第三条并列理由的源出处未对账。** V2 body §5 与 RF0022 写 "细则并列列出四概念错误、前提不真、材料分析三条可用理由"，但 `B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` line 86 的 Decision 只点 "三段论四概念错误或前提不真" 两条，`03_claudecode_lane/suite_reports/2026西城一模.md` line 12 也只写 "三段论-四概念 (或前提不真)" 两条；rubric 73-77 范围内是否真有 "材料分析" 作并列第三条，本文件读到的本仓证据**无法证实**。如果 "材料分析" 是教学编辑层加的兜底口径而不是细则原文并列项，那 V2 body 当前措辞会让学生以为答 "个人补偿诉求与公共利益不是非此即彼" 一句就能拿到细则承认的得分，而细则可能不收单纯材料分析。这是本审 P1。

2. **V2 body / RF0022 不直接引细则行号。** Q0018-Q0026 backcheck 文件已对每题列出 rubric 文件 + 行号（Q0026 是 `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77`），但这些行号没有进入 RF0022 ledger 的字段、也没有进入 V2 body §5 的正文（V2 body 只写 "西城一模细则没有把本题理由分成…"）。学生不需要看到文件路径，但 ledger 与正文之间需要可追源——目前评级 / 答句 / 同类题对比层都在 "信任 backcheck 已对" 的基础上，而 backcheck 与本次 V2 body 的并列理由数量本身不一致。这是本审 P1。

3. **Check 7 仍 fail：本审 Claude V3 NOT_PASS、GPT Pro 仍未提交。** `PROMOTION_LOG.md` 全部行 check7 列写 "fail: Claude V2 NOTPASS, GPT Pro pending"；`COVERAGE_GAP.csv` GAP010 P0 自述 "GPT Pro packets prepared but not submitted"。本文件写盘后 check7 应同步更新为 "fail: Claude V3 NOT_PASS, GPT Pro pending"。门控 Check 7 仍未通过；任何 "post-V2 补丁已闭环" 的判断不成立。

此外 V2 review 列出的若干 P2/P3 残项在本轮没有进展（V2-F7 PROMOTION_LOG row 合并、V2-F10 MAIN_THINKING_LEDGER 漏 Q0004/Q0017、V2-F13 PROMOTION_QUALITY_CHECK Current Ratings row 合并、V2-F15 Q0019 "和"/"或" 不一致），不构成发布门级阻断，但会影响外部读者追溯逐题进度，列在 P2 必须修正栏。覆盖压力没有变化：26 source-locked vs 估计 60+ 题；GAP008 规范选言推理样本仍空缺。

未达可发布门槛。下一步只能进入 V4：先把 Q0026 "材料分析" 第三条理由的细则出处对账（要么删掉、要么补回到 backcheck/suite_report、要么 quote 细则原文）、把 rubric 行号写进 V2 body 与 ledger、把 V2-F7/F10/F13/F15 残项收尾，然后真实提交 GPT Pro V4 外审，再开 Claude V4 外审。

## Delta Fixed（V2 → post-V2 patches）

| V2 # | V2 严重度 | post-V2 修复状态 | 修复证据 |
|---|---|---|---|
| V2-F1 (= V1 F5) Q0026 甲细则主次链 | Critical | **fixed via different path** | V2 body §5 与 RF0022 改为 "细则没有主次链，而是并列可用理由" + 合写卷面句；旁证 `B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` line 84-86 rubric 73-77 与 `03_claudecode_lane/suite_reports/2026西城一模.md` line 12 "或" 字一致。新路径比 V2 review 要求的 "硬指主链" 更尊重源事实。但 "材料分析" 第三条并列出处未对账（见 P1 V3-F1）。 |
| V2-F2 PROMOTION_QUALITY_CHECK `partial-plus` 未定义档 | High | **fully fixed** | Current Ratings 表全部降回 `partial`，Rating Rules 与表自洽；decision 列仍 hold；Immediate Quality Gaps 新增 "Q0026 甲, Q0020, Q0017, body usage entries, and cross-book/cross-section references were patched afterward and need re-review"。 |
| V2-F3 (= V1 F9(a)) Q0020 §1 独立子节 | High | **substantially fixed** | V2 body §1 已增 "两个样本怎么落地" 段，第二段是 Q0020 专属材料引述与无效推理说明。学生只读 §1 能看到 Q0020 真实材料动作。但 §1 卷面答案句仍是 Q0008+Q0020 共用结构句，无 Q0020 题面 specific 答句（次要瑕疵，见 P2 V3-F5）。 |
| V2-F4 §4 漏下反对关系 | High | **fully fixed** | V2 body §4 "可检查式子" 段现写 "矛盾关系：必有一真一假。反对关系：不能同真，可以同假。下反对关系：可以同真，不能同假"，三关系齐备。 |
| V2-F5 V2 body 开头加 "如何使用本宝典" 5 点路径 | High | **partial (3 paths instead of 5)** | 思维册头部 "如何使用本稿" 已给 3 条路径（材料动作 / 知识点反查 / 选择题入口）；推理册头部已给 3 条路径（按形式找题 / 每形式至少读两个样本 / 翻译式子再写答句）。但 V2 review 要求的 "复合题节点 / 易混专题 / 同类题对比阅读法" 三条未单列。当前 3 条覆盖了 5 条中最常用的入口；不构成 P0/P1 阻断。 |
| V2-F6 COVERAGE_GAP.csv priority / owner / milestone 列 | High | **fully fixed** | 三列齐备，10 项填值；P0 两项、P1 四项、P2 四项；owner 与 milestone 与 next_action 对齐。 |
| V2-F7 PROMOTION_LOG row 列逐题展开 | Medium | **not fixed** | PROMOTION_LOG.md 仍把 "Q0018-Q0026"（9 题）/"Q0004/Q0012/Q0015/Q0016/Q0017/Q0024"（6 题）/"Q0005-Q0010/Q0013/Q0020/Q0022/Q0025/Q0026"（9 题）/"Q0001/Q0002/Q0003/Q0014/Q0019/Q0021/Q0023/Q0004/Q0011/Q0017"（10 题）合并打一行 check 状态。Q0026 / Q0020 / Q0017 在 post-V2 都各有补丁但仍合并在大行里。本审 P2 V3-F2。 |
| V2-F8 Q0023 ↔ 推理册 §2 跨册 cross-ref | Medium | **fully fixed** | 思维册 §3 末加 "推理形式和提高可靠性的写法要回看推理册 §2 Q0018/Q0025"；推理册 §2 末加 "调研改进题里要回看思维册 §3 Q0023"。双向 cross-ref 闭合。 |
| V2-F9 V2 body §6/§7/§8 末段加 Q0011 复合题指针 | Medium | **fully fixed** | §6 Q0001 末："另见 §1 Q0011：Q0011 是'科学思维总帽下三模块复合'题，Q0001 的三性写法对应其中科学思维子段"；§7 Q0002 末："另见 §1 Q0011：Q0011 中'分阶段实施、任务明确'的辩证模块…"；§8 Q0003 末："另见 §1 Q0011：Q0011 的创新 3 分模块提醒学生…"。三处指针齐。 |
| V2-F10 MAIN_THINKING_LEDGER 增 Q0004/Q0017 主线 entry | Medium | **not fixed** | MAIN_THINKING_LEDGER.csv 仍只有 MT0001-MT0008 八行，无 Q0004 / Q0017 主线 entry；CHOICE_TRAP_LEDGER CT0001 (Q0004) / CT0005 (Q0017) 字段口径仍与 MAIN_THINKING_LEDGER 不同。本审 P2 V3-F3。 |
| V2-F11 Q0017 卷面答案句双段 | Medium | **fully fixed** | V2 body §5 卷面句："材料给出的是系统化、数字化的资源整合动作，没有发散、逆向、联想、超前等明确创新思维动作；因此不能判为'体现创新思维'，正确判断应落在'整合医保与商保资源，形成一站式清分结算新机制'。" 排除路径 + 正确答案并列。 |
| V2-F12 PROMOTION_LOG notes / PROMOTION_QUALITY_CHECK Immediate Quality Gaps 自我披露 V2 硬伤 | Medium | **substantially fixed** | PROMOTION_QUALITY_CHECK Immediate Quality Gaps 新段明示 "Q0026 甲, Q0020, Q0017, body usage entries, and cross-book/cross-section references were patched afterward and need re-review"；PROMOTION_LOG Q0018-Q0026 行 notes 写 "see Claude V2 findings and post-V2 patches"。仍可进一步细化（见 V3-F4）。 |
| V2-F13 PROMOTION_QUALITY_CHECK Current Ratings row 列展开 | Medium | **not fixed** | Current Ratings 表 row 列仍把 "Q0001/Q0002/Q0003/Q0011/Q0014/Q0019/Q0021/Q0023" 8 题、"Q0005/Q0006/Q0007/Q0008/Q0009/Q0010/Q0013/Q0020/Q0022" 9 题等合并成一行。Q0011（V1 F1 焦点）/ Q0023（V1 F3 焦点）/ Q0026（V1 F5/V2-F1 焦点）/ Q0020（V2-F3 焦点）未单独成行。本审 P2 V3-F4。 |
| V2-F14 PROGRESS 状态码追加 Q0026 / 评级口径 缺口 | Low | **fully fixed** | PROGRESS.md line 55 新状态码：`CLAUDE_V2_NOTPASS_POST_REVIEW_PATCHED_Q0026_Q0020_QUALITY_RATING_FIXED_GPTPRO_AND_COVERAGE_GAPS_PENDING`。包含本轮 P0 关键事项。 |
| V2-F15 Q0019 V2 body §10 "和" vs MT0006 "或" | Low | **not fixed** | V2 body §10 卷面句仍写 "可以运用联想思维中的迁移和想象…"；MAIN_THINKING_LEDGER MT0006 answer_sentence 仍写 "要运用迁移或想象…"。连接词不一。本审 P2 V3-F5。 |

小结：V2 共 15 项新 findings 中，post-V2 8 项 fully fixed（V2-F2/V2-F4/V2-F6/V2-F8/V2-F9/V2-F11/V2-F12/V2-F14）、2 项 substantially fixed（V2-F1 走改路径、V2-F3）、1 项 partial（V2-F5 3/5 路径）、4 项 not fixed（V2-F7/V2-F10/V2-F13/V2-F15）。其中 V2-F1 改路径属于本轮最大动作，但留下 "材料分析" 第三条出处未对账的 P1。

EXTERNAL_REVIEW_STATUS.md 已增 V2 段（line 48-65）含 post-V2 补丁清单，V1 review 残项 F17 一并落实；PROGRESS line 5-55 时间线连续可读。

## Remaining P0/P1 Findings

| # | 严重度 | 文件 / 位置 | 问题 | 必须修正 |
|---|---|---|---|---|
| V3-F1 | **P1** | `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` §5；`02_codex_lane/REASONING_FORM_LEDGER.csv` RF0022 | V2 body §5 与 RF0022 写 "细则并列列出四概念错误、前提不真、材料分析三条可用理由"，但旁证文件 `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` line 84-86 rubric `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77` 的 Decision 只列 "三段论四概念错误**或**前提不真" 两条；`03_claudecode_lane/suite_reports/2026西城一模.md` line 12 "三段论-四概念 (或前提不真)" 同样只两条。"材料分析" 作并列第三条的出处在本仓证据中**无法确认**。若细则原文未把 "材料分析" 列为独立得分路径，V2 body 的 "若时间紧，至少要写清'个人补偿诉求与公共利益不是非此即彼'这一材料分析" 兜底句会误导学生以为单写一句材料分析就能拿到细则承认的得分。 | (a) 直接打开 `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77` 原文，把 Q0026 甲允许的并列理由原句逐条抄入 RF0022 evidence 字段或 V2 body §5 注脚；(b) 如果原文确无 "材料分析" 第三条，把 V2 body §5 "细则并列列出…三条" 改为 "两条"（四概念错误 / 前提不真），并把 "若时间紧" 兜底句改为 "若两个角度都写不全，至少要把材料分析交代清楚——这一句可能算同义改写而不是独立第三条"；(c) 如果原文确有，把 backcheck Decision 与 suite_report 同步补到 "三条"，三处口径统一。 |
| V3-F2 | **P1** | `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` §5；`04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` §5；`02_codex_lane/REASONING_FORM_LEDGER.csv` 全表 evidence 列 | V2 body 正文与 ledger 都不直接引细则行号。Backcheck 文件已对每题列 rubric 路径（Q0026 是 `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77`），但这些行号没有进入 ledger evidence 字段或 V2 body 注脚。学生不需要看到文件路径，但 ledger 与正文之间需要可追源——目前评级 / 答句 / 同类题对比层都在 "信任 backcheck 已对" 的基础上，而 backcheck 与 V2 body 的并列理由数量本身不一致（V3-F1）。 | (a) REASONING_FORM_LEDGER 增 `rubric_source` 列，逐行填 backcheck 中已列的 rubric 路径 + 行号；(b) MAIN_THINKING_LEDGER 同样增 `rubric_source` 列；(c) V2 body 在每段 "样本：" 行后或末段加 "细则出处见 `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md` 对应小节" 注脚。 |
| V3-F3 | **P0** | `01_source_inventory/COVERAGE_GAP.csv` GAP010；`04_fusion/PROMOTION_LOG.md` check7 列 | GPT Pro 真实外审仍未提交（GAP010 P0 / BLK-013 仍 open）。PROMOTION_LOG check7 列仍全行写 "fail: Claude V2 NOTPASS, GPT Pro pending"；本文件写盘后应改为 "fail: Claude V3 NOT_PASS, GPT Pro pending"。三轮 Claude 外审累计三次 NOT_PASS（V0/V1/V2 + 本审 V3 四次），GPT Pro 仍未走。任何 "post-V2 补丁已闭环可发布" 判断都因 Check 7 fail 而不成立。 | (a) 真实提交 `10_packets/GPTPRO_REVIEW_PACKET_V4.md`（用户可见或显式接收），不要继续 prepared_not_submitted；(b) 收到 GPT Pro 结果后，先把结果保存为 `05_gptpro_review/...` 下的具体文件，再启动 Claude V4 复审；(c) PROMOTION_LOG check7 列同步更新 Claude V3 NOT_PASS 字样。 |
| V3-F4 | **P1** | `04_fusion/PROMOTION_LOG.md` notes 列；`04_fusion/PROMOTION_QUALITY_CHECK.md` Immediate Quality Gaps 段 | PROMOTION_LOG 多行 notes 只说 "see Claude V2 findings and post-V2 patches"，未点名当前未闭合的具体 P1（V3-F1 "材料分析" 出处未对账 / V3-F2 ledger 缺 rubric_source 列）。PROMOTION_QUALITY_CHECK Immediate Quality Gaps 段列了 post-V2 patches 待复审，但未点名 V3-F1 与 V3-F2。门控自身依赖外部 review 文件描述风险，会让下轮调度看不到本审具体缺口。 | (a) PROMOTION_LOG notes 列对应行补 "Q0026 材料分析 third reason provenance unverified (V3-F1)"、"ledger rubric_source column missing (V3-F2)"；(b) PROMOTION_QUALITY_CHECK Immediate Quality Gaps 段增 "Q0026 third parallel reason '材料分析' not confirmed against rubric lines 73-77; ledger lacks per-row rubric source citation column"；(c) decision 列保持 hold。 |
| V3-F5 | **P1** | `01_source_inventory/COVERAGE_GAP.csv` GAP008；`02_codex_lane/REASONING_FORM_LEDGER.csv` 全表 | GAP008 "规范选言推理代表题" 仍 status=open、P0；当前 ledger 中 Q0022 写的是 "选言判断遗漏" 与 "概念划分规则"，不等于规范的相容/不相容选言推理有效式或无效式样本。推理册 §10 "概念划分与选言判断" 段也只覆盖到选言判断遗漏一面，未覆盖 "或前 或后" / "肯定一个否定另一个" 等规范选言推理结构。学生学到本轮推理册仍读不到一个规范选言推理样本。 | (a) Codex A 在 2024-2026 北京套卷中扫规范选言推理题，锁住至少一个有效式样本与一个无效式样本；(b) 锁定后新增 RF0025 / RF0026 行并补 V2 body §10 子节；(c) 若搜遍三年仍无规范样本，GAP008 必须改写为 "本轮暂以选言判断遗漏代表，规范选言推理样本缺失，宝典中不得宣称'选言推理穷尽'"，并把宝典正文 §10 末加该免责段。 |

P0 = 直接阻断 V4 启动；P1 = V4 前必须修，不修则学生 / 后续阶段会被误导。

## Gate Audit

| 文件 | 当前状态 | 是否自洽 | 处置 |
|---|---|---|---|
| `PROMOTION_LOG.md` | check1-7 列齐；row 列仍合并（V2-F7 未修，列为 V3-F2-related P2）；状态名去 V1 化；check7 全 fail | 结构自洽；row 合并仍会让 Q0026/Q0020/Q0017 等单题进度不可见 | 拆 row + 同步 Claude V3 NOT_PASS（V3-F4） |
| `PROMOTION_QUALITY_CHECK.md` | Rating Rules 三档；Current Ratings 全 `partial`；`partial-plus` 已消除；decision 全 hold；Immediate Quality Gaps 段列 post-V2 待复审 | 评级口径自洽 ✓ | row 列仍合并多题（V2-F13 未修），但不破坏门控 |
| `BLOCKER_RECONCILIATION.md` | BLK-003/004 双状态保留；本审未深读 | 本审 scope 内未单独审；如未补 priority/milestone 仍是 V2-F6 同型残项 | 下轮单独读 |
| `COVERAGE_GAP.csv` | priority / owner / milestone 三列齐；10 项全填；status 全 open | 字段自洽 ✓；GAP008/GAP010 P0 是真正阻断项 | 推进 P0 落地（V3-F3/V3-F5） |
| `PROGRESS.md` | line 55 状态码含本轮 P0/P1 关键词；line 51-53 三个 open 项明列 | 自洽 ✓ | 本文件写盘后再追加 Claude V3 NOT_PASS 关键词 |
| `EXTERNAL_REVIEW_STATUS.md` | V0/V1/V2 三段齐；post-V2 补丁清单已落 | 自洽 ✓ | 本文件写盘后再加 V3 段 |

总结：post-V2 在门控自洽性上有实质修复（partial-plus 消除、COVERAGE_GAP 三列齐），但仍有两个未关的口子——Check 7（外审）与 row 列合并粒度。第一个是 P0（V3-F3），第二个是 P2（V3-F2-related）。门控合规度从 V2 的 "口径不自洽" 提升到 V3 的 "口径自洽但 Check 7 长期 fail"。

## Required Next Patches（按学生使用风险倒序）

1. **Q0026 "材料分析" 第三条理由出处对账**（V3-F1）。打开 `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77` 原文，确认是否真有三条并列；按确认结果同步 RF0022、V2 body §5、backcheck Decision、suite_report 四处口径。
2. **真实提交 GPT Pro V4 外审包**（V3-F3 = COVERAGE_GAP GAP010 P0 = BLK-013）。`10_packets/GPTPRO_REVIEW_PACKET_V4.md` 状态从 `prepared_not_submitted` 推进到 `submitted` 并保留可读结果文件。
3. **ledger 增 `rubric_source` 列**（V3-F2）。REASONING_FORM_LEDGER / MAIN_THINKING_LEDGER 逐行填 backcheck 中已有的 rubric 路径 + 行号；V2 body 每段加细则出处注脚。
4. **规范选言推理代表题 source-lock**（V3-F5 = GAP008 P0）。Codex A 扫 2024-2026 套卷锁有效式 + 无效式各一；或写明 "本轮规范选言推理样本缺失" 并在宝典正文 §10 末加免责段。
5. **PROMOTION_LOG row 列逐题展开 + notes 列点名 V3 P1**（V2-F7 + V3-F4）。至少把 Q0011 / Q0017 / Q0019 / Q0020 / Q0023 / Q0026 各题单独成行；notes 列写 "Q0026 第三条理由出处未对账 (V3-F1)"、"ledger rubric_source 列缺 (V3-F2)"。
6. **PROMOTION_QUALITY_CHECK Current Ratings row 列展开**（V2-F13 残项）。同样把 V1/V2 焦点题单行化；Immediate Quality Gaps 段补 V3-F1/V3-F2/V3-F3/V3-F5 四项点名。
7. **MAIN_THINKING_LEDGER 增补 Q0004 / Q0017 主线 entry**（V2-F10 残项）。新增 MT0009 Q0004 思维抽象与具体 / MT0010 Q0017 治理事实边界两行，与 V2 body §4/§5 对齐。
8. **Q0019 V2 body §10 "和" vs MT0006 "或" 统一**（V2-F15 残项）。回源 `gpt_sources/3a11db4bade216d1_2026朝阳一模细则.md:40-49` 确认细则是否要求两方法都落到方案中（"和"）还是允许任选其一（"或"），按细则改一处。
9. **Q0020 § 1 加 Q0020-specific 卷面应用句**（V3 次要补强）。在 "两个样本怎么落地" Q0020 段末加一句 "卷面应针对该书店写：该推理是充分条件假言推理，但仅由后件'已考虑老年人需求并提供适老服务'成立，无法倒推前件'该书店是全民阅读设施管理单位'，属于肯定后件式无效结构"。
10. **V2 body 头部 "如何使用本稿" 扩到 5 路径**（V2-F5 残项）。在现有 3 路径基础上加 "复合题节点（§1 Q0011 / §10 Q0019）" 与 "同类题对比阅读法（先读 pass 段，再读 partial 段对照）" 两条。
11. **EXTERNAL_REVIEW_STATUS 加 V3 段**（本文件写盘后调度方动作）。含 runner、result、return_code、verdict、summary，与 V0/V1/V2 段格式对齐。
12. **PROGRESS line 55 状态码追加 Claude V3**。建议：`CLAUDE_V3_NOTPASS_POST_REVIEW_PATCHES_VERIFIED_PARTIAL_Q0026_THIRD_REASON_SOURCE_UNCONFIRMED_GPTPRO_PENDING`。
13. **真实启动 Claude V4 外审**（仅在 #1-#3 与 #4 修完后才有资格）。本文件写盘前不要直接进入。

## Coverage Pressure（无显著变化，仅追加 V3 视角）

仍按 V2 同表对照：

1. **规范选言推理代表题**（V1 #1 / V2 #1 / GAP008 P0 / V3-F5）：本轮无进展。
2. **2024 backlog**（V1 #2 / V2 #2 / GAP006 P2）：无进展。
3. **2025 backlog**（V1 #3 / V2 #3 / GAP005 P2）：无进展。
4. **2026 选择题语料**（V1 #4 / V2 #4 / GAP003/GAP004 P2）：无进展。
5. **北京高考 Q19(2) 青海防沙治沙**（V1 #5 / V2 #5 / GAP007 P1）：无进展。
6. **2024朝阳二模 Q7**（V1 #6 / V2 #6 / GAP001 P1）：无进展。
7. **2026海淀一模 Q17(1) 完整问卷**（V1 #7 / V2 #7 / GAP002 P1）：无进展。
8. **复合题节点扩容**（V1 #8 / V2 #8 / GAP009 P1）：无进展，Q0011 仍是唯一例。
9. **类比 + 不完全归纳对比题**（V1 #9 / V2 #9）：仍只有 Q0025（楚王 + 晏子）。
10. **真实 GPT Pro 外审**（V1 #10 / V2 #10 / GAP010 P0 / V3-F3）：仍未提交。
11. **评标实录 / 讲评 PPT 三角证据**（V1 #11 / V2 #11）：仅 Q0002 三重。
12. **Q0026 "材料分析" 第三条理由出处**（本审 V3 新增）：未对账。

source-locked 总数 26 vs 估计 60+。

## Forbidden Final Claims

下列说法在任何 user-facing 产物（宝典 MD / DOCX / PDF / README / 进度小结 / 移交消息 / 用户对话）中**均不得书写、不得显示、不得暗示**：

- 不得写 "选必三《逻辑与思维》宝典 已完成 / 终稿 / 定稿 / V3 / 最终版"。
- 不得写 "已穷尽 2024-2026 三年北京选必三考题"、"全量覆盖"、"已覆盖所有选必三题"。
- 不得写 "已经过 Claude 外审 / 通过 Claude review / Claude PASS"。V0/V1/V2/V3 四轮累计四次 NOT_PASS。
- 不得写 "已经过 GPT Pro 外审 / GPT Pro 已通过 / GPT Pro 已认可"（GAP010 / BLK-013 仍 open；V3-F3 P0）。
- 不得用 "思维宝典涵盖 X 种思维方法 / 推理宝典涵盖 Y 种推理形式" 暗示完备性。
- 不得宣称 "Q0026 已完成宝典级修复"——V3-F1 显示 "材料分析" 第三条出处未对账。post-V2 改路径方向正确，但 "并列三条理由" 中第三条尚不可在本仓证据上证实。
- 不得宣称 "Q0026 主链已经回源"——post-V2 走的是 "细则原本就是并列、不存在主次链" 路径，不是 "回源后确认了主链"。两种描述互斥；任何说 "已确认主链" 的话都与 post-V2 补丁本身矛盾。
- 不得宣称 "Q0020 / Q0017 / Q0023 / Q0021 / Q0004 已完成宝典级修复"——V2 body 已改但门控 Check 7 仍未通过；Q0020 §1 应用句仍是结构共用句，无题面 specific 应用语。
- 不得宣称 "Q0011 三模块复合已扩容"——GAP009 P1 仍 open，Q0011 仍是唯一同型例。
- 不得宣称 "评级口径已与门控规则完全一致" —— `partial-plus` 已消除是真，但 PROMOTION_LOG 与 PROMOTION_QUALITY_CHECK 的 row 列均仍合并多题（V2-F7/V2-F13 未修），逐题进度仍不可追溯。可写的最强表述是 "评级档位已自洽，单题进度仍合并展示"。
- 不得宣称 "PROMOTION_GATE 已生效阻断 V0/V1/V2 既有失效模式"——门控 Check 7 仍 fail，本审仍 NOT_PASS。
- 不得宣称 "BLK-003 / BLK-004 已闭合"（拆为 evidence_closed + promotion_held 双状态，promotion 仍 held）；BLK-002/005-013 仍 open。
- 不得宣称 "覆盖缺口已收口" / "缺口已收尾" —— GAP008 / GAP010 P0 仍 open，本轮无源头进展。COVERAGE_GAP 增 priority 列只代表 "缺口已被排序可执行"，不代表 "缺口已被处理"。
- 不得宣称 "规范选言推理已覆盖" —— GAP008 P0 仍 open，Q0022 不等于规范选言推理。
- 不得写 "可作为学生练习材料 / 可直接发学生 / 可印刷下发 / 可作期末复习底稿"。V2 body 大部分段已达弱学生标准，但 §5 Q0026 仍有 V3-F1 出处疑点，整书未通过任何一轮外审。
- 不得写 "A/B 双线已对齐 / 双线闭合 / 双线一致"（V2-F10/V2-F15 残项显示 ledger 与 body 仍有口径错位）。
- 不得写 "已交付 / delivered / ready-to-ship / 入正稿 / 入终稿 / 入印"。
- 不得给区/年份/试卷-级完成率数字（仍 26 / 估计 60+）。
- 不得引用本审结果反过来说 "Claude V3 已确认 Q0001-Q0026 教学语言无问题"。本审深度核了 Q0020 / Q0026 / Q0017 / Q0019 / 使用入口 / 跨册 cross-ref / 评级口径 / 覆盖缺口列结构 / Check 7 状态，但未对每条逐字回源原始试题与细则；V3-F1 显示 Q0026 仍有出处疑点。
- 不得把 `PROMOTION_LOG` 中含 `pending_next_external_review` / `v2_body_coverage_added_hold_external_review_and_gaps` / `f1_crossref_fixed_pending_body_rewrite_and_next_review` / `source_locked_hold_pending_next_external_review` / `choice_options_embedded_hold_other_gates` 字样的状态名解读为 "已通过 V3 门"——Check 7 至今 fail。
- 不得宣称 "V2 全部 15 findings 已修复"。本审显示 8 项 fully fixed / 2 项 substantially fixed / 1 项 partial / 4 项 not fixed。
- 不得宣称 "V2 body draft 已等同于宝典正文"——它仍是 body rewrite 草稿，且 "如何使用本稿" 仅 3 路径（V2-F5 demanded 5）、Q0019 连接词仍与 ledger 不一（V2-F15）、Q0020 §1 仍无题面 specific 应用句。
- 不得在 PROGRESS.md 状态码中把 `EXTERNAL_REVIEW_V3_DONE_NOT_PASS` 简写为 "external review v3 done"——必须保留 NOT_PASS 后缀。
- 不得宣称 "post-V2 补丁已闭环" / "post-V2 patches closed" / "post-V2 已收口"——本审 V3 仍 NOT_PASS，且 V3-F1 / V3-F2 / V3-F3 / V3-F5 仍 P0/P1 open。
- 不得宣称 "Q0026 细则并列三条理由已经过 Claude 外审确认"——本审 V3-F1 P1 显式指 "三条" 第三条出处未对账，不可作终稿用。
- 不得用 "Claude 外审 V3 通过 / Claude V3 PASS / Claude V3 approved" 表述本文件——本文件结论是 `EXTERNAL_REVIEW_DONE_NOT_PASS`。

下一可达状态（建议命名）：`V3_EXTERNAL_REVIEWED_REQUIRES_Q0026_THIRD_REASON_SOURCE_CONFIRMATION_LEDGER_RUBRIC_COLUMN_AND_REAL_GPTPRO_BEFORE_V4`。

— Claude 外审 V3（独立 lane）· 完
