"""Tests for text chunking utility."""

from app.utils.chunking import chunk_text


def test_chunk_text_empty():
    assert chunk_text("") == []
    assert chunk_text("   ") == []


def test_chunk_text_paragraphs():
    text = "Paragraph one.\n\nParagraph two with more content.\n\nParagraph three."
    chunks = chunk_text(text, chunk_size=50, overlap=10)
    assert len(chunks) >= 1
    assert all(isinstance(c, str) for c in chunks)


def test_chunk_long_paragraph():
    long_para = "word " * 500
    chunks = chunk_text(long_para, chunk_size=100, overlap=20)
    assert len(chunks) > 1
