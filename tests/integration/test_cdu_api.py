import pytest
import httpx
import respx
from calc_cdu.main import app


@pytest.mark.asyncio
async def test_cdu_add_then_double():
    async with respx.MockRouter() as mock:
        # stub del MS de suma
        mock.post("http://localhost:8001/microservice/send_data/").respond(
            json={"data": 9}, status_code=200
        )
        # stub del MS de multiplicar
        mock.post("http://localhost:8002/microservice/send_data/").respond(
            json={"data": 18}, status_code=200
        )

        # llamamos al endpoint del CDU
        async with httpx.AsyncClient(
            app=app, base_url="http://test"
        ) as client:
            r = await client.post("/cdu/add_then_double/", 
                                  json={"a": 4, "b": 5})

        assert r.status_code == 200
        assert r.json()["data"] == 18
