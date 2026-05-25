"""Application configuration loaded from environment variables."""

from pathlib import Path
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Central configuration for the RAG knowledge assistant."""

    model_config = SettingsConfigDict(
        env_file=str(BACKEND_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Gemini API
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.0-flash"
    gemini_embedding_model: str = "models/text-embedding-004"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    # RAG
    chunk_size: int = 800
    chunk_overlap: int = 150
    top_k_results: int = 5

    # Storage paths (relative to backend root)
    upload_dir: str = "data/uploads"
    chroma_dir: str = "data/chroma"
    metadata_dir: str = "data/metadata"
    chat_history_dir: str = "data/chat_history"
    log_dir: str = "logs"

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    def resolve_path(self, relative: str) -> Path:
        path = BACKEND_ROOT / relative
        path.mkdir(parents=True, exist_ok=True)
        return path

    @property
    def uploads_path(self) -> Path:
        return self.resolve_path(self.upload_dir)

    @property
    def chroma_path(self) -> Path:
        return self.resolve_path(self.chroma_dir)

    @property
    def metadata_path(self) -> Path:
        return self.resolve_path(self.metadata_dir)

    @property
    def chat_history_path(self) -> Path:
        return self.resolve_path(self.chat_history_dir)

    @property
    def logs_path(self) -> Path:
        return self.resolve_path(self.log_dir)


@lru_cache
def get_settings() -> Settings:
    return Settings()
