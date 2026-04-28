# OCR-needed 漏项回收审计 · S001 · 2024 东城一模

- 复核者：ClaudeCode（v5 cache-first 重启）
- 复核日期：2026-04-29
- 工作目录：`C:\bp_sync_visible`
- 资料包：`C:\bp_sync_visible\cloudcode\s001_windows_package`
- 输出目录：`C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28`

---

## 1. 复核证据来源（cache-first）

| 来源 | 路径 | 用途 |
|---|---|---|
| 套卷打包说明 | `cloudcode/s001_windows_package/suite_bundle.md` | 来源元数据、PDF/PPTX hash、转写状态 |
| 细则原始 PPTX 文本 | `cloudcode/s001_windows_package/rubric_text.txt` | 细则原文（pptx-xml 提取，9254 字符） |
| 细则 GPT-readable | `cloudcode/s001_windows_package/rubric_source.md` | 同上文本的 markdown 包装版 |
| 试卷分页图（10 页） | `cloudcode/s001_windows_package/paper_pages/page_001..012.png` | 787×1106，单图 ≤2000px |
| 答案分页图（1 页） | `cloudcode/s001_windows_package/answer_pages/answer_page_001.png` | 1574×1106，单图 ≤2000px |
| 本轮生成裁切图 | `cloudcode/s001_windows_package/crops_v5/*.png` | 答案表/页 1/2/3/4/5/6/9 顶底裁切，全部 ≤2000px |

未使用的来源（均符合任务禁止项）：
- 未读取 `reports/ocr_rerun_windows_2026-04-28`（Codex 临时审计草稿，禁用）
- 未读取旧 `final_deliverables` 或旧 `artifacts`
- 未把 `visible_runs/claude_ocr_rerun_S001_windows_stream_v4.jsonl` 当作题面/答案证据
- 未读取 `hires_pages/answer_p01.png`、`answer_top_zoom.png`、`answer_bot_zoom.png`、`answer_subj_left_top.png` 等 >2000px 的高分辨率图（包内未提供，本身也已被任务禁止）

底层原始文件（仅在缓存不足时备查，本轮未直接打开）：
- 试卷 PDF：`C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\试卷\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治试卷(1).pdf` （sha256 `74cdfac9253763bf12c9443d036ebbeab12693ba7015a2f335d19ccfcab6d96b`）
- 答案 PDF：`...\其他材料\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治答案(1).pdf` （sha256 `7b4eece2963205d8ac02ef13063307a3dad70cf6542b6169f3ed34276f16e115`）
- 细则 PPTX：`...\细则\2024东城一模细则.pptx` （sha256 `4b2073bcc9e26f626b49b66dd6e0c64ec93650292d50719806830d7aea9fa3ce`）

---

## 2. 图片读取合规

任务限制：
1. 不读宽或高 > 2000px 的图片。
2. 不读 hires_pages 系列、answer_top_zoom 等指定大图。
3. 不在同一轮工具调用中读 > 4 张图片。

合规情况：
- `paper_pages/page_001..012.png`：787×1106；本轮分批读取，每轮 ≤4 张。
- `answer_pages/answer_page_001.png`：1574×1106；先整页读，再生成 553-tall 子裁切。
- `crops_v5/*`：本轮自行生成的 553-tall（或 1106-tall × 530/1044-wide）裁切，单图均 ≤2000px。
- 所有读图调用按 4 张/轮上限分批，未触发 many-images 上限。

包内未提供任务说明里列举的官方 crops 目录（`crops/answer_page_001_top.png` 等不存在）。本轮自行生成 `crops_v5/`，依然遵守 ≤2000px、≤4 张/轮 的限制。

---

## 3. 题号 ↔ 模块归属 ↔ 证据来源

### 3.1 客观题（共 15 题，每题 3 分）

