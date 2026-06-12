# 哲学宝典迁移包 0612 交接计划

## STEP-01 三层 SOP

读取并刷新项目 master governor，读取 worker daily orders、压缩清单、自学习记录、必修四 skill 与哲学硬规则。

验收标准：记录本次读取的报告时间、对应 skill、硬规则文件。

## STEP-02 迁移包结构盘点

核对包内文件夹、版本件、工作底稿、索引表、构建脚本、交接说明。

验收标准：明确主 Word、唯一内容源、题源转录依据、基础分配表和旧审计表的口径。

## STEP-03 统计与指纹

统计 `sections/`、`inventory/`、`q_assigned.json`，计算关键文件 SHA256。

验收标准：给出 35 section、63 inventory、341 题、1159 成书条目、关键文件 hash。

## STEP-04 v9 渲染 QA

用文档渲染流程将 v9 主件导出为页面 PNG 和 PDF，检查是否导出失败、空白页或明显乱码。

验收标准：渲染成功，记录页数、PDF 路径、自动空白页检测结果和人工抽样页。

## STEP-05 补齐交接控制台

创建 `00_control` 下的简报、进度、ledger、coverage、governor、final acceptance 和下一线程接手卡。

验收标准：控制文件齐全，明确 `TASK_COMPLETE` 仅指迁移交接包，不指全项目源证据终审。
