---
name: feige-politics-garden
description: "Use when the user says 飞哥政治庄园, /飞哥政治庄园, 飞哥政治讲堂, /飞哥政治讲堂, 飞哥正志庄园, or casually asks for Beijing Gaokao politics research and the book/module must be routed. Route full-book overnight four-lane Codex + ClaudeCode + Claude Opus + GPT-5.5 Pro orchestration to feige-politics-garden-book-orchestrator; route 必修四 philosophy/culture work to feige-politics-garden-bixiu4, 选择性必修一《当代国际政治与经济》 work to feige-politics-garden-xuanbiyi, 选择性必修二《法律与生活》 work to feige-politics-garden-xuanbier, and 选择性必修三《逻辑与思维》思维部分 work to feige-politics-garden-xuanbisan. Keep cache-first evidence, scoring-rubric guardrails, four-lane production/review, and document-rendering requirements."
---

# 飞哥政治庄园

This is the router entrypoint for the user's Beijing Gaokao politics research system. The aliases `飞哥政治庄园`, `/飞哥政治庄园`, `飞哥政治讲堂`, `/飞哥政治讲堂`, and `飞哥正志庄园` all mean this same router. Do not run substantial research from this file directly; choose the correct branch skill first.

When the user invokes `/飞哥政治讲堂` and then speaks casually, infer the intended book/module, mode, and deliverable from their wording and recent context. If the casual request sounds like selecting a book, running a whole book/module, sleeping/letting the system finish, Codex+ClaudeCode cooperation, GPT/Claude guidance, or final document generation, route to `feige-politics-garden-book-orchestrator` and use its whole-book SOP. Ask only the missing questions needed to avoid a wrong run.

If the final artifact is `.docx`, also use the `documents` skill and render every DOCX before delivery.

## Route

Use `~/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md` when the task is about:

- Selecting one book/module and having Codex plus ClaudeCode plus advisor/reviewer lanes run the whole thing end-to-end into a final teaching document.
- Overnight or long-running multi-role workflows, GPT-5.5 Pro review prompts, Claude Opus teaching-text prompts, ClaudeCode production, final Word/PDF delivery, and Confucius zero-baseline learning verification.
- User wording such as `/飞哥政治讲堂 跑选必一`, `/飞哥政治讲堂 我睡觉了你搞完`, `/飞哥政治讲堂 按上次三线`, `四线`, `四线终极版`, `选一本书`, `两线一起跑`, `Codex和ClaudeCode`, `GPT和Claude指导`, `我睡觉去了`, `终极文档`, or `整本书总控`.

Use `~/.codex/skills/feige-politics-garden-bixiu4/SKILL.md` when the task is about:

- 必修四, 哲学, 文化, 哲学与文化.
- Material-to-knowledge trigger chains, principle/method framework placement, choice-question wrong-option patterns, or 必修四 cumulative artifacts.
- The existing long-running 飞哥政治庄园 workflow, governor review, cache-first corpus work, Word deliverables, GitHub sync, or cross-machine continuation for the 必修四 line.

Use `~/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md` when the task is about:

- 选择性必修一, 选必一, 当代国际政治与经济, 国政经.
- Main-question scoring rubrics, marking rules, 细则术语 accumulation, 完整设问, 细则位置, 材料触发, 答案句.
- Topics such as 国际竞争, 国际合作, 经济全球化, 世界多极化, 中国外交, 中国与联合国, 南南合作, 全球治理.

Use `~/.codex/skills/feige-politics-garden-xuanbier/SKILL.md` when the task is about:

- 选择性必修二, 选必二, 法律与生活.
- Legal-question source exhaustion, evidence grading, 主观题细则链, 法律关系判断, 争点识别, 责任/效力/程序落点, 法治意义收束.
- Topics such as 合同, 侵权, 知识产权, 不正当竞争, 劳动关系, 消费者权益, 格式条款, 继承, 物权, 人格权, 相邻关系, 调解, 诉讼, 司法确认.

Use `~/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md` when the task is about:

