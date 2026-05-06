# 选必一触发宝典可直接讲版验收报告

## Deliverables

- Markdown：`10_teaching_rebuild_20260504/04_delivery/选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.md`
- Word：`10_teaching_rebuild_20260504/04_delivery/选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.docx`
- PDF：`10_teaching_rebuild_20260504/04_delivery/选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.pdf`
- 教师核查索引：`10_teaching_rebuild_20260504/04_delivery/选必一_触发宝典_教师核查索引_20260504.csv`
- 核心点频次：`10_teaching_rebuild_20260504/04_delivery/选必一_触发宝典_核心点频次_20260504.csv`

## Structure QA

- 主线训练题：47。
- 每题顺序检查：47/47 均为 `完整设问 -> 本题踩分点清单 -> 本题命中框架`。
- `本题踩分点清单`：47。
- `本题命中框架`：47。
- `整题汇总卷面答案`：47。
- `踩分词`标记：433 行。
- 红色踩分词/红字 run：Markdown 5159 处；DOCX XML `C00000` 5159 处。
- 重点词可见性：`制度型开放` 115；`霸权主义` 32；`强权政治` 29。
- 禁用词扫描：路径、debug/audit、GPT/Claude/Opus、candidate/guarded、证据层级、评标、参考答案、评分细则、PPTX/DOCX/PDF、fallback、source_id、atom_id 均为 0。
- 前台后台词清理：`要落到` 0；`设问要求` 0；`同槽` 0。

## Document QA

- DOCX：204,947 bytes。
- PDF：542,331 bytes，218 页。
- DOCX textutil 抽取：223,378 字；标题、制度型开放、霸权主义、强权政治、本题踩分点清单、本题命中框架均可检索。
- PDF pypdf 抽取：240,948 字；标题、制度型开放、霸权主义、强权政治、本题踩分点清单、本题命中框架均可检索。
- QuickLook DOCX 缩略图：`10_teaching_rebuild_20260504/04_delivery/quicklook_docx_触发宝典_20260504/选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.docx.png`，已人工查看首屏。
- QuickLook PDF 缩略图：`10_teaching_rebuild_20260504/04_delivery/quicklook_pdf_触发宝典_20260504/选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.pdf.png`，已人工查看首屏。
- `render_docx.py`：因本机缺少 `soffice/libreoffice` 失败，未伪称 render PASS；本轮使用 QuickLook、textutil、DOCX XML、PDF 文本与页数作为 fallback QA。

## External / Role Closure

- Claude Opus 4.7 Adaptive：真实同一 Claude 对话已捕获，见 `10_teaching_rebuild_20260504/02_external/claude_opus_teaching_rebuild_response_20260504.md`。
- GPT-5.5 Pro：本轮新增教学返工未安全提交；ChatGPT App 被 Computer Use 禁止，Safari 受跨线程护栏约束。未计 PASS，见 `10_teaching_rebuild_20260504/03_review/external_model_status_20260504.md`。
- Codex Governor：本地结构、禁用词、红字、题序、PDF/DOCX fallback QA 通过。
- Confucius：按 artifact-only 视角检查，学生可从首页读题法进入六桶，再到核心点触发和按题训练闭环；本版不替代旧 `09_delivery`，作为更像哲学/选必三宝典结构的可讲版。

## Verdict

`PASS_WITH_GPT_DELTA_PENDING`：新版触发宝典已经形成 Markdown/Word/PDF 与本地验收证据，可作为用户要求的“更接近哲学/选必三标杆的可直接讲版”。本轮没有新增 GPT-5.5 Pro 安全回执，所以不把 GPT gate 写成闭合 PASS；旧终稿仍保留不覆盖。
