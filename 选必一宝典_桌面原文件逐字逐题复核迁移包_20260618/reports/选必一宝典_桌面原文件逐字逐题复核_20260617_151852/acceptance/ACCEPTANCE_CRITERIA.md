# ACCEPTANCE_CRITERIA

This run is not complete until all criteria below are satisfied:

1. The source DOCX hash in `00_control/SOURCE_LEDGER.csv` still matches the desktop original.
2. A structural inventory identifies every visible question/term entry in document order.
3. Each entry has an audit row for the required fields: 术语、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界.
4. Every claimed scoring term points to scoring-rule evidence or is marked BLOCKED/LOW_EVIDENCE.
5. ClaudeCode opus4.8max review is either captured with traceable output or explicitly marked NOT_COMPLETED.
6. Codex and ClaudeCode disagreements are reconciled or listed as open questions.
7. No final/all-covered claim is made from page count, entry count, document thickness, or model self-report alone.
