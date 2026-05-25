# Claude External Review Result V2

Status: `EXTERNAL_REVIEW_DONE_NOT_PASS`

Reviewer lane: independent Claude external review V2, distinct from ClaudeCode B 线生产、Claude V0 外审、Claude V1 外审。本文件是本审唯一权威产物。

Scope: PROGRESS / 06_claude_review/V1 / 04_fusion 全部十一件（含 V2 body draft、PROMOTION_QUALITY_CHECK、PROMOTION_LOG、BLOCKER_RECONCILIATION、REVIEW_DRAFT 两本）/ 01_source_inventory/COVERAGE_GAP.csv / 02_codex_lane 三张 ledger（MAIN_THINKING / REASONING_FORM / CHOICE_TRAP）。专项回查：V1 列出的 18 条 findings 哪些已 V2 修复、V2 新建的 trigger-organized body 是否真正达到弱学生触发链标准、PROMOTION_QUALITY_CHECK 评级口径是否自洽、Q0026 甲主链是否回源。

## Verdict

**NOT_READY_FOR_FINAL — V2_BODY_EXPANDED_PARTIALLY_REPAIRED_REQUIRES_RUBRIC_REVERIFICATION_AND_REAL_EXTERNAL_REVIEW_BEFORE_V3.**

V2 在六个结构动作上确实推进了：(a) `THINKING_BAODIAN_V2_BODY_DRAFT.md` 与 `REASONING_BAODIAN_V2_BODY_DRAFT.md` 两份正文草稿建立，思维 10 段 / 推理 11 段全部按 V1 F11 要求的 "见 'XX' -> 思维方法 / 推理形式" 触发链标题组织，每段含 5 块（材料动作 / 为什么能想到 / 卷面答案句 / 易错边界 / 同类题对比），V1 F2/F9 在 V2 body 这一层得到 prose 级覆盖；(b) `THINKING_BAODIAN_REVIEW_DRAFT.md` §二.3 与 §三.2 新增"复合题指针"段落明确指向 §一.2 Q0011，V1 F1(a) 已落实；(c) Q0011 易错边界由 V1 的扣分口径改写为 4 条学生写作失误清单（V1 F1(b) 落实）；(d) Q0023 卷面答案句改写为 "示范一 / 示范二" 可剪贴段落（V1 F3 落实）；(e) Q0021 在 V2 body §2 与 REVIEW_DRAFT §四.1 均明确 "运用超前思维的矛盾分析方法"（V1 F4 落实）；(f) PROMOTION_LOG 增加 check 1-7 七列、状态名去除 `v1_candidate` 字样并改为 `pending_next_external_review`（V1 F6/F18 落实），新建 `PROMOTION_QUALITY_CHECK.md`（V1 F7 结构落实），`BLOCKER_RECONCILIATION.md` 将 BLK-003/004 拆为 `source_lock_evidence_closed` + `v1_promotion_held_pending_body_quality` 两层状态（V1 F8 落实），新建 `01_source_inventory/COVERAGE_GAP.csv` 列 10 项缺口（V1 F15 落实），REVIEW_DRAFT §五.3 加入 反对/下反对/矛盾三关系对照表（V1 F12 落实）。

但 V2 仍有四类未释放的硬伤：

1. **V1 F5 未真正修复。** Q0026 甲（西城一模 Q19(3) 甲）V1 F5 明确要求"回源细则，明确细则主链（四概念 vs 前提不真），另一条写成可选第二角度"。V2 body draft `REASONING_BAODIAN_V2_BODY_DRAFT.md` §5 卷面答案句仍写"甲把正当个人补偿诉求与公共利益处理成非此即彼，前提不真，并且在三段论中窄化了'公共利益'的外延，犯四概念错误"——两条理由并列、未指明哪条是细则主链。`02_codex_lane/REASONING_FORM_LEDGER.csv` RF0022 字段 `validity_or_fallacy` 写 "错误：四概念或前提不真"，依旧是 "或" 并列。V2 既没有引用 `gpt_sources/.../2026西城一模细则.md` 具体行号，也没有把另一条标 "可选第二角度，得分上限 X"。学生答错主链仍只能拿一半分。

2. **V2 body §1 Q0020 材料动作仍缺失。** V1 F9(a) 要求 "§一.2 Q0020 独立成子节，给材料动作、形式化、判定、易错"。V2 reasoning body §1 把 Q0008（岩松鼠 / 红嘴蓝鹊）和 Q0020（海淀期末电梯加装相关）合并到 "充分条件肯定后件错误" 同形式说明下，举的具体材料只有 Q0008 一组；Q0020 在 §1 通段中 0 字符具体材料引述（只在样本行出现 "2026海淀期末 Q20(1)" 标签）。学生只读 §1 仍看不到 Q0020 的具体材料动作。

3. **PROMOTION_QUALITY_CHECK 自创未定义评级 `partial-plus`。** 该文件 §"Rating Rules" 只定义三档：`pass` / `partial` / `fail`。但 §"Current Ratings" 表四行的 thinking quality / reasoning quality 列全部写 `partial-plus`，且 notes 字段统一写 "pending external review"。这等于在门控文件里凭空多出一档，把"V2 body 已写但未审"的实情包装为优于 `partial` 的状态。门控规则与门控评级互不自洽——本质是 V1 F7 "非空 + 教学合规双判" 的同一漏洞换皮。

