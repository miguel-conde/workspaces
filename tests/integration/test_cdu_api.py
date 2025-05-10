import pytest
from calc_cdu.app.config import settings


@pytest.mark.asyncio
async def test_cdu_add_then_double(async_client, respx_mock):
    respx_mock.post(settings.addition_url).respond(json={"data": 8})
    respx_mock.post(settings.multiply_url).respond(json={"data": 16})

    r = await async_client.post("/cdu/add_then_double/", json={"a": 5, "b": 3})

    assert r.status_code == 200
    assert r.json()["data"] == 16
