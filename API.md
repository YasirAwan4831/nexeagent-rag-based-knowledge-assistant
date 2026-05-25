# NEXEAGENT API Documentation

Base URL: `http://localhost:8000/api`

Interactive docs: `http://localhost:8000/docs`

---

## Health

### `GET /health`

Returns system health and statistics.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "gemini_configured": true,
  "documents_count": 3,
  "vector_chunks": 42
}
```

### `GET /settings`

Returns application configuration (non-sensitive).

---

## Documents

### `GET /documents`

List all indexed documents.

**Response:**
```json
{
  "documents": [
    {
      "id": "uuid",
      "filename": "policy.pdf",
      "file_type": ".pdf",
      "file_size": 102400,
      "chunk_count": 15,
      "status": "indexed",
      "uploaded_at": "2026-05-23T10:00:00+00:00"
    }
  ],
  "total": 1
}
```

### `GET /documents/{doc_id}`

Get a single document by ID.

### `DELETE /documents/{doc_id}`

Delete document from storage, metadata, and vector database.

---

## Upload

### `POST /upload`

Upload and index a document.

**Content-Type:** `multipart/form-data`

**Body:** `file` (PDF, TXT, or DOCX)

**Response:**
```json
{
  "success": true,
  "message": "Document 'policy.pdf' indexed successfully",
  "document": { ... }
}
```

---

## Chat

### `POST /chat`

Send a message and receive an AI response with optional RAG context.

**Body:**
```json
{
  "message": "What is the company refund policy?",
  "session_id": "optional-uuid",
  "use_rag": true
}
```

**Response:**
```json
{
  "answer": "Based on the company documents...",
  "session_id": "uuid",
  "sources": [
    {
      "filename": "policy.pdf",
      "chunk_index": 3,
      "similarity": 0.87,
      "preview": "Refund policy states..."
    }
  ],
  "used_rag": true
}
```

### `GET /chat/sessions`

List all chat sessions.

### `GET /chat/sessions/{session_id}`

Get full chat history for a session.

### `DELETE /chat/sessions/{session_id}`

Delete a chat session.

---

## Error Responses

```json
{
  "detail": "Error message",
  "error_code": "INTERNAL_ERROR"
}
```

| Status | Meaning |
|--------|---------|
| 400 | Bad request (invalid file type, etc.) |
| 404 | Resource not found |
| 500 | Server error |
| 503 | Gemini API not configured |
