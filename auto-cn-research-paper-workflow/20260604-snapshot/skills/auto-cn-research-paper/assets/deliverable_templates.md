# Deliverable Templates

## 选题评分表

| 编号 | 候选题目 | 研究对象 | 范围 | 方法 | 文献可得性 | 材料可得性 | 对象清晰度 | 方法可行性 | 创新风险 | 贡献限度 | 完成风险 | 总分 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

生成 20-30 个候选题目；`结论` 中必须且只能有 1 个 `主选` 和 3 个 `备选`。评分列必须写数字，不能只写“高/中/低”。

## 检索日志

| 时间 | 数据库 | 检索式 | 筛选条件 | 命中量 | 采用文献 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |

## 文献矩阵

| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Source Provenance Ledger

For every `full_text_read` or `PDF_or_user_exported` source, generate `source_provenance_ledger.md` with `scripts/source_provenance_ledger.py`.

| source_id | run_id | title | database | route_url | method | local_file | sha256 | file_size | retrieved_at | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 材料文件迁移审计

Use `scripts/source_file_audit.py` to create `23_材料文件迁移审计.md` after changing devices or before rebuilding citation evidence.

| Recorded source | Current source | Recorded text | Current text | Evidence status |
| --- | --- | --- | --- | --- |

## Mac 材料重建队列

Use `scripts/source_rebuild_queue.py` to create `24_Mac材料重建队列.md` when current-machine source files are missing.

| Source ID | Title | Authors | Year | Action | Retrieval URL or clue | Missing recorded file | 下一步脚本 |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 优秀论文范式提取

| 文献 | 核验状态 | 可借鉴写法 | 对应位置 | 为什么有效 | 本文如何转化 | 不可复制边界 |
| --- | --- | --- | --- | --- | --- | --- |

## 论证骨架

### 题目

### 主问题

### 子问题

1.
2.
3.

### 中心判断

### 章节功能表

| 章节 | 功能 | 回答的问题 | 所需证据 | 当前证据状态 | 风险 |
| --- | --- | --- | --- | --- | --- |

## 观点-来源表

| 正文位置 | 关键判断 | 来源 | 来源状态 | 位置/页码 | 风险 |
| --- | --- | --- | --- | --- | --- |

## 引用与证据审查

| 问题级别 | 位置 | 问题 | 证据 | 修改建议 |
| --- | --- | --- | --- | --- |

Use issue levels: `must_fix`, `should_fix`, `optional_polish`.

## 完成度审计

| 要求 | 当前证据 | 结论 |
| --- | --- | --- |
| 用户给一个主题后自动确定选题 |  | pending/pass/partial/fail |
| 通过人大图书馆代理知网查询相关论文 |  | pending/pass/partial/fail |
| 下载或读取可用全文 |  | pending/pass/partial/fail |
| 按优秀论文写作方式提取范式 |  | pending/pass/partial/fail |
| 生成研究生水平文章 |  | pending/pass/partial/fail |
| 证据与引用可追溯 |  | pending/pass/partial/fail |
| 彻底解放双手 |  | pending/pass/partial/fail |

Completion audit must preserve the real scope. CAPTCHA, SSO, slider, or identity checks are user-action gates, not automatable steps.

## 外部评审记录

Use `scripts/visible_review_record.py` to update `15_外部评审与迭代计划.md`.

| lane | visible channel | status | raw record | review URL | local adoption status |
| --- | --- | --- | --- | --- | --- |
