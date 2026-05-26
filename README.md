<div align="center">

<!-- ANIMATED SVG BANNER -->
<img 
  src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=NEXE-AGENT%20RAG%20Knowledge%20Assistant&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Muhammad%20Yasir%20-%20AI%20AUTOMATION%20INTERN%20-%20NEXE%20AGENT&descAlignY=65&descSize=22&descColor=d1d5db" 
  width="100%"
/>

<!-- TYPING ANIMATION -->
<a href="https://git.io/typing-svg">
  <img 
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6366F1&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=80&lines=AI+for+Your+Company+Documents;Upload+-+Embed+-+Retrieve+-+Answer;Powered+by+Google+Gemini+and+ChromaDB" 
    alt="Typing SVG" 
  />
</a>


<br/>

<!-- BADGES ROW 1 -->
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-5+-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev)

<!-- BADGES ROW 2 -->
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)](https://www.trychroma.com)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<!-- BADGES ROW 3 -->
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)](https://github.com)
[![Internship](https://img.shields.io/badge/NEXE.AGENT-Internship%20Project-6366F1?style=for-the-badge)](https://nexe.agent)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)](https://github.com)

<br/>

> **🚀 A production-grade AI Knowledge Assistant** — Upload company documents, generate intelligent embeddings, and get contextual AI-powered answers. Think ChatGPT, but trained exclusively on *your* documents.

<br/>

</div>

---

<div align="center">

## 🧭 Quick Navigation

| Section | Link |
|---|---|
| 🌟 Features | [View Features](#-features) |
| 🏗️ Architecture | [View Architecture](#️-architecture-overview) |
| ⚡ Quick Start | [Get Started](#-quick-start) |
| 🔌 API Reference | [View API](#-api-reference) |
| 📁 Project Structure | [View Structure](#-project-structure) |
| 🛠️ Tech Stack | [View Stack](#️-tech-stack) |
| 🚀 Deployment | [Deploy](#-deployment) |
| 🤝 Contributing | [Contribute](#-contributing) |

</div>

---

<br/>

## 📖 Project Overview

<table>
<tr>
<td width="60%">

**NEXEAGENT RAG Knowledge Assistant** is a full-stack, production-style AI application that transforms static company documents into a **dynamic, conversational knowledge base**.

Built on the **Retrieval-Augmented Generation (RAG)** paradigm, it combines the power of **Google Gemini AI** with a **ChromaDB vector database** to deliver precise, document-grounded answers — no hallucinations, no guesswork.

Think of it as **ChatGPT, but trained on your company's internal knowledge** — policies, manuals, reports, and more.

**Developed as part of the AI & Automation Internship at [NEXE.AGENT](https://nexe.agent)**

</td>
<td width="40%" align="center">

```
📄 Upload Documents
        ↓
🔍 Extract & Chunk Text
        ↓
🧮 Generate Embeddings
        ↓
🗄️ Store in ChromaDB
        ↓
💬 User Asks Question
        ↓
🔎 Vector Similarity Search
        ↓
🤖 Gemini Generates Answer
        ↓
✅ Contextual Response
```

</td>
</tr>
</table>

---

<br/>

## 🌟 Features

<div align="center">

| 🗂️ Document Management | 🤖 AI Intelligence | 💻 Developer Experience |
|---|---|---|
| PDF, TXT, DOCX upload | Google Gemini 2.0 Flash | FastAPI + Swagger docs |
| Drag & drop interface | Context-aware answers | Hot reload dev server |
| Document indexing | Streaming AI responses | Clean REST API design |
| View & delete docs | No hallucinations | Pytest test suite |
| Metadata tracking | Source attribution | Modular architecture |

</div>

<br/>

### 🔑 Core Feature Details

<details>
<summary><b>📤 Intelligent Document Upload System</b></summary>
<br/>

- **Multi-format support**: PDF, TXT, DOCX with automatic format detection
- **Drag & Drop UI**: Modern React-based file upload with progress indicators
- **Validation**: File type and size validation before processing
- **Persistent storage**: Files stored locally with JSON metadata tracking
- **Batch processing**: Upload and process multiple documents simultaneously

</details>

<details>
<summary><b>🧮 Advanced RAG Pipeline</b></summary>
<br/>

- **Smart chunking**: Configurable chunk sizes (default: 800 tokens) with overlap (150 tokens)
- **Gemini Embeddings**: Uses `models/text-embedding-004` for high-quality vector representations
- **ChromaDB storage**: Persistent vector store with fast similarity search
- **TOP-K Retrieval**: Configurable result count for optimal context assembly
- **Context assembly**: Intelligent merging of retrieved chunks for coherent prompting

</details>

<details>
<summary><b>💬 AI Chat Interface</b></summary>
<br/>

- **Session-based history**: Persistent chat conversations per session
- **Context injection**: Retrieved document chunks automatically injected into prompts
- **Streaming responses**: Real-time token streaming for responsive UX
- **Source transparency**: Answers cite which documents were used
- **Fallback handling**: Graceful responses when no relevant documents found

</details>

<details>
<summary><b>📊 Modern Dashboard</b></summary>
<br/>

- **React + Vite**: Lightning-fast development and build times
- **Tailwind CSS**: Utility-first styling with dark mode support
- **Framer Motion**: Smooth animations and page transitions
- **Responsive layout**: Works on desktop, tablet, and mobile
- **Real-time stats**: Document count, index status, query metrics

</details>

---

<br/>

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        NEXEAGENT SYSTEM ARCHITECTURE                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌──────────────────────┐         ┌──────────────────────────────┐    │
│   │   REACT FRONTEND      │ ──────► │      FASTAPI BACKEND         │    │
│   │                      │  HTTP   │                              │    │
│   │  • Upload Page       │ ◄────── │  • /api/upload               │    │
│   │  • Chat Interface    │  REST   │  • /api/documents            │    │
│   │  • Documents Page    │         │  • /api/chat                 │    │
│   │  • Settings Page     │         │  • /api/health               │    │
│   │  • Dashboard/Home    │         │                              │    │
│   └──────────────────────┘         └──────────┬───────────────────┘    │
│                                               │                        │
│                          ┌────────────────────┼──────────────────┐     │
│                          │                    │                  │     │
│                    ┌─────▼──────┐    ┌────────▼───────┐  ┌──────▼───┐ │
│                    │ RAG SERVICE │    │ GEMINI SERVICE  │  │  VECTOR  │ │
│                    │            │    │                │  │  STORE   │ │
│                    │ • Chunking │    │ • Embeddings   │  │          │ │
│                    │ • Pipeline │    │ • Chat/LLM     │  │ ChromaDB │ │
│                    │ • Context  │    │ • Streaming    │  │  SQLite  │ │
│                    └────────────┘    └────────────────┘  └──────────┘ │
│                                                                         │
│   ┌──────────────────────────────────────────────────────────────────┐ │
│   │                        DATA LAYER                                │ │
│   │  📁 data/uploads/  │  🗄️ data/chroma/  │  📋 data/metadata/    │ │
│   │  📜 data/chat_history/  │  📝 data/logs/                        │ │
│   └──────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘
```

### 🔄 RAG Pipeline Deep Dive

```
INGESTION PHASE
───────────────
📄 Raw Document
    │
    ▼
📝 Text Extraction (PDF/DOCX/TXT parsers)
    │
    ▼
✂️  Smart Chunking  ──── chunk_size: 800 tokens
    │                    chunk_overlap: 150 tokens
    ▼
🧮 Gemini Embedding Generation (text-embedding-004)
    │
    ▼
🗄️  ChromaDB Vector Storage  ──── Persistent SQLite backend


QUERY PHASE
───────────
💬 User Query
    │
    ▼
🧮 Query Embedding Generation
    │
    ▼
🔎 Cosine Similarity Search (TOP-K=5)
    │
    ▼
📋 Context Assembly (retrieved chunks)
    │
    ▼
🤖 Gemini LLM  ──── System prompt + Context + Query
    │
    ▼
✅ Grounded, Accurate Answer
```

---

<br/>

## 📁 Project Structure

```
nexeagent-rag-knowledge-assistant/
│
├── 📄 README.md                      # You are here
├── 📄 API.md                         # Full API documentation
├── 🔐 .env                           # Root env (optional)
│
├── 🐍 backend/
│   ├── 📄 run.py                     # Entry point — starts Uvicorn server
│   ├── 📄 requirements.txt           # Python dependencies
│   ├── 📄 pytest.ini                 # Test configuration
│   ├── 🔐 .env                       # Backend environment variables
│   │
│   ├── 📦 app/
│   │   ├── 📄 main.py                # FastAPI app initialization + CORS
│   │   ├── 📄 config.py              # Settings loader (env vars)
│   │   │
│   │   ├── 🔌 api/
│   │   │   └── routes/
│   │   │       ├── 📄 chat.py        # POST /api/chat endpoint
│   │   │       ├── 📄 documents.py   # GET/DELETE /api/documents
│   │   │       ├── 📄 upload.py      # POST /api/upload endpoint
│   │   │       └── 📄 health.py      # GET /api/health
│   │   │
│   │   ├── 🧠 services/
│   │   │   ├── 📄 rag_service.py         # Core RAG orchestration
│   │   │   ├── 📄 gemini_service.py      # Google Gemini API client
│   │   │   ├── 📄 embedding_service.py   # Embedding generation
│   │   │   ├── 📄 vector_store_service.py# ChromaDB operations
│   │   │   ├── 📄 retrieval_service.py   # Similarity search logic
│   │   │   ├── 📄 query_service.py       # Query processing pipeline
│   │   │   └── 📄 pdf_service.py         # Document text extraction
│   │   │
│   │   ├── 📐 models/
│   │   │   └── 📄 schemas.py         # Pydantic request/response models
│   │   │
│   │   └── 🛠️  utils/
│   │       ├── 📄 chunking.py        # Text chunking strategies
│   │       ├── 📄 file_utils.py      # File I/O helpers
│   │       └── 📄 logger.py          # Structured logging setup
│   │
│   ├── 📦 data/
│   │   ├── 📁 uploads/               # Raw uploaded documents
│   │   ├── 🗄️  chroma/               # ChromaDB vector store files
│   │   │   └── chroma.sqlite3
│   │   ├── 📋 metadata/              # Document metadata (JSON)
│   │   └── 💬 chat_history/          # Saved chat sessions (JSON)
│   │
│   ├── 📝 logs/                      # Application logs
│   ├── 📚 sample_docs/
│   │   └── company_policy.txt        # Sample document for testing
│   └── 🧪 tests/
│       ├── test_api.py               # API endpoint tests
│       └── test_chunking.py          # Chunking logic tests
│
└── ⚛️  frontend/
    ├── 📄 index.html                 # Root HTML template
    ├── 📄 package.json               # Node.js dependencies
    ├── 📄 vite.config.js             # Vite build configuration
    ├── 📄 tailwind.config.js         # Tailwind CSS configuration
    ├── 📄 postcss.config.js          # PostCSS configuration
    │
    └── 📦 src/
        ├── 📄 App.jsx                # Root React component + routing
        ├── 📄 main.jsx               # React DOM entry point
        ├── 📄 index.css              # Global styles + Tailwind imports
        │
        ├── 🧩 components/
        │   ├── ChatMessage.jsx       # Individual chat bubble component
        │   ├── FileUpload.jsx        # Drag & drop upload component
        │   ├── Layout.jsx            # App shell with sidebar
        │   ├── LoadingSpinner.jsx    # Animated loading indicator
        │   ├── Sidebar.jsx           # Navigation sidebar
        │   ├── StatCard.jsx          # Dashboard stat display card
        │   └── TypingIndicator.jsx   # AI "thinking" animation
        │
        ├── 📄 context/
        │   └── ThemeContext.jsx      # Dark/light mode context
        │
        ├── 📄 pages/
        │   ├── Home.jsx              # Dashboard with stats overview
        │   ├── Chat.jsx              # Main AI chat interface
        │   ├── Documents.jsx         # Document library & management
        │   ├── Upload.jsx            # File upload workflow page
        │   └── Settings.jsx          # App configuration page
        │
        └── 📄 services/
            └── api.js                # Axios API client + all endpoints
```

---

<br/>

## ⚡ Quick Start

### 📋 Prerequisites

Before you begin, ensure you have:

| Requirement | Version | Download |
|---|---|---|
| Python | 3.11+ | [python.org](https://python.org) |
| Node.js | 18+ | [nodejs.org](https://nodejs.org) |
| Google Gemini API Key | — | [aistudio.google.com](https://aistudio.google.com/apikey) |
| Git | Latest | [git-scm.com](https://git-scm.com) |

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/nexeagent-rag-knowledge-assistant.git
cd nexeagent-rag-knowledge-assistant
```

---

### 2️⃣ Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env      # Windows
# cp .env.example .env      # macOS/Linux
```

Edit `backend/.env` with your API key:

```env
# ── Google Gemini ──────────────────────────────────
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
GEMINI_EMBEDDING_MODEL=models/text-embedding-004

# ── RAG Configuration ─────────────────────────────
CHUNK_SIZE=800
CHUNK_OVERLAP=150
TOP_K_RESULTS=5

# ── Server ────────────────────────────────────────
HOST=0.0.0.0
PORT=8000
DEBUG=false
```

Start the backend server:

```bash
python run.py
```

> ✅ API running at **http://localhost:8000**

> 📚 Swagger docs at **http://localhost:8000/docs**

> 📖 ReDoc at **http://localhost:8000/redoc**


---

### 3️⃣ Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

> ✅ Frontend running at **http://localhost:5173**

---

### 4️⃣ Test the Full RAG Pipeline

```
1. Open http://localhost:5173
2. Navigate to → Upload
3. Upload the sample file: backend/sample_docs/company_policy.txt
4. Wait for indexing to complete ✅
5. Navigate to → Chat
6. Ask: "What is the refund policy?"
7. Receive a grounded AI answer from your document 🎉
```

---

<br/>

## 🔧 Environment Variables Reference

| Variable | Description | Default | Required |
|---|---|---|---|
| `GEMINI_API_KEY` | Google Gemini API authentication key | — | ✅ Yes |
| `GEMINI_MODEL` | Chat/generation model ID | `gemini-2.0-flash` | ✅ Yes |
| `GEMINI_EMBEDDING_MODEL` | Embedding model ID | `models/text-embedding-004` | ✅ Yes |
| `CHUNK_SIZE` | Token count per text chunk | `800` | ❌ No |
| `CHUNK_OVERLAP` | Overlap tokens between chunks | `150` | ❌ No |
| `TOP_K_RESULTS` | Number of chunks retrieved per query | `5` | ❌ No |
| `HOST` | Backend server host | `0.0.0.0` | ❌ No |
| `PORT` | Backend server port | `8000` | ❌ No |
| `DEBUG` | Enable debug mode | `false` | ❌ No |

---

<br/>

## 🔌 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

---

#### 🟢 `GET /api/health`
Check if the API is alive.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

#### 📤 `POST /api/upload`
Upload and index a document into the RAG pipeline.

**Request:** `multipart/form-data`

| Field | Type | Description |
|---|---|---|
| `file` | File | PDF, TXT, or DOCX file |

**Response:**
```json
{
  "success": true,
  "document_id": "doc_abc123",
  "filename": "company_policy.txt",
  "chunks_created": 14,
  "message": "Document indexed successfully"
}
```

---

#### 💬 `POST /api/chat`
Send a message and receive an AI-generated, document-grounded response.

**Request Body:**
```json
{
  "message": "What is the refund policy?",
  "session_id": "session_xyz789",
  "stream": false
}
```

**Response:**
```json
{
  "answer": "According to the company policy document, refunds are processed within 7-10 business days...",
  "sources": ["company_policy.txt"],
  "session_id": "session_xyz789",
  "tokens_used": 342
}
```

---

#### 📋 `GET /api/documents`
Retrieve a list of all indexed documents.

**Response:**
```json
{
  "documents": [
    {
      "id": "doc_abc123",
      "filename": "company_policy.txt",
      "size_bytes": 24310,
      "chunks": 14,
      "uploaded_at": "2024-01-15T10:00:00Z",
      "status": "indexed"
    }
  ],
  "total": 1
}
```

---

#### 🗑️ `DELETE /api/documents/{document_id}`
Remove a document and its vectors from the knowledge base.

**Response:**
```json
{
  "success": true,
  "message": "Document doc_abc123 deleted successfully"
}
```

---

#### 🔍 `GET /api/documents/{document_id}`
Retrieve metadata for a specific document.

**Response:**
```json
{
  "id": "doc_abc123",
  "filename": "company_policy.txt",
  "chunks": 14,
  "status": "indexed",
  "uploaded_at": "2024-01-15T10:00:00Z"
}
```

---

<br/>

## 🛠️ Tech Stack

<div align="center">

### Frontend Layer

| Technology | Version | Purpose |
|---|---|---|
| ⚛️ **React.js** | 18+ | UI component framework |
| ⚡ **Vite** | 5+ | Build tool & dev server |
| 🎨 **Tailwind CSS** | 3.x | Utility-first styling |
| 🎭 **Framer Motion** | 11+ | Animations & transitions |
| 🔗 **Axios** | 1.x | HTTP client for API calls |
| 🎯 **Lucide React** | Latest | Icon library |

### Backend Layer

| Technology | Version | Purpose |
|---|---|---|
| 🐍 **Python** | 3.11+ | Core runtime language |
| 🚀 **FastAPI** | 0.110+ | Async REST API framework |
| 🦄 **Uvicorn** | Latest | ASGI server |
| 🔍 **Pydantic** | 2.x | Data validation & schemas |

### AI & Machine Learning Layer

| Technology | Version | Purpose |
|---|---|---|
| 🤖 **Google Gemini** | 2.0 Flash | LLM for chat responses |
| 🧮 **Gemini Embeddings** | text-embedding-004 | Vector generation |
| 🗄️ **ChromaDB** | Latest | Vector database |

### Storage & Infrastructure

| Technology | Purpose |
|---|---|
| 📁 **Local Filesystem** | Raw document storage |
| 🗃️ **SQLite** | ChromaDB backend |
| 📋 **JSON** | Metadata & chat history |

</div>

---

<br/>

## 🖥️ Frontend Pages

| Page | Route | Description |
|---|---|---|
| 🏠 **Home / Dashboard** | `/` | System stats, quick actions, overview |
| 💬 **Chat** | `/chat` | AI conversation interface with history |
| 📤 **Upload** | `/upload` | Drag & drop document upload |
| 📚 **Documents** | `/documents` | Document library, index status, delete |
| ⚙️ **Settings** | `/settings` | API keys, model config, preferences |

---

<br/>

## 🧪 Running Tests

```bash
# Navigate to backend
cd backend

# Activate virtual environment
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_api.py -v
pytest tests/test_chunking.py -v

# Run with coverage report
pytest tests/ -v --cov=app --cov-report=html
```

**Test Coverage:**

| Test File | Tests | Coverage |
|---|---|---|
| `test_api.py` | API endpoint validation | Upload, Chat, Documents, Health routes |
| `test_chunking.py` | Text processing logic | Chunking strategies, overlap, edge cases |

---

<br/>

## 📸 Screenshots

> 💡 *Add your screenshots here after running the project locally.*

<div align="center">

| Dashboard | Chat Interface |
|---|---|
| `[dashboard-screenshot.png]` | `[chat-screenshot.png]` |

| Document Upload | Document Library |
|---|---|
| `[upload-screenshot.png]` | `[documents-screenshot.png]` |

</div>

---

<br/>

## 🚀 Deployment

### 🐳 Docker Deployment (Recommended)

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend/data:/app/data

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

```bash
docker-compose up --build
```

### ☁️ Cloud Deployment Options

| Platform | Backend | Frontend |
|---|---|---|
| **Railway** | ✅ Python/FastAPI | ✅ Static |
| **Render** | ✅ Python service | ✅ Static site |
| **Vercel** | ❌ (use separate) | ✅ Best for React |
| **Fly.io** | ✅ Docker support | ✅ Docker support |
| **AWS EC2** | ✅ Full control | ✅ Full control |

### 📦 Production Build

```bash
# Frontend production build
cd frontend
npm run build
# Output in: frontend/dist/

# Backend production start
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

<br/>

## 🔐 Security Notes

> ⚠️ **Important security considerations for production deployment:**

- 🔑 **Never commit `.env` files** to version control — use `.gitignore`
- 🛡️ **CORS Configuration** — Restrict `allow_origins` to your actual frontend domain in production
- 🔒 **API Key Rotation** — Regularly rotate your Gemini API key
- 📏 **File Size Limits** — Configure upload limits to prevent resource exhaustion
- 🚫 **Rate Limiting** — Add rate limiting to chat and upload endpoints
- 🗂️ **File Type Validation** — Only allow PDF, TXT, DOCX; reject executable files
- 🔐 **Auth Layer** — Add JWT authentication before exposing to public internet

---

<br/>

## 🔮 Future Improvements

```
Planned Roadmap
───────────────

Phase 2 — Enhanced Intelligence
  □ Multi-document cross-referencing
  □ Streaming responses with SSE
  □ Source highlighting in responses
  □ Confidence scores for answers

Phase 3 — Enterprise Features
  □ User authentication (JWT)
  □ Role-based access control
  □ Multi-tenant document namespacing
  □ Audit logging for compliance

Phase 4 — Scale & Performance
  □ Redis for chat session caching
  □ Celery for async document processing
  □ PostgreSQL for metadata (replace JSON)
  □ S3-compatible cloud document storage

Phase 5 — Advanced AI
  □ Model switching (OpenAI, Anthropic, local LLMs)
  □ Fine-tuned domain-specific embeddings
  □ Document summarization pipeline
  □ Automated knowledge graph extraction
```

---

<br/>

## 🤝 Contributing

Contributions are welcome! Follow these steps:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YasirAwan4831/nexeagent-rag-knowledge-assistant.git

# 3. Create a feature branch
git checkout -b feature/amazing-feature

# 4. Make your changes and commit
git add .
git commit -m "feat: add amazing feature"

# 5. Push to your fork
git push origin feature/amazing-feature

# 6. Open a Pull Request on GitHub
```

### Commit Message Convention

```
feat:     New feature
fix:      Bug fix
docs:     Documentation update
style:    Code formatting (no logic change)
refactor: Code restructuring
test:     Adding tests
chore:    Build or config changes
```

---

<br/>

## 📄 License

```
MIT License

Copyright (c) 2026 Muhammad Yasir — NEXE.AGENT Internship

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense and/or sell
copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

See the full [LICENSE](./LICENSE) file for details.

---

<br/>

## 👤 About the Developer

<div align="center">

<!-- REPLACE THE PLACEHOLDERS BELOW WITH YOUR ACTUAL DETAILS -->


| Platform | Link |
|:---|:---|
| 🌐 **Portfolio** | [yasirawaninfo.vercel.app](https://yasirawaninfo.vercel.app/) |
| 💼 **LinkedIn** | [linkedin.com/in/yasirawan4831](https://linkedin.com/in/yasirawan4831) |
| ▶️ **YouTube** | [youtube.com/@YasirTech-t1d](https://www.youtube.com/@YasirTech-t1d) |
| 🐙 **GitHub** | [github.com/YasirAwan4831](https://github.com/YasirAwan4831) |
| 🐦 **X (Twitter)** | [x.com/yasirawan4831](https://x.com/yasirawan4831) |
| 📸 **Instagram** | [instagram.com/yasirawan4831](https://instagram.com/yasirawan4831) |
| 🔗 **Linktree** | [yasirawan4831.github.io/futuristic-links-dashboard](https://yasirawan4831.github.io/futuristic-links-dashboard/) |
| 📧 **Email** | my3154831409@gmail.com |

<!-- BADGES — REPLACE YOUR_USERNAME WITH YOUR ACTUAL GITHUB USERNAME -->
<!--
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](YOUR_LINKEDIN_URL)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/YOUR_USERNAME)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-6366F1?style=for-the-badge&logo=vercel)](YOUR_PORTFOLIO_URL)
-->

</div>

---

<br/>

## 🙏 Acknowledgements

- **[NEXE.AGENT](https://nexe.agent)** — For the AI & Automation Internship opportunity
- **[Google Gemini](https://deepmind.google/technologies/gemini/)** — For the powerful LLM and embedding APIs
- **[ChromaDB](https://www.trychroma.com/)** — For the excellent open-source vector database
- **[FastAPI](https://fastapi.tiangolo.com/)** — For the elegant Python API framework
- **[Shields.io](https://shields.io/)** — For the beautiful README badges
- **[Capsule Render](https://github.com/kyechan99/capsule-render)** — For the SVG banner animations
- **[Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg)** — For the typing animation

---


**⭐ If this project helped you, please consider giving it a star!**

------------
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&text=Developed%20%20By%20Muhammad Yasir at Nexe-Adent&fontSize=20&fontColor=ffffff&animation=fadeIn" width="100%"/>
