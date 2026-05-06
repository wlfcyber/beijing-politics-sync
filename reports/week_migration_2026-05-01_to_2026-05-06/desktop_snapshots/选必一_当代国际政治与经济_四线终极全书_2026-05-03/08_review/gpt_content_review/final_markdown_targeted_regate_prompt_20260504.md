# GPT-5.5 Pro Final Targeted Regate Prompt Record

time: 2026-05-04
conversation: same ChatGPT Pro conversation used for this run, `https://chatgpt.com/c/69f7099a-36e0-839a-b579-db4d592f1848`
method: Safari, same conversation, targeted evidence packet rather than a new chat
artifact: `09_delivery/选必一_当代国际政治与经济_完整学生讲义_20260504.md`

## Prompt Purpose

Ask GPT-5.5 Pro to re-check only the old final-markdown blockers against current final evidence, without reopening the entire source-extraction debate.

## Evidence Packet Sent

- The final Markdown uses `和平与安全、发展、人权三大支柱` for the UN pillars issue.
- The 海淀期中 coffee-enterprise question is split into enterprise, industry organization, and government actions.
- The three wrong-prompt regressions were corrected:
  - `2024朝阳二模 Q20`: climate-governance table question.
  - `2026朝阳期末 Q20`: major-country diplomacy and China's modernization external environment.
  - `2025东城期末 Q20`: NEV export and EU countervailing-duty short essay.
- `2026西城期末 Q20` climate governance is split into concrete answer lines instead of a one-sentence concept pile.
- Clean scan excludes local paths, debug/audit terms, model-chat terms, source labels, scoring labels, and `2026石景山期末`.
- Final QA counts: 48 main training questions, 177 item chains, DOCX/PDF already generated for layout QA.

## Requested Output Schema

Return `verdict: PASS` only if the old blockers are closed and no new blocking issue appears. Otherwise return `verdict: NEEDS_FIX` with concrete must-fix items tied to visible final content.

