---
name: auto-cn-research-paper
description: "Use when Codex needs to run an automated Chinese humanities or social-science research-paper workflow from a user-provided theme: autonomously narrow a topic, generate CNKI/RUC library search strings, use authorized Chinese database access, download or ingest user-exported literature, build a literature matrix, extract writing patterns from strong papers, create an argument spine, draft a graduate-course-paper-level Chinese article, and audit citations and evidence. Must not fabricate sources, data, CNKI records, page numbers, interviews, survey results, or unverifiable claims."
---

# Auto CN Research Paper

## Purpose

Run a controlled "theme -> topic -> database search -> verified sources -> paper-pattern extraction -> argument spine -> draft -> audit" workflow for Chinese graduate-level course papers or humanities/social-science research papers.

This skill is a coordinator. Use `cn-undergrad-thesis` as the evidence, citation, database-access, and Chinese academic-writing base. Prefer Chrome for logged-in RUC/CNKI sessions; use Computer Use only within the authorized browser-access limits when Chrome is unavailable and the URL can be reliably identified.

## User Goal Contract

For the user's current goal, the target is not just a paper helper. The target is an end-to-end automatic research-paper operator:

1. The user may provide only a theme or direction.
2. Codex must narrow and select a feasible topic on its own unless a missing constraint would make the work unsafe or impossible.
3. Codex must use an authorized RUC Library/CNKI route through Chrome or another approved browser-control path, with the user personally completing login, CAPTCHA, SSO, payment, identity, or download-confirmation gates.
4. Codex must learn from verified strong papers by extracting craft and argument patterns, not copying prose, typologies, or unsupported concepts.
5. Codex must draft a source-backed graduate-level Chinese paper, then audit evidence, citation anchors, method-material fit, text quality, and final gate status.
6. The run is not complete until both Claude Opus / Opus 4.8 Max and GPT Pro / GPT-5.5 Pro provide real `pass` reviews, their channels and raw records are recorded, all accepted revisions are applied and verified locally, and `workflow_gate_matrix.py` prints `final_user_goal_ready=yes`.

`CONDITIONAL_PASS`, `REVISE`, missing login, preflight-only checks, CLI calls without raw records, keyword-only page candidates, and material-count success are not completion. They are work queues.

## Non-Negotiable Rules

- Do not fabricate references, authors, journal names, years, DOI, URL, CNKI records, page numbers, quotations, data, interviews, surveys, advisor comments, or school rules.
- Do not bypass RUC Library, CNKI, Wanfang, VIP, school-library login, CAPTCHA, SSO, paywall, download limit, access control, or institutional rules.
- Do not inspect, copy, save, export, or analyze passwords, cookies, local storage, browser passwords, session files, or authentication credentials.
- The user must personally complete login, CAPTCHA, SSO, payment, download confirmation, and identity verification.
- Even if the user says Codex may solve a puzzle, do not solve or bypass CAPTCHA, slider, SSO, identity checks, or access controls. Pause, let the user complete them, then resume from the current page.
- Treat title/abstract-only sources as candidates, not formal evidence.
- Treat public reposts, search-portal full texts, WeChat/public-account reposts, and non-journal mirror pages as background candidates, not formal evidence, unless the original journal/database PDF, official HTML full text, or user-exported full text is verified.
- Use only verified full text, user-exported PDFs/CAJ, exported bibliographic records, or user-provided materials for final claims.
- Do not promise plagiarism-check, AI-check, advisor-review, defense, publication, or submission success.

## External Advisor Provenance Gate

When using Claude Opus, GPT Pro, GPT-5.5 Pro, ChatGPT Pro, or any other external advisor, record the exact channel:

- `web_session`: the prompt was submitted in the user's visible web chat/session and should leave a user-visible conversation record.
- `app_session`: the prompt was submitted in a visible ChatGPT or Claude app session and should leave a user-visible conversation/app record.
- `cli_or_api_real_call`: the prompt was submitted through a local CLI/API/backend tool and the raw response or job receipt was saved locally; it may help with skill-building advice, but it cannot satisfy the user's final GPT/Claude review gate.
- `preflight_only`: only login, browser, model, quota, or tool readiness was checked; no advisor review was submitted.

