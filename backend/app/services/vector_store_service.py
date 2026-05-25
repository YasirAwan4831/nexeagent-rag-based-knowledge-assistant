"""ChromaDB vector store for document embeddings."""

import chromadb
from chromadb.config import Settings as ChromaSettings

from app.config import get_settings
from app.utils.logger import logger

COLLECTION_NAME = "nexeagent_knowledge"


class VectorStoreService:
    """Persistent ChromaDB vector storage."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._client = chromadb.PersistentClient(
            path=str(self.settings.chroma_path),
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self._collection = self._client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
        logger.info("ChromaDB initialized at %s", self.settings.chroma_path)

    @property
    def collection(self):
        return self._collection

    def add_chunks(
        self,
        doc_id: str,
        chunks: list[str],
        embeddings: list[list[float]],
        filename: str,
    ) -> int:
        if len(chunks) != len(embeddings):
            raise ValueError("Chunks and embeddings count must match")

        ids = [f"{doc_id}_chunk_{i}" for i in range(len(chunks))]
        metadatas = [
            {
                "document_id": doc_id,
                "filename": filename,
                "chunk_index": i,
                "chunk_count": len(chunks),
            }
            for i in range(len(chunks))
        ]

        self._collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )
        logger.info("Added %d chunks for document %s", len(chunks), doc_id)
        return len(chunks)

    def delete_document(self, doc_id: str) -> int:
        try:
            results = self._collection.get(where={"document_id": doc_id})
            ids = results.get("ids", [])
            if ids:
                self._collection.delete(ids=ids)
            logger.info("Deleted %d chunks for document %s", len(ids), doc_id)
            return len(ids)
        except Exception as e:
            logger.error("Delete document from vector store failed: %s", e)
            return 0

    def query(
        self,
        query_embedding: list[float],
        top_k: int | None = None,
        document_id: str | None = None,
    ) -> dict:
        k = top_k or self.settings.top_k_results
        where = {"document_id": document_id} if document_id else None

        results = self._collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where=where,
            include=["documents", "metadatas", "distances"],
        )
        return results

    def count(self) -> int:
        return self._collection.count()

    def reset(self) -> None:
        self._client.delete_collection(COLLECTION_NAME)
        self._collection = self._client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
        logger.warning("Vector store collection reset")


_vector_store: VectorStoreService | None = None


def get_vector_store() -> VectorStoreService:
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStoreService()
    return _vector_store
