"""Health check endpoints."""

from fastapi import APIRouter

from app import __version__
from app.models.schemas import HealthResponse, SettingsResponse
from app.services.gemini_service import get_gemini_service
from app.services.vector_store_service import get_vector_store
from app.utils.file_utils import load_documents_metadata
from app.config import get_settings

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    settings = get_settings()
    vector_store = get_vector_store()
    gemini = get_gemini_service()
    docs = load_documents_metadata()

    return HealthResponse(
        status="healthy",
        version=__version__,
        gemini_configured=gemini.is_configured,
        documents_count=len(docs),
        vector_chunks=vector_store.count(),
    )


@router.get("/settings", response_model=SettingsResponse)
async def get_app_settings():
    settings = get_settings()
    gemini = get_gemini_service()
    return SettingsResponse(
        gemini_model=settings.gemini_model,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        top_k_results=settings.top_k_results,
        gemini_configured=gemini.is_configured,
    )
