# Codex 连续任务使用说明

## 这套机制做什么

- 让 `codex` 先读计划文档，再按进度文档继续开发。
- 每一轮都要求 Codex 回写进度。
- 只有当进度文档和计划文档完全对齐且全部任务为 `done` 时，循环才停止。

## 现有文件

- `codex_连续任务开发计划.md`
- `codex_连续任务开发进度.md`
- `scripts/codex_plan_status.py`
- `scripts/codex_continuous_dev.sh`

## 启动方式

```bash
bash scripts/codex_continuous_dev.sh
```

- 脚本会把每一轮的任务提示通过标准输入传给 `codex exec`，这也是 `codex exec --help` 明确支持的调用方式。

也可以显式指定计划文档和进度文档：

```bash
bash scripts/codex_continuous_dev.sh \
  /绝对路径/开发计划.md \
  /绝对路径/开发进度.md
```

## 常用环境变量

```bash
MAX_ITERATIONS=20
CODEX_MODEL=gpt-5.4
CODEX_SANDBOX=workspace-write
CODEX_LOG_DIR=.codex-continuous
PYTHON_BIN=python3
```

## 开新任务时怎么用

1. 重写 `codex_连续任务开发计划.md` 的 `## 任务清单`。
2. 重写 `codex_连续任务开发进度.md`：
   - 把 `总体状态` 改成 `in_progress`
   - 让 `步骤状态` 中的 `ID` 与计划文档完全一致
   - 把未完成项的状态改成 `todo`
3. 运行：

```bash
bash scripts/codex_continuous_dev.sh
```

## 日志输出

- 默认日志目录：`.codex-continuous/`
- 每轮会落下：
  - `prompt-N.txt`
  - `last-message-N.txt`
  - `codex-output-N.log`

## 停止规则

- 自动停止：全部任务都为 `done`
- 异常停止：
  - 有任务被标成 `blocked`
  - 文档格式无效
  - `codex exec` 非零退出
  - 达到 `MAX_ITERATIONS`
