from fastapi import APIRouter
from addition_ms.app.schemas.request_schema import AddRequestBody
from addition_ms.app.schemas.response_schema import ResponseBody
from addition_ms.app.services import micro_service

router = APIRouter()


@router.post("/microservice/send_data/", response_model=ResponseBody)
async def send_data(body: AddRequestBody):
    result = await micro_service.execute(body)
    return ResponseBody(data=result)
