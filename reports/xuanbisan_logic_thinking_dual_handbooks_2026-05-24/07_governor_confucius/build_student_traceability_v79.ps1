param(
  [string]$ProjectRoot = "",
  [string]$ThinkingArtifactPath = "",
  [string]$ReasoningArtifactPath = "",
  [string]$AliasPath = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
  $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$coveragePath = Join-Path $ProjectRoot '01_source_inventory\QUESTION_COVERAGE_MATRIX.csv'
$matrixPath = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv'
$summaryPath = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md'
$defaultAliasPath = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv'
$checkedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')

if ([string]::IsNullOrWhiteSpace($ThinkingArtifactPath) -or [string]::IsNullOrWhiteSpace($ReasoningArtifactPath)) {
  throw 'Pass -ThinkingArtifactPath and -ReasoningArtifactPath explicitly.'
}

$artifacts = @(
  @{
    artifact = 'thinking_framework'
    path = $ThinkingArtifactPath
  },
  @{
    artifact = 'reasoning_type'
    path = $ReasoningArtifactPath
  }
)

function Normalize-Text {
  param([string]$Value)
  if ($null -eq $Value) { return '' }
  $normalized = ($Value -replace '\s+', '')
  $normalized = $normalized.Replace([string][char]0xFF08, '(').Replace([string][char]0xFF09, ')')
  return $normalized.Trim()
}

function Get-PropertyValue {
  param(
    [object]$Object,
    [string]$Name
  )
  if ($null -eq $Object) { return '' }
  $property = $Object.PSObject.Properties | Where-Object { $_.Name -eq $Name } | Select-Object -First 1
  if ($null -eq $property) { return '' }
  return [string]$property.Value
}

function Split-SourceLabels {
  param([string]$Value)
  if ([string]::IsNullOrWhiteSpace($Value)) { return @() }
  $rawParts = @($Value -split '[,\uFF0C;\uFF1B\u3001]' | ForEach-Object { $_.Trim() } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
  $parts = New-Object System.Collections.Generic.List[string]
  foreach ($part in $rawParts) {
    if ($part -notmatch 'Q[0-9]+' -and $parts.Count -gt 0) {
      $parts[$parts.Count - 1] = ($parts[$parts.Count - 1] + ' ' + $part).Trim()
    } else {
      $parts.Add($part) | Out-Null
    }
  }
  return $parts.ToArray()
}

function Parse-SourceLabel {
  param([string]$Label)
  $trimmed = $Label.Trim().Trim('`').Replace([string][char]0xFF08, '(').Replace([string][char]0xFF09, ')')
  $pattern = '^(?<suite>.+?)\s*Q(?<question>[0-9]+(?:\([0-9A-Za-z]+\))?)(?<tail>.*)$'
  if ($trimmed -match $pattern) {
    return [pscustomobject]@{
      suite = $Matches.suite.Trim()
      question_no = $Matches.question.Trim()
      tail = $Matches.tail.Trim()
      parse_status = 'parsed'
    }
  }
  return [pscustomobject]@{
    suite = ''
    question_no = ''
    tail = ''
    parse_status = 'unparsed'
  }
}

function Find-CoverageRow {
  param(
    [object[]]$Coverage,
    [string]$Suite,
    [string]$QuestionNo,
    [string]$Tail = ''
  )
  $suiteNorm = Normalize-Text $Suite
  $questionNorm = Normalize-Text $QuestionNo
  $questionWithTailNorm = Normalize-Text ($QuestionNo + $Tail)
  foreach ($row in $Coverage) {
    $rowSuite = Normalize-Text (Get-PropertyValue $row 'suite_name')
    $rowQuestion = Normalize-Text (Get-PropertyValue $row 'question_no')
    if ($rowSuite -eq $suiteNorm -and $rowQuestion -eq $questionNorm) {
      return $row
    }
  }
  if ($questionWithTailNorm -ne $questionNorm) {
    foreach ($row in $Coverage) {
      $rowSuite = Normalize-Text (Get-PropertyValue $row 'suite_name')
      $rowQuestion = Normalize-Text (Get-PropertyValue $row 'question_no')
      if ($rowSuite -eq $suiteNorm -and $rowQuestion -eq $questionWithTailNorm) {
        return $row
      }
    }
  }
  foreach ($row in $Coverage) {
    $rowSuite = Normalize-Text (Get-PropertyValue $row 'suite_name')
    $rowQuestion = Normalize-Text (Get-PropertyValue $row 'question_no')
    if ($rowQuestion -eq $questionNorm -and $rowSuite.StartsWith($suiteNorm)) {
      return $row
    }
  }
  foreach ($row in $Coverage) {
    $rowSuite = Normalize-Text (Get-PropertyValue $row 'suite_name')
    $rowQuestion = Normalize-Text (Get-PropertyValue $row 'question_no')
    if ($rowQuestion -eq $questionNorm -and $suiteNorm.StartsWith($rowSuite)) {
      return $row
    }
  }
  return $null
}

function Import-TraceabilityAliases {
  param(
    [string]$Path,
    [string]$DefaultPath
  )

  $resolvedPath = ''
  if (-not [string]::IsNullOrWhiteSpace($Path)) {
    if ([IO.Path]::IsPathRooted($Path)) {
      $resolvedPath = $Path
    } else {
      $resolvedPath = Join-Path $ProjectRoot $Path
    }
    if (-not (Test-Path -LiteralPath $resolvedPath -PathType Leaf)) {
      throw "Missing alias table: $resolvedPath"
    }
  } elseif (Test-Path -LiteralPath $DefaultPath -PathType Leaf) {
    $resolvedPath = $DefaultPath
  }

  $map = @{}
  if ([string]::IsNullOrWhiteSpace($resolvedPath)) {
    return [pscustomobject]@{
      path = ''
      map = $map
    }
  }

  foreach ($row in @(Import-Csv -LiteralPath $resolvedPath)) {
    $label = (Get-PropertyValue $row 'alias_label').Trim()
    if ([string]::IsNullOrWhiteSpace($label)) { continue }
    if ($map.ContainsKey($label)) {
      throw "Duplicate traceability alias: $label"
    }
    $suite = (Get-PropertyValue $row 'target_suite').Trim()
    $questionNo = (Get-PropertyValue $row 'target_question_no').Trim()
    if ([string]::IsNullOrWhiteSpace($suite) -or [string]::IsNullOrWhiteSpace($questionNo)) {
      throw "Traceability alias lacks target suite/question: $label"
    }
    $map[$label] = [pscustomobject]@{
      suite = $suite
      question_no = $questionNo
      note = (Get-PropertyValue $row 'note').Trim()
    }
  }

  return [pscustomobject]@{
    path = $resolvedPath
    map = $map
  }
}

function Resolve-SourceLabelAliases {
  param(
    [string]$Label,
    [hashtable]$AliasMap
  )

  if ($null -eq $AliasMap -or $AliasMap.Count -eq 0) { return @() }
  $trimmed = $Label.Trim().Trim('`')
  if ([string]::IsNullOrWhiteSpace($trimmed)) { return @() }

  if ($AliasMap.ContainsKey($trimmed)) {
    $aliasTarget = $AliasMap[$trimmed]
    return @([pscustomobject]@{
      source_label = $trimmed
      suite = $aliasTarget.suite
      question_no = $aliasTarget.question_no
      tail = ''
      parse_status = 'alias'
      alias_label = $trimmed
      alias_note = $aliasTarget.note
    })
  }

  $tokens = @($trimmed -split '\s+' | ForEach-Object { $_.Trim() } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
  if ($tokens.Count -le 1) { return @() }
  foreach ($token in $tokens) {
    if (-not $AliasMap.ContainsKey($token)) {
      return @()
    }
  }

  $resolved = New-Object System.Collections.Generic.List[object]
  foreach ($token in $tokens) {
    $aliasTarget = $AliasMap[$token]
    $resolved.Add([pscustomobject]@{
      source_label = $token
      suite = $aliasTarget.suite
      question_no = $aliasTarget.question_no
      tail = ''
      parse_status = 'alias'
      alias_label = $token
      alias_note = $aliasTarget.note
    }) | Out-Null
  }
  return $resolved.ToArray()
}

function New-TraceRowsFromArtifact {
  param(
    [string]$ArtifactName,
    [string]$FullPath,
    [object[]]$Coverage,
    [hashtable]$AliasMap
  )

  if (-not (Test-Path -LiteralPath $FullPath -PathType Leaf)) {
    throw "Missing artifact: $FullPath"
  }

  $rows = New-Object System.Collections.Generic.List[object]
  $lines = Get-Content -LiteralPath $FullPath -Encoding UTF8
  $h2 = ''
  $h3 = ''
  $currentSection = $null
  $sectionIndex = 0

  function Flush-Section {
    if ($null -eq $script:currentSectionLocal) { return }
  }

  foreach ($line in $lines) {
    if ($line -match '^##\s+(.+)$' -and $line -notmatch '^###') {
      $h2 = $Matches[1].Trim()
      $h3 = ''
      continue
    }
    if ($line -match '^###\s+(.+)$' -and $line -notmatch '^####') {
      $h3 = $Matches[1].Trim()
      continue
    }
    if ($line -match '^####\s+(.+)$') {
      $sectionIndex += 1
      $currentSection = [ordered]@{
        section_index = $sectionIndex
        section_heading = $Matches[1].Trim()
        h2 = $h2
        h3 = $h3
        source_recorded = $false
      }
      continue
    }
    $trimmedLine = $line.Trim()
    if ($null -ne $currentSection -and -not $currentSection.source_recorded -and $trimmedLine -match 'Q[0-9]+' -and $trimmedLine -match '[:\uFF1A]') {
      $currentSection.source_recorded = $true
      $sourceText = ($trimmedLine -split '[:\uFF1A]', 2)[1]
      $sourceLabels = @(Split-SourceLabels $sourceText)
      if ($sourceLabels.Count -eq 0) {
        $sourceLabels = @('')
      }
      foreach ($sourceLabel in $sourceLabels) {
        $parsed = Parse-SourceLabel $sourceLabel
        if ($parsed.parse_status -eq 'parsed') {
          $traceTargets = @([pscustomobject]@{
            source_label = $sourceLabel
            suite = $parsed.suite
            question_no = $parsed.question_no
            tail = $parsed.tail
            parse_status = $parsed.parse_status
            alias_label = ''
            alias_note = ''
          })
        } else {
          $traceTargets = @(Resolve-SourceLabelAliases -Label $sourceLabel -AliasMap $AliasMap)
          if ($traceTargets.Count -eq 0) {
            $traceTargets = @([pscustomobject]@{
              source_label = $sourceLabel
              suite = $parsed.suite
              question_no = $parsed.question_no
              tail = $parsed.tail
              parse_status = $parsed.parse_status
              alias_label = ''
              alias_note = ''
            })
          }
        }

        foreach ($traceTarget in $traceTargets) {
          $matchedCoverage = $null
          if ($traceTarget.parse_status -ne 'unparsed') {
            $matchedCoverage = Find-CoverageRow -Coverage $Coverage -Suite $traceTarget.suite -QuestionNo $traceTarget.question_no -Tail $traceTarget.tail
          }
          $matched = $null -ne $matchedCoverage
          $rows.Add([pscustomobject]@{
            artifact = $ArtifactName
            artifact_file = (Resolve-Path -LiteralPath $FullPath).Path
            section_index = $currentSection.section_index
            chapter_path = (@($currentSection.h2, $currentSection.h3) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join ' / '
            section_heading = $currentSection.section_heading
            source_label = $traceTarget.source_label
            parsed_suite = $traceTarget.suite
            parsed_question_no = $traceTarget.question_no
            parse_status = $traceTarget.parse_status
            coverage_status = $(if ($matched) { 'matched' } elseif ($traceTarget.parse_status -ne 'unparsed') { 'unmatched' } else { 'unparsed' })
            alias_label = $traceTarget.alias_label
            alias_note = $traceTarget.alias_note
            question_id = $(if ($matched) { $matchedCoverage.question_id } else { '' })
            year = $(if ($matched) { $matchedCoverage.year } else { '' })
            district = $(if ($matched) { $matchedCoverage.district } else { '' })
            stage = $(if ($matched) { $matchedCoverage.stage } else { '' })
            suite_name = $(if ($matched) { $matchedCoverage.suite_name } else { '' })
            question_no = $(if ($matched) { $matchedCoverage.question_no } else { '' })
            book_part = $(if ($matched) { $matchedCoverage.book_part } else { '' })
            question_type = $(if ($matched) { $matchedCoverage.question_type } else { '' })
            evidence_level = $(if ($matched) { $matchedCoverage.evidence_level } else { '' })
            source_packet = $(if ($matched) { $matchedCoverage.source_packet } else { '' })
            source_status = $(if ($matched) { $matchedCoverage.status } else { '' })
            decision_reason = $(if ($matched) { $matchedCoverage.decision_reason } else { '' })
          }) | Out-Null
        }
      }
    }
  }

  return $rows.ToArray()
}

if (-not (Test-Path -LiteralPath $coveragePath -PathType Leaf)) {
  throw "Missing coverage matrix: $coveragePath"
}

$coverageRows = @(Import-Csv -LiteralPath $coveragePath)
$aliasImport = Import-TraceabilityAliases -Path $AliasPath -DefaultPath $defaultAliasPath
$aliasMap = $aliasImport.map
$allRows = New-Object System.Collections.Generic.List[object]
foreach ($artifact in $artifacts) {
  if ([IO.Path]::IsPathRooted($artifact.path)) {
    $artifactPath = $artifact.path
  } else {
    $artifactPath = Join-Path $ProjectRoot $artifact.path
  }
  $artifactRows = @(New-TraceRowsFromArtifact -ArtifactName $artifact.artifact -FullPath $artifactPath -Coverage $coverageRows -AliasMap $aliasMap)
  foreach ($row in $artifactRows) {
    $allRows.Add($row) | Out-Null
  }
}

$allRows | Export-Csv -LiteralPath $matrixPath -NoTypeInformation -Encoding UTF8

$total = $allRows.Count
$matched = @($allRows | Where-Object { $_.coverage_status -eq 'matched' }).Count
$unmatched = @($allRows | Where-Object { $_.coverage_status -eq 'unmatched' }).Count
$unparsed = @($allRows | Where-Object { $_.coverage_status -eq 'unparsed' }).Count
$thinkingRows = @($allRows | Where-Object { $_.artifact -eq 'thinking_framework' }).Count
$reasoningRows = @($allRows | Where-Object { $_.artifact -eq 'reasoning_type' }).Count
$uniqueQuestions = @($allRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.question_id) } | Select-Object -ExpandProperty question_id -Unique).Count

$summary = @()
$aliasDisplayPath = 'none'
if (-not [string]::IsNullOrWhiteSpace($aliasImport.path)) {
  $resolvedProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path.TrimEnd('\')
  $resolvedAliasPath = (Resolve-Path -LiteralPath $aliasImport.path).Path
  if ($resolvedAliasPath.StartsWith($resolvedProjectRoot + '\', [StringComparison]::OrdinalIgnoreCase)) {
    $aliasDisplayPath = $resolvedAliasPath.Substring($resolvedProjectRoot.Length + 1)
  } else {
    $aliasDisplayPath = $resolvedAliasPath
  }
}
$summary += '# Student Artifact Traceability Summary V79'
$summary += ''
$summary += 'Status: `TRACEABILITY_READY_PRE_EXTERNAL`'
$summary += ''
$summary += "- Checked at: $checkedAt"
$summary += "- Matrix: ``07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv``"
$summary += "- Alias table: ``$aliasDisplayPath``"
$summary += "- Thinking review base: ``$ThinkingArtifactPath``"
$summary += "- Reasoning review base: ``$ReasoningArtifactPath``"
$summary += ''
$summary += '## Counts'
$summary += ''
$summary += "- Total trace rows: ``$total``"
$summary += "- Thinking trace rows: ``$thinkingRows``"
$summary += "- Reasoning trace rows: ``$reasoningRows``"
$summary += "- Matched source labels: ``$matched``"
$summary += "- Unmatched source labels: ``$unmatched``"
$summary += "- Unparsed source labels: ``$unparsed``"
$summary += "- Unique matched question ids: ``$uniqueQuestions``"
$summary += ''
$summary += '## Guardrail'
$summary += ''
$summary += '- This matrix is a pre-external traceability control. It does not count as GPT Pro review, Claude review, Governor final pass, Confucius final pass, or Word/PDF QA.'
$summary += '- External-review suggestions still must be routed back through local source evidence before changing student-facing artifacts.'
$summary += ''

if ($unmatched -gt 0 -or $unparsed -gt 0) {
  $summary += '## Needs Attention'
  $summary += ''
  foreach ($row in @($allRows | Where-Object { $_.coverage_status -ne 'matched' } | Select-Object -First 30)) {
    $summary += "- $($row.artifact) section $($row.section_index): ``$($row.source_label)`` -> $($row.coverage_status)"
  }
  $summary += ''
}

Set-Content -LiteralPath $summaryPath -Value $summary -Encoding UTF8

if ($total -eq 0) {
  exit 2
}

exit 0
