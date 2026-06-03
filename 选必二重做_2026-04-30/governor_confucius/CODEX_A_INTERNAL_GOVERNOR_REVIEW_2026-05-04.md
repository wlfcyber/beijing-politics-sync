# Codex A 内部 Governor 初验报告

日期：2026-05-04

角色边界：本报告由 Codex A 内部 Governor/Confucius 预验子角色生成，只做 artifact-only 初验和本地风险归纳。未重新打开原始试卷、细则、PPT、PDF、网页端 GPT-5.5 Pro 或网页端 Claude Opus 对话。它不是 Final Governor PASS。

写域边界：仅写入 `governor_confucius/`。未修改脚本，未修改 `final_legal_outputs/` 主体文档，未修改 ClaudeCode 或 Opus 报告。

## 读取对象

1. `final_legal_outputs/选必二法律与生活最终进化框架_2026-05-03.md`
2. `final_legal_outputs/选必二法律题全量处理合集_2026-05-03.md`
3. `claudecode_lane/outputs/CLAUDECODE_B_CONFLICTS_FOR_CODEX_2026-05-04.md`
4. `opus_writer/reports/CLAUDE_OPUS47_ADAPTIVE_XUANBIER_REPORT_20260504.md`

第 4 个文件存在，已纳入本次预验。

## 总结论

内部 Governor 初验结论：CONDITIONAL LOCAL PRECHECK PASS / FINAL PASS BLOCKED。

可认可：当前框架文档已经明确标注“本地候选框架稿”，且在开头声明 GPT-5.5 Pro 网页审议和双方交叉批判回收前不得写成正式 V1/Governor PASS。框架主干已保留一核、二线、三问、四步，并将八域标为后台索引版，学生前台压成五域。

不可放行：本轮不能给 Final Governor PASS。原因是 GPT-5.5 Pro 网页报告和 GPT-Claude 双向交叉批判在已读 artifact 中未完成闭环；合集仍含大量原料层、审计层、参考答案/评分细则语言，不应直接视为学生成品；26/113 待正式细则锁定、9 道选择题官方答案待锁、14 道混合/特殊题待拆分仍是硬风险。

## 核心闸门检查

| 检查项 | 初验判断 | 证据/说明 |
|---|---|---|
| 是否明确非 Final PASS | 通过 | 框架文档开头声明 GPT-5.5 Pro 网页审议和交叉批判前不得写成正式 V1/Governor PASS。 |
| 一核 | 通过 | 框架保留“以事实为根据、以法律为准绳，通过具体法律关系中的规则适用实现定分止争”。 |
| 二线 | 基本通过 | 已采用“权利保护与权利边界 / 规则适用与程序救济”，并把价值后置；这吸收了 Opus 对“德治价值线过虚”的修订意见。 |
| 三问 | 通过 | 保留“判什么/怎么处理、凭什么、有什么意义”。 |
| 四步 | 基本通过 | 保留“定主体关系 -> 找争点事实 -> 对规则条件 -> 按题型落结果”，且第四步已改为按题型选落点。 |
| 五域前台 | 通过但需成品化压缩 | 学生版五域存在，程序救济横切、生态公益/新业态开放容器；仍需后续转成干净学生手册。 |
| 八域后台索引 | 通过 | 框架写明八域只用于 Codex/教师后台标签和索引，不作为学生前台背诵主干。 |
| `rubric_pending` / `answer_pending` 标签 | 基本通过 | 框架中 `rubric_match_pending` 26 次、`answer_pending_official` 9 次；合集里 `rubric_match_pending` 27 次、`answer_pending_official` 9 次。标签存在，但 Lane B 指出候选答案格式仍需统一。 |
| 审计语言污染学生内容 | 未通过 | 合集是原料/处理合集，含大量“证据状态、匹配方式、证据等级、评分细则、参考答案、OCR、可从……角度作答”等审计或原答案语言，不能直接给学生。框架文档也保留部分细则/参考答案摘录，作为教师/后台材料可以，作为学生主体不干净。 |

## 本地 Governor 风险

