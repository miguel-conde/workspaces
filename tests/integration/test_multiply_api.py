import pytest
from multiply_ms.main import app as multiply_app


@pytest.mark.asyncio
async def test_multiply_direct(async_client_factory, respx_mock):
    async with async_client_factory(app=multiply_app) as client:
        r = await client.post(
            "/microservice/send_data/", 
            json={"value": 6}
        )
    assert r.status_code == 200
    assert r.json()["data"] == 12
