"""
Configuración del microservicio utilizando Pydantic.

"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # identidad / metadatos
    project_name: str = "addition-ms"
    environment: str = "development"

    # puerto (no lo usa FastAPI directamente,
    #        pero puede servir a health probes o docs)
    port: int = 8001

    model_config = SettingsConfigDict(
        env_file=".env",        # busca en la misma carpeta del servicio
        extra="ignore"          # ignora variables no declaradas
    )


settings = Settings()
