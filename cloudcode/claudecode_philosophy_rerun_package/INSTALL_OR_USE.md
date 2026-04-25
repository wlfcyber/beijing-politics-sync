# How To Use With Claude Code

## Same Windows Machine

1. Open Claude Code in `C:\Users\Administrator\Desktop`.
2. Paste the full contents of `CLAUDE_CODE_PROMPT_V2_KEEP_CODEX_STYLE.md` if rerunning philosophy.
   - Use `CLAUDE_CODE_PROMPT.md` only as the older generic prompt.
3. Let Claude Code read the live paths listed in the prompt.

Claude Code does not need to "install" the Codex skill. It should treat `skill/feige-politics-garden/SKILL.md` and the files under `skill/feige-politics-garden/references/` as normal project instructions.

## Another Machine

Copy these folders too, otherwise the prompt will reference paths that do not exist:

- `C:\Users\Administrator\Desktop\2024各区模拟题`
- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`
- Any existing final artifacts you want Claude Code to compare against

Then edit the paths in `CLAUDE_CODE_PROMPT.md` before running it.

## If Claude Code Has Subagents

Use real agents for:

- 决策者
- 监管者
- 补丁者
- 劳动者
- 自动化检测者

Register them in `THREAD_REGISTRY.md`.

## If Claude Code Has No Subagents

Create separate role report files under the run directory and enforce the same checks through files. Do not pretend that roles existed; record the downgrade in `DECISION_LOG.md`.
