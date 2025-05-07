import pytest
import httpx
from addition_ms.main import app


@pytest.mark.asyncio
async def test_addition_endpoint():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        r = await client.post("/microservice/send_data/",
                              json={"a": 1, "b": 3})
        assert r.status_code == 200
        assert r.json()["data"] == 4
