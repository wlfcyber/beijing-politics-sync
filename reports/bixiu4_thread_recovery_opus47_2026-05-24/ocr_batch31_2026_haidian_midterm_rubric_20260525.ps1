param(
    [string]$RenderDir = "C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\e65381bd22912637",
    [string]$OutText = "",
    [string]$OutLines = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
Add-Type -AssemblyName System.Runtime.WindowsRuntime

if ([string]::IsNullOrWhiteSpace($OutText)) {
    $OutText = Join-Path $PSScriptRoot "BATCH31_2026_HAIDIAN_MIDTERM_RUBRIC_OCR_TRANSCRIPTION_20260525.md"
}
if ([string]::IsNullOrWhiteSpace($OutLines)) {
    $OutLines = Join-Path $PSScriptRoot "BATCH31_2026_HAIDIAN_MIDTERM_RUBRIC_OCR_LINES_20260525.md"
}

$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.IRandomAccessStreamWithContentType, Windows.Storage.Streams, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapPixelFormat, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapAlphaMode, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrResult, Windows.Media.Ocr, ContentType = WindowsRuntime]
$null = [Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime]

$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() |
    Where-Object {
        $_.Name -eq "AsTask" -and
        $_.IsGenericMethodDefinition -and
        $_.GetParameters().Count -eq 1 -and
        $_.ReturnType.Name -eq "Task``1" -and
        $_.GetGenericArguments().Count -eq 1
    } |
    Select-Object -First 1
if ($null -eq $asTaskGeneric) {
    throw "Unable to find WindowsRuntimeSystemExtensions.AsTask(IAsyncOperation<T>)."
}

function Await-Operation($Operation, [Type]$ResultType) {
    $task = $asTaskGeneric.MakeGenericMethod($ResultType).Invoke($null, @($Operation))
    $task.Wait()
    return $task.Result
}

$language = [Windows.Globalization.Language]::new("zh-Hans-CN")
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($language)
if ($null -eq $engine) {
    throw "Windows OCR engine zh-Hans-CN is unavailable."
}

$images = Get-ChildItem -LiteralPath $RenderDir -Filter "page_*.png" | Sort-Object Name
if ($images.Count -eq 0) {
    throw "No rendered page images found in $RenderDir"
}

$textBuilder = [System.Text.StringBuilder]::new()
$lineBuilder = [System.Text.StringBuilder]::new()

$null = $textBuilder.AppendLine("# Batch31 OCR Transcription - 2026 Haidian Midterm Rubric")
$null = $textBuilder.AppendLine("")
$null = $textBuilder.AppendLine('status: `RUBRIC_OCR_GENERATED`')
$null = $textBuilder.AppendLine("")
$null = $textBuilder.AppendLine(('- rubric render dir: `{0}`' -f $RenderDir))
$null = $textBuilder.AppendLine("- OCR engine: Windows.Media.Ocr zh-Hans-CN")
$null = $textBuilder.AppendLine(('- rendered page count: `{0}`' -f $images.Count))
$null = $textBuilder.AppendLine("")
$null = $textBuilder.AppendLine("## Rubric Pages")
$null = $textBuilder.AppendLine("")

$null = $lineBuilder.AppendLine("# Batch31 OCR Lines - 2026 Haidian Midterm Rubric")
$null = $lineBuilder.AppendLine("")
$null = $lineBuilder.AppendLine('status: `RUBRIC_OCR_GENERATED`')
$null = $lineBuilder.AppendLine("")

foreach ($image in $images) {
    $stream = $null
    $bitmap = $null
    try {
        $file = Await-Operation ([Windows.Storage.StorageFile]::GetFileFromPathAsync($image.FullName)) ([Windows.Storage.StorageFile])
        $stream = Await-Operation ($file.OpenReadAsync()) ([Windows.Storage.Streams.IRandomAccessStreamWithContentType])
        $decoder = Await-Operation ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
        $bitmap = Await-Operation ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
        if ($bitmap.BitmapPixelFormat -ne [Windows.Graphics.Imaging.BitmapPixelFormat]::Bgra8 -or $bitmap.BitmapAlphaMode -ne [Windows.Graphics.Imaging.BitmapAlphaMode]::Premultiplied) {
            $converted = [Windows.Graphics.Imaging.SoftwareBitmap]::Convert(
                $bitmap,
                [Windows.Graphics.Imaging.BitmapPixelFormat]::Bgra8,
                [Windows.Graphics.Imaging.BitmapAlphaMode]::Premultiplied
            )
            $bitmap.Dispose()
            $bitmap = $converted
        }
        $result = Await-Operation ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
        $pageLines = @($result.Lines | ForEach-Object { $_.Text })

        $null = $textBuilder.AppendLine("### $($image.Name)")
        $null = $textBuilder.AppendLine("")
        $null = $textBuilder.AppendLine('```text')
        foreach ($line in $pageLines) {
            $null = $textBuilder.AppendLine($line)
        }
        $null = $textBuilder.AppendLine('```')
        $null = $textBuilder.AppendLine("")

        $null = $lineBuilder.AppendLine("### $($image.Name)")
        $null = $lineBuilder.AppendLine("")
        $lineNo = 1
        foreach ($line in $pageLines) {
            $null = $lineBuilder.AppendLine(("{0:D3}: {1}" -f $lineNo, $line))
            $lineNo++
        }
        $null = $lineBuilder.AppendLine("")
    }
    finally {
        if ($null -ne $bitmap) { $bitmap.Dispose() }
        if ($null -ne $stream) { $stream.Dispose() }
    }
}

[System.IO.File]::WriteAllText($OutText, $textBuilder.ToString(), [System.Text.UTF8Encoding]::new($false))
[System.IO.File]::WriteAllText($OutLines, $lineBuilder.ToString(), [System.Text.UTF8Encoding]::new($false))
Write-Output "OCR complete: $($images.Count) pages"
Write-Output $OutText
Write-Output $OutLines
