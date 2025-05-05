from pydantic import BaseModel


class AddRequestBody(BaseModel):
    a: float
    b: float
