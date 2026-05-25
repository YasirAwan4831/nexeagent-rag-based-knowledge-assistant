"""Google Gemini API integration for chat completions."""

from google import genai

from app.config import get_settings
from app.utils.logger import logger

SYSTEM_PROMPT = """You are NEXEAGENT, an intelligent company knowledge assistant.
Your role is to answer questions accurately based on the provided company document context.

Rules:
1. Prioritize information from the provided context over general knowledge.
2. If the context contains the answer, cite specific details from it.
3. If the context does not contain enough information, clearly state what is missing.
4. Never invent company-specific facts, policies, or numbers not in the context.
5. Be professional, concise, and helpful.
6. Format responses with clear structure when appropriate."""


class GeminiService:
    """Handles Gemini chat generation using google-genai SDK."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._configured = False
        self._client = None
        self._configure()

    def _configure(self) -> None:
        if not self.settings.gemini_api_key or self.settings.gemini_api_key == "YOUR_API_KEY_HERE":
            logger.warning("GEMINI_API_KEY not configured. Set it in backend/.env")
            return
        try:
            # Initialize google-genai client
            self._client = genai.Client(api_key=self.settings.gemini_api_key)
            self._configured = True
            logger.info("Gemini service initialized with model: %s", self.settings.gemini_model)
        except Exception as e:
            logger.error("Failed to configure Gemini: %s", e)

    @property
    def is_configured(self) -> bool:
        return self._configured

    def generate_response(
        self,
        user_message: str,
        context: str = "",
        chat_history: list[dict[str, str]] | None = None,
    ) -> str:
        """Generate a response using Gemini with RAG context.
        
        Args:
            user_message: User's question
            context: Retrieved document context (optional)
            chat_history: Previous messages in conversation (optional)
            
        Returns:
            Generated response text
        """
        if not self._configured or not self._client:
            raise RuntimeError(
                "Gemini API is not configured. Set GEMINI_API_KEY in backend/.env"
            )

        prompt_parts = []

        if context:
            prompt_parts.append(
                f"--- COMPANY DOCUMENT CONTEXT ---\n{context}\n--- END CONTEXT ---\n"
            )

        if chat_history:
            for msg in chat_history[-6:]:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                prompt_parts.append(f"{role.upper()}: {content}")

        prompt_parts.append(f"USER QUESTION: {user_message}")
        prompt_parts.append(
            "Provide a helpful answer based on the company document context above. "
            "If context is insufficient, say so clearly."
        )

        full_prompt = "\n\n".join(prompt_parts)

        try:
            logger.debug("Generating response with model: %s", self.settings.gemini_model)
            
            # Use google-genai client.models.generate_content()
            response = self._client.models.generate_content(
                model=self.settings.gemini_model,
                contents=full_prompt,
            )
            
            if not response:
                logger.warning("Empty response from Gemini API")
                return "I could not generate a response."
            
            # Parse response from google-genai
            if hasattr(response, 'text'):
                result_text = response.text
            elif hasattr(response, 'candidates') and response.candidates:
                # Handle candidates structure
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    result_text = "".join(part.text for part in candidate.content.parts if hasattr(part, 'text'))
                else:
                    result_text = ""
            else:
                logger.warning("Unexpected response structure: %s", type(response))
                result_text = ""
            
            return result_text.strip() if result_text else "I could not generate a response."
            
        except Exception as e:
            logger.error("Gemini generation error: %s", e, exc_info=True)
            raise RuntimeError(f"AI generation failed: {e}") from e


_gemini_service: GeminiService | None = None


def get_gemini_service() -> GeminiService:
    """Get or create singleton GeminiService instance."""
    global _gemini_service
    if _gemini_service is None:
        _gemini_service = GeminiService()
    return _gemini_service