- 选择性必修三, 选必三, 逻辑与思维, 思维部分.
- Material-action-to-thinking-method trigger chains, scientific/dialectical/innovative thinking methods, main-question evidence grading, choice-question thinking traps, zero-baseline classroom templates, or full-suite exhaustion for the thought-method line.
- Topics such as 科学思维, 辩证思维, 创新思维, 超前思维, 分析与综合, 发散思维, 聚合思维, 逆向思维, 联想思维, 迁移和想象, 思维抽象, 思维具体, 感性具体.

If the user asks for a mixed-book task, route each term to its real book/module. Do not force 必修二、选必二、选必三, or 必修四 terms into the 选必一 table.

## Shared Rules

- For every substantial 飞哥政治庄园 production task, default to the four-lane final workflow unless the user explicitly narrows the task. This applies across all books/modules.
- Four-lane role assignment:
  1. `Codex 20x`: local controller, local evidence judge, production lane A, final fusion owner, document generator, and acceptance reporter.
  2. `ClaudeCode 20x`: production lane B, independent full-source rerun, batch source processing, omission hunting, suite/question matrices, blockers, and conflict candidates.
  3. `Claude Opus 4.7 Adaptive`: teaching-text editor after evidence lock; turns verified entries into readable, transferable student-facing prose, structure, examples, and answer language.
  4. `GPT-5.5 Pro`: chief content reviewer and pressure tester; checks conceptual mistakes, missing triggers, weak transfer chains, unsupported wording, and final artifact risks.
- GPT-5.5 Pro and Claude Opus 4.7 Adaptive must be real external/model calls for substantial framework, whole-book, final-document, or content-review work. Do not count Codex subagents, local simulations, generic advisor roles, or Codex-written "as-if GPT/Claude" notes as GPT-5.5 Pro or Claude Opus participation. Codex subagents may prepare context, summaries, questions, and local prechecks, but they never satisfy the GPT/Claude lanes.
- If the user requires user-visible ChatGPT `GPT-5.5 Pro` and Claude `Opus 4.7 Adaptive Thinking`, CLI/API calls such as `codex exec -m gpt-5.5` or `claude -p --model opus` are only provisional advisor references unless the user explicitly accepts them for that gate. The official gate must be run in a fresh, user-visible web/app conversation with the requested mode selected or otherwise clearly confirmed.
- If the real GPT-5.5 Pro or Claude Opus 4.7 Adaptive call is unavailable, blocked, unauthenticated, stalled, or not yet run, continue only the local evidence work that is safe to continue, log `blocked_advisor` / `real_call_pending`, and do not mark the relevant phase, framework, content review, final artifact, Governor gate, or Confucius closure as passed unless the user explicitly waives that real-call requirement for that exact phase.
- The user's original five Garden roles are Codex production lane A's own internal agents, not a replacement for the four-lane workflow. For substantial runs, Codex A should instantiate or explicitly ledger these internal agents: `决策者` chooses the next bottleneck and wakes stalled work; `劳动者` processes assigned suites/questions with source evidence; `补丁者` checks missed multi-point triggers, same-core merge errors, and framework misplacement; `监管者/Governor` rejects weak evidence and fake closure inside Codex A before the final Governor gate; `自动化检测者` verifies plan/progress/source ledger/coverage/report/artifact consistency and issues the next concrete assignment when any lane stalls.
- If real subagent/thread execution is available and the scope is substantial, Codex A should create separate internal agents for those five roles with non-overlapping responsibilities and visible outputs under `codex_lane/agents/` or the equivalent role-ledger folder. If the scope is narrow or the tool is unavailable, Codex must still run and record the five role checks locally instead of silently collapsing them into one undifferentiated pass.
- Codex and ClaudeCode are both workhorse production lanes. Do not demote ClaudeCode to a mere reviewer, and do not let Codex become only a dispatcher or monitor. Both must leave auditable source/evidence outputs when the scope is substantial.
- Claude Opus and GPT-5.5 Pro are not evidence authorities. Any new term, correction, deletion, or conceptual claim from them must be routed back to Codex local source verification before it can affect the student artifact.
- The standard substantial-run layout should include separate lanes or equivalent folders for `codex_lane/`, `claudecode_lane/`, `fusion/`, `opus_writer/`, `gpt55_review/`, `governor_confucius/`, and `delivery/`.
- Final fusion order: Codex source evidence + ClaudeCode source evidence -> Codex conflict裁决 -> Claude Opus teaching-text pass -> GPT-5.5 Pro content review -> Codex evidence-verified patching -> Governor -> Confucius artifact-only learning check -> Markdown/DOCX/PDF delivery.
- Even when Codex is doing a narrow patch or solo local continuation, the Garden roles must not disappear. Leave a visible role ledger and run at least local `Governor` and `Confucius` passes before calling the artifact closed. If a lane is not rerun because the delta is narrow, record that explicitly with the reason; do not silently omit the role.
- `Governor` and `Confucius` are role checks, not optional model identities. Codex may instantiate them locally for bounded Markdown/sample work, but the outputs must be written under `governor_confucius/` or the equivalent audit folder.
- Use the reusable corpus cache before raw Office/PDF/PPT conversion. On this Mac, search under `/Users/wanglifei/Desktop/北京高考政治` first; on Windows mirrors, the known historical cache was `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`.
- Cache-first is not cache-only. Return to the original Word/PDF/PPT when cached text is missing, confusing, incomplete, or insufficient for evidence.
- Do not invent rubrics, answer keys, scoring rules, or source files.
- Do not treat ordinary reference answers as scoring rubrics unless the user explicitly confirms that file is usable.
- 2026石景山期末：用户逐题复核确认没有可用评分细则；所有书、所有模块都不处理这套试卷，可删除/排除。除非用户明确提供新的评分细则来源，否则不得用答案及评分参考补入。
- Preserve the user's framework over generic category systems. If a scoring term cannot fit cleanly, record the closest location and why.
- For long-running work, keep source ledgers, progress/control files, and governor decisions aligned before declaring completion.

