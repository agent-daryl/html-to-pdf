# HTML to PDF Converter

Convert HTML files (or URLs) to PDF with configurable page size and margins. A thin wrapper around [weasyprint](https://weasyprint.org/) — no browser, no Node.js, no headless Chrome. Pure Python.

## Quick Start

```bash
# Convert an HTML file to PDF
python3 html_to_pdf.py report.html

# Custom output name and page size
python3 html_to_pdf.py report.html -o report.pdf -f a4 -m 15
```

## Usage

```
python3 html_to_pdf.py <input> [options]

positional arguments:
  input                 HTML file path or URL to convert

options:
  -o, --output PATH     Output PDF path (default: input name + .pdf)
  -f, --format FORMAT   Page format: letter, a4, legal, a3, a5 (default: letter)
  -m, --margins MM      Page margins in mm (default: 10)
```

## Examples

```bash
# Basic — converts input.html to input.pdf (US Letter, 10mm margins)
python3 html_to_pdf.py input.html

# A4 paper, 15mm margins
python3 html_to_pdf.py input.html -f a4 -m 15

# Custom output name
python3 html_to_pdf.py input.html -o final_report.pdf

# From a URL
python3 html_to_pdf.py https://example.com -o webpage.pdf

# Legal size, wide margins
python3 html_to_pdf.py input.html -f legal -m 20
```

## Supported Page Formats

| Format | Size |
|---|---|
| `letter` (default) | 8.5 x 11 in |
| `a4` | 210 x 297 mm |
| `legal` | 8.5 x 14 in |
| `a3` | 297 x 420 mm |
| `a5` | 148 x 210 mm |

## Requirements

- Python 3.6+
- weasyprint (`pip3 install weasyprint`)

That's it. No other dependencies.

## How It Works

The script generates an inline `@page` CSS rule with your chosen size and margins, then passes it to weasyprint along with the HTML source. Weasyprint renders the full HTML/CSS to PDF, including:

- Inline and external CSS
- Background colors and gradients
- Embedded fonts (if available on the system)
- Tables, lists, and all standard HTML elements
- `@media print` styles

## License

MIT
