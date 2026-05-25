"""Document management endpoints."""

from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.config import get_settings
from app.models.schemas import DocumentInfo, DocumentListResponse
from app.services.rag_service import get_rag_service
from app.utils.file_utils import get_document_metadata, load_documents_metadata
from app.utils.logger import logger

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("", response_model=DocumentListResponse)
async def list_documents():
    docs = load_documents_metadata()
    documents = [
        DocumentInfo(
            id=d["id"],
            filename=d["filename"],
            file_type=d.get("file_type", ""),
            file_size=d.get("file_size", 0),
            chunk_count=d.get("chunk_count", 0),
            status=d.get("status", "indexed"),
            uploaded_at=d.get("uploaded_at"),
        )
        for d in docs
    ]
    return DocumentListResponse(documents=documents, total=len(documents))


@router.get("/{doc_id}", response_model=DocumentInfo)
async def get_document(doc_id: str):
    doc = get_document_metadata(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return DocumentInfo(
        id=doc["id"],
        filename=doc["filename"],
        file_type=doc.get("file_type", ""),
        file_size=doc.get("file_size", 0),
        chunk_count=doc.get("chunk_count", 0),
        status=doc.get("status", "indexed"),
        uploaded_at=doc.get("uploaded_at"),
    )


@router.delete("/{doc_id}")
async def delete_document(doc_id: str):
    doc = get_document_metadata(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    settings = get_settings()
    stored = doc.get("stored_filename")
    if stored:
        file_path = settings.uploads_path / stored
        if file_path.exists():
            try:
                file_path.unlink()
            except OSError as e:
                logger.warning("Could not delete file %s: %s", stored, e)

    rag = get_rag_service()
    if not rag.delete_document(doc_id):
        raise HTTPException(status_code=500, detail="Failed to delete document")

    return {"success": True, "message": f"Document {doc['filename']} deleted"}
