# Claude Zero Run Decision Log

## D001: Independent Run Root

Decision: Use `/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/` as the new output root because the user explicitly required these artifact paths.

Reason: The older `选必二法律主观题框架_从题源生长` lane is flagged by the master governor as possible false closure and must not be used as the active production lane.

## D002: Old Artifacts Are Contamination Risk

Decision: Previous v8/v9/v10/v11/v12 files may be inspected only for style DNA or as negative checks; they may not provide source evidence, question count, framework categories, or conclusions.

Reason: The user explicitly ordered a from-zero rerun.

## D003: ClaudeCode Launch Evidence

Decision: Save `claude --version`, command path, launch command, stdout/stderr log, PID, and model/effort if available.

Reason: Cross-book V3 requires a ClaudeCode hard lock before treating a ClaudeCode lane as production evidence.

## D004: Unattended Overnight Constraint

Decision: Use a system wake guard during execution so display sleep does not stop the worker process.

Boundary: This can keep the Mac awake while powered and open; it cannot guarantee survival across lid-close sleep, shutdown, power loss, network loss, or a Claude-side session interruption.

## D005: VS Code Formality Boundary

Decision: The user asked to see the run, so the production lane was launched through VS Code ClaudeCode rather than hidden background CLI.

Evidence: VS Code ClaudeCode session `827a92c7-6d8b-46b5-bcac-f1d2dbf89fe1`, process pid `41907`, entrypoint `claude-vscode`, model log reports `claude-opus-4-7`.

Reason: The hard-rule notebook records the user's 2026-05-20 requirement that the formal ClaudeCode production/audit channel should use VS Code. This also satisfies the user's live request to make the work visible.

## D006: Wake Guard

Decision: Start a 12-hour macOS wake guard labeled `com.wanglifei.claude-zero-caffeinate`.

Boundary: This keeps the system awake while powered and open. It does not protect against lid-close forced sleep, shutdown, power loss, network loss, or an upstream Claude session interruption.
