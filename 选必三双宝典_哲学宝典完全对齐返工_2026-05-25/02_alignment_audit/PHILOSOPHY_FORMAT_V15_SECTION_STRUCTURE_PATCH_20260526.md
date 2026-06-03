# PHILOSOPHY_FORMAT_V15_SECTION_STRUCTURE_PATCH_20260526

status: `LOCAL_V15_SECTION_STRUCTURE_QA_PASS_NOT_FINAL`

## 本轮反思

V14 已经补齐水印、自然题号、目录样式等显性格式，但再次用哲学宝典 DOCX 本体检查时发现一个底层 Word 结构差距：

- 哲学宝典是 2 个 section：封面/前言/目录后进入连续正文 section。
- V14 双宝典只有 1 个 section。
- 哲学宝典 section header/footer distance 为 `457200 / 457200`。
- V14 双宝典此前是 `431800 / 431800`。

这说明 V14 还不能说“Word 格式完全对齐哲学宝典”，即使页面肉眼已经接近。

## 修补

已修补 `tools/build_handbook_docs.py`：

- 新增统一 section geometry helper。
- 默认 section 设置为哲学宝典同款 A4、页边距、header/footer distance。
- 在目录后新增 `WD_SECTION.CONTINUOUS` 正文 section。
- 第一 section 保持 `different_first_page_header_footer=True`。
- 正文 section 设置为 `different_first_page_header_footer=False`。
- Word 导出 PDF 后重新归一化 DOCX TOC 样式，避免回退到 `TOC11/TOC21`。

## 验证

对照文件：

- 哲学宝典：`/Users/wanglifei/Desktop/哲学宝典最终版 5.2双终极融合版_目录页码美化版_副本.docx`
- 思维宝典：`07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- 推理宝典：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`

实测结果：

| 项目 | 哲学宝典 | 思维宝典 V15 | 推理宝典 V15 |
| --- | --- | --- | --- |
| section 数 | 2 | 2 | 2 |
| page size | `7560310 x 10692130` | 同哲学 | 同哲学 |
| margins | `756285 / 720090 / 774065 / 774065` | 同哲学 | 同哲学 |
| header/footer distance | `457200 / 457200` | 同哲学 | 同哲学 |
| first section different first page | `True` | `True` | `True` |
| body section different first page | `False` | `False` | `False` |

其他门禁：

- 思维 DOCX：`TOC1=4 / TOC2=15 / TOC11=0 / TOC21=0`。
- 推理 DOCX：`TOC1=8 / TOC2=61 / TOC11=0 / TOC21=0`。
- 思维 DOCX/PDF：`Q refs=0`、`1A/1B/1C/1D=0`、`候选稿门禁=0`、`待回源=0`。
- 推理 DOCX/PDF：`Q refs=0`、`1A/1B/1C/1D=0`、`【完整题干】=36`、`【完整选项】=36`、`候选稿门禁=0`、`待回源=0`。
- PDF 页数：思维 35 页，推理 54 页。

## 仍然不能写最终版

- GPT Pro 真实审查仍为 `real_call_pending / blocked_advisor`。
- Claude 最新真实 verdict 仍是 V9 `CONDITIONAL_PASS`，不是 `PASS`。
- V15 只关闭一个底层 Word section 结构缺口，不能替代真实外审和最终 Governor/Confucius。

