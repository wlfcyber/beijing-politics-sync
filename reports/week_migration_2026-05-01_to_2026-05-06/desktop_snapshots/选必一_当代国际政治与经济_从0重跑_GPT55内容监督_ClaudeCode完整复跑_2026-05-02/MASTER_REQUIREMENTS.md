# Master Requirements

## Authority Order

Resolve conflicts as: latest user message in this thread > local lane notebook > latest skill files > current run control files > old artifacts.

## Overnight Authorization Update: 2026-05-03

- User is going to sleep and wants a finished 选必一 version by morning.
- Continue non-destructive reading, writing, extraction, OCR/rendering, model-advisor calls, ClaudeCode restarts, document generation, and validation inside this run folder.
- Claude may direct ClaudeCode, but only after Codex converts that advice into local worker tasks. Claude, GPT, and ClaudeCode do not decide source facts or scoring locations.
- Do not delete, overwrite, or mutate the old final artifact or previous run folder.
- Morning deliverable target: final student Markdown, DOCX, PDF, and `FINAL_ACCEPTANCE_REPORT.md` with validation evidence and remaining blockers if any source-boundary issue is genuinely unresolved.

## Scope

- Book/module: 选择性必修一《当代国际政治与经济》.
- Question type: 主观题 by default. Do not process choice questions unless the user explicitly asks later.
- Mode: 整本书/整模块从0重跑 into a student-facing scoring-term teaching artifact.
- Main framework: six buckets from the xuanbiyi notebook and branch protocol:
  1. 时代背景
  2. 理论
  3. 经济全球化
  4. 政治多极化
  5. 中国
  6. 联合国

## Start Boundary

- This is a zero-start rerun. Old 选必一 entries, old student drafts, old acceptance reports, and old conclusions are invalid as evidence.
- The previous run folder `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_双线总控_2026-05-02` must not be deleted, overwritten, or mutated.
- The old final student artifact is preserved because the user remembered its quality as possibly useful. It may be used only as a quality reference, omission-risk list, or source locator. It must not be copied as a conclusion.
- Every included term must be re-supported in this run by current source evidence and current entries.

## Source Range

Primary raw source roots:

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`

Allowed as cache, mirror, source locator, or missing-file supplement only:

- `/Users/wanglifei/Desktop/北京高考政治`
- `/Users/wanglifei/GaokaoPolitics`

Cache-first is not cache-only. If cached text is incomplete, unclear, missing options/tables/images/rubric structure, or insufficient to verify a scoring point, reopen the original PDF/Word/PPT/image/table source.

## Evidence Priority

1. Formal scoring rubrics, marking rules, marking reports, formal 评标/阅卷细则/阅卷总结.
2. Materials that explicitly讲分、标分、替换词、必答点.
3. User-confirmed scoring material.
4. Ordinary reference answers only as support. They are not scoring rubrics and cannot provide `细则位置` unless the user explicitly confirms them.

No source, no entry. If no clear scoring source/location exists, record the blocker and keep the item out of the main term table.

## Fixed User Corrections

- 2026通州期末 Q20 must preserve the user-corrected six-point structure:
  1. 共商共建共享全球治理观
  2. 时代主题、经济全球化、顺应各国人民愿望等
  3. 符合《联合国宪章》
  4. 推动构建国际新秩序、倡导国际关系民主化、践行多边主义、坚持正确义利观、兼顾利益等任意点
  5. 人类命运共同体
  6. 贡献中国智慧、中国方案、勇于大国担当
- 2026朝阳期中 Q17 and similar 总说/分说 items must preserve total/general layers plus all sublayers.
- 2026石景山期末 is excluded for all modules unless the user later provides new scoring-rule evidence.
- 2026西城期末 Q20 is must-include if current source evidence supports it.
- 2025海淀期中 Q16(2), 2025海淀期中 Q21(2), 2025海淀期末 Q22, 2024东城一模 Q16, and 2024东城一模 Q20 are must-check/must-include if current source evidence supports them.
- 2026海淀期末 is user-confirmed as no 选必一 and should be excluded unless new source evidence changes that.

## Entry Contract

Each accumulated term entry must include exactly the required fields:

```markdown
**术语：<rubric original phrase(s)>**

