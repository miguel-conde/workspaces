from fastapi import FastAPI
from multiply_ms.app.routes import microservice_endpoints
from multiply_ms.app.config import settings

app = FastAPI(title="Multiply‑MS")
app.include_router(microservice_endpoints.router)


@app.get("/health")
async def health():
    """
    Health check endpoint para comprobar si el microservicio está en 
    funcionamiento.
    """
    return {"message": "Fast API Skeleton is up!"}


@app.on_event("startup")
async def on_startup():
    print(f"Starting {settings.PROJECT_NAME} in \
            {settings.ENVIRONMENT} environment...")


@app.on_event("shutdown")
async def on_shutdown():
    print(f"Shutting down {settings.PROJECT_NAME}...")