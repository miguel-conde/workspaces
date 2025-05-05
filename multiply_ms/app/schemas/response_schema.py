from pydantic import BaseModel
from typing import Any


class ResponseBody(BaseModel):
    data: Any
    message: str = "ok"
