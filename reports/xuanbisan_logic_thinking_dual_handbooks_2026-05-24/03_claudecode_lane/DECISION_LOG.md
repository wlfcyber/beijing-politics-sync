# B Line Decision Log

## D-001 2026-05-24

- decision: 不继承 2026-05-06 版本的任何结论，只把它作为旧索引和候选定位工具。
- reason: 用户与本轮 prompt 明示“2026-05-06 不是四线终极全量穷尽版”。
- check: 任何与旧版重叠的条目必须重新回源核验。

## D-002 2026-05-24

- decision: 2026石景山期末本轮继续排除。
- reason: 用户此前逐题复核确认无可用评分细则；本轮 prompt 维持该排除。
- check: 若 source_ledger 之后出现新的可用 rubric，再行解锁；否则保持 boundary。

## D-003 2026-05-24

- decision: 评分细则原词优先；只有真正的细则才能 `A-formal`，讲评/评标 PPT 仅在含明确给分口径时落 `A-support`。
- reason: 选必一/二/必修四老教训；普通参考答案与教师版答案不得冒充正式细则。
- check: 每条 entry 的 `evidence_source` 写明确文件名与状态。

## D-004 2026-05-24

- decision: 框架优先组织 thick body：思维部分按思维类型 -> 三性/三新/小方法 -> 模拟题；推理部分按推理形式树 -> 规则口令 -> 同类题。
- reason: 用户本轮明确否定按地区/年份/题号流水展开。
- check: thick_body_REVIEW_ONLY.md 二级/三级标题必须是框架节点，不得是“2026朝阳期中”这种文件式标题。

## D-005 2026-05-24

- decision: 2026顺义一模 Q19(2) 锁定为科学思维三性 (`客观性`/`预见性`/`可检验性`) 三层评分。
- reason: 顺义一模 PPT 细则 `de758e5e79500dd0_2026顺义一模细则.md` 第 143-148 行明示三层 1+1 给分。
- check: 此条目必须进入 `main_thinking_entries.jsonl`，且 thick body 在“科学思维 -> 客观性/预见性/可检验性”三节点各引用一次。

## D-006 2026-05-24

- decision: 2026顺义一模 Q19(1) 锁定为三段论推理判断题，进入推理册。
- reason: 同一套卷细则 142 行起明示“演绎推理两个条件”、“三段论推理规则”给分。
- check: 推理 entries 应保留三段论形式 (M 中项)、有效式/无效式判断、规则口令。

## D-007 2026-05-25

- decision: 2026 二模 B 线采用 suite-slice 真实复跑结果作为有效证据，不采用整套一次性复跑的 `-1`/挂起结果作为审核结论。
- reason: 一次性复跑没有生成必需产物；分段复跑覆盖 Q0113-Q0140 并逐段返回 `0`，原始 stdout 已留档。
- check: 任何后续“B 线已审”表述必须指向 `03_claudecode_lane/logs/claudecode_2026_ermo_*_stdout.log` 与 `entries/2026_ermo_b_line_entries.jsonl`，不得把这说成外审通过。

## D-008 2026-05-25

- decision: 顺义初跑关于正文文件不存在的判断作废，以正文路径补充复核为准。
- reason: 初跑提示使用旧文件名 `BODY_思维宝典.md` / `BODY_推理宝典.md`；实际正文草稿在 `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` 与 `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`。
- check: Q0136/Q0139/Q0140 的正文层判断以后必须引用 `claudecode_2026_ermo_shunyi_body_supplement_stdout.log`。

## D-009 2026-05-25

- decision: 2026 二模当前不能进入 release-bearing 状态；先处理 `blockers_2026_ermo.csv` 的本地可修项，再提交 GPT Pro V61 和 Claude V59。
- reason: B 线发现同形聚合、正文层级、边界持久化和 CT 行缺口；真实外审仍未捕获。
- check: 任何 Word/PDF 或“宝典成品”动作前，必须确认 blockers 已关闭或逐条有接受性豁免记录。

## D-010 2026-05-25

- decision: 对 B 线发现的本地可修项，优先采用“保留原分类 + 显式边界/证据层级标注”的补丁方式，不在未外审前大幅重排正文。
- reason: 多数问题是 A-support 层级、综合题边界、同形索引或 CT 缺口，不需要推翻 A 线 source-lock；真正的大结构聚合需等下一轮结构审查统一处理。
- check: `blockers_2026_ermo.csv` 中 P1/P2 本地补丁可标 `patched_pending_external_review`；同形聚合用全局索引收口后，只保留 P0 外审门控 open。

## D-011 2026-05-25

- decision: 推理册同形聚合先用全局“同形聚合索引”收口，不在当前未外审阶段重排 60 多个正文小节。
- reason: 用户硬性要求是“同一推理形式汇总到一块”；当前索引已经把必要条件、定义、类比、不完全归纳、三段论、同一律/矛盾律等同形样本显式汇总，满足复习路径要求，同时避免大范围改写引入新错。
- check: 下一次正文成品化可在该索引基础上做章节级重排；当前 B 线发现项只保留外审门控 open。
