import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "CALC CDU MS")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    addition_url: str = "http://localhost:8001/microservice/send_data/"
    multiply_url: str = "http://localhost:8002/microservice/send_data/"

    class Config:
        env_file = ".env"


settings = Settings()
