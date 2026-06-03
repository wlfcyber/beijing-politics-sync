# Deep Research MCP/API Reference

Use this reference when the user wants API-backed Deep Research or an MCP server such as `pminervini/deep-research-mcp`.

Repository: `https://github.com/pminervini/deep-research-mcp`

## What It Is

The Deep Research MCP path exposes long-running research tools to Codex through MCP/API infrastructure. It is different from `pro-cli`:

- `pro-cli` uses the user's logged-in ChatGPT web session.
- Deep Research MCP/API uses configured API credentials and server tools.

Use this path only when the server or tools are actually available in the current session, or when the user explicitly asks to set them up.

## Capability Check

Before promising Deep Research output, inspect the available tools or config. Look for tool names such as:

- `deep_research`
- `research_with_context`
- `research_status`

If the tools are not exposed, explain that the Deep Research MCP lane is not currently connected. Do not simulate it.

## Setup Boundary

Installing or configuring a Deep Research MCP server may require:

- API keys or provider credentials.
- Model access such as OpenAI Deep Research models.
- MCP configuration changes.
- A long-running local server.

Do not ask the user to paste secrets into chat. If setup is requested, guide them to place credentials in the expected local config or environment, then verify with non-revealing health checks.

## Research Workflow

1. Write a narrow research question.
2. Include source-quality requirements and citation expectations.
3. Start the research job with the MCP tool if available.
4. Poll status for long-running jobs.
5. Save the raw result and citation metadata.
6. Convert findings into local Codex tasks.
7. Verify any claim that will affect code, documents, grading rubrics, legal conclusions, or final artifacts.

## Prompt Template

```markdown
# Research Question
<one precise question>

# Scope
<date range, domain limits, geography, source types>

# Required Output
- Findings with citations.
- Confidence and uncertainty.
- Source-quality notes.
- Follow-up questions.
- Claims that require local verification before adoption.

# Constraints
Do not treat this research output as final authority. Codex will verify locally before implementing or publishing.
```

## When To Prefer pro-cli Instead

Prefer `pro-cli` when:

- The user explicitly says GPT Pro, ChatGPT Pro, GPT-5.5 Pro, or their Pro account.
- The task is advisor review rather than independent web research.
- The user wants to use the ChatGPT web session they already have.
- MCP tools are not exposed but `pro-cli` is installed and healthy.

Prefer Deep Research MCP/API when:

- The user asks for Deep Research specifically.
- Citation-heavy web research matters.
- A configured MCP tool is visible.
- The task needs async status polling and formal research output.