4. **真实外审仍未进行。** `COVERAGE_GAP.csv` GAP010 自述 "GPT Pro packet V1 prepared but not submitted"；PROMOTION_LOG check7 列每行写 "fail: Claude V1 NOT_PASS, GPT Pro pending"；本审 V2 才是 Claude 外审第二轮，结果仍 NOT_PASS。门控 Check 7 仍未通过。所有把 V2 body 已写视为 "可放行" 的判断都不成立。

此外，覆盖压力没有变化：26 条 source-locked vs 估计 60+ 题；BLK-002/005/006/007/008/009/010 全 open；选言推理规范代表题、北京高考 19(2) 仍无 source-lock；Q0011 类复合题节点仅 1 例，无同型扩容。

未达可发布门槛。下一步只能进入 V3：先回源细则修 Q0026 甲主链、拆 Q0020 独立子节、统一 PROMOTION_QUALITY_CHECK 评级口径、真实提交 GPT Pro 外审，然后才有资格再开 Claude V3 外审。

## Fixed Items（V1 → V2）

| V1 # | V1 严重度 | V2 修复状态 | 修复证据 |
|---|---|---|---|
| F1(a) Q0011 cross-ref §二/§三 | Critical | **fully fixed** | `THINKING_BAODIAN_REVIEW_DRAFT.md` §二.3 "复合题指针：科学总帽下的辩证模块"（line 117-121）+ §三.2 "复合题指针：科学总帽下的创新模块"（line 141-145）均明示 "完整分析见 §一.2"。另在 §"如何使用本稿"（line 11）补 "复习科学思维客观性时，同时看 Q0001 和 Q0011；复习创新思维三新时…还要看 Q0011 的 3 分创新模块；复习辩证整体性时，也要回看 Q0011 的 2 分辩证模块"。 |
| F1(b) Q0011 易错边界写作失误清单 | Critical | **fully fixed** | `THINKING_BAODIAN_V2_BODY_DRAFT.md` §1 易错边界 4 条 + `THINKING_BAODIAN_REVIEW_DRAFT.md` §一.2 ④ 四条具体错误情景。已是学生写作失误清单，不再是扣分口径。 |
| F2 章节正文 4 块化 | High | **partial-plus**（V2 body 全段 5 块；REVIEW_DRAFT 仍多为 2 段式） | V2 body draft 思维 10 段 / 推理 11 段每段含 材料动作 / 为什么能想到 / 卷面答案句 / 易错边界 / 同类题对比，含 "为什么" 教学桥段命中 18 处教学性问句。但 REVIEW_DRAFT 除 Q0011 以外章节正文仍是 触发口诀 + 答题模板 2 段式（grep "为什么" 在 REVIEW_DRAFT 思维部分只命中 4 处，3 处是 meta 描述）。 |
| F3 Q0023 答案句可剪贴 | High | **fully fixed** | `THINKING_BAODIAN_V2_BODY_DRAFT.md` §3 给 "示范一 / 示范二" 两段，每段先写知识、再贴材料，可直接搬上考卷。MT0008 ledger answer_sentence 字段也改成可剪贴示例。 |
| F4 Q0021 超前 vs 辩证 矛盾分析归属 | High | **fully fixed** | `THINKING_BAODIAN_V2_BODY_DRAFT.md` §2 "运用超前思维中的矛盾分析方法，前瞻性识别建设运营成本与居民需求之间的潜在张力"；`THINKING_BAODIAN_REVIEW_DRAFT.md` §四.1 同样明示 "超前思维的矛盾分析方法（不同于辩证思维的矛盾分析）"。 |
| F5 Q0026 甲主次链 | High | **not fixed** | V2 body §5 + RF0022 ledger 仍把 四概念 与 前提不真 并列。未引细则行号、未指主链。 |
| F6 PROMOTION_LOG 状态名去 V1 化 | High | **fully fixed** | `PROMOTION_LOG.md` 状态名改为 `f1_crossref_fixed_pending_body_rewrite_and_next_review` / `source_locked_hold_pending_next_external_review` / `v2_body_coverage_added_hold_external_review_and_gaps`，不再含 `v1_candidate`。 |
| F7 门控升级为质量评级 | High | **partial**（建了文件，但评级口径不自洽） | `PROMOTION_QUALITY_CHECK.md` 建立 + Rating Rules 定义 pass/partial/fail；但 Current Ratings 全用未定义档 `partial-plus`。本审 P0-3。 |
| F8 BLK-003/004 拆状态 | High | **fully fixed** | `BLOCKER_RECONCILIATION.md` 表头 "decision" 列写 `source_lock_evidence_closed` + `v1_promotion_held_pending_body_quality` 双状态，逐项可独立打钩。 |
| F9 Q0008/Q0020/Q0018/Q0025 章节正文 | High | **partial**（Q0008/Q0018/Q0025 已扩；Q0020 仍合并） | V2 reasoning body §1（Q0008+Q0020）/ §2（Q0018+Q0025 楚王）/ §3（Q0025 晏子）章节正文均扩到 5 块。但 Q0020 在 §1 无独立材料动作子节，与 Q0008 共用形式描述，违反 V1 F9(a) "Q0020 独立成子节"。本审 P1-2。 |
| F10 Q0004 平行隐喻 / Q0017 创新动作词 | Medium | **fully fixed** | `THINKING_BAODIAN_V2_BODY_DRAFT.md` §4 "水脉、文脉、人脉是平行隐喻和理念展开，不是由两类对象相似推出其他属性相似的类比推理"；§5 "创新思维需要看到发散、聚合、逆向、联想、超前等明确思维动作，本题没有"。 |
| F11 触发动作 -> 方法 形式标题 | Medium | **fully fixed**（在 V2 body draft 中） | V2 body draft 思维 10 段标题全为 "见 'XX' -> XX 思维方法 / 推理形式"；REVIEW_DRAFT 章节标题仍为思维类型层级，未改。 |
| F12 反对/下反对/矛盾三关系表 | Medium | **fully fixed**（在 REVIEW_DRAFT 中） | `REASONING_BAODIAN_REVIEW_DRAFT.md` §五.3 line 284-292 给三关系对照表，含 Q-ID 标注；V2 body §4 只写两关系，未含下反对。本审 P2 提醒 V2 body 也应补全。 |
| F13 "如何使用本宝典" 入口 | Medium | **partial**（REVIEW_DRAFT 有；V2 body 无） | `THINKING_BAODIAN_REVIEW_DRAFT.md` §"如何使用本稿"（line 7-13）含 3 段使用路径；`REASONING_BAODIAN_REVIEW_DRAFT.md` 同样含使用入口。但 V2 body draft 开头仅 1 段状态声明，无使用路径。本审 P2-1。 |
| F14 A_B_DIFF_SNAPSHOT 措辞 | Medium | **not verified**（未在本审 scope 内重读） | 本审未单独读 A_B_DIFF_SNAPSHOT；如未改硬，下轮再评。 |
| F15 覆盖率差距台账 | Medium | **fully fixed** | `01_source_inventory/COVERAGE_GAP.csv` 已建，含 GAP001-010 十项，覆盖 BLK-002/005/006/007/008/009/010 + 选言推理 + 复合题扩容 + GPT Pro 外审。 |
| F16 §八 分两栏 | Low | **not verified** | 本审未深读 REVIEW_DRAFT §八；如未改，下轮列。 |
| F17 EXTERNAL_REVIEW_STATUS V1 段 | Low | **not verified** | 本审未读该文件；写盘后请由调度方在 STATUS 中补 V2 段。 |
| F18 PROMOTION_LOG check 1-7 列 | Low | **fully fixed** | 七列齐备，每行逐项写状态。 |