- 完整设问：<full prompt>
- 细则位置：<suite, question, scoring section, exact point, score, required/optional/evidence level>
- 来源：<year district exam + question>
- 材料触发：<why this prompt/material relation triggers this scoring term>
- 答案句：<candidate answer-sheet sentence: scoring term + material fact + reasoning/result>
```

Do not add `真题规律`.

`术语：` must preserve source scoring phrase(s), not Codex/Claude/GPT summaries.

`材料触发` must be real trigger logic: what the question asks, what relation the material sets up, and why that relation triggers the term. It must not be a material paraphrase plus a slogan.

`答案句` must read like a candidate's answer: scoring term + this question's material fact + because/therefore/effect. It must not contain backstage/meta language.

Forbidden in answer sentences and student-facing text: `采分点`, `要落到`, `并结合材料说明`, `设问要求`, `细则要求`, `本题需要`, `证据层级`, `v7`, `材料中`, `评标`, `参考答案`, paths, debug/OCR/status/model chatter.

## Module Boundary

- Do not force 必修二 terms such as `扩大国际市场`, `推进高水平对外开放`, `落实开放发展理念`, `新发展理念`, `高质量发展`, `现代化产业体系` into the 选必一 main table when the scoring source is clearly 必修二.
- Do not force 选必二、选必三、政治与法治、法律、逻辑, or 必修四 terms into the 选必一 table.
- Mixed questions may keep boundary notes outside the main table.

## GPT-5.5 Pro Supervision

- GPT-5.5 Pro is required as strategic commander/advisor and concrete content reviewer.
- Use the currently opened Safari ChatGPT Pro conversation as the main GPT-5.5 Pro feedback thread. Do not start a new temporary chat unless that thread is unavailable, stale, or the user changes the instruction.
- Send only sanitized phase reports and generated student-facing content. Do not send local absolute paths, accounts, secrets, raw logs, full source files, large raw exam passages, or large raw scoring-rule passages.
- GPT advice is P4, not evidence. Codex must digest each suggestion into local tasks and verify substantive content corrections against local source evidence before patching.
- Governor G11 requires the fixed trigger objects `outline`, `section_batch`, `final_markdown`, and `word_pdf`. Each must be reviewed by GPT-5.5 Pro or covered by an explicit fallback/waiver.
- A raw GPT review is not enough. `content_correction_log.md` must record issue, severity, local evidence check, Codex decision, patch status, and verified-closed status. Markdown PASS and Word/PDF PASS are separate.

## ClaudeCode Lane

- Start ClaudeCode as an independent production rerun lane from the same raw sources and the same notebook.
- Do not set a `--max-budget-usd` cap. The user explicitly said they never set a budget cap and wants ClaudeCode to run the full version.
- Claude advisor may issue commander-style advice for ClaudeCode, but Codex must translate it into bounded local prompts and must not treat it as evidence.
- ClaudeCode must not copy Codex entries or old-run entries.
- ClaudeCode writes primarily under this run folder's `claudecode_lane/` and its own structured outputs. It must not delete, overwrite, or mutate the previous run folder or old final artifact.
- ClaudeCode must close suites with source ledger, entries, suite reports, coverage matrix, blockers, and draft student artifact. Natural-language completion without files is invalid.
- Codex must supervise continuously: inspect process state, logs, progress files, ledgers, coverage, suite reports, and outputs; correct or restart ClaudeCode if it stalls, drifts, skips non-text materials, asks broad permission, or claims completion early.

## Codex Lane

Codex must also run a production lane. Codex cannot be only dispatcher/supervisor. Codex must inventory sources, read/render/OCR when needed, create entries, close suites, update control files, compare with ClaudeCode, fuse, and generate student artifacts.

## Deliverables

- Final Markdown student document.
- Final Word document with rendered/visual QA and Microsoft Word validation when available.
- PDF/rendered visual evidence when practical.
- Source ledger, coverage matrix, suite reports, conflict register, GPT phase advice and GPT content-review logs, Confucius report, and final acceptance report.

Final PASS is blocked until current-run evidence, ClaudeCode comparison, GPT content review/correction, Governor, Confucius, and Word/PDF validation gates are satisfied.
