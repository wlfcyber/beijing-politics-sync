$ErrorActionPreference = 'Stop'

function U {
  param([int[]]$Codes)
  return -join ($Codes | ForEach-Object { [char]$_ })
}

$Run = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$Desktop = [Environment]::GetFolderPath('Desktop')
$Years = @('2024','2025','2026')
$SourceRoots = foreach ($year in $Years) {
  Get-ChildItem -LiteralPath $Desktop -Directory |
    Where-Object { $_.Name -like "$year*" } |
    Sort-Object Name |
    Select-Object -First 1
}

$Districts = @(
  (U @(0x6d77,0x6dc0)),
  (U @(0x897f,0x57ce)),
  (U @(0x4e1c,0x57ce)),
  (U @(0x671d,0x9633)),
  (U @(0x4e30,0x53f0)),
  (U @(0x623f,0x5c71)),
  (U @(0x987a,0x4e49)),
  (U @(0x77f3,0x666f,0x5c71)),
  (U @(0x95e8,0x5934,0x6c9f)),
  (U @(0x5ef6,0x5e86)),
  (U @(0x901a,0x5dde)),
  (U @(0x660c,0x5e73)),
  (U @(0x5927,0x5174)),
  (U @(0x6000,0x67d4)),
  (U @(0x5e73,0x8c37)),
  (U @(0x5bc6,0x4e91)),
  (U @(0x71d5,0x5c71))
)
$Phases = @((U @(0x4e00,0x6a21)), (U @(0x4e8c,0x6a21)))

function Get-SourceSuites {
  $rows = @{}
  foreach ($root in $SourceRoots) {
    if (-not $root -or -not (Test-Path -LiteralPath $root.FullName)) { continue }
    $year = if ($root.Name -match '202[456]') { $Matches[0] } else { '' }
    Get-ChildItem -LiteralPath $root.FullName -Recurse -File | ForEach-Object {
      $rel = $_.FullName.Substring($root.FullName.Length + 1)
      $district = $null
      foreach ($d in $Districts) {
        if ($rel -like "*$d*") { $district = $d; break }
      }
      $phase = $null
      foreach ($ph in $Phases) {
        if ($rel -like "*$ph*") { $phase = $ph; break }
      }
      if ($district -and $phase) {
        $suite = "$year$district$phase"
        if (-not $rows.ContainsKey($suite)) {
          $rows[$suite] = [pscustomobject]@{
            suite = $suite
            year = $year
            phase = $phase
            source_example = $rel
          }
        }
      }
    }
  }
  return $rows.Values | Sort-Object suite
}

function Get-DocxText {
  param([string]$DocxPath)
  Add-Type -AssemblyName System.IO.Compression.FileSystem
  $zip = [System.IO.Compression.ZipFile]::OpenRead($DocxPath)
  try {
    $entry = $zip.GetEntry('word/document.xml')
    $reader = [IO.StreamReader]::new($entry.Open())
    try { $xml = $reader.ReadToEnd() } finally { $reader.Close() }
  } finally {
    $zip.Dispose()
  }
  $pattern = '<w:t[^>]*>(.*?)</w:t>'
  $matches = [regex]::Matches($xml, $pattern)
  return (($matches | ForEach-Object { [System.Net.WebUtility]::HtmlDecode($_.Groups[1].Value) }) -join '')
}

$Delivery = Join-Path $Run '05_delivery'
$Docx = Get-ChildItem -LiteralPath $Delivery -Filter '*.docx' | Where-Object { $_.Name -notlike '*backup*' } | Select-Object -First 1
if (-not $Docx) { throw "No final DOCX found in $Delivery" }

$DocText = Get-DocxText -DocxPath $Docx.FullName
$ClosurePath = Join-Path $Run '06_governor_confucius\COVERAGE_CLOSURE_MATRIX_V2.csv'
$ClosureSuites = @{}
if (Test-Path -LiteralPath $ClosurePath) {
  Import-Csv -LiteralPath $ClosurePath | ForEach-Object { $ClosureSuites[$_.suite] = $_.closure_status }
}

