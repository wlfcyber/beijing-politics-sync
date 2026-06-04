# Browser Access Gate

Use this gate before claiming that live RUC Library/CNKI automation is available.

## Required Checks

| Check | Evidence Required | Status Values |
| --- | --- | --- |
| Browser path | Chrome extension or approved browser-control path can read title and URL | pass / fail |
| User login | User personally completed RUC/CNKI login, CAPTCHA, SSO, or identity checks | pass / waiting_user |
| Authorized page | Current page is RUC Library database entry, CNKI home, CNKI search, or CNKI result page | pass / fail |
| Search | A test search was executed using task-relevant terms | pass / fail |
| Result detail | At least one result detail page was opened | pass / fail |
| Full text/export | Full text was opened/downloaded, or the need for user export was recorded | pass / blocked |
| Ledger | Search log and source status were recorded | pass / fail |

## Mac Revalidation Rule

When moving from the earlier Windows trial to this Mac, do not inherit browser readiness. Re-run the gate on the Mac and record fresh evidence:

- Chrome tab title and URL are readable from the active Mac browser-control path;
- the current page is the RUC Library portal, a `libproxy.ruc.edu.cn` CNKI page, or a task-relevant CNKI result/detail page;
- any RUC login, CAPTCHA, SSO, identity check, or download confirmation was completed by the user;
- a task-relevant search, result-detail open, and full-text/export attempt happened in the Mac session;
- the search log and source ledger were updated after the Mac run.

Old Windows evidence can explain the workflow design, but it cannot make `hands_free_ready: yes` on macOS.

## Run Artifact

For each live database run, generate or update `12_浏览器准入验收.md` with `scripts/browser_gate_report.py`.

On macOS, first generate `chrome_cdp_probe.md`:

```bash
python scripts/ruc_cnki_entry.py <run-dir> --open --mode offcampus
python scripts/chrome_cdp_probe.py <run-dir>
```

The entry script opens the official RUC Library CNKI journal database entry. The probe may prove that Chrome CDP can list a tab and read its title/URL. It is not enough for hands-free readiness unless the selected tab is an authenticated authorized RUC/CNKI page and later checks prove search, result-detail, and full-text/export flow. If the selected tab is `登录 - 中国人民大学`, SSO, CAPTCHA, slider, or identity verification, record `waiting_user`. The probe must not read cookies, browser passwords, local storage, form values, or page text. The probe must also carry the current run id; browser gate reports reject probes copied from a different run.

Keep these layers separate:

| Layer | Meaning | Evidence | Can support paper claims? |
| --- | --- | --- | --- |
| CDP visible | Chrome tab title and URL can be read | `chrome_cdp_probe.md` says `browser_path_status: pass` | no |
| Authorized URL | Current tab is RUC/CNKI or RUC proxy route | `chrome_cdp_probe.md` says `authorized_page_status: pass` | no |
| Source access | Full text or export exists and is recorded | `source_provenance_ledger.md` with route, retrieval time, and sha256 for files | yes |

Never use the first two layers as proof that Codex accessed source content.

The run is not hands-free unless the report says:

- `hands_free_ready: yes`;
- `browser_path_status: pass`;
- `current_url_status: pass`;
- `user_verification_status: pass`;
- RUC route, search, result detail, full text/export, and ledger checks are all `pass`.

Being able to list Chrome tabs is not enough. The browser controller must also read the current URL/title and interact with the authorized RUC/CNKI page without a CAPTCHA, identity check, download-confirmation blocker, or URL-confidence failure.

## Capability Tiers

Record the highest tier currently proven. Do not infer a higher tier from a lower one.

| Tier | Meaning | Enough for hands-free? |
| --- | --- | --- |
| `tab_list` | Can list open Chrome tabs and visible URLs | no |
| `claim_url` | Can claim a target tab and read title/URL | no |
| `screenshot` | Can capture a readable screenshot of the authorized page | no |
| `page_controls` | Can identify or operate page controls without timing out | no |
| `search_flow` | Can submit a task-relevant search and inspect results | no |
| `download_flow` | Can open a result detail page and download/open usable full text | yes, if all other evidence gates pass |

When a run proves only `screenshot` or lower, continue offline work and record the browser recovery attempt, but do not click download controls for new sources until the current URL and page controls are reliable.

## Stop Conditions

Stop and ask for user action when any of these appears:

- login page;
- CAPTCHA;
- `verify/home` safety-verification page;
- slider or puzzle verification;
- SSO or university identity page;
- payment, permission, or download confirmation;
- browser URL cannot be reliably determined by the automation tool;
- download limit or institutional access warning;
- full text is not visible and no user-exported PDF/CAJ is available.

## Allowed Evidence Labels

- `title_visible`: title or listing only; not usable for final claims.
- `abstract_visible`: abstract visible; usable for screening only.
- `full_text_read`: full text read through an authorized visible session; usable with location notes.
- `PDF_or_user_exported`: user-downloaded/exported file; usable after metadata check.
- `needs_user_export`: candidate source requires user export before final use.
- `not_usable_yet`: missing traceability or access.

## RUC Proxy Notes

- Prefer CNKI pages reached from the RUC Library portal and visible under `libproxy.ruc.edu.cn`.
- Result-page generic download links may yield CAJ; detail-page `PDF下载` is preferred when available.
- Directly opening CNKI `download/order` endpoints may fail source checks. Use visible page controls instead of constructing download URLs.
- If the user completes CAPTCHA or identity checks, resume from the current visible page and record the interruption and continuation in the search log.
