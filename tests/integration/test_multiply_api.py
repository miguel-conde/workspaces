import pytest
import httpx
from multiply_ms.main import app


@pytest.mark.asyncio
async def test_multiply_endpoint():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        r = await client.post("/microservice/send_data/", json={"value": 6})
        assert r.status_code == 200
        assert r.json()["data"] == 12