$Rows = foreach ($src in Get-SourceSuites) {
  $mentionCount = ([regex]::Matches($DocText, [regex]::Escape($src.suite))).Count
  [pscustomobject]@{
    suite = $src.suite
    year = $src.year
    phase = $src.phase
    source_example = $src.source_example
    final_docx_mentions = $mentionCount
    in_current_closure_matrix = [bool]$ClosureSuites.ContainsKey($src.suite)
    current_closure_status = if ($ClosureSuites.ContainsKey($src.suite)) { $ClosureSuites[$src.suite] } else { 'INHERITED_BASE_NOT_REOPENED_THIS_DELTA' }
    coverage_bucket = if ($mentionCount -gt 0 -and $ClosureSuites.ContainsKey($src.suite)) {
      'DELTA_OR_FIRST_MOCK_MATRIX_CLOSED'
    } elseif ($mentionCount -gt 0) {
      'DOCX_BASE_COVERED_NOT_REOPENED_THIS_DELTA'
    } else {
      'MISSING_FROM_FINAL_DOCX'
    }
  }
}

$OutDir = Join-Path $Run '06_governor_confucius'
$Csv = Join-Path $OutDir 'FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv'
$Md = Join-Path $OutDir 'FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.md'
$Rows | Export-Csv -LiteralPath $Csv -NoTypeInformation -Encoding UTF8

$Total = @($Rows).Count
$Missing = @($Rows | Where-Object { $_.coverage_bucket -eq 'MISSING_FROM_FINAL_DOCX' }).Count
$MatrixClosed = @($Rows | Where-Object { $_.coverage_bucket -eq 'DELTA_OR_FIRST_MOCK_MATRIX_CLOSED' }).Count
$Inherited = @($Rows | Where-Object { $_.coverage_bucket -eq 'DOCX_BASE_COVERED_NOT_REOPENED_THIS_DELTA' }).Count

$Lines = @()
$Lines += '# Full Source vs DOCX Coverage Audit 2026-05-24'
$Lines += ''
$Lines += ("Final DOCX: " + $Docx.FullName)
$Lines += ''
$Lines += '## Summary'
$Lines += ''
$Lines += '| item | count |'
$Lines += '|---|---:|'
$Lines += "| raw source suites detected from Desktop 2024-2026 first/second mock folders | $Total |"
$Lines += "| suites present in final DOCX and current closure matrix | $MatrixClosed |"
$Lines += "| suites present in final DOCX but inherited from accepted base, not reopened in this delta | $Inherited |"
$Lines += "| suites missing from final DOCX | $Missing |"
$Lines += ''
$Lines += '## Boundary'
$Lines += ''
$Lines += '- This audit proves suite-name coverage in the final DOCX against the current Desktop source folders.'
$Lines += '- It does not independently re-score every inherited 2024/2025 second-mock row; those rows are treated as base-handbook coverage unless a separate row-level rerun is ordered.'
$Lines += '- The 2024-2026 first-mock plus 2026 second-mock delta closure is still governed by `COVERAGE_CLOSURE_MATRIX_V2.csv`.'
$Lines += ''
$Lines += '## Suites'
$Lines += ''
$Lines += '| suite | final_docx_mentions | current_closure_status | coverage_bucket | source_example |'
$Lines += '|---|---:|---|---|---|'
foreach ($row in $Rows) {
  $safeExample = $row.source_example -replace '\|','/'
  $Lines += "| $($row.suite) | $($row.final_docx_mentions) | $($row.current_closure_status) | $($row.coverage_bucket) | $safeExample |"
}

$Lines | Set-Content -LiteralPath $Md -Encoding UTF8

Write-Output $Csv
Write-Output $Md
Write-Output "total=$Total matrix_closed=$MatrixClosed inherited=$Inherited missing=$Missing"
