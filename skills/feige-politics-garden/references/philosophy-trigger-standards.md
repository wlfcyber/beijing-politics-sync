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
- Re-run Claude Code only for:
  - missing or failed suite audit results;
  - source evidence gaps;
  - OCR/conversion blockers;
  - wrong framework placement;
  - incomplete question prompt;
  - shallow or hallucinated trigger logic that cannot be repaired from cached fields.
- When re-running, use the smallest same-suite bundle that preserves the full question prompt, material trigger excerpt, answer key if relevant, and scoring evidence.
- If a suite stalls but Claude Code is confirmed running with the requested model and no error, allow a longer wait. If restarting is necessary, restart the same suite; do not skip forward silently.

## 7. Governor Checks

Reject a batch if:

- final student entries are organized by questions rather than framework nodes;
- trigger logic merely says the rubric mentioned a point;
- answer landing is a meta-instruction rather than a concrete answer sentence;
- source paths or line/file/slide ids appear in the student-facing document;
- full question prompts are missing;
- ordinary reference answers are treated as rubrics;
- OCR-needed or source-missing items are hidden as completed;
- old v2/v3 conclusions are reused as evidence.
