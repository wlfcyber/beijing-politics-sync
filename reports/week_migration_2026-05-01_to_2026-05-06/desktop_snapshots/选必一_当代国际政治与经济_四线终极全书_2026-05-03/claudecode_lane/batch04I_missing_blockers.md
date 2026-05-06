# Batch04I Missing / Blockers — 2026丰台一模

## Status: 无阻塞

## Source Inventory

| 资源 | 路径 | 状态 |
|---|---|---|
| PPTX 细则/参考答案 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx | 已解压；Q19 命中 slide41/42/43–47/48；试题分析 + 8 分参考答案 + 典型示例 + 学生问题及建议齐全 |
| 试卷 PDF | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/试卷/试卷.pdf | Codex A 已渲染 → 02_extraction/visual_renders/batch04I_fengtai2026_paper/page_01..10.png；Q19 在 page_08，材料触发词可读 |

## Source-Grade Caveat（重要，非缺料）

- PPTX **不含逐点赋分细则**（无"X 分=Y 子点"切分），系本卷 PPTX 固有结构；
- 已按 `P0_scoring_pptx_reference_answer_guarded` 处置，不视为 missing，**无须等待补料**；
- 若后续从其他渠道（如官方阅卷会纪要、教研组细则文档）拿到 Q19 标准 P0 细则，可触发一次重处理（rerun batch04I），并将 promotion_status 由 `candidate_for_fusion_guarded` 升级为 `candidate_for_fusion`。

## Items to Watch（非 blocker，仅观察）

1. PPTX slide43–47 标题为"三、典型示例"但正文体多为图片（OCR 后多为空文本），未抓到典型示例书面作答；如后续需要"高分样卷术语对齐"，可向 Codex A 申请 slide43–47 图层的视觉渲染。当前不影响术语原子产出。
2. PPTX slide49 引"五、复练试题：2025年丰台一模"，2025丰台一模 Q19 已在 batch04F 处理，本批次不再重复登记。
