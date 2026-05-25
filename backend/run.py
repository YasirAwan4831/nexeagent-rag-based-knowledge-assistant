"""Run the FastAPI development server.

Usage:
    python run.py                                    # Uses config from .env
    uvicorn app.main:app --reload --reload-dir app  # Direct uvicorn command
"""

import uvicorn

from app.config import get_settings

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        reload_dirs=["app"] if settings.debug else None,
    )
