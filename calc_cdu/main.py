from fastapi import FastAPI
from common.exception_handlers import add_exception_handlers
from calc_cdu.app.routes import cdu_endpoints
from calc_cdu.app.config import settings
from common.logging import configure_logging
from common.middleware import TraceMiddleware

app = FastAPI(title="Calc‑CDU")
configure_logging()
app.add_middleware(TraceMiddleware)
add_exception_handlers(app)
app.include_router(cdu_endpoints.router)


@app.get("/health")
async def health():
    """
    Health check endpoint para comprobar si el Cado de Uso está en 
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