小结：18 项 V1 findings 中，10 项 fully fixed（F1(a)/F1(b)/F3/F4/F6/F8/F10/F11/F15/F18）、3 项 partial（F2/F9/F13）、2 项 partial 含口径漏洞（F7/F12 仅 REVIEW_DRAFT 或 V2 body 一侧达标）、1 项 not fixed（F5）、3 项 not verified（F14/F16/F17）。F5 仍 High，且是学生答题直接失分点，列为 P0。

## Findings Table（V2 新发现）

| # | 严重度 | 文件 / 位置 | 问题 | 必须修正 |
|---|---|---|---|---|
| V2-F1 | **Critical**（继承 V1 F5 未修复） | `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` §5；`04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` 相应段（如有）；`02_codex_lane/REASONING_FORM_LEDGER.csv` RF0022 | Q0026 甲（西城一模 Q19(3) 甲）卷面答案句仍把 "前提不真" 和 "犯四概念错误" 并列写出，未指明哪条是细则主链。学生若只写一条，可能不是主链，最终只拿一半分。V1 F5 明确要求 "回源细则；明确细则主链；将另一条写成可选第二角度，得分上限 X"——V2 未做。RF0022 字段也仍写 "错误：四概念或前提不真"，"或" 字未消除。 | (a) 回源 `gpt_sources/22206a780a1503a6_2026西城一模细则.md:73-77`（或实际行号），引用原文判定主链；(b) V2 body §5 卷面答案句改为 "甲观点错误。细则主链：前提不真，因为正当个人补偿诉求可以是合法个人利益，与公共利益不构成非此即彼；可选第二角度：在三段论中窄化'公共利益'外延，构成四概念错误（得分上限 X 分）"——主链与可选两层明确分开；(c) RF0022 字段改为 "主链：前提不真；可选：四概念"（或反之，按细则）。 |
| V2-F2 | **High** | `04_fusion/PROMOTION_QUALITY_CHECK.md` Rating Rules vs Current Ratings | Rating Rules 只定义 `pass` / `partial` / `fail` 三档，Current Ratings 全用未定义档 `partial-plus`。本质是把 "V2 body 已写但仍未通过外审" 的状态包装成优于 `partial` 的隐性 4 档。这与 V1 F7 "非空等于通过" 是同源漏洞——评级口径自身不自洽。 | (a) Rating Rules 中明确加 `partial-plus` 档定义（例如："body sections written and source-supported, awaiting external review pass"），或 (b) 直接把 Current Ratings 中所有 `partial-plus` 降回 `partial`，理由 "external review still fails"；(c) decision 列保持 `hold`，不允许出现任何 `release` 状态名直到 check 7 实际通过。 |
| V2-F3 | High | `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` §1 Q0008 与 Q0020 合并段 | 同形式归组的 Q0020 在 §1 0 字符具体材料引述。V1 F9(a) 明确要求 "Q0020 独立成子节，给材料动作、形式化、判定、易错"。当前结构是 Q0008 主例 + Q0020 标签贴出。学生只读 §1 仍看不到 Q0020 海淀期末 Q20(1) 的具体材料动作。 | §1 在共用形式描述之后增加两个独立子段：(a) Q0008 子段：保留岩松鼠/红嘴蓝鹊；(b) Q0020 子段：补海淀期末 Q20(1) 的具体材料动作（"如果 A 则 B；已知 B，结论 A" 三句改写为 Q0020 实际材料文字），并独立给出该题卷面答案句。 |
| V2-F4 | High | `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` §4 与 §5；`02_codex_lane/REASONING_FORM_LEDGER.csv` RF0022/RF0023 | §4（Q0016 + Q0026 乙）"可检查式子" 段只写 "矛盾关系：必有一真一假。反对关系：不能同真，可以同假。" 漏 "下反对关系：可以同真，不能同假"。REVIEW_DRAFT §五.3 有三关系完整对照表，V2 body 应同样对齐——不然 V2 body 独立使用时学生仍可能把 "有些 S 是 P / 有些 S 不是 P" 当矛盾关系。 | V2 body §4 "可检查式子" 段补 "下反对关系：有些 S 是 P / 有些 S 不是 P，可以同真，不能同假"；并复用 REVIEW_DRAFT §五.3 的 Q-ID 标注表（反对 Q0026 乙 / 下反对 当前未锁代表题 / 矛盾 Q0016）。 |
| V2-F5 | High | `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` 与 `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` 开头 | 两本 V2 body draft 开头各 1 段状态声明（"本稿把当前 source-locked 的 XX 条目从索引层推进到正文层…"），无 "如何使用本宝典" 5 点路径（从材料动作进入 / 从知识点反查 / 选择题陷阱入口 / 易混专题入口 / 索引表位置）。REVIEW_DRAFT 已加 V1 F13 要求的使用入口；V2 body 若被视为最终 body 来源，使用入口必须同样存在。 | V2 body draft 开头加 "如何使用本宝典" 段：① 从材料动作进入（举例：见 "蹲点观察" 想到科学思维客观性 → 翻 §6 Q0001）；② 从知识点反查（举例：复习创新思维三新 → 翻 §1 Q0011 + §8 Q0003）；③ 复合题节点（§1 Q0011 / §10 Q0019）；④ 易混专题（§4 矛盾 vs 反对 / §5 三段论与前提不真）；⑤ 同类题对比阅读法。 |
| V2-F6 | High | `01_source_inventory/COVERAGE_GAP.csv` GAP001-010 与 `BLOCKER_RECONCILIATION.md` Still Open 块 | COVERAGE_GAP.csv 已列 10 项，但所有 status 均为 `open`，next_action 仅写 "Open paper / Scan suite-by-suite / Submit GPT Pro"，未给优先级与里程碑。BLOCKER_RECONCILIATION Still Open 8 项也无优先级。学生 / 后续阶段会以为 "缺口已记账" 等于 "缺口在收尾"，但实际无可执行节奏。 | (a) COVERAGE_GAP.csv 增加 priority 列（P0/P1/P2）：选言推理规范代表题 P0；GPT Pro V1 外审 P0；2026 海淀一模 Q17(1) 完整问卷 P1；2024朝阳二模 Q7 P1；2025/2024 backlog P2；北京高考 19(2) P1；(b) 每行加 owner 列与 milestone 列。 |
| V2-F7 | Medium | `04_fusion/PROMOTION_LOG.md` row 列 "Q0018-Q0026" / "Q0005-Q0010/Q0013/Q0020/Q0022/Q0025/Q0026" 等 | row 列用范围/集合表达，丢失逐题状态。例如 "Q0005-Q0010/Q0013/Q0020/Q0022/Q0025/Q0026" 共 9 个题号合并打一个 gate status；但事实是其中 Q0026 甲（V2-F1 P0）与其他 Q0005 类有效充分条件式题情况完全不同。合并表使 check3/4/5 列只能写 "partial-plus" 笼统态，掩盖逐题问题。 | row 列按逐题展开；每题独立一行；check3/4/5/6/7 列各题独立打分。Q0026 甲 / 乙 / 丙三小题应各占一行（如果 ledger 已分行）。 |
| V2-F8 | Medium | `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` §3 Q0023 与 `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md` §2 Q0018/Q0025 之间无跨册 cross-ref | Q0023 思维段 "示范二" 提 "不完全归纳推理"，但没有指 "见推理册 §2 Q0018 识别题 / §2 Q0025 楚王评析题"。学生若在思维册写 "不完全归纳" 但不知道推理册有规范判定模板，会写不到 "扩大样本、寻找因果联系" 等加分动作。两本宝典之间需要 explicit cross-ref。 | Q0023 思维段 "示范二" 末加 "→ 不完全归纳推理的判定与提高可靠性写法，详见推理册 §2 Q0018/Q0025"。反过来推理册 §2 末段加 "→ 不完全归纳推理用于调研改进题的两段示范，见思维册 §3 Q0023"。 |
| V2-F9 | Medium | `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` §6/§7/§8/§9 + REVIEW_DRAFT §二/§三/§四 | V2 body 思维段 §6（Q0001 科学三性）/ §7（Q0002 辩证）/ §8（Q0003 创新）/ §9（Q0014 辩证）末尾均未补 "复合题指针" 提示 "本题与 Q0011 三模块复合的关系"——REVIEW_DRAFT §二.3/§三.2 已加该指针，V2 body 未对齐。学生若 V2 body 独立使用，看不到 Q0011 复合题入口。 | V2 body §6 末加 "另见 §1 Q0011：'科学思维总帽下三模块复合' 题型，本题三性是其中科学思维 2 分子段的扩展"；§7 末加 "另见 §1 Q0011 辩证思维 2 分模块"；§8 末加 "另见 §1 Q0011 创新思维 3 分模块"。 |
| V2-F10 | Medium | `02_codex_lane/MAIN_THINKING_LEDGER.csv` 与 V2 body draft 之间 | V2 body 思维段还覆盖 Q0004（思维抽象与具体）与 Q0017（治理事实边界）两个原本归 `CHOICE_TRAP_LEDGER.csv` 的题号；但 MAIN_THINKING_LEDGER 只有 MT0001-MT0008 八行，没有对应 Q0004/Q0017 entry。CHOICE_TRAP_LEDGER 有 CT0001/CT0005 但字段口径（trap_type / wrong_option_traps）与 MAIN_THINKING_LEDGER（trigger_logic / answer_sentence）不同。V2 body 把它们当思维主线写时，缺主线 ledger 字段（material_action / trigger_logic / answer_sentence）的对账。 | (a) MAIN_THINKING_LEDGER 增加 MT0009 Q0004 思维抽象与具体 / MT0010 Q0017 治理事实边界两行，与 V2 body §4/§5 对齐；或 (b) PROMOTION_LOG 说明 "Q0004/Q0017 主线评估在 CHOICE_TRAP_LEDGER + V2 body draft 联合层面"，并标注 evidence_level。 |
| V2-F11 | Medium | `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` §5 Q0017 卷面答案句 | 卷面答案句写 "该中心运用系统化、数字化的模式整合基本医保和商业保险资源，形成一站式清分结算新机制。" 是正确选项 D 的解释口径，但作为选择题题型答案是用作 "排除创新思维" 的反例不是主答案语。学生需要的是 "怎样判断不写创新思维" 的判断口径，而不是再抄一遍 D 选项解释。 | 卷面答案句改为 "材料给出系统化、数字化的资源整合动作，没有发散 / 逆向 / 联想 / 超前等明确的创新思维动作；因此正确判断不是'体现创新思维'，而是'整合医保与商保资源形成一站式新机制（D）'。" 即把 "为什么不是创新思维" 与 "正确选项是什么" 并列写出。 |
| V2-F12 | Medium | `04_fusion/PROMOTION_LOG.md` notes 列 与 `04_fusion/PROMOTION_QUALITY_CHECK.md` Immediate Quality Gaps 段 | PROMOTION_LOG 多行 notes 写 "B-line high-confidence additions are source-locked but not released"；PROMOTION_QUALITY_CHECK Immediate Quality Gaps 只 3 行。两文件对 "V2 body 写完但 Q0026 甲主链未解 / Q0020 子节未独立 / 评级口径不自洽" 这些 V2 新硬伤无任何提及。门控自身依赖外部文件描述风险，而不是自我披露。 | (a) PROMOTION_QUALITY_CHECK Immediate Quality Gaps 段补：①Q0026 甲细则主链未回源；②Q0020 在 §1 缺独立子节；③`partial-plus` 评级未在 Rating Rules 中定义；(b) PROMOTION_LOG notes 列对应行也加 "see V2 review F1/F2/F3"。 |
| V2-F13 | Medium | `04_fusion/PROMOTION_QUALITY_CHECK.md` Current Ratings 表 row 列 | row 列直接把 "Q0001/Q0002/Q0003/Q0011/Q0014/Q0019/Q0021/Q0023" 等八条合并成一行，给统一 partial-plus 评级；但 Q0011 是复合题（V1 F1 焦点），Q0019 是联想思维（V1 F9 之外的稳态题），Q0023 是调研改进综合题（V1 F3 焦点）。把它们绑在一行使外部读者无法追溯单题修复进度。 | row 列按逐题展开；至少把 V1 findings 直接点名的题号（Q0011/Q0019/Q0021/Q0023）单独成行；其他可暂时合并但需说明依据。 |
| V2-F14 | Low | `PROGRESS.md` line 52 | 状态码 `CLAUDE_V1_NOTPASS_A_LINE_26_LOCKED_V2_BODY_EXPANDED_EXTERNAL_REVIEW_AND_COVERAGE_GAPS_PENDING` 保留 NOT_PASS 与 PENDING，方向正确；但未含 V2-F1 P0 (Q0026 甲细则主链)，下一轮易被误读为 "只欠外审"。 | 本文件写盘后，PROGRESS 状态码追加 V2 关键 P0：`CLAUDE_V2_NOTPASS_Q0026_RUBRIC_MAINLINE_PENDING_QUALITY_CHECK_RATING_INCONSISTENT_EXTERNAL_REVIEW_PENDING`。 |
| V2-F15 | Low | `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` §10 与 `02_codex_lane/MAIN_THINKING_LEDGER.csv` MT0006 | V2 body §10 卷面答案句写 "可以运用联想思维中的迁移和想象，把铁路文化、科技和历史元素迁移到产品设计中，并想象出具有铁路特色、可展示和可使用的新产品形态"；MT0006 ledger 写 "设计中国铁路博物馆文创产品时，要运用迁移或想象…"。一者写 "迁移和想象"（联言），另者写 "迁移或想象"（选言）。原始细则若锁联想思维要求 "迁移和想象同时" 应统一为 "和"；若锁 "任选一种方法" 应统一为 "或"。当前两份文件口径不一。 | 回源对应细则（如 2026朝阳一模 Q17(1) 后半），统一 V2 body §10 与 MT0006 ledger 的连接词；若细则允许 "任选其一" 应改为 "或"，否则改为 "和" 并要求两方法都落到产品方案中。 |

