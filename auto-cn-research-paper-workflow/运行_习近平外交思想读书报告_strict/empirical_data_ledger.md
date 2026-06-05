# 实证数据采集台账

## 路线状态

- empirical_route: not_required_reading_report
- data_collection_status: not_run_by_user_requirement
- source_access_type: user_provided_pdf_and_official_web_fulltext
- crawler_compliance: no_crawler_used
- records_collected: 0
- dataset_hash: not_applicable

## 路线选项

- online_public_dataset: 公开或授权在线数据，可来自官方网页、公开网页、API、公开数据集、平台可见页面、政策数据库、公告、报告、授权图书馆/数据库导出，允许在合规条件下使用爬虫或脚本下载。
- secondary_case_comparison: 二手案例、文献、政策、报告、官方材料组成的案例比较。
- policy_text_corpus: 政策文本、规章、通知、官方网页组成的文本语料。
- quantitative_dataset_required: 需要统计、面板、变量或可量化数据；优先尝试由公开或授权在线数据构造。
- primary_fieldwork_required: 只有研究问题确实需要访谈、问卷、观察或内部材料时才使用。

## 采集计划

| 项目 | 内容 |
| --- | --- |
| 数据来源 | 不采集实证数据；使用课程参考书目 PDF 与官方网页全文 |
| URL/API/数据库路径 | 见 `03_文献矩阵.md` 与 `source_provenance_ledger.md` |
| 访问权限 | 用户提供 PDF；公开官方网页 |
| 是否允许爬取/下载 | 未使用爬虫；未批量下载 |
| 采集时间范围 | 不适用 |
| 样本纳入规则 | 不适用 |
| 样本排除规则 | 不适用 |
| 字段清单 | 不适用 |
| 清洗步骤 | 不适用 |
| 导出文件 | 不适用 |
| 可复现命令或脚本 | 不适用 |

## 采集日志

| 时间 | 来源 | 动作 | 数量 | 输出 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-05 | 用户指令 | 明确“不用实证” | 0 | 本台账 | 将任务定位为课程读书报告，不虚构数据、案例编码、访谈或问卷 |
| 2026-06-05 | 用户提供 PDF 与官方网页 | 读取并纳入文献矩阵 | 8 | `03_文献矩阵.md` | 这些是阅读/证据材料，不是实证数据集 |

## 使用规则

不得绕过登录、验证码、付费、下载限制或访问控制；不得采集密码、cookie、直接个人身份信息或敏感个人数据。若无法合法、安全采集，则改写研究问题或改用二手案例/政策文本路线。
