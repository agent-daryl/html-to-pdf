#!/usr/bin/env python3
"""
html_to_pdf — Convert HTML files to PDF using weasyprint.

Takes an HTML file (or URL) and produces a PDF with configurable page
size, margins, and output options. Zero dependencies beyond weasyprint.

_usage:_
    python html_to_pdf.py <input.html> [output.pdf]
    python html_to_pdf.py <input.html> --output output.pdf --format a4 --margins 20

_examples:_
    # Basic conversion
    python html_to_pdf.py report.html

    # Custom output name and page size
    python html_to_pdf.py report.html --output report.pdf --format a4

    # Custom margins (in mm)
    python html_to_pdf.py report.html --margins 15

    # From a URL
    python html_to_pdf.py https://example.com --output page.pdf

_config:_
    Default output: same name as input with .pdf extension
    Default format: letter (8.5 x 11 in)
    Default margins: 10mm all sides
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from weasyprint import HTML
except ImportError:
    print("Error: weasyprint is not installed.")
    print("Install it with: pip3 install weasyprint")
    sys.exit(1)


FORMATS = {
    "letter": (8.5, 11),
    "a4": (210, 297),
    "legal": (8.5, 14),
    "a3": (297, 420),
    "a5": (148, 210),
}


def convert(html_path, output_path, fmt, margins):
    """Convert HTML to PDF with the given options."""
    fmt_key = fmt.lower()
    if fmt_key in FORMATS:
        width, height = FORMATS[fmt_key]
        if fmt_key == "letter" or fmt_key == "legal":
            size = (f"{width}in", f"{height}in")
        else:
            size = (f"{width}mm", f"{height}mm")
    else:
        size = None

    css = f"""@page {{
        size: {size or 'auto'};
        margin: {margins}mm;
    }}"""

    from weasyprint import CSS
    html = HTML(filename=html_path)
    html.write_pdf(output_path, stylesheets=[CSS(string=css)])
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert HTML files to PDF using weasyprint",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", help="HTML file path or URL to convert")
    parser.add_argument(
        "--output", "-o",
        help="Output PDF path (default: same name as input with .pdf extension)"
    )
    parser.add_argument(
        "--format", "-f",
        default="letter",
        choices=list(FORMATS.keys()),
        help="Page format (default: letter)"
    )
    parser.add_argument(
        "--margins", "-m",
        type=float,
        default=10,
        help="Page margins in mm (default: 10)"
    )

    args = parser.parse_args()

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        stem = Path(args.input).stem
        output_path = f"{stem}.pdf"

    print(f"Converting: {args.input}")
    print(f"Output:     {output_path}")
    print(f"Format:     {args.format}")
    print(f"Margins:    {args.margins}mm")
    print()

    try:
        convert(args.input, output_path, args.format, args.margins)
        size = os.path.getsize(output_path)
        if size < 1024:
            size_str = f"{size} B"
        elif size < 1024 * 1024:
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size / (1024 * 1024):.1f} MB"
        print(f"Done: {output_path} ({size_str})")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
