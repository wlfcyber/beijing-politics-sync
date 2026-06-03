# Codex Local Configuration Notes

Snapshot date: 2026-06-03

Recoverable settings observed on this Mac:

- Default model: `gpt-5.5`
- Reasoning effort: `xhigh`
- Service tier: `priority`
- Sandbox mode: `danger-full-access`
- Approval policy: `never`
- Goals feature enabled.
- Memories feature enabled.
- Chronicle feature enabled.
- `max_concurrent_threads_per_session = 1000000`

Local proxy environment was configured through `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, and lowercase variants pointing at `127.0.0.1:18001`.

Do not sync sqlite state databases, logs, browser state, connector state, or provider API keys. The backup file `~/.codex/config.toml.bak-20260602-subagent-limit` remains local unless a sanitized copy is needed.
