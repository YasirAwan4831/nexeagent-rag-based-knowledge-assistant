"""Intelligent text chunking for RAG indexing."""

from app.config import get_settings


def chunk_text(text: str, chunk_size: int | None = None, overlap: int | None = None) -> list[str]:
    """
    Split text into overlapping chunks using paragraph-aware splitting.
    Falls back to character-based splitting for long paragraphs.
    """
    settings = get_settings()
    size = chunk_size or settings.chunk_size
    ov = overlap or settings.chunk_overlap

    text = text.strip()
    if not text:
        return []

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""

    for para in paragraphs:
        if len(para) > size:
            if current:
                chunks.append(current.strip())
                current = ""
            chunks.extend(_split_long_text(para, size, ov))
            continue

        candidate = f"{current}\n\n{para}".strip() if current else para
        if len(candidate) <= size:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())
            current = para

    if current:
        chunks.append(current.strip())

    return _apply_overlap(chunks, ov) if chunks else []


def _split_long_text(text: str, size: int, overlap: int) -> list[str]:
    """Character-based sliding window for oversized paragraphs."""
    result = []
    start = 0
    while start < len(text):
        end = start + size
        result.append(text[start:end].strip())
        start = end - overlap if end < len(text) else len(text)
    return [c for c in result if c]


def _apply_overlap(chunks: list[str], overlap: int) -> list[str]:
    """Merge tiny trailing chunks and ensure minimum content."""
    if len(chunks) <= 1 or overlap <= 0:
        return chunks

    merged: list[str] = []
    for i, chunk in enumerate(chunks):
        if i > 0 and len(chunk) < overlap // 2 and merged:
            merged[-1] = f"{merged[-1]}\n\n{chunk}"
        else:
            merged.append(chunk)
    return merged
