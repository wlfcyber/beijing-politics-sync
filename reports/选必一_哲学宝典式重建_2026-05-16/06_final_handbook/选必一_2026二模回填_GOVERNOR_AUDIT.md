# 选必一 2026各区二模回填审计

- 回填日期：2026-05-23
- 正式入库批次：`03_fusion/BATCH_014_FINAL_AFTER_GPT_AND_CLAUDE.md`
- Codex 独立稿：`08_2026_second_mock_backfill/03_codex_independent/CODEX_INDEPENDENT_THICK_DRAFT.md`
- ClaudeCode 独立稿：`08_2026_second_mock_backfill/02_claudecode_independent/CLAUDECODE_ORIGINALS_THICK_DRAFT.md`
- GPT Pro 主融合输出：`08_2026_second_mock_backfill/05_gpt_pro_packet/GPT_PRO_OUTPUT_CAPTURE.md`
- GPT Pro 归一化稿：`08_2026_second_mock_backfill/05_gpt_pro_packet/GPT_PRO_OUTPUT_NORMALIZED_FOR_CLAUDE.md`
- ClaudeCode/Opus 复核：`08_2026_second_mock_backfill/06_claudecode_after_gpt_review/claudecode_gpt_review_stdout.txt`

## 入库范围

本轮新增主链题例 34 条，覆盖 8 道可入库题：

- 2026朝阳二模 Q20(1)
- 2026朝阳二模 Q20(2)
- 2026东城二模 Q20(3)
- 2026房山二模 Q20
- 2026海淀二模 Q20(2)
- 2026石景山二模 Q18
- 2026西城二模 Q19(1)
- 2026西城二模 Q19(2)

暂不入链 2 题：

- 2026丰台二模 Q20：PPT 主观题阅卷细则和 OCR 后 70 张讲评页中未定位到该题对应评分块。
- 2026顺义二模 Q20：当前目录只有 PDF 试卷，无答案、评标、阅卷细则、讲评 PPT 或教师细则。

## 终稿计数

- 输入批次终稿：14
- 输出题例：279（选必一主链278条，附录模块边界1条）
- 输出核心节点：103
- 时代背景：3个核心节点，16条题例
- 理论：4个核心节点，16条题例
- 经济全球化：42个核心节点，92条题例
- 政治多极化：17个核心节点，58条题例
- 中国：32个核心节点，85条题例
- 联合国：4个核心节点，10条题例

## 分类复核

- `国际新秩序 / 新型国际关系` 已归入政治多极化；`提供中国方案` 单独归入中国。
- 房山、海淀的 `正确义利观` 均归入中国，未放入理论。
- 东城开放红利相关术语按经济全球化细分处理，未压成单一“开放型世界经济”节点。
- 丰台、顺义未进入主链。

## 验证

- `python scripts/build_xuanbiyi_baodian.py` 已完成基础重建。
- `python scripts/fuse_xuanbiyi_opus47_final.py` 已重新叠加 2026-05-17/18 终稿补丁。
- `python scripts/validate_xuanbiyi_final.py` 通过，核心节点数为 103。
- Word 文件已重新生成：
  - `选必一_当代国际政治与经济_主观题术语宝典_学生版.docx`
  - `选必一_当代国际政治与经济_主观题术语宝典_考前导航版.docx`
  - 同步更新 `_gpt_claude_patch.docx` 两个同名交付版本。

## 渲染说明

官方 `render_docx.py` 渲染失败，原因为本机缺少 LibreOffice/soffice 可执行文件。随后尝试用 Word COM 导出 PDF，但 Word 导出超时未产出 PDF，已结束该导出进程。已完成 `python-docx` 结构打开校验：学生版与导航版 DOCX 均可正常打开并读取段落。
