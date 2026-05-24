# 外审材料包清单

## 主审文件

- `01_xuanbiyi_candidate_student_local_clean.md`：本轮推荐外审候选稿。已清理工程痕迹，未改变题例实质。
- `01_xuanbiyi_candidate_student.md`：原始候选稿，用于必要时回查。
- `01_xuanbiyi_candidate_student.docx`：原始 Word 版。

## 标杆文件

- `02_bixiu4_philosophy_benchmark_student.md`：必修四哲学宝典标杆正文。
- `02_bixiu4_philosophy_benchmark_student.pdf`：必修四哲学宝典标杆 PDF。
- `03_bixiu4_benchmark_status.md`：哲学标杆状态与边界说明。

## 控制文件

- `../00_control/MASTER_REQUIREMENTS.md`
- `../00_control/LOCAL_PRECHECK.md`
- `../02_gptpro_web/GPTPRO_ACCEPTANCE_PROMPT.md`
- `../03_claude_opus/CLAUDE_OPUS_ACCEPTANCE_PROMPT.md`

## 使用顺序

1. 先给 GPT Pro：GPT prompt + 清洁候选稿 + 哲学标杆 + 本地预检。
2. 保存 GPT Pro 完整输出。
3. 按 GPT Pro P0 意见修订或生成待 Claude 审核稿。
4. 给 Claude Opus：Claude prompt + GPT 输出 + 待审稿 + 哲学标杆。
5. 保存 Claude 完整输出。
6. 按双审意见修订，必要时回到 GPT Pro/Claude 复审。
