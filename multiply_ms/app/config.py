"""
Configuración del microservicio utilizando Pydantic.

"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "multiply-ms"
    environment: str = "development"
    port: int = 8002

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
