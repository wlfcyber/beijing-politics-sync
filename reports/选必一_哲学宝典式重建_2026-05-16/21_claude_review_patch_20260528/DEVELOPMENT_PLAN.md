# DEVELOPMENT_PLAN

1. Gate: 读取 master governor、worker orders、context manifest、adaptive/self-learning ledgers、选必一 skill 与 hard-rule references、上一轮 run 控制文件。
2. Parse: 解析 Claude 复核 DOCX 的正文、批注、修订痕迹，整理成待核验意见清单。
3. Verify: 对每条意见回查上一轮最终稿、19 版 OCR/来源文本、原始试卷和细则。
4. Patch: 只把成立意见定点写入新版最终稿；保留不成立意见并说明原因。
5. QA: 生成 DOCX/MD/PDF、修改台账、核验报告、压缩交付包，并做结构和版式抽查。

