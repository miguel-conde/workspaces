import pytest
from addition_ms.app.schemas.request_schema import AddRequestBody
from addition_ms.app.services import micro_service


@pytest.mark.asyncio
async def test_execute_sum():
    body = AddRequestBody(a=2, b=5)
    result = await micro_service.execute(body)   # ← await
    assert result == 7