## Durable User Notebook Rules

- Before any substantial book/module run, rerun, Word generation, or handoff to Claude Code, locate and read the user's lane notebook first. Treat the notebook as the highest task-local rule source; new requirements append to it and must not silently overwrite old requirements.
- When the user corrects Codex for a missed requirement, first turn that correction into a durable, checkable notebook rule in the branch notebook and the current run control files before continuing the same workflow. Record the missed behavior, the new hard rule, and the validation check that will prevent the same mistake in a fresh thread.
- Known notebook pattern: 必修四 uses `00_飞哥必修四宝典硬性要求记事本.md`; 选必一 uses `选必一_交付要求记事本.md`; 选必二 uses `00_飞哥选必二法律与生活要求小本本.md`. If the exact path differs by machine, search the Beijing politics workspace before starting.
- If the user says an old lane is `全部作废`, `从0开始`, or `不继承旧结论`, restart from raw 2024-2026 district-paper sources and the current notebook. Old artifacts may only help locate files or audit differences when the user explicitly allows that; they are not evidence and not conclusions.
- If the user narrows scope, keep that boundary throughout research, worker prompts, and final artifacts. Example: `只要哲学，不要文化` means 必修四文化 content must not enter the philosophy deliverable.
- If a source is PDF, Word, PPT, image, scan, screenshot, table, or comic question, use available conversion, rendering, OCR, vision, screenshot, or Office tools. Do not abandon the source merely because one tool such as pdftoppm, tesseract, pandoc, or a parser is missing.
- Cache-first never means text-only. If cache text loses options, tables, cartoons, page layout, or rubric structure, return to the original file and render/read the page.
- Evidence hierarchy stays strict: formal scoring rules, marking rubrics, marking reports, and user-confirmed scoring sources outrank ordinary reference answers. A reference answer cannot be called a rubric unless the user confirms it.

## Worker Supervision