## Trigger-Chain Weak-Student Standard 检查

V1 F2 要求每段必须能让 "只读章节、不读顶部表 / 不读 ledger 的学生" 独立完成 "看材料 → 想方法 → 写答案 → 避免边界错误" 四步。V2 body draft 当前评估：

| 段 | 思维 V2 body | 标题触发链 | 教学桥段（为什么） | 卷面答案句可剪贴 | 易错边界写作失误 | 同类题对比 | 状态 |
|---|---|---|---|---|---|---|---|
| §1 | Q0011 | ✓ "真实调查 + 方法创新 + 分阶段安排" -> 科学总帽下复合 | ✓ | ✓ | ✓ 4 条具体写作错误 | n/a（无同形式题） | pass |
| §2 | Q0021 | ✓ "城市书房未来建设运营" -> 超前思维方法链 | ✓ | ✓ | ✓ | n/a | pass |
| §3 | Q0023 | ✓ "调研方案有缺陷，任选两个角度提建议" -> 方法匹配 | ✓ | ✓ 示范一 + 示范二 | ✓ | 缺与推理册 Q0018/Q0025 cross-ref | partial（见 V2-F8） |
| §4 | Q0004 | ✓ "具体经验 -> 抽出理念 -> 回到完整图景" | ✓ | ✓ | ✓ 平行隐喻警告 | n/a | pass |
| §5 | Q0017 | ✓ "数据打通 + 一站式结算 + 形成新机制" | ✓ | partial（只写正面解释，未先写排除路径） | ✓ B/C 项排除 | n/a | partial（见 V2-F11） |
| §6 | Q0001 | ✓ "蹲点观察 + 趋势预判 + 多轮测试" -> 三性 | ✓ | ✓ | ✓ | 缺与 Q0011 复合题 cross-ref | partial（见 V2-F9） |
| §7 | Q0002 | ✓ "共享主体+领域+程度+路径" -> 辩证多方法 | ✓ | ✓ | ✓ | 缺与 Q0011 cross-ref | partial（见 V2-F9） |
| §8 | Q0003 | ✓ "人文底蕴+趋势预判+冷热转换" -> 创新组合 | ✓ | ✓ | ✓ | 缺与 Q0011 cross-ref | partial（见 V2-F9） |
| §9 | Q0014 | ✓ "机遇挑战+拆分综合+持续投入" -> 辩证 | ✓ | ✓ | ✓ | n/a | pass |
| §10 | Q0019 | ✓ "铁路元素转文创产品" -> 联想思维 | ✓ | ✓（但口径与 ledger 不一） | ✓ | n/a | partial（见 V2-F15） |

