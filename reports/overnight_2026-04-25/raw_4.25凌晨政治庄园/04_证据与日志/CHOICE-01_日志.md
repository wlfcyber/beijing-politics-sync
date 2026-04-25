# CHOICE-01 日志

## 2026-04-25 01:55

- 读取并采用 `beijing-gaokao-politics-rubric`、`beijing-politics-analyst` 的选择题证据规则。
- 写入边界确认：只写 `CHOICE-01_2026与2025选择题错肢.md` 和 CHOICE-01 必要日志/抽取文件；不覆盖其他线程文件。
- 已生成 CHOICE-01 自有抽取目录：`C:\Users\Administrator\Desktop\4.25凌晨政治庄园\04_证据与日志\CHOICE-01_extracts`
  - `MANIFEST.tsv`：2025/2026 可读 PDF、DOCX、PPTX 抽取清单。
  - `ANSWER_CANDIDATES.tsv`：自动检出的客观答案候选片段。
  - `KEY_LEDGER_CANDIDATES.tsv`：按套卷整理的 15 项答案候选/待复核/缺口台账。
- 已生成重点缺口末页渲染图：`C:\Users\Administrator\Desktop\4.25凌晨政治庄园\04_证据与日志\CHOICE-01_rendered_pages`
  - `2026_Fengtai_Yimo_page8.png` 至 `page10.png`
  - `2026_Fangshan_Yimo_page9.png` 至 `page11.png`
  - `2026_Fengtai_Qimo_page7.png` 至 `page9.png`
- 人工核验结论：
  - `2026丰台一模`：试卷末页仍为主观题；细则 PPT 为主观题阅卷说明，未见选择题答案表。
  - `2026房山一模`：试卷末页仍为主观题；细则 docx 为主观题评分细则，未见选择题答案表。
  - `2026丰台期末`：试卷末页仍为主观题；细则 PDF 为主观题讲评/评标，未见选择题答案表。
- 已完成最小闭环一：`2026东城期末` 15 道选择题，客观答案来自教师版试卷答案表，已整理错肢、错误类型、原因、规范改写、可脱离材料判断、同类合并和回填提醒。
- 已完成最小闭环二：`2026朝阳一模` 15 道选择题，教师版试卷题干与答案表均可抽取，答案为 `B A D B D D C A C C B A B C C`，已追加错肢库。
- 推进中发现：
  - `2026海淀期末`：可抽出答案表，但题干页为无文本层扫描页，暂不入库，需 OCR/读图。
  - `2026西城期末`：可抽出答案表，但题干页为无文本层扫描页，暂不入库，需 OCR/读图。

## 待继续

- 下一批建议处理：`2026朝阳期中`、`2026海淀期中`、`2026石景山一模`，这些已确认题干文本可读。
- 所有 `KEY_LEDGER_CANDIDATES.tsv` 中 `NO_KEY_CANDIDATE` 和 `NEEDS_MANUAL_REVIEW` 项，未逐题复核前不得入库。
