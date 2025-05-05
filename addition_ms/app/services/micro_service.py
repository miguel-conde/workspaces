from addition_ms.app.schemas.request_schema import AddRequestBody


async def execute(body: AddRequestBody) -> float:
    return body.a + body.b
