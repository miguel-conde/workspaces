import pytest
from multiply_ms.app.schemas.request_schema import MultiplyRequestBody
from multiply_ms.app.services import micro_service


@pytest.mark.asyncio
async def test_execute_double():
    body = MultiplyRequestBody(value=4)
    result = await micro_service.execute(body)
    assert result == 8