Never describe `preflight_only` as an advisor review. Never imply a `cli_or_api_real_call` has a web-chat trace unless the web page or returned job metadata proves it. For this user's target, the final approving reviews must be real visible web/app sessions. CLI/API responses may be recorded as advisory evidence while building the skill, but they do not count as final paper approval.

For this user's target, the external-review status file must contain these fields before the final gate can pass:

- `external_review_passed: yes`;
- `claude_opus_review_status: pass`;
- `claude_opus_review_channel: web_session` or `app_session`;
- `claude_opus_real_submission: true`;
- `claude_opus_review_run_id: <current-run-id>`;
- `claude_opus_review_recorded_at: <ISO timestamp>`;
- `claude_opus_raw_record: <path-or-url>`;
- `gpt_pro_review_status: pass`;
- `gpt_pro_review_channel: web_session` or `app_session`;
- `gpt_pro_real_submission: true`;
- `gpt_pro_review_run_id: <current-run-id>`;
- `gpt_pro_review_recorded_at: <ISO timestamp>`;
- `gpt_pro_raw_record: <path-or-url>`.

If the user explicitly asks for web-visible history, both channels must be `web_session`. If the review is done in a visible desktop/mobile app, use `app_session`. A command-line or API call can still be useful advisory evidence, but it does not satisfy the final approval gate.

Before submitting a visible web/app review, verify the lane is actually usable:

- Web tabs must not be on `logout`, login, loading-only, or no-input pages. Record the URL/title/input-count preflight if possible.
- App sessions must show a visible chat input or an equivalent user-visible compose state. A running app process alone is only `preflight_only`.
- On macOS, if Codex cannot click or paste into a visible app because Accessibility permission is denied, record that as a tool-permission blocker. Do not mark the advisor lane as submitted.
- If the visible app is usable but macOS blocks automation, use `scripts/visible_app_handoff.py` to prepare the clipboard/pending prompt and record `manual_submission_pending`. This is not a review submission and cannot satisfy the final gate.
- If the user manually pastes the prompt, record the visible response, screenshot/export, and channel as `app_session` or `web_session`; otherwise keep the lane pending.

## Browser Gate

Before claiming live CNKI automation works, verify all items in `references/browser_access_gate.md`.

If Chrome extension access is available, prefer Chrome for logged-in RUC/CNKI sessions. For the user's RUC workflow, prefer `libproxy.ruc.edu.cn` pages entered through the RUC Library electronic resources portal. Do not use CNKI personal login as the main route, and do not directly paste CNKI `download/order` URLs when the site requires a page-origin click.

If Computer Use can see a browser window but cannot reliably identify the URL, stop browser automation and ask the user to use Chrome or simplify the visible browser state. Do not use foreground keyboard/mouse fallbacks to bypass the URL safety check.

## Mac Workstation Notes

This workflow may move between Windows and macOS. On this Mac, default work under `/Users/wanglifei/Documents/论文写作` and keep run directories inside `workflows/auto-cn-research-paper-workflow/` or another explicit paper workspace. Use `python3` when the shell does not provide `python`.

Mac paths differ from the prior Windows trial:

- use `/Users/...` paths rather than `C:\Users\Administrator\...`;
- common tool locations include `~/.bun/bin`, `~/.local/bin`, `/opt/homebrew/bin`, and `/usr/local/bin`;
- `pro-cli` requires Bun, so missing Bun is an upstream blocker for the GPT Pro / GPT-5.5 Pro lane;
- Chrome profiles, native messaging host registration, and browser-control availability must be revalidated on the Mac instead of inherited from the Windows snapshot;
- keep Chinese paths, but prefer running scripts from the workspace root with relative run-directory paths when a tool shows encoding trouble.

At the start of a Mac run, write a readiness report:

```bash
python3 scripts/mac_readiness_report.py <run-dir-or-workspace>
```

