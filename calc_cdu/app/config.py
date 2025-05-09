from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "calc-cdu"
    environment: str = "development"
    addition_url: str = "http://localhost:8001/microservice/send_data/"
    multiply_url: str = "http://localhost:8002/microservice/send_data/"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()  # se evalúa en import
