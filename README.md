# NEXEAGENT RAG Knowledge Assistant

A production-style **Retrieval-Augmented Generation (RAG)** application — **ChatGPT for Company Documents**.

Built as part of the **AI & Automation Internship** at [NEXE.AGENT](https://nexe.agent).

---

## Features

- **Document Upload** — PDF, TXT, DOCX support with drag & drop
- **RAG Pipeline** — Text extraction → chunking → Gemini embeddings → ChromaDB storage
- **AI Chat** — Context-aware answers powered by Google Gemini
- **Document Management** — View, index, and delete company documents
- **Chat History** — Persistent session-based conversations
- **Modern Dashboard** — React UI with dark mode, animations, and responsive layout

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React, Vite, Tailwind CSS, Framer Motion, Lucide React |
| Backend | Python, FastAPI, Uvicorn |
| AI | Google Gemini API (chat + embeddings) |
| Vector DB | ChromaDB |
| Storage | Local files + JSON metadata |

---

## Project Structure

```
nexeagent-rag-knowledge-assistant/
├── backend/
│   ├── app/
│   │   ├── api/routes/       # REST API endpoints
│   │   ├── services/         # RAG, Gemini, embeddings, vector store
│   │   ├── models/           # Pydantic schemas
│   │   └── utils/            # Chunking, logging, file utils
│   ├── data/                 # Uploads, ChromaDB, metadata, chat history
│   ├── tests/
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       └── context/
├── API.md
└── README.md
```

---

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- [Google Gemini API Key](https://aistudio.google.com/apikey)

### 1. Backend Setup

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux
```

Edit `backend/.env` and set your API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

Start the backend:

```bash
python run.py
```

API runs at **http://localhost:8000** — Docs at **http://localhost:8000/docs**

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at **http://localhost:5173**

### 3. Test the RAG Pipeline

1. Open **http://localhost:5173**
2. Go to **Upload** and upload `backend/sample_docs/company_policy.txt`
3. Go to **Chat** and ask: *"What is the refund policy?"*
4. The AI should answer using your uploaded document context

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | — |
| `GEMINI_MODEL` | Chat model | `gemini-2.0-flash` |
| `GEMINI_EMBEDDING_MODEL` | Embedding model | `models/text-embedding-004` |
| `CHUNK_SIZE` | Text chunk size | `800` |
| `CHUNK_OVERLAP` | Chunk overlap | `150` |
| `TOP_K_RESULTS` | Retrieval count | `5` |
| `PORT` | Server port | `8000` |

---

## Running Tests

```bash
cd backend
# Activate venv first
pip install -r requirements.txt
pytest tests/ -v
```

---

## RAG Workflow

```
Upload → Extract Text → Chunk → Embed (Gemini) → Store (ChromaDB)
                                                      ↓
User Query → Embed Query → Similarity Search → Context → Gemini → Answer
```

---

## API Documentation

See [API.md](./API.md) for full endpoint reference.

---

## License

MIT License — Developed by Muhammad Yasir for NEXE.AGENT Internship.

---

**فولڈر سٹرکچر — مکمل**

```
nexeagent-rag-knowledge-assistant/
├── API.md
├── README.md
├── .env
├── backend/
│   ├── .env
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── run.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── chat.py
│   │   │       ├── documents.py
│   │   │       ├── health.py
│   │   │       └── upload.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── embedding_service.py
│   │   │   ├── gemini_service.py
│   │   │   ├── pdf_service.py
│   │   │   ├── query_service.py
│   │   │   ├── rag_service.py
│   │   │   ├── retrieval_service.py
│   │   │   └── vector_store_service.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── chunking.py
│   │       ├── file_utils.py
│   │       └── logger.py
│   ├── data/
│   │   ├── chat_history/
│   │   ├── chroma/
│   │   │   └── chroma.sqlite3
│   │   ├── metadata/
│   │   └── uploads/
│   ├── logs/
│   ├── sample_docs/
│   │   └── company_policy.txt
│   └── tests/
│       ├── test_api.py
│       └── test_chunking.py
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   ├── public/
│   └── src/
│       ├── App.jsx
│       ├── index.css
│       ├── main.jsx
│       ├── components/
│       │   ├── ChatMessage.jsx
│       │   ├── FileUpload.jsx
│       │   ├── Layout.jsx
│       │   ├── LoadingSpinner.jsx
│       │   ├── Sidebar.jsx
│       │   ├── StatCard.jsx
│       │   └── TypingIndicator.jsx
│       ├── context/
│       │   └── ThemeContext.jsx
│       ├── pages/
│       │   ├── Chat.jsx
│       │   ├── Documents.jsx
│       │   ├── Home.jsx
│       │   ├── Settings.jsx
│       │   └── Upload.jsx
│       └── services/
│           └── api.js
└── (دیگر فائلیں/فولڈرز یہاں شامل نہیں کیے گئے: node_modules, dist, .pytest_cache, __pycache__ وغیرہ)
```
