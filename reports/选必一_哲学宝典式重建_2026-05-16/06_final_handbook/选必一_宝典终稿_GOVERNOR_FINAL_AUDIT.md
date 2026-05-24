# 选必一宝典终稿 GOVERNOR FINAL AUDIT

审计时间：2026-05-24

## Governor 判定

WEAK_PASS：正文与导航本体 PASS；页面视觉渲染 QA 已补齐；GPT Pro 终稿复核仍未闭合。

当前学生厚版与考前导航版本体已达到“哲学宝典式”的可交付标准：核心点按教材模块与评分术语分桶，题例按来源题独立呈现，频次与题例数同步，边界题不硬塞主链。页面图片渲染 QA 已在安装 LibreOffice 后通过等效 DOCX -> PDF -> PNG 链路补齐。仍未闭合的是 GPT Pro 终稿复核：该项受 Chrome profile/扩展接管问题阻塞，不能声明 GPT Pro 已审核通过。

## 最终交付文件

- 学生厚版 Markdown：`reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_学生版.md`
- 学生厚版 Word：`reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_学生版.docx`
- 考前导航版 Markdown：`reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md`
- 考前导航版 Word：`reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_考前导航版.docx`

## 最新结构统计

| 项目 | 数量 |
|---|---:|
| 核心答题点 | 138 |
| 主链题例 | 373 |
| 边界附录题例 | 7 |
| 总题例 | 380 |
| 频次不一致 | 0 |
| 疑似多题合并题例标题 | 0 |
| 题例序号不连续 | 0 |
| 导航核心点行 | 138 |
| 导航边界提示行 | 7 |
| 导航总数据行 | 145 |

字段完整性：`【什么时候写】`、`【设问】`、`【为什么能想到】`、`【卷面句】`、`【同题组】` 均为 380 次。

DOCX 结构：

- 学生版 DOCX：Heading 1 = 8；Heading 2 = 152；Heading 3 = 380。
- 考前导航版 DOCX：Heading 2 = 8；表格 18 个；表格行 163 行。

## 全桌面覆盖闭合

已覆盖桌面 `2024各区模拟题`、`2025各区模拟题`、`2026各区模拟题` 的选必一主观题候选。机械候选表给出的 `absent` 不直接等于漏题；最终以题面、答案、细则/评标/讲评上下文是否形成选必一主链评分价值为准。

本轮关键闭合：

- 2025东城二模Q20、2025朝阳二模Q21、2026西城一模Q20(2)的共同利益条目已补入“国家间共同利益是国家合作的基础”。
- 2026石景山期末Q19(2)人工智能全球治理已按源文本补入 7 个明确支持节点：和平发展时代潮流、共同利益、人类命运共同体、多边主义、共商共建共享、国际秩序公正合理、中国方案。
- 2026石景山期末Q19(2)未挂入“新型国际关系”，因为源文本没有出现该细则术语。
- 2025丰台一模Q21、2025门头沟一模Q20、2025海淀期末Q16、2026房山一模Q20 已作为边界提示，不进入主链频次。
- 2024顺义二模Q18已回源到正式细则，主线为《政治与法治》人民代表大会制度、国家机关协调高效运转、全过程人民民主，未给出选必一主链评分点，因此不进入主链，也不进入边界附录。

## 反合并判定

当前终稿没有发现两个不同来源题合并成一个 `###` 案例。允许同一道来源题因多个评分角度分别挂入多个核心点；不允许把两道来源题压成一个案例。本轮 QA 脚本对标题层做了合并题例扫描，结果为 0。

题例序号已按每个核心答题点内的独立题例顺序重新排列；本轮 QA 脚本新增序号连续性检查，结果为 0。

## 页面渲染 QA

页面渲染 QA 已闭合。`render_docx.py` 在 Windows 上直接调用仍受 `soffice.exe` 挂起和 `-env:UserInstallation=file://C:\...` 路径兼容问题影响；本轮改用同等验收链路：ASCII 临时 DOCX 文件名 -> `soffice.com` 导出 PDF -> PyMuPDF/fitz 1.27.2.3 渲染 PNG。

