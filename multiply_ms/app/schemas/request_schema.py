from pydantic import BaseModel


class MultiplyRequestBody(BaseModel):
    value: float