| 段 | 推理 V2 body | 形式归组 | 可检查式子 | 同类题对比 | 主链/可选区分 | 状态 |
|---|---|---|---|---|---|---|
| §1 | 充分条件肯后无效 Q0008+Q0020 | ✓ | ✓ p->q;q;therefore p | ✓ Q0006/Q0009 | Q0020 无独立材料动作 | partial（见 V2-F3） |
| §2 | 不完全归纳识别 vs 评析 Q0018+Q0025 楚王 | ✓ | ✓ | ✓ | n/a | pass |
| §3 | 类比推理 Q0025 晏子 | ✓ | ✓ | ✓ 与楚王对比 | n/a | pass |
| §4 | 矛盾 vs 反对 Q0016+Q0026 乙 | ✓ | partial（漏下反对） | ✓ | n/a | partial（见 V2-F4） |
| §5 | 三段论 + 前提不真 Q0026 甲 | ✓ | partial | partial | **fail**（四概念/前提不真并列） | **fail**（见 V2-F1 P0） |
| §6 | 充分条件有效式+无效式 Q0005/Q0006/Q0009 | ✓ | ✓ 三式齐 | ✓ | n/a | pass |
| §7 | 必要条件 Q0007/Q0009/Q0010 | ✓ | ✓ q->p；肯后有效肯前无效 | ✓ | n/a | pass |
| §8 | 三段论审查 Q0005/Q0010/Q0012/Q0013/Q0015 | ✓ | ✓ | ✓ | n/a | pass |
| §9 | 矛盾律/同一律 Q0005/Q0026/Q0024 | ✓ | ✓ | ✓ | n/a | pass |
| §10 | 概念划分+选言判断 Q0022+Q0024 A | ✓ | ✓ | ✓ | n/a | pass |
| §11 | 形式逻辑综合选择 Q0024 | ✓ | ✓ | ✓ | n/a | pass |

