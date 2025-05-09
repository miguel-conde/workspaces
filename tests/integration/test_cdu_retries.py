import respx
import pytest
import httpx
from calc_cdu.main import app
from calc_cdu.app.config import settings


@respx.mock
@pytest.mark.asyncio
async def test_cdu_retries(respx_mock):
    # 1.ª y 2.ª llamada fallan, 3.ª funciona
    route_add = respx_mock.post(settings.addition_url).mock(
        side_effect=[
            httpx.ConnectTimeout("boom"),
            httpx.ConnectTimeout("boom"),
            httpx.Response(200, json={"data": 9})
        ]
    )

    # Multiply‑MS responde bien a la primera
    respx_mock.post(settings.multiply_url).respond(json={"data": 18})

    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        r = await client.post("/cdu/add_then_double/", json={"a": 4, "b": 5})

    assert route_add.call_count == 3
    assert r.status_code == 200
    assert r.json()["data"] == 18
