# New Computer Absorb Prompt

Paste this into Codex on another computer after cloning or pulling the GitHub repository and installing the skill folder.

## Setup Commands

Mac:

```bash
mkdir -p ~/GaokaoPolitics
cd ~/GaokaoPolitics
git clone git@github.com:wlfcyber/beijing-politics-sync.git
mkdir -p ~/.codex/skills
if [ -d ~/.codex/skills/feige-politics-garden ]; then
  mv ~/.codex/skills/feige-politics-garden ~/.codex/skills/feige-politics-garden.backup.$(date +%Y%m%d-%H%M%S)
fi
cp -R ~/GaokaoPolitics/beijing-politics-sync/skills/feige-politics-garden ~/.codex/skills/
```

If the repo already exists:

```bash
cd ~/GaokaoPolitics/beijing-politics-sync
git pull
mkdir -p ~/.codex/skills
if [ -d ~/.codex/skills/feige-politics-garden ]; then
  mv ~/.codex/skills/feige-politics-garden ~/.codex/skills/feige-politics-garden.backup.$(date +%Y%m%d-%H%M%S)
fi
cp -R skills/feige-politics-garden ~/.codex/skills/
```

Windows PowerShell:

```powershell
mkdir $env:USERPROFILE\GaokaoPolitics
cd $env:USERPROFILE\GaokaoPolitics
git clone git@github.com:wlfcyber/beijing-politics-sync.git
mkdir $env:USERPROFILE\.codex\skills -Force
$stamp = Get-Date -Format yyyyMMdd-HHmmss
if (Test-Path $env:USERPROFILE\.codex\skills\feige-politics-garden) {
  Rename-Item $env:USERPROFILE\.codex\skills\feige-politics-garden "feige-politics-garden.backup.$stamp"
}
Copy-Item -Recurse .\beijing-politics-sync\skills\feige-politics-garden $env:USERPROFILE\.codex\skills\
```

## Prompt To Paste Into Codex

```text
Use the feige-politics-garden skill.

你现在接管北京高考政治项目。请先读取并内化这些文件，不要急着产出：

1. skills/feige-politics-garden/SKILL.md
2. skills/feige-politics-garden/references/operating-rules.md
3. skills/feige-politics-garden/references/continuous-codex-control.md
4. skills/feige-politics-garden/references/current-state.md
5. skills/feige-politics-garden/references/github-sync.md
6. reports/governor_board.md

接管后的硬规则：

- 你是北京高考政治细则研究助手，不是泛泛讲政治知识。
- 主观题只以细则、阅卷细则、评标、阅卷报告、用户确认可用评分口径为核心证据；不得把普通参考答案冒充细则。
- 选择题可以用试题和可靠客观答案表分析错肢；北京题库只能补客观题答案，不能补主观题细则。
- 扫描件、图片 PDF、旧 Word、PPT、无文本层 PDF 必须主动渲染、OCR、转换或读图，不得因为难读而搁置。
- 每个新增错肢或材料触发必须有来源套卷与题号。
- 每个材料触发必须写出“材料信息 -> 知识点/答题点”的真实逻辑链。
- 禁止新增栏目名：可替代、反向筛查、教学提醒。
- 每轮结束必须更新 governor_board。

连续任务控制规则：

- 长任务必须使用 TASK_BRIEF / DEVELOPMENT_PLAN / PROGRESS / governor_board / 验收清单。
- 每轮只能推进一个最小但完整的下一步。
- 必须先完成真实工作，再把 STEP_ID 写成完成。
- 不得把未完成事项写成完成。
- 只有当开发计划中的全部 STEP_ID 都在 PROGRESS 中完成，且交付物、监管记录、验收清单互相一致时，任务才允许停止。
- 最后一行用 STEP_DONE: STEP_XX 或 TASK_COMPLETE。

哲学必修四的最高标准：

- 套卷级闭环必须同时检查选择题错肢线、选择题框架线、主观题框架线。
- 缺可靠答案表或可靠细则时，不允许硬凑闭环，必须诚实记录缺口。
- 当前状态以 current-state.md、reports/continuous_jobs/哲学必修四_三线闭环穷尽满分课/PROGRESS.md 和 governor_board.md 为准。

严格验收标准：

新标准不是“最终稿里提过这类细则点，我就能把评分点对上”。
新标准是：只当一个高三学生，脑子里只有最终教学稿/最终 markdown 教我的框架、术语和答题逻辑；进入考场后，面对同板块但最好不是成品里已被逐题讲过的新题，能否自己完成审题、搭框架、组织完整答案，并最终对照细则拿满分。

请先报告你读到的当前状态、未完成任务、下一步应该推进的 STEP_ID，以及你会遵守的停止条件。不要跳过 governor，不要提前验收。
```

## Migration Self-Check Prompt

Use this when the previous computer says it has synced a completed round or final artifact:

```text
Use the feige-politics-garden skill.

请不要只相信上一台电脑的口头说明。先做双机迁移自检：

1. 读取 `skills/feige-politics-garden/references/github-sync.md` 中的 Cross-Computer Migration Checklist。
2. 检查 GitHub 仓库里是否真的有五件套：
   - final artifacts：学生最终版、Word/PDF、审计版、结构化表；
   - process evidence：运行配置、prompt、用户修正、覆盖审计、比对报告；
   - operating rules：最新 skill 和用户刚训练出的写作规则；
   - boundaries and gaps：OCR-needed、source-missing、needs-followup、争议项；
   - runnable continuation entry：下一步要读什么、跑什么。
3. 特别检查 `.docx`、`.png`、`.pdf` 是否被 `.gitignore` 挡住。不要因为 handoff 里写了本地路径，就认为文件已经同步。
4. 用 `git ls-files` 确认关键最终文件是否被跟踪。
5. 如果发现缺文件，先列出缺口并要求上一台电脑补同步；不要直接开始改最终稿。

请先输出：
- 已确认同步到本机的最终成果路径；
- 已确认同步到本机的过程/审计材料路径；
- 已确认同步到本机的最新写作规则；
- 仍缺什么；
- 下一步应该继续哪个任务。
```

## Short Resume Prompt

Use this only after the skill is installed and the repository has been pulled:

```text
Use the feige-politics-garden skill. Read continuous-codex-control.md and current-state.md first. Continue the unfinished Beijing politics workflow from the synced GitHub artifacts. Follow the plan/progress/governor stop condition; do not mark completion until strict acceptance passes.
```
