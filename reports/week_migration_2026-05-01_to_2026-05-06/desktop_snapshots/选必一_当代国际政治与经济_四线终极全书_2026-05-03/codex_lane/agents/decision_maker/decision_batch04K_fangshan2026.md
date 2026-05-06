# Decision Maker Batch04K Next Step - 2026房山一模

裁决时间：2026-05-04
角色边界：Codex A 决策者；只做分工、瓶颈和放行建议；不改 fusion / student / delivery 文件；不宣布最终成品。

## 1. 当前状态裁决

Batch04K 可以维持“Codex A prelim candidate”状态，但不能做最终闭合。

- Q19 是本批唯一可进入选必一候选融合的主观题：P0 正式细则 DOCX + 原卷 PDF 视觉核读已支撑“海南自贸港封关助力国际循环”。
- Q16(1) 维持 boundary-only：经济与社会题，不进入选必一主频。
- Q20 维持 boundary-only：综合等级题，虽有“中国智慧 / 中国方案”表达，但不是选必一逐点评分细则。
- 学生稿、Word/PDF、最终交付和 coverage close 继续 BLOCK；本批只能进入内部预览/候选修补阶段。

## 2. 是否必须等待 ClaudeCode B

必须等待 ClaudeCode B 后再作 Batch04K 最终闭合。

理由：
- ClaudeCode B 的 Batch04K screen 已启动但尚未形成可比对输出；当前只有 Codex A 预融合，缺少独立 lane 的 A/B 校验。
- Q19 存在评分结构疑点，属于会影响 atom 拆分与分值归属的 P0 问题，不能靠单线解释直接放行。
- 在 B 输出前，允许 Patcher / Governor 做本地预审和阻断条件准备，但不允许把 `candidate_pre_ab_review` 宣告为 `candidate_with_fixes` 或 closure。

## 3. Q19 8分结构疑点处理

当前四组 atom 只能作为工作假设，不作为最终评分法宣布：

- FS26-01：市场/消费侧，超大规模市场、货物服务贸易升级、要素自由流动、资源优化配置、贸易投资自由化便利化。
- FS26-02：生产/产业侧，技术研发、企业竞争力、产业升级、融入全球产业分工和合作。
- FS26-03：投资/营商环境侧，优化营商环境、吸引外商投资、引进来。
- FS26-04：中国方案侧，制度型开放 + 中国方案 / 国内国际双循环 / 两个市场两种资源联动效应。

必须先让 Patcher/Governor 判定原始 DOCX 中“表示1-5，每个2分，总分不超过6分”的精确归属：

1. 若“1-5”只约束前三类机制表达，则前三组进入“最高6分的机制池”，FS26-04 作为独立 2 分中国方案侧保留，合计 8 分。
2. 若“1-5”覆盖所有候选表达且总分只给 6 分，则当前四个 atom 的分值结构必须返修，不能按四组各 2 分进入主表。
3. 若剩余 2 分来自“制度型开放/中国方案/两市场两资源联动效应”中的单独评分口径，需在 merge register 中明确写成“6分机制池 + 2分中国方案侧”，避免学生稿误读为四个并列必答点。
4. 若原文还有“完整作答、材料结合、逻辑链”等结构性给分，Patcher 必须补回原文证据，Governor 再决定是否拆为边界说明或补丁行。

在该疑点未闭合前，禁止把 Q19 写成“4个独立2分点必背模板”。

## 4. 输出形态门槛

进入学生稿前，Q19 必须补齐用户已纠正的六段形态：

完整设问 -> 设问触发 -> 材料触发 -> 框架落点 -> 答题点自身积累 -> 答案句变体。

当前 prelim atom 表已有材料触发和融合句基础，但还不等于学生可读条目。后续补丁者需要把 Q19 改写为可迁移的按题学习结构，且不得把 source path、P0、atom、candidate、merge guard、DOCX/PDF 等内部词带入学生正文。

## 5. 角色任务

Codex 生产：
- 暂停 Batch04K 主表正式合并，只保留 prelim candidate 证据链。
- 等 ClaudeCode B 输出后，做 A/B difference table：重点比对 Q19 是否同意“6分机制池 + 2分中国方案侧”。
- 可并行准备 Batch04L 的 source locator 和 coverage 定位，但不替代 Batch04K 闭合。

劳动者：
- 不重复劳动整批；只在 ClaudeCode B 输出后复核 Q19 的设问、材料三行和细则原文锚点。
- 特别核对“表示1-5，每个2分，总分不超过6分”前后文，记录它管辖哪些答案要点。

Patcher：
- 先做本地证据核验：回到 `细则.docx` 原文，摘出 Q19 分值结构所在段落的精确文字位置。
- 准备两套补丁：一套按“前三机制最高6 + 中国方案2”修；一套按“当前四组分值不可独立成立”返修。
- 不改学生稿，不改正式主融合表。

Governor：
- 设定 gate：无 ClaudeCode B 对照、无原文分值结构核验、无输出形态补丁，三者缺一即 BLOCK。
- 若 B 与 Patcher 均确认“6+2”结构，可给 PASS_WITH_FIXES，允许后续进入 candidate_with_fixes。
- 若 B 或 Patcher 发现 cap 解释不成立，必须 BLOCK，要求重拆 atom 分值与 merge register。

自动化检测者：
- 监控 ClaudeCode B 是否产出 Batch04K 对照文件。
- 检查本轮是否误改 fusion/student/delivery 文件；如有非授权变更，立即报 Governor。
- 后续进入 candidate_with_fixes 前，跑 coverage/status 一致性检查，确保 Q16(1)、Q20 仍是 boundary-only。

## 6. 可并行与阻断边界

可以并行：
- Patcher 做 Q19 原文分值核验。
- Governor 准备 gate 条件。
- 自动化检测者监控 ClaudeCode B 输出和文件变更边界。
- Codex 生产预备下一批 source locator。

不能并行越界：
- 不能把 Batch04K 写入学生稿。
- 不能更新正式主融合表或 final delivery。
- 不能把 Q19 四组 atom 宣布为最终 8 分结构。
- 不能因等待 B 而停工；等待期间转入证据核验、gate 准备和下一批源定位。

## 7. 下一批建议

Batch04K 闭合后，下一批建议进入 Batch04L：2026石景山一模 source-reverify。

注意：此前排除的是 2026石景山期末；不等同于排除 2026石景山一模。Batch04L 仍需按“评分细则/评标/阅卷总结优先、原始本地目录优先、只收选必一主观题逐点口径”的规则重新筛。
