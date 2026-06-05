#!/usr/bin/env python3
"""Create a repeatable Chinese research-paper run directory."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


FILES: dict[str, str] = {
    "00_运行状态.md": """# 自动科研流运行状态

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 运行主题 | {theme} |
| 自动选定题目 | 待生成 |
| 目标类型 | 研究生课程论文 |
| 引用格式 | GB/T 7714，先做元数据核验 |
| 数据库入口 | 中国人民大学图书馆电子资源平台进入的中国知网代理页 |
| 强制入口规则 | 只使用 `libproxy.ruc.edu.cn` 代理路径，不使用知网个人登录路径 |
| 当前阶段 | initialized |

## 门槛状态

| 门槛 | 状态 | 证据 |
| --- | --- | --- |
| Chrome 插件接管 | pending |  |
| 人大图书馆代理路径 | pending |  |
| CNKI 检索 | pending |  |
| 结果详情页 | pending |  |
| 全文下载或用户导出 | pending |  |
| PDF 可读性 | pending |  |
| 文献矩阵 | pending | 见 `03_文献矩阵.md` |
| 优秀论文范式提取 | pending | 见 `04_优秀论文范式提取.md` |
| 论文初稿 | pending | 见 `06_论文初稿.md` |
| 引用与证据审查 | pending | 见 `07_引用与证据审查.md` |

## 当前边界

登录、拼图、滑块、验证码、SSO、下载确认和身份确认均由用户本人完成。Codex 不代过、不绕过，只在用户完成后续跑。
""",
    "01_选题评分表.md": """# 选题评分表

| 编号 | 候选题目 | 研究对象 | 范围 | 方法 | 文献可得性 | 材料可得性 | 创新风险 | 完成风险 | 总分 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""",
    "02_检索日志.md": """# 检索日志

## 强制路径

本次检索只承认中国人民大学图书馆进入的知网代理路径。有效 URL 必须位于 `libproxy.ruc.edu.cn` 代理域名下，或由人大图书馆电子资源平台跳转进入。

| 时间 | 数据库 | 检索式 | 筛选条件 | 命中量 | 采用文献 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
""",
    "03_文献矩阵.md": """# 文献矩阵

## 可用于正文的全文文献

| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 候选但暂不正式使用的文献

| 编号 | 核验状态 | 题名 | 说明 |
| --- | --- | --- | --- |

## 使用规则

正文中的核心判断只能使用已获得 `full_text_read` 或 `PDF_or_user_exported` 核验状态的文献。题录、摘要和不可读 CAJ 只能作为候选线索。
""",
    "04_优秀论文范式提取.md": """# 优秀论文范式提取

本文件只提取写作方法和论证结构，不复制原文表达。每条范式均来自已核验 PDF 或全文。

| 文献 | 核验状态 | 可借鉴写法 | 对应位置 | 为什么有效 | 本文如何转化 | 不可复制边界 |
| --- | --- | --- | --- | --- | --- | --- |
""",
    "05_论证骨架.md": """# 论证骨架

## 题目

待生成

## 主问题

待生成

## 子问题

1. 待生成
2. 待生成
3. 待生成

## 中心判断

待生成

## 章节功能表

| 章节 | 功能 | 回答的问题 | 所需证据 | 当前证据状态 | 风险 |
| --- | --- | --- | --- | --- | --- |
""",
    "06_论文初稿.md": """# 论文初稿

说明：只有在文献矩阵中完成全文核验的材料才能支撑正文核心判断。
""",
    "07_引用与证据审查.md": """# 引用与证据审查

## 观点-来源表

| 正文位置 | 关键判断 | 来源 | 来源状态 | 位置/页码 | 风险 |
| --- | --- | --- | --- | --- | --- |

## 审查结果

| 问题级别 | 位置 | 问题 | 证据 | 修改建议 |
| --- | --- | --- | --- | --- |
""",
    "08_终稿修改清单.md": """# 终稿修改清单

## 必须修改

| 编号 | 修改项 | 说明 |
| --- | --- | --- |

## 建议修改

| 编号 | 修改项 | 说明 |
| --- | --- | --- |

## 可选润色

| 编号 | 修改项 | 说明 |
| --- | --- | --- |
""",
    "09_完成度审计.md": """# 完成度审计

## 目标拆解

| 要求 | 当前证据 | 结论 |
| --- | --- | --- |
| 用户给一个主题后自动确定选题 |  | pending |
| 通过人大图书馆代理知网查询相关论文 |  | pending |
| 下载或读取可用全文 |  | pending |
| 按优秀论文写作方式提取范式 |  | pending |
| 生成研究生水平文章 |  | pending |
| 证据与引用可追溯 |  | pending |
| 彻底解放双手 |  | pending |
""",
    "15_外部评审与迭代计划.md": """# 外部评审与迭代计划

## 闸口状态

- external_review_passed: no
- claude_opus_review_status: pending
- claude_opus_review_channel: unknown
- claude_opus_real_submission: false
- claude_opus_review_scope: unspecified
- claude_opus_review_run_id: unknown
- claude_opus_review_recorded_at: unknown
- claude_opus_raw_record: unknown
- gpt_pro_review_status: pending
- gpt_pro_review_channel: unknown
- gpt_pro_real_submission: false
- gpt_pro_review_scope: unspecified
- gpt_pro_review_run_id: unknown
- gpt_pro_review_recorded_at: unknown
- gpt_pro_raw_record: unknown

## 规则

Claude Opus / Opus 4.8 Max 和 GPT Pro / GPT-5.5 Pro 必须分别在真实可见的网页版或 App 会话中给出 `pass`，且每一路都必须记录 `web_session` 或 `app_session` 渠道、`review_scope=full_draft`、当前 run id、记录时间、原始记录和 `real_submission=true`，才允许把 `external_review_passed` 改为 `yes`。CLI/API 调用可作构建 skill 的参考意见；修订差异审阅、引用页码抽查和预检也可作为补充证据，但不能算最终论文全文审阅通过。

`REVISE` 或 `CONDITIONAL_PASS` 必须先转化为修订单，完成本地修改、复验与重新评审后，才能再次尝试通过外部评审闸口。
""",
}


def slugify(value: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|\r\n\t]+", "_", value).strip(" ._")
    return cleaned[:40] or "paper-run"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".", help="Workspace root for the run directory.")
    parser.add_argument("--theme", required=True, help="User-provided research theme.")
    parser.add_argument("--slug", help="Directory suffix. Defaults to a sanitized theme.")
    parser.add_argument("--prefix", default="运行", help="Run directory prefix.")
    parser.add_argument("--force", action="store_true", help="Allow writing into an existing directory.")
    args = parser.parse_args()

    workspace = Path(args.workspace).expanduser().resolve()
    slug = slugify(args.slug or args.theme)
    run_dir = workspace / f"{args.prefix}_{slug}"
    if run_dir.exists() and not args.force:
        raise SystemExit(f"Run directory already exists: {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)

    for name, template in FILES.items():
        path = run_dir / name
        if path.exists() and not args.force:
            continue
        path.write_text(template.format(theme=args.theme), encoding="utf-8")

    manifest = run_dir / "run_manifest.md"
    if not manifest.exists() or args.force:
        manifest.write_text(
            "# Run Manifest\n\n"
            f"- theme: {args.theme}\n"
            f"- created_at: {datetime.now().isoformat(timespec='seconds')}\n"
            "- route: RUC library proxy -> CNKI -> detail page -> PDF/user export -> evidence audit\n",
            encoding="utf-8",
        )

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