Treat `bun_missing_for_pro_cli`, `pro_cli_missing`, missing Chrome, missing Claude, or `browser_hands_free_gate_requires_fresh_mac_validation` as active work items, not as reasons to weaken the final goal.

## Reusable Scripts

Use bundled scripts instead of rewriting the same mechanics:

- `scripts/init_run.py`: create a run directory from a theme with all required deliverable files.
- `scripts/mac_readiness_report.py`: record macOS tool readiness, including Python, Claude, pro-cli, Google Chrome, and active blockers inherited from the device switch.
- `scripts/ruc_cnki_entry.py`: record the official RUC Library CNKI journal database entry candidates and open the selected official entry in Chrome CDP. It may open the RUC login/SSO page, but it must not complete login, CAPTCHA, identity verification, or permission prompts.
- `scripts/chrome_cdp_probe.py`: record Chrome CDP tab-title and URL evidence without reading cookies, page storage, forms, or page text. Use it on Mac before claiming a Chrome/RUC/CNKI browser path is visible and controllable. The report includes `run_id` and `generated_at`; browser gates reject probes copied from another run.
- `scripts/topic_engine_audit.py`: verify `01_选题评分表.md` has 20-30 candidate topics, all required scoring dimensions, numeric score cells, exactly one `主选`, and exactly three `备选`. Run it before treating a user-provided theme as automatically narrowed into a usable topic.
- `scripts/source_file_audit.py`: verify that recorded source PDFs/HTML files and extracted text files exist on the current machine. Use it after device migration and before rebuilding `evidence_index.md`; Windows-era paths are not current Mac evidence.
- `scripts/source_rebuild_queue.py`: convert missing current-machine source files into `24_Mac材料重建队列.md`, classifying each formal source as public official PDF/HTML rebuild, RUC/CNKI re-download, or manual migration from the old device.
- `scripts/source_provenance_ledger.py`: create and validate `source_provenance_ledger.md`, recording each verified source's per-record run id, retrieval time, database/route URL, acquisition method, local file path, and sha256 hash when a PDF/user export is used. Validation rejects copied records whose run id does not match the current run directory.
- `scripts/extract_pdfs.py`: extract text from authorized downloaded PDFs and optionally write an extraction manifest. Point it at a task-specific PDF directory or pass `--pattern` to avoid unrelated downloads.
- `scripts/convert_kdh_caj.py`: convert locally downloaded CNKI KDH/CAJ files into repaired PDFs using PyMuPDF, then feed those PDFs into `extract_pdfs.py`. Use only for files already downloaded or exported through authorized access; never use online converters.
- `scripts/build_evidence_index.py`: build a page-level keyword and context index from extracted full text for citation location checks. Prefer relative paths from the workspace when Windows shell encoding corrupts Chinese absolute paths.
- `scripts/citation_plan.py`: map draft citation markers like `[1]` to verified matrix sources and page/location candidates.
- `scripts/citation_page_suggestions.py`: build a per-body-citation page-candidate table from `citation_plan.md`/`evidence_index.md` so final footnote polishing starts from source-backed page suggestions rather than manual searching.
- `scripts/citation_verify_passages.py`: create `citation_passage_verification.md`, a keyword/page-candidate table for body citations. It is stronger than raw reference mapping, but it is not final semantic passage verification and must not set `final_anchor_ready=yes` by itself.
- `scripts/citation_semantic_verify.py`: create `citation_semantic_verification.md`, a stricter paragraph-level semantic-alignment candidate table. It can reduce manual search work, but it remains an agent-generated candidate layer unless an accepted external/manual verification process explicitly promotes the anchors.
- `scripts/citation_final.py`: build `citation_final.md`, an anchoring worksheet that promotes source-backed page candidates into working anchors while blocking public reprint sources until primary PDF/database verification. By default these are not final citation-level page anchors. Use `--verified-citation-pages` only after external/manual citation-level passage-page verification; do not use keyword or semantic candidates alone as final anchors.
- `scripts/citation_evidence_workbench.py`: build `citation_evidence_workbench.md`, attaching source-page excerpts to every body citation so a human or visible ChatGPT/Claude reviewer can verify citation-level support. This workbench never finalizes anchors by itself; it keeps `citation_level_verified_anchors=0` and `final_anchor_ready=no`.
- `scripts/inventory_sources.py`: inventory downloaded PDFs/CAJ files, extracted text files, file headers, and evidence status.
- `scripts/queue_status.py`: summarize `10_候选下载队列.md`, user-verification waits, and the next candidate sources to try.
- `scripts/browser_gate_report.py`: write `12_浏览器准入验收.md` to record whether Chrome/Computer Use can actually control the authorized RUC/CNKI session without CAPTCHA, URL-confidence, or access-control blockers.
- `scripts/run_audit.py`: check required deliverables, verified full-text count, RUC proxy evidence, draft citation range, body-citation page suggestions, browser gate, primary-fulltext gate, external-review gate, policy-citation merge, and page-number readiness.
- `scripts/quality_gate_audit.py`: check text-quality gates before final review, including weak review-led paragraph openings, workflow/meta phrases in the draft, method-data fit, comparison-table honesty, research-design consistency, and conclusion boundary conditions. Review/backing verb counts are diagnostics only, not a pass/fail proof of quality.
- `scripts/workflow_report.py`: create a one-page status report combining full-text count, source inventory, evidence index, queue status, browser access, external review, policy-citation merge, page-number readiness, and user-verification waits.
- `scripts/workflow_gate_matrix.py`: run all major gates and write `16_总闸口矩阵.md`; use it before making any final completion claim.
- `scripts/external_review_orchestrator.py`: build sanitized prompt packs for Claude Opus and GPT Pro/GPT-5.5 Pro, run available CLI advisor lanes for non-final skill-building advice, save raw outputs, and update `15_外部评审与迭代计划.md` without pretending unavailable lanes ran. CLI/API lanes are not final approval for this user's paper goal; final pass must be recorded from visible web/app sessions.
- `scripts/final_review_packet.py`: build `25_引用页码终核包.md` and `26_最终外部评审包.md` for visible ChatGPT/Claude web/app review. Use it before final visible reviews so advisors see the draft, gate matrix, external-review status, and the rule that keyword-derived working anchors cannot be treated as final page numbers.
- `scripts/pdf_page_anchor_audit_pack.py`: build a visible PDF/page-image audit pack for disputed citation anchors by rendering source PDF pages from the provenance ledger and current citation workbench. Use it when a visible reviewer requires independent page-level verification beyond self-reported anchor tables.
- `scripts/visible_app_handoff.py`: prepare a manual visible-app advisor handoff on macOS by writing a pending prompt file, optionally copying it to the clipboard and opening the app. It never updates `15_外部评审与迭代计划.md`, never records `real_submission=true`, and never counts as a review.
- `scripts/visible_review_record.py`: record a final visible ChatGPT/Claude web or app review after the user or Codex has captured the visible review transcript/export/screenshot note. Use this, not CLI output, to update the final external-review gate.

