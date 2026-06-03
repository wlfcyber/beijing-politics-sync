# TASK BRIEF

## Objective

根据用户粘贴的 Claude 复审任务文本，对第5轮阐释收口版进行质量复审：

1. 聚合 `v5_out_1.txt` 到 `v5_out_10.txt` 的逐条复审结果。
2. 统计 `为什么能想到` 的四档质量：真推理、套路、错位、臆造。
3. 统计并列出答案落点硬伤。
4. 判断是否需要回到 Word 文档继续修订；如需要，后续必须在对应条目内修，不得另起补丁页。

## Inputs

- 用户粘贴文本：`01_inputs/pasted_request.txt`
- batch JSON：`01_inputs/v5_batch_*.json`
- Claude 批审输出：`02_batch_outputs/v5_out_*.txt`
- 当前交付件：`/Users/wanglifei/Desktop/选必一6.1最终版_第5轮阐释收口版_带水印.docx`

## Output

- `03_aggregate/v5_quality_reaudit_summary.md`
- `03_aggregate/v5_quality_reaudit_findings.csv`

