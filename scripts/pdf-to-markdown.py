#!/usr/bin/env python3
"""
PDF to Markdown Converter

Converts government PDFs (native and scanned) to searchable markdown format.
Supports:
- Native PDFs (MOHUA Guidelines, NBC, RPWD Act, RERA documents)
- Scanned documents (GRs, circulars) with OCR

Output includes:
- Metadata header (source URL, extraction date, original date)
- Searchable markdown with preserved hierarchy
- Table extraction and formatting
- Image references with extraction status

Usage:
    python pdf-to-markdown.py <input_pdf> <output_markdown> [--url <source_url>] [--date <original_date>]
    python pdf-to-markdown.py --batch <config_file>
"""

import argparse
import sys
import os
from pathlib import Path
from datetime import datetime
import json
import logging
from typing import Optional, List, Dict, Tuple

try:
    import PyPDF2
    from pdfplumber import PDF
    import pdfplumber
except ImportError:
    print("Error: Required packages not installed.")
    print("Install with: pip install -r requirements.txt")
    sys.exit(1)

# Optional OCR support
try:
    import easyocr
    HAS_OCR = True
except ImportError:
    HAS_OCR = False

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PDFToMarkdownConverter:
    """Convert PDF to structured markdown format."""
    
    def __init__(self, enable_ocr: bool = True):
        """
        Initialize converter.
        
        Args:
            enable_ocr: Enable OCR for scanned documents (requires easyocr)
        """
        self.enable_ocr = enable_ocr and HAS_OCR
        if enable_ocr and not HAS_OCR:
            logger.warning("easyocr not available; scanned PDFs will have reduced accuracy")
        self.ocr_reader = None
    
    def _get_ocr_reader(self):
        """Lazily initialize OCR reader."""
        if not self.ocr_reader and self.enable_ocr:
            logger.info("Initializing OCR reader (first run may take time)...")
            try:
                self.ocr_reader = easyocr.Reader(['en'], gpu=False)
                logger.info("OCR reader initialized")
            except Exception as e:
                logger.error(f"Failed to initialize OCR: {e}")
                self.enable_ocr = False
        return self.ocr_reader
    
    def extract_text_and_tables(self, pdf_path: str) -> Tuple[str, List[Dict]]:
        """
        Extract text and tables from PDF using pdfplumber.
        Falls back to OCR for scanned PDFs if needed.
        
        Args:
            pdf_path: Path to input PDF
            
        Returns:
            Tuple of (extracted_text, tables_list)
        """
        markdown_content = []
        tables = []
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                num_pages = len(pdf.pages)
                logger.info(f"Processing PDF with {num_pages} pages")
                
                for page_num, page in enumerate(pdf.pages, 1):
                    # Extract text
                    text = page.extract_text()
                    if text and text.strip():
                        markdown_content.append(text)
                    
                    # Extract tables
                    page_tables = page.extract_tables()
                    if page_tables:
                        for table_idx, table in enumerate(page_tables):
                            tables.append({
                                'page': page_num,
                                'index': table_idx,
                                'data': table
                            })
                    
                    if page_num % 10 == 0:
                        logger.info(f"  Processed {page_num}/{num_pages} pages")
        
        except Exception as e:
            logger.warning(f"pdfplumber extraction failed: {e}")
            if self.enable_ocr:
                logger.info("Attempting OCR extraction...")
                return self._ocr_extract(pdf_path)
            else:
                raise
        
        return "\n\n".join(markdown_content), tables
    
    def _ocr_extract(self, pdf_path: str) -> Tuple[str, List[Dict]]:
        """
        Extract text from scanned PDF using OCR.
        
        Args:
            pdf_path: Path to input PDF
            
        Returns:
            Tuple of (extracted_text, empty_tables_list)
        """
        from pdf2image import convert_from_path
        
        markdown_content = []
        reader = self._get_ocr_reader()
        
        if not reader:
            raise RuntimeError("OCR reader not available")
        
        try:
            images = convert_from_path(pdf_path)
            logger.info(f"Converted PDF to {len(images)} images for OCR")
            
            for page_num, image in enumerate(images, 1):
                result = reader.readtext(image)
                text_lines = [item[1] for item in result]
                page_text = "\n".join(text_lines)
                if page_text.strip():
                    markdown_content.append(f"### Page {page_num}\n\n{page_text}")
                
                if page_num % 5 == 0:
                    logger.info(f"  OCR processed {page_num}/{len(images)} pages")
        
        except ImportError:
            raise RuntimeError(
                "pdf2image required for OCR. Install with: pip install pdf2image"
            )
        
        return "\n\n".join(markdown_content), []
    
    def format_tables_as_markdown(self, tables: List[Dict]) -> str:
        """
        Format extracted tables as markdown.
        
        Args:
            tables: List of table data
            
        Returns:
            Formatted markdown string
        """
        if not tables:
            return ""
        
        markdown = "\n## Extracted Tables\n\n"
        
        for table_info in tables:
            markdown += f"### Table (Page {table_info['page']}, Index {table_info['index']})\n\n"
            table = table_info['data']
            
            if table and len(table) > 0:
                # Create header
                headers = table[0]
                markdown += "| " + " | ".join(str(h) for h in headers) + " |\n"
                markdown += "|" + "|".join(["---" for _ in headers]) + "|\n"
                
                # Add rows
                for row in table[1:]:
                    markdown += "| " + " | ".join(str(cell) for cell in row) + " |\n"
            
            markdown += "\n"
        
        return markdown
    
    def create_metadata_header(
        self,
        source_url: Optional[str] = None,
        original_date: Optional[str] = None,
        title: Optional[str] = None
    ) -> str:
        """
        Create markdown metadata header.
        
        Args:
            source_url: URL of original PDF
            original_date: Original publication/issue date
            title: Document title
            
        Returns:
            Formatted metadata header
        """
        extraction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        header = "---\n"
        if title:
            header += f"title: {title}\n"
        if source_url:
            header += f"source_url: {source_url}\n"
        if original_date:
            header += f"original_date: {original_date}\n"
        header += f"extracted_date: {extraction_date}\n"
        header += f"extraction_tool: pdf-to-markdown.py\n"
        header += "---\n\n"
        
        return header
    
    def convert(
        self,
        input_pdf: str,
        output_markdown: str,
        source_url: Optional[str] = None,
        original_date: Optional[str] = None,
        title: Optional[str] = None
    ) -> bool:
        """
        Convert PDF to markdown.
        
        Args:
            input_pdf: Path to input PDF
            output_markdown: Path to output markdown file
            source_url: URL of original PDF
            original_date: Original publication date
            title: Document title
            
        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info(f"Converting {input_pdf}...")
            
            # Extract text and tables
            text, tables = self.extract_text_and_tables(input_pdf)
            
            # Build markdown
            markdown = self.create_metadata_header(source_url, original_date, title)
            markdown += text
            
            if tables:
                markdown += self.format_tables_as_markdown(tables)
            
            # Add extraction notes
            markdown += "\n## Extraction Notes\n\n"
            markdown += f"- Tables extracted: {len(tables)}\n"
            if self.enable_ocr:
                markdown += "- OCR used for text extraction\n"
            markdown += f"- Source: {source_url or 'Not provided'}\n"
            
            # Write output
            output_path = Path(output_markdown)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            logger.info(f"Successfully converted to {output_markdown}")
            return True
        
        except Exception as e:
            logger.error(f"Conversion failed: {e}")
            return False


def main():
    """CLI interface."""
    parser = argparse.ArgumentParser(
        description="Convert government PDFs to searchable markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert single PDF
  python pdf-to-markdown.py input.pdf output.md --url https://source.gov/doc.pdf
  
  # Convert with metadata
  python pdf-to-markdown.py nbcpdf.pdf nbc.md \\
    --url https://example.gov/nbc-2016.pdf \\
    --date "2016-01-01" \\
    --title "NBC 2016 Section 13"
  
  # Batch convert from config
  python pdf-to-markdown.py --batch config.json
        """
    )
    
    parser.add_argument('input_pdf', nargs='?', help='Input PDF file path')
    parser.add_argument('output_markdown', nargs='?', help='Output markdown file path')
    parser.add_argument('--url', help='Source URL of the PDF')
    parser.add_argument('--date', help='Original publication/issue date')
    parser.add_argument('--title', help='Document title')
    parser.add_argument('--batch', help='Batch config JSON file (alternative to single file mode)')
    parser.add_argument('--no-ocr', action='store_true', help='Disable OCR for scanned PDFs')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.batch:
        return run_batch_conversion(args.batch, not args.no_ocr)
    elif args.input_pdf and args.output_markdown:
        converter = PDFToMarkdownConverter(enable_ocr=not args.no_ocr)
        success = converter.convert(
            args.input_pdf,
            args.output_markdown,
            source_url=args.url,
            original_date=args.date,
            title=args.title
        )
        return 0 if success else 1
    else:
        parser.print_help()
        return 1


