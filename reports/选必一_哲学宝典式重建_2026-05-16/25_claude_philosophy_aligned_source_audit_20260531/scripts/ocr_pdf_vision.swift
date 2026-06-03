import AppKit
import Foundation
import PDFKit
import Vision

func fail(_ message: String) -> Never {
    fputs(message + "\n", stderr)
    exit(1)
}

if CommandLine.arguments.count < 3 {
    fail("usage: swift ocr_pdf_vision.swift INPUT.pdf OUTPUT.txt [maxPages]")
}

let inputURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2])
let maxPages = CommandLine.arguments.count >= 4 ? Int(CommandLine.arguments[3]) : nil

guard let document = PDFDocument(url: inputURL) else {
    fail("Cannot open PDF: \(inputURL.path)")
}

let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.recognitionLanguages = ["zh-Hans", "en-US"]
request.usesLanguageCorrection = true

var allLines: [String] = []
let pageCount = min(document.pageCount, maxPages ?? document.pageCount)

for pageIndex in 0..<pageCount {
    guard let page = document.page(at: pageIndex) else { continue }
    let bounds = page.bounds(for: .mediaBox)
    let scale: CGFloat = 2.0
    let imageSize = NSSize(width: bounds.width * scale, height: bounds.height * scale)
    let image = NSImage(size: imageSize)

    image.lockFocus()
    guard let nsContext = NSGraphicsContext.current else {
        image.unlockFocus()
        continue
    }
    let ctx = nsContext.cgContext
    NSColor.white.setFill()
    ctx.fill(CGRect(origin: .zero, size: imageSize))
    ctx.saveGState()
    ctx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx)
    ctx.restoreGState()
    image.unlockFocus()

    guard
        let tiff = image.tiffRepresentation,
        let rep = NSBitmapImageRep(data: tiff),
        let cgImage = rep.cgImage
    else {
        allLines.append("[page \(pageIndex + 1)] <render failed>")
        continue
    }

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    do {
        try handler.perform([request])
        let observations = (request.results as? [VNRecognizedTextObservation]) ?? []
        let lines = observations.compactMap { $0.topCandidates(1).first?.string }
        allLines.append("[page \(pageIndex + 1)]")
        allLines.append(contentsOf: lines)
    } catch {
        allLines.append("[page \(pageIndex + 1)] <ocr failed: \(error)>")
    }
}

let output = allLines.joined(separator: "\n")
try output.write(to: outputURL, atomically: true, encoding: .utf8)
print("OCR \(inputURL.lastPathComponent): \(pageCount) pages -> \(outputURL.path)")
