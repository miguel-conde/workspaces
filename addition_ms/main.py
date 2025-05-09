from fastapi import FastAPI
from common.exception_handlers import add_exception_handlers
from addition_ms.app.routes import microservice_endpoints
from addition_ms.app.config import settings
from common.logging import configure_logging
from common.middleware import TraceMiddleware


app = FastAPI(title="Addition‑MS")
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


@app.on_event("startup")
async def on_startup():
    print(f"Starting {settings.project_name} in \
            {settings.environment} environment...")


@app.on_event("shutdown")
async def on_shutdown():
    print(f"Shutting down {settings.project_name}...")