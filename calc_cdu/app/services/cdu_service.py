import httpx
from tenacity import (
    retry, stop_after_attempt, wait_fixed, retry_if_exception_type
)
from fastapi import Request
from calc_cdu.app.config import settings  
from common.exceptions import UpstreamError, InputError
from calc_cdu.app.schemas.request_schema import AddThenDoubleRequestBody
from calc_cdu.app.schemas.response_schema import ResponseBody
from common.middleware import TRACE_HEADER

ADDITION_URL = settings.addition_url
MULTIPLY_URL = settings.multiply_url

TIMEOUT = httpx.Timeout(3.0)  # 3 s a cada microservicio

# policy:  3 intentos, espera 0.5 s entre ellos, sólo si recibe UpstreamError
retry_policy = retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_fixed(0.5),
    retry=retry_if_exception_type(UpstreamError)
)


@retry_policy
async def call_ms(url: str, payload: dict, trace_id: str) -> float:
    headers = {TRACE_HEADER: trace_id}
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        try:
            r = await client.post(url, json=payload, headers=headers)
        except httpx.RequestError as exc:
            raise UpstreamError(
                f"microservicio no disponible: {exc}"
            ) from exc

        if r.status_code != 200:
            raise UpstreamError(
                f"microservicio respondió {r.status_code}: {r.text}"
            )

        return r.json()["data"]  # puede lanzar KeyError


async def add_then_double(
    body: AddThenDoubleRequestBody,
    request: Request,
) -> ResponseBody:
    if body.a is None or body.b is None:
        raise InputError("Faltan a o b")

    trace_id = request.state.trace_id         # ← más claro
    logger = request.state.logger.bind(service="calc-cdu")

    logger.info("orchestration_start", a=body.a, b=body.b)

    suma = await call_ms(ADDITION_URL, {"a": body.a, "b": body.b}, trace_id)
    doble = await call_ms(MULTIPLY_URL, {"value": suma}, trace_id)

    logger.info("orchestration_end", result=doble)
    return ResponseBody(data=doble)