| 题号 | 答案 | 证据图（题面） | 证据图（答案键） | 模块 | 必修四相关性 |
|---|---|---|---|---|---|
| 1 | C | `paper_pages/page_001.png`（整页）+ `crops_v5/p01_top.png` `crops_v5/p01_bot.png` | `crops_v5/ans_left.png` 第一行 | 必修1 + 必修3 国际 | 错项①含中华民族精神边界，仅边界辨析素材 |
| 2 | B | `crops_v5/p01_bot.png` | `crops_v5/ans_left.png` | 必修四 文化 | ✓ 主索引 |
| 3 | A | `crops_v5/p02_top.png` | `crops_v5/ans_left.png` | 必修四 哲学+文化 | ✓ 主索引 |
| 4 | A | `crops_v5/p02_top.png` `crops_v5/p02_bot.png` | `crops_v5/ans_left.png` | 必修3 政治与法治 | — |
| 5 | D | `crops_v5/p02_bot.png` | `crops_v5/ans_left.png` | 必修3 政治与法治 | — |
| 6 | D | `paper_pages/page_003.png` | `crops_v5/ans_table.png` | 选修3 逻辑与思维 | — |
| 7 | A | `paper_pages/page_003.png` | `crops_v5/ans_table.png` | 选修3 逻辑与思维 | — |
| 8 | D | `paper_pages/page_003.png` | `crops_v5/ans_table.png` | 选修3 逻辑与思维 | — |
| 9 | B | `paper_pages/page_003.png` | `crops_v5/ans_left.png` | 选修2 法律与生活 | — |
| 10 | C | `crops_v5/p04_top.png` | `crops_v5/ans_left.png` | 选修2 法律与生活 | — |
| 11 | A | `crops_v5/p04_top.png` `crops_v5/p04_bot.png` | `crops_v5/ans_left.png` | 必修3 政治与法治 | — |
| 12 | B | `crops_v5/p04_bot.png` | `crops_v5/ans_left.png` | 必修2 经济与社会 | — |
| 13 | D | `crops_v5/p05_top.png` | `crops_v5/ans_left.png` + `crops_v5/ans_table.png` | 必修2 经济与社会 | — |
| 14 | C | `crops_v5/p05_top.png` | `crops_v5/ans_table.png` | 必修1 + 国际 | — |
| 15 | C | `crops_v5/p05_bot.png` | `crops_v5/ans_table.png` | 必修四 哲学 | ✓ 主索引 |

> 答案表证据：从 `crops_v5/ans_table.png` 与 `crops_v5/ans_left.png` 双图核对得出
> | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
> | C | B | A | A | D | D | A | D |
> | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
> | B | C | A | B | D | C | C |

### 3.2 主观题（共 6 题，55 分）

| 题号 | 分值 | 题干模块限定（证据） | 材料证据 | 答案证据 | 必修四相关性 |
|---|---|---|---|---|---|
| 16 | 7 | 限定《哲学与文化》（`crops_v5/p06_bot.png`） | `paper_pages/page_006.png` + `crops_v5/p06_top.png` `crops_v5/p06_bot.png` | `rubric_text.txt` 16题阅卷细则 + 16题答案示例 + `crops_v5/ans_left.png` 等级表 + `rubric_source.md` 行 53–62 | ✓ 主索引 |
| 17 | 7 | 限定"经济和法治的角度"（`crops_v5/p06_bot.png`） | `paper_pages/page_006.png` 的资料卡 | `crops_v5/ans_left.png` 17题 + `rubric_text.txt` "是何 2分 / 影响 2分 / 措施 3分" | — |
| 18(1) | 8 | 限定《经济与社会》（`paper_pages/page_007.png`） | `paper_pages/page_007.png` 北京新质生产力图表 | `crops_v5/ans_left.png` + `crops_v5/ans_r_q1.png` 18(1) 优势+如何助力 | — |
| 18(2) | 6 | 题干"分析政协…作用"（`paper_pages/page_008.png`） | `paper_pages/page_008.png` 甲乙丙地政协调研 | `crops_v5/ans_r_q1.png` 18(2) 政协 6分 | — |
| 18(3) | 6 | 限定《逻辑与思维》（`paper_pages/page_008.png`） | `paper_pages/page_008.png` 传统产业与未来产业 | `crops_v5/ans_r_q1.png` 18(3) 是何/如何 + `rubric_text.txt` "理论+分析 3+3" | 模块边界，不入必修四 |
| 19 | 6 | 限定《法律与生活》（`crops_v5/p09_top.png`） | `crops_v5/p09_top.png` 案件1+案件2+资料卡 | `crops_v5/ans_r_q1.png` 19题 6分 + `rubric_text.txt` 法律理论+实践逻辑 | — |
| 20 | 8 | 限定"经济的相关知识"（`crops_v5/p09_bot.png`） | `crops_v5/p09_bot.png` 内循环+外循环材料 | `crops_v5/ans_r_q1.png` `crops_v5/ans_r_q2.png` 20题 4选3+起点措施+路径+效果 | — |
| 21 | 7 | "运用所学"（`paper_pages/page_010.png`） | `paper_pages/page_010.png` 通勤圈+功能圈+产业圈 | `crops_v5/ans_r_q2.png` 21题等级表 + `rubric_text.txt` 三圈四角度 + 示例 | ✓ 哲学触发主索引 |

