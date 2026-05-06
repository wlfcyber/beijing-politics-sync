# Governor Entry Boundary Scan 2026-05-02

## Scope

- scanned: `codex_lane/entries/*.md`
- result: 16 entry files, 97 term entries
- required-field check: pass
- answer-sentence forbidden-language check: pass

## Bucket Counts

- 中国：23
- 经济全球化：19
- 理论：8
- 政治多极化：30
- 联合国：9
- 时代背景：8

## Boundary Decisions

### 2026朝阳期中 Q17

- finding: `经济平稳可持续发展 / 高质量发展 / 注入新动能...` can look like 必修二 if lifted out alone.
- decision: retain only as the development-side subpoint under `处理好发展和安全的关系`.
- edit made: moved from `经济全球化` to `理论`.
- final-doc rule: do not promote this group into an independent 必修二-style node.

### 2024东城一模 Q20

- finding: prompt says `运用经济的相关知识`, but rubric contains `对标国际规则`、`制度型开放`、`深入融入经济全球化`、`两个市场两种资源`.
- decision: keep as cross-book confirmed evidence because the scoring source explicitly gives 选必一-compatible terms.
- final-doc rule: preserve the source boundary; do not turn `高质量发展` or generic `新发展格局` into standalone 选必一术语.

### 2026门头沟一模 Q20

- finding: contains domestic-growth effects and open-world effects.
- decision: keep only the economic-globalization and opening terms; do not elevate domestic growth language into the 选必一 main chain.

## Language Scan Notes

- `答案句` lines have no hits for `材料中`、`采分点`、`要落到`、`细则要求`、`本题需要`、paths, debug/state fields, or version chatter.
- Some `材料触发` fields still use audit phrasing such as `设问要求`. These are acceptable in the audit entry layer but must be rewritten before generating the student-facing document.

## ClaudeCode Difference

- ClaudeCode currently records `2026西城期末 Q20` as `blocked_missing_full_prompt` because its restart prompt limited source search to the three Desktop source roots.
- Codex resolved the blocker by finding the synced teacher PDF in `/Users/wanglifei/GaokaoPolitics/2026各区模拟题/...`.
- Fusion rule: keep the ClaudeCode blocker as useful evidence of the Desktop-source gap, but do not let it override the later Codex source recovery.
