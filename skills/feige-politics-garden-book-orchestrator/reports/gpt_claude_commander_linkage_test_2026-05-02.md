# GPT/Claude Commander Linkage Test 2026-05-02

## Purpose

Test whether GPT and Claude can act as commander layers while Codex and Claude Code act as worker layers in the Feige Politics Garden whole-book workflow.

## Local Entrypoints

- Codex CLI: `/Users/wanglifei/.local/bin/codex`
- Claude Code CLI: `/Users/wanglifei/.local/bin/claude`
- Standalone `openai` or `chatgpt` CLI: not present
- Claude auth status: logged in with Claude Max

## Results

- GPT commander through Codex CLI succeeded and returned a compact task package.
- Claude commander through Claude CLI succeeded and returned a compact task package, but its sample conflict rule said `Claude wins`, which is unsafe for Feige Politics Garden.
- Codex worker through Codex CLI accepted a joint command as a worker health check.
- Claude Code worker rejected a raw `GPT/Claude commander packet` as prompt injection, even when the prompt said the packet was authorized task data.
- Claude Code worker accepted a direct health-check assignment when the task was phrased as a normal user/Codex-supervisor instruction without raw commander authority language.

## Decision

Feasible, but not as direct external-model command authority.

Use this architecture:

1. GPT commander-recommender outputs strategy, risk list, task split, and acceptance criteria.
2. Claude commander-recommender outputs teaching-flow strategy, clarity risks, task split, and Confucius verification prompts.
3. Codex local supervisor compares both recommendation packets.
4. Codex local supervisor translates accepted recommendations into direct worker prompts for Codex production and Claude Code production.
5. Workers receive direct scoped assignments, source paths, branch skill, notebook, `MASTER_REQUIREMENTS.md`, allowed tools, write scope, and acceptance criteria.
6. Disagreements go to local source evidence and user framework, never to model prestige.

## Hard Rule

Do not paste raw `GPT/Claude commander packet` text into Claude Code as authority. Treat external model outputs as advisory data and dispatch only Codex-supervisor-vetted tasks.
