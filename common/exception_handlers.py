# common/exception_handlers.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from common.exceptions import (
    AppError, InputError, BusinessError, UpstreamError
)


def add_exception_handlers(app: FastAPI) -> None:
    """Registra manejadores JSON uniformes en la instancia FastAPI."""

    @app.exception_handler(InputError)
    async def handle_input(_, exc: InputError):
        return JSONResponse({"detail": str(exc)}, status_code=400)

    @app.exception_handler(BusinessError)
    async def handle_business(_, exc: BusinessError):
        return JSONResponse({"detail": str(exc)}, status_code=422)

    @app.exception_handler(UpstreamError)
    async def handle_upstream(_, exc: UpstreamError):
        return JSONResponse({"detail": str(exc)}, status_code=502)

    @app.exception_handler(AppError)
    async def handle_app(_, exc: AppError):
        return JSONResponse({"detail": str(exc)}, status_code=500)
