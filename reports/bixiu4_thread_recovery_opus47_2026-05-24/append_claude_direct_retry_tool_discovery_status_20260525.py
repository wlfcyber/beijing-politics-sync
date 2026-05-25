from __future__ import annotations

from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent


def append_once(path: Path, marker: str, text: str) -> None:
    current = path.read_text(encoding="utf-8")
    if marker in current:
        return
    path.write_text(current.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")

    model_text = f"""
## CLAUDE_DIRECT_WEB_RETRY_TOOL_DISCOVERY_STATUS_20260525

status: `REAL_CALL_PENDING_TOOLING_NOT_CONFIRMED`

- Updated: {now}.
- After matrix risk queue closure, this thread attempted to discover callable Chrome/Claude web automation for a direct `https://claude.ai` retry.
- The available tool discovery result did not expose a callable Chrome navigation/session tool in this execution context; it exposed unrelated connectors and `node_repl`.
- No Claude web/app Opus 4.7 full-artifact review was executed in this turn.
- This is not a login-failure blocker and not a Google-login blocker. The correct next retry path remains direct `https://claude.ai` in the already logged-in user session.
- Full Claude Opus 4.7 web/app DOCX/PDF artifact review remains `real_call_pending`.
"""

    governor_text = f"""
## Governor Finding: Claude Direct Web Retry Tooling Status
Updated: {now}

- Governor decision: `REAL_CALL_PENDING_TOOLING_NOT_CONFIRMED`.
- Direct `https://claude.ai` remains the required route for the next Claude Opus 4.7 web/app full-artifact review.
- This turn did not complete a real Claude web/app full-artifact review because a callable logged-in Chrome navigation/session tool was not exposed after tool discovery.
- The blocker is tool availability in this execution context, not webpage login failure and not Google-login failure.
- No Sonnet, Haiku, or model-unknown output is counted as qualified evidence.
"""

    status_text = f"""
## Claude Direct Web Retry Tooling Status
Updated: {now}

- Status: `REAL_CALL_PENDING_TOOLING_NOT_CONFIRMED`.
- Correct route remains direct `https://claude.ai` using the already logged-in user session.
- No real Claude web/app Opus 4.7 full DOCX/PDF artifact review was completed in this turn.
- The current blocker is absence of a callable logged-in Chrome navigation/session tool in this execution context, not login failure.
"""

    append_once(BASE / "MODEL_EVIDENCE_LEDGER.md", "CLAUDE_DIRECT_WEB_RETRY_TOOL_DISCOVERY_STATUS_20260525", model_text)
    append_once(BASE / "GOVERNOR_RECOVERY_REPORT_20260524.md", "Governor Finding: Claude Direct Web Retry Tooling Status", governor_text)
    append_once(BASE / "THREAD_RECOVERY_STATUS_20260524.md", "Claude Direct Web Retry Tooling Status", status_text)
    print("claude_direct_retry_tooling_status_appended")


if __name__ == "__main__":
    main()
