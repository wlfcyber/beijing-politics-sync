# GPT / Claude Interaction Test

Date: 2026-05-02
Workspace: `/Users/wanglifei/Desktop/北京高考政治`

## Goal

Verify whether Codex can call GPT-side and Claude-side workers/advisors for the 飞哥政治庄园整本书双线总控 workflow.

## Local Entrypoints

- `claude`: `/Users/wanglifei/.local/bin/claude`
- `codex`: `/Users/wanglifei/.local/bin/codex`
- `openai`: not found as a standalone CLI
- `OPENAI_API_KEY`: not set
- `ANTHROPIC_API_KEY`: not set

## Claude Code Test

Command shape:

```bash
claude -p --no-session-persistence --output-format json --tools "" --max-budget-usd 0.05 '<short JSON-only advisor prompt>'
```

Result:

- Status: PASS
- Auth: `loggedIn=true`, `authMethod=claude.ai`, `subscriptionType=max`
- Output returned:

```json
{
  "agent": "claude",
  "can_advise": true,
  "task": "给 Codex 提一个下一步教研任务",
  "suggestion": "整理2020-2025年北京高考政治主观题的高频考点与评分标准，形成结构化知识库。"
}
```

Notes:

- Email and organization details were redacted from terminal output.
- `--tools ""` works for pure advisor/generation calls.

## GPT / Codex CLI Test

Command shape:

```bash
codex exec --skip-git-repo-check --ephemeral --ignore-rules --sandbox read-only -C /tmp -m gpt-5.4-mini '<short JSON-only advisor prompt>'
```

Result:

- Status: PASS
- Output returned:

```json
{
  "agent": "gpt",
  "can_advise": true,
  "task": "给 ClaudeCode 提一个下一步教研任务",
  "suggestion": "先按最近一套北京区模考的客观题错项类型，补一版可直接用于课堂的“错误选项陷阱清单”并配3道新题。"
}
```

Notes:

- Codex CLI can act as the GPT-side worker/advisor without a standalone `openai` CLI or `OPENAI_API_KEY`.
- The command emitted non-fatal `403 Forbidden` warnings while warming plugin ids / analytics against `chatgpt.com`; the model call still completed and returned the requested JSON.
- For future production use, prefer `--ephemeral`, `--sandbox read-only`, explicit model, and a narrow prompt for advisor-only lanes.

## Operational Conclusion

The planned workflow is viable:

- Codex can call Claude Code as a Claude advisor/worker.
- Codex can call a separate Codex CLI session as a GPT-side advisor/worker.
- Both can generate task suggestions or structured advisor outputs.
- Advisor outputs must remain advisory only; source evidence and 飞哥政治庄园 branch skills remain the authority.

## Recommended Integration

- Use Claude Code for long-form explanation critique, Word layout instincts, and independent suite reruns.
- Use Codex CLI/GPT worker for adversarial task assignment, coverage-gap prompts, structured JSON audits, and independent checklist generation.
- Capture every cross-model call in `advisor_prompts/` and `advisor_reports/`.
- If Codex CLI plugin-sync 403 warnings become noisy but non-blocking, ignore them for advisor calls; if they block future calls, retry with reduced plugin loading or a cleaner config.
