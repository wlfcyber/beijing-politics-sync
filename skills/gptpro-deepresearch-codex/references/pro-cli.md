# pro-cli Reference

Use this reference when the GPT Pro lane should go through the user's logged-in ChatGPT web session via `ratacat/pro-cli`.

Repository: `https://github.com/ratacat/pro-cli`

## What It Is

`pro-cli` is a Bun/TypeScript command-line interface for agents. It sends prompts through a ChatGPT browser session the user controls, then returns JSON-first results for Codex to consume.

Use it for:

- ChatGPT Pro or GPT-5.5 Pro advisor calls.
- Deep Research-style tasks when available to the user's ChatGPT account.
- Long async jobs that may need waiting, polling, or recovery.
- Structured JSON outputs with schema validation.
- Probability or odds scoring through repeated calls.

Do not describe it as bypassing authentication, subscriptions, rate limits, access controls, or account restrictions.

## Installation And Setup

Check first:

```bash
command -v pro-cli
pro-cli --version
```

If missing and the user asked for setup, install from the repository:

```bash
curl -fsSL https://raw.githubusercontent.com/ratacat/pro-cli/main/scripts/install.sh | bash
```

The CLI requires Bun and a logged-in ChatGPT Chrome session. Prefer a dedicated Chrome profile for normal operation.

Normal setup commands:

```bash
pro-cli setup --json
pro-cli auth command --json
pro-cli auth capture --cdp http://127.0.0.1:9222 --json
pro-cli doctor --json
```

Use the existing Chrome profile path only when the user explicitly consents to temporary local browser access.

## Health Checks

Use health checks that do not spend Pro quota:

```bash
pro-cli doctor --json
pro-cli models --json
pro-cli config get --json
pro-cli limits --json
```

Do not run `pro-cli ask` merely as a smoke test after an error or empty response. Use `doctor` for setup validation.

## Default Model And Reasoning

Common configuration:

```bash
pro-cli config set model gpt-5-5-pro --json
pro-cli config set reasoning extended --json
```

Before assuming a model id, check:

```bash
pro-cli models --json
```

## Calling Patterns

Short direct call:

```bash
pro-cli ask @prompt.md --json
```

High-effort advisor call:

```bash
pro-cli ask @prompt.md --reasoning extended --json
```

Durable long-running job:

```bash
pro-cli job create @prompt.md --wait --json
```

Long job with explicit reasoning and compact final answer:

```bash
pro-cli job create @prompt.md --reasoning extended --condensed-response 800 --wait --json
```

Polling without failing a local command:

```bash
pro-cli job wait <job-id> --soft-timeout 60000 --json
pro-cli job result <job-id> --json
```

List or cancel jobs:

```bash
pro-cli job list --limit 20 --json
pro-cli job cancel <job-id> --json
```

Daemon checks:

```bash
pro-cli daemon status --json
pro-cli daemon restart --json
```

## Structured Results

When Codex needs a typed result, provide a schema:

```bash
pro-cli job create @prompt.md --wait --schema @schema.json --json
```

Treat `data.result` as the main answer when present. Save the full JSON envelope because it may contain job ids, model settings, result statistics, and recovery metadata.

## Security Rules

Treat `~/.pro-cli` like browser session data or SSH keys.

Never paste, print, commit, sync, or share:

- Raw cookies.
- Session tokens.
- Local bearer tokens.
- `.env` files.
- Private keys.
- Browser profile internals.

The safest operational pattern is a dedicated ChatGPT Chrome profile created for `pro-cli`.

## Prompt Template

Use this compact structure for advisor calls:

```markdown
# Role
You are an external GPT Pro advisor for Codex. You are not the evidence source and cannot decide final facts.

# Task
<exact question>

# Context
<sanitized summary, constraints, short excerpts, source statistics>

# Output
Return:
1. Key findings or critique.
2. Suggestions, each with rationale.
3. Required local verification step for each substantive suggestion.
4. Risks, blockers, and assumptions.
```

For Beijing politics, always add:

```markdown
Do not invent exam evidence, rubric facts, or source wording. Mark every correction as advisory and state what local paper, answer key, rubric, or lecture source Codex must check before adoption.
```
