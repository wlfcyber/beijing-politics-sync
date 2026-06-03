---
name: gptpro-deepresearch-codex
description: Use when Codex should call or coordinate ChatGPT Pro, GPT Pro, GPT-5.5 Pro, pro-cli, OpenAI Deep Research, Deep Research API/MCP, deep-research-mcp, or 深度研究 as an external advisor or research lane from Codex. Handles safe prompt-pack creation, pro-cli ask/job workflows, Deep Research MCP/API fallback, advisor result logging, conversion of external advice into locally verified Codex tasks, and Beijing Gaokao politics workflows where GPT Pro or Deep Research must never become the evidence source.
---

# GPT Pro DeepResearch Codex

Use this skill to let Codex route appropriate work to a real external GPT Pro or Deep Research lane while Codex remains the local controller, evidence judge, and implementer.

## Core Rule

External GPT Pro, ChatGPT Pro, Deep Research, and MCP research outputs are advisory. They may suggest risks, missing angles, search directions, critique points, or draft improvements. They do not prove source facts, scoring rules, legal facts, or local-file claims.

Never pretend a real GPT Pro or Deep Research call happened. If the tool, browser session, API key, model, quota, or account access is unavailable, record the lane as `blocked_advisor` or `real_call_pending` and continue only local work that is safe without that lane.

## Route Selection

Prefer `pro-cli` when the user wants Codex to consult their ChatGPT Pro web account, GPT Pro, GPT-5.5 Pro, or Deep Research-style capability through a logged-in ChatGPT browser session.

Prefer Deep Research MCP/API when the user explicitly asks for API-backed OpenAI Deep Research, an MCP server such as `deep-research-mcp` is already configured, or the task needs long-running formal web research with citations and status polling.

Use local Codex work only when the task is already answerable from local sources and no external advisor would change the result.

Read these references only as needed:

- `references/pro-cli.md`: installing, checking, and calling `pro-cli`.
- `references/deep-research-mcp.md`: using an MCP/API Deep Research lane.
- `references/advisor-boundaries.md`: safe prompt packs, evidence boundaries, and Beijing politics-specific rules.

## Standard Workflow

1. Define the advisor job:
   - User goal and exact question.
   - Whether the lane is strategy review, content review, deep research, probability scoring, or structured extraction.
   - What output shape Codex needs back.
   - What local verification is required before adoption.

2. Create a run folder:
   - Use `work/gptpro_advisor/<timestamp>-<slug>/` when the current workspace has `work/`.
   - Otherwise use `.codex/advisor-runs/<timestamp>-<slug>/`.
   - Save prompts, raw responses, parsed summaries, and decision logs there.

3. Build a sanitized prompt pack:
   - Include the goal, scope, constraints, relevant summaries, short excerpts, and explicit questions.
   - Exclude secrets, raw cookies, tokens, `.env` files, private keys, local absolute paths unless essential and safe, account details, and unnecessary private filenames.
   - For exam/rubric work, include source statistics and brief evidence summaries instead of long raw exam passages or long raw scoring-rule passages.

4. Preflight the selected external lane:
   - For `pro-cli`, run health checks with `pro-cli doctor --json`, not a paid/limited `ask` smoke test.
   - For MCP/API Deep Research, verify the tool or server is configured before promising a result.

5. Submit the job:
   - Use blocking `pro-cli ask @prompt.md --json` only for short direct advisor calls.
   - Use `pro-cli job create @prompt.md --wait --json` for long, durable, recoverable tasks.
   - Use MCP/API Deep Research tools only when exposed in the current tool list or explicitly configured in the environment.

6. Save the raw output:
   - Keep the JSON envelope if using `pro-cli`.
   - Extract the main response into a readable Markdown file.
   - Preserve job ids, model/config metadata, and timestamps.

7. Convert advice into local tasks:
   - For every substantive suggestion, write an adoption decision: accept, reject, defer, or needs user input.
   - For every accepted suggestion, write the local verification step.
   - Do not edit final artifacts from external advice until local verification passes.

8. Report honestly:
   - State whether a real external call was made.
   - State which lane was used.
   - State what was accepted, rejected, or still pending local verification.

## Output Discipline

When returning results to the user, distinguish:

- `External result`: what GPT Pro or Deep Research said.
- `Codex decision`: what Codex accepts after local reasoning.
- `Local verification`: what files, commands, citations, or checks support the decision.
- `Remaining risk`: anything not verified, blocked, or quota-limited.

For user-facing deliverables, strip advisor chatter, backend logs, source ids, local paths, and evidence-rank labels unless the user explicitly asks for backend material.