When an external advisor returns `REVISE` or `CONDITIONAL_PASS`, convert it into `17_外部评审修订单.md` before editing the draft. Track each advisor suggestion as accept/reject/defer/needs verification and rerun `workflow_gate_matrix.py` after local changes.

Run scripts with UTF-8 enabled when the shell may mishandle Chinese paths. On macOS, prefer `python3 scripts/<name>.py` from the skill or workflow root and pass relative paths such as `运行_主题` and `fulltext_extract` when possible. In Windows workspaces with Chinese path segments, set the working directory to the project root and prefer relative arguments such as `.\试运行_主题` and `.\fulltext_extract` over long absolute Chinese paths.

## Visible Citation Review Ladder

Use this ladder after `citation_evidence_workbench.py` and before any final visible advisor approval.

1. Treat `citation_evidence_workbench.md` as a candidate review workbench. Statuses such as `visible_advisor_batch_pass_candidate`, `visible_advisor_repair_candidate`, or `visible_advisor_html_support_candidate_not_page_anchor` prove only candidate-level support, not final anchors.
2. Visible batch prompts should be small enough for strict review, usually about ten body-citation rows. Include the exact cited sentence, source id, candidate page/location, source excerpt, and a rule that the advisor must not browse the web or use adjacent citations as support.
3. If an advisor gives a broad batch pass but local evidence looks title-only, abstract-only, adjacent-context-only, or source-near rather than citation-exact, run a stricter repair prompt for those rows. Do not promote the row just because a broad batch response was positive.
4. An official HTML full text can support content, but it is not a formal page anchor unless the citation style explicitly accepts URL/location-only evidence. Mark it separately and keep `final_anchor_ready=no` until the page/location rule is solved.
5. `visible_reviewed_rows=all`, `rows_with_source_excerpt=all`, or `missing_excerpt=0` does not imply `citation_level_verified_anchors>0`. These are readiness facts, not final page-number facts.
6. After every visible citation batch or repair, rerun `citation_evidence_workbench.py`, `final_review_packet.py`, and `workflow_gate_matrix.py`. The final visible GPT/Claude review packet must still block `PASS` whenever `final_anchor_ready` is not `yes`.
7. If a final visible advisor returns `REVISE`, keep it as a work queue and record the raw response. If a final visible advisor returns `PASS` while the packet says `final_anchor_ready=no`, reject that as an invalid pass or resubmit a stricter prompt.

