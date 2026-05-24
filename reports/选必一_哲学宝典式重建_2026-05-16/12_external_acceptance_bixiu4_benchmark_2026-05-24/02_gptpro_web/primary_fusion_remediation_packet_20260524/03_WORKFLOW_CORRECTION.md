# Workflow Correction - Claude App and Dual Production

## Why This File Exists

The user corrected two workflow defects on 2026-05-24:

1. Do not use Claude web for the final Opus / Adaptive review. Use the installed Claude desktop app.
2. ClaudeCode is not a reviewer lane. ClaudeCode must be an independent production lane, parallel to Codex.

This correction supersedes the earlier `PENDING_CLAUDE_WEB` status language.

## Correct Role Split

- Codex production lane A: independent source-backed thick draft and local evidence control.
- ClaudeCode production lane B: independent source-backed thick draft, not a structure-only reviewer.
- GPT Pro: primary fusion / deep content review after receiving Codex and ClaudeCode production outputs.
- Claude App Opus 4.7 Adaptive: final teaching-language and misuse-risk review after GPT Pro fusion.
- Codex after GPT/Claude: evidence backcheck, patch landing, Governor/Confucius, and GitHub sync.

## Current Evidence Reclassification

These existing files remain useful, but their authority is reclassified:

- `03_claude_opus/CLAUDE_CODE_OPUS_V6_REVIEW_CAPTURE_20260524.md`
- `03_claude_opus/CLAUDE_CODE_OPUS_V6_REVIEW2_CAPTURE_20260524.md`
- `03_claude_opus/CLAUDE_CODE_OPUS_AFTER_GPT_PASS_FALLBACK_CAPTURE_20260524.md`

They are local ClaudeCode QA / fallback checks only. They do not satisfy the required Claude App Opus / Adaptive gate, and they do not define ClaudeCode's main role.

## Evidence Gaps Still To Close

The current v6 has a real GPT Pro final PASS review, but the strict "Codex independent thick draft + ClaudeCode independent thick draft -> GPT Pro primary fusion" chain still needs an explicit full-body remediation capture, because the earlier `11_strict_final_rebuild_2026-05-23/07_gpt_pro_fusion/*CAPTURE.md` files captured stalled one-character outputs.

Therefore, until remediation is complete, the honest status is:

`PENDING_GPT_PRIMARY_FUSION_REMEDIATION_AND_CLAUDE_APP_REVIEW`

## Remediation Plan

1. Prepare a GPT Pro primary-fusion remediation packet using:
   - Codex independent production evidence;
   - ClaudeCode independent production evidence;
   - current v6 final student artifact;
   - local QA and anti-merge audit.
2. Submit that packet to a real GPT Pro conversation and save the full response.
3. Apply only source-verified must-fix changes.
4. Submit the resulting final artifact to the installed Claude desktop app with Opus 4.7 Adaptive selected.
5. Save Claude App output as the final Claude lane evidence.
6. Update final acceptance only after both real outputs are captured.
