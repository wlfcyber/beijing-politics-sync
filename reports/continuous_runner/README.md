# Codex 连续任务执行器

这个目录提供一套最小可用的闭环：

- 先用 `TASK_BRIEF` 说明任务
- 再由 Codex 先产出 `开发计划文档`
- 然后按计划逐步开发
- 每完成一步，就把完成情况写入 `进度文档`
- 直到 `进度文档` 覆盖 `开发计划文档` 里的全部步骤才停止

这里对“计划和进度一致”的定义是：

- `开发计划文档` 中的每一个 `STEP_ID`
- 都已经在 `进度文档` 中以 `- [x] STEP_ID: ...` 的格式出现

## 文件

- [TASK_BRIEF.template.md](/Users/wanglifei/Desktop/北京高考政治/codex_continuous/TASK_BRIEF.template.md)
  - 任务说明模板
- [IMPLEMENTATION_PLAN.md](/Users/wanglifei/Desktop/北京高考政治/codex_continuous/IMPLEMENTATION_PLAN.md)
  - 本轮“连续任务执行器”自身的开发计划
- [IMPLEMENTATION_PROGRESS.md](/Users/wanglifei/Desktop/北京高考政治/codex_continuous/IMPLEMENTATION_PROGRESS.md)
  - 本轮“连续任务执行器”自身的开发进度
- [check_task_state.py](/Users/wanglifei/Desktop/北京高考政治/codex_continuous/check_task_state.py)
  - 检查计划和进度是否对齐
- [run_codex_until_done.sh](/Users/wanglifei/Desktop/北京高考政治/codex_continuous/run_codex_until_done.sh)
  - 持续调用 `codex` 命令推进任务

## 计划文档格式

计划文档中的步骤必须严格写成：

```md
- [ ] STEP_01: 第一步描述
- [ ] STEP_02: 第二步描述
```

允许把计划项写成 `- [x]`，但推荐计划文档始终保留为 `- [ ]`，进度文档负责记录完成情况。

## 进度文档格式

进度文档中的完成记录必须严格写成：

```md
- [x] STEP_01: 完成说明
- [x] STEP_02: 完成说明
```

## 使用方式

1. 准备任务说明文档。

建议先复制模板：

```bash
mkdir -p /absolute/path/to/job
cp /Users/wanglifei/Desktop/北京高考政治/codex_continuous/TASK_BRIEF.template.md /absolute/path/to/job/TASK_BRIEF.md
```

2. 修改 `TASK_BRIEF.md`，把任务目标、约束、交付物写清楚。

3. 运行执行器：

```bash
bash /Users/wanglifei/Desktop/北京高考政治/codex_continuous/run_codex_until_done.sh \
  /absolute/path/to/job/TASK_BRIEF.md \
  /absolute/path/to/job/DEVELOPMENT_PLAN.md \
  /absolute/path/to/job/PROGRESS.md \
  /absolute/path/to/workdir
```

4. 如果需要更激进的执行方式，可以加环境变量：

```bash
RUN_MODE=danger \
bash /Users/wanglifei/Desktop/北京高考政治/codex_continuous/run_codex_until_done.sh \
  /absolute/path/to/job/TASK_BRIEF.md \
  /absolute/path/to/job/DEVELOPMENT_PLAN.md \
  /absolute/path/to/job/PROGRESS.md \
  /absolute/path/to/workdir
```

说明：

- 默认 `RUN_MODE=safe`
- `safe` 使用 `codex exec --full-auto`
- `danger` 使用 `codex exec --dangerously-bypass-approvals-and-sandbox`

## 脚本行为

- 如果计划文档不存在或没有任何 `STEP_ID`，脚本会先要求 Codex 创建开发计划，并初始化进度文档
- 之后每一轮只推进下一个未完成步骤
- 每一轮尽量复用同一个 Codex 会话
- 会把最新会话 id 保存到任务目录旁边的 `.codex_session_id`
- 当全部步骤完成时，脚本自动退出

## 验证命令

可以手动检查状态：

```bash
python3 /Users/wanglifei/Desktop/北京高考政治/codex_continuous/check_task_state.py \
  /absolute/path/to/job/DEVELOPMENT_PLAN.md \
  /absolute/path/to/job/PROGRESS.md
```

输出会告诉你：

- 计划步骤数
- 已完成步骤数
- 尚未完成的 `STEP_ID`
- 是否已经完成
