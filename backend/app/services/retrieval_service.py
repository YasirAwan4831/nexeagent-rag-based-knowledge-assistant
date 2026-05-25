"""Context retrieval from vector store."""

from app.config import get_settings
from app.services.embedding_service import get_embedding_service
from app.services.vector_store_service import get_vector_store
from app.utils.logger import logger


class RetrievalService:
    """Semantic search and context assembly."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self.embedding_service = get_embedding_service()
        self.vector_store = get_vector_store()

    def retrieve(
        self,
        query: str,
        top_k: int | None = None,
        document_id: str | None = None,
    ) -> list[dict]:
        k = top_k or self.settings.top_k_results

        if self.vector_store.count() == 0:
            logger.warning("Vector store is empty - no documents indexed")
            return []

        query_embedding = self.embedding_service.embed_query(query)
        results = self.vector_store.query(
            query_embedding=query_embedding,
            top_k=k,
            document_id=document_id,
        )

        return self._format_results(results)

    def build_context(self, retrieved: list[dict], max_chars: int = 6000) -> str:
        if not retrieved:
            return ""

        parts = []
        total = 0
        for i, item in enumerate(retrieved, 1):
            chunk = item.get("content", "")
            source = item.get("metadata", {}).get("filename", "unknown")
            entry = f"[Source {i}: {source}]\n{chunk}"
            if total + len(entry) > max_chars:
                break
            parts.append(entry)
            total += len(entry)

        return "\n\n---\n\n".join(parts)

    def _format_results(self, results: dict) -> list[dict]:
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        formatted = []
        for doc, meta, dist in zip(documents, metadatas, distances):
            similarity = round(1 - dist, 4) if dist is not None else 0.0
            formatted.append({
                "content": doc,
                "metadata": meta or {},
                "similarity": similarity,
            })

        formatted.sort(key=lambda x: x["similarity"], reverse=True)
        return formatted


_retrieval_service: RetrievalService | None = None


def get_retrieval_service() -> RetrievalService:
    global _retrieval_service
    if _retrieval_service is None:
        _retrieval_service = RetrievalService()
    return _retrieval_service
