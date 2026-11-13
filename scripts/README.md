# Scripts: Governance Utilities for Accessibility Case Management

This folder contains reusable Python scripts for converting, validating, and structuring accessibility case materials.

---

## Contents

### `pdf-to-markdown.py`
**PDF to Markdown Converter for Government Mandates**

Converts government PDFs (native and scanned) to searchable markdown format for LLM accessibility and repository optimization.

#### Features
- **Native PDF extraction** – Handles PDFs with embedded text (MOHUA Guidelines, NBC, RPWD Act)
- **Scanned document OCR** – Processes scanned GRs, circulars, and other government documents
- **Table extraction** – Detects and formats tables as markdown
- **Metadata header** – Includes source URL, extraction date, original document date
- **Batch processing** – Convert multiple PDFs via configuration file
- **Error handling** – Graceful fallback to OCR for problematic PDFs; detailed logging

#### Dependencies
See `requirements.txt` for complete list:
- `PyPDF2` – PDF parsing and structure extraction
- `pdfplumber` – Text and table extraction
- `easyocr` – OCR for scanned documents (optional but recommended)
- `Pillow` – Image processing
- `pdf2image` – PDF-to-image conversion for OCR

#### Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

**Note:** easyocr first-run downloads language models (~200 MB); subsequent runs are faster.

#### Usage

##### Single File Conversion
```bash
# Basic conversion
python pdf-to-markdown.py input.pdf output.md

# With metadata
python pdf-to-markdown.py mohua-guidelines.pdf mohua.md \
  --url "https://mohua.gov.in/upload/publishedDocument/MOHUA_Guidelines.pdf" \
  --date "2021-10-15" \
  --title "MOHUA Building Guidelines 2021"

# Without OCR (faster, native PDFs only)
python pdf-to-markdown.py input.pdf output.md --no-ocr
```

##### Batch Conversion
Create a configuration file `config.json`:
```json
{
  "conversions": [
    {
      "input": "mandates/national/MOHUA-guidelines.pdf",
      "output": "mandates/national/01-MOHUA-building-guidelines-2021.md",
      "url": "https://mohua.gov.in/upload/publishedDocument/...",
      "date": "2021-10-15",
      "title": "MOHUA Building Guidelines 2021"
    },
    {
      "input": "mandates/national/rpwd-act-2016.pdf",
      "output": "mandates/national/03-RPWD-Act-2016.md",
      "url": "https://www.indiacode.nic.in/",
      "date": "2016-12-28",
      "title": "Rights of Persons with Disabilities Act, 2016"
    }
  ]
}
```

Run batch conversion:
```bash
python pdf-to-markdown.py --batch config.json
```

#### Output Format

Markdown output includes:

1. **Metadata Header**
   ```markdown
   ---
   title: MOHUA Building Guidelines 2021
   source_url: https://mohua.gov.in/...
   original_date: 2021-10-15
   extracted_date: 2026-11-10 10:30:00
   extraction_tool: pdf-to-markdown.py
   ---
   ```

2. **Extracted Text** – Preserved with paragraph breaks

3. **Tables** – Formatted as markdown tables with source page/index reference

4. **Extraction Notes** – Summary of extraction method (native text vs. OCR) and table count

#### Example Workflow

Convert government mandate PDFs for repository:

```bash
# Create batch config
cat > mandate-conversion.json << 'EOF'
{
  "conversions": [
    {
      "input": "original-pdfs/RPWD-Act-2016.pdf",
      "output": "mandates/national/03-RPWD-Act-2016-Sections-40-44-47.md",
      "url": "https://legislative.gov.in/...",
      "date": "2016-04-27",
      "title": "RPWD Act 2016 - Rights of Persons with Disabilities"
    }
  ]
}
EOF

# Run conversion
python pdf-to-markdown.py --batch mandate-conversion.json

# Verify output
cat mandates/national/03-RPWD-Act-2016-Sections-40-44-47.md
```

#### Limitations

- **Scanned PDFs**: OCR quality depends on scan resolution and clarity (90%+ accuracy typical, lower for poor scans)
- **Complex layouts**: Multi-column, sidebar text, and overlapping elements may not format perfectly
- **Images**: Extracted as reference comments; manual review recommended
- **Forms**: Filled form fields may not extract clearly; visual review advised
- **Languages**: easyocr supports English; other languages require language pack installation

#### Troubleshooting

**Issue: "pdfplumber extraction failed; attempting OCR"**
- PDF has unusual structure or embedded fonts
- Fallback to OCR in progress; this is normal behavior

**Issue: "easyocr not available"**
- Install easyocr: `pip install easyocr`
- Or skip: `python pdf-to-markdown.py input.pdf output.md --no-ocr`

**Issue: OCR is very slow**
- First run downloads language models (~200 MB); this is normal
- Subsequent runs are much faster
- Consider using `--no-ocr` for native PDFs

**Issue: Tables not detected**
- pdfplumber may miss poorly formatted tables
- Manual review and markdown table formatting recommended
- Check extraction notes for table count

---

## Future Scripts

Planned governance utilities:

1. **Case validator** – Validate structured case data against template schema
2. **Mandate reference tool** – Query mandate text by section/topic
3. **Evidence inventory manager** – Catalog and organize case evidence files
4. **Batch case importer** – Import structured case data from spreadsheets

---

## Contributing

To contribute new scripts or improvements:

1. Follow Python best practices (PEP 8, type hints, docstrings)
2. Include CLI documentation with examples
3. Test against sample files (mandates/, cases/)
4. Update this README with usage instructions
5. Add dependencies to requirements.txt
6. Submit via GitHub issue or PR

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
