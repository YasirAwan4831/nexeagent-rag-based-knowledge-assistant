"""API request/response schemas."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    version: str
    gemini_configured: bool
    documents_count: int
    vector_chunks: int


class DocumentInfo(BaseModel):
    id: str
    filename: str
    file_type: str
    file_size: int
    chunk_count: int = 0
    status: str = "indexed"
    uploaded_at: str | None = None


class DocumentListResponse(BaseModel):
    documents: list[DocumentInfo]
    total: int


class UploadResponse(BaseModel):
    success: bool
    message: str
    document: DocumentInfo | None = None


class ChatMessage(BaseModel):
    role: str
    content: str
    timestamp: str | None = None
    sources: list[dict[str, Any]] | None = None


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    session_id: str | None = None
    use_rag: bool = True


class ChatResponse(BaseModel):
    answer: str
    session_id: str
    sources: list[dict[str, Any]] = []
    used_rag: bool = True


class ChatHistoryResponse(BaseModel):
    session_id: str
    messages: list[ChatMessage]
    created_at: str | None = None
    updated_at: str | None = None


class ChatSessionSummary(BaseModel):
    session_id: str
    title: str
    message_count: int
    updated_at: str | None = None


class ChatSessionsResponse(BaseModel):
    sessions: list[ChatSessionSummary]


class ErrorResponse(BaseModel):
    detail: str
    error_code: str | None = None


class SettingsResponse(BaseModel):
    gemini_model: str
    chunk_size: int
    chunk_overlap: int
    top_k_results: int
    gemini_configured: bool
