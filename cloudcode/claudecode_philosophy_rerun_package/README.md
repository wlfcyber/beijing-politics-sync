# Claude Code Philosophy Rerun Handoff Package

This package lets Claude Code reuse the user's Beijing politics research workflow without depending on Codex-specific skill loading.

Use `CLAUDE_CODE_PROMPT.md` as the main prompt. The prompt points Claude Code to the live project paths on this machine.

If the user wants Claude Code to preserve Codex's original framework presentation, use `CLAUDE_CODE_PROMPT_V2_KEEP_CODEX_STYLE.md` instead. That is now the recommended prompt for rerunning philosophy.

## Included

- `skill/feige-politics-garden/`: copied Codex skill, including rules, scripts, references, and current artifacts.
- `cache_indexes/`: lightweight indexes for the reusable preprocessed corpus.
- `CLAUDE_CODE_PROMPT.md`: prompt to paste into Claude Code.
- `CLAUDE_CODE_PROMPT_V2_KEEP_CODEX_STYLE.md`: stricter prompt that preserves Codex's source-grounded framework format.
- `CODEX_PRESENTATION_STYLE_GUIDE.md`: concrete presentation rules and required entry format.
- `INSTALL_OR_USE.md`: how to use this package.

## Live Data Paths On This Machine

- Skill source: `C:\Users\Administrator\.codex\skills\feige-politics-garden`
- Preprocessed corpus cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`
- Raw source roots:
  - `C:\Users\Administrator\Desktop\2024各区模拟题`
  - `C:\Users\Administrator\Desktop\2025各区模拟题`
  - `C:\Users\Administrator\Desktop\2026各区模拟题`
- Research workspace: `C:\Users\Administrator\Desktop\beijing_politics_research`
- Run workspace: `C:\Users\Administrator\Desktop\飞哥的政治庄园`

## Important

Cache-first is not cache-only. Claude Code should first use the preprocessed cache. If the cache is confusing, incomplete, or insufficient for a source judgment, it should open the original Word/PDF/PPT and record why.
