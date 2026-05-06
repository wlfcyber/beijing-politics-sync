# Suite Report — 2026门头沟一模 (Batch04H, ClaudeCode Lane B)

## Suite Identity

- Suite name: 2026门头沟一模（北京·门头沟区2026年高三年级综合练习）
- Date processed: 2026-05-03
- Processing lane: ClaudeCode Lane B
- Run dir: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

## Source Audit

| Source | Path | Status |
|---|---|---|
| 评分细则 (P0) | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模/细则/细则.docx | OK · textutil 提取 150 行 · Q20 / Q21 段完整 |
| 试卷 (P3) | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模/试卷/试卷.pdf | OK · 已定位 · 细则示例段已含足够材料触发词 |

## Question Map

| Q | 模块 | 分值 | 处置 |
|---|---|---|---|
| 16 | 哲学 + 文化 | 8 | excluded |
| 17 | 政治与法治 | 8 | excluded |
| 18(1) | 法律与生活 | 8 | excluded |
| 18(2) | 逻辑与思维 | 7 | excluded |
| 19 | 经济与社会 | 7 | excluded |
| **20** | **当代国际政治与经济** | **7** | **candidate_for_fusion**（主目标） |
| 21 | 综合（中特+经济与社会+当代国际政治与经济） | 10（其中当代4分块） | boundary_only |

## Q20 Scoring Skeleton (验证自 P0)

```
为什么 = 原因(2) + 意义(中国2 + 世界2) + 逻辑(1) = 7 分
```

- 原因 2：四术语并列 — 对外开放基本国策 / 互利共赢战略 / 经济全球化 / 高水平对外开放
- 中国 2：4 子点任两点（贸易自由化便利化 / 产业链升级·新质生产力 / 营商环境 / 双循环联动·开放型经济新优势）
- 世界 2：4 子点任两点（市场准入·世界市场空间 / 制度型开放·高水平开放新范例 / 产业链供应链稳定 / 国际分工·开放型世界经济）
- 逻辑 1：分角度作答，逻辑连贯

## Boundary Reminders

1. 单侧封顶：只答中国侧或只答世界侧，最高 4 分。
2. 脱材封顶：完全照搬教材未结合海南封关材料，最高 5 分。
3. 高信息量术语保形：贸易自由化便利化 / 制度型开放 / 开放型世界经济 / 国内国际双循环 / 国内国际两种市场两种资源联动 / 高水平对外开放 不可压缩。
4. 原因段四术语必须并列出现（"综合运用"硬要求）。

## Atoms Produced

10 个术语/骨架原子（ATOM-MTG2026-Q20-01 至 -10）+ 1 个 Q21 边界证据登记（BOUNDARY-MTG2026-Q21-W）+ 5 个 excluded 条目，详见 `claudecode_lane/batch04H_mengtougou2026_matrix.csv` 与 `claudecode_lane/batch04H_mengtougou2026_entries.md`。

## Promotion Decisions

- **candidate_for_fusion**：MTG2026-Q20（9 术语 + 1 逻辑骨架）
- **boundary_only**：MTG2026-Q21 当代国际政治与经济 4 分块（关键词：大国担当 / 互利共赢的开放战略 / 构建人类命运共同体）
- **excluded**：Q16 / Q17 / Q18(1) / Q18(2) / Q19

## Conflicts Forwarded to Codex A

- C1：两种市场两种资源在世界意义题（2025 Q19）排除 vs. 中国意义题（2026 Q20）正面赋分 — 题型方向标签处置。
- C2：经济全球化方向句多卷同核心收敛（2025 Q19 ATOM-MT01 ↔ 2026 Q20 ATOM-06）。
- C3："高水平开放新范例"是否新开核心点 — 倾向并入"制度型开放"桶下示范子簇。
- C4：Q21 等级水平 4 分块沿用 boundary_only 规则。

详见 `claudecode_lane/batch04H_conflicts_for_codex.md`。

## Blockers

无。Q20 P0 完整可审计；Q21 boundary 处置无须补料。
