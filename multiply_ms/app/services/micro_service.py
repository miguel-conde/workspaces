from multiply_ms.app.schemas.request_schema import MultiplyRequestBody


async def execute(body: MultiplyRequestBody) -> float:
    return body.value * 2