| 文档 | PDF 大小 | PNG 页数 | PNG 尺寸 | 空白/近空白页 |
|---|---:|---:|---|---:|
| 学生厚版 | 3,996,805 bytes | 200 | 1275 x 1650 | 0 |
| 考前导航版 | 899,425 bytes | 20 | 1754 x 1241 | 0 |

已查看学生厚版 10 张 contact sheet 覆盖 p1-p200、导航版 1 张 contact sheet 覆盖 p1-p20，并抽查原尺寸页图：学生版 p1、p28、p100、p199；导航版 p5、p20。未发现空白页、整页裁切、明显重叠、表格溢出或页脚异常。

## 外部审核记录

- ClaudeCode Opus 对 43 条机械 absent 候选做三分法 triage，原始文件：`12_full_desktop_extract_20260524/XUANBIYI_ABSENT43_TRIAGE.md`。
- 本地回源后的 triage 校正：`12_full_desktop_extract_20260524/XUANBIYI_ABSENT43_TRIAGE_POSTCHECK_20260524.md`。
- Claude Opus 覆盖补丁后只读复核：`12_full_desktop_extract_20260524/CLAUDE_OPUS_FINAL_QA_AFTER_COVERAGE_PATCH.md`。结论：正文和导航本体 PASS，旧审计文件需去除旧数字。
- Claude Opus 文档修复后只读复核：`12_full_desktop_extract_20260524/CLAUDE_OPUS_FINAL_QA_AFTER_DOC_FIX_20260524.md`。结论：正文和导航本体 PASS；指出 Governor 文件旧数字仍需同步。本文件即为同步后的最终 Governor 审计。
- 独立 agent 完成性复核：`12_full_desktop_extract_20260524/AGENT_FINAL_COMPLETION_AUDIT_20260524.md`。结论：正文与导航本体 WEAK_PASS；未发现合并题例或明显错误归类；指出 GPT Pro、页面渲染、旧覆盖审计口径和题例序号问题。本轮已修复旧覆盖审计口径、题例序号问题，并补齐页面渲染 QA。
- ClaudeCode Opus 4.7 终稿完成性复核：`12_full_desktop_extract_20260524/CLAUDECODE_OPUS47_FINAL_COMPLETION_AUDIT_20260524.md`。结论：正文与导航本体 PASS，2024-2026 覆盖闭合 PASS，反合并 PASS；当时整体仍为 WEAK_PASS，原因是 GPT Pro 复核与页面渲染 QA 未闭合。本轮之后页面渲染 QA 已补齐，GPT Pro 仍未闭合。
- GPT Pro 终稿复核：`12_full_desktop_extract_20260524/GPT_PRO_FINAL_REVIEW_BLOCKED_20260524.md`。当前为 blocked，不能写入“已通过”证据链。

## QA 与脚本

- `scripts/apply_xuanbiyi_coverage_fixes_20260524.py`：回填主链/边界并重建导航。
- `scripts/qa_xuanbiyi_final_handbook_20260524.py`：核验核心点、题例数、频次、字段完整性、合并题例标题、题例序号连续性、DOCX 结构。
- `06_final_handbook/WORD_REBUILD_QA_20260524_FREQUENCY_COVERAGE.md`：Word 重建与结构 QA。
- `06_final_handbook/WORD_RENDER_QA_20260524.md`：Word 页面渲染 QA。
- `06_final_handbook/WORD_RENDER_QA_SUMMARY_20260524.json`：页面渲染 QA 机器摘要。
- `06_final_handbook/选必一_终稿逐题覆盖与频次修复审计_20260524.md`：逐题覆盖与频次修复审计。

## 残留风险

- GPT Pro 终稿复核未通过：不是 GPT Pro 给出负面意见，而是当前 Chrome 扩展接管链路无法连通，尚未取得 GPT Pro 输出。
