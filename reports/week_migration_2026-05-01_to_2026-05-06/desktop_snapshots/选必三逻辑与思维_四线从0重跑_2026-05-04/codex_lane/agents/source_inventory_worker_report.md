# Codex Lane Source Inventory Worker Report

角色：Codex 内部源材料盘点 worker  
时间：2026-05-04  
范围：选必三《逻辑与思维》思维部分 + 推理部分  
写入边界：本轮只写本文件与 `01_source_inventory/source_scan_notes.md`；未修改 `SOURCE_LEDGER.csv`、学生版或其他 lane 文件。

## 已读取规则源

- `MASTER_REQUIREMENTS.md`
- `USER_FRAMEWORK.md`
- `00_control/NOTEBOOK_DIGEST.md`
- `feige-politics-garden-xuanbisan` 硬规则笔记本

执行口径：

- 旧选必三稿、旧双线/四线跑产物、选必一/选必二缓存只能作定位线索，不作为本轮证据。
- 主观题必须回到原试卷 + 细则/评标/阅卷/讲评给分口径。
- 选择题必须回到原题面 + 可靠客观答案源；不得从旧稿或解释反推答案。
- 推理部分本轮纳入盘点，但要单独成章，不能并入思维主链。
- `2026石景山期末` 位于 `/Users/wanglifei/Desktop/2026模拟题/已放弃/2026石景山期末`，按硬规则排除，除非用户另给新评分来源。

## Source Roots 扫描边界

本轮扫描了用户指定 5 个 source roots：

| root | 本轮扫描状态 | 原始政治材料数量 |
|---|---:|---:|
| `/Users/wanglifei/Desktop/北京高考政治` | 已扫；主要发现旧稿、旧跑缓存、索引和本轮空 ledger | 不计入原始区卷数量 |
| `/Users/wanglifei/Desktop/2024模拟题` | 已扫 | 65 |
| `/Users/wanglifei/Desktop/2025模拟题` | 已扫 | 61 |
| `/Users/wanglifei/Desktop/2026模拟题` | 已扫 | 50 |
| `/Users/wanglifei/GaokaoPolitics/2025各区模拟题` | 已扫；与 Desktop 2025 部分镜像/补充 | 61 |

四个非项目 source roots 合计发现 `237` 个政治试卷/答案/细则/讲评类 PDF/Word/PPT/RTF 文件。

2026 新材料状态：

- `/Users/wanglifei/Desktop/2026模拟题/2026各区一模` 下已存在东城、丰台、延庆、房山、朝阳、海淀、石景山、西城、门头沟、顺义一模。
- `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中` 下已存在东城期末、丰台期末、朝阳期中、朝阳期末、海淀期中、海淀期末、西城期末、通州期末。
- 本轮 source roots 未发现 `2026各区二模` 目录；只能记录为“本轮未发现”，不能写成客观考试事实。

## 关键文件类别

### A. 可直接使用的原始区卷材料

这类是后续提取优先回源对象，可直接用于题面、答案源、细则源核验。

- 试卷：各区 `试卷/试卷.pdf` 或 `试卷/试卷.docx`。
- 细则：各区 `细则/细则.pdf`、`细则/细则.docx`、`细则/细则.pptx`、分题细则 PPT/Word。
- 补充评分材料：`评标`、`阅卷总结`、`阅卷报告`、`讲评`、`参考答案—评分细则`。
- 2024 一模分类汇编：`/Users/wanglifei/Desktop/2024模拟题/202404各区一模试题分类（按模块）/2024届各区一模试题分类汇编选必3.doc` 只能作定位和去重辅助，不是独立证据。

### B. 本轮必须重点回源的思维部分候选

优先级来自本轮扫描 + 旧跑定位线索，仍需逐题回原始试卷/细则确认。

