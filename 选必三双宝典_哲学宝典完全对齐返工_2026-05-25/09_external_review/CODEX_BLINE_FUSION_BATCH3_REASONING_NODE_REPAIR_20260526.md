# Codex/B 线融合 Batch3：推理残差节点与思维复挂修补 2026-05-26

verdict: `NOT_COMPLETE_BATCH3_FUSION_APPLIED_REBUILD_REQUIRED`

本批处理上一轮裁决矩阵中尚未审完的 F2/F3/F5 残差。原则仍然是：B 线内容只有和本 run source-lock、coverage、现有候选稿一致时才进入学生正文；若 B 线更厚但题源对象或题型与 source-lock 冲突，只能拒绝或降级为审计线索。

## 已吸收进正文

| 编号 | 处理 | 正文变化 |
| --- | --- | --- |
| F2.2 `2024西城一模 Q19(3)` | 吸收属种/真包含表达 | 推理稿“概念外延关系：相容/属种关系”答案落点改为：`新型举国体制` 的外延包含在 `举国体制` 的外延之中，是种概念与属概念之间的真包含关系；因此属于属种关系，也属于相容关系。 |
| F2.3 `2024.11朝阳期中 Q18` | 不用 B 线污染材料，改用本 run source-lock 厚化 | 推理稿类比条目改写为“橘因水土不同而性状变化”类比“人因社会环境不同而行为表现变化”，明确已知相似属性、被推出未知属性、或然性和反驳功能。 |
| F3.1 `2024东城一模 Q18(3)` | 吸收更卷面化的辩证否定句 | 思维稿辩证否定条目答案落点改为“传统产业是未来产业的基础和起点，未来产业是对传统产业的扬弃改造和前瞻布局”，同时保留改造传统产业与布局未来产业两个来源支持方向。 |
| F3.3 `2026海淀二模 Q18(1)` | 接受联想节点复挂 | 思维稿在“联想、迁移和想象”下新增该题复挂，专门写“由现有月季品种联想到野生近缘种、扩大基因来源、再经田间试验检验整体性状”。 |

## 已拒绝或降级的 B 线条目

| B 线 entry | 裁决 | 理由 |
| --- | --- | --- |
| `RM-2025-FENGTAI-2MO-Q16-2` | reject for source conflict | 本 run coverage `Q0111` 锁定为三段论构建题，现推理稿也在“三段论构建”节点；B 线写成 `AI 助教` 类比人类辅导教师，与 source-lock 不一致。不得进入类比章节。 |
| `RM-2026-CHAOYANG-2MO-Q19-1` | reject for source conflict | 本 run coverage `Q0121` 锁定为“生产性服务业”概念内涵/定义方法题；B 线写成电动汽车与燃油车类比替代，与 source-lock 不一致。不得进入类比章节。 |
| `RM-2024-CHAOYANG-MID-Q18` 的 B 线材料 | reject for source conflict | 本 run coverage `Q0025` 和现推理稿锁定为楚王轻率概括、晏子橘/水土类比；B 线写成人体免疫系统与企业风险控制类比，与 source-lock 不一致。只保留本 run 已锁定的晏子条目。 |
| `RM-2024-XICHENG-1MO-Q19-5` | reject for current body | 本 run coverage `Q0066` 属思维主观题线索，描述为未来产业方向研判及超前思维等采分点；B 线写成枚举概括/同一律主观题，与 coverage 描述不一致。逻辑规律章节继续保留已锁定的 `2024西城一模 Q11`、`2024东城一模 Q6`、`2025朝阳期末 Q19` 等题，不机械新增该 B 线条目。 |
| `T-2025-HAIDIAN-FINAL-Q18` | keep current Codex source-lock | 当前思维稿锁定为北京城市图书馆；B 线写成社区闲置厂房，上一轮已判不直接替换。本批继续维持原判。 |

## 本批后的仍未完成

- 本批只修改 Markdown 正文，尚未重建 Word/PDF。
- 真实 GPT Pro / Claude 外审仍为 `real_call_pending`。
- fresh-context 零基础盲测尚未运行。
- Governor / Confucius 尚未以本批更新后的 Word/PDF 作 artifact-only 终验。
