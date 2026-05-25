"""RAG orchestration - indexing and query pipeline."""

from pathlib import Path

from app.services.embedding_service import get_embedding_service
from app.services.pdf_service import get_document_service
from app.services.retrieval_service import get_retrieval_service
from app.services.vector_store_service import get_vector_store
from app.utils.chunking import chunk_text
from app.utils.file_utils import (
    add_document_metadata,
    generate_document_id,
    remove_document_metadata,
)
from app.utils.logger import logger


class RAGService:
    """End-to-end RAG pipeline for document indexing and retrieval."""

    def __init__(self) -> None:
        self.document_service = get_document_service()
        self.embedding_service = get_embedding_service()
        self.vector_store = get_vector_store()
        self.retrieval_service = get_retrieval_service()

    def index_document(self, file_path: Path, original_filename: str) -> dict:
        doc_id = generate_document_id()
        logger.info("Indexing document: %s (id=%s)", original_filename, doc_id)

        text = self.document_service.extract_text(file_path)
        chunks = chunk_text(text)

        if not chunks:
            raise ValueError("Document produced no indexable text chunks")

        embeddings = self.embedding_service.embed_batch(chunks)
        chunk_count = self.vector_store.add_chunks(
            doc_id=doc_id,
            chunks=chunks,
            embeddings=embeddings,
            filename=original_filename,
        )

        metadata = add_document_metadata({
            "id": doc_id,
            "filename": original_filename,
            "file_type": file_path.suffix.lower(),
            "file_size": file_path.stat().st_size,
            "stored_filename": file_path.name,
            "chunk_count": chunk_count,
            "status": "indexed",
        })

        logger.info("Successfully indexed %s with %d chunks", original_filename, chunk_count)
        return metadata

    def delete_document(self, doc_id: str) -> bool:
        removed_chunks = self.vector_store.delete_document(doc_id)
        removed_meta = remove_document_metadata(doc_id)
        return removed_meta or removed_chunks > 0

    def retrieve_context(self, query: str, document_id: str | None = None) -> tuple[str, list[dict]]:
        retrieved = self.retrieval_service.retrieve(query, document_id=document_id)
        context = self.retrieval_service.build_context(retrieved)
        return context, retrieved


_rag_service: RAGService | None = None


def get_rag_service() -> RAGService:
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service
