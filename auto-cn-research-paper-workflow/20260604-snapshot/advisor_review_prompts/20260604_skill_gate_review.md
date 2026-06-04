# Role

You are an external advisor reviewing a Codex skill for automated Chinese graduate-level research-paper production. Be strict and concrete.

# User Goal

The user wants Codex to receive only a theme or direction, independently choose a feasible topic, use an authorized RUC Library/CNKI route through Chrome or Computer Use, read and learn from verified strong Chinese papers, draft a source-backed graduate-level Chinese paper, and iterate until both GPT-5.5 Pro and Claude Opus 4.8 Max give real pass reviews.

# Current Skill Design

- The skill forbids fabricated sources, page numbers, quotations, surveys, interviews, CNKI records, and advisor comments.
- RUC/CNKI access must respect user login, CAPTCHA, SSO, identity checks, payment, download limits, and institutional rules.
- Windows browser evidence is explicitly invalid on Mac; Mac must revalidate Chrome, RUC/CNKI, full-text/export, and external advisor lanes.
- `mac_readiness_report.py` now records Python, Bun, Claude CLI, pro-cli, Chrome, and pro-cli doctor status.
- `chrome_cdp_probe.py` now records Chrome CDP tab titles and URLs only; it does not read cookies, local storage, forms, page text, or credentials.
- `browser_gate_report.py` now adopts `chrome_cdp_probe.md` evidence when status arguments are unknown.
- `run_audit.py` and `workflow_gate_matrix.py` require per-lane external review evidence, not a single summary line.
- `final_user_goal_ready=yes` is the only allowed final success signal.

# Current Evidence

- GPT-5.5 Pro route via pro-cli is live and ready.
- Chrome CDP can read the current tab title/URL.
- Current Chrome tab is ChatGPT, not RUC/CNKI, so browser gate remains not ready.
- Old trial run still reports `final_user_goal_ready=no`.
- Browser gate says Chrome path is readable, but current URL is not an authorized RUC/CNKI page.
- External final paper review is not passed; no final paper completion is being claimed.

# Request

Return a concise Chinese review with exactly these sections:

1. `verdict`: PASS_FOR_SKILL_INCREMENT, CONDITIONAL_PASS, or REVISE.
2. `strongest_parts`: what parts of the skill now correctly protect the user's goal.
3. `remaining_workflow_gaps`: concrete gaps that still prevent the skill from autonomously producing a real graduate-level paper.
4. `must_add_to_skill_or_scripts`: specific additions to make in the next development turn.
5. `risk_of_false_completion`: where Codex might still overclaim completion.
6. `recommended_next_step`: the single highest-leverage next implementation step.

Do not invent external facts. Judge only the design and evidence above.
