from fastapi import APIRouter
from multiply_ms.app.schemas.request_schema import MultiplyRequestBody
from multiply_ms.app.schemas.response_schema import ResponseBody
from multiply_ms.app.services import micro_service

router = APIRouter()


@router.post("/microservice/send_data/", response_model=ResponseBody)
async def send_data(body: MultiplyRequestBody):
    result = await micro_service.execute(body)
    return ResponseBody(data=result)
