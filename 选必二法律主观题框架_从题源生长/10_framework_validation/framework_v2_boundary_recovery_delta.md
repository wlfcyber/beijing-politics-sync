# framework_v2 边界恢复 delta

更新时间：2026-05-19 13:19 CST

## 计数口径

- v1 原 PASS：37 道。
- 非 PASS 中可恢复为核心的原题单位：9 道。
- 拆分后可恢复为核心的新法律小问：2 道。
- reference/open 容器保留：6 道，其中原题单位 5 道，拆分 formal open 1 道。
- 暂不计数的缺证据/疑似重复：2 道。
- 明确剔除非法律或错配：12 道。
- 旧父题被拆分或去重，不再作为独立法律题计数：7 道。

## 当前可用题量

- 严格核心闭合题：37 + 9 + 2 = 48 道。
- 核心 + 开放/参考容器可教学运行题：48 + 6 = 54 道。
- 若把“题面法律但细则待补”的 CC0259 暂列待补证据池，则可跟踪题量为 55 道。

这解释了“为什么不是 35 题”：35/37 只是 v1 框架压测的严格 PASS 口径；回源后，至少有一批低频 formal 法律题、reference/open 题和拆分小问不应被当作无题。

也解释了“为什么暂时还不能直接宣称六十多道满分闭合”：当前有 12 个非法律/错配项必须剔除，另有若干父题是综合题或重复页，不能为了凑数重复计入。

## 后续动作

1. 等 GPT-5.5 Pro 边界恢复复核完成，保存到 `10_framework_validation/gpt55pro_boundary_recovery_review.md`。
2. Claude Opus 上传受阻时，保留 handoff prompt 和 packet，不重复点发送；若无法恢复，记录 `real_call_upload_blocked`。
3. 将 `core_recovered` 和 `core_recovered_split` 写入 framework_v2 的开放容器/低频节点修订，不让 reference_only 单独支撑核心节点。
4. 对 `pending_missing_legal_rubric` 继续回源找细则；找不到则只进待补证据清单。