def run_batch_conversion(config_path: str, enable_ocr: bool = True) -> int:
    """
    Run batch conversion from config file.
    
    Config file format:
    {
        "conversions": [
            {
                "input": "input.pdf",
                "output": "output.md",
                "url": "https://source.gov/doc.pdf",
                "date": "2016-01-01",
                "title": "Document Title"
            },
            ...
        ]
    }
    
    Args:
        config_path: Path to config JSON file
        enable_ocr: Enable OCR support
        
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        converter = PDFToMarkdownConverter(enable_ocr=enable_ocr)
        conversions = config.get('conversions', [])
        
        logger.info(f"Running batch conversion with {len(conversions)} files...")
        
        successful = 0
        failed = 0
        
        for idx, conversion in enumerate(conversions, 1):
            logger.info(f"\n[{idx}/{len(conversions)}]")
            success = converter.convert(
                conversion['input'],
                conversion['output'],
                source_url=conversion.get('url'),
                original_date=conversion.get('date'),
                title=conversion.get('title')
            )
            if success:
                successful += 1
            else:
                failed += 1
        
        logger.info(f"\nBatch conversion complete: {successful} succeeded, {failed} failed")
        return 0 if failed == 0 else 1
    
    except Exception as e:
        logger.error(f"Batch conversion failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