合计：思维 10 段中 5 pass / 5 partial / 0 fail；推理 11 段中 8 pass / 2 partial / 1 fail（§5 Q0026 甲）。

V2 body 比 V1 同位置（顶部索引表 + 章节正文 2 段式）有显著进步——大部分段已达到 "学生能独立读章节、写答案" 的弱学生标准。但 §5 Q0026 甲的 fail 是直接学生失分点，必须 V3 前修。

## Source Ledger Coverage 检查

V2 body draft 中所有题号已在源 ledger 中存在：

- 思维 V2 body 覆盖 Q0001/Q0002/Q0003/Q0004/Q0011/Q0014/Q0017/Q0019/Q0021/Q0023 共 10 题
  - MAIN_THINKING_LEDGER MT0001-MT0008 覆盖 Q0001/Q0002/Q0003/Q0011/Q0014/Q0019/Q0021/Q0023 8 题
  - Q0004 在 CHOICE_TRAP_LEDGER CT0001（thinking）
  - Q0017 在 CHOICE_TRAP_LEDGER CT0005（thinking）
  - 问题：Q0004/Q0017 在 MAIN_THINKING_LEDGER 无主线 entry，CHOICE_TRAP_LEDGER 字段口径不同（见 V2-F10）

- 推理 V2 body 覆盖 Q0005/Q0006/Q0007/Q0008/Q0009/Q0010/Q0012/Q0013/Q0015/Q0016/Q0018/Q0020/Q0022/Q0024/Q0025/Q0026 共 16 题
  - REASONING_FORM_LEDGER RF0001-RF0024 覆盖全部 16 题（含 Q0005 三主张分行 / Q0009 两推理分行 / Q0010 甲乙分行 / Q0025 楚王晏子分行 / Q0026 甲乙丙分行）
  - 全部 source-locked ✓