## Default Target

If the user does not specify the article type, target a graduate course paper rather than a journal submission or degree thesis. This keeps scope realistic while still requiring stronger structure than an undergraduate essay.

## Workflow

### 1. Intake and Scope

Start from the user's theme. Ask only for essential missing constraints if they change feasibility: discipline/course, target type, word count, deadline, citation style, required method, and available materials. If the user wants "hands-free", choose defaults and record them.

For a new run, initialize artifacts first:

```bash
python scripts/init_run.py --workspace <workspace> --theme "<theme>"
```

### 1.5 Text-Quality Design Gate

Before drafting, create a research-design spine that proves the paper is not just a literature pile:

- research object: a case, policy process, platform, actor group, corpus, or explicitly bounded secondary-comparison set; never only a broad concept such as "digital formalism";
- one-sentence thesis: no more than 80 Chinese characters when possible, with actor/object, mechanism, and boundary condition;
- core concept budget: no more than three core analytical concepts; all other concepts must be subordinate or background;
- preliminary puzzle gate before strong-paper imitation: state the paper's puzzle, single claim, falsification condition, and the existing explanation it replaces or extends before copying any strong-paper chapter structure;
- strong-paper craft comparison: identify how strong papers create problem consciousness, make concepts bite into evidence, handle rival explanations, and preserve author voice; do not copy chapter templates, typologies, case details, or mechanism words as decoration;
- method-data fit: the named method must match the available material. If there is no primary fieldwork, do not write as if there are interviews, surveys, or original cases. If the paper claims comparison, require same-dimension coding across the compared cases;
- pseudo-progress ban: source counts, SHA/full-text status, citation mapping, review/backing verb counts, and complete-looking chapter checklists are necessary diagnostics but never prove the argument is strong;
- paragraph-lead rule: mechanism/body paragraphs must be driven by the author's claim or material movement, not by "Author X points out..." review chaining. Use a deletion test: after removing sentences that only report another author's finding without connecting to the paper's claim, a coherent argument should remain.

If this gate fails, do not draft. If a later external advisor says the problem is structural, trigger a rewrite gate instead of continuing patch-level edits.

### 2. Topic Engine

Generate 20-30 candidate topics. Score them by literature availability, material availability, object clarity, method feasibility, originality risk, contribution modesty, and completion risk. Select one main topic and three backups.

Before moving to database search, run:

```bash
python scripts/topic_engine_audit.py <run-dir>
```

If the audit returns `INCOMPLETE`, fix `01_选题评分表.md` first. Do not treat a broad theme as solved merely because one promising title was chosen.