### G1. Final Governor gate 仍被阻塞

已读 artifact 只能证明 Claude Opus 4.7 Adaptive 报告存在，并且该报告自身声明未读本地源文件、具体题目均需 Codex 本地核验。未见 GPT-5.5 Pro 网页端正式报告，也未见 GPT 与 Claude 对彼此方案的双向交叉批判闭环。

裁决：禁止写“Final Governor PASS”“正式 V1”“Confucius 闭环”。

### G2. 证据锁定比例仍不足以支撑无条件主干

框架和合集一致给出：入册法律题 113，formal/评标/阅卷/评分证据 78，仍待正式细则锁定 26，官方答案待锁选择题 9，混合/特殊题待拆分复核 14。Lane B 的 C-001 进一步指出，`paper_source` / `unknown` 不应等同于 rubric matched；当前主干必须继续区分“formal 口径”和“含 pending 口径”。

裁决：高频主干可以作为候选观察，不得把待锁题当作正式细则样本讲给学生。

### G3. 选择题候选答案标签仍需统一

Lane B 的 C-003 指出，9 道官方答案待锁选择题目前存在标签格式不统一风险。框架和合集已有 `answer_pending_official`，但学生或后续 reviewer 仍可能把候选答案误读为官方答案。

裁决：后续修订应统一为“候选答案 X｜未锁定（answer_pending_official）”，并在学生版隐藏或隔离。

### G4. OCR / 扫描件缺口会影响题目覆盖闭环

合集末尾列出多套“未入册/待 OCR 套卷提示”，包括 2024 朝阳一模、2024 海淀期中、2024 丰台一模、2026 顺义一模、2026 西城期末等。Lane B 的 C-004 特别点名 2026 东城一模第 10、11 题需按题号 OCR。

裁决：当前不能声称 source exhaustion 完成；只能说已做 artifact-level 初步汇总。

### G5. 混合/特殊题待拆分造成频次失真风险

Lane B 的 C-006 指出 14 道 `included_needs_review` 未拆分前不应无差别计入域频次。Opus 报告也把“14 道 included_needs_review 是否计入主干频次”列为需本地核验。

裁决：后续报告必须保留两套口径：已拆法律小问入框口径、含待拆混合题观察口径。

### G6. 学生内容污染风险显著

合集含大量原始参考答案、评分细则、非法律模块答案、哲学/文化/逻辑/经济角度提示、OCR 和证据标签。这些对后台追溯有价值，但若直接进入学生内容，会破坏“选必二法律可学化”目标。

裁决：学生版必须单独抽取、重写、去审计化；合集只能作为教师/后台原料包。

## 必须修后才能进入下一轮验收

1. 补齐 GPT-5.5 Pro 网页端正式报告，并完成 GPT-5.5 Pro 与 Claude Opus 4.7 Adaptive 的双向交叉批判。
2. 对 26 个 `rubric_match_pending` 给出逐题清单、当前阻塞原因、下一步来源路径；不得仅保留总数。
3. 对 9 个 `answer_pending_official` 统一标签，并禁止生成正式错项判断。
4. 对 14 道混合/特殊题拆出法律小问；拆不出的不得计入 formal 主干频次。
5. 将学生版和后台版彻底分离：学生版只保留五域、一核二线三问四步、命题路径分型、可迁移动作；后台版保留八域索引、细则摘录、证据状态。
6. 清理学生版污染词：`证据状态`、`匹配方式`、`证据等级`、`OCR`、`评分细则`、`评标`、`参考答案`、`可从……角度作答`、原始非法律模块答案等不得进入学生主体。

## 初验状态

本地 Governor 状态：`internal_precheck_done`

Final Governor 状态：`blocked_real_gpt55_cross_critique_pending`

学生交付状态：`blocked_student_clean_version_pending`

## changed files

- `governor_confucius/CODEX_A_INTERNAL_GOVERNOR_REVIEW_2026-05-04.md`
- `governor_confucius/CONFUCIUS_ARTIFACT_ONLY_PRECHECK_2026-05-04.md`
