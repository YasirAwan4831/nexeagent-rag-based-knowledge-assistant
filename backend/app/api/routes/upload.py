"""Document upload endpoints."""

from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import get_settings
from app.models.schemas import DocumentInfo, UploadResponse
from app.services.rag_service import get_rag_service
from app.utils.file_utils import allowed_file, generate_document_id
from app.utils.logger import logger

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    if not allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Allowed: PDF, TXT, DOCX",
        )

    settings = get_settings()
    doc_id = generate_document_id()
    suffix = Path(file.filename).suffix.lower()
    stored_name = f"{doc_id}{suffix}"
    dest_path = settings.uploads_path / stored_name

    # Step 1: Save uploaded file to disk
    try:
        with open(dest_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        logger.info("File saved: %s -> %s", file.filename, stored_name)
    except (OSError, IOError) as e:
        logger.error("File save failed: %s", e)
        raise HTTPException(status_code=500, detail="Failed to save uploaded file") from e
    except Exception as e:
        logger.error("Unexpected error during file save: %s", e)
        raise HTTPException(status_code=500, detail="Unexpected error during file upload") from e

    # Step 2: Index document with RAG pipeline (text extraction + embeddings)
    try:
        rag = get_rag_service()
        logger.info("Starting indexing for document: %s", file.filename)
        metadata = rag.index_document(dest_path, file.filename)
        
        logger.info("Document indexed successfully: %s (chunks=%s)", 
                   file.filename, metadata.get("chunk_count", 0))
        
        doc_info = DocumentInfo(
            id=metadata["id"],
            filename=metadata["filename"],
            file_type=metadata["file_type"],
            file_size=metadata["file_size"],
            chunk_count=metadata.get("chunk_count", 0),
            status=metadata.get("status", "indexed"),
            uploaded_at=metadata.get("uploaded_at"),
        )
        return UploadResponse(
            success=True,
            message=f"Document '{file.filename}' indexed successfully",
            document=doc_info,
        )
    except ValueError as e:
        # Text extraction or processing error
        if dest_path.exists():
            dest_path.unlink()
        logger.error("Text processing failed for %s: %s", file.filename, e)
        raise HTTPException(status_code=422, detail=f"Invalid document format: {str(e)}") from e
    except RuntimeError as e:
        # Embedding or API error
        if dest_path.exists():
            dest_path.unlink()
        logger.error("Embedding/API error for %s: %s", file.filename, e)
        raise HTTPException(status_code=503, detail="AI service unavailable. Check API key and try again.") from e
    except Exception as e:
        if dest_path.exists():
            dest_path.unlink()
        logger.error("Indexing failed for %s: %s", file.filename, e, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to index document: {str(e)}") from e
