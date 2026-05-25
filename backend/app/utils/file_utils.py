"""File handling utilities."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.config import get_settings
from app.utils.logger import logger

ALLOWED_EXTENSIONS = {".pdf", ".txt", ".docx"}
METADATA_FILE = "documents.json"


def allowed_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def generate_document_id() -> str:
    return str(uuid.uuid4())


def metadata_file_path() -> Path:
    settings = get_settings()
    return settings.metadata_path / METADATA_FILE


def load_documents_metadata() -> list[dict[str, Any]]:
    path = metadata_file_path()
    if not path.exists():
        return []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError) as e:
        logger.error("Failed to load metadata: %s", e)
        return []


def save_documents_metadata(documents: list[dict[str, Any]]) -> None:
    path = metadata_file_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2, default=str)


def add_document_metadata(entry: dict[str, Any]) -> dict[str, Any]:
    documents = load_documents_metadata()
    entry.setdefault("uploaded_at", datetime.now(timezone.utc).isoformat())
    entry.setdefault("status", "indexed")
    documents.append(entry)
    save_documents_metadata(documents)
    return entry


def remove_document_metadata(doc_id: str) -> bool:
    documents = load_documents_metadata()
    updated = [d for d in documents if d.get("id") != doc_id]
    if len(updated) == len(documents):
        return False
    save_documents_metadata(updated)
    return True


def get_document_metadata(doc_id: str) -> dict[str, Any] | None:
    for doc in load_documents_metadata():
        if doc.get("id") == doc_id:
            return doc
    return None


def update_document_metadata(doc_id: str, updates: dict[str, Any]) -> dict[str, Any] | None:
    documents = load_documents_metadata()
    for i, doc in enumerate(documents):
        if doc.get("id") == doc_id:
            documents[i] = {**doc, **updates}
            save_documents_metadata(documents)
            return documents[i]
    return None
