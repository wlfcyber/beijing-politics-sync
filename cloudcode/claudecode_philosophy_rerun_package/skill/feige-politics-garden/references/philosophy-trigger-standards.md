# 必修四哲学触发链与答案落点硬标准

Use this reference for 必修四哲学 material-to-knowledge framework work, especially when supervising Claude Code or repairing cached suite results.

## 1. Source Boundary

- The three-year organized local corpus is the base source: 2024, 2025, and 2026 Beijing district mock papers, answer keys, rubrics, marking rules, lecture files, and confirmed scoring reports.
- Do not copy old v2/v3 conclusions as evidence. Old outputs may be used only as an audit index or cache to locate already processed suites.
- Reliable rubric evidence means scoring rubrics, marking rules, marking reports, lecture scoring standards, or user-confirmed scoring files.
- Ordinary reference answers do not by themselves support a main-question framework entry unless the user explicitly authorizes them as scoring evidence.
- If question text, material, answer key, or rubric is missing/OCR-needed, record a followup boundary instead of inventing or reverse-engineering a trigger.

## 2. Final Artifact Shape

- Student-facing final documents are organized by the user's original principle/method framework nodes, not by suite or question order.
- The required title for the final student-facing Word document is `2026北京高考政治哲学宝典---三年模拟全触发全链条`.
- The cover page should be clean, atmospheric, and student-facing: show only the title and a large signature `飞哥正志讲堂`. Remove subtitles, process notes, source notes, logs, and explanatory clutter from the cover.
- Page 2 should reserve a foreword section for the user to write later. Do not fill it with work logs or generated process explanation.
- Claude Code may design the Word layout according to its own aesthetic judgment, but it must not change the verified content, framework organization, or evidence boundaries.
- Each main-question entry must include:
  - knowledge point;
  - material trigger point;
  - why this material triggers the principle and how the principle answers the question;
  - material/question excerpt with the full question prompt;
  - rubric/scoring correspondence;
  - necessary boundary notes only when they help avoid misuse.
- The full question prompt is mandatory. Do not reduce it to a question number or half prompt.
- Materials may be excerpted only around the trigger words, relations, actions, conflicts, subject, or process.
- Student-facing documents must not display source paths, line ids, file ids, slide ids, entry ids, OCR/debug notes, or audit provenance such as `L24`, `F04`, `slide3`, `S015_F01`, `/Users/...`, `pdf`, `docx`, `pptx`.
- Keep provenance, source paths, line numbers, blockers, and verification notes in a separate audit evidence file.
- The final student-facing document must contain no work log appendix. Work logs, OCR trails, path evidence, comparison tables, and unresolved evidence notes belong in audit files only.

## 3. Trigger Logic Standard

`trigger_logic` is not a filing reason. It is the teaching chain from material to answer.

It must include:

1. Material signal: the exact material word, phrase, relation, subject action, contradiction, process, value orientation, or condition.
2. Knowledge trigger: why that signal fits a specific principle/method, stated in knowledge terms.
3. Answer landing: how that principle/method answers the exact question.

Forbidden trigger logic:

- "The rubric mentions this principle, so it can be placed here."
- "This point should respond to the question."
- "Let the principle serve the question."
- "Turn the principle into a method."
- "Explain that the material reflects this principle."

Rubric mentions are accuracy checks, not teaching logic. Put them in `rubric_excerpt`, `boundary_note`, or the audit evidence file.

## 4. Answer Landing Requirement

Every main-question `trigger_logic` must contain a concrete answer landing. The preferred wording is:

`答案落点：...`

The answer landing must be something a student could put into an answer or use to build an answer sentence.

For "为什么/何以/为何/意义/原因" questions:

- Write why the material fact, through the principle, proves the reason, value, or necessity asked by the question.
- Bad: "Use development to explain why."
- Good: "答案落点：春节之所以生生不息，是因为它不是停滞保存旧形式，而是在继承中创新，把传统年俗同新技术、新消费、新国际传播结合起来，所以体现发展观点和辩证否定。"

For "如何/怎样/怎么做/建议/措施" questions:

