# Phase04 Lane B Targeted Verification Plan

- phase: `Phase04 targeted evidence fusion with open coverage blockers`
- lane: ClaudeCode Lane B
- date: 2026-05-04
- status: PLAN_ACTIVE_BATCH01_IN_PROGRESS

---

## 执行范围概述

本计划依据 GPT Phase03 裁决 `GO_BUT_WITH_BLOCKERS` 制定。
Lane B 的任务是对 Codex A 未覆盖或存疑项目进行独立回源复核，不接受 Codex 结论为事实。

**总目标集合（全部批次）**：

| 类别 | 数量 | 控制文件 |
|------|------|---------|
| A-only in-scope/cross keys | 76 | phase04_in_scope_cross_119_index.md |
| B-only candidate keys | 7 | phase04_in_scope_cross_119_index.md |
| A blocked rows | 42 | phase04_blocked_questions_final_for_phase04.csv |
| visual blockers union | ~15 套卷 render 相关 | phase03_laneB_visual_blockers.md |
| unread sources | 14（Batch01读了024+026；剩余约12） | phase03_laneB_source_registry.csv |
| pending suites | 4 | 见下文 |
| 推理主观题 | 全部 | phase03_laneB_reasoning_attachment.csv |
| 形式逻辑综合题 | 全部 | HS05等 |
| 选择题答案配对风险题 | 全部 | phase04_answer_key_pairing_matrix.csv |
| PPTX内嵌图片/图形批注/学生答卷图片相关题 | Q11类(推理图) | 024/052 等 |

---

## Batch 01 — P0 Gap Queue + Codex Patch 状态复核（本次执行）

### 优先执行目标

1. P0 gap queue 10 行（phase03_post_patch_gap_queue.csv）
2. Codex local patch addendum 6 行（phase03_codex_local_patch_addendum.csv）
3. Lane B focused patch 2 行（phase03_laneB_patch_addendum.csv，已为 PASS_TO_FUSION）

**Batch 01 target list**：

| target_id | suite | qno | batch01_priority |
|-----------|-------|-----|-----------------|
| Q-2024西城一模-11 | 2024西城一模 | 11 | P0/L0_BLOCKED |
| Q-2025海淀二模-12 | 2025海淀二模 | 12 | P0/B-only-BLOCKED |
| Q-2025海淀二模-13 | 2025海淀二模 | 13 | P0/B-only-BLOCKED |
| Q-2025海淀期末-2 | 2025海淀期末 | 2 | P0/L0_BLOCKED_境界 |
| Q-2025西城二模-16-2 | 2025西城二模 | 16(2) | P0/Codex-patch-verify |
| Q-2025西城二模-16-3 | 2025西城二模 | 16(3) | P0/Codex-patch-verify |
| Q-2025西城二模-7 | 2025西城二模 | 7 | P0/L0_BLOCKED |
| Q-2026丰台一模-suite | 2026丰台一模 | PENDING | P0/suite-scan |
| Q-2026朝阳期中-11 | 2026朝阳期中 | 11 | P0/Codex-patch-verify |
| Q-2026朝阳期中-13 | 2026朝阳期中 | 13 | P0/Codex-patch-verify |
| Q-2026朝阳期中-14 | 2026朝阳期中 | 14 | P0/Codex-patch-verify |
| Q-2026朝阳期中-15 | 2026朝阳期中 | 15 | P0/Codex-patch-verify |
| Q-2025海淀二模-20 | 2025海淀二模 | 20 | LOCKED_FOR_FUSION maintain |
| Q-2026丰台一模-18-2 | 2026丰台一模 | 18(2) | LOCKED_FOR_FUSION maintain |

---

## Batch 02 — A-only 76 主体批次（待执行）

已在 119 index 中标记 L1_A_ONLY_PENDING_B_TARGET 的 72 行（扣除已升级为 LOCKED_FOR_FUSION 的 2 行及 Batch01 已处理的约 6 行）进入 Batch 02。

优先顺序：
1. 推理主观题 A-only（2024西城一模 Q19 系列、2024朝阳一模 Q20/Q21、2024朝阳二模 Q16 系列等）
2. 思维主观题 A-only（高分题、待判边界题）
3. 推理选择题 A-only（批量配对）
4. 交叉/边界题

**Batch 02 中 remaining A-only 76 rows（未在 Batch01 处理的）** → 全部写入 `remaining` 队列：

包含套卷：2024朝阳一模/二模/期中、2024海淀二模、2024西城一模（其余题）、2025东城期末、2025丰台期末、2025海淀二模（其余）、2025海淀期末（其余）、2025西城二模（16(1)/17系列）、2025顺义一模、2026东城一模/期末、2026朝阳期中（其余）、2026通州期末、2026顺义一模

---

## Batch 03 — B-only 7 + visual blockers（待执行）

B-only 7 rows（从 gap queue 中抽出）：
- 2024西城一模 PENDING（主观题方向未明）
- 2024朝阳一模 主观题（创新思维 PENDING_READ）
- 2025顺义一模 主观题（PENDING_READ）
- 2026东城期末 选择题 全部（完整，B-only）
- 2026丰台一模 PENDING（suite scan blocked）
- 其余 2 行待从 gap queue 对齐

Visual blockers 专项：
- 008 renders（2025海淀二模 paper，Q12/Q13 选择题视觉）
- 042 renders（2026丰台一模 paper，全套）
- 052 renders（2026东城一模 Q19(1) 细则图片）
- 047 renders（2026东城一模 扫描版）

---

## Batch 04 — 形式逻辑综合 + 推理主观 + 剩余 pending suites（待执行）

- 2026东城期末 Q17(2)（HS05 C-boundary 形式逻辑综合）
- 4 pending suites 补读（见下文 pending_suites_patch.md）
- 剩余 unread sources（14 → 约12 after Batch01）

---

## 4 Pending Suites（Batch 03-04 目标）

| suite_id | suite | 状态 | 影响119 index |
|----------|-------|------|--------------|
| S09 | 2024西城一模 | paper=024已读；细则025未读；answer=026已读 | Q11(L0)、Q13-Q19(L1)共7+行 |
| S11 | 2024朝阳一模 | paper=030已读(partial)；细则031 PARTIAL；讲评032未读 | Q7/Q9/Q20/Q21共4行 |
| S12 | 2025顺义一模 | paper=033已读；细则034/036未读；教师版035未读 | Q3-Q7/Q10/Q17系列共7行 |
| S15 | 2026丰台一模 | paper=042 SCAN_BLOCKED；细则043 PARTIAL | Q18(2)已锁；其余choice未知 |

---

## 硬规则（Lane B 执行遵守）

- 选择题：缺完整四选项 → 不入学生稿
- 选择题：无可靠答案来源 → 不入学生稿
- 主观题：无设问/评分落点 → 不入学生稿
- 视觉未确认 → 不能 locked
- A-only 题 Codex 已写 ≠ 自动 locked
- evidence fusion 可进 → `can_enter_student_draft=no`
- 不生成学生版正文
- 不写"最终完成"
