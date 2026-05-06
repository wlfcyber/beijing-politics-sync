# Unresolved Blockers

## Active

- HS02 2025 海淀二模 Q20 原卷文本层不可用，仅 168 chars；已做页面渲染视觉核读，但必须等待第二视觉/模型审稿 pass 独立确认后才能进入最终学生稿。
- top-level `SOURCE_LEDGER.csv` 当前仍含旧选必三产物定位行；它只能暂作搜索定位，不可作为最终证据登记表。最终需要用 `01_source_inventory/A_source_registry_phase02.csv` 和后续逐套原始源扫描重写/替换。
- 2026 二模源文件在本轮已扫描根目录中暂未发现；不能写“2026 二模覆盖完成”。
- 全书逐套逐题 coverage 尚未开始，当前 `COVERAGE_MATRIX.csv` 只记录五个硬样本。
- HS02 的 scoring structure 已由主细则、讲评 PDF、评标实录三源锁定为“三个角度选两个，每角度1+2”；不再把“答案正文缺失”作为硬阻塞，但仍需最终学生表达前的视觉核题。
- 学生稿、Opus 成文化、Word/PDF 交付、最终 PASS 均被 GPT-5.5 Pro 当前 gate 禁止。

## Tool Gaps With Workarounds

- Missing: `pdftotext`, `pdftoppm`, `soffice`, `tesseract`, `ocrmypdf`, ImageMagick.
- Working: PyMuPDF, PIL, python-docx, python-pptx, `textutil`, `qlmanage`, `sips`.
- Rule: tool gaps must trigger fallback processing, not abandonment.
