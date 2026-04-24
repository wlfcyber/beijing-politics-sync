# Windows Visible Thread Restore

This project is a separate Windows restore copy of:

```text
https://github.com/wlfcyber/beijing-politics-sync.git
```

Current local path:

```text
C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible
```

## Thread IDs

| Role | Thread ID | Recommendation |
|---|---|---|
| supervisor | `019dbe09-cc94-73b0-9c5c-f982409d8dfd` | Open first. Main visible handoff entry. |
| philosophy-forward | `019db91f-5d73-78d3-afca-49bd7492a610` | Read-only unless explicitly resumed. |
| philosophy-reverse | `019dbe59-6286-7c60-8235-48969e2cb049` | Read-only unless explicitly resumed. |
| culture | `019dbe88-393f-7202-a214-cc47f5c8c75c` | Keep separate from philosophy files. |
| elective1 | `019dba05-359f-7382-8229-4bac5b46b6e2` | Accepted; normally do not restart. |
| elective2 | `019dba0d-267b-7a83-8ce0-94ac53aaf636` | Accepted; normally do not restart. |
| elective3 | `019dba73-b9bf-7bb1-8915-f30eb7aa7eac` | Accepted; normally do not restart. |

## If Codex CLI Works

From this repo:

```powershell
.\scripts\open_visible_thread.ps1 supervisor
```

Other roles:

```powershell
.\scripts\open_visible_thread.ps1 philosophy-forward
.\scripts\open_visible_thread.ps1 philosophy-reverse
.\scripts\open_visible_thread.ps1 culture
.\scripts\open_visible_thread.ps1 elective1
.\scripts\open_visible_thread.ps1 elective2
.\scripts\open_visible_thread.ps1 elective3
```

## If Codex CLI Is Not Usable On Windows

This Windows machine currently exposes Codex through the Desktop app, and direct terminal execution of the bundled `codex.exe` may fail with `Access denied`.

In that case, create a new visible Codex Desktop thread in this project and paste this:

```text
你是北京高考政治项目的可见督工接管线程。当前项目目录是：

C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible

请先执行 git pull --ff-only，然后阅读：

1. reports/主机可见线程接管指南.md
2. skills/beijing-gaokao-politics-rubric/references/current-state.md
3. reports/continuous_jobs/哲学必修四_三线闭环穷尽满分课/PROGRESS.md
4. reports/governor_board.md
5. RESTORE_THREADS.md

保持可见接管状态，不要启动后台 exec，不要自动重启已经验收通过的选必一、选必二、选必三。读完后报告当前状态和建议下一步，等待用户确认。
```

## Current Do-Not-Repeat Items

- `2024丰台一模` 已作为正向线和倒序线交汇点合并闭环，不要再开两线重复做。
- `2024朝阳期中` 已闭环并上传，错肢库新增 35 条，当前总行数 `1395`。
- 哲学剩余选择题答案源缺口只剩：`2026丰台一模`、`2026房山一模`、`2026丰台期末`、`2024丰台二模`。
- 选必一、选必二、选必三已经通过严格验收，除非明确要求返工，否则不要重启。
