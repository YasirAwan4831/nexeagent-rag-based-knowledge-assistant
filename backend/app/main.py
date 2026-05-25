"""NEXEAGENT RAG Knowledge Assistant - FastAPI Application Entry Point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app import __version__
from app.api.routes import chat, documents, health, upload
from app.config import get_settings
from app.utils.logger import logger, setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    settings = get_settings()
    settings.uploads_path
    settings.chroma_path
    settings.metadata_path
    settings.chat_history_path
    logger.info("NEXEAGENT RAG Knowledge Assistant v%s starting", __version__)
    yield
    logger.info("Application shutdown")


app = FastAPI(
    title="NEXEAGENT RAG Knowledge Assistant",
    description="Production-style RAG API for company document knowledge",
    version=__version__,
    lifespan=lifespan,
)

settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(documents.router, prefix="/api")
app.include_router(chat.router, prefix="/api")


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled error on %s: %s", request.url.path, exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred", "error_code": "INTERNAL_ERROR"},
    )


@app.get("/")
async def root():
    return {
        "name": "NEXEAGENT RAG Knowledge Assistant",
        "version": __version__,
        "docs": "/docs",
        "health": "/api/health",
    }