无 "V2 body 写了但 ledger 不存在" 的情况。但有口径不一致（V2-F15 Q0019 "和" vs "或"）与 ledger 字段缺失（V2-F10 Q0004/Q0017 主线 entry）问题。

## Hold/Gate 文件诚实度评估

| 文件 | 诚实表达 | 包装/失实风险 | 处置 |
|---|---|---|---|
| `PROMOTION_LOG.md` | check 1-7 列完整、check 7 列每行明写 "fail: Claude V1 NOT_PASS, GPT Pro pending"、状态名去 V1 化 | row 列合并多题号（V2-F7/F13）；notes 列未自我披露 V2 新硬伤（V2-F12） | 拆 row + 补 notes |
| `PROMOTION_QUALITY_CHECK.md` | 明确 hold；Immediate Quality Gaps 段承认 GPT Pro 未提交 + 覆盖缺口 | Current Ratings 表全用未定义档 `partial-plus`（V2-F2）；Immediate Quality Gaps 漏列 Q0026 甲细则主链未回源、Q0020 子节未独立 | 修评级口径 + 扩 Gaps 段 |
| `BLOCKER_RECONCILIATION.md` | BLK-003/004 拆双状态 ✓；Still Open 8 项列名清晰 | Still Open 项无优先级，无 milestone | 加 priority / milestone（V2-F6） |
| `COVERAGE_GAP.csv` | 10 项全列、status 全 open ✓ | 无 priority / owner / milestone（V2-F6） | 加列 |
| `PROGRESS.md` | line 52 状态码保留 NOT_PASS + PENDING ✓；line 48/49/50 三个 open 项明列 | 状态码未含 V2-F1 P0 主链回源缺口（V2-F14） | 追加 |

总结：hold/gate 文件结构层面完成度高，但仍有两个口径漏洞会让外部读者把 "V2 body 已写" 误读为 "已接近发布"——分别是 PROMOTION_QUALITY_CHECK 的 `partial-plus` 隐性 4 档（V2-F2）与 PROMOTION_LOG 的 row 合并（V2-F7）。这两条不修，门控就不能阻断 V0/V1 已点出的 "字段非空 / 状态名给人通过感" 类失效模式。

## Highest-Priority Rewrite List

按学生使用风险倒序，V2 -> V3 必须先做：

1. **Q0026 甲细则主链回源 + 答案句改写**（V2-F1 = V1 F5 未修复）。引 `gpt_sources/.../2026西城一模细则.md` 行号，主链与可选两层明示。
2. **Q0020 在 §1 拆独立子节**（V2-F3 = V1 F9(a) 未完成）。补海淀期末 Q20(1) 具体材料动作与卷面答案句。
3. **PROMOTION_QUALITY_CHECK 评级口径自洽**（V2-F2）。把 `partial-plus` 写入 Rating Rules 定义、或全部降回 `partial`。
4. **V2 body §4 补下反对关系**（V2-F4）。对齐 REVIEW_DRAFT §五.3 三关系表。
5. **V2 body 开头加 "如何使用本宝典" 5 点路径**（V2-F5）。
6. **PROMOTION_LOG row 列逐题展开 + notes 自我披露 V2 硬伤**（V2-F7/V2-F12）。
7. **V2 body §6/§7/§8 末段加 Q0011 复合题指针**（V2-F9）。
8. **V2 body §3 与推理册 §2 互加 cross-ref**（V2-F8）。
9. **V2 body §5 Q0017 卷面答案句补 "为什么不是创新思维" + 正确选项 D 双段**（V2-F11）。
10. **MAIN_THINKING_LEDGER 增补 Q0004/Q0017 主线 entry**（V2-F10）。
11. **COVERAGE_GAP.csv 加 priority / owner / milestone 列**（V2-F6）。
12. **PROGRESS 状态码追加 Q0026 主链 / 评级口径 缺口**（V2-F14）。
13. **V2 body §10 Q0019 与 MT0006 ledger 统一 "和" 或 "或" 连接词**（V2-F15）。
14. **真实提交 GPT Pro V1 / V2 外审包**（COVERAGE_GAP GAP010 + BLK-013 仍 open；外审是 V3 启动前提条件）。
15. **真实启动 Claude V3 外审**（本文件写盘后才能进入下一轮）。

## Coverage Pressure List

按需要释放压力倒序，与 V1 同表对照（无显著变化，仅追加 V2 视角）：

