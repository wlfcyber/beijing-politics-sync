# Batch04D 朝阳扩展 — Missing Sources & Blockers

generated: 2026-05-03
lane: ClaudeCode production lane B
batch: Batch04D Chaoyang

---

## BLOCKER-D1: 2025朝阳一模 Q20/Q21 — 细则.pdf 无法提取文字

**Suite:** 2025朝阳一模
**Questions:** Q20, Q21
**Impact:** 2 questions unclassifiable

**Status:** `missing_scoring_source`

**Evidence trail:**
- 主细则: `2025朝阳一模/细则/细则.pdf` (SRC_c3d1aea637c9) — 文字提取结果为空白，无法确认评分细则
- 补充材料: Q17/Q18/Q19 各有独立阅卷总结.doc（已读），但均为非选必一题目，无Q20/Q21补充评分
- 试卷: `2025朝阳一模/试卷/试卷.pdf` (SRC_832947a8c994) — 已读，提示词可见

**试卷题目提示（P3 级别仅供路由，不可作评分依据）:**
- Q20: 涉及产业链供应链、全球化相关内容（纸质阅卷提示词含选必一可能性）
- Q21: 综合题，全文无法确认是否含选必一部分

**Blocker resolution needed:** 对 `细则.pdf` 进行视觉渲染（截图/图片模式读取），确认 Q20/Q21 评分细则是否存在及内容。如视觉渲染仍为空，需查找补充材料目录。

**Codex action required:** 视觉渲染 `SRC_c3d1aea637c9` 或 `2025朝阳一模/细则/细则.pdf`；若有内容，对 Q20/Q21 重新分类并写条目；若仍空，标记为永久 `missing_scoring_source`。

---

## BLOCKER-D2: 2025朝阳期末 Q21 — 主细则.pdf 空白，P0 级别证据缺失

**Suite:** 2025朝阳期末
**Question:** Q21
**Impact:** Q21 当前以 P2 证据入库，无 P0 正式细则确认

**Status:** `in_scope` (P2) — 但 P0 来源仍未找到

**Evidence trail:**
- 主细则: `2025朝阳期末/细则/细则.pdf` (SRC_49b23fecab97) — 文字提取为空白
- 试卷: `2025朝阳期末/试卷/试卷.pdf` (SRC_131c6c890bd4) — 已读，Q21完整设问确认，参考答案为描述性（无具体评分细则）
- P2 升级来源: `2025朝阳期末/其他材料/朝阳高三期末2025.pptx` — 通过 python-pptx 提取，slide 32-34 含 Q21 详细评分结构（共5大维度，合8分，逐条有得分）

**P2 PPTX 评分结构已确认:**
- ①总分结构分 (1分)
- ②营造总体外部环境 (1分): 习近平外交思想、人类命运共同体、独立自主外交政策、和平共处五项原则、三大全球倡议
- ③营造良好外部政治环境 (2分): 世界多极化、新型国际关系、反对霸权、国际关系民主化、联合国体系
- ④营造良好外部经济环境 (2分): 推动经济全球化朝开放包容普惠平衡共赢方向（核心）、推进高水平对外开放（边界）
- ⑤营造良好外部文化舆论环境 (1分): 正确义利观、文化自信（边界：选必三）

**Blocker resolution needed:** 视觉渲染 `SRC_49b23fecab97` 或 `2025朝阳期末/细则/细则.pdf`，确认是否有 P0 细则。若存在，与当前 P2 条目核对；若仍空，保留 P2 来源，Codex A 标记为 P2 永久。

**Codex action required:** 决定是否接受 P2 PPTX 来源作为本题最终证据级别，或指示进一步搜索 P0 来源。

---

## BLOCKER-D3: 2026朝阳期末 — 细则.pdf + 试卷.pdf 全部空白

**Suite:** 2026朝阳期末
**Questions:** 全部
**Impact:** 整套试卷无法分类任何题目

**Status:** `missing_scoring_source` (整套)

**Evidence trail:**
- 主细则: `2026朝阳期末/细则/细则.pdf` (SRC_e80d35a6d904) — 文字提取为空白
- 试卷: `2026朝阳期末/试卷/试卷.pdf` (SRC_0056d930a7a9) — 文字提取为空白
- 其他材料目录: 已通过 ls 确认；其他材料目录内容未单独读取

**Blocker resolution needed:** 
1. 视觉渲染 `细则.pdf` 和 `试卷.pdf`
2. 如有其他材料（.pptx/.docx/.doc），尝试文字提取作为 P2/P0 备用证据

**Codex action required:** 对 `2026朝阳期末/` 目录内所有可视文件执行视觉渲染；如有内容，按标准分类流程处理；如仍无内容，标记整套为永久 `missing_scoring_source`，写入 suite_report 备注。

---

## 继承 Blocker（来自前序批次，本批次未解决）

以下 blocker 来自 Batch01-Batch03，本批次（Batch04D）未找到新证据，状态维持不变：

| Suite | Question | Blocker | 说明 |
|---|---|---|---|
| 2025海淀期中 | Q16(2) | P0 正式评分细则来源 | 本地视觉确认 image2.png 为评分图，但 P0 文字细则仍未文字提取 |
| 2025海淀期中 | Q21(2) | P0 正式评分细则来源 | 本地视觉确认 image8.png 为评分图，但 P0 文字细则仍未文字提取 |
| 2025海淀期末 | Q22 | P0 升级 | 当前仅 P2/P3 来源；P0 细则未找到 |
| 2024东城一模 | Q16 | 完整设问 + 细则 | 设问全文和 P0 评分细则均未确认 |
| 2024东城一模 | Q20 | P0 升级 | 已有部分信息但 P0 正式细则来源仍未确认 |
