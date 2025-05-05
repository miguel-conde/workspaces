from pydantic import BaseModel


class AddThenDoubleRequestBody(BaseModel):
    a: float
    b: float
