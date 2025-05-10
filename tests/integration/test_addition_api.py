import pytest
from addition_ms.main import app as addition_app


@pytest.mark.asyncio
async def test_addition_direct(async_client_factory, respx_mock):
    async with async_client_factory(app=addition_app) as client:
        r = await client.post(
            "/microservice/send_data/", 
            json={"a": 2, "b": 3}
        )
    assert r.status_code == 200
    assert r.json()["data"] == 5