- When supervising Claude Code or another worker, pass the branch skill, lane notebook, master requirements, and current patch instructions explicitly. Keep telling the worker to continue until the final target is actually satisfied, not merely until a partial artifact exists.
- If the user has granted broad authorization for the run, allow necessary reading, writing, conversion, rendering, screenshots, OCR/vision, script execution, restarts, and Office validation without repeatedly stopping for confirmation.
- On every wakeup, inspect process state, debug logs, progress files, decision logs, source ledger, coverage matrix, suite reports, audit folder, and outputs. If progress stalls, the worker asks for confirmation, drifts out of scope, skips suite closure, or claims completion without final validation, give corrective instructions or restart it.
- Long runs must close the loop at suite/question level: source ledger, coverage matrix, progress/control files, suite reports, audit records, and final acceptance report must agree before completion.

## Student Artifact Contract

- Final student-facing documents are teaching artifacts, not work logs. They must not contain source paths, file ids, line ids, OCR/debug notes, audit status words, English pipeline fields, model chatter, or wording such as `评标`, `参考答案`, `答案写`, `可从...角度作答`, `yes`, `pass`, `filled`, or `correct_option_chain` as if it were student content.
- 必修四哲学 deliverables must be organized by the user's original principle/method framework, not by paper order. Each main-question entry should read in student thinking order: `材料触发点` -> `设问` -> `为什么能想到` -> `答案落点`.
- `材料触发点` must cite real material signals from the original question. `为什么能想到` must explain the knowledge logic from those signals to the principle. `答案落点` must be a natural answer sentence or direction a student could write, not meta-instructions about how to answer.
- 主观题 `设问` must contain the actual task sentence. Do not dump full material into the question field; if a cached field says `材料与设问`, split the material back into the trigger field and keep only the real question in `设问`.
- Choice questions should display all four option units when the final product is meant for student review. Split options onto separate readable lines when useful, and keep the option group together so one option is not stranded across pages.
- Comic and image-based questions should preserve the actual image in the Word/PDF artifact whenever possible. After any DOCX rewrite, verify `word/media` or rendered pages so images have not disappeared.
- Use Chinese double quotation marks `“”` for key material quotations in Chinese teaching documents; avoid mismatched straight quotes or single quotes for quoted material.
- Avoid awkward or misleading classroom terms. If the user objects to a term such as `配伍`, replace it with natural student-facing wording that preserves the knowledge content.

## Word Delivery And Format QA

- A `.docx` deliverable is not complete just because a script generated it. Render/export it for visual QA, and when Microsoft Word is available, open/save/validate it in Word before final acceptance.
- Native TOC should be clickable and page-referenced when the user asks for a polished Word document. Page numbers should be present. Heading colors may be tasteful, but TOC entries should not all turn blue unless the user explicitly wants that style.
- Format edits must preserve knowledge content. When the user says `不要动内容`, interpret that as `do not change knowledge substance`; still fix formatting, missing images, option visibility, labels, TOC, pagination, and watermarks as requested.
- Before and after format-only operations, compare paragraph text counts or hashes when practical, and verify media counts, drawing counts, TOC/PAGEREF fields, rendered sample pages, and known hard samples.
- For watermarks, use a low-interference body/document watermark when requested and make it visible enough for the user's preference. Be honest that editable DOCX watermarks are not mathematically impossible to remove; a flattened PDF is the stronger distribution form when anti-removal matters.

## Reflection Patches From 2026-05-02 Philosophy Run

- Preserve the accepted version as the base once the user says they are satisfied. Apply narrow deltas on top of that base instead of rebuilding from a different artifact and accidentally changing content, TOC styling, images, or layout.
- Do not over-style the document. The title or high-level headings can be blue and polished, but directory entries, body labels, and hyperlinks must be checked visually after the change.
- Do not make broad regex cleanup rules over all numbered questions. Scope deduplication and choice repairs to the exact question type/paragraph pattern, because an over-broad rule can damage subjective-question structure.
- If choices are missing or inconsistently displayed, recover them from original local sources, answer keys, rendered pages, or OCR/vision instead of assuming the existing text is complete.
- After adding or deepening a watermark, re-render sample pages and confirm it does not cover serious content, change pagination unexpectedly, remove images, or break TOC/page-reference fields.
- Final acceptance should be artifact-only: use the produced Markdown/Word/PDF itself to check whether a zero-baseline student could follow `material signal -> principle/method -> answer sentence`. Internal audit confidence is not enough.
