import uuid
import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

TRACE_HEADER = "X-Trace-Id"


class TraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = request.headers.get(TRACE_HEADER, str(uuid.uuid4()))
        # logger con trace vinculado
        logger = structlog.get_logger().bind(trace_id=trace_id)

        # guarda en el estado de la request para usar en endpoints
        request.state.logger = logger
        request.state.trace_id = trace_id
        response = await call_next(request)
        response.headers[TRACE_HEADER] = trace_id
        return response
