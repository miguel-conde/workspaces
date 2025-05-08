import os
import httpx
from tenacity import (
    retry, stop_after_attempt, wait_fixed, retry_if_exception_type
)
from common.exceptions import UpstreamError, InputError
from calc_cdu.app.schemas.request_schema import AddThenDoubleRequestBody
from calc_cdu.app.schemas.response_schema import ResponseBody

ADDITION_URL = os.getenv("ADDITION_URL",
                         "http://localhost:8001/microservice/send_data/")
MULTIPLY_URL = os.getenv("MULTIPLY_URL",
                         "http://localhost:8002/microservice/send_data/")

TIMEOUT = httpx.Timeout(3.0)  # 3 s a cada microservicio

# policy:  3 intentos, espera 0.5 s entre ellos, sólo si recibe UpstreamError
retry_policy = retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_fixed(0.5),
    retry=retry_if_exception_type(UpstreamError)
)


@retry_policy
async def call_ms(url: str, payload: dict) -> float:
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        try:
            r = await client.post(url, json=payload)
        except httpx.RequestError as exc:
            raise UpstreamError(
                f"microservicio no disponible: {exc}"
            ) from exc

        if r.status_code != 200:
            raise UpstreamError(
                f"microservicio respondió {r.status_code}: {r.text}"
            )

        return r.json()["data"]  # puede lanzar KeyError


async def add_then_double(body: AddThenDoubleRequestBody) -> ResponseBody:
    # validación simple de entrada
    if body.a is None or body.b is None:
        raise InputError("Faltan a o b")

    suma = await call_ms(ADDITION_URL, {"a": body.a, "b": body.b})
    doble = await call_ms(MULTIPLY_URL, {"value": suma})

    return ResponseBody(data=doble)
