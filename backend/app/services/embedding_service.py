"""Embedding generation using Google Gemini embedding API."""

from google import genai

from app.config import get_settings
from app.utils.logger import logger


class EmbeddingService:
    """Generates vector embeddings via Gemini using google-genai SDK."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._configured = False
        self._client = None
        self._configure()

    def _configure(self) -> None:
        if not self.settings.gemini_api_key or self.settings.gemini_api_key == "YOUR_API_KEY_HERE":
            logger.warning("GEMINI_API_KEY not configured for embeddings")
            return
        try:
            # Initialize google-genai client
            self._client = genai.Client(api_key=self.settings.gemini_api_key)
            self._configured = True
            logger.info("Embedding service initialized: %s", self.settings.gemini_embedding_model)
        except Exception as e:
            logger.error("Failed to configure embedding service: %s", e)

    @property
    def is_configured(self) -> bool:
        return self._configured

    def embed_text(self, text: str, task_type: str = "retrieval_document") -> list[float]:
        """Generate embedding for a single text using google-genai SDK.
        
        Args:
            text: Text to embed
            task_type: Task type ("retrieval_document" or "retrieval_query")
            
        Returns:
            Embedding vector as list of floats
        """
        if not self._configured or not self._client:
            raise RuntimeError("Embedding service not configured. Set GEMINI_API_KEY.")
        
        if not text or not text.strip():
            raise ValueError("Cannot embed empty text")
        
        try:
            text_to_embed = str(text).strip()
            logger.debug("Embedding text of length: %d", len(text_to_embed))
            
            # Call google-genai client.models.embed_content()
            response = self._client.models.embed_content(
                model=self.settings.gemini_embedding_model,
                contents=text_to_embed,
            )
            
            # Parse response from google-genai SDK
            if not response:
                raise RuntimeError("No response from embedding API")
            
            # Handle response structure from google-genai
            if hasattr(response, 'embedding'):
                embedding = response.embedding
            elif isinstance(response, dict) and 'embedding' in response:
                embedding = response['embedding']
            else:
                logger.error("Unexpected response structure: %s", type(response))
                raise RuntimeError("Invalid response format from embedding API")
            
            if not embedding or len(embedding) == 0:
                raise RuntimeError("Invalid embedding: empty vector")
            
            # Ensure embedding is list of floats
            embedding_list = list(embedding) if not isinstance(embedding, list) else embedding
            
            logger.debug("Generated embedding with %d dimensions", len(embedding_list))
            return embedding_list
            
        except ValueError as e:
            logger.error("Text validation error: %s", e)
            raise
        except Exception as e:
            logger.error("Embedding API error for text of length %d: %s", len(text), e, exc_info=True)
            raise RuntimeError(f"Failed to generate embedding: {e}") from e

    def embed_batch(self, texts: list[str], task_type: str = "retrieval_document") -> list[list[float]]:
        """Generate embeddings for multiple texts.
        
        Args:
            texts: List of texts to embed
            task_type: Task type ("retrieval_document" or "retrieval_query")
            
        Returns:
            List of embedding vectors
        """
        embeddings = []
        for i, text in enumerate(texts):
            if i > 0 and i % 10 == 0:
                logger.debug("Embedded %d/%d chunks", i, len(texts))
            embeddings.append(self.embed_text(text, task_type=task_type))
        return embeddings

    def embed_query(self, query: str) -> list[float]:
        """Generate embedding for a query text.
        
        Args:
            query: Query text to embed
            
        Returns:
            Embedding vector as list of floats
        """
        return self.embed_text(query, task_type="retrieval_query")


_embedding_service: EmbeddingService | None = None


def get_embedding_service() -> EmbeddingService:
    global _embedding_service
    if _embedding_service is None:
        _embedding_service = EmbeddingService()
    return _embedding_service