> 第 18 题为大题型 20 分共 3 问。题干"运用《逻辑与思维》知识"明确限定第(3)问为选修3，是把这部分排除出必修四的硬证据。
> 第 21 题为综合"运用所学"，但本套官方细则示例用了"以人民为中心""系统优化""新发展理念""比较优势"等必修四哲学/经济交叉触发点，可纳入必修四哲学方法论训练。

---

## 4. 必修四主索引最终落点

- 客观题主索引：第 2、3、15 题
- 客观题边界辨析素材：第 1 题错项①
- 主观题主索引：第 16 题（题干硬限定 7 分）
- 主观题哲学方法论训练：第 21 题（细则触发 7 分）

合计 必修四主索引分值：客观 9 分 + 主观 14 分 = 23 分（占全卷 23%）。

---

## 5. 旧条目处置建议（与 RESULTS 文件呼应）

- 旧条目把第 18(3) 列入必修四《哲学与文化》——降级为"概念交叉示例"，标注题干限定为选修3《逻辑与思维》。
- 旧条目把第 17、19、20 题列入必修四——删除。
- 旧条目把第 1 题作为必修四主索引——降级为"中华民族精神/根与魂"边界辨析素材。

## 6. 证据缺口与待办

- 第 17 题答案在 `crops_v5/ans_left.png` 仅完整显示前半部分；后半部分（"维护公平公正的市场竞争秩序，创新监管方式，引导经营者有序规范投放"）已通过 `rubric_text.txt` 的"参考答案"段补全。两源一致，无冲突。
- 第 18(1) 关于"图表数据 36.7% / 136.8%"已通过 `paper_pages/page_007.png` 直接读出；图表本身分辨率较低，但"教育人才优势/研发投入持续增长/数字经济/科技体制改革"四个优势点在 `rubric_text.txt` "优势：…(2分)" 段被官方细则锁定，结论可靠。
- 第 21 题等级评分细则在 `rubric_text.txt` 与 `crops_v5/ans_r_q2.png` 等级表两处一致出现，无冲突。
- 未来若需高分辨率核对，可重新渲染 PDF（保持每页宽 ≤2000px）后再做单题深读。本轮在现有约束下已经回收所有必修四证据链。

## 7. 失败原因记录（v4 → v5）

- v4 失败：`visible_runs/claude_ocr_rerun_S001_windows_stream_v4.jsonl` 中读取了高分辨率答案图（>2000px），触发 many-images 请求限制，未产出正文。该文件本轮仅作"失败原因记录"参考，不作为题面/答案证据。
- v5 修复：本轮全程使用 ≤2000px 的页面图与自生成 ≤2000px 的子裁切图，每轮工具调用图片数 ≤4，正文已完整生成。

## 8. 输出三件套清单

- 学生可读正文：`reports/ocr_rerun_claudecode_2026-04-28/S001_2024东城一模.md`
- 回收结论：`reports/ocr_rerun_claudecode_2026-04-28/OCR_RERUN_RESULTS.md`
- 复核审计（本文件）：`reports/ocr_rerun_claudecode_2026-04-28/OCR_RERUN_AUDIT.md`