1. **选言推理规范代表题**（V1 #1，仍 open）：GAP008。Q0022 是选言判断遗漏，不等于规范选言推理。
2. **2024 backlog**（V1 #2，仍 open）：GAP006。
3. **2025 backlog**（V1 #3，仍 open）：GAP005。
4. **2026 选择题语料**（V1 #4，仍 open）：GAP003/GAP004。
5. **北京高考 Q19(2) 青海防沙治沙**（V1 #5，仍 open）：GAP007。
6. **2024朝阳二模 Q7**（V1 #6，仍 open）：GAP001 / BLK-002。
7. **2026海淀一模 Q17(1) 完整问卷**（V1 #7，仍 open）：GAP002 / BLK-005。
8. **复合题节点扩容**（V1 #8，仍 open）：GAP009。Q0011 类同型题只 1 例。
9. **类比 + 不完全归纳对比题**（V1 #9，仍 open）：Q0025（楚王 + 晏子）单点稀缺。
10. **真实 GPT Pro 外审**（V1 #10，仍 open）：GAP010 / BLK-013。
11. **评标实录 / 讲评 PPT 三角证据**（V1 #11，仍 open）：仅 Q0002 三重。
12. **V2 新增**：**Q0026 甲细则主链回源**——本审 V2-F1 P0，未做。

## Forbidden Final Claims

下列说法在任何 user-facing 产物（宝典 MD / DOCX / PDF / README / 进度小结 / 移交消息 / 用户对话）中**均不得书写、不得显示、不得暗示**：

- 不得写 "选必三《逻辑与思维》宝典 已完成 / 终稿 / 定稿 / V2 / 最终版"。
- 不得写 "已穷尽 2024-2026 三年北京选必三考题"、"全量覆盖"、"已覆盖所有选必三题"。
- 不得写 "已经过 Claude 外审 / 通过 Claude review / Claude PASS"。V0/V1/V2 三轮累计三次 NOT_PASS。
- 不得写 "已经过 GPT Pro 外审 / GPT Pro 已通过"（GAP010 / BLK-013：未提交）。
- 不得用 "思维宝典涵盖 X 种思维方法 / 推理宝典涵盖 Y 种推理形式" 暗示完备性。
- 不得宣称 "Q0011 / 2024海淀二模 17(1) 已完成宝典级修复"（V1 F1 已修，但本审 V2 未审完整 prose 与新增同型扩容）。
- 不得宣称 "Q0023 / Q0021 / Q0004 / Q0017 已完成宝典级修复"（V2 body 已改但门控未通过 Check 7）。
- 不得宣称 "Q0026 已完成判定"——V2-F1 显示甲题细则主链未回源、不可作终稿用。
- 不得宣称 "PROMOTION_GATE 已生效阻断 V0/V1 既有失效模式"（V2-F2/V2-F7：评级口径与 row 合并仍有薄壁）。
- 不得宣称 "PROMOTION_QUALITY_CHECK 已达 pass" 或 "已达 partial-plus 代表接近 pass"——`partial-plus` 未在 Rating Rules 中定义。
- 不得宣称 "BLK-003 / BLK-004 已闭合"（拆为 evidence_closed + promotion_held 双状态，promotion 仍 held）；BLK-002/005-013 仍 open。
- 不得写 "可作为学生练习材料 / 可直接发学生 / 可印刷下发"。V2 body 大部分段已 pass 弱学生标准，但 §5 Q0026 甲 fail、§1 Q0020 partial，整书仍不达交付门。
- 不得写 "A/B 双线已对齐 / 双线闭合 / 双线一致"（V2-F10/V2-F15 显示 ledger 与 body 仍有口径错位）。
- 不得写 "已交付 / delivered / ready-to-ship / 入正稿"。
- 不得给区/年份/试卷-级完成率数字（仍 26 / 估计 60+）。
- 不得引用本审结果反过来说 "Claude 已确认 Q0001-Q0026 教学语言无问题"。本审深度检查了 Q0011 / Q0017 / Q0019 / Q0020 / Q0023 / Q0026 等点位，但未对每条逐字回源原始试题与细则。
- 不得把 `PROMOTION_LOG` 中含 `pending_next_external_review` / `v2_body_coverage_added_hold_external_review_and_gaps` 字样的状态名解读为 "已通过 V2 门"——Check 7 至今 fail。
- 不得宣称 "V1 全部 18 findings 已修复"。本审显示 10 项 fully fixed / 3 项 partial / 2 项 partial 含口径漏洞 / 1 项 not fixed（F5）/ 3 项 not verified（F14/F16/F17）。
- 不得宣称 "V2 body draft 已等同于宝典正文"——它只是 body rewrite 草稿，且未含使用入口（V2-F5）。
- 不得在 PROGRESS.md 状态码中把 `EXTERNAL_REVIEW_V2_DONE_NOT_PASS` 简写为 "external review v2 done"——必须保留 NOT_PASS 后缀。
- 不得宣称 "PROMOTION_QUALITY_CHECK 已升级使门控合规"——其评级未在规则中定义，反而引入了未识别的第 4 档。

下一可达状态（建议命名）：`V2_EXTERNAL_REVIEWED_REQUIRES_Q0026_RUBRIC_MAINLINE_FIX_AND_QUALITY_CHECK_RATING_CONSISTENCY_AND_REAL_GPTPRO_BEFORE_V3`。

— Claude 外审 V2（独立 lane）· 完