- Write what the subject should do under this method, based on the concrete material condition.
- Bad: "The subject should turn the principle into action."
- Good: "答案落点：网络文艺创作者应从中老年观众搜索不便、即时文艺消费不足这一实际出发，改进推荐方式、观看方式和付费模式，使作品供给符合中老年群体的真实需要。"

For "说明/体现/阐述/谈谈认识/理解/看法" questions:

- Map material actions, relations, or processes to principle points and state what they prove.
- Bad: "Explain that the material reflects the principle."
- Good: "答案落点：调查工作先整体安排阶段任务，再分别推进准备、调查、分析和应用，说明科学思维不是零散行动，而是把各环节作为系统来把握，体现整体与部分、系统优化。"

For relation questions:

- State how the two sides are distinct, connected, mutually promoted, mutually constrained, or jointly produce the result asked by the question.
- Good: "答案落点：接受人民监督侧重外部约束，自我革命侧重党内自我净化；二者既区别又相互促进，共同服务于跳出历史周期率，所以应以对立统一概括两者关系。"

## 5. Choice Question Standard

- Choice-question rows require both question text and a reliable answer key.
- Correct-option logic must explain which material signal makes the correct option fit the principle.
- Wrong-option notes must explain each wrong option's error type and boundary: condition inflation, subject mismatch, cause-purpose swap, scope mismatch, material inference boundary, legal relation mismatch, over-absolute wording, or module-boundary error.
- Do not enter choice-question patterns that are only one-off context reading unless they expose reusable wrong-expression logic.

## 6. Cache And Re-Run Policy

- Use cache-assisted repair when a suite has already been source-audited and the problem is final-document wording, format cleanup, removal of provenance, or conversion from rubric-based phrasing to student-facing answer landing.
- Distinguish source-derived cache from old conclusions. Converted source text, suite bundles, manifest rows, and rendered page images are first-read source cache; old framework entries, old CSV judgments, old candidate JSON, and old model summaries are conclusions and cannot be used as evidence.
- For suites already processed under the same source evidence, use cache to repair wording and format quickly. For genuinely new suites or previously OCR-needed suites, re-read the full suite evidence instead of copying the old result.
- Re-run Claude Code only for:
  - missing or failed suite audit results;
  - source evidence gaps;
  - OCR/conversion blockers;
  - wrong framework placement;
  - incomplete question prompt;
  - shallow or hallucinated trigger logic that cannot be repaired from cached fields.
- When re-running, use the smallest same-suite bundle that preserves the full question prompt, material trigger excerpt, answer key if relevant, and scoring evidence.
- For Claude Code reruns, prefer Opus 4.7 with adaptive/max effort when available. If the CLI exposes only `--model opus --effort max`, use that and verify the stream reports the intended Opus model.
- If a suite stalls, judge with process and log data: process alive, stream/debug log growth, file mtime changes, tool calls, and network/auth errors. Do not kill a run merely because it has been thinking for a while. If restarting is necessary, restart the same suite; do not skip forward silently and do not narrow the task by feeding it only the answer fragments.

## 7. Cross-Model Review And Merge

- Preserve a comparison lane between Claude Code output and Codex output.
- Entries independently placed by both models under the same principle/method node, with matching source suite, question number, question prompt, material trigger, and rubric boundary, receive higher confidence but still require source evidence.
- Entries that appear in Codex but not Claude Code, or Claude Code but not Codex, must be reviewed from the source before deletion or promotion.
- For differing placements, decide by the local source evidence and the user's framework, then list remaining disagreements for user review.
- When Claude Code's explanation chain is clearer but Codex catches a missing source, merge the strengths: keep the verified source placement and rewrite the student-facing chain so a zero-baseline senior student can understand how to move from material to principle to answer.

## 8. Governor Checks

Reject a batch if:

- final student entries are organized by questions rather than framework nodes;
- trigger logic merely says the rubric mentioned a point;
- answer landing is a meta-instruction rather than a concrete answer sentence;
- source paths or line/file/slide ids appear in the student-facing document;
- full question prompts are missing;
- ordinary reference answers are treated as rubrics;
- OCR-needed or source-missing items are hidden as completed;
- old v2/v3 conclusions are reused as evidence.
- a Word final contains cover clutter, source/path/debug residues, or work logs;
- Claude/Codex disagreements are silently discarded without source review.