| 套卷 | 题源类型 | 原始源材料 |
|---|---|---|
| 2026顺义一模 | 科学思维硬样本；主观题候选 | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/细则/细则.pptx` |
| 2026朝阳期中 | 创新思维复合题硬样本；主观题候选 | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/细则.docx`; `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/补充材料/细则.docx` |
| 2026通州期末 | 思维抽象与思维具体选择题硬样本；推理/形式逻辑边界也需扫 | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/细则/细则.pptx` |
| 2025海淀二模 | 辩证思维复合题硬样本；讲评/评标补充 | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/细则.docx`; `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/补充材料/2025年海淀二模评标实录.docx`; `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/其他材料/2025届二模考试讲评0510.pdf` |
| 2025东城期末 | 创新思维/登月服候选 | `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025东城期末/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025东城期末/细则/细则.pdf`; `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025东城期末/细则/补充材料/东城期末.pptx` |
| 2025海淀期末 | 创新思维/公共文化空间候选 | `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期末/试卷/试卷.docx`; `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期末/细则/细则.pptx` |
| 2024朝阳期中 | 创新思维/推理混合硬样本 | `/Users/wanglifei/Desktop/2024模拟题/2024朝阳期中/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳期中/细则/细则.docx`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳期中/细则/补充材料/2024.11期中政治朝阳评标2.docx`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳期中/细则/补充材料/细则.rtf` |
| 2024朝阳二模 | 辩证思维/类比推理候选 | `/Users/wanglifei/Desktop/2024模拟题/2024朝阳二模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳二模/细则/细则.pdf`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳二模/细则/补充材料/细则.docx` |
| 2024西城一模 | 超前思维/未来产业候选 | `/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx`; `/Users/wanglifei/Desktop/2024模拟题/西城一模/细则/细则.docx`; `/Users/wanglifei/Desktop/2024模拟题/西城一模/细则/补充材料/2024.4高三统一测试思想政治答案.docx` |
| 2024海淀二模 | 思维抽象与思维具体/调查研究候选 | `/Users/wanglifei/Desktop/2024模拟题/海淀二模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2024模拟题/海淀二模/细则/细则.docx`; `/Users/wanglifei/Desktop/2024模拟题/海淀二模/细则/补充材料/高三二模：政治答案(2).docx` |

### C. 本轮必须重点回源的推理部分候选

| 套卷 | 推理方向 | 原始源材料 |
|---|---|---|
| 2024朝阳一模 | 三段论、逻辑三律、假言推理讲评候选 | `/Users/wanglifei/Desktop/2024模拟题/2024朝阳一模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳一模/细则/细则.pptx`; `/Users/wanglifei/Desktop/2024模拟题/2024朝阳一模/其他材料/202404朝阳高三政治一模试卷讲评.pptx` |
| 2024朝阳期中 | 楚王/晏子推理，类比/假言/三段论误答 | 同上 B 表中朝阳期中原始材料 |
| 2025顺义一模 | 假言判断、相容选言判断、推理条件 | `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025顺义一模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025顺义一模/细则/细则.docx`; `/Users/wanglifei/GaokaoPolitics/2025各区模拟题/2025各区一模/2025顺义一模/2025北京顺义高三一模政治（教师版）.pdf`; `/Users/wanglifei/GaokaoPolitics/2025各区模拟题/2025各区一模/2025顺义一模/顺义区2025届高三第一次模拟考试参考答案—评分细则.docx` |
| 2025西城二模 | 充分条件假言判断/推理规则 | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025西城二模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025西城二模/细则/细则.docx`; `/Users/wanglifei/GaokaoPolitics/2025各区模拟题/2025各区二模/2025西城二模/讨论定稿-答案细则 -25.5西城高三政治二模-1.docx` |
| 2025丰台期末 | 判断保真条件、必要条件假言判断 | `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025丰台期末/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025丰台期末/细则/细则.pptx` |
| 2026丰台一模 | 必要条件假言推理 + 三段论错误；评标细则强 | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx` |
| 2026东城期末 | 三段论、必要条件假言、充分条件假言边界；硬样本 Q17(2) 需核 | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/细则/细则.pptx` |
| 2026东城一模 | 换质位/选言/形式逻辑候选；另有分题评标 PPT | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/试卷/试卷.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/试卷/补充材料/2026东城一模 原卷扫描版.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/细则/细则.pdf`; `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/细则/分题细则/东城一模评标细则（勿传）/*.pptx` |

## 可直接使用的原始 PDF / Word / PPT

后续 worker 可优先从这些原始文件抽题，不必先看旧稿：

- 2024 原始卷与细则：`2024东城一模`、`2024朝阳一模`、`2024朝阳二模`、`2024朝阳期中`、`2024海淀一模`、`2024海淀二模`、`东城二模`、`丰台一模/二模`、`西城一模/二模`、`顺义思政二模`。
- 2025 原始卷与细则：Desktop 版 `2025各区一模/二模/期末`，GaokaoPolitics 版同名目录可作为镜像/补充；若两处同套文件冲突，需以路径、文件名、页码和实际内容重新裁定。
- 2026 原始卷与细则：`2026各区一模` 全部现有区卷；`2026各区期末和期中` 下现有期中/期末卷。
- 分题细则优先级高：如 `2026东城一模/细则/分题细则/东城一模评标细则（勿传）/*.pptx`、`2025丰台二模/细则/分题细则/.../*.docx`、`2024东城二模/细则/分题细则/阅卷总结/...`。

## 需要回源验证的缓存 / 旧稿索引

以下可用于快速定位，但不得直接作为本轮证据：

- `/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_框架+三年题链_穷尽版.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_逐题材料-思维路径积累_穷尽版.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_零基础满分课稿.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维双线四线终极跑_2026-05-04/01_source_inventory/*.md|*.csv`
- `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维双线四线终极跑_2026-05-04/02_extraction/priority_source_texts/*.txt`
- `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维双线四线终极跑_2026-05-04/03_entries/*candidate_shortlist*`
- `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/preprocess_v2_2026-05-03/text_cache/*.txt`
- `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/02_extraction/full_source_text_cache_20260503/*.txt`

这些缓存的价值：

- 能提示可能的套卷、题号、关键词和源路径。
- 能暴露旧稿/旧缓存中混入选必一、选必二、哲学、文化、法律材料的噪声。
- 不能替代本轮对原 PDF/Word/PPT 的页面、题号、设问、答案和细则核验。

## 明显 Blocker

1. 当前本轮 `01_source_inventory/SOURCE_INVENTORY.csv` 与 `01_source_inventory/FILE_TYPE_ROUTING.csv` 只有表头；本 worker 按用户边界未修改 CSV，后续 ledger worker 需要补正式行。
2. PDF 提取质量不稳定：旧跑 manifest 显示部分 PDF 抽取字符很少，例如 `2025海淀二模/试卷/试卷.pdf` 抽取仅 94 chars、`2024东城一模/试卷/试卷.pdf` 抽取仅 145 chars、其答案 PDF 仅 10 chars；这些必须渲染/OCR 或视觉核验。
3. 旧跑缓存命中数很大但噪声高：候选表里混有选必一、选必二、必修四、法律、经济材料，必须按设问模块和评分术语过滤。
4. `2024届各区一模试题分类汇编选必3.doc` 是分类汇编，不是独立套卷；只能帮助定位，不能重复计数。
5. GaokaoPolitics 与 Desktop 2025 目录存在同套镜像/补充；需去重并记录 canonical source。
6. 讲评 PPT/PDF 若只有普通讲解而无明确给分口径，只能作为 `A-support` 或定位线索；不得升为正式细则。
7. 推理题大量属于选择题或形式逻辑规则识别；本轮要纳入推理章，但不能污染“思维方法触发链”主链。
8. `2026石景山期末` 已在已放弃目录，且硬规则要求排除。

## 下一 worker 建议

- 先建立正式 `SOURCE_LEDGER.csv` / `COVERAGE_MATRIX.csv` 行，再逐套回源。
- 每套卷先判定：题面是否明确《逻辑与思维》、答案/细则是否匹配、题号是否稳定、是否思维主观题/推理题/选择题/边界题。
- 对 PDF 抽取低字符量的源，优先渲染页图或 OCR，避免用空文本判断缺题。
- 对 2026 新卷不要继承旧时间口径；本轮已确认有 2026 一模和期中/期末材料，但未发现 2026 二模目录。
