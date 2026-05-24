## 一致性核查结果

**数字口径（138 / 373 / 7 / 380 / 145）三文件一致**

| 来源文件 | 核心点 | 主链 | 边界 | 总 | 导航数据行 |
|---|---:|---:|---:|---:|---:|
| `选必一_宝典终稿_GOVERNOR_FINAL_AUDIT.md` | 138 | 373 | 7 | 380 | 145 |
| `WORD_REBUILD_QA_20260524_FREQUENCY_COVERAGE.md` | 138 | 373 | 7 | 380 | 145 |
| `选必一_终稿逐题覆盖与频次修复审计_20260524.md` | 138 | 373 | 7 | 380 | 145 |
| `XUANBIYI_ABSENT43_TRIAGE.md`（执行后） | 138 | 373 | 7 | 380 | 145 |

**Triage RAW 与最终执行版差异已闭合**

- RAW（ClaudeCode Opus 原始）：A=1，B=5，C=36，NEEDS_SOURCE=1，合计 43。
- 最终执行：A=1，B=4，C/PASS=36，回源后排除=1（2024 顺义二模 Q18），合计 43。
- 差异点为 RAW 的 B4（= NEEDS_SOURCE N1）即 2024 顺义二模 Q18；本地回源到 `2024顺义思政二模细则.docx` 后主线为人代会/全过程人民民主，无选必一主链评分点，正确判为「不进主链、不进边界」。该校正记入 `XUANBIYI_ABSENT43_TRIAGE_RAW_CLAUDECODE_OPUS.md` 末尾 POSTCHECK 段，并指向 `XUANBIYI_ABSENT43_TRIAGE_POSTCHECK_20260524.md`。

**学生厚版本体校验**

- `###` 题例 380；`##` 二级标题 152（= DOCX Heading 2）；【什么时候写】出现 380 次（字段完整）。
- 2026 石景山期末 Q19(2) 人工智能全球治理已落入 7 个主链节点（"新型国际关系" 未挂入，与裁决一致）。
- 2025 东城二模 Q20 / 2025 朝阳二模 Q21 / 2026 西城一模 Q20(2) 共同利益题例已补入。
- `# 附：模块边界 / 跨书提示` 段存在（line 6029），4 条边界题（丰台/门头沟/海淀/房山）齐备。
- 2024 顺义二模 Q18：终稿 0 次（与排除裁决一致）。

**结论：DOCX 无需重新构建。**

```
verdict: PASS
body_pass: yes
docs_pass: yes
remaining_issues: 仅页面图片视觉 QA 未通过（本机无 LibreOffice/soffice，Microsoft Word COM 导出 PDF 超时），属环境限制而非内容/结构失败；Governor 已显式记为 "PASS WITH RENDER LIMITATION"。正式印刷或分发前，建议在具备稳定 LibreOffice 或 Word PDF 导出环境的机器上补做页面渲染抽检。
```
