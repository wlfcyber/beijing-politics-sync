# ClaudeCode Suite Report — Batch04G 2025门头沟一模

**Run identity**: ClaudeCode production lane B, Batch04G  
**Run directory**: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`  
**Date**: 2026-05-03

---

## Suite Overview

| Field | Value |
|---|---|
| Suite | 2025门头沟一模 |
| 政治总分 | 100分 |
| 选必一题目 | Q19（8分，四角度×2分） |
| P0 评分来源 | 细则.doc（textutil 完整提取，Q19细则可审计） |
| 试卷来源 | 试卷.pdf（pypdf提取，Q19材料和设问在第6–7页） |

---

## Question Disposition

| Question | Module | Disposition | Reason |
|---|---|---|---|
| Q16 | 文化/哲学 | excluded | 非选必一 |
| Q17 | 政治与法治 | excluded | 非选必一 |
| Q18 | 经济与社会 | excluded | 必修二模块 |
| Q19 | 当代国际政治与经济 | **promoted: candidate_for_fusion** | P0细则，四角度完整，MT01–MT04全部可审计 |
| Q20 | 法律与生活 | excluded | 非选必一 |
| Q21(1) | 逻辑与思维 | excluded | 非选必一 |
| Q21(2) | 经济与社会/综合 | no_xuanbiyi | 综合水平赋分题，无直接选必一细则评分点 |

---

## Q19 Scoring Atom Summary

**完整设问**：结合材料，运用《当代国际政治与经济》的相关知识，分析中国做"赋能型大国"的世界意义？

| Atom ID | 角度 | 桶位 | 术语核心 | 分值 | 子结构 |
|---|---|---|---|---|---|
| MT01 | 推动全球经济包容性增长 | 经济全球化 | 为世界提供广大而充满创新活力的市场；推动经济全球化朝着开放包容普惠平衡共赢方向发展 | 2分 | 1+1 |
| MT02 | 促进技术共享和民生改善 | 中国→责任 | 以科技助力发展中国家发展；为全球可持续发展贡献力量 | 2分 | 1+1 |
| MT03 | 完善全球治理实践路径 | 中国→智慧/责任 | 提供国际公共产品/贡献中国智慧中国方案；推动构建人类命运共同体 | 2分 | 1+1 |
| MT04 | 重构国际治理价值体系 | 政治多极化 | 倡导文明平等互鉴，弘扬全人类共同价值；推动国际秩序向着更加公正合理方向发展 | 2分 | 1+1 |

---

## Critical Boundary Alerts

以下三点来自细则原文，必须在学生版中保留为禁用/慎用提醒：

1. **充分利用两个市场两种资源** — 角度一明示不给分。此短语描述中国自身开放路径，不是"赋能世界"的表达。
2. **只答对中国的意义** — 细则明示不给分。学生必须写世界层面的效果，不能写"有利于中国…"。
3. **国家关系民主化、世界多极化、多边主义单独写** — 角度四明示不给分。必须落到"文明互鉴/全人类共同价值/国际秩序更公正合理"。

---

## Merge Register Flags (for Codex A)

| Flag ID | Overlap Target | Action |
|---|---|---|
| MERGE-MTG-01 | 经济全球化桶"推动经济全球化开放包容普惠平衡共赢"核心 | 补入本题场景为表述积累，不开新核心 |
| MERGE-MTG-02 | 人类命运共同体核心点 | 追加门头沟Q19"国际公共产品→HMC实践路径"为触发场景 |
| MERGE-MTG-03 | 丰台FT04"推动全球治理体制向着更加公正合理方向发展" | 补入"国际秩序"写法为表述积累 |
| MERGE-MTG-04 | 东城DC系列文明互鉴/全人类共同价值相关条目 | Codex A 核查后决定合并或新建 |

---

## Lane B Status

- Source read: **COMPLETE** (P0 细则 + P3 试卷)
- Triage: **COMPLETE** (7问全部分类)
- Entry draft: **COMPLETE** (MT01–MT04，见 batch04G_mengtougou_entries.md)
- Missing blockers: **NONE** (见 batch04G_missing_blockers.md)
- Conflicts for Codex: **4 MERGE FLAGS** (见 batch04G_conflicts_for_codex.md，无证据分歧)
- Promotion status: Q19 `candidate_for_fusion`，等待 Patcher/Governor 复核

---

## What Codex A Must Do Before Student Draft Update

1. 核查四个 MERGE 标记，决定路由（补积累 vs. 新建核心）。
2. 将 MT01–MT04 送 Patcher 复核1+1内部结构是否保留完整。
3. 将三条边界警示写入学生稿 Q19 条目的"慎用提醒"栏。
4. Governor 确认后方可将本批次条目并入 scoring_atom_table 和 merge_register。
