import Foundation
import PDFKit
import AppKit

if CommandLine.arguments.count < 4 {
    fputs("usage: render_pdf_pages.swift input.pdf out_dir page[,page...] [scale]\n", stderr)
    exit(2)
}

let input = CommandLine.arguments[1]
let outDir = CommandLine.arguments[2]
let pages = CommandLine.arguments[3].split(separator: ",").compactMap { Int($0.trimmingCharacters(in: .whitespaces)) }
let scale = CommandLine.arguments.count > 4 ? (Double(CommandLine.arguments[4]) ?? 2.0) : 2.0

guard let doc = PDFDocument(url: URL(fileURLWithPath: input)) else {
    fputs("cannot open pdf\n", stderr)
    exit(1)
}

try FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)

for pageNo in pages {
    guard pageNo >= 1, pageNo <= doc.pageCount, let page = doc.page(at: pageNo - 1) else {
        fputs("skip invalid page \(pageNo)\n", stderr)
        continue
    }
    let bounds = page.bounds(for: .mediaBox)
    let width = Int(bounds.width * scale)
    let height = Int(bounds.height * scale)
    let image = page.thumbnail(of: NSSize(width: width, height: height), for: .mediaBox)
    guard let tiff = image.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff),
          let data = rep.representation(using: .png, properties: [:]) else {
        fputs("cannot render thumbnail for page \(pageNo)\n", stderr)
        continue
    }
    let out = URL(fileURLWithPath: outDir).appendingPathComponent(String(format: "page-%03d.png", pageNo))
    try data.write(to: out)
    print(out.path)
    /*
    guard let rep = NSBitmapImageRep(
        bitmapDataPlanes: nil,
        pixelsWide: width,
        pixelsHigh: height,
        bitsPerSample: 8,
        samplesPerPixel: 4,
        hasAlpha: true,
        isPlanar: false,
        colorSpaceName: .deviceRGB,
        bytesPerRow: 0,
        bitsPerPixel: 0
    ) else {
        fputs("cannot create bitmap for page \(pageNo)\n", stderr)
        continue
    }
    rep.size = NSSize(width: bounds.width, height: bounds.height)
    NSGraphicsContext.saveGraphicsState()
    let ctx = NSGraphicsContext(bitmapImageRep: rep)!
    NSGraphicsContext.current = ctx
    NSColor.white.setFill()
    NSBezierPath(rect: NSRect(x: 0, y: 0, width: bounds.width, height: bounds.height)).fill()
    ctx.cgContext.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx.cgContext)
    NSGraphicsContext.restoreGraphicsState()
    if let data = rep.representation(using: .png, properties: [:]) {
        let out = URL(fileURLWithPath: outDir).appendingPathComponent(String(format: "page-%03d.png", pageNo))
        try data.write(to: out)
        print(out.path)
    }
    */
}