### 3. Search Plan

Generate at least three search-string groups:

- core concept searches;
- object/case/search-domain searches;
- method/theory/scenario searches.

Record each query in a search log. Use the table shape in `assets/deliverable_templates.md`.

### 4. Authorized Database Work

Use the user's logged-in and lawful RUC Library/CNKI/Wanfang/VIP/school-library browser session, or user-exported/downloaded files. Stop for user action at login, CAPTCHA, SSO, permission, payment, or download-confirmation screens.

For each candidate source, record title, author, source, year, database, URL/database path, visible abstract or summary, keywords, visible level, and verification status.

After authorized PDF downloads, extract readable text before drafting:

```bash
python scripts/extract_pdfs.py --pdf-dir <download-dir> --pattern "<task-pattern>" --out-dir <workspace>/fulltext_extract --manifest <run-dir>/fulltext_manifest.md --skip-existing
```

Then inventory usable and incomplete files:

```bash
python scripts/inventory_sources.py --download-dir <download-dir> --text-dir <workspace>/fulltext_extract --pattern "<task-pattern>" --out <run-dir>/source_inventory.md
python scripts/source_file_audit.py <run-dir> --min-current-fulltext 8 --search-root <workspace>
```

If `source_file_audit.py` reports Windows-era paths, missing source files, or missing extracted text, do not build the paper from those records. Generate the rebuild queue:

```bash
python scripts/source_rebuild_queue.py <run-dir>
```

Then migrate the files, re-download/re-export through authorized access, or re-run extraction on the current machine first. Public official PDFs/HTML may be fetched directly from the official URLs recorded in the queue; CNKI/RUC sources must still use the authorized browser route or old-device file migration.

If an authorized download yields a local KDH/CAJ file, try local conversion before treating it as unusable:

```bash
python scripts/convert_kdh_caj.py <downloaded.caj> --out-dir <workspace>/converted_caj --manifest <run-dir>/kdh_caj_conversion_manifest.md
python scripts/extract_pdfs.py --pdf-dir <workspace>/converted_caj --out-dir <workspace>/fulltext_extract --manifest <run-dir>/fulltext_manifest_converted_caj.md
```

Only promote a converted CAJ source into the formal literature matrix after the converted PDF opens, text extraction succeeds, and the source enters `source_inventory.md` plus `evidence_index.md`.

Build a page-level evidence index before citation polishing:

```bash
python scripts/source_file_audit.py <run-dir> --min-current-fulltext 8 --search-root <workspace>
python scripts/build_evidence_index.py --text-dir .\fulltext_extract --out .\<run-dir>\evidence_index.md
```

Map draft citations to source records and evidence pages:

```bash
python scripts/citation_plan.py .\<run-dir>
python scripts/citation_page_suggestions.py .\<run-dir>
python scripts/citation_verify_passages.py .\<run-dir>
python scripts/citation_semantic_verify.py .\<run-dir>
python scripts/citation_final.py .\<run-dir>
```

Treat `working_anchor_ready=yes` as a polishing aid, not a final submission gate. `final_anchor_ready=yes` requires manual or explicitly accepted external citation-level passage/page verification, not keyword-derived or agent semantic candidates alone.

Generate a one-page readiness report:

```bash
python scripts/workflow_report.py .\<run-dir> --target-fulltext 8
```

Interpret report fields strictly:

- `paper_material_ready=yes` means the paper evidence set has enough verified full-text material and citation/evidence indexing.
- `hands_free_workflow_ready=yes` means paper materials plus live authorized browser/database automation are both proven.
- `formal_ready=yes` is reserved for the user's final hands-free workflow target, not merely for an adequate paper draft.

When browser access is attempted or fails, first record the visible Chrome tab state:

```bash
python scripts/ruc_cnki_entry.py <run-dir> --open --mode offcampus
python scripts/chrome_cdp_probe.py <run-dir>
```

