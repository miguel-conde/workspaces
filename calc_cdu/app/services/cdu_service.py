import os
import httpx
from calc_cdu.app.schemas.request_schema import AddThenDoubleRequestBody
from calc_cdu.app.schemas.response_schema import ResponseBody

ADDITION_URL = os.getenv("ADDITION_URL", 
                         "http://localhost:8001/microservice/send_data/")
MULTIPLY_URL = os.getenv("MULTIPLY_URL", 
                         "http://localhost:8002/microservice/send_data/")


async def add_then_double(body: AddThenDoubleRequestBody) -> ResponseBody:
    async with httpx.AsyncClient() as client:
        # 1) Sumar  (QUITAMOS el wrapper "body")
        r1 = await client.post(
            ADDITION_URL,
            json={"a": body.a, "b": body.b}
        )
        r1.raise_for_status()     # buena práctica: lanza excepción si != 2xx
        suma = r1.json()["data"]

        # 2) Multiplicar
        r2 = await client.post(
            MULTIPLY_URL,
            json={"value": suma}  # también sin wrapper
        )
        r2.raise_for_status()
        doble = r2.json()["data"]

    return ResponseBody(data=doble)
