# Claude 页锚抽查复审提示

你上一轮给出 `REVISE / safe_to_record_as_final_visible_review_pass: no`，但同时明确承认：

- 正文作为研究生课程论文质量合格偏强；
- 来源台账、hash、方法-材料匹配可接受；
- `citation_final.md` 与 `citation_evidence_workbench.md` 已经修复 No.45/47/48/49/50 的页码占位和张冠李戴问题；
- 唯一阻断是：包内自报摘录不能替代真实 PDF 页面的独立抽查。

本次我附上 `30_Claude独立页锚抽查包.pdf`。这个 PDF 是从 `source_provenance_ledger.md` 登记的本地真实来源 PDF 按 SHA256 校验后生成的抽查包。每条引用先给出元数据页，然后紧跟对应来源 PDF 的原始页面。

请只审查你上一轮要求的“若干页锚实际抽查”是否成立，重点是 No.45、No.47、No.48、No.49、No.50：

- No.45 `[13]` S-013 `p.7-p.11`
- No.47 `[10]` S-010 `p.1, p.4, p.7, p.14-p.15`
- No.48 `[5]` S-005 `p.2, p.4`
- No.49 `[14]` S-014 `p.1, p.5, p.8-p.11`
- No.50 `[7]` S-007 `p.1-p.2, p.5-p.9`

审查规则：

- 请对照 PDF 中可见原页，不要只相信元数据页或工作台摘录。
- 如果这些原页不能支撑对应引用语境，请判 `REVISE` 并指出具体 No. 和页码问题。
- 如果这 5 条抽查足以解除你上一轮唯一阻断，并且你没有新的客观硬伤，请判 `PASS`。
- 不要仅因 `external_review_passed=no`、`claude_opus_review_status=revise` 或 `final_user_goal_ready=no` 判 `REVISE`，因为这些字段等待你本轮结论更新。
- 如果你仍然不能给 PASS，请明确说明还缺哪一种客观证据；不要只说“继续自洽不够”。

请按以下格式返回：

```text
verdict: PASS / REVISE
pdf_page_spotcheck_judgment: ...
row_45_judgment: ...
row_47_judgment: ...
row_48_judgment: ...
row_49_judgment: ...
row_50_judgment: ...
remaining_blocker_if_revise: ...
safe_to_record_as_final_visible_review_pass: yes/no
```
