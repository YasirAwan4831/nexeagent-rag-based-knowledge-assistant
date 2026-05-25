"""Centralized logging configuration."""

import logging
import sys
from pathlib import Path

from app.config import get_settings


def setup_logging() -> logging.Logger:
    settings = get_settings()
    log_dir = settings.logs_path
    log_file = log_dir / "nexeagent.log"

    logger = logging.getLogger("nexeagent")
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG if settings.debug else logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logging()
