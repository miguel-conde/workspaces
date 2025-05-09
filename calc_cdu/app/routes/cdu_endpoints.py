from fastapi import Request
from fastapi import APIRouter
from calc_cdu.app.schemas.request_schema import AddThenDoubleRequestBody
from calc_cdu.app.services import cdu_service

router = APIRouter()


@router.post("/cdu/add_then_double/")
async def add_then_double(body: AddThenDoubleRequestBody, request: Request):
    return await cdu_service.add_then_double(body, request)
