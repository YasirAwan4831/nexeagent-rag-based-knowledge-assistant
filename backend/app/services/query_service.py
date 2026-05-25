"""Chat query processing with RAG and history management."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.config import get_settings
from app.services.gemini_service import get_gemini_service
from app.services.rag_service import get_rag_service
from app.utils.logger import logger


class QueryService:
    """Processes user queries through the RAG + Gemini pipeline."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self.gemini = get_gemini_service()
        self.rag = get_rag_service()

    def process_query(
        self,
        message: str,
        session_id: str | None = None,
        use_rag: bool = True,
    ) -> dict[str, Any]:
        session_id = session_id or str(uuid.uuid4())
        history = self._load_session(session_id)

        context = ""
        sources: list[dict] = []
        used_rag = False

        if use_rag:
            try:
                context, sources = self.rag.retrieve_context(message)
                used_rag = bool(context)
            except Exception as e:
                logger.warning("RAG retrieval failed, proceeding without context: %s", e)

        chat_history = [{"role": m["role"], "content": m["content"]} for m in history.get("messages", [])]

        answer = self.gemini.generate_response(
            user_message=message,
            context=context,
            chat_history=chat_history,
        )

        user_msg = self._make_message("user", message)
        assistant_msg = self._make_message("assistant", answer, sources=sources if sources else None)

        history.setdefault("messages", []).extend([user_msg, assistant_msg])
        history["session_id"] = session_id
        history["updated_at"] = datetime.now(timezone.utc).isoformat()
        if not history.get("created_at"):
            history["created_at"] = history["updated_at"]
        if not history.get("title"):
            history["title"] = message[:60] + ("..." if len(message) > 60 else "")

        self._save_session(session_id, history)

        return {
            "answer": answer,
            "session_id": session_id,
            "sources": self._format_sources(sources),
            "used_rag": used_rag,
        }

    def get_session(self, session_id: str) -> dict | None:
        return self._load_session(session_id)

    def list_sessions(self) -> list[dict]:
        sessions_dir = self.settings.chat_history_path
        sessions = []
        for path in sessions_dir.glob("*.json"):
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append({
                    "session_id": data.get("session_id", path.stem),
                    "title": data.get("title", "Untitled Chat"),
                    "message_count": len(data.get("messages", [])),
                    "updated_at": data.get("updated_at"),
                })
            except (json.JSONDecodeError, OSError):
                continue
        sessions.sort(key=lambda s: s.get("updated_at") or "", reverse=True)
        return sessions

    def delete_session(self, session_id: str) -> bool:
        path = self._session_path(session_id)
        if path.exists():
            path.unlink()
            return True
        return False

    def _session_path(self, session_id: str) -> Path:
        safe_id = "".join(c for c in session_id if c.isalnum() or c in "-_")
        return self.settings.chat_history_path / f"{safe_id}.json"

    def _load_session(self, session_id: str) -> dict:
        path = self._session_path(session_id)
        if not path.exists():
            return {"session_id": session_id, "messages": []}
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {"session_id": session_id, "messages": []}

    def _save_session(self, session_id: str, data: dict) -> None:
        path = self._session_path(session_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)

    @staticmethod
    def _make_message(role: str, content: str, sources: list | None = None) -> dict:
        msg = {
            "role": role,
            "content": content,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        if sources:
            msg["sources"] = sources
        return msg

    @staticmethod
    def _format_sources(sources: list[dict]) -> list[dict]:
        formatted = []
        for s in sources:
            meta = s.get("metadata", {})
            formatted.append({
                "filename": meta.get("filename", "unknown"),
                "chunk_index": meta.get("chunk_index", 0),
                "similarity": s.get("similarity", 0),
                "preview": (s.get("content", "")[:200] + "...") if s.get("content") else "",
            })
        return formatted


_query_service: QueryService | None = None


def get_query_service() -> QueryService:
    global _query_service
    if _query_service is None:
        _query_service = QueryService()
    return _query_service
