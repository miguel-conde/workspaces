import pytest
import httpx
from calc_cdu.app.config import settings


@pytest.mark.asyncio
async def test_cdu_retries(async_client, respx_mock):
    # 1.ª y 2.ª llamada fallan, 3.ª funciona
    route_add = respx_mock.post(settings.addition_url).mock(
        side_effect=[
            httpx.ConnectTimeout("boom"),
            httpx.ConnectTimeout("boom"),
            httpx.Response(200, json={"data": 9})
        ]
    )

    # Multiply-MS responde bien a la primera
    respx_mock.post(settings.multiply_url).respond(json={"data": 18})

    r = await async_client.post("/cdu/add_then_double/", json={"a": 4, "b": 5})

    assert route_add.call_count == 3
    assert r.status_code == 200
    assert r.json()["data"] == 18