The RUC entry script opens the official CNKI journal database entry from the RUC Library electronic resources platform. This only proves the entry was opened. The CDP probe only proves the `tab_list` / `claim_url` tier. It does not prove search, page controls, download, user verification, or full-text access. If the selected URL is ChatGPT, a login page, a blank tab, or any non-RUC/CNKI page, the browser/database gate is still not ready.

Keep the browser gate in three separate layers:

1. CDP/browser path can read a tab title and URL.
2. The current tab is an authorized RUC/CNKI page.
3. A verified full text or user export exists and is recorded in `source_provenance_ledger.md` with matching run id, retrieval path, time, and local file hash when applicable.

Never describe layer 1 or 2 as source access. Only layer 3 can support paper evidence.

Then record the browser gate explicitly:

```bash
python scripts/browser_gate_report.py .\<run-dir> --browser-path-status fail --current-url-status unknown --computer-use-status fail
```

If `<run-dir>/chrome_cdp_probe.md` exists and the status arguments are left as `unknown`, `browser_gate_report.py` adopts the probe evidence for browser path and authorized URL status. Use `pass` only when the tool actually read the live title/URL and could interact with the authorized RUC/CNKI page. A user-completed CAPTCHA may clear the website, but it does not by itself prove that Codex can control the page.

Browser evidence is run-scoped. `browser_gate_report.py` must not adopt a `chrome_cdp_probe.md` whose `run_id` does not match the current run directory.

### 5. Literature Matrix and Evidence Ledger

Every source used in final writing must enter the literature matrix. Mark status as one of:

- `title_visible`;
- `abstract_visible`;
- `full_text_read`;
- `PDF_or_user_exported`;
- `needs_user_export`;
- `not_usable_yet`.

Only `full_text_read` and `PDF_or_user_exported` can support final paper claims.

For each `full_text_read` or `PDF_or_user_exported` source, record provenance:

```bash
python scripts/source_provenance_ledger.py <run-dir> --add --source-id S-001 --title "<title>" --database "CNKI via RUC Library" --route-url "<visible-or-recorded-route>" --method PDF_or_user_exported --local-file "<downloaded-or-exported-file>"
python scripts/source_provenance_ledger.py <run-dir> --validate
```

For browser-read full text without a local export, the ledger still needs database, route URL, retrieval time, and acquisition method. For PDF/user-exported files, sha256 is mandatory.

### 6. Strong-Paper Pattern Extraction

From verified full texts, extract reusable craft, not copied prose or chapter templates:

- how the author turns a broad theme into a research puzzle;
- how the author makes one core concept earn its place against the evidence;
- how the author moves from literature to a claim, not only to a topic list;
- how rival explanations are handled, narrowed, or absorbed;
- how materials are made comparable or bounded when cases differ;
- where the author voice dominates and where citations merely provide evidence;
- how conclusion force and boundary conditions are written.

Keep a short "do not copy" note for each strong-paper pattern.

### 7. Argument Spine

Build the paper around:

- title;
- main research question;
- two or three subquestions;
- central claim;
- chapter-function map;
- required evidence per chapter;
- likely objections and responses.

Each chapter must perform a clear function: define, review, describe, compare, analyze, explain, evaluate, or conclude.

### 8. Drafting

Draft only from verified or user-provided material. Keep claims bounded by the evidence. Avoid vague phrases, slogans, and inflated contribution claims. Include a claim-source table after the draft or maintain it as an audit artifact.

### 9. Audit

Before calling the run complete, audit:

- topic scope;
- research-question coherence;
- source traceability;
- full-text verification;
- citation/reference matching;
- method-material fit;
- unsupported claims;
- copied or over-close pattern imitation;
- overclaiming;
- missing appendices or exports.

Output issues as `must_fix`, `should_fix`, and `optional_polish`.

## Required Deliverables

For a complete run, create or update:

1. `选题评分表.md`
2. `检索日志.md`
3. `文献矩阵.md`
4. `优秀论文范式提取.md`
5. `论证骨架.md`
6. `论文初稿.md`
7. `引用与证据审查.md`
8. `终稿修改清单.md`
9. `完成度审计.md`

