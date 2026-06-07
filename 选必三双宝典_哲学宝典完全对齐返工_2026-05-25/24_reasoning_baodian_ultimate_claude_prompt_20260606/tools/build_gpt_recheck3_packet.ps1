param([int]$Round = 3)

$ErrorActionPreference = "Stop"
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$enc = [System.Text.UTF8Encoding]::new($false)

$roundNames = @{ 3 = "Third"; 4 = "Fourth"; 5 = "Fifth"; 6 = "Sixth"; 7 = "Seventh"; 8 = "Post-Source" }
$roundName = $roundNames[$Round]
if (-not $roundName) {
  $roundName = "Round $Round"
}

$out = "external_review\CHATGPT_PRO_RECHECK${Round}_PACKET_20260606.md"
$finalMarkdownPath = (Get-ChildItem -LiteralPath "delivery" -Filter "*.md" | Select-Object -First 1).FullName
$sections = @(
  @{ Title = "WEB_MODEL_REVIEW_PROMPT"; Path = "external_review\WEB_MODEL_REVIEW_PROMPT_20260606.md" },
  @{ Title = "CLAUDE_CODE_COWORK_RECHECK_RESULT"; Path = "external_review\CLAUDE_CODE_COWORK_RECHECK_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_INITIAL_BLOCK_RESULT"; Path = "external_review\CHATGPT_PRO_REVIEW_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_FIRST_RECHECK_BLOCK_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_SECOND_RECHECK_BLOCK_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK2_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_THIRD_RECHECK_REVISE_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK3_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_FOURTH_RECHECK_REVISE_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK4_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_FIFTH_RECHECK_REVISE_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK5_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_SIXTH_RECHECK_REVISE_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK6_RESULT_20260606.md" },
  @{ Title = "GPT_PRO_SEVENTH_RECHECK_ACCEPT_RESULT"; Path = "external_review\CHATGPT_PRO_RECHECK7_RESULT_20260606.md" },
  @{ Title = "CLAUDE_CHAT_OPUS_FINAL_ACCEPT_RESULT"; Path = "external_review\CLAUDE_CHAT_OPUS_FINAL_REVIEW_RESULT_20260606.md" },
  @{ Title = "POST_SOURCE_TRI_REVIEW_SOURCE_EVIDENCE"; Path = "external_review\POST_SOURCE_TRI_REVIEW_SOURCE_EVIDENCE_20260606.md" },
  @{ Title = "FINAL_ACCEPTANCE_REPORT"; Path = "FINAL_ACCEPTANCE_REPORT.md" },
  @{ Title = "QA_REPORT"; Path = "qa\QA_REPORT_V24_20260606.md" },
  @{ Title = "QA_GATES_JSON"; Path = "qa\QA_GATES_V24_20260606.json" },
  @{ Title = "PDF_RENDER_QA_JSON"; Path = "qa\PDF_RENDER_QA_V24_20260606.json" },
  @{ Title = "DEFECT_LEDGER_CSV"; Path = "qa\DEFECT_LEDGER_V24_20260606.csv" },
  @{ Title = "CHANGELOG"; Path = "qa\CHANGELOG_V24_20260606.md" },
  @{ Title = "FINAL_MARKDOWN_ARTIFACT"; Path = $finalMarkdownPath }
)
if ($Round -eq 3) {
  $sections = $sections | Where-Object { $_.Title -ne "GPT_PRO_THIRD_RECHECK_REVISE_RESULT" -and $_.Title -ne "GPT_PRO_FOURTH_RECHECK_REVISE_RESULT" -and $_.Title -ne "GPT_PRO_FIFTH_RECHECK_REVISE_RESULT" -and $_.Title -ne "GPT_PRO_SIXTH_RECHECK_REVISE_RESULT" }
}
if ($Round -eq 4) {
  $sections = $sections | Where-Object { $_.Title -ne "GPT_PRO_FOURTH_RECHECK_REVISE_RESULT" -and $_.Title -ne "GPT_PRO_FIFTH_RECHECK_REVISE_RESULT" -and $_.Title -ne "GPT_PRO_SIXTH_RECHECK_REVISE_RESULT" }
}
if ($Round -eq 5) {
  $sections = $sections | Where-Object { $_.Title -ne "GPT_PRO_FIFTH_RECHECK_REVISE_RESULT" -and $_.Title -ne "GPT_PRO_SIXTH_RECHECK_REVISE_RESULT" }
}
if ($Round -eq 6) {
  $sections = $sections | Where-Object { $_.Title -ne "GPT_PRO_SIXTH_RECHECK_REVISE_RESULT" }
}
if ($Round -lt 8) {
  $sections = $sections | Where-Object { $_.Title -ne "GPT_PRO_SEVENTH_RECHECK_ACCEPT_RESULT" -and $_.Title -ne "CLAUDE_CHAT_OPUS_FINAL_ACCEPT_RESULT" -and $_.Title -ne "POST_SOURCE_TRI_REVIEW_SOURCE_EVIDENCE" }
}

