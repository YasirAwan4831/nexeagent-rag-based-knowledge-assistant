"""Chat and query endpoints."""

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    ChatHistoryResponse,
    ChatMessage,
    ChatRequest,
    ChatResponse,
    ChatSessionSummary,
    ChatSessionsResponse,
)
from app.services.query_service import get_query_service
from app.utils.logger import logger

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        query_service = get_query_service()
        result = query_service.process_query(
            message=request.message,
            session_id=request.session_id,
            use_rag=request.use_rag,
        )
        return ChatResponse(
            answer=result["answer"],
            session_id=result["session_id"],
            sources=result["sources"],
            used_rag=result["used_rag"],
        )
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e)) from e
    except Exception as e:
        logger.error("Chat error: %s", e)
        raise HTTPException(status_code=500, detail="Failed to process chat message") from e


@router.get("/sessions", response_model=ChatSessionsResponse)
async def list_chat_sessions():
    query_service = get_query_service()
    sessions = query_service.list_sessions()
    return ChatSessionsResponse(
        sessions=[
            ChatSessionSummary(
                session_id=s["session_id"],
                title=s["title"],
                message_count=s["message_count"],
                updated_at=s.get("updated_at"),
            )
            for s in sessions
        ]
    )


@router.get("/sessions/{session_id}", response_model=ChatHistoryResponse)
async def get_chat_history(session_id: str):
    query_service = get_query_service()
    session = query_service.get_session(session_id)
    if not session or not session.get("messages"):
        raise HTTPException(status_code=404, detail="Chat session not found")

    return ChatHistoryResponse(
        session_id=session.get("session_id", session_id),
        messages=[
            ChatMessage(
                role=m["role"],
                content=m["content"],
                timestamp=m.get("timestamp"),
                sources=m.get("sources"),
            )
            for m in session.get("messages", [])
        ],
        created_at=session.get("created_at"),
        updated_at=session.get("updated_at"),
    )


@router.delete("/sessions/{session_id}")
async def delete_chat_session(session_id: str):
    query_service = get_query_service()
    if not query_service.delete_session(session_id):
        raise HTTPException(status_code=404, detail="Chat session not found")
    return {"success": True, "message": "Chat session deleted"}
