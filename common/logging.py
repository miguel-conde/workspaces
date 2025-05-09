import logging
import os
import structlog
from pythonjsonlogger import jsonlogger

LEVEL_NAME = os.getenv("LOG_LEVEL", "INFO").upper()
MIN_LEVEL = getattr(logging, LEVEL_NAME, logging.INFO)  # ← traduce a numérico


def configure_logging():
    # formateador JSON para el root logger
    handler = logging.StreamHandler()
    handler.setFormatter(jsonlogger.JsonFormatter())

    logging.basicConfig(
        handlers=[handler],
        level=MIN_LEVEL,
        force=True
    )

    # structlog env‑friendly
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(MIN_LEVEL),
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ]
    )