$builder = [System.Text.StringBuilder]::new()
[void]$builder.AppendLine("# ChatGPT Pro $roundName Recheck Packet")
[void]$builder.AppendLine("")
[void]$builder.AppendLine("Please run an external recheck after the latest local repair pass. The local artifact has been regenerated and QA/PDF checks rerun after repairing the latest review findings.")
[void]$builder.AppendLine("")
[void]$builder.AppendLine("Specific retest targets:")
[void]$builder.AppendLine("")
if ($Round -eq 8) {
  [void]$builder.AppendLine("1. Review the current source-complete artifact after the final Haidian Q20(1) source recovery.")
  [void]$builder.AppendLine("2. Confirm the earlier neutral missing-source state is obsolete: the defect ledger now has 0 rows and no entry remains neutralized for missing source.")
  [void]$builder.AppendLine("3. Check the recovered Haidian Q20(1) six-layer entry against the source-evidence note: reasoning type, correctness judgment, and affirming-the-consequent explanation.")
  [void]$builder.AppendLine("4. Re-check that answer layers are student-copyable and not copied from thinking/rubric layers.")
  [void]$builder.AppendLine("5. Re-check language for template tone, backend traces, broken punctuation, OCR/page residue, material/answer mismatch, and answer-layer incompleteness.")
} elseif ($Round -eq 7) {
  [void]$builder.AppendLine("1. Confirm the sixth-recheck REVISE items are closed: the Shijingshan option-set sync, the Xicheng table-flow cleanup, and the Fengtai broken score-tail removal.")
  [void]$builder.AppendLine("2. Confirm expanded G13 currently reports zero visible text break hits for option-set mismatch, repeated table headers, and broken score-tail fragments.")
  [void]$builder.AppendLine("3. Re-sample fifth-recheck repairs: scientificity line break, definition-narrowness quote, missing-source process wording, and title residue.")
  [void]$builder.AppendLine("4. Re-sample prior material-layer repairs, the two neutral missing-source entries, and answer-layer completeness.")
  [void]$builder.AppendLine("5. Re-check language for template tone, backend traces, broken punctuation, and answer-layer incompleteness.")
} elseif ($Round -eq 6) {
  [void]$builder.AppendLine("1. Confirm the fifth-recheck REVISE items are closed: the scientificity line break, the missing left quote before definition-narrowness, missing-source process wording, and revision-title residue.")
  [void]$builder.AppendLine("2. Confirm expanded G13 currently reports zero visible text break hits for these newest patterns.")
  [void]$builder.AppendLine("3. Re-sample prior fourth-recheck material repairs: city OCR, AT1/GS3 material OCR, AI-analysis table flow, and the two-conclusion AI answer layer.")
  [void]$builder.AppendLine("4. Re-sample prior material-layer repairs, the two neutral missing-source entries, and answer-layer completeness.")
  [void]$builder.AppendLine("5. Re-check language for template tone, backend traces, broken punctuation, and answer-layer incompleteness.")
} elseif ($Round -eq 5) {
  [void]$builder.AppendLine("1. Confirm the fourth-recheck REVISE items are closed: the city-name OCR, the AT1/GS3 material OCR, and the AI-analysis table flow.")
  [void]$builder.AppendLine("2. Confirm the updated answer for the AI-analysis item covers both AI conclusions, not only the contradiction-law part.")
  [void]$builder.AppendLine("3. Confirm expanded G13 currently reports zero visible text break hits and catches the latest OCR patterns.")
  [void]$builder.AppendLine("4. Re-sample prior material-layer repairs, the two neutral missing-source entries, and answer-layer completeness.")
  [void]$builder.AppendLine("5. Re-check language for template tone, backend traces, broken punctuation, and answer-layer incompleteness.")
} elseif ($Round -eq 4) {
  [void]$builder.AppendLine("1. Confirm the third-recheck REVISE item about the broken rubric chain is closed.")
  [void]$builder.AppendLine("2. Confirm the third-recheck REVISE item about OCR-fragment material layers is closed.")
  [void]$builder.AppendLine("3. Confirm expanded G13 evidence catches these issues and currently reports zero visible text break hits.")
  [void]$builder.AppendLine("4. Re-sample prior material-layer repairs, the two neutral missing-source entries, and answer-layer completeness.")
  [void]$builder.AppendLine("5. Re-check language for template tone, backend traces, broken punctuation, and answer-layer incompleteness.")
} else {
  [void]$builder.AppendLine("1. Confirm the first second-recheck blocker no longer contains the visible residual ellipsis phrase and that its focus sentence is complete.")
  [void]$builder.AppendLine("2. Confirm the second second-recheck blocker now reaches the final required conclusion, not only the intermediate conclusion.")
  [void]$builder.AppendLine("3. Confirm the third second-recheck blocker explains why the required option pair is necessary and why the other candidates are not stable.")
  [void]$builder.AppendLine("4. Re-sample the previously fixed material-layer issues and the two neutral missing-source entries.")
  [void]$builder.AppendLine("5. Re-check language for template tone, backend traces, broken punctuation, and answer-layer incompleteness.")
}
[void]$builder.AppendLine("")
[void]$builder.AppendLine("Use the same output shape as the review prompt. Verdict must be ACCEPT / REVISE / BLOCK. Treat external review as advisory only; do not invent original paper material or scoring rules.")
[void]$builder.AppendLine("")

foreach ($section in $sections) {
  [void]$builder.AppendLine("---")
  [void]$builder.AppendLine("")
  [void]$builder.AppendLine("## " + $section.Title)
  [void]$builder.AppendLine("")
  if ([System.IO.Path]::IsPathRooted($section.Path)) {
    $sourceLabel = "delivery\" + (Split-Path -Leaf $section.Path)
  } else {
    $sourceLabel = $section.Path
  }
  [void]$builder.AppendLine("Source file: " + $sourceLabel)
  [void]$builder.AppendLine("")
  if ([System.IO.Path]::IsPathRooted($section.Path)) {
    $fullPath = $section.Path
  } else {
    $fullPath = Join-Path (Get-Location) $section.Path
  }
  [void]$builder.AppendLine([System.IO.File]::ReadAllText($fullPath, $enc))
  [void]$builder.AppendLine("")
}

[System.IO.File]::WriteAllText((Join-Path (Get-Location) $out), $builder.ToString(), $enc)
Get-Item $out | Select-Object FullName, Length, LastWriteTime
