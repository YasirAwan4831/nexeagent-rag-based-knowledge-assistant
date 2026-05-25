"""Document text extraction for PDF, TXT, and DOCX files."""

from pathlib import Path

from pypdf import PdfReader
from docx import Document as DocxDocument

from app.utils.logger import logger


class DocumentProcessingService:
    """Extracts plain text from supported document formats."""

    def extract_text(self, file_path: Path) -> str:
        suffix = file_path.suffix.lower()
        extractors = {
            ".pdf": self._extract_pdf,
            ".txt": self._extract_txt,
            ".docx": self._extract_docx,
        }
        extractor = extractors.get(suffix)
        if not extractor:
            raise ValueError(f"Unsupported file type: {suffix}")

        text = extractor(file_path)
        if not text or not text.strip():
            raise ValueError(f"No text could be extracted from {file_path.name}")

        logger.info("Extracted %d characters from %s", len(text), file_path.name)
        return text.strip()

    def _extract_pdf(self, file_path: Path) -> str:
        reader = PdfReader(str(file_path))
        pages = []
        for page in reader.pages:
            content = page.extract_text()
            if content:
                pages.append(content)
        return "\n\n".join(pages)

    def _extract_txt(self, file_path: Path) -> str:
        for encoding in ("utf-8", "latin-1", "cp1252"):
            try:
                return file_path.read_text(encoding=encoding)
            except UnicodeDecodeError:
                continue
        raise ValueError(f"Could not decode text file: {file_path.name}")

    def _extract_docx(self, file_path: Path) -> str:
        doc = DocxDocument(str(file_path))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)


_document_service: DocumentProcessingService | None = None


def get_document_service() -> DocumentProcessingService:
    global _document_service
    if _document_service is None:
        _document_service = DocumentProcessingService()
    return _document_service
