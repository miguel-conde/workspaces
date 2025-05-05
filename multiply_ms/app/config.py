"""
Configuración del microservicio utilizando Pydantic.

"""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "MULTIPLY MS")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")


settings = Settings()