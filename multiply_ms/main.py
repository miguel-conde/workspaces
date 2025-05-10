from contextlib import asynccontextmanager
from fastapi import FastAPI
from common.exception_handlers import add_exception_handlers
from multiply_ms.app.routes import microservice_endpoints
from multiply_ms.app.config import settings
from common.logging import configure_logging
from common.middleware import TraceMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    print(f"🌱 {settings.project_name} up"
          f"in {settings.environment}…")
    yield
    print(f"🌿 {settings.project_name} down"
          f"in {settings.environment}…")


app = FastAPI(title=settings.project_name, lifespan=lifespan)
configure_logging()
app.add_middleware(TraceMiddleware)
add_exception_handlers(app)
app.include_router(microservice_endpoints.router)


@app.get("/health")
async def health():
    """
    Health check endpoint para comprobar si el microservicio está en 
    funcionamiento.
    """
    return {"message": "Fast API Skeleton is up!"}