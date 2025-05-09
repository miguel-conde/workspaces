import structlog
from multiply_ms.app.schemas.request_schema import MultiplyRequestBody


async def execute(body: MultiplyRequestBody) -> float:
    logger = structlog.get_logger().bind(service="multiply-ms")
    result = body.value * 2
    logger.info("multiply_completed", value=body.value, result=result)
    return result
