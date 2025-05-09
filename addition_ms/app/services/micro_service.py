import structlog
from addition_ms.app.schemas.request_schema import AddRequestBody


async def execute(body: AddRequestBody) -> float:
    logger = structlog.get_logger().bind(service="addition-ms")
    result = body.a + body.b
    logger.info("sum_completed", a=body.a, b=body.b, result=result)
    return result