For interrupted CNKI runs, also create a candidate queue such as `10_候选下载队列.md` so the next turn resumes from visible candidates instead of rediscovering them.

Use `assets/deliverable_templates.md` for table and section shapes.

## Completion Standard

Do not claim the automatic research flow is complete unless current evidence proves:

- Chrome or another approved browser path is stable for the logged-in authorized database session;
- at least one live database search was completed;
- at least one result detail page was opened;
- at least one usable full text was downloaded or user-exported, or a clear export blocker was recorded;
- literature matrix and evidence ledger exist;
- strong-paper patterns came from verified full texts;
- the draft is based on traceable sources;
- page/location evidence exists for verified full texts, usually in `evidence_index.md`;
- every body citation has final citation-level anchors, not merely keyword, semantic, or visible-advisor candidate support;
- citation and evidence audits passed with no fabricated or unverified core claims.

For a formal graduate-course paper, target 8-12 verified full-text sources unless the user supplies a smaller course-specific requirement. Use `scripts/run_audit.py <run-dir> --min-fulltext 8` before claiming formal readiness. A run that pauses at CAPTCHA can be a valid partial run, but it is not "fully hands-free".

Before external final review, run the text-quality gate:

```bash
python scripts/quality_gate_audit.py <run-dir> --require-quality-plan --require-method-data-fit
```

If the title, method, or body claims case comparison, also run:

```bash
python scripts/quality_gate_audit.py <run-dir> --require-quality-plan --require-method-data-fit --require-comparison-table
```

Do not send a draft to Claude/GPT as a final review if this text-quality gate fails. Structural `REVISE` feedback from an advisor must become a rewrite task, not another patch list.

Before claiming the user's fully automatic workflow is achieved, also run:

```bash
python scripts/run_audit.py <run-dir> --min-fulltext 8 --require-browser-gate
```

The `--require-browser-gate` check must pass. Otherwise the evidence may support a partial paper run, but not a verified hands-free database workflow.

Before claiming material readiness for a real paper, require source provenance:

```bash
python scripts/run_audit.py <run-dir> --min-fulltext 8 --require-source-provenance
```

This must pass before a verified source can be treated as safely traceable. A literature matrix without `source_provenance_ledger.md` is a screening artifact, not final paper evidence.

For stricter final-submission readiness, especially when public reposts were used as temporary full-text evidence, run:

```bash
python scripts/run_audit.py <run-dir> --min-fulltext 8 --require-primary-fulltext
```

This must pass before claiming all formal sources are primary PDF, user-exported, or database full text.

Before claiming the final paper is ready for formal submission, also run:

```bash
python scripts/run_audit.py <run-dir> --min-fulltext 8 --require-policy-citation-merged --require-page-numbers
```

This must pass before claiming verified policy sources have entered the draft and references/page ranges are complete.

Before claiming the user's final external-review target is achieved, run:

```bash
python scripts/run_audit.py <run-dir> --min-fulltext 8 --require-source-id-freeze
python scripts/visible_review_record.py <run-dir> --lane gpt_pro --status pass --channel web_session --raw-record <visible-chatgpt-review-record>
python scripts/visible_review_record.py <run-dir> --lane claude_opus --status pass --channel app_session --raw-record <visible-claude-review-record>
python scripts/run_audit.py <run-dir> --min-fulltext 8 --require-external-review
```

The source-ID freeze audit must pass before external review so S/C source numbers are not silently reused after a source is demoted. The external-review gate must pass only after real visible web/app Claude Opus and GPT Pro/GPT-5.5 Pro review records exist, both say `pass`, each lane records channel, current run id, recorded time, raw record, and `real_submission=true`, and Codex has locally verified and adopted the required revisions. A single summary line such as `external_review_passed: yes` is insufficient unless the per-lane evidence fields also pass.

For an end-to-end completion audit, run:

```bash
python scripts/workflow_gate_matrix.py <run-dir> --min-fulltext 8
```

Only `final_user_goal_ready=yes` permits saying the user's hands-free automatic research-paper workflow has been achieved